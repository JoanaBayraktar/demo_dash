from dash import Dash, html, dcc, Input, Output, dash_table
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Import Datasets
pa = pd.read_csv("party_attention.csv", sep=",")
fig = px.bar(pa, x="Partei", y="Anzahl", title="Wie oft wurden die Parteien erwähnt?")

dfCSU = pd.read_csv("CSU.csv", sep=",")
dfSPD = pd.read_csv("SPD.csv", sep=",")
dfFDP = pd.read_csv("FDP.csv", sep=",")
dfGRÜNE = pd.read_csv("GRÜNE.csv", sep=",")
dfAfD = pd.read_csv("AfD.csv", sep=",")
dfFW = pd.read_csv("FW.csv", sep=",")

CSU = dash_table.DataTable(
    data=dfCSU.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfCSU.columns],
    style_table={'height': '300px', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12}
)

SPD = dash_table.DataTable(
    data=dfSPD.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfSPD.columns],
    style_table={'height': '300px', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12}
)

FW = dash_table.DataTable(
    data=dfFW.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfFW.columns],
    style_table={'height': '300px', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12},
)

GRÜNE = dash_table.DataTable(
    data=dfGRÜNE.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfGRÜNE.columns],
    style_table={'height': '300px', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12}
)

FDP = dash_table.DataTable(
    data=dfFDP.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfFDP.columns],
    style_table={'height': '300px', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12}
)

AfD = dash_table.DataTable(
    data=dfAfD.to_dict('records'),
    columns=[{'id': c, 'name': c} for c in dfAfD.columns],
    style_table={'height': '300px', 'maxWidth': '110%', 'overflowX': 'auto'},
    style_cell={'textAlign': 'left', 'fontSize': 12, 'overflow': 'hidden'}
)

app = Dash(external_stylesheets=[dbc.themes.LUMEN])

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Medien Monitor Bayern",
    brand_href="#",
    color="primary",
    dark=True,
)



# ------------ APP LAYOUT ----------------------------------------------

app.layout = html.Div(children=[
    navbar,

    dbc.Row(
        [
            dbc.Col(
                html.H1("Herzlich Willkommen!")
            )
        ], className="m-3"
    ),

    dbc.Row(
            [
                dbc.Col(html.Div(
                    dcc.Graph(
                        id='example-graph-2',
                        figure=fig),
                    ),
                    lg=5
                    ,
                    className="bg-light border"),
                dbc.Col(html.Div("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."), className="bg-light border"),
            ], className="m-3"),

    dbc.Row(
        [dbc.Col(html.H5("Artikel, in denen die jeweilige Partei erwähnt wird"), className="mt-4 mx-4"
        ),
            dcc.Dropdown(['CSU', 'SPD', 'GRÜNE', 'FW', 'AfD', 'FDP'], id='demo-dropdown', className="m-4"),

            html.Div(id='dd-output-container',
                     className="m-4")

        ], className="m-3 bg-light", justify="center"),



])


# -------------- Call Backs -----------------------------------------
@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output(value):
    var = value
    if value == "CSU":
        return CSU
    elif value == "SPD":
        return SPD
    elif value == "GRÜNE":
        return GRÜNE
    elif value == "FW":
        return FW
    elif value == "AfD":
        return AfD


if __name__ == '__main__':
    app.run_server(debug=False)
