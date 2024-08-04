import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import requests

# Função para ler dados da planilha
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Função para buscar dados de uma API (exemplo)
def fetch_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()

# Criação do aplicativo Dash
app = Dash(__name__)

# Layout do dashboard
app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Arraste e solte ou ',
            html.A('Selecione um arquivo')
        ]),
        style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed',
            'borderRadius': '5px', 'textAlign': 'center', 'margin': '10px'
        },
        multiple=False
    ),
    dcc.Input(id='api-url', type='text', placeholder='Digite a URL da API', style={'width': '50%'}),
    html.Button('Buscar API', id='fetch-api', n_clicks=0),
    dcc.Graph(id='graph'),
    html.Div(id='output-data-upload'),
])

# Callback para atualizar o gráfico com dados da planilha
@app.callback(
    Output('graph', 'figure'),
    Input('upload-data', 'contents'),
    Input('fetch-api', 'n_clicks'),
    [Input('api-url', 'value')]
)
def update_output(file_contents, n_clicks, api_url):
    if file_contents:
        # Ler dados da planilha
        content_type, content_string = file_contents.split(',')
        decoded = base64.b64decode(content_string)
        df = pd.read_excel(io.BytesIO(decoded))
    elif n_clicks > 0 and api_url:
        # Buscar dados da API
        df = fetch_api_data(api_url)
    else:
        df = pd.DataFrame()

    if not df.empty:
        # Criar um gráfico de exemplo
        fig = px.line(df, x=df.columns[0], y=df.columns[1])
    else:
        fig = {}

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
