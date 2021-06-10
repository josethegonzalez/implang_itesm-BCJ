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

df_denue_poranio = pd.read_csv('df_denue_poranio.csv')
fig_line = px.line(df_denue_poranio, x="Año", y='Num. Comercios', title='Cantidad de Comercios por Año')
fig_line.update_layout(plot_bgcolor='white')


from app import app

layout =html.Div([

    ####################################### COMIENZA ESPACIO DE EDICIÓN #######################################

    ## BANNER PRINCIPAL

    # SECCIÓN 1

       # dbc.Container([
       #  html.Br(),
       #  html.Br(),
       #  dbc.Row([

       #      dbc.Col(
       #          html.Div(
       #              html.A(dbc.Button("Comercios", outline = True, color="primary", block = True, className="mr-1"), href = '#seccion1'))
       #          ),
       #      dbc.Col(
       #          html.Div(
       #              dbc.Button("Población", outline = True, color="primary", block = True, className="mr-1"))
       #          ),
       #      dbc.Col(
       #          html.Div(
       #              dbc.Button("Usos de Suelo", outline = True, color="primary", block = True, className="mr-1", href = '#top'))
       #          )
       #      ]),
       #  html.Br(),
       #  html.Br(),
       #  ]),

    dbc.Container([

        ## Títutlo
        dbc.Row(
            dbc.Col(
                html.H1('Evolución del Municipio', style = {'text-align':'center'})
                ), className='px-1 pt-4 py-3'
            ),


        # dbc.Row([

        #     dbc.Col(
        #         html.Div(
        #             html.A(dbc.Button("Comercios", outline = True, color="primary", block = True, className="mr-1", style = {'background-color': '#3F698F', 'color': 'white', 'border': '0px'}), href = '#seccion1'))
        #         ),
        #     dbc.Col(
        #         html.Div(
        #             html.A(dbc.Button("Población", outline = True, color="primary", block = True, className="mr-1", style = {'background-color': '#3F698F', 'color': 'white', 'border': '0px'}), href = '#seccion2'))
        #         ),
        #     dbc.Col(
        #         html.Div(
        #             html.A(dbc.Button("Usos de Suelo", outline = True, color="primary", block = True, className="mr-1", style = {'background-color': '#3F698F', 'color': 'white', 'border': '0px'}), href = '#seccion3'))
        #         )
        #     ]),

        dbc.Row([

            dbc.Col(
                html.Div(
                    html.A(dbc.Button("Comercios", outline = True, color="dark", block = True, className="mr-1"), href = '#seccion1'))
                ),
            dbc.Col(
                html.Div(
                    html.A(dbc.Button("Población", outline = True, color="dark", block = True, className="mr-1"), href = '#seccion2'))
                ),
            dbc.Col(
                html.Div(
                    html.A(dbc.Button("Usos de Suelo", outline = True, color="dark", block = True, className="mr-1"), href = '#seccion3'))
                )
            ]),

        html.Br(),
        html.Br(),
        dbc.Row(
            dbc.Col([
            	#html.Img(src='../assets/st1.jpeg', style={'max-width':'110%', 'height':'auto'}),
                html.Img(src='../assets/st1.jpeg', style={'width':'auto', 'height':'auto'}),
                html.H2('San Pedro es una ciudad para todos',
                    style={'position': 'absolute', 'top': '50%', 'left': '50%',
                    'transform': 'translate(-50%, -50%)','color': 'white','text-align':'center'})
                ])
            )
        ]),

    # dbc.Container([

    #     dash_table.DataTable(
    #         id='table',
    #         columns=[{"name": i, "id": i} for i in final_2v.columns],
    #         data=final_2v.to_dict('records'),
    #         )


    #     ]),

    #'#f7f8f9'
    #

    dbc.Container([
        html.Br(),
        html.H2('  Incremento en Comercios', className='py-3', style = {'text-align':'center','background-color': '#A4C2DE', 'color': 'white'}, id = 'seccion1'),
        html.Br(),
        dbc.Row([
            dbc.Col(
                html.Img(src='../assets/st2.jpg', style={'max-width':'60%', 'height':'auto', 'align':'right'}),
                ),
            dbc.Col([

                html.H5('Georgia – 65+ años'),
                html.Br(),
                dcc.Markdown('En los últimos 10 años he notado más **tráfico y más edificios**. También he notado más parques y mejoras en pavimentación.'),
                dcc.Markdown('Vivir en San Pedro siempre ha sido más caro que otros municipios. Creo que actualmente hay más vivienda, pero si va **aumentando mucho el comercio**.'),
                dcc.Markdown('Lo que más me gusta de vivir en San Pedro es la seguridad que siento, que toda mi familia vive aquí, y que tenemos todo lo que necesitamos a la mano.'),
                #html.P('"En los últimos 10 años he notado más <b> tráfico y más edificios </b>. También he notado más parques y mejoras en pavimentación. Vivir en San Pedro siempre ha sido más caro que otros municipios. Creo que actualmente hay más vivienda, pero si va aumentando mucho el comercio. Lo que más me gusta de vivir en San Pedro es la seguridad que siento, que toda mi familia vive aquí, y que tenemos todo lo que necesitamos a la mano."'),
                ]),
            ]),
       	html.Br(),
        ]),


    dbc.Container([
    	html.Hr(),
    	html.H4('Observa los cambios en los comercios por ti mismo.', style = {'text-align':'center'}),
    	html.Br(),
        html.Div([

        	#html.H5('')

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
    	html.Br(),
    	html.Br(),
    	html.Br(),
    	html.Hr(),
    	html.H4('En 10 años, la cantidad de comercios ha incrementado en un 64%.', style = {'text-align':'center'}),
        html.Div([
         html.Div([

             dcc.Graph(
                 figure = fig_line
                 ),

             ])
         ])

    ]),


    # dbc.Container([
    #     html.Br(),
    #     html.Br(),
    #     html.Span([
    #         html.H5('¿Cuántos años tienes tu?'),
    #         # dbc.Row([
    #         #     dbc.Col([
    #         #         dcc.Graph(figure=fig)
    #         #         ], lg=6, md=4, sm=1),
    #         #     dbc.Col([
    #         #         dcc.Graph(figure=fig)
    #         #         ], lg=6, md=4, sm=1)
    #         #     ])
    #         ], id = 'seccion1'),
    #     html.Br(),
    #     html.Br(),
    #     ]),

    # dbc.Container([

    #     html.Div([

    #        html.Div([


    #           dcc.Dropdown(
    #            id = 'dropdown1',
    #            placeholder="Selecciona tu rango de edad",
    #            value = '0-14 años',
    #            options=[
    #            {'label': '0-14 años', 'value': '0-14 años'},
    #            {'label': '15-25 años', 'value': '15-25 años'},
    #            {'label': '25-64 años', 'value': '25-64 años'},
    #            {'label': '65 años y más', 'value': '65 años y más'},
    #            ],
    #            ),

    #           html.Br(),
    #           html.H6(children="callback not executed", id='my-output'),

    #           dcc.Graph(
    #            id = 'my_graph',
    #            figure = {}
    #            ),

    #           ])
    #        ])

    #     ]),

        dbc.Container([
            ## Texto
            html.Br(),
            html.Br(),
            html.H2('  Cambios en la Población', className='py-3', style = {'text-align':'center','background-color': '#A4C2DE', 'color': 'white'}, id = 'seccion2'),
            html.Br(),
            # dbc.Row([
            #     dbc.Col([
            #         html.H5('Daniela, 26-64 años'),
            #         html.Br(),
            #         html.P('"Últimamente si he notado cambios en San Pedro y en el costo de vivir en San Pedro. También creo que han cambiado los números de comercios y viviendas en los últimos años. Lo que más me gusta de vivir en San Pedro es la calidad de vida, la disponibilidad de servicios, comercios, y opciones."')
            #     ], className= 'px-5 py-4')
            #     ]),

            dbc.Row(
                dbc.Col([
                    html.Img(src='../assets/st5.jpg', style={'max-width':'100%', 'height':'auto', 'align':'right'}),
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

            	html.H5('Daniel – 25 a 64 años'),
                html.Br(),
                dcc.Markdown('En los últimos 10 años he notado cambios en San Pedro, ha incrementado el **costo de vivir** en el municipio.'),
                dcc.Markdown('Sí creo que han aumentado el número de comercios; así como **disminuido la cantidad de viviendas disponibles.**'),
                dcc.Markdown('Por esto, las casas son tan caras que **resulta casi inalcanzable comenzar una familia en San Pedro**. Las personas que llevan aquí más tiempo no tienen este problema.'),


  
                ]),
            dbc.Col(
                html.Img(src='../assets/st3.jpg', style={'max-width':'60%', 'height':'auto', 'align':'right'}),
                ),
            ])
        ]),


    dbc.Container([
        html.Br(),
        html.Br(),
        html.Hr(),
        html.Span([
            html.H4('¿Cuántos años tienes tu?', style = {'text-align':'center'}),
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
              html.H6(children="callback not executed", id='my-output', style = {'text-align':'center'}),

              dcc.Graph(
               id = 'my_graph',
               figure = {}
               ),

              ])
           ])

        ]),



    dbc.Container([
        html.Br(),
        html.Br(),
        html.Span([
            html.H2('  Usos de Suelo', className='py-3', style = {'text-align':'center','background-color': '#A4C2DE', 'color': 'white'})
            # dbc.Row([
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1),
            #     dbc.Col([
            #         dcc.Graph(figure=fig)
            #         ], lg=6, md=4, sm=1)
            #     ])
            ], id = 'seccion3'),
        html.Br(),
        ]),

    # dbc.Container([
    #         ## Texto
    #         # dbc.Row(
    #         #     dbc.Col([
    #         #         html.H5('Armando, 26-64 años'),
    #         #         html.Br(),
    #         #         html.P('"Últimamente he notado cambios en San Pedro y en el costo de vivir en San Pedro. Lo que más me gusta de vivir en San Pedro es la calidad de vida y seguridad."')
    #         #     ]), className='px-5 py-4'
    #         #     )
    #         # ]),

            dbc.Container([
            ## Texto
            dbc.Row(
                dbc.Col([
                    html.Img(src='../assets/stg7.png', style={'max-width':'100%', 'height':'auto'}),
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
                html.Img(src='../assets/st8.jpg', style={'max-width':'60%', 'height':'auto'}),
                ),
            dbc.Col([

            	html.H5('Natalia – 15 a 24 años'),
                html.Br(),
                dcc.Markdown('En **Centrito** encuentro **los mejores bares y antros** para salir con mis amigas.'),
                dcc.Markdown('Los nuevos centros comerciales en **Valle Oriente** es donde hay más **variedad de tiendas y restaurantes.**'),
                dcc.Markdown('En el **Casco Urbano** siempre encuentro cosas que no tienen en otros lugares; tal y como **antigüedades y experiencias únicas**.'),
           
                ]),
            ]),
            html.Br(),
            html.Br(),
            html.Br()
        ]),


    dbc.Container([
    html.Br(),
    html.Hr(),
    html.H4('Las zonas principales son las más afectadas.',style = {'text-align':'center'}),
    html.Br(),
    html.Br(),
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
                    ], lg=6, md=4, sm=1),
                dbc.Col([
                    dcc.Graph(
                    id = 'my_map_2',
                    figure = {}
                        )
                    ], lg=6, md=4, sm=1),
                ])
            ], id = 'seccion10'),

            dbc.Row([
                html.Br(),
                html.Br(),
                dbc.Col([
                    dbc.Row([
                    html.H6('Gráfica 2011')], justify="center", align="center")]),
                dbc.Col([
                    dbc.Row([
                    html.H6('Gráfica 2020')], justify="center", align="center")]),
                ]),

            html.Img(src='../assets/legend3.png', style={'max-width':'110%', 'height':'auto', 'align' :'center', 'text-align' :'center'}),

            html.Br(),
            html.Hr(),
            html.Br(),
            html.H4('Observa los cambios en los principales usos de suelo.',style = {'text-align':'center'}),
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



        # dbc.Container([
        # html.Br(),
        # html.Br(),
        # html.Span([
        #     html.H5('Evolución del Municipio'),
        #     dbc.Row([
        #         dbc.Col([
        #             dcc.Graph(figure=fig)
        #             ], lg=6, md=4, sm=1),
        #         dbc.Col([
        #             dcc.Graph(figure=fig)
        #             ], lg=6, md=4, sm=1)
        #         ])
        #     ], id = 'seccion1'),
        # html.Br(),
        # html.Br(),
        # ]),

        ## SECCION 2
        dbc.Container([
            # Título
            dbc.Row(
                dbc.Col(
                    html.H2(' ')
                    ),className='py-3', style={'background-color': 'grey','color': 'white'}
                ),

            ## Texto
            dbc.Row([
                dbc.Col([
                    html.H5('Alejandra – 65+ años'),
                    html.Br(),
                    dcc.Markdown('*Lo que más me gusta de vivir en San Pedro es todo el municipio, la belleza, la seguridad, el gobierno, la calidad de vida, entre muchas otras cosas.*')
                ], lg=6, md=9, sm=4 ),
                dbc.Col(
                    html.Img(src='../assets/st4.jpg', style={'max-width':'60%', 'height':'auto'}),
                ),

                ],className='py-3'),

            dbc.Row(
                dbc.Col(
                    html.H2(' ')
                    ),className='py-3', style={'background-color': 'grey','color': 'white'}
                ),
            html.Br(),
            html.Br(),

            dbc.Row([


                html.H4('Y tú, ¿qué municipio le quieres dejar a tu familia?')

                ], justify="center", align="center"),
            html.Br(),
            html.Br()
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

            ],style={'background-color': '#f7f8f9','color': 'black'}),

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
