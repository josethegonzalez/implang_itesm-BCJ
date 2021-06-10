import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import dash_cytoscape as cyto  # pip install dash-cytoscape==0.2.0 or higher
from dash.dependencies import Input, Output
import math
from dash import no_update
import plotly.offline as offline

import dash_table


import callbacks


df_final_2020 = pd.read_csv('df_final_2020.csv')
df_final_2020.set_index('RML')
df_final_2011 = pd.read_csv('df_final_2011.csv')
df_final_2011.set_index('RML')
df_SUELOS_PIVOT = pd.read_csv('df_SUELOS_PIVOT.csv')

df_final_2020['geometry'] = gpd.GeoSeries.from_wkt(df_final_2020['geometry'])
df_final_2020 = gpd.GeoDataFrame(df_final_2020, geometry='geometry')
df_final_2011['geometry'] = gpd.GeoSeries.from_wkt(df_final_2011['geometry'])
df_final_2011 = gpd.GeoDataFrame(df_final_2011, geometry='geometry')

final_2v = pd.read_csv('PoblacionFinal.csv')
df_denue = pd.read_csv('df_denue.csv')

app = dash.Dash(__name__, title='Instituto Municipal de Planeación y Gestión Urbana - IMPLANG', external_stylesheets=[dbc.themes.BOOTSTRAP],
				meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])



server = app.server


# Connect to app pages

from apps import home, itesm



# App Layout

app.layout = dbc.Container([

	dbc.NavbarSimple(
		[

        	dbc.Button('ITESM', href='/apps/itesm', color='light'),

		],
		brand='IMPLANG',
		brand_href='/apps/home'
	),

	html.Div(id='page-content', children=[]),
	dcc.Location(id='url', refresh=False)

])


@app.callback(Output(component_id='page-content', component_property=
					'children'),
			[Input(component_id='url', component_property='pathname')])

def display_page(pathname):
	if pathname == '/apps/itesm':
		return itesm.layout
	else:
		return home.layout

@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='dropdown1', component_property='value'))
def update_output(edad2):
    #fig = px.bar(df_denue, x = comercios, y = [1]*len(comercios))

    tryout2 = final_2v[final_2v['Age_Range'] == edad2]
    v_2010 = tryout2[tryout2['Año'] == 2010]['Población'].to_list()[0]
    v_2020 = tryout2[tryout2['Año'] == 2020]['Población'].to_list()[0]

    percentage = round(((v_2020-v_2010)/v_2010)*100,2)
    pos = ''

    if percentage < 0:
        pos = 'menos'
    else:
        pos = 'más'

    return 'Diferencia en 10 años: {}% '.format(percentage)



@app.callback(
    Output(component_id='my_graph',component_property= 'figure'),
    Input(component_id='dropdown1',component_property= 'value'))
def update_output(edad):
    #fig = px.bar(df_denue, x = comercios, y = [1]*len(comercios))

    tryout = final_2v[final_2v['Age_Range'] == edad]

    fig = go.Figure(data=[go.Bar(
            x=tryout['Año'].to_list(),
            y=tryout['Población'].to_list(),
            text=tryout['Población'].to_list(),
            textposition='auto',
            #marker_color = '#aac2de',
        )])

    fig.update_layout(plot_bgcolor='white')
    return fig

@app.callback(
    Output('my_map', 'figure'),
    Input('dropdown2', 'value'),
)
def update_output(comercios):
    #fig = px.bar(df_denue, x = comercios, y = [1]*len(comercios))


    fig_d = px.scatter_mapbox(df_denue[df_denue['Clasificador'].isin(comercios)], lat="latitud", lon="longitud", hover_name="Clasificador",
                        color_discrete_sequence=["black"], zoom=12, height=600, animation_frame='Año',custom_data=['Clasificador'])

    fig_d.update_layout(mapbox_style="carto-positron")
    fig_d.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_d.update_traces(hovertemplate = "%{customdata[0]}")

    return fig_d

#CLOROPLETH

@app.callback(
    Output('my_map3', 'figure'),
    Input('dropdown3', 'value'),
)
def update_output(zona):

    to_figure = df_final_2020[df_final_2020['ZONA'] == zona]
    lon = 0
    lat = 0

    if zona == 'Valle Oriente':
        lon = -100.33
        lat = 25.648
    elif zona == 'Casco Urbano':
        lon = -100.4025
        lat = 25.6573
    elif zona == 'Centrito':
        lon = -100.366
        lat = 25.66
    else:
        lon = -100.402428
        lat = 25.664909

    fig_d = px.choropleth_mapbox(to_figure, geojson=to_figure.geometry, locations = to_figure.index,
    color=to_figure.Categoria, zoom=13.5, center = {"lat": lat, "lon": lon},
    #animation_frame = 'Year',
    color_discrete_map={
        'ABANDONADA'  : 'rgb(204,102,0)',
        'AREA NATURAL PROTEGIDA': 'rgb(153,255,204)',
        'BALDIO NO URBANO': 'rgb(153,76,0)',
        'BALDIO URBANO' : 'rgb(102,51,0)',
        'COMERCIO'  : 'rgb(255,0,0)',
        'DERECHO DE PASO' : 'rgb(229,204,255)',
        'ESPACIOS ABIERTOS' : 'rgb(204,255,153)',
        'EN CONSTRUCCION' : 'rgb(153,153,0)',
        'EQUIPAMIENTO PRIVADO' : 'rgb(128,128,128)',
        'EQUIPAMIENTO URBANO' : 'rgb(160,160,160)',
        'HABITACIONAL MULTIFAMILIAR' : 'rgb(255,165,0)',
        'HABITACIONAL UNIFAMILIAR' : '#FFFD82',
        'INFRAESTRUCTURA' : 'rgb(102,0,51)',
        'INDUSTRIA': 'rgb(102,102,255)',
        'HABITACIONAL CON COMERCIO O SERVICIOS' : 'rgb(255,153,153)',
        'COMERCIOS Y SERVICIOS' : 'rgb(255,51,51)',
        'PRESERVACION ECOLOGICA': 'rgb(255,165,0)',
        'RIO': 'rgb(0,0,255)',
        'SERVICIOS'  : 'rgb(255,51,51)'})
    #No tiene color: Baldio no urbano, baldio urbano, derecho de paso, contruccion, Equipamiento urbano y publico, infraestructura, habitacional con comercio,
    fig_d.update_layout(mapbox_style="carto-positron")
    fig_d.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_d.update_layout(showlegend=False)

    return fig_d

@app.callback(
    Output('my_map_2', 'figure'),
    Input('dropdown3', 'value'),
)
def update_output2(zona):

    to_figure = df_final_2011[df_final_2011['ZONA'] == zona]
    lon = 0
    lat = 0

    if zona == 'Valle Oriente':
        lon = -100.33
        lat = 25.648
    elif zona == 'Casco Urbano':
        lon = -100.4025
        lat = 25.6573
    elif zona == 'Centrito':
        lon = -100.366
        lat = 25.66
    else:
        lon = -100.402428
        lat = 25.664909

    fig_d = px.choropleth_mapbox(to_figure, geojson=to_figure.geometry, locations = to_figure.index,
    color=to_figure.Categoria, zoom=13.5, center = {"lat": lat, "lon": lon},
    #animation_frame = 'Year',
    color_discrete_map={
        'ABANDONADA'  : 'rgb(204,102,0)',
        'AREA NATURAL PROTEGIDA': 'rgb(153,255,204)',
        'BALDIO NO URBANO': 'rgb(153,76,0)',
        'BALDIO URBANO' : 'rgb(102,51,0)',
        'COMERCIO'  : 'rgb(255,0,0)',
        'DERECHO DE PASO' : 'rgb(229,204,255)',
        'ESPACIOS ABIERTOS' : 'rgb(204,255,153)',
        'EN CONSTRUCCION' : 'rgb(153,153,0)',
        'EQUIPAMIENTO PRIVADO' : 'rgb(128,128,128)',
        'EQUIPAMIENTO URBANO' : 'rgb(160,160,160)',
        'HABITACIONAL MULTIFAMILIAR' : 'rgb(255,165,0)',
        'HABITACIONAL UNIFAMILIAR' : '#FFFD82',
        'INFRAESTRUCTURA' : 'rgb(102,0,51)',
        'INDUSTRIA': 'rgb(102,102,255)',
        'HABITACIONAL CON COMERCIO O SERVICIOS' : 'rgb(255,153,153)',
        'COMERCIOS Y SERVICIOS' : 'rgb(255,51,51)',
        'PRESERVACION ECOLOGICA': 'rgb(255,165,0)',
        'RIO': 'rgb(0,0,255)',
        'SERVICIOS'  : 'rgb(255,51,51)'})
    #No tiene color: Baldio no urbano, baldio urbano, derecho de paso, contruccion, Equipamiento urbano y publico, infraestructura, habitacional con comercio,
    fig_d.update_layout(mapbox_style="carto-positron")
    fig_d.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig_d.update_layout(showlegend=False)

    return fig_d


@app.callback(
    Output('bargraph', 'figure'),
    Input('dropdown3', 'value'),
)
def update_output3(zona):

    df_bar = df_SUELOS_PIVOT[df_SUELOS_PIVOT['ZONA'] == zona]

    #bar = px.bar(df_bar, x= 'Categoria', y = 'Value', color = 'Year', barmode="group")

    bar_2011 = df_bar[df_bar['Year'] == 2011]['Value']
    bar_2011 = bar_2011.to_list()

    bar_2020 = df_bar[df_bar['Year'] == 2020]['Value']
    bar_2020 = bar_2020.to_list()

    bar = go.Figure(data=[
        go.Bar(name='2011', x=df_bar['Categoria'].unique().tolist(), y=bar_2011, text =bar_2011 ,  textposition='auto'),
        go.Bar(name='2020', x=df_bar['Categoria'].unique().tolist(), y=bar_2020, text = bar_2020, textposition='auto', marker_color = '#CFD674')
    ])
    
    # Change the bar mode
    bar.update_layout(barmode='group')
    bar.update_layout(plot_bgcolor='white')

    return bar

app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
	app.run_server(debug=True)


