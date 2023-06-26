import mysql.connector
import speech_recognition as sr
import pyttsx4

# Configuração da conexão com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ordem",
    port=1308
)

r = sr.Recognizer()

engine = pyttsx4.init()


def get_sales(month, year):
    with mydb.cursor() as cursor:
        # Conta o número de vendas no mês e ano informados
        sql = "SELECT COUNT(*) FROM vendas WHERE MONTH(venda_data_emissao) = %s AND YEAR(venda_data_emissao) = %s"
        cursor.execute(sql, (month, year))
        num_vendas = cursor.fetchone()[0]

        # Obtém o produto mais vendido no mês e ano informados
        sql = "SELECT produtos.produto, SUM(movvendasp.quantidade) AS total_vendido \
               FROM movvendasp \
               INNER JOIN vendas ON vendas.id = movvendasp.id_venda \
               INNER JOIN produtos ON produtos.id = movvendasp.id_produto \
               WHERE MONTH(vendas.venda_data_emissao) = %s AND YEAR(vendas.venda_data_emissao) = %s \
               GROUP BY produtos.produto \
               ORDER BY total_vendido DESC LIMIT 1"
        cursor.execute(sql, (month, year))
        result = cursor.fetchone()
        if result is not None:
            produto_mais_vendido, quantidade = result
            engine.say(
                f"O produto mais vendido em {month}/{year} foi {produto_mais_vendido}, com {quantidade} unidades vendidas.")
        else:
            engine.say(
                f"Não foi encontrado nenhum produto vendido em {month}/{year}.")

        # Fala o número de vendas
        engine.setProperty(
            'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')
        engine.say(f"Vendemos {num_vendas} produtos no mês {month} de {year}")
        engine.runAndWait()


engine.setProperty('rate', 200)
while True:
    with sr.Microphone() as source:
        print("Diga o mês e o ano para obter as vendas:")
        audio = r.listen(source)
    try:
        # Reconhecimento do que foi dito
        text = r.recognize_google(audio, language='pt-BR')
        print(f"Você disse {text}")

        # Tratamento da entrada do usuário
        month = None
        year = None
        for word in text.split():
            if word.isnumeric():
                if len(word) == 4:
                    year = word
                else:
                    month = word.lower()

        # Verificação se mês e ano foram encontrados
        if not month or not year:
            raise ValueError("Mês ou ano não foram identificados")

        get_sales(month, year)
    except sr.UnknownValueError:
        # print("Não entendi o que você disse")
        engine.say(
            "Desculpe, não entendi o que você disse. Por favor, tente novamente.")
        engine.runAndWait()
    except sr.RequestError as e:
        print(f"Erro ao reconhecer a fala: {e}")
        engine.say(
            "Desculpe, ocorreu um erro ao reconhecer a sua voz. Por favor, tente novamente.")
        engine.runAndWait()
    except ValueError as e:
        print(e)
        engine.say(
            "Desculpe, não foi possível identificar o mês ou ano. Por favor, tente novamente.")
        engine.runAndWait()
