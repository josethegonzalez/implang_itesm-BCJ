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
        )])

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


app.config.suppress_callback_exceptions = True

if __name__ == '__main__':
	app.run_server(debug=True)


