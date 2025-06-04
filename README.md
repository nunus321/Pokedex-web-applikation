# Pokemon Pokedex Flask Web Application
A Flask-based Pokemon Pokedex web application that allows you to browse, view detailed information, and add new Pokemon to your collection.

## Database Schema
The application follows the E/R diagram with the following entities:
- **Pokemon**: Main entity with name, Pokedex number, height, weight, legendary status
- **Types**: Pokemon types (Fire, Water, Grass, etc.) with associated colors
- **Regions**: Pokemon regions (Kanto, Johto, etc.)
- **Pokemon-Types**: Many-to-many relationship for dual-type Pokemon

## Installation and Setup
### Prerequisites
- Python installed
- Flask
- Some dependencies(under step 2)

### Step 1: Set up Python Virtual Environment
Start off by navigating to the folder pokedex_webapp in the terminal

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
First run:
Set-ExecutionPolicy Unrestricted -Scope Process

Then run:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate


### Step 2: Install Dependencies
Run the following in the terminal:

pip install -r requirements.txt

### Step 3: Run the Application
python app.py

## Usage and features of the web application
### Browsing Pokemon
- Visit the main page to see all Pokemon
- Each Pokemon card shows:
  - Pokemon picture
  - Pokedex number
  - Name (with star for legendary Pokemon)
  - Type(s) of the pokemon with appropriate colors

### Viewing Pokemon Details
- Click on any Pokemon card to view detailed information
- Details include all attributes from the E/R diagram and more. Some of the details:
  - Physical stats (height, weight)
  - Type information
  - Legendary status
  - Region of origin

### Adding New Pokemon
- Click "Add Pokemon" in the navigation
- Fill out the form with Pokemon information:
  - Pokedex number (required, must be unique)
  - Name (required)
  - Form (optional, for variants like "Alolan")
  - Height and weight
  - Primary and secondary types
  - Region
  - Legendary status checkbox
  - Stats

