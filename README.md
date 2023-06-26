Leitor de Vendas no MySQL com Função de Fala
Este projeto consiste em uma aplicação de Inteligência Artificial (IA) que realiza a leitura de vendas armazenadas em um banco de dados MySQL e é capaz de fornecer a informação por meio de uma saída de voz. Essa aplicação é útil para automatizar a leitura de dados de vendas e fornecer informações de forma auditiva, tornando-a acessível a pessoas com deficiência visual ou para situações em que a leitura visual não é possível ou conveniente.

Funcionalidades
Conexão com banco de dados MySQL: A aplicação se conecta ao banco de dados MySQL para obter as informações das vendas.
Leitura dos dados de vendas: A IA lê as informações relevantes das vendas, como nome do cliente, valor total da venda, data e produtos vendidos.
Síntese de voz: A aplicação converte as informações lidas em voz, permitindo que sejam ouvidas pelo usuário.
Interface de linha de comando (CLI): A interação com a aplicação é realizada por meio de comandos digitados no terminal.
Requisitos
Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

Python 3.x
Biblioteca MySQL Connector/Python: Instale utilizando o comando pip install mysql-connector-python.
Biblioteca pyttsx4: Instale utilizando o comando pip install pyttsx4.
Configuração
Antes de executar a aplicação, é necessário realizar algumas configurações:

Certifique-se de ter um servidor MySQL em execução e tenha as credenciais de acesso (host, usuário, senha, nome do banco de dados).
Abra o arquivo db_config.py e atualize as variáveis host, user, password e database com as informações do seu banco de dados.
Utilização
No terminal, navegue até o diretório onde os arquivos da aplicação estão localizados.
Execute o comando python main.py para iniciar a aplicação.
Siga as instruções exibidas na tela para interagir com a aplicação. Por exemplo, você pode usar o comando ler vendas para que a IA leia as informações de vendas armazenadas no banco de dados.
Limitações
Este projeto foi desenvolvido para ler informações de vendas específicas armazenadas em um banco de dados MySQL. Se você deseja adaptá-lo para ler outros tipos de informações ou usar outros bancos de dados, será necessário fazer ajustes no código.
A síntese de voz é realizada por meio do serviço gTTS, que requer uma conexão com a internet. Certifique-se de estar conectado para que a função de fala funcione corretamente.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para enviar sugestões, relatar problemas ou enviar pull requests para aprimorar este projeto.

Licença
Este projeto está licenciado sob a MIT License.