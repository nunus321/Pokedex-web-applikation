import sqlite3

from data import regions
from data import abilities_data
from data import pokemon_abilities_data
from data import pokemon_data
from data import type_effectiveness_data
from data import types_data
from data import pokemon_types_data

DATABASE = "pokedex.db"


def db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db_connection()

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """
    )

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT
        )
    """
    )

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

    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS abilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    """
    )

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

    # Insert sample data
    insert_sample_data(conn)
    conn.commit()
    conn.close()


def insert_sample_data(conn):
    conn.executemany("INSERT OR IGNORE INTO regions (name) VALUES (?)", regions)

    conn.executemany(
        "INSERT OR IGNORE INTO types (name, color) VALUES (?, ?)", types_data
    )

    conn.executemany(
        "INSERT OR IGNORE INTO abilities (name, description) VALUES (?, ?)",
        abilities_data,
    )

    conn.executemany(
        """
    INSERT OR IGNORE INTO type_effectiveness
        (attacking_type_id, defending_type_id, multiplier)
    VALUES (?, ?, ?)
    """,
        type_effectiveness_data,
    )
    conn.executemany(
        """
    INSERT OR IGNORE INTO type_effectiveness
        (attacking_type_id, defending_type_id, multiplier)
    VALUES (?, ?, ?)
    """,
        type_effectiveness_data,
    )

    conn.executemany(
        """INSERT OR IGNORE INTO pokemon 
                       (pokedex_number, name, form, average_height, average_weight, legendary, region_id,
                        base_hp, base_attack, base_defense, base_special_attack, base_special_defense, base_speed,
                        description, habitat) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        pokemon_data,
    )

    conn.executemany(
        """INSERT OR IGNORE INTO pokemon_types 
                       (pokemon_id, type_id, is_first_type) 
                       VALUES (?, ?, ?)""",
        pokemon_types_data,
    )

    conn.executemany(
        """INSERT OR IGNORE INTO pokemon_abilities 
                       (pokemon_id, ability_id, is_hidden) 
                       VALUES (?, ?, ?)""",
        pokemon_abilities_data,
    )


if __name__ == "__main__":
    init_db()
