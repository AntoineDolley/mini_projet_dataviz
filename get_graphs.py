import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from plotly import graph_objs as go 
import plotly.graph_objects as go
import numpy as np
from dash.dependencies import Input, Output

"""colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}"""

def histofunding(df,colors):
    df['new_total_funding_usd'] = df['funding_total_usd'].apply(lambda x: 80000000 if x >= 80000000 else x)
    
    tickvaleurs = [0,4000000,8000000, 12000000,16000000, 20000000, 30000000, 40000000, 50000000,60000000,70000000,80000000]

    fig = px.histogram(df,x='new_total_funding_usd',color='status',color_discrete_map={'acquired': '#4831D4', 'closed': '#FF69B4'})

    fig.update_xaxes(tickvals=tickvaleurs, ticktext=['0','4M','8M','12M','16M','20M','30M','40M','50M','60M','70M','>80M'],tickmode='array')
    fig.update_traces(xbins_size=4000000)
    fig.update_xaxes(title_text='Funding Total (USD)')
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'])
    return fig



def barSector(df):
    category_proportions = df.groupby('Sector')['status'].apply(lambda x: (x == 'acquired').mean()).reset_index(name='proportion')
    px.bar(category_proportions, x='Sector', y='proportion',
                              labels={'new_total_funding_usd': 'Funding Total (en USD)'},
                              color='Sector',
                              title='Proportion of Acquired Companies by Sector',
                              )