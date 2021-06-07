import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import geopandas as gpd
import plotly.graph_objects as go
import dash_cytoscape as cyto  # pip install dash-cytoscape==0.2.0 or higher
from dash.dependencies import Output, Input
import math
from dash import no_update
import plotly.offline as offline

import dash_table


df_final_2020 = pd.read_csv('df_final_2020.csv')
df_final_2020.set_index('RML')
df_final_2011 = pd.read_csv('df_final_2011.csv')
df_final_2011.set_index('RML')
df_SUELOS_PIVOT = pd.read_csv('df_SUELOS_PIVOT.csv')

df_final_2020['geometry'] = gpd.GeoSeries.from_wkt(df_final_2020['geometry'])
df_final_2020 = gpd.GeoDataFrame(df_final_2020, geometry='geometry')
df_final_2011['geometry'] = gpd.GeoSeries.from_wkt(df_final_2011['geometry'])
df_final_2011 = gpd.GeoDataFrame(df_final_2011, geometry='geometry')

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

df_denue = pd.read_csv('df_denue.csv')

final_2v = pd.read_csv('PoblacionFinal.csv')
from app import app

layout =html.Div([

    ####################################### COMIENZA ESPACIO DE EDICIÓN #######################################

    ## BANNER PRINCIPAL

    # SECCIÓN 1
    dbc.Container([

        ## Títutlo
        dbc.Row(
            dbc.Col(
                html.H2('Evolución del Municipio')
                ), className='px-1 pt-4 py-3'
            ),


        dbc.Row(
            dbc.Col([
                html.Img(src='../assets/st1.jpeg', style={'max-width':'100%', 'height':'auto'}),
                html.H2('Una ciudad más inclusiva se está construyendo',
                    style={'position': 'absolute', 'top': '50%', 'left': '50%',
                    'transform': 'translate(-50%, -50%)','color': 'white','text-align':'center'})
                ])
            )
        ]),
    dbc.Container([
        html.Br(),
        html.Br(),
        dbc.Row([

            dbc.Col(
                html.Div(
                    html.A(dbc.Button("Ir a seccion 1", outline = True, color="primary", block = True, className="mr-1"), href = '#seccion1'))
                ),
            dbc.Col(
                html.Div(
                    dbc.Button("Ir a seccion 2", outline = True, color="primary", block = True, className="mr-1"))
                ),
            dbc.Col(
                html.Div(
                    dbc.Button("Ir a seccion 3", outline = True, color="primary", block = True, className="mr-1", href = '#top'))
                )
            ]),
        html.Br(),
        html.Br(),
        ]),

    # dbc.Container([

    #     dash_table.DataTable(
    #         id='table',
    #         columns=[{"name": i, "id": i} for i in final_2v.columns],
    #         data=final_2v.to_dict('records'),
    #         )


    #     ]),


    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col(
                html.Img(src='../assets/st2.jpg', style={'max-width':'100%', 'height':'auto'}),
                ),
            dbc.Col([
                html.H5('Titulo de testimonio 1'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')
                ]),
            ])
        ]),


    dbc.Container([
        html.Br(),
        html.Br(),
        html.Span([
            html.H5('Evolución del Municipio'),
            # dbc.Row([
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1),
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1)
            #     ])
            ], id = 'seccion1'),
        html.Br(),
        html.Br(),
        ]),

    dbc.Container([

        html.Div([

           html.Div([


              dcc.Dropdown(
               id = 'dropdown1',
               placeholder="Selecciona tu rango de edad",
               value = '0-14 años',
               options=[
               {'label': '0-14 años', 'value': '0-14 años'},
               {'label': '15-25 años', 'value': '15-25 años'},
               {'label': '25-64 años', 'value': '25-64 años'},
               {'label': '65 años y más', 'value': '65 años y más'},
               ],
               ),

              html.Br(),
              html.H6(children="callback not executed", id='my-output'),

              dcc.Graph(
               id = 'my_graph',
               figure = {}
               ),

              ])
           ])

        ]),

        dbc.Container([
            ## Texto
            dbc.Row(
                dbc.Col(
                    html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')
                    ), className='px-5 py-4'
                ),

            dbc.Row(
                dbc.Col([
                    html.Img(src='../assets/st5.jpg', style={'max-width':'100%', 'height':'auto'}),
                    html.H2('San Pedro sigue creciendo',
                        style={'position': 'absolute', 'top': '50%', 'left': '50%',
                        'transform': 'translate(-50%, -50%)'})
                    ], style={'color': 'white', 'position': 'relative', 'text-align': 'center'})
                )
            ]),

    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col([
                html.H5('Titulo de testimonio 2'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')
                ]),
            dbc.Col(
                html.Img(src='../assets/st3.jpg', style={'max-width':'100%', 'height':'auto'}),
                ),
            ])
        ]),

    dbc.Container([
     html.Div([

         html.Div(id='text-output'),

         dcc.Dropdown(
             id = 'dropdown3',
             placeholder="Selecciona la Zona a Filtrar",
             value = 'Casco Urbano',
             multi = False,
             options=[
                {'label': 'Valle Oriente', 'value': 'Valle Oriente'},
                {'label': 'Casco Urbano', 'value': 'Casco Urbano'},
                {'label': 'Centrito', 'value': 'Centrito'}
              ],
         ),

        html.Span([
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                    id = 'my_map3',
                    figure = {}
                        )
                    ], lg=5, md=2, sm=1),
                dbc.Col([
                    html.Img(src='../assets/Legend.png', style={'max-width':'200%', 'height':'auto'})
                    ], lg=1, md=1, sm=1),
                dbc.Col([
                    dcc.Graph(
                    id = 'my_map_2',
                    figure = {}
                        )
                    ], lg=5, md=2, sm=1),
                ])
            ], id = 'seccion10'),

            dbc.Row([
                html.Br(),
                html.Br(),
                dbc.Col([
                    dbc.Row([
                    html.H5('Gráfica 2011')], justify="center", align="center")]),
                dbc.Col([
                    dbc.Row([
                    html.H5('Gráfica 2020')], justify="center", align="center")]),
                ]),

            dbc.Row([
                dbc.Col([
                    dcc.Graph(
                        id = 'bargraph',
                        figure = {}
                     ),
                    ]),
                ]),

     ])
        ]),

    dbc.Container([
        html.Br(),
        html.Br(),
        html.Span([
            html.H5('Evolución del Municipio')
            # dbc.Row([
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1),
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1)
            #     ])
            ], id = 'seccion1'),
        html.Br(),
        html.Br(),
        ]),

    dbc.Container([

        html.Div([

         html.Div([


             html.Div(id='text-output'),

             dcc.Dropdown(
                 id = 'dropdown2',
                 placeholder="Selecciona los tipos de comercio a filtrar",
                 value = ['Comercio al por menor','Comercio al por mayor'],
                 multi = True,
                 options = [
                 {'label': clasi.capitalize(), 'value': clasi}
                 for clasi in sorted(df_denue['Clasificador'].unique().tolist())
                 ]
                 ),

             dcc.Graph(
                 id = 'my_map',
                 figure = {}
                 ),

             ])
         ])

        ]),

    dbc.Container([
            ## Texto
            dbc.Row(
                dbc.Col(
                    html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')
                    ), className='px-5 py-4'
                )
            ]),

            dbc.Container([
            ## Texto
            dbc.Row(
                dbc.Col([
                    html.Img(src='../assets/st6.jpg', style={'max-width':'100%', 'height':'auto'}),
                    html.H2('San Pedro sigue creciendo',
                        style={'position': 'absolute', 'top': '50%', 'left': '50%',
                        'transform': 'translate(-50%, -50%)'})
                    ], style={'color': 'white', 'position': 'relative', 'text-align': 'center'})
                )
            ]),

    dbc.Container([
        html.Br(),
        dbc.Row([
            dbc.Col(
                html.Img(src='../assets/st4.jpg', style={'max-width':'100%', 'height':'auto'}),
                ),
            dbc.Col([
                html.H5('Titulo de testimonio 2'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible. La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'),
                html.Br(),
                html.P('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.')
                ]),
            ]),
            html.Br(),
            html.Br(),
            html.Br()
        ]),

        dbc.Container([
        html.Br(),
        html.Br(),
        html.Span([
            html.H5('Evolución del Municipio'),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(figure=fig)
                    ], lg=6, md=4, sm=1),
                dbc.Col([
                    dcc.Graph(figure=fig)
                    ], lg=6, md=4, sm=1)
                ])
            ], id = 'seccion1'),
        html.Br(),
        html.Br(),
        ]),

        ## SECCION 2
        dbc.Container([
            # Título
            dbc.Row(
                dbc.Col(
                    html.H2('Otro ejemplo de título')
                    ),className='py-3', style={'background-color': 'black','color': 'white'}
                ),

            ## Texto
            dbc.Row([
                dbc.Col(
                    html.H5('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'), lg=3, md=9, sm=4
                    ),
                dbc.Col(
                    html.H5('La bicicleta tiene enormes beneficios no sólo para la salud sino también para el medio ambiente, ya que se trata de un medio de transporte que favorece la movilidad sostenible.'), lg=9, md=3, sm=8
                    ),
                ],className='py-3')

            ]),

        ######################################## TERMINA ESPACIO DE EDICIÓN ########################################

        # Footer
        dbc.Container([

            dbc.Row(
                dbc.Col(
                  html.H6('Envíanos un correo a implang@sanpedro.gob.mx')
                  ), className='px-1 pt-4'
                ),

            dbc.Row(
                dbc.Col([
                    html.A(
                        html.Img(src='../assets/instagram.png', style={'max-width':'85px', 'height':'34px'}),
                        href='https://www.instagram.com/implang_spgg/', target='blank'
                        ),

                    html.A(
                        html.Img(src='../assets/facebook.png', style={'max-width':'85px', 'height':'34px'}),
                        href='https://www.facebook.com/implangspgg', target='blank', className='pl-3'
                        ),

                    html.A(
                        html.Img(src='../assets/twitter.png', style={'max-width':'85px', 'height':'34px'}),
                        href='https://twitter.com/implang_spgg', target='blank', className='pl-3'
                        ),

                    html.A(
                        html.Img(src='../assets/youtube.png',style={'max-width':'85px', 'height':'34px'}),
                        href='https://www.youtube.com/channel/UCZwYFPh0dHnKhXqzaxlaqNg', target='blank',
                        className='pl-3'
                        )
                    ]), className='px-1 py-4'
                )

            ]),

        dbc.Container([

         dbc.Row(
            dbc.Col(
                html.H6('Instituto Municipal de Planeación y Gestión Urbana')
                ), className='px-1 pt-3'
            ),

         dbc.Row(
            dbc.Col(
                html.H6('San Pedro Garza García, Nuevo León, México')
                ), className='px-1 py-3'
            )

         ], style={'background-color': 'black','color': 'white'}
         )
        ])
