import sqlite3

import data

DATABASE = "pokedex.db"


def db_connection():
    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    conn = db_connection()

    # Entities:

    # pokemon(id : int,
    #         pokedex_number : int,
    #         name : str,
    #         form : str,
    #         average_height : float,
    #         average_weight : float,
    #         legendary : bool,
    #         region_id : int,
    #         base_hp : int,
    #         base_attack : int,
    #         base_defense : int,
    #         base_special_attack : int
    #         base_special_defense : int
    #         base_speed : int
    #         description : str,
    #         habitat : str)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pokedex_number INTEGER NOT NULL UNIQUE,
            name TEXT NOT NULL,
            form TEXT,
            average_height REAL,
            average_weight REAL,
            legendary BOOLEAN DEFAULT FALSE,
            region_id INTEGER,
            base_hp INTEGER,
            base_attack INTEGER,
            base_defense INTEGER,
            base_special_attack INTEGER,
            base_special_defense INTEGER,
            base_speed INTEGER,
            description TEXT,
            habitat TEXT,
            FOREIGN KEY (region_id) REFERENCES regions (id)
        )
        """
    )

    # types(id : int, name : str, color : str)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT
        )
        """
    )

    # abilities(id : int, name : str, description : str)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS abilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
        """
    )

    # regions(id : int, name : str)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
        """
    )

    # Relations:

    # pokemon_types(pokemon_id : int, type_id : int, is_first_type : bool)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon_types (
            pokemon_id INTEGER,
            type_id INTEGER,
            is_first_type BOOLEAN DEFAULT TRUE,
            PRIMARY KEY (pokemon_id, type_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
            FOREIGN KEY (type_id) REFERENCES types (id)
        )
        """
    )

    # type_effectiveness(attacking_type_id : int,
    #                    defending_type_id : int,
    #                    multiplier : float)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS type_effectiveness (
            attacking_type_id INTEGER,
            defending_type_id INTEGER,
            multiplier REAL,
            PRIMARY KEY (attacking_type_id, defending_type_id),
            FOREIGN KEY (attacking_type_id) REFERENCES types (id),
            FOREIGN KEY (defending_type_id) REFERENCES types (id)
        )
        """
    )

    # pokemon_abilities(pokemon_id : int,
    #                   ability_id : int,
    #                   is_hidden : bool)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS pokemon_abilities (
            pokemon_id INTEGER,
            ability_id INTEGER,
            is_hidden BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (pokemon_id, ability_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
            FOREIGN KEY (ability_id) REFERENCES abilities (id)
        )
        """
    )

    insert_sample_data(conn)

    conn.commit()
    conn.close()


def insert_sample_data(conn):
    conn.executemany(
        """
        INSERT OR IGNORE INTO regions
            (name)
        VALUES (?)
        """,
        data.regions,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO types
            (name, color)
        VALUES (?, ?)
        """,
        data.types_data,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO abilities
            (name, description)
        VALUES (?, ?)
        """,
        data.abilities_data,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO type_effectiveness
            (attacking_type_id, defending_type_id, multiplier)
        VALUES (?, ?, ?)
        """,
        data.type_effectiveness_data,
    )
    conn.executemany(
        """
        INSERT OR IGNORE INTO type_effectiveness
            (attacking_type_id, defending_type_id, multiplier)
        VALUES (?, ?, ?)
        """,
        data.type_effectiveness_data,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO pokemon 
            (pokedex_number,
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
        data.pokemon_data,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO pokemon_types 
            (pokemon_id, type_id, is_first_type) 
        VALUES (?, ?, ?)
        """,
        data.pokemon_types_data,
    )

    conn.executemany(
        """
        INSERT OR IGNORE INTO pokemon_abilities 
            (pokemon_id, ability_id, is_hidden) 
        VALUES (?, ?, ?)
        """,
        data.pokemon_abilities_data,
    )


if __name__ == "__main__":
    init_db()
