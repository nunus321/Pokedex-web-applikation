import sqlite3
import os
from data import abilities_data
from data import pokemon_abilities_data
from data import pokemon_data
from data import type_effectiveness_data
from data import types_data
from data import pokemon_types_data

DATABASE = 'pokedex.db'

def setup_database():
    # Remove existing database to start fresh
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    
    # Create tables
    conn.execute('''
        CREATE TABLE regions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')
    
    conn.execute('''
        CREATE TABLE types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            color TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE pokemon (
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
    ''')
    
    conn.execute('''
        CREATE TABLE pokemon_types (
            pokemon_id INTEGER,
            type_id INTEGER,
            is_first_type BOOLEAN DEFAULT TRUE,
            PRIMARY KEY (pokemon_id, type_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
            FOREIGN KEY (type_id) REFERENCES types (id)
        )
    ''')
    
    # Type effectiveness table
    conn.execute('''
        CREATE TABLE type_effectiveness (
            attacking_type_id INTEGER,
            defending_type_id INTEGER,
            multiplier REAL,
            PRIMARY KEY (attacking_type_id, defending_type_id),
            FOREIGN KEY (attacking_type_id) REFERENCES types (id),
            FOREIGN KEY (defending_type_id) REFERENCES types (id)
        )
    ''')
    
    # Pokemon abilities
    conn.execute('''
        CREATE TABLE abilities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            description TEXT
        )
    ''')
    
    conn.execute('''
        CREATE TABLE pokemon_abilities (
            pokemon_id INTEGER,
            ability_id INTEGER,
            is_hidden BOOLEAN DEFAULT FALSE,
            PRIMARY KEY (pokemon_id, ability_id),
            FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
            FOREIGN KEY (ability_id) REFERENCES abilities (id)
        )
    ''')
    
    # Insert regions
    regions = [
        ('Kanto',), ('Johto',), ('Hoenn',), ('Sinnoh',), 
        ('Unova',), ('Kalos',), ('Alola',), ('Galar',)
    ]
    conn.executemany('INSERT INTO regions (name) VALUES (?)', regions)

    conn.executemany('INSERT INTO types (name, color) VALUES (?, ?)', types_data)
    

    conn.executemany('INSERT INTO abilities (name, description) VALUES (?, ?)', abilities_data)
    
    conn.executemany(
    '''
    INSERT OR IGNORE INTO type_effectiveness
        (attacking_type_id, defending_type_id, multiplier)
    VALUES (?, ?, ?)
    ''',
    type_effectiveness_data
)
    conn.executemany(
    '''
    INSERT OR IGNORE INTO type_effectiveness
        (attacking_type_id, defending_type_id, multiplier)
    VALUES (?, ?, ?)
    ''',
    type_effectiveness_data
)

    conn.executemany('''INSERT INTO pokemon 
                       (pokedex_number, name, form, average_height, average_weight, legendary, region_id,
                        base_hp, base_attack, base_defense, base_special_attack, base_special_defense, base_speed,
                        description, habitat) 
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', pokemon_data)
    
    conn.executemany('''INSERT INTO pokemon_types 
                       (pokemon_id, type_id, is_first_type) 
                       VALUES (?, ?, ?)''', pokemon_types_data)
    
    
    conn.executemany('''INSERT INTO pokemon_abilities 
                       (pokemon_id, ability_id, is_hidden) 
                       VALUES (?, ?, ?)''', pokemon_abilities_data)
    
    conn.commit()
    conn.close()
    print("Enhanced database setup complete! Added 3 Pokemon with full stats and type effectiveness.")

if __name__ == '__main__':
    setup_database()
