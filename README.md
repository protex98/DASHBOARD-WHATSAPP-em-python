#Dashboard do WhatsApp Business
------------------------
Descrição
Este projeto é um dashboard interativo desenvolvido com Python, Dash e Plotly, destinado a monitorar e visualizar dados do WhatsApp Business em tempo real. O dashboard exibe informações sobre mensagens, novos contatos, saídas de contatos, grupos completados, e mais, tudo atualizado a cada minuto.
------------------------
Funcionalidades
Integração com a API do WhatsApp Business: Coleta dados reais sobre mensagens, contatos e grupos.
Visualização Interativa: Gráficos interativos que permitem uma análise detalhada dos dados.
Atualização Automática: O dashboard atualiza os dados automaticamente a cada minuto.
Filtros por Data: Permite filtrar e visualizar dados em intervalos de datas selecionados pelo usuário.
-------------------------
Gráficos Detalhados:
Número de Mensagens por Dia
Novos Contatos por Dia
Contatos que Saíram por Dia
Grupos Completados por Dia
Grupos com Mais Mensagens
Mensagens do Dia
--------------------------
Pré-requisitos
Antes de começar, certifique-se de ter o seguinte instalado:
--------------------------
Python 3.7 ou superior
Bibliotecas listadas em requirements.txt
-------------------------
Instalação
Clone o Repositório
----------------------------
git clone 
Crie e Ative um Ambiente Virtual
--------------------------
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as Dependências

bash
---------------------------
pip install -r requirements.txt
Configure as Variáveis de Ambiente

Crie um arquivo .env na raiz do projeto com as seguintes variáveis:

plaintext
---------------------------
WHATSAPP_API_URL=https://graph.facebook.com/v13.0/YOUR_PHONE_NUMBER_ID/messages
WHATSAPP_ACCESS_TOKEN=YOUR_ACCESS_TOKEN
Uso
Para iniciar o dashboard, execute:

bash
-----------------------------------
python main.py
O dashboard estará acessível em http://127.0.0.1:8050.
-----------------------------------
Estrutura do Projeto
plaintext
.
├── main.py              # Script principal para executar o dashboard
├── requirements.txt     # Lista de dependências do Python
└── README.md            # Este arquivo
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
--------------------------------
Licença
Este projeto está licenciado sob a MIT License.


