from map import create_3maps_dict
from geodata import get_geodata
from dashboard import create_dashboard
from data import open_and_process_data


if __name__ == '__main__':
    """
    Le point d'entrée principal du programme.
    Charge les données géographiques, crée les cartes et initialise le tableau de bord Dash.
    """
    
    # Charger les données géographiques des start-ups
    startUp_data = get_geodata()

    #charger les données du dataset
    file_path = "startup_data.csv"
    df = open_and_process_data(file_path)
    
    # Créer les cartes de visualisation
    map_dict = create_3maps_dict(startUp_data)
    
    # Créer le tableau de bord Dash
    app = create_dashboard(map_dict, df)
    
    # Lancer le serveur Dash
    app.run_server(debug=True)
