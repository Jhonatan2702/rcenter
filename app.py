import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Confirmação das bibliotecas importadas
print("As bibliotecas foram importadas com sucesso!")

# Inicialização do app Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

# Criação de um menu dropdown
dropdown = dbc.DropdownMenu(
    label="Menu",
    children=[
        dbc.DropdownMenuItem("Resumo", href="/"),
        dbc.DropdownMenuItem("Rotas", href="/rotas"),
        dbc.DropdownMenuItem("Transferências", href="/transferencias"),
        dbc.DropdownMenuItem("Estoque", href="/estoque"),
    ],
    nav=True,
    in_navbar=True,
)

# Layout do aplicativo com a logo no Navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.Navbar(
        dbc.Container([
            dbc.Row([
                dbc.Col(
                    html.A(
                        html.Img(src=app.get_asset_url('logo.png'), height="40px"),
                        href="/"
                    ),
                    width="auto"
                ),
                dbc.Col(
                    dbc.NavbarBrand(" ", className="ms-2")
                ),
                dbc.Col(
                    dbc.Nav(
                        [dropdown],
                        className="ms-auto",
                        navbar=True
                    ),
                    width="auto"
                )
            ], align="center", className="g-0"),
        ], fluid=True),
        color="primary",
        dark=True,
    ),
    html.Div(
        id="page-content",
        style={"margin": "20px"}
    )
])

# Callbacks para navegação
@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/rotas":
        return html.Div("Esta é a página de Rotas")
    elif pathname == "/transferencias":
        return html.Div("Esta é a página de Transferências")
    elif pathname == "/estoque":
        return html.Div("Esta é a página de Estoque")
    else:
        return html.Div("Esta é a página de Resumo")

# Rodando o servidor
if __name__ == "__main__":
    print("Rodando o servidor...")
    app.run_server(debug=True, host='0.0.0.0')
