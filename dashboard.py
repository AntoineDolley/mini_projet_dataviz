import dash
from dash import dcc, html, Input, Output
from map import create_3maps_dict
from geodata import get_geodata
from graphs import create_graphs_dict,barSector
from data import open_and_process_data

def create_dashboard(map_dict, df) -> dash.Dash:
    """Crée un tableau de bord Dash avec des cartes et des graphiques basés sur les données fournies.

    Args:
        map_dict (dict): Un dictionnaire contenant des objets cartographiques.
        df (pd.DataFrame): DataFrame contenant les données des startups.

    Returns:
        dash.Dash: L'application Dash avec le tableau de bord configuré.
    """

    # Initialisation de l'application Dash
    app = dash.Dash(__name__)

    # Crée un dictionnaire de graphiques basé sur les données fournies
    graph_dict = create_graphs_dict(df)

    # Layout de l'application Dash
    app.layout = html.Div(
        className='fullscreen',
        style={'backgroundColor': '#1f2630', 'color': '#ecf0f1'},
        children=[
            html.H2(
                children='How start-up succeed in America',
                style={'text-align':'center','font-family': 'Arial, sans-serif','padding-top':'20px','color':'#01B8AA'}),

            html.Div([
                html.Div(
                    [
                    dcc.Dropdown(
                    id="map-selector",
                    options=[
                        {"label": "Number of start-ups by region", "value": "startups"},
                        {"label": "Average Relationships of start-ups by region", "value": "relationships"},
                        {"label": "Start-up Success Ratio per Region", "value": "success_ratio"},
                    ],
                    value="startups",
                    style={'backgroundColor': '#252e3f', 'color': '#01B8AA','margin-right': '270px','padding-left':'250px','font-family': 'Arial, sans-serif'}
                )],
                style={'padding-top':'25px','padding-bottom':'25px'}
                ),
                html.Iframe(
                    id="map-container",
                    width="80%",
                    height="400px",  # Réduit la hauteur de l'iframe
                    srcDoc=map_dict["startups"].get_root().render(),
                    style={'display': 'block', 'margin':'auto'}
                )
                ],
                style={'backgroundColor': '#252e3f','margin-left': '15px','margin-right':'15px'},
            ),
            html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(
                            id="histogram-container",
                            figure=barSector(df)
                        ),
                    ],
                    style={'width': '48%', 'display': 'inline-block','backgroundColor': '#1f2630', 'color': '#01B8AA','margin-left': '17px','padding-bottom':'50px','font-family': 'Arial, sans-serif'},
                ),
                html.Div(
                    [   
                        html.Div(
                            children =[dcc.Dropdown(
                                id="graph-selector",
                                options=[
                                    {"label": key, "value": key} for key in graph_dict.keys()
                                ],
                                value=list(graph_dict.keys())[0],
                                style={'backgroundColor': '#252e3f', 'color': '#01B8AA','font-family': 'Arial, sans-serif','margin-right': '140px','padding-left':'100px'},
                            )],
                            style={'backgroundColor': '#252e3f','padding-top':'20px'}
                        ),
                        dcc.Graph(
                            id="graph-container1",
                        ),
                    ],
                    style={'width': '48%', 'display': 'inline-block','backgroundColor': '#1f2630', 'color': '#01B8AA', 'margin-left': '20px', 'padding-bottom': '13px','padding-top':'20px'},
                ),
            ],
        ),
        ],
    )

   # Callback pour mettre à jour la carte en fonction de la sélection de l'utilisateur
    @app.callback(
        Output("map-container", "srcDoc"),
        [Input("map-selector", "value")],
    )
    def update_map(selected_map):
        """Mise à jour de la carte en fonction de la sélection de l'utilisateur.

        Args:
            selected_map (str): La clé de la carte sélectionnée dans map_dict.

        Returns:
            str: Le HTML rendu de la carte sélectionnée.
        """
        return map_dict[selected_map].get_root().render()

    # Callback pour mettre à jour le graphique en fonction de la sélection de l'utilisateur
    @app.callback(
        Output("graph-container1", "figure"),
        [Input("graph-selector", "value")],
    )
    def update_graph(selected_graph):
        """Mise à jour du graphique en fonction de la sélection de l'utilisateur.

        Args:
            selected_graph (str): La clé du graphique sélectionné dans graph_dict.

        Returns:
            dict: L'objet figure du graphique sélectionné.
        """
        if selected_graph in graph_dict:
            fig1 = graph_dict[selected_graph]
        else:
            fig1 = {}
        return fig1

    return app


if __name__ == "__main__":
    # Charger les données géographiques des startups
    startUp_data = get_geodata()

    # Charger et traiter les données des startups à partir du fichier CSV
    file_path = "startup_data.csv"
    df = open_and_process_data(file_path)

    # Créer un dictionnaire de cartes basé sur les données géographiques
    map_dict = create_3maps_dict(startUp_data)

    # Initialiser le tableau de bord Dash
    app = create_dashboard(map_dict, df)

    # Exécuter l'application Dash
    app.run_server(debug=True)


