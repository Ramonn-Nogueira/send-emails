import csv
from email.message import Message
import smtplib

lista_amigos = []
corpo_email = ''

with open('index.html', 'r', encoding='utf-8') as index:
    corpo_email = index.read()

def recuperarEmail(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        linhas = csv.reader(arquivo)

        for linha in linhas:
            lista_amigos.append(linha)

    lista_amigos.pop(0)


def enviar_email_smtp(corpo_email_envio, email_to):
    mensagem = Message()
    mensagem['Subject'] = "Hello"
    mensagem['From'] = 'EXEMPLO@gmail.com'
    mensagem['To'] = email_to
    password = 'SENHA'
    mensagem.add_header('Content-Type', 'text/html')
    mensagem.set_payload(corpo_email_envio)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login
    s.login(mensagem['From'], password)
    s.sendmail(mensagem['From'], [mensagem['To']], mensagem.as_string().encode('utf-8'))
    print('Email enviado')


def enviar_email():
    for i in lista_amigos:
        hello_friend = i[0].replace(';', ',').split(',')
        paragrafo = '<p>Nome: {}'

        corpo = corpo_email.replace('Hello', paragrafo.format(hello_friend[1]))

        enviar_email_smtp(corpo, hello_friend[3])


nome_arquivo = 'emails.csv'
recuperarEmail(nome_arquivo)
enviar_email()
