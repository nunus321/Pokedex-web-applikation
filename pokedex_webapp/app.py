from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3
import re

from database import init_db, db_connection

init_db()

app = Flask(__name__)
app.secret_key = "1234"


@app.route("/")
def index():
    return redirect(url_for("pokedex"))


@app.route("/pokedex")
def pokedex():
    conn = db_connection()

    # get all pokemon with their types
    pokemon_query = """
        SELECT 
            p.id, 
            p.pokedex_number, 
            p.name, 
            p.form, 
            p.legendary,
            GROUP_CONCAT(t.name || ':' || t.color || ':' || pt.is_first_type, '|') AS types
        FROM 
            pokemon p
        LEFT JOIN 
            pokemon_types pt ON p.id = pt.pokemon_id
        LEFT JOIN 
            types t ON pt.type_id = t.id
        GROUP BY 
            p.id
        ORDER BY 
            p.pokedex_number
        """

    pokemon_rows = conn.execute(pokemon_query).fetchall()

    conn.close()

    # unpack type data
    def unpack_type_data(pokemon_data):
        type_data = []

        for type_info in pokemon_data["types"].split("|"):
            type_name, color, is_first = type_info.split(":")
            type_data.append(
                {"name": type_name, "color": color, "is_first": bool(int(is_first))}
            )

        # return sorted types, with first type as first
        return sorted(type_data, key=lambda x: not x["is_first"])

    pokemon_list = []
    for pokemon_data in map(dict, pokemon_rows):
        pokemon_data["type_list"] = (
            unpack_type_data(pokemon_data) if pokemon_data["types"] else []
        )
        pokemon_list.append(pokemon_data)

    return render_template("pokedex.html", pokemon_list=pokemon_list)


@app.route("/pokemon/<int:pokedex_number>")
def pokemon_detail(pokedex_number):
    conn = db_connection()

    # get pokemon details
    pokemon_query = """
        SELECT
            p.*, r.name as region_name
        FROM
            pokemon p
        LEFT JOIN
            regions r ON p.region_id = r.id
        WHERE
            p.pokedex_number = ?
    """

    pokemon = conn.execute(pokemon_query, (pokedex_number,)).fetchone()

    if not pokemon:
        flash("Pokemon not found!")
        return redirect(url_for("pokedex"))

    # get pokemon types
    types_query = """
        SELECT
            t.name, t.color, pt.is_first_type
        FROM
            pokemon_types pt
        JOIN
            types t ON pt.type_id = t.id
        WHERE
            pt.pokemon_id = ?
        ORDER BY
            pt.is_first_type DESC
    """

    types = conn.execute(types_query, (pokemon["id"],)).fetchall()

    # get pokemon abilities
    abilities_query = """
        SELECT
            a.name, a.description, pa.is_hidden
        FROM
            pokemon_abilities pa
        JOIN
            abilities a ON pa.ability_id = a.id
        WHERE
            pa.pokemon_id = ?
        ORDER BY
            pa.is_hidden
    """

    abilities = conn.execute(abilities_query, (pokemon["id"],)).fetchall()

    # get type effectiveness (weaknesses and strengths)
    type_ids_query = """
        SELECT
            id
        FROM
            types t
        JOIN
            pokemon_types pt ON t.id = pt.type_id
        WHERE
            pt.pokemon_id = ?
    """

    type_ids = [
        t["id"]
        for t in conn.execute(
            type_ids_query,
            (pokemon["id"],),
        ).fetchall()
    ]

    # calculate weaknesses (types that are super effective against this Pokemon)
    weaknesses = []
    if type_ids:
        weakness_query = """
            SELECT DISTINCT
                t.name, t.color, te.multiplier
            FROM
                type_effectiveness te
            JOIN
                types t ON te.attacking_type_id = t.id
            WHERE
                te.defending_type_id IN ({}) AND te.multiplier > 1.0
        """.format(
            ",".join("?" * len(type_ids))
        )
        weaknesses = conn.execute(weakness_query, type_ids).fetchall()

    # calculate strengths (types this Pokemon resists)
    strengths = []
    if type_ids:
        strength_query = """
            SELECT DISTINCT
                t.name, t.color, te.multiplier
            FROM
                type_effectiveness te
            JOIN
                types t ON te.attacking_type_id = t.id
            WHERE
                te.defending_type_id IN ({}) AND te.multiplier < 1.0
        """.format(
            ",".join("?" * len(type_ids))
        )
        strengths = conn.execute(strength_query, type_ids).fetchall()

    conn.close()

    return render_template(
        "pokemon_detail.html",
        pokemon=pokemon,
        types=types,
        abilities=abilities,
        weaknesses=weaknesses,
        strengths=strengths,
    )


def add_pokemon_post():
    name = request.form["name"]

    if not re.fullmatch(r"[A-Za-zÀ-ÿ\-\s]+", name):
        flash("Invalid Pokémon name. Only letters, spaces and hyphens allowed.")
        return redirect(url_for("add_pokemon"))

    # fmt: off

    pokedex_number          = request.form["pokedex_number"]
    form                    = request.form.get("form")
    legendary               = "legendary" in request.form
    description             = x        if (x := request.form.get("description")) else None
    habitat                 = x        if (x := request.form.get("habitat")) else None
    height                  = float(x) if (x := request.form.get("height")) else None
    weight                  = float(x) if (x := request.form.get("weight")) else None
    region_id               = int(x)   if (x := request.form.get("region_id")) else None
    base_hp                 = int(x)   if (x := request.form.get("base_hp")) else None
    base_attack             = int(x)   if (x := request.form.get("base_attack")) else None
    base_defense            = int(x)   if (x := request.form.get("base_defense")) else None
    base_special_attack     = int(x)   if (x := request.form.get("base_special_attack")) else None
    base_special_defense    = int(x)   if (x := request.form.get("base_special_defense")) else None
    base_speed              = int(x)   if (x := request.form.get("base_speed")) else None

    # fmt: on

    conn = db_connection()
    try:
        cursor = conn.execute(
            """
            INSERT INTO
                pokemon (
                    pokedex_number,
                    name,
                    form,
                    average_height,
                    average_weight,
                    legendary,
                    region_id,
                    base_hp,
                    base_attack,
                    base_defense,
                    base_special_attack,
                    base_special_defense,
                    base_speed,
                    description,
                    habitat)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                pokedex_number,
                name,
                form,
                height,
                weight,
                legendary,
                region_id,
                base_hp,
                base_attack,
                base_defense,
                base_special_attack,
                base_special_defense,
                base_speed,
                description,
                habitat,
            ),
        )

        pokemon_id = cursor.lastrowid

        # add types
        type1 = request.form.get("type1")
        type2 = request.form.get("type2")

        if type1:
            conn.execute(
                "INSERT INTO pokemon_types (pokemon_id, type_id, is_first_type) VALUES (?, ?, ?)",
                (pokemon_id, type1, True),
            )
        if type2 and type2 != type1:
            conn.execute(
                "INSERT INTO pokemon_types (pokemon_id, type_id, is_first_type) VALUES (?, ?, ?)",
                (pokemon_id, type2, False),
            )

        # add abilities
        ability1 = request.form.get("ability1")
        ability2 = request.form.get("ability2")
        hidden_ability = request.form.get("hidden_ability")

        if ability1:
            conn.execute(
                "INSERT INTO pokemon_abilities (pokemon_id, ability_id, is_hidden) VALUES (?, ?, ?)",
                (pokemon_id, ability1, False),
            )
        if ability2 and ability2 != ability1:
            conn.execute(
                "INSERT INTO pokemon_abilities (pokemon_id, ability_id, is_hidden) VALUES (?, ?, ?)",
                (pokemon_id, ability2, False),
            )
        if hidden_ability and hidden_ability not in (ability1, ability2):
            conn.execute(
                "INSERT INTO pokemon_abilities (pokemon_id, ability_id, is_hidden) VALUES (?, ?, ?)",
                (pokemon_id, hidden_ability, True),
            )

        conn.commit()

        flash(f"{name} has been added to the Pokedex!")

        return redirect(url_for("pokedex"))

    except sqlite3.IntegrityError:
        flash("Pokemon with this Pokedex number already exists!")
    finally:
        conn.close()


@app.route("/add_pokemon", methods=["GET", "POST"])
def add_pokemon():
    if request.method == "POST":
        add_pokemon_post()

    # Get regions, types, and abilities for form
    conn = db_connection()
    regions = conn.execute("SELECT * FROM regions ORDER BY name").fetchall()
    types = conn.execute("SELECT * FROM types ORDER BY name").fetchall()
    abilities = conn.execute("SELECT * FROM abilities ORDER BY name").fetchall()
    conn.close()

    return render_template(
        "add_pokemon.html", regions=regions, types=types, abilities=abilities
    )


@app.route("/delete_pokemon/<int:pokedex_number>", methods=["POST"])
def delete_pokemon(pokedex_number):
    conn = db_connection()

    # first get the pokemon to check if it exists
    pokemon = conn.execute(
        "SELECT * FROM pokemon WHERE pokedex_number = ?", (pokedex_number,)
    ).fetchone()

    if not pokemon:
        flash("Pokemon not found!")
        conn.close()
        return redirect(url_for("pokedex"))

    try:
        pokemon_id = pokemon["id"]

        # delete related records first (foreign key constraints)
        conn.execute("DELETE FROM pokemon_types WHERE pokemon_id = ?", (pokemon_id,))
        conn.execute("DELETE FROM pokemon_abilities WHERE pokemon_id = ?", (pokemon_id,))

        # delete the pokemon
        conn.execute("DELETE FROM pokemon WHERE id = ?", (pokemon_id,))

        conn.commit()
        flash(f'{pokemon["name"]} has been deleted from the Pokedex!')
    except Exception as e:
        conn.rollback()
        flash(f"Error deleting Pokemon: {str(e)}")
    finally:
        conn.close()

    return redirect(url_for("pokedex"))


if __name__ == "__main__":
    app.run(debug=True)
