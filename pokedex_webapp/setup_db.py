import sqlite3
import os
from data import abilities_data
from data import pokemon_abilities_data
from data import pokemon_data
from data import type_effectiveness_data
from data import types_data

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
    
    # Insert Pokemon types relationships
    pokemon_types_data = [
        # Bulbasaur line
        (1, 5, 1), (1, 8, 0),    # Bulbasaur: Grass/Poison
        (2, 5, 1), (2, 8, 0),    # Ivysaur: Grass/Poison
        (3, 5, 1), (3, 8, 0),    # Venusaur: Grass/Poison
        
        # Charmander line
        (4, 2, 1),               # Charmander: Fire
        (5, 2, 1),               # Charmeleon: Fire
        (6, 2, 1), (6, 10, 0),   # Charizard: Fire/Flying
        
        # Squirtle line
        (7, 3, 1),               # Squirtle: Water
        (8, 3, 1),               # Wartortle: Water
        (9, 3, 1),               # Blastoise: Water
        
        # Caterpie line
        (10, 12, 1),             # Caterpie: Bug
        (11, 12, 1),             # Metapod: Bug
        (12, 12, 1), (12, 10, 0), # Butterfree: Bug/Flying
        
        # Weedle line
        (13, 12, 1), (13, 8, 0), # Weedle: Bug/Poison
        (14, 12, 1), (14, 8, 0), # Kakuna: Bug/Poison
        (15, 12, 1), (15, 8, 0), # Beedrill: Bug/Poison
        
        # Pidgey line
        (16, 1, 1), (16, 10, 0), # Pidgey: Normal/Flying
        (17, 1, 1), (17, 10, 0), # Pidgeotto: Normal/Flying
        (18, 1, 1), (18, 10, 0), # Pidgeot: Normal/Flying
        
        # Rattata line
        (19, 1, 1),              # Rattata: Normal
        (20, 1, 1),              # Raticate: Normal
        
        # Spearow line
        (21, 1, 1), (21, 10, 0), # Spearow: Normal/Flying
        (22, 1, 1), (22, 10, 0), # Fearow: Normal/Flying
        
        # Ekans line
        (23, 8, 1),              # Ekans: Poison
        (24, 8, 1),              # Arbok: Poison
        
        # Pikachu line
        (25, 4, 1),              # Pikachu: Electric
        (26, 4, 1),              # Raichu: Electric
        
        # Sandshrew line
        (27, 9, 1),              # Sandshrew: Ground
        (28, 9, 1),              # Sandslash: Ground
        
        # Nidoran♀ line
        (29, 8, 1),              # Nidoran♀: Poison
        (30, 8, 1),              # Nidorina: Poison
        (31, 8, 1), (31, 9, 0),  # Nidoqueen: Poison/Ground
        
        # Nidoran♂ line
        (32, 8, 1),              # Nidoran♂: Poison
        (33, 8, 1),              # Nidorino: Poison
        (34, 8, 1), (34, 9, 0),  # Nidoking: Poison/Ground
        
        # Clefairy line
        (35, 18, 1),             # Clefairy: Fairy
        (36, 18, 1),             # Clefable: Fairy
        
        # Vulpix line
        (37, 2, 1),              # Vulpix: Fire
        (38, 2, 1),              # Ninetales: Fire
        
        # Jigglypuff line
        (39, 1, 1), (39, 18, 0), # Jigglypuff: Normal/Fairy
        (40, 1, 1), (40, 18, 0), # Wigglytuff: Normal/Fairy
        
        # Zubat line
        (41, 8, 1), (41, 10, 0), # Zubat: Poison/Flying
        (42, 8, 1), (42, 10, 0), # Golbat: Poison/Flying
        
        # Oddish line
        (43, 5, 1), (43, 8, 0),  # Oddish: Grass/Poison
        (44, 5, 1), (44, 8, 0),  # Gloom: Grass/Poison
        (45, 5, 1), (45, 8, 0),  # Vileplume: Grass/Poison
        
        # Paras line
        (46, 12, 1), (46, 5, 0), # Paras: Bug/Grass
        (47, 12, 1), (47, 5, 0), # Parasect: Bug/Grass
        
        # Venonat line
        (48, 12, 1), (48, 8, 0), # Venonat: Bug/Poison
        (49, 12, 1), (49, 8, 0), # Venomoth: Bug/Poison
        
        # Diglett line
        (50, 9, 1),              # Diglett: Ground
        (51, 9, 1),              # Dugtrio: Ground
        
        # Meowth line
        (52, 1, 1),              # Meowth: Normal
        (53, 1, 1),              # Persian: Normal
        
        # Psyduck line
        (54, 3, 1),              # Psyduck: Water
        (55, 3, 1),              # Golduck: Water
        
        # Mankey line
        (56, 7, 1),              # Mankey: Fighting
        (57, 7, 1),              # Primeape: Fighting
        
        # Growlithe line
        (58, 2, 1),              # Growlithe: Fire
        (59, 2, 1),              # Arcanine: Fire
        
        # Poliwag line
        (60, 3, 1),              # Poliwag: Water
        (61, 3, 1),              # Poliwhirl: Water
        (62, 3, 1), (62, 7, 0),  # Poliwrath: Water/Fighting
        
        # Abra line
        (63, 11, 1),             # Abra: Psychic
        (64, 11, 1),             # Kadabra: Psychic
        (65, 11, 1),             # Alakazam: Psychic
        
        # Machop line
        (66, 7, 1),              # Machop: Fighting
        (67, 7, 1),              # Machoke: Fighting
        (68, 7, 1),              # Machamp: Fighting
        
        # Bellsprout line
        (69, 5, 1), (69, 8, 0),  # Bellsprout: Grass/Poison
        (70, 5, 1), (70, 8, 0),  # Weepinbell: Grass/Poison
        (71, 5, 1), (71, 8, 0),  # Victreebel: Grass/Poison
        
        # Tentacool line
        (72, 3, 1), (72, 8, 0),  # Tentacool: Water/Poison
        (73, 3, 1), (73, 8, 0),  # Tentacruel: Water/Poison
        
        # Geodude line
        (74, 13, 1), (74, 9, 0), # Geodude: Rock/Ground
        (75, 13, 1), (75, 9, 0), # Graveler: Rock/Ground
        (76, 13, 1), (76, 9, 0), # Golem: Rock/Ground
        
        # Ponyta line
        (77, 2, 1),              # Ponyta: Fire
        (78, 2, 1),              # Rapidash: Fire
        
        # Slowpoke line
        (79, 3, 1), (79, 11, 0), # Slowpoke: Water/Psychic
        (80, 3, 1), (80, 11, 0), # Slowbro: Water/Psychic
        
        # Magnemite line
        (81, 4, 1), (81, 17, 0), # Magnemite: Electric/Steel
        (82, 4, 1), (82, 17, 0), # Magneton: Electric/Steel
        
        # Farfetch'd
        (83, 1, 1), (83, 10, 0), # Farfetch'd: Normal/Flying
        
        # Doduo line
        (84, 1, 1), (84, 10, 0), # Doduo: Normal/Flying
        (85, 1, 1), (85, 10, 0), # Dodrio: Normal/Flying
        
        # Seel line
        (86, 3, 1),              # Seel: Water
        (87, 3, 1), (87, 6, 0),  # Dewgong: Water/Ice
        
        # Grimer line
        (88, 8, 1),              # Grimer: Poison
        (89, 8, 1),              # Muk: Poison
        
        # Shellder line
        (90, 3, 1),              # Shellder: Water
        (91, 3, 1), (91, 6, 0),  # Cloyster: Water/Ice
        
        # Gastly line
        (92, 14, 1), (92, 8, 0), # Gastly: Ghost/Poison
        (93, 14, 1), (93, 8, 0), # Haunter: Ghost/Poison
        (94, 14, 1), (94, 8, 0), # Gengar: Ghost/Poison
        
        # Onix
        (95, 13, 1), (95, 9, 0), # Onix: Rock/Ground
        
        # Drowzee line
        (96, 11, 1),             # Drowzee: Psychic
        (97, 11, 1),             # Hypno: Psychic
        
        # Krabby line
        (98, 3, 1),              # Krabby: Water
        (99, 3, 1),              # Kingler: Water
        
        # Voltorb line
        (100, 4, 1),             # Voltorb: Electric
        (101, 4, 1),             # Electrode: Electric
        
        # Exeggcute line
        (102, 5, 1), (102, 11, 0), # Exeggcute: Grass/Psychic
        (103, 5, 1), (103, 11, 0), # Exeggutor: Grass/Psychic
        
        # Cubone line
        (104, 9, 1),             # Cubone: Ground
        (105, 9, 1),             # Marowak: Ground
        
        # Hitmonlee
        (106, 7, 1),             # Hitmonlee: Fighting
        
        # Hitmonchan
        (107, 7, 1),             # Hitmonchan: Fighting
        
        # Lickitung
        (108, 1, 1),             # Lickitung: Normal
        
        # Koffing line
        (109, 8, 1),             # Koffing: Poison
        (110, 8, 1),             # Weezing: Poison
        
        # Rhyhorn line
        (111, 9, 1), (111, 13, 0), # Rhyhorn: Ground/Rock
        (112, 9, 1), (112, 13, 0), # Rhydon: Ground/Rock
        
        # Chansey
        (113, 1, 1),             # Chansey: Normal
        
        # Tangela
        (114, 5, 1),             # Tangela: Grass
        
        # Kangaskhan
        (115, 1, 1),             # Kangaskhan: Normal
        
        # Horsea line
        (116, 3, 1),             # Horsea: Water
        (117, 3, 1),             # Seadra: Water
        
        # Goldeen line
        (118, 3, 1),             # Goldeen: Water
        (119, 3, 1),             # Seaking: Water
        
        # Staryu line
        (120, 3, 1),             # Staryu: Water
        (121, 3, 1), (121, 11, 0), # Starmie: Water/Psychic
        
        # Mr. Mime
        (122, 11, 1), (122, 18, 0), # Mr. Mime: Psychic/Fairy
        
        # Scyther
        (123, 12, 1), (123, 10, 0), # Scyther: Bug/Flying
        
        # Jynx
        (124, 6, 1), (124, 11, 0), # Jynx: Ice/Psychic
        
        # Electabuzz
        (125, 4, 1),             # Electabuzz: Electric
        
        # Magmar
        (126, 2, 1),             # Magmar: Fire
        
        # Pinsir
        (127, 12, 1),            # Pinsir: Bug
        
        # Tauros
        (128, 1, 1),             # Tauros: Normal
        
        # Magikarp line
        (129, 3, 1),             # Magikarp: Water
        (130, 3, 1), (130, 10, 0), # Gyarados: Water/Flying
        
        # Lapras
        (131, 3, 1), (131, 6, 0), # Lapras: Water/Ice
        
        # Ditto
        (132, 1, 1),             # Ditto: Normal
        
        # Eevee evolutions
        (133, 1, 1),             # Eevee: Normal
        (134, 3, 1),             # Vaporeon: Water
        (135, 4, 1),             # Jolteon: Electric
        (136, 2, 1),             # Flareon: Fire
        
        # Porygon
        (137, 1, 1),             # Porygon: Normal
        
        # Omanyte line
        (138, 13, 1), (138, 3, 0), # Omanyte: Rock/Water
        (139, 13, 1), (139, 3, 0), # Omastar: Rock/Water
        
        # Kabuto line
        (140, 13, 1), (140, 3, 0), # Kabuto: Rock/Water
        (141, 13, 1), (141, 3, 0), # Kabutops: Rock/Water
        
        # Aerodactyl
        (142, 13, 1), (142, 10, 0), # Aerodactyl: Rock/Flying
        
        # Snorlax
        (143, 1, 1),             # Snorlax: Normal
        
        # Legendary birds
        (144, 6, 1), (144, 10, 0), # Articuno: Ice/Flying
        (145, 4, 1), (145, 10, 0), # Zapdos: Electric/Flying
        (146, 2, 1), (146, 10, 0), # Moltres: Fire/Flying
        
        # Dratini line
        (147, 15, 1),            # Dratini: Dragon
        (148, 15, 1),            # Dragonair: Dragon
        (149, 15, 1), (149, 10, 0), # Dragonite: Dragon/Flying
        
        # Mewtwo
        (150, 11, 1),            # Mewtwo: Psychic
        
        # Mew
        (151, 11, 1),            # Mew: Psychic
    ]

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