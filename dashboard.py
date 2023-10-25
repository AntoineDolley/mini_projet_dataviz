import dash
from dash import dcc, html, Input, Output
from map_visualization import create_3maps_dict
from generate_geodata import get_geodata
from get_graphs import create_graphs_dict,barSector
from get_data import open_and_process_data

def create_dashboard(map_dict, graph_dict) -> dash.Dash:
    app = dash.Dash(__name__)

    app.layout = html.Div(style={'backgroundColor': '#1f2630', 'color': '#ecf0f1'},
        children=[
            html.H2(children='How start-up succeed in America'),

            dcc.Dropdown(
                id="map-selector",
                options=[
                    {"label": "General Data", "value": "startups"},
                    {"label": "Average Relationships", "value": "relationships"},
                    {"label": "Start-up Success Ratio per Region", "value": "success_ratio"},
                ],
                value="startups",
                style={'backgroundColor': '#252e3f', 'color': '#ecf0f1',},
            ),
            html.Div(
                [
                html.Iframe(
                    id="map-container",
                    width="80%",
                    height="400px",  # Réduit la hauteur de l'iframe
                    srcDoc=map_dict["startups"].get_root().render(),
                    style={'display': 'block', 'margin': 'auto'}
                )
                ],
                style={'backgroundColor': '#252e3f'}
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
                    style={'width': '50%', 'display': 'inline-block','backgroundColor': '#2c3e50', 'color': '#ecf0f1'},
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            id="graph-selector",
                            options=[
                                {"label": key, "value": key} for key in graph_dict.keys()
                            ],
                            value=list(graph_dict.keys())[0],
                            style={'backgroundColor': '#252e3f', 'color': '#ecf0f1'},
                        ),
                        dcc.Graph(
                            id="graph-container1",
                        ),
                    ],
                    style={'width': '50%', 'display': 'inline-block','backgroundColor': '#1f2630', 'color': '#ecf0f1'},
                ),
            ],
        ),
        ],
    )

    @app.callback(
        Output("map-container", "srcDoc"),
        [Input("map-selector", "value")],
    )
    def update_map(selected_map):
        return map_dict[selected_map].get_root().render()

    @app.callback(
        Output("graph-container1", "figure"),
        [Input("graph-selector", "value")],
    )
    def update_graph(selected_graph):
        if selected_graph in graph_dict:
            fig1 = graph_dict[selected_graph]
        else:
            fig1 = {}
        return fig1

    return app


if __name__ == "__main__":
    startUp_data = get_geodata()
    file_path = "startup_data.csv"
    df = open_and_process_data(file_path)
    map_dict = create_3maps_dict(startUp_data)
    graph_dict = create_graphs_dict(df)
    app = create_dashboard(map_dict, graph_dict)
    app.run_server(debug=True)
