
# Insert regions
regions = [
    ('Kanto',), ('Johto',), ('Hoenn',), ('Sinnoh',), ('Unova',), ('Kalos',), ('Alola',), ('Galar',)
]

# Insert abilities
abilities_data = [
    ('Overgrow', 'Powers up Grass-type moves in a pinch.'),
    ('Chlorophyll', 'Boosts Speed in sunshine.'),
    ('Blaze', 'Powers up Fire-type moves in a pinch.'),
    ('Solar Power', 'Raises Sp. Atk in sun; loses HP each turn.'),
    ('Torrent', 'Powers up Water-type moves in a pinch.'),
    ('Rain Dish', 'Gradually restores HP in rain.'),
    ('Shield Dust', 'Blocks added effects of attacks taken.'),
    ('Compound Eyes', 'Boosts accuracy.'),
    ('Tinted Lens', '“Not very effective” moves deal normal damage.'),
    ('Swarm', 'Powers up Bug-type moves in a pinch.'),
    ('Sniper', 'Critical hits inflict extra damage.'),
    ('Keen Eye', 'Prevents accuracy reduction.'),
    ('Tangled Feet', 'Raises evasion if confused.'),
    ('Big Pecks', 'Prevents Defense drops.'),
    ('Guts', 'Attack rises if the user has a status.'),
    ('Hustle', 'Boosts Attack but lowers accuracy.'),
    ('Intimidate', 'Lowers the foe’s Attack on entry.'),
    ('Unnerve', 'Foes cannot eat held Berries.'),
    ('Static', 'Contact may paralyze.'),
    ('Lightning Rod', 'Draws in Electric moves; raises Sp. Atk.'),
    ('Sand Veil', 'Raises evasion in sandstorm.'),
    ('Sand Rush', 'Doubles Speed in sandstorm.'),
    ('Sand Force', 'Boosts Rock/Ground/Steel moves in sandstorm.'),
    ('Poison Point', 'Contact may poison.'),
    ('Rivalry', 'Stronger against same-gender foes.'),
    ('Sheer Force', 'Trades added effects for stronger power.'),
    ('Cute Charm', 'Contact may infatuate.'),
    ('Magic Guard', 'Only damage from direct attacks is taken.'),
    ('Unaware', 'Ignores foe’s stat changes.'),
    ('Flash Fire', 'Fire immunity; powers up Fire moves when hit.'),
    ('Flame Body', 'Contact may burn.'),
    ('Run Away', 'Ensures escape from wild battles.'),
    ('Pickup', 'May pick up items after battle.'),
    ('Gluttony', 'Eats held Berry at ½ HP instead of ¼.'),
    ('Early Bird', 'Awakens from sleep twice as fast.'),
    ('Scrappy', 'Normal/Fighting moves hit Ghosts.'),
    ('Inner Focus', 'Prevents flinching.'),
    ('Synchronize', 'Passes burn/paralysis/poison back to the foe.'),
    ('Clear Body', 'Prevents stat reductions.'),
    ('Liquid Ooze', 'Draining moves damage the user instead.'),
    ('Stench', 'May cause flinch.'),
    ('Rock Head', 'Prevents recoil damage.'),
    ('Sturdy', 'Cannot be KO’d in one hit.'),
    ('Magnet Pull', 'Traps Steel-type foes.'),
    ('Levitate', 'Immune to Ground moves.'),
    ('Effect Spore', 'Contact may poison, sleep, or paralyze.'),
    ('Dry Skin', 'Heals in rain; hurt by sun & Fire.'),
    ('Damp', 'Prevents Self-Destruct & Explosion.'),
    ('Water Veil', 'Prevents burns.'),
    ('Stench (Alt)', 'Second instance of Stench kept unique.'),
    ('Sticky Hold', 'Items can’t be removed.'),
    ('Poison Touch', 'Contact moves may poison.'),
    ('Weak Armor', 'Contact lowers Defense, sharply raises Speed.'),
    ('Cursed Body', 'May disable the attacker’s move.'),
    ('Insomnia', 'Prevents sleep.'),
    ('Forewarn', 'Reveals a strong move the foe knows.'),
    ('Frisk', 'Reveals the foe’s held item.'),
    ('Thick Fat', 'Halves Fire & Ice damage.'),
    ('Hydration', 'Cures status in rain.'),
    ('Ice Body', 'Heals in hail.'),
    ('Shell Armor', 'Blocks critical hits.'),
    ('Skill Link', 'Multi-hit moves always strike 5 times.'),
    ('Overcoat', 'Immune to weather & powder moves.'),
    ('Infiltrator', 'Passes through barriers like Reflect.'),
    ('Arena Trap', 'Prevents foes fleeing or switching.'),
    ('Wonder Skin', 'Status moves used on this Pokémon have 50 % acc.'),
    ('Arena Trap (Alt)', 'Duplicate kept unique for FK consistency.'),
    ('Soundproof', 'Immune to sound-based moves.'),
    ('Friend Guard', 'Reduces damage done to allies.'),
    ('Magic Bounce', 'Reflects status moves back to the foe.'),
    ('Friend Guard (Alt)', 'Second Friend Guard kept unique.'),
    ('Competitive', 'Sharply raises Sp. Atk when a stat is lowered.'),
    ('Wonder Skin (Alt)', 'Second Wonder Skin kept unique.'),
    ('Technician', 'Boosts weaker moves.'),
    ('Limber', 'Prevents paralysis.'),
    ('Cloud Nine', 'Negates weather effects while in battle.'),
    ('Vital Spirit', 'Prevents sleep.'),
    ('Anger Point', 'Maxes Attack after a critical hit.'),
    ('Defiant', 'Raises Attack when stats are lowered.'),
    ('Justified', 'Dark-type hit raises Attack.'),
    ('No Guard', 'All moves (by or against) land.'),
    ('Analytic', 'Moves hit harder if the user acts last.'),
    ('Hyper Cutter', 'Prevents Attack reduction.'),
    ('Aftermath', 'Damages the foe if KO’d by contact.'),
    ('Harvest', 'May recycle a used Berry each turn.'),
    ('Battle Armor', 'Blocks critical hits.'),
    ('Reckless', 'Boosts recoil & crash moves.'),
    ('Unburden', 'Losing item doubles Speed.'),
    ('Iron Fist', 'Boosts punching moves.'),
    ('Natural Cure', 'Cures status on switching out.'),
    ('Serene Grace', 'Doubles the chance of added effects.'),
    ('Healer', 'May heal an ally’s status each turn.'),
    ('Leaf Guard', 'Prevents status in sunshine.'),
    ('Early Bird (Alt)', 'Second Early Bird kept unique.'),
    ('Illuminate', 'Lowers foe’s accuracy; raises wild encounter rate.'),
    ('Filter', 'Weakens super-effective moves.'),
    ('Steadfast', 'Flinching raises Speed.'),
    ('Mold Breaker', 'Moves ignore the foe’s abilities.'),
    ('Moxie', 'Attack rises after KOing a foe.'),
    ('Rattled', 'Bug/Ghost/Dark hit raises Speed.'),
    ('Immunity', 'Prevents poison.'),
    ('Adaptability', 'STAB bonus becomes 2×.'),
    ('Anticipation', 'Shudders at foe’s strong moves.'),
    ('Volt Absorb', 'Heals ¼ HP if hit by Electric move.'),
    ('Quick Feet', 'Status doubles Speed; ignores Speed drop from paralysis.'),
    ('Trace', 'Copies a foe’s ability on entry.'),
    ('Download', 'Raises Atk or Sp. Atk based on foe’s defenses.'),
    ('Pressure', 'Foes expend 2 PP instead of 1.'),
    ('Snow Cloak', 'Raises evasion in hail.'),
    ('Marvel Scale', 'Status boosts Defense.'),
    ('Multiscale', 'Halves damage at full HP.')
]

# Insert Pokemon abilities
pokemon_abilities_data = [
    # Bulbasaur line
    (1, 1, 0),   # Bulbasaur: Overgrow
    (1, 2, 1),   # Bulbasaur: Chlorophyll (hidden)
    (2, 1, 0),   # Ivysaur: Overgrow
    (2, 2, 1),   # Ivysaur: Chlorophyll (hidden)
    (3, 1, 0),   # Venusaur: Overgrow
    (3, 2, 1),   # Venusaur: Chlorophyll (hidden)
    
    # Charmander line
    (4, 3, 0),   # Charmander: Blaze
    (4, 4, 1),   # Charmander: Solar Power (hidden)
    (5, 3, 0),   # Charmeleon: Blaze
    (5, 4, 1),   # Charmeleon: Solar Power (hidden)
    (6, 3, 0),   # Charizard: Blaze
    (6, 4, 1),   # Charizard: Solar Power (hidden)
    
    # Squirtle line
    (7, 5, 0),   # Squirtle: Torrent
    (7, 6, 1),   # Squirtle: Rain Dish (hidden)
    (8, 5, 0),   # Wartortle: Torrent
    (8, 6, 1),   # Wartortle: Rain Dish (hidden)
    (9, 5, 0),   # Blastoise: Torrent
    (9, 6, 1),   # Blastoise: Rain Dish (hidden)
    
    # Caterpie line
    (10, 7, 0),  # Caterpie: Shield Dust
    (10, 32, 1), # Caterpie: Run Away (hidden)
    (11, 58, 0), # Metapod: Shed Skin
    (12, 8, 0),  # Butterfree: Compound Eyes
    (12, 9, 1),  # Butterfree: Tinted Lens (hidden)
    
    # Weedle line
    (13, 7, 0),  # Weedle: Shield Dust
    (13, 32, 1), # Weedle: Run Away (hidden)
    (14, 58, 0), # Kakuna: Shed Skin
    (15, 10, 0), # Beedrill: Swarm
    (15, 11, 1), # Beedrill: Sniper (hidden)
    
    # Pidgey line
    (16, 12, 0), # Pidgey: Keen Eye
    (16, 13, 0), # Pidgey: Tangled Feet
    (16, 14, 1), # Pidgey: Big Pecks (hidden)
    (17, 12, 0), # Pidgeotto: Keen Eye
    (17, 13, 0), # Pidgeotto: Tangled Feet
    (17, 14, 1), # Pidgeotto: Big Pecks (hidden)
    (18, 12, 0), # Pidgeot: Keen Eye
    (18, 13, 0), # Pidgeot: Tangled Feet
    (18, 14, 1), # Pidgeot: Big Pecks (hidden)
    
    # Rattata line
    (19, 32, 0), # Rattata: Run Away
    (19, 15, 0), # Rattata: Guts
    (19, 16, 1), # Rattata: Hustle (hidden)
    (20, 32, 0), # Raticate: Run Away
    (20, 15, 0), # Raticate: Guts
    (20, 16, 1), # Raticate: Hustle (hidden)
    
    # Spearow line
    (21, 12, 0), # Spearow: Keen Eye
    (21, 11, 1), # Spearow: Sniper (hidden)
    (22, 12, 0), # Fearow: Keen Eye
    (22, 11, 1), # Fearow: Sniper (hidden)
    
    # Ekans line
    (23, 17, 0), # Ekans: Intimidate
    (23, 58, 0), # Ekans: Shed Skin
    (23, 18, 1), # Ekans: Unnerve (hidden)
    (24, 17, 0), # Arbok: Intimidate
    (24, 58, 0), # Arbok: Shed Skin
    (24, 18, 1), # Arbok: Unnerve (hidden)
    
    # Pikachu line
    (25, 19, 0), # Pikachu: Static
    (25, 20, 1), # Pikachu: Lightning Rod (hidden)
    (26, 19, 0), # Raichu: Static
    (26, 20, 1), # Raichu: Lightning Rod (hidden)
    
    # Sandshrew line
    (27, 21, 0), # Sandshrew: Sand Veil
    (27, 22, 1), # Sandshrew: Sand Rush (hidden)
    (28, 21, 0), # Sandslash: Sand Veil
    (28, 22, 1), # Sandslash: Sand Rush (hidden)
    
    # Nidoran♀ line
    (29, 24, 0), # Nidoran♀: Poison Point
    (29, 25, 0), # Nidoran♀: Rivalry
    (29, 16, 1), # Nidoran♀: Hustle (hidden)
    (30, 24, 0), # Nidorina: Poison Point
    (30, 25, 0), # Nidorina: Rivalry
    (30, 16, 1), # Nidorina: Hustle (hidden)
    (31, 24, 0), # Nidoqueen: Poison Point
    (31, 25, 0), # Nidoqueen: Rivalry
    (31, 26, 1), # Nidoqueen: Sheer Force (hidden)
    
    # Nidoran♂ line
    (32, 24, 0), # Nidoran♂: Poison Point
    (32, 25, 0), # Nidoran♂: Rivalry
    (32, 16, 1), # Nidoran♂: Hustle (hidden)
    (33, 24, 0), # Nidorino: Poison Point
    (33, 25, 0), # Nidorino: Rivalry
    (33, 16, 1), # Nidorino: Hustle (hidden)
    (34, 24, 0), # Nidoking: Poison Point
    (34, 25, 0), # Nidoking: Rivalry
    (34, 26, 1), # Nidoking: Sheer Force (hidden)
    
    # Clefairy line
    (35, 27, 0), # Clefairy: Cute Charm
    (35, 28, 0), # Clefairy: Magic Guard
    (35, 71, 1), # Clefairy: Friend Guard (hidden)
    (36, 27, 0), # Clefable: Cute Charm
    (36, 28, 0), # Clefable: Magic Guard
    (36, 29, 1), # Clefable: Unaware (hidden)
    
    # Vulpix line
    (37, 30, 0), # Vulpix: Flash Fire
    (37, 63, 1), # Vulpix: Drought (hidden)
    (38, 30, 0), # Ninetales: Flash Fire
    (38, 63, 1), # Ninetales: Drought (hidden)
    
    # Jigglypuff line
    (39, 27, 0), # Jigglypuff: Cute Charm
    (39, 72, 0), # Jigglypuff: Competitive
    (39, 71, 1), # Jigglypuff: Friend Guard (hidden)
    (40, 27, 0), # Wigglytuff: Cute Charm
    (40, 72, 0), # Wigglytuff: Competitive
    (40, 71, 1), # Wigglytuff: Friend Guard (hidden)
    
    # Zubat line
    (41, 37, 0), # Zubat: Inner Focus
    (41, 49, 1), # Zubat: Infiltrator (hidden)
    (42, 37, 0), # Golbat: Inner Focus
    (42, 49, 1), # Golbat: Infiltrator (hidden)
    
    # Oddish line
    (43, 2, 0),  # Oddish: Chlorophyll
    (43, 32, 1), # Oddish: Run Away (hidden)
    (44, 2, 0),  # Gloom: Chlorophyll
    (44, 50, 1), # Gloom: Stench (hidden)
    (45, 2, 0),  # Vileplume: Chlorophyll
    (45, 46, 1), # Vileplume: Effect Spore (hidden)
    
    # Paras line
    (46, 46, 0), # Paras: Effect Spore
    (46, 47, 0), # Paras: Dry Skin
    (46, 48, 1), # Paras: Damp (hidden)
    (47, 46, 0), # Parasect: Effect Spore
    (47, 47, 0), # Parasect: Dry Skin
    (47, 48, 1), # Parasect: Damp (hidden)
    
    # Venonat line
    (48, 8, 0),  # Venonat: Compound Eyes
    (48, 9, 0),  # Venonat: Tinted Lens
    (48, 32, 1), # Venonat: Run Away (hidden)
    (49, 7, 0),  # Venomoth: Shield Dust
    (49, 9, 0),  # Venomoth: Tinted Lens
    (49, 73, 1), # Venomoth: Wonder Skin (hidden)
    
    # Diglett line
    (50, 21, 0), # Diglett: Sand Veil
    (50, 67, 0), # Diglett: Arena Trap
    (50, 23, 1), # Diglett: Sand Force (hidden)
    (51, 21, 0), # Dugtrio: Sand Veil
    (51, 67, 0), # Dugtrio: Arena Trap
    (51, 23, 1), # Dugtrio: Sand Force (hidden)
    
    # Meowth line
    (52, 33, 0), # Meowth: Pickup
    (52, 74, 0), # Meowth: Technician
    (52, 18, 1), # Meowth: Unnerve (hidden)
    (53, 75, 0), # Persian: Limber
    (53, 74, 0), # Persian: Technician
    (53, 18, 1), # Persian: Unnerve (hidden)
    
    # Psyduck line
    (54, 48, 0), # Psyduck: Damp
    (54, 76, 0), # Psyduck: Cloud Nine
    (54, 52, 1), # Psyduck: Swift Swim (hidden)
    (55, 48, 0), # Golduck: Damp
    (55, 76, 0), # Golduck: Cloud Nine
    (55, 52, 1), # Golduck: Swift Swim (hidden)
    
    # Mankey line
    (56, 77, 0), # Mankey: Vital Spirit
    (56, 78, 0), # Mankey: Anger Point
    (56, 79, 1), # Mankey: Defiant (hidden)
    (57, 77, 0), # Primeape: Vital Spirit
    (57, 78, 0), # Primeape: Anger Point
    (57, 79, 1), # Primeape: Defiant (hidden)
    
    # Growlithe line
    (58, 17, 0), # Growlithe: Intimidate
    (58, 30, 0), # Growlithe: Flash Fire
    (58, 80, 1), # Growlithe: Justified (hidden)
    (59, 17, 0), # Arcanine: Intimidate
    (59, 30, 0), # Arcanine: Flash Fire
    (59, 80, 1), # Arcanine: Justified (hidden)
    
    # Poliwag line
    (60, 49, 0), # Poliwag: Water Absorb
    (60, 48, 0), # Poliwag: Damp
    (60, 52, 1), # Poliwag: Swift Swim (hidden)
    (61, 49, 0), # Poliwhirl: Water Absorb
    (61, 48, 0), # Poliwhirl: Damp
    (61, 52, 1), # Poliwhirl: Swift Swim (hidden)
    (62, 49, 0), # Poliwrath: Water Absorb
    (62, 48, 0), # Poliwrath: Damp
    (62, 52, 1), # Poliwrath: Swift Swim (hidden)
    
    # Abra line
    (63, 38, 0), # Abra: Synchronize
    (63, 37, 0), # Abra: Inner Focus
    (63, 28, 1), # Abra: Magic Guard (hidden)
    (64, 38, 0), # Kadabra: Synchronize
    (64, 37, 0), # Kadabra: Inner Focus
    (64, 28, 1), # Kadabra: Magic Guard (hidden)
    (65, 38, 0), # Alakazam: Synchronize
    (65, 37, 0), # Alakazam: Inner Focus
    (65, 28, 1), # Alakazam: Magic Guard (hidden)
    
    # Machop line
    (66, 15, 0), # Machop: Guts
    (66, 81, 0), # Machop: No Guard
    (66, 37, 1), # Machop: Steadfast (hidden)
    (67, 15, 0), # Machoke: Guts
    (67, 81, 0), # Machoke: No Guard
    (67, 37, 1), # Machoke: Steadfast (hidden)
    (68, 15, 0), # Machamp: Guts
    (68, 81, 0), # Machamp: No Guard
    (68, 37, 1), # Machamp: Steadfast (hidden)
    
    # Bellsprout line
    (69, 2, 0),  # Bellsprout: Chlorophyll
    (69, 34, 1), # Bellsprout: Gluttony (hidden)
    (70, 2, 0),  # Weepinbell: Chlorophyll
    (70, 34, 1), # Weepinbell: Gluttony (hidden)
    (71, 2, 0),  # Victreebel: Chlorophyll
    (71, 34, 1), # Victreebel: Gluttony (hidden)
    
    # Tentacool line
    (72, 39, 0), # Tentacool: Clear Body
    (72, 40, 0), # Tentacool: Liquid Ooze
    (72, 6, 1),  # Tentacool: Rain Dish (hidden)
    (73, 39, 0), # Tentacruel: Clear Body
    (73, 40, 0), # Tentacruel: Liquid Ooze
    (73, 6, 1),  # Tentacruel: Rain Dish (hidden)
    
    # Geodude line
    (74, 42, 0), # Geodude: Rock Head
    (74, 43, 0), # Geodude: Sturdy
    (74, 21, 1), # Geodude: Sand Veil (hidden)
    (75, 42, 0), # Graveler: Rock Head
    (75, 43, 0), # Graveler: Sturdy
    (75, 21, 1), # Graveler: Sand Veil (hidden)
    (76, 42, 0), # Golem: Rock Head
    (76, 43, 0), # Golem: Sturdy
    (76, 21, 1), # Golem: Sand Veil (hidden)
    
    # Ponyta line
    (77, 32, 0), # Ponyta: Run Away
    (77, 30, 0), # Ponyta: Flash Fire
    (77, 31, 1), # Ponyta: Flame Body (hidden)
    (78, 32, 0), # Rapidash: Run Away
    (78, 30, 0), # Rapidash: Flash Fire
    (78, 31, 1), # Rapidash: Flame Body (hidden)
    
    # Slowpoke line
    (79, 54, 0), # Slowpoke: Oblivious
    (79, 55, 0), # Slowpoke: Own Tempo
    (79, 56, 1), # Slowpoke: Regenerator (hidden)
    (80, 54, 0), # Slowbro: Oblivious
    (80, 55, 0), # Slowbro: Own Tempo
    (80, 56, 1), # Slowbro: Regenerator (hidden)
    
    # Magnemite line
    (81, 44, 0), # Magnemite: Magnet Pull
    (81, 43, 0), # Magnemite: Sturdy
    (81, 82, 1), # Magnemite: Analytic (hidden)
    (82, 44, 0), # Magneton: Magnet Pull
    (82, 43, 0), # Magneton: Sturdy
    (82, 82, 1), # Magneton: Analytic (hidden)
    
    # Farfetch'd
    (83, 12, 0), # Farfetch'd: Keen Eye
    (83, 37, 0), # Farfetch'd: Inner Focus
    (83, 79, 1), # Farfetch'd: Defiant (hidden)
    
    # Doduo line
    (84, 32, 0), # Doduo: Run Away
    (84, 35, 0), # Doduo: Early Bird
    (84, 13, 1), # Doduo: Tangled Feet (hidden)
    (85, 32, 0), # Dodrio: Run Away
    (85, 35, 0), # Dodrio: Early Bird
    (85, 13, 1), # Dodrio: Tangled Feet (hidden)
    
    # Seel line
    (86, 83, 0), # Seel: Thick Fat
    (86, 84, 0), # Seel: Hydration
    (86, 85, 1), # Seel: Ice Body (hidden)
    (87, 83, 0), # Dewgong: Thick Fat
    (87, 84, 0), # Dewgong: Hydration
    (87, 85, 1), # Dewgong: Ice Body (hidden)
    
    # Grimer line
    (88, 41, 0), # Grimer: Stench
    (88, 51, 0), # Grimer: Sticky Hold
    (88, 86, 1), # Grimer: Poison Touch (hidden)
    (89, 41, 0), # Muk: Stench
    (89, 51, 0), # Muk: Sticky Hold
    (89, 86, 1), # Muk: Poison Touch (hidden)
    
    # Shellder line
    (90, 61, 0), # Shellder: Shell Armor
    (90, 57, 0), # Shellder: Skill Link
    (90, 87, 1), # Shellder: Overcoat (hidden)
    (91, 61, 0), # Cloyster: Shell Armor
    (91, 57, 0), # Cloyster: Skill Link
    (91, 87, 1), # Cloyster: Overcoat (hidden)
    
    # Gastly line
    (92, 43, 0), # Gastly: Levitate
    (93, 45, 0), # Haunter: Levitate
    (94, 88, 0), # Gengar: Cursed Body
    
    # Onix
    (95, 42, 0), # Onix: Rock Head
    (95, 43, 0), # Onix: Sturdy
    (95, 89, 1), # Onix: Weak Armor (hidden)
    
    # Drowzee line
    (96, 47, 0), # Drowzee: Insomnia
    (96, 48, 0), # Drowzee: Forewarn
    (96, 37, 1), # Drowzee: Inner Focus (hidden)
    (97, 47, 0), # Hypno: Insomnia
    (97, 48, 0), # Hypno: Forewarn
    (97, 37, 1), # Hypno: Inner Focus (hidden)
    
    # Krabby line
    (98, 90, 0), # Krabby: Hyper Cutter
    (98, 61, 0), # Krabby: Shell Armor
    (98, 26, 1), # Krabby: Sheer Force (hidden)
    (99, 90, 0), # Kingler: Hyper Cutter
    (99, 61, 0), # Kingler: Shell Armor
    (99, 26, 1), # Kingler: Sheer Force (hidden)
    
    # Voltorb line
    (100, 91, 0), # Voltorb: Soundproof
    (100, 19, 0), # Voltorb: Static
    (100, 92, 1), # Voltorb: Aftermath (hidden)
    (101, 91, 0), # Electrode: Soundproof
    (101, 19, 0), # Electrode: Static
    (101, 92, 1), # Electrode: Aftermath (hidden)
    
    # Exeggcute line
    (102, 2, 0), # Exeggcute: Chlorophyll
    (102, 93, 1), # Exeggcute: Harvest (hidden)
    (103, 2, 0), # Exeggutor: Chlorophyll
    (103, 93, 1), # Exeggutor: Harvest (hidden)
    
    # Cubone line
    (104, 42, 0), # Cubone: Rock Head
    (104, 20, 0), # Cubone: Lightning Rod
    (104, 94, 1), # Cubone: Battle Armor (hidden)
    (105, 42, 0), # Marowak: Rock Head
    (105, 20, 0), # Marowak: Lightning Rod
    (105, 94, 1), # Marowak: Battle Armor (hidden)
    
    # Hitmonlee
    (106, 75, 0), # Hitmonlee: Limber
    (106, 95, 0), # Hitmonlee: Reckless
    (106, 96, 1), # Hitmonlee: Unburden (hidden)
    
    # Hitmonchan
    (107, 12, 0), # Hitmonchan: Keen Eye
    (107, 97, 0), # Hitmonchan: Iron Fist
    (107, 37, 1), # Hitmonchan: Inner Focus (hidden)
    
    # Lickitung
    (108, 55, 0), # Lickitung: Own Tempo
    (108, 54, 0), # Lickitung: Oblivious
    (108, 76, 1), # Lickitung: Cloud Nine (hidden)
    
    # Koffing line
    (109, 43, 0), # Koffing: Levitate
    (110, 43, 0), # Weezing: Levitate
    
    # Rhyhorn line
    (111, 20, 0), # Rhyhorn: Lightning Rod
    (111, 42, 0), # Rhyhorn: Rock Head
    (111, 95, 1), # Rhyhorn: Reckless (hidden)
    (112, 20, 0), # Rhydon: Lightning Rod
    (112, 42, 0), # Rhydon: Rock Head
    (112, 95, 1), # Rhydon: Reckless (hidden)
    
    # Chansey
    (113, 98, 0), # Chansey: Natural Cure
    (113, 99, 0), # Chansey: Serene Grace
    (113, 100, 1), # Chansey: Healer (hidden)
    
    # Tangela
    (114, 2, 0), # Tangela: Chlorophyll
    (114, 101, 0), # Tangela: Leaf Guard
    (114, 56, 1), # Tangela: Regenerator (hidden)
    
    # Kangaskhan
    (115, 102, 0), # Kangaskhan: Early Bird
    (115, 36, 0), # Kangaskhan: Scrappy
    (115, 37, 1), # Kangaskhan: Inner Focus (hidden)
    
    # Horsea line
    (116, 52, 0), # Horsea: Swift Swim
    (116, 11, 0), # Horsea: Sniper
    (116, 48, 1), # Horsea: Damp (hidden)
    (117, 86, 0), # Seadra: Poison Point
    (117, 11, 0), # Seadra: Sniper
    (117, 48, 1), # Seadra: Damp (hidden)
    
    # Goldeen line
    (118, 52, 0), # Goldeen: Swift Swim
    (118, 49, 0), # Goldeen: Water Veil
    (118, 20, 1), # Goldeen: Lightning Rod (hidden)
    (119, 52, 0), # Seaking: Swift Swim
    (119, 49, 0), # Seaking: Water Veil
    (119, 20, 1), # Seaking: Lightning Rod (hidden)
    
    # Staryu line
    (120, 103, 0), # Staryu: Illuminate
    (120, 98, 0), # Staryu: Natural Cure
    (120, 82, 1), # Staryu: Analytic (hidden)
    (121, 103, 0), # Starmie: Illuminate
    (121, 98, 0), # Starmie: Natural Cure
    (121, 82, 1), # Starmie: Analytic (hidden)
    
    # Mr. Mime
    (122, 91, 0), # Mr. Mime: Soundproof
    (122, 104, 0), # Mr. Mime: Filter
    (122, 74, 1), # Mr. Mime: Technician (hidden)
    
    # Scyther
    (123, 10, 0), # Scyther: Swarm
    (123, 74, 0), # Scyther: Technician
    (123, 105, 1), # Scyther: Steadfast (hidden)
    
    # Jynx
    (124, 54, 0), # Jynx: Oblivious
    (124, 48, 0), # Jynx: Forewarn
    (124, 47, 1), # Jynx: Dry Skin (hidden)
    
    # Electabuzz
    (125, 19, 0), # Electabuzz: Static
    (125, 77, 1), # Electabuzz: Vital Spirit (hidden)
    
    # Magmar
    (126, 31, 0), # Magmar: Flame Body
    (126, 77, 1), # Magmar: Vital Spirit (hidden)
    
    # Pinsir
    (127, 90, 0), # Pinsir: Hyper Cutter
    (127, 106, 0), # Pinsir: Mold Breaker
    (127, 107, 1), # Pinsir: Moxie (hidden)
    
    # Tauros
    (128, 17, 0), # Tauros: Intimidate
    (128, 78, 0), # Tauros: Anger Point
    (128, 26, 1), # Tauros: Sheer Force (hidden)
    
    # Magikarp line
    (129, 52, 0), # Magikarp: Swift Swim
    (129, 108, 1), # Magikarp: Rattled (hidden)
    (130, 17, 0), # Gyarados: Intimidate
    (130, 107, 1), # Gyarados: Moxie (hidden)
    
    # Lapras
    (131, 49, 0), # Lapras: Water Absorb
    (131, 61, 0), # Lapras: Shell Armor
    (131, 84, 1), # Lapras: Hydration (hidden)
    
    # Ditto
    (132, 75, 0), # Ditto: Limber
    (132, 109, 1), # Ditto: Imposter (hidden)

    # Eevee line
    (133, 32, 0), # Eevee: Run Away
    (133, 110, 0), # Eevee: Adaptability
    (133, 111, 1), # Eevee: Anticipation (hidden)
    (134, 49, 0), # Vaporeon: Water Absorb
    (134, 84, 1), # Vaporeon: Hydration (hidden)
    (135, 112, 0), # Jolteon: Volt Absorb
    (135, 113, 1), # Jolteon: Quick Feet (hidden)
    (136, 30, 0), # Flareon: Flash Fire
    (136, 15, 1), # Flareon: Guts (hidden)
    
    # Porygon
    (137, 114, 0), # Porygon: Trace
    (137, 115, 0), # Porygon: Download
    (137, 82, 1), # Porygon: Analytic (hidden)
    
    # Omanyte line
    (138, 52, 0), # Omanyte: Swift Swim
    (138, 61, 0), # Omanyte: Shell Armor
    (138, 89, 1), # Omanyte: Weak Armor (hidden)
    (139, 52, 0), # Omastar: Swift Swim
    (139, 61, 0), # Omastar: Shell Armor
    (139, 89, 1), # Omastar: Weak Armor (hidden)
    
    # Kabuto line
    (140, 52, 0), # Kabuto: Swift Swim
    (140, 94, 0), # Kabuto: Battle Armor
    (140, 89, 1), # Kabuto: Weak Armor (hidden)
    (141, 52, 0), # Kabutops: Swift Swim
    (141, 94, 0), # Kabutops: Battle Armor
    (141, 89, 1), # Kabutops: Weak Armor (hidden)
    
    # Aerodactyl
    (142, 42, 0), # Aerodactyl: Rock Head
    (142, 116, 0), # Aerodactyl: Pressure
    (142, 96, 1), # Aerodactyl: Unburden (hidden)
    
    # Snorlax
    (143, 109, 0), # Snorlax: Immunity
    (143, 83, 0), # Snorlax: Thick Fat
    (143, 34, 1), # Snorlax: Gluttony (hidden)
    
    # Articuno
    (144, 116, 0), # Articuno: Pressure
    (144, 117, 1), # Articuno: Snow Cloak (hidden)
    
    # Zapdos
    (145, 116, 0), # Zapdos: Pressure
    (145, 20, 1), # Zapdos: Lightning Rod (hidden)
    
    # Moltres
    (146, 116, 0), # Moltres: Pressure
    (146, 31, 1), # Moltres: Flame Body (hidden)
    
    # Dratini line
    (147, 58, 0), # Dratini: Shed Skin
    (147, 118, 1), # Dratini: Marvel Scale (hidden)
    (148, 58, 0), # Dragonair: Shed Skin
    (148, 118, 1), # Dragonair: Marvel Scale (hidden)
    (149, 37, 0), # Dragonite: Inner Focus
    (149, 119, 1), # Dragonite: Multiscale (hidden)
    
    # Mewtwo
    (150, 116, 0), # Mewtwo: Pressure
    (150, 18, 1), # Mewtwo: Unnerve (hidden)
    
    # Mew
    (151, 38, 0), # Mew: Synchronize
]


# Pokemon data
pokemon_data = [
    (1, 'Bulbasaur', None, 0.7, 6.9, 0, 1, 45, 49, 49, 65, 65, 45, 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon.', 'Grassland'),
    (2, 'Ivysaur', None, 1.0, 13.0, 0, 1, 60, 62, 63, 80, 80, 60, 'When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs.', 'Grassland'),
    (3, 'Venusaur', None, 2.0, 100.0, 0, 1, 80, 82, 83, 100, 100, 80, 'The plant blooms when it is absorbing solar energy. It stays on the move to seek sunlight.', 'Grassland'),
    (4, 'Charmander', None, 0.6, 8.5, 0, 1, 39, 52, 43, 60, 50, 65, 'Obviously prefers hot places. When it rains, steam is said to spout from the tip of its tail.', 'Mountain'),
    (5, 'Charmeleon', None, 1.1, 19.0, 0, 1, 58, 64, 58, 80, 65, 80, 'When it swings its burning tail, it elevates the temperature to unbearably hot levels.', 'Mountain'),
    (6, 'Charizard', None, 1.7, 90.5, 0, 1, 78, 84, 78, 109, 85, 100, 'Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.', 'Mountain'),
    (7, 'Squirtle', None, 0.5, 9.0, 0, 1, 44, 48, 65, 50, 64, 43, 'After birth, its back swells and hardens into a shell. Powerfully sprays foam from its mouth.', 'Waters-edge'),
    (8, 'Wartortle', None, 1.0, 22.5, 0, 1, 59, 63, 80, 65, 80, 58, 'Often hides in water to stalk unwary prey. For swimming fast, it moves its ears to maintain balance.', 'Waters-edge'),
    (9, 'Blastoise', None, 1.6, 85.5, 0, 1, 79, 83, 100, 85, 105, 78, 'A brutal Pokemon with pressurized water jets on its shell. They are used for high speed tackles.', 'Waters-edge'),
    (10, 'Caterpie', None, 0.3, 2.9, 0, 1, 45, 30, 35, 20, 20, 45, 'Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls.', 'Forest'),
    (11, 'Metapod', None, 0.7, 9.9, 0, 1, 50, 20, 55, 25, 25, 30, 'This Pokemon is vulnerable to attack while its shell is soft, exposing its weak and tender body.', 'Forest'),
    (12, 'Butterfree', None, 1.1, 32.0, 0, 1, 60, 45, 50, 90, 80, 70, 'In battle, it flaps its wings at high speed to release highly toxic dust into the air.', 'Forest'),
    (13, 'Weedle', None, 0.3, 3.2, 0, 1, 40, 35, 30, 20, 20, 50, 'Often found in forests, eating leaves. It has a sharp venomous stinger on its head.', 'Forest'),
    (14, 'Kakuna', None, 0.6, 10.0, 0, 1, 45, 25, 50, 25, 25, 35, 'Almost incapable of moving, this Pokemon can only harden its shell to protect itself from predators.', 'Forest'),
    (15, 'Beedrill', None, 1.0, 29.5, 0, 1, 65, 90, 40, 45, 80, 75, 'Flies at high speed and attacks using its large venomous stingers on its forelegs and tail.', 'Forest'),
    (16, 'Pidgey', None, 0.3, 1.8, 0, 1, 40, 45, 40, 35, 35, 56, 'A common sight in forests and woods. It flaps its wings at ground level to kick up blinding sand.', 'Forest'),
    (17, 'Pidgeotto', None, 1.1, 30.0, 0, 1, 63, 60, 55, 50, 50, 71, 'Very protective of its sprawling territorial area, this Pokemon will fiercely peck at any intruder.', 'Forest'),
    (18, 'Pidgeot', None, 1.5, 39.5, 0, 1, 83, 80, 75, 70, 70, 101, 'When hunting, it skims the surface of water at high speed to pick off unwary prey such as Magikarp.', 'Forest'),
    (19, 'Rattata', None, 0.3, 3.5, 0, 1, 30, 56, 35, 25, 35, 72, 'Bites anything when it attacks. Small and very quick, it is a common sight in many places.', 'Grassland'),
    (20, 'Raticate', None, 0.7, 18.5, 0, 1, 55, 81, 60, 50, 70, 97, 'It uses its whiskers to maintain its balance. It apparently slows down if they are cut off.', 'Grassland'),
    (21, 'Spearow', None, 0.3, 2.0, 0, 1, 40, 60, 30, 31, 31, 70, 'Eats bugs in grassy areas. It has to flap its short wings at high speed to stay airborne.', 'Rough-terrain'),
    (22, 'Fearow', None, 1.2, 38.0, 0, 1, 65, 90, 65, 61, 61, 100, 'With its huge and magnificent wings, it can keep aloft without ever having to land for rest.', 'Rough-terrain'),
    (23, 'Ekans', None, 2.0, 6.9, 0, 1, 35, 60, 44, 40, 54, 55, 'Moves silently and stealthily. Eats the eggs of birds, such as Pidgey and Spearow, whole.', 'Grassland'),
    (24, 'Arbok', None, 3.5, 65.0, 0, 1, 60, 95, 69, 65, 79, 80, 'It is rumored that the ferocious warning markings on its belly differ from area to area.', 'Grassland'),
    (25, 'Pikachu', None, 0.4, 6.0, 0, 1, 35, 55, 40, 50, 50, 90, 'When several of these Pokemon gather, their electricity could build and cause lightning storms.', 'Forest'),
    (26, 'Raichu', None, 0.8, 30.0, 0, 1, 60, 90, 55, 90, 80, 110, 'Its long tail serves as a ground to protect itself from its own high voltage power.', 'Forest'),
    (27, 'Sandshrew', None, 0.6, 12.0, 0, 1, 50, 75, 85, 20, 30, 40, 'Burrows deep underground in arid locations far from water. It only emerges to hunt for food.', 'Rough-terrain'),
    (28, 'Sandslash', None, 1.0, 29.5, 0, 1, 75, 100, 110, 45, 55, 65, 'Curls up into a spiny ball when threatened. It can roll while curled up to attack or escape.', 'Rough-terrain'),
    (29, 'Nidoran♀', None, 0.4, 7.0, 0, 1, 55, 47, 52, 40, 40, 41, 'Although small, its venomous barbs render this Pokemon dangerous. The female has smaller horns.', 'Grassland'),
    (30, 'Nidorina', None, 0.8, 20.0, 0, 1, 70, 62, 67, 55, 55, 56, 'The female\'s horn develops slowly. Prefers physical attacks such as clawing and biting.', 'Grassland'),
    (31, 'Nidoqueen', None, 1.3, 60.0, 0, 1, 90, 92, 87, 75, 85, 76, 'Its hard scales provide strong protection. It uses its hefty bulk to execute powerful moves.', 'Grassland'),
    (32, 'Nidoran♂', None, 0.5, 9.0, 0, 1, 46, 57, 40, 40, 40, 50, 'Stiffens its ears to sense danger. The larger its horns, the more powerful its secreted venom.', 'Grassland'),
    (33, 'Nidorino', None, 0.9, 19.5, 0, 1, 61, 72, 57, 55, 55, 65, 'An aggressive Pokemon that is quick to attack. The horn on its head secretes a powerful venom.', 'Grassland'),
    (34, 'Nidoking', None, 1.4, 62.0, 0, 1, 81, 102, 77, 85, 75, 85, 'It uses its powerful tail in battle to smash, constrict, then break the prey\'s bones.', 'Grassland'),
    (35, 'Clefairy', None, 0.6, 7.5, 0, 1, 70, 45, 48, 60, 65, 35, 'Its magical and cute appeal has many admirers. It is rare and found only in certain areas.', 'Mountain'),
    (36, 'Clefable', None, 1.3, 40.0, 0, 1, 95, 70, 73, 95, 90, 60, 'A timid fairy Pokemon that is rarely seen. It will run and hide the moment it senses people.', 'Mountain'),
    (37, 'Vulpix', None, 0.6, 9.9, 0, 1, 38, 41, 40, 50, 65, 65, 'At the time of birth, it has just one tail. The tail splits from its tip as it grows older.', 'Grassland'),
    (38, 'Ninetales', None, 1.1, 19.9, 0, 1, 73, 76, 75, 81, 100, 100, 'Very smart and vindictive. Grabbing one of its many tails could result in a 1000-year curse.', 'Grassland'),
    (39, 'Jigglypuff', None, 0.5, 5.5, 0, 1, 115, 45, 20, 45, 25, 20, 'When its huge eyes light up, it sings a mysteriously soothing melody that lulls its enemies to sleep.', 'Grassland'),
    (40, 'Wigglytuff', None, 1.0, 12.0, 0, 1, 140, 70, 45, 85, 50, 45, 'The body is soft and rubbery. When angered, it will suck in air and inflate itself to an enormous size.', 'Grassland'),
    (41, 'Zubat', None, 0.8, 7.5, 0, 1, 40, 45, 35, 30, 40, 55, 'Forms colonies in perpetually dark places. Uses ultrasonic waves to identify and approach targets.', 'Cave'),
    (42, 'Golbat', None, 1.6, 55.0, 0, 1, 75, 80, 70, 65, 75, 90, 'Once it strikes, it will not stop draining energy from the victim even if it gets too heavy to fly.', 'Cave'),
    (43, 'Oddish', None, 0.5, 5.4, 0, 1, 45, 50, 55, 75, 65, 30, 'During the day, it keeps its face buried in the ground. At night, it wanders around sowing its seeds.', 'Grassland'),
    (44, 'Gloom', None, 0.8, 8.6, 0, 1, 60, 65, 70, 85, 75, 40, 'The fluid that oozes from its mouth isn\'t drool. It is a nectar that is used to attract prey.', 'Grassland'),
    (45, 'Vileplume', None, 1.2, 18.6, 0, 1, 75, 80, 85, 110, 90, 50, 'The larger its petals, the more toxic pollen it contains. It has the largest petals in the world.', 'Grassland'),
    (46, 'Paras', None, 0.3, 5.4, 0, 1, 35, 70, 55, 45, 55, 25, 'Burrows to suck tree roots. The mushrooms on its back grow by drawing nutrients from the bug host.', 'Forest'),
    (47, 'Parasect', None, 1.0, 29.5, 0, 1, 60, 95, 80, 60, 80, 30, 'A host-parasite pair in which the parasite mushroom has taken over the host bug. Prefers damp places.', 'Forest'),
    (48, 'Venonat', None, 1.0, 30.0, 0, 1, 60, 55, 50, 40, 55, 45, 'Lives in the shadows of tall trees where it eats insects. It is attracted to light at night.', 'Forest'),
    (49, 'Venomoth', None, 1.5, 12.5, 0, 1, 70, 65, 60, 90, 75, 90, 'The dust-like scales covering its wings are color coded to indicate the kinds of poison it has.', 'Forest'),
    (50, 'Diglett', None, 0.2, 0.8, 0, 1, 10, 55, 25, 35, 45, 95, 'Lives about one yard underground where it feeds on plant roots. It also appears above ground.', 'Cave'),
    (51, 'Dugtrio', None, 0.7, 33.3, 0, 1, 35, 100, 50, 50, 70, 120, 'A team of Diglett triplets. It triggers huge earthquakes by burrowing 60 miles underground.', 'Cave'),
    (52, 'Meowth', None, 0.4, 4.2, 0, 1, 40, 45, 35, 40, 40, 90, 'Adores circular objects. Wanders the streets on a nightly basis to look for dropped loose change.', 'Urban'),
    (53, 'Persian', None, 1.0, 32.0, 0, 1, 65, 70, 60, 65, 65, 115, 'Although its fur has many admirers, it is tough to raise as a pet because of its fickle meanness.', 'Urban'),
    (54, 'Psyduck', None, 0.8, 19.6, 0, 1, 50, 52, 48, 65, 50, 55, 'While lulling its enemies with its vacant look, this wily Pokemon will use psychokinetic powers.', 'Waters-edge'),
    (55, 'Golduck', None, 1.7, 76.6, 0, 1, 80, 82, 78, 95, 80, 85, 'Often seen swimming elegantly by lake shores. It is often mistaken for the Japanese monster, Kappa.', 'Waters-edge'),
    (56, 'Mankey', None, 0.5, 28.0, 0, 1, 40, 80, 35, 35, 45, 70, 'Extremely quick to anger. It could be docile one moment then thrashing away the next instant.', 'Mountain'),
    (57, 'Primeape', None, 1.0, 32.0, 0, 1, 65, 105, 60, 60, 70, 95, 'Always furious and tenacious to boot. It will not abandon chasing its quarry until it is caught.', 'Mountain'),
    (58, 'Growlithe', None, 0.7, 19.0, 0, 1, 55, 70, 45, 70, 50, 60, 'Very protective of its territory. It will bark and bite to repel intruders from its space.', 'Grassland'),
    (59, 'Arcanine', None, 1.9, 155.0, 0, 1, 90, 110, 80, 100, 80, 95, 'A Pokemon that has been admired since the past for its beauty. It runs agilely as if on wings.', 'Grassland'),
    (60, 'Poliwag', None, 0.6, 12.4, 0, 1, 40, 50, 40, 40, 40, 90, 'Its newly grown legs prevent it from running. It appears to prefer swimming than trying to stand.', 'Waters-edge'),
    (61, 'Poliwhirl', None, 1.0, 20.0, 0, 1, 65, 65, 65, 50, 50, 90, 'Capable of living in or out of water. When out of water, it sweats to keep its body slimy.', 'Waters-edge'),
    (62, 'Poliwrath', None, 1.3, 54.0, 0, 1, 90, 95, 95, 70, 90, 70, 'An adept swimmer at both the front crawl and breast stroke. Easily overtakes the best human swimmers.', 'Waters-edge'),
    (63, 'Abra', None, 0.9, 19.5, 0, 1, 25, 20, 15, 105, 55, 90, 'Using its ability to read minds, it will identify impending danger and teleport to safety.', 'Urban'),
    (64, 'Kadabra', None, 1.3, 56.5, 0, 1, 40, 35, 30, 120, 70, 105, 'It emits special alpha waves from its body that induce headaches just by being close by.', 'Urban'),
    (65, 'Alakazam', None, 1.5, 48.0, 0, 1, 55, 50, 45, 135, 95, 120, 'Its brain can outperform a supercomputer. Its intelligence quotient is said to be 5,000.', 'Urban'),
    (66, 'Machop', None, 0.8, 19.5, 0, 1, 70, 80, 50, 35, 35, 35, 'Loves to build its muscles. It trains in all styles of martial arts to become even stronger.', 'Mountain'),
    (67, 'Machoke', None, 1.5, 70.5, 0, 1, 80, 100, 70, 50, 60, 45, 'Its muscular body is so powerful, it must wear a power save belt to be able to regulate its motions.', 'Mountain'),
    (68, 'Machamp', None, 1.6, 130.0, 0, 1, 90, 130, 80, 65, 85, 55, 'Using its heavy muscles, it throws powerful punches that can send the victim clear over the horizon.', 'Mountain'),
    (69, 'Bellsprout', None, 0.7, 4.0, 0, 1, 50, 75, 35, 70, 30, 40, 'A carnivorous Pokemon that traps and eats bugs. It uses its root feet to soak up needed moisture.', 'Forest'),
    (70, 'Weepinbell', None, 1.0, 6.4, 0, 1, 65, 90, 50, 85, 45, 55, 'It spits out poison powder to immobilize the enemy and then finishes it with a spray of acid.', 'Forest'),
    (71, 'Victreebel', None, 1.7, 15.5, 0, 1, 80, 105, 65, 100, 70, 70, 'Said to live in huge colonies deep in jungles, although no one has ever returned from there.', 'Forest'),
    (72, 'Tentacool', None, 0.9, 45.5, 0, 1, 40, 40, 35, 50, 100, 70, 'Drifts in shallow seas. Anglers who hook them by accident are often punished by its stinging acid.', 'Sea'),
    (73, 'Tentacruel', None, 1.6, 55.0, 0, 1, 80, 70, 65, 80, 120, 100, 'The tentacles are normally kept short. On hunts, they are extended to ensnare and immobilize prey.', 'Sea'),
    (74, 'Geodude', None, 0.4, 20.0, 0, 1, 40, 80, 100, 30, 30, 20, 'Found in fields and mountains. Mistaking them for boulders, people often step or trip on them.', 'Mountain'),
    (75, 'Graveler', None, 1.0, 105.0, 0, 1, 55, 95, 115, 45, 45, 35, 'Rolls down slopes to move. It rolls over any obstacle without slowing or changing its direction.', 'Mountain'),
    (76, 'Golem', None, 1.4, 300.0, 0, 1, 80, 120, 130, 55, 65, 45, 'Its boulder-like body is extremely hard. It can easily withstand dynamite blasts without damage.', 'Mountain'),
    (77, 'Ponyta', None, 1.0, 30.0, 0, 1, 50, 85, 55, 65, 65, 90, 'Its hooves are 10 times harder than diamonds. It can trample anything completely flat in little time.', 'Grassland'),
    (78, 'Rapidash', None, 1.7, 95.0, 0, 1, 65, 100, 70, 80, 80, 105, 'Very competitive, this Pokemon will chase anything that moves fast in the hopes of racing it.', 'Grassland'),
    (79, 'Slowpoke', None, 1.2, 36.0, 0, 1, 90, 65, 65, 40, 40, 15, 'Incredibly slow and dopey. It takes 5 seconds for it to feel pain when under attack.', 'Waters-edge'),
    (80, 'Slowbro', None, 1.6, 78.5, 0, 1, 95, 75, 110, 100, 80, 30, 'The Shellder that is latched onto Slowpoke\'s tail is said to feed on the host\'s left over scraps.', 'Waters-edge'),
    (81, 'Magnemite', None, 0.3, 6.0, 0, 1, 25, 35, 70, 95, 55, 45, 'Uses anti-gravity to stay suspended. Appears without warning and uses Thunder Wave and similar moves.', 'Urban'),
    (82, 'Magneton', None, 1.0, 60.0, 0, 1, 50, 60, 95, 120, 70, 70, 'Formed by several Magnemite linking together. They frequently appear when sunspots flare up.', 'Urban'),
    (83, 'Farfetch\'d', None, 0.8, 15.0, 0, 1, 52, 90, 55, 58, 62, 60, 'The plant stalk it holds is its weapon. The stalk is used like a sword to cut all sorts of things.', 'Grassland'),
    (84, 'Doduo', None, 1.4, 39.2, 0, 1, 35, 85, 45, 35, 35, 75, 'A bird that makes up for its poor flying with its fast foot speed. Leaves giant footprints.', 'Grassland'),
    (85, 'Dodrio', None, 1.8, 85.2, 0, 1, 60, 110, 70, 60, 60, 110, 'Uses its three brains to execute complex plans. While two heads sleep, one head stays awake.', 'Grassland'),
    (86, 'Seel', None, 1.1, 90.0, 0, 1, 65, 45, 55, 45, 70, 45, 'The protruding horn on its head is very hard. It is used for bashing through thick ice.', 'Sea'),
    (87, 'Dewgong', None, 1.7, 120.0, 0, 1, 90, 70, 80, 70, 95, 70, 'Stores thermal energy in its body. Swims at a steady 8 knots even in intensely cold waters.', 'Sea'),
    (88, 'Grimer', None, 0.9, 30.0, 0, 1, 80, 80, 50, 40, 50, 25, 'Appears in filthy areas. Thrives by sucking up polluted sludge that is pumped out of factories.', 'Urban'),
    (89, 'Muk', None, 1.2, 30.0, 0, 1, 105, 105, 75, 65, 100, 50, 'Thickly covered with a filthy, vile sludge. It is so toxic, even its footprints contain poison.', 'Urban'),
    (90, 'Shellder', None, 0.3, 4.0, 0, 1, 30, 65, 100, 45, 25, 40, 'Its hard shell repels any kind of attack. It is vulnerable only when its shell is open.', 'Sea'),
    (91, 'Cloyster', None, 1.5, 132.5, 0, 1, 50, 95, 180, 85, 45, 70, 'When attacked, it launches its horns in quick volleys. Its innards have never been seen.', 'Sea'),
    (92, 'Gastly', None, 1.3, 0.1, 0, 1, 30, 35, 30, 100, 35, 80, 'Almost invisible, this gaseous Pokemon cloaks the target and puts it to sleep without notice.', 'Cave'),
    (93, 'Haunter', None, 1.6, 0.1, 0, 1, 45, 50, 45, 115, 55, 95, 'Because of its ability to slip through block walls, it is said to be from another dimension.', 'Cave'),
    (94, 'Gengar', None, 1.5, 40.5, 0, 1, 60, 65, 60, 130, 75, 110, 'Under a full moon, this Pokemon likes to mimic the shadows of people and laugh at their fright.', 'Cave'),
    (95, 'Onix', None, 8.8, 210.0, 0, 1, 35, 45, 160, 30, 45, 70, 'As it grows, the stone portions of its body harden to become similar to a diamond, but colored black.', 'Cave'),
    (96, 'Drowzee', None, 1.0, 32.4, 0, 1, 60, 48, 45, 43, 90, 42, 'Puts enemies to sleep then eats their dreams. Occasionally gets sick from eating bad dreams.', 'Urban'),
    (97, 'Hypno', None, 1.6, 75.6, 0, 1, 85, 73, 70, 73, 115, 67, 'When it locks eyes with an enemy, it will use a mix of psi powers such as Hypnosis and Confusion.', 'Urban'),
    (98, 'Krabby', None, 0.4, 6.5, 0, 1, 30, 105, 90, 25, 25, 50, 'Its pincers are not only powerful, they are also very dexterous. It can catch prey or battle with them.', 'Waters-edge'),
    (99, 'Kingler', None, 1.3, 60.0, 0, 1, 55, 130, 115, 50, 50, 75, 'The large pincer has 10000 hp of crushing power. However, its huge size makes it unwieldy to use.', 'Waters-edge'),
    (100, 'Voltorb', None, 0.5, 10.4, 0, 1, 40, 30, 50, 55, 55, 100, 'Usually found in power plants. Easily mistaken for a Poke Ball, they have zapped many people.', 'Urban'),
    (101, 'Electrode', None, 1.2, 66.6, 0, 1, 60, 50, 70, 80, 80, 150, 'It stores electric energy under very high pressure. It often explodes with little or no provocation.', 'Urban'),
    (102, 'Exeggcute', None, 0.4, 2.5, 0, 1, 60, 40, 80, 60, 45, 40, 'Often mistaken for eggs. When disturbed, they quickly gather and attack in swarms.', 'Forest'),
    (103, 'Exeggutor', None, 2.0, 120.0, 0, 1, 95, 95, 85, 125, 75, 55, 'Legend has it that on rare occasions, one of its heads will drop off and continue living as an Exeggcute.', 'Forest'),
    (104, 'Cubone', None, 0.4, 6.5, 0, 1, 50, 50, 95, 40, 50, 35, 'Because it never removes its skull helmet, no one has ever seen this Pokemon\'s real face.', 'Mountain'),
    (105, 'Marowak', None, 1.0, 45.0, 0, 1, 60, 80, 110, 50, 80, 45, 'The bone it holds is its key weapon. It throws the bone skillfully like a boomerang to KO targets.', 'Mountain'),
    (106, 'Hitmonlee', None, 1.5, 49.8, 0, 1, 50, 120, 53, 35, 110, 87, 'When in a hurry, its legs lengthen progressively. It runs smoothly with extra long, loping strides.', 'Urban'),
    (107, 'Hitmonchan', None, 1.4, 50.2, 0, 1, 50, 105, 79, 35, 110, 76, 'While apparently doing nothing, it fires punches in lightning fast volleys that are impossible to see.', 'Urban'),
    (108, 'Lickitung', None, 1.2, 65.5, 0, 1, 90, 55, 75, 60, 75, 30, 'Its tongue can be extended like a chameleon\'s. It leaves a tingling sensation when it licks enemies.', 'Grassland'),
    (109, 'Koffing', None, 0.6, 1.0, 0, 1, 40, 65, 95, 60, 45, 35, 'Because it stores several kinds of toxic gases in its body, it is prone to exploding without warning.', 'Urban'),
    (110, 'Weezing', None, 1.2, 9.5, 0, 1, 65, 90, 120, 85, 70, 60, 'Where two kinds of poison gases meet, 2 Koffings can fuse into a Weezing over many years.', 'Urban'),
    (111, 'Rhyhorn', None, 1.0, 115.0, 0, 1, 80, 85, 95, 30, 30, 25, 'Its massive bones are 1000 times harder than human bones. It can easily knock a trailer truck flying.', 'Rough-terrain'),
    (112, 'Rhydon', None, 1.9, 120.0, 0, 1, 105, 130, 120, 45, 45, 40, 'Protected by an armor-like hide, it is capable of living in molten lava of 3,600 degrees.', 'Rough-terrain'),
    (113, 'Chansey', None, 1.1, 34.6, 0, 1, 250, 5, 5, 35, 105, 50, 'A rare and elusive Pokemon that is said to bring happiness to those who manage to get it.', 'Urban'),
    (114, 'Tangela', None, 1.0, 35.0, 0, 1, 65, 55, 115, 100, 40, 60, 'The whole body is swathed with wide vines that are similar to seaweed. Its vines shake as it walks.', 'Grassland'),
    (115, 'Kangaskhan', None, 2.2, 80.0, 0, 1, 105, 95, 80, 40, 80, 90, 'The infant rarely ventures out of its mother\'s protective pouch until it is 3 years old.', 'Grassland'),
    (116, 'Horsea', None, 0.4, 8.0, 0, 1, 30, 40, 70, 70, 25, 60, 'Known to shoot down flying bugs with precision blasts of ink from the surface of the water.', 'Sea'),
    (117, 'Seadra', None, 1.2, 25.0, 0, 1, 55, 65, 95, 95, 45, 85, 'Capable of swimming backwards by rapidly flapping its wing-like pectoral fins and stout tail.', 'Sea'),
    (118, 'Goldeen', None, 0.6, 15.0, 0, 1, 45, 67, 60, 35, 50, 63, 'Its tail fin billows like an elegant ballroom dress, giving it the nickname of the Water Queen.', 'Waters-edge'),
    (119, 'Seaking', None, 1.3, 39.0, 0, 1, 80, 92, 65, 65, 80, 68, 'In the autumn spawning season, they can be seen swimming powerfully up rivers and creeks.', 'Waters-edge'),
    (120, 'Staryu', None, 0.8, 34.5, 0, 1, 30, 45, 55, 70, 55, 85, 'An enigmatic Pokemon that can effortlessly regenerate any appendage it loses in battle.', 'Sea'),
    (121, 'Starmie', None, 1.1, 80.0, 0, 1, 60, 75, 85, 100, 85, 115, 'Its central core glows with the seven colors of the rainbow. Some people value the core as a gem.', 'Sea'),
    (122, 'Mr. Mime', None, 1.3, 54.5, 0, 1, 40, 45, 65, 100, 120, 90, 'If interrupted while it is miming, it will slap around the offender with its broad hands.', 'Urban'),
    (123, 'Scyther', None, 1.5, 56.0, 0, 1, 70, 110, 80, 55, 80, 105, 'With ninja-like agility and speed, it can create the illusion that there is more than one.', 'Grassland'),
    (124, 'Jynx', None, 1.4, 40.6, 0, 1, 65, 50, 35, 115, 95, 95, 'It seductively wiggles its hips as it walks. It can cause people to dance in unison with it.', 'Urban'),
    (125, 'Electabuzz', None, 1.1, 30.0, 0, 1, 65, 83, 57, 95, 85, 105, 'Normally found near power plants, they can wander away and cause major blackouts in cities.', 'Urban'),
    (126, 'Magmar', None, 1.3, 44.5, 0, 1, 65, 95, 57, 100, 85, 93, 'Its body always burns with an orange glow that enables it to hide perfectly among flames.', 'Mountain'),
    (127, 'Pinsir', None, 1.5, 55.0, 0, 1, 65, 125, 100, 55, 70, 85, 'If it fails to crush the victim in its pincers, it will swing it around and toss it hard.', 'Forest'),
    (128, 'Tauros', None, 1.4, 88.4, 0, 1, 75, 100, 95, 40, 70, 110, 'When it targets an enemy, it charges furiously while whipping its body with its long tails.', 'Grassland'),
    (129, 'Magikarp', None, 0.9, 10.0, 0, 1, 20, 10, 55, 15, 20, 80, 'In the distant past, it was somewhat stronger than the horribly weak descendants that exist today.', 'Waters-edge'),
    (130, 'Gyarados', None, 6.5, 235.0, 0, 1, 95, 125, 79, 60, 100, 81, 'Rarely seen in the wild. Huge and vicious, it is capable of destroying entire cities in a rage.', 'Waters-edge'),
    (131, 'Lapras', None, 2.5, 220.0, 0, 1, 130, 85, 80, 85, 95, 60, 'A Pokemon that has been overhunted almost to extinction. It can ferry people across bodies of water.', 'Sea'),
    (132, 'Ditto', None, 0.3, 4.0, 0, 1, 48, 48, 48, 48, 48, 48, 'Capable of copying an enemy\'s genetic code to instantly transform itself into a duplicate of the enemy.', 'Urban'),
    (133, 'Eevee', None, 0.3, 6.5, 0, 1, 55, 55, 50, 45, 65, 55, 'Its genetic code is irregular. It may mutate if it is exposed to radiation from element stones.', 'Urban'),
    (134, 'Vaporeon', None, 1.0, 29.0, 0, 1, 130, 65, 60, 110, 95, 65, 'Lives close to water. Its long tail is ridged with a fin which is often mistaken for a mermaid\'s.', 'Waters-edge'),
    (135, 'Jolteon', None, 0.8, 24.5, 0, 1, 65, 65, 60, 110, 95, 130, 'It accumulates negative ions in the atmosphere to blast out 10000-volt lightning bolts.', 'Urban'),
    (136, 'Flareon', None, 0.9, 25.0, 0, 1, 65, 130, 60, 95, 110, 65, 'When storing thermal energy in its body, its temperature could soar to over 1600 degrees.', 'Grassland'),
    (137, 'Porygon', None, 0.8, 36.5, 0, 1, 65, 60, 70, 85, 75, 40, 'A Pokemon that consists entirely of programming code. Capable of moving freely in cyberspace.', 'Urban'),
    (138, 'Omanyte', None, 0.4, 7.5, 0, 1, 35, 40, 100, 90, 55, 35, 'Although long extinct, in rare cases, it can be genetically resurrected from fossils.', 'Sea'),
    (139, 'Omastar', None, 1.0, 35.0, 0, 1, 70, 60, 125, 115, 70, 55, 'A prehistoric Pokemon that died out when its heavy shell made it impossible to catch prey.', 'Sea'),
    (140, 'Kabuto', None, 0.5, 11.5, 0, 1, 30, 80, 90, 55, 45, 55, 'A Pokemon that was resurrected from a fossil found in what was once the ocean floor eons ago.', 'Sea'),
    (141, 'Kabutops', None, 1.3, 40.5, 0, 1, 60, 115, 105, 65, 70, 80, 'Its sleek shape is perfect for swimming. It slashes prey with its claws and drains the body fluids.', 'Sea'),
    (142, 'Aerodactyl', None, 1.8, 59.0, 0, 1, 80, 105, 65, 60, 75, 130, 'A ferocious, prehistoric Pokemon that goes for the enemy\'s throat with its serrated saw-like fangs.', 'Mountain'),
    (143, 'Snorlax', None, 2.1, 460.0, 0, 1, 160, 110, 65, 65, 110, 30, 'Very lazy. Just eats and sleeps. As its rotund bulk builds, it becomes steadily more slothful.', 'Mountain'),
    (144, 'Articuno', None, 1.7, 55.4, 1, 1, 90, 85, 100, 95, 125, 85, 'A legendary bird Pokemon that is said to appear to doomed people who are lost in icy mountains.', 'Cave'),
    (145, 'Zapdos', None, 1.6, 52.6, 1, 1, 90, 90, 85, 125, 90, 100, 'A legendary bird Pokemon that is said to appear from clouds while dropping enormous lightning bolts.', 'Mountain'),
    (146, 'Moltres', None, 2.0, 60.0, 1, 1, 90, 100, 90, 125, 85, 90, 'Known as the legendary bird of fire. Every flap of its wings creates a dazzling flash of flames.', 'Mountain'),
    (147, 'Dratini', None, 1.8, 3.3, 0, 1, 41, 64, 45, 50, 50, 50, 'Long considered a mythical Pokemon until recently when a small colony was found living underwater.', 'Waters-edge'),
    (148, 'Dragonair', None, 4.0, 16.5, 0, 1, 61, 84, 65, 70, 70, 70, 'A mystical Pokemon that exudes a gentle aura. Has the ability to change climate conditions.', 'Waters-edge'),
    (149, 'Dragonite', None, 2.2, 210.0, 0, 1, 91, 134, 95, 100, 100, 80, 'An extremely rarely seen marine Pokemon. Its intelligence is said to match that of humans.', 'Waters-edge'),
    (150, 'Mewtwo', None, 2.0, 122.0, 1, 1, 106, 110, 90, 154, 90, 130, 'It was created by a scientist after years of horrific gene splicing and DNA engineering experiments.', 'Rare'),
    (151, 'Mew', None, 0.4, 4.0, 1, 1, 100, 100, 100, 100, 100, 100, 'So rare that it is still said to be a mirage by many experts. Only a few people have seen it worldwide.', 'Rare')
]





# Complete type effectiveness data (attacking_type_id, defending_type_id, multiplier)
# Type IDs: Normal=1, Fire=2, Water=3, Electric=4, Grass=5, Ice=6, Fighting=7, Poison=8, 
#          Ground=9, Flying=10, Psychic=11, Bug=12, Rock=13, Ghost=14, Dragon=15, Dark = 16,
#          Steel = 17, Fairy = 18.
type_effectiveness_data = [
    # Normal type effectiveness
    (1, 13, 0.5),  # Normal vs Rock - Not very effective
    (1, 14, 0.0),  # Normal vs Ghost - No effect
    (1, 17, 0.5),  # Normal vs Steel - Not very effective
    
    # Fire type effectiveness
    (2, 2, 0.5),   # Fire vs Fire - Not very effective
    (2, 3, 0.5),   # Fire vs Water - Not very effective
    (2, 5, 2.0),   # Fire vs Grass - Super effective
    (2, 6, 2.0),   # Fire vs Ice - Super effective
    (2, 9, 0.5),   # Fire vs Ground - Not very effective
    (2, 12, 2.0),  # Fire vs Bug - Super effective
    (2, 13, 0.5),  # Fire vs Rock - Not very effective
    (2, 15, 0.5),  # Fire vs Dragon - Not very effective
    (2, 17, 2.0),  # Fire vs Steel - Super effective
    
    # Water type effectiveness
    (3, 2, 2.0),   # Water vs Fire - Super effective
    (3, 3, 0.5),   # Water vs Water - Not very effective
    (3, 5, 0.5),   # Water vs Grass - Not very effective
    (3, 9, 2.0),   # Water vs Ground - Super effective
    (3, 13, 2.0),  # Water vs Rock - Super effective
    (3, 15, 0.5),  # Water vs Dragon - Not very effective
    
    # Electric type effectiveness
    (4, 3, 2.0),   # Electric vs Water - Super effective
    (4, 4, 0.5),   # Electric vs Electric - Not very effective
    (4, 5, 0.5),   # Electric vs Grass - Not very effective
    (4, 9, 0.0),   # Electric vs Ground - No effect
    (4, 10, 2.0),  # Electric vs Flying - Super effective
    (4, 15, 0.5),  # Electric vs Dragon - Not very effective
    
    # Grass type effectiveness
    (5, 2, 0.5),   # Grass vs Fire - Not very effective
    (5, 3, 2.0),   # Grass vs Water - Super effective
    (5, 5, 0.5),   # Grass vs Grass - Not very effective
    (5, 8, 0.5),   # Grass vs Poison - Not very effective
    (5, 9, 2.0),   # Grass vs Ground - Super effective
    (5, 10, 0.5),  # Grass vs Flying - Not very effective
    (5, 12, 0.5),  # Grass vs Bug - Not very effective
    (5, 13, 2.0),  # Grass vs Rock - Super effective
    (5, 15, 0.5),  # Grass vs Dragon - Not very effective
    (5, 17, 0.5),  # Grass vs Steel - Not very effective
    
    # Ice type effectiveness
    (6, 3, 0.5),   # Ice vs Water - Not very effective
    (6, 5, 2.0),   # Ice vs Grass - Super effective
    (6, 6, 0.5),   # Ice vs Ice - Not very effective
    (6, 9, 2.0),   # Ice vs Ground - Super effective
    (6, 10, 2.0),  # Ice vs Flying - Super effective
    (6, 15, 2.0),  # Ice vs Dragon - Super effective
    (6, 17, 0.5),  # Ice vs Steel - Not very effective
    
    # Fighting type effectiveness
    (7, 1, 2.0),   # Fighting vs Normal - Super effective
    (7, 6, 2.0),   # Fighting vs Ice - Super effective
    (7, 8, 0.5),   # Fighting vs Poison - Not very effective
    (7, 10, 0.5),  # Fighting vs Flying - Not very effective
    (7, 11, 0.5),  # Fighting vs Psychic - Not very effective
    (7, 12, 0.5),  # Fighting vs Bug - Not very effective
    (7, 13, 2.0),  # Fighting vs Rock - Super effective
    (7, 14, 0.0),  # Fighting vs Ghost - No effect
    (7, 16, 2.0),  # Fighting vs Dark - Super effective
    (7, 17, 2.0),  # Fighting vs Steel - Super effective
    
    # Poison type effectiveness
    (8, 5, 2.0),   # Poison vs Grass - Super effective
    (8, 8, 0.5),   # Poison vs Poison - Not very effective
    (8, 9, 0.5),   # Poison vs Ground - Not very effective
    (8, 13, 0.5),  # Poison vs Rock - Not very effective
    (8, 14, 0.5),  # Poison vs Ghost - Not very effective
    (8, 17, 0.0),  # Poison vs Steel - No effect
    (8, 18, 2.0),  # Poison vs Fairy - Super effective
    
    # Ground type effectiveness
    (9, 2, 2.0),   # Ground vs Fire - Super effective
    (9, 4, 2.0),   # Ground vs Electric - Super effective
    (9, 5, 0.5),   # Ground vs Grass - Not very effective
    (9, 8, 2.0),   # Ground vs Poison - Super effective
    (9, 10, 0.0),  # Ground vs Flying - No effect
    (9, 12, 0.5),  # Ground vs Bug - Not very effective
    (9, 13, 2.0),  # Ground vs Rock - Super effective
    (9, 17, 2.0),  # Ground vs Steel - Super effective
    
    # Flying type effectiveness
    (10, 4, 0.5),  # Flying vs Electric - Not very effective
    (10, 5, 2.0),  # Flying vs Grass - Super effective
    (10, 7, 2.0),  # Flying vs Fighting - Super effective
    (10, 12, 2.0), # Flying vs Bug - Super effective
    (10, 13, 0.5), # Flying vs Rock - Not very effective
    (10, 17, 0.5), # Flying vs Steel - Not very effective
    
    # Psychic type effectiveness
    (11, 7, 2.0),  # Psychic vs Fighting - Super effective
    (11, 8, 2.0),  # Psychic vs Poison - Super effective
    (11, 11, 0.5), # Psychic vs Psychic - Not very effective
    (11, 16, 0.0), # Psychic vs Dark - No effect
    (11, 17, 0.5), # Psychic vs Steel - Not very effective
    
    # Bug type effectiveness
    (12, 2, 0.5),  # Bug vs Fire - Not very effective
    (12, 5, 2.0),  # Bug vs Grass - Super effective
    (12, 7, 0.5),  # Bug vs Fighting - Not very effective
    (12, 8, 0.5),  # Bug vs Poison - Not very effective
    (12, 10, 0.5), # Bug vs Flying - Not very effective
    (12, 11, 2.0), # Bug vs Psychic - Super effective
    (12, 14, 0.5), # Bug vs Ghost - Not very effective
    (12, 16, 2.0), # Bug vs Dark - Super effective
    (12, 17, 0.5), # Bug vs Steel - Not very effective
    
    # Rock type effectiveness
    (13, 2, 2.0),  # Rock vs Fire - Super effective
    (13, 6, 2.0),  # Rock vs Ice - Super effective
    (13, 7, 0.5),  # Rock vs Fighting - Not very effective
    (13, 9, 0.5),  # Rock vs Ground - Not very effective
    (13, 10, 2.0), # Rock vs Flying - Super effective
    (13, 12, 2.0), # Rock vs Bug - Super effective
    (13, 17, 0.5), # Rock vs Steel - Not very effective
    
    # Ghost type effectiveness
    (14, 1, 0.0),  # Ghost vs Normal - No effect
    (14, 11, 2.0), # Ghost vs Psychic - Super effective
    (14, 14, 2.0), # Ghost vs Ghost - Super effective
    (14, 16, 0.5), # Ghost vs Dark - Not very effective
    
    # Dragon type effectiveness
    (15, 15, 2.0), # Dragon vs Dragon - Super effective
    (15, 17, 0.5), # Dragon vs Steel - Not very effective
    (15, 18, 0.0), # Dragon vs Fairy - No effect
    
    # Dark type effectiveness (Gen 2 but in case we add more)
    (16, 7, 0.5),  # Dark vs Fighting - Not very effective
    (16, 11, 2.0), # Dark vs Psychic - Super effective
    (16, 14, 2.0), # Dark vs Ghost - Super effective
    (16, 16, 0.5), # Dark vs Dark - Not very effective
    (16, 18, 0.5), # Dark vs Fairy - Not very effective
    
    # Steel type effectiveness (Gen 2 but in case we add more)
    (17, 2, 0.5),  # Steel vs Fire - Not very effective
    (17, 3, 0.5),  # Steel vs Water - Not very effective
    (17, 4, 0.5),  # Steel vs Electric - Not very effective
    (17, 6, 2.0),  # Steel vs Ice - Super effective
    (17, 13, 2.0), # Steel vs Rock - Super effective
    (17, 17, 0.5), # Steel vs Steel - Not very effective
    (17, 18, 2.0), # Steel vs Fairy - Super effective
    
    # Fairy type effectiveness (Gen 2 but in case we add more)
    (18, 2, 0.5),  # Fairy vs Fire - Not very effective
    (18, 7, 2.0),  # Fairy vs Fighting - Super effective
    (18, 8, 0.5),  # Fairy vs Poison - Not very effective
    (18, 15, 2.0), # Fairy vs Dragon - Super effective
    (18, 16, 2.0), # Fairy vs Dark - Super effective
    (18, 17, 0.5), # Fairy vs Steel - Not very effective
]




# Insert types (name, color)
types_data = [
    ('Normal', '#A8A878'),      # 0
    ('Fire', '#F08030'),        # 1
    ('Water', '#6890F0'),       # 2
    ('Electric', '#F8D030'),    # 3
    ('Grass', '#78C850'),       # 4
    ('Ice', '#98D8D8'),         # 5
    ('Fighting', '#C03028'),    # 6
    ('Poison', '#A040A0'),      # 7
    ('Ground', '#E0C068'),      # 8
    ('Flying', '#A890F0'),      # 9
    ('Psychic', '#F85888'),     # 10
    ('Bug', '#A8B820'),         # 11
    ('Rock', '#B8A038'),        # 12
    ('Ghost', '#705898'),       # 13
    ('Dragon', '#7038F8'),      # 14
    ('Dark', '#705848'),        # 15
    ('Steel', '#B8B8D0'),       # 16
    ('Fairy', '#EE99AC')        # 17
]

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
