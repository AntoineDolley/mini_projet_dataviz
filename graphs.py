import plotly.express as px
import plotly

def histofunding(df) -> plotly.graph_objs:
    """
    Crée un histogramme de la répartition des fonds selon le statut des entreprises.

    Args:
        df (pd.DataFrame): Les données à visualiser.

    Returns:
        plotly.graph_objs.Figure: L'objet figure contenant l'histogramme.
    """

    colors = {
    'background': '#111111',
    'text': '#7FDBFF'
    }

    # Définir les valeurs de graduation pour l'axe x
    tickvaleurs = [0,4000000,8000000, 12000000,16000000, 20000000, 30000000, 40000000, 50000000,60000000,70000000,80000000]

    # Créer l'histogramme
    fig = px.histogram(df,x='new_total_funding_usd',color='status',color_discrete_map={'success': '#4831D4', 'closed': '#FF69B4'})

    # Mettre à jour les graduations de l'axe x
    fig.update_xaxes(tickvals=tickvaleurs, ticktext=['0','4M','8M','12M','16M','20M','30M','40M','50M','60M','70M','>80M'],tickmode='array')

    # Mettre à jour la taille des barres
    fig.update_traces(xbins_size=4000000)

    # Mettre à jour le titre de l'axe x et les couleurs de fond
    fig.update_xaxes(title_text='Funding Total (USD)')
    fig.update_layout(
    plot_bgcolor='#34495e',   # Dark background for the plot
    paper_bgcolor='#252e3f',  # Dark background surrounding the plot
    font=dict(color='#01B8AA')  # Light font color
    )
    return fig

def barSector(df) -> plotly.graph_objs.Figure:
    """
    Crée un graphique en barres de la proportion d'entreprises acquises par secteur.

    Args:
        df (pd.DataFrame): Les données à visualiser.

    Returns:
        plotly.graph_objs.Figure: L'objet figure contenant le graphique en barres.
    """
    # Calculer la proportion d'entreprises acquises par secteur
    category_proportions = df.groupby('Sector')['status'].apply(lambda x: (x == 'success').mean()).reset_index(name='proportion')

    # Créer le graphique en barres
    fig = px.bar(
        category_proportions, x='Sector', y='proportion',
        labels={'new_total_funding_usd': 'Funding Total (en USD)'},
        color='Sector',
        title='Proportion of successful Companies by Sector',
    )
    fig.update_layout(
    plot_bgcolor='#34495e',   # Dark background for the plot
    paper_bgcolor='#252e3f',  # Dark background surrounding the plot
    font=dict(color='#01B8AA')  # Light font color
    )
    return fig

def historelation(df) -> plotly.graph_objs.Figure:
    """
    Crée un histogramme de la répartition des relations selon le statut des entreprises.

    Args:
        df (pd.DataFrame): Les données à visualiser.

    Returns:
        plotly.graph_objs.Figure: L'objet figure contenant l'histogramme.
    """
    # Créer l'histogramme
    fig = px.histogram(df,x='relationships',color='status',color_discrete_map={'success': '#4831D4', 'closed': '#FF69B4'})

    # Mettre à jour la taille des barres
    fig.update_traces(xbins_size=2)
    fig.update_layout(
    plot_bgcolor='#34495e',   # Dark background for the plot
    paper_bgcolor='#252e3f',  # Dark background surrounding the plot
    font=dict(color='#01B8AA')  # Light font color
    )
    return fig



def create_graphs_dict(df) -> dict:
    """
    Crée un dictionnaire de graphiques à partir des données fournies.

    Args:
        df (pd.DataFrame): Les données à visualiser.

    Returns:
        dict: Un dictionnaire contenant les graphiques.
    """
    histo_dict = {
        'Réussite par fonds': histofunding(df),
        'Réussite par relation': historelation(df),
    }
    return histo_dict
