# Send E-mails.py

### Um protótipo de programa em python que envia e-mails listados em um arquivo .csv

---

# Bibliotecas

## Email.message

## CSV

## Smtplib

---

# Email.message

O analisador sintático pega a versão serializada de uma mensagem de e-mail (um fluxo de bytes) e a converte em uma árvore de objetos EmailMessage. O gerador pega um EmailMessage e o transforma novamente em um fluxo de bytes serializado. (O analisador sintático e o gerador também lidam com fluxos de caracteres de texto, mas esse uso é desencorajado, pois é muito fácil terminar com mensagens que não são válidas de uma maneira ou de outra.)

```
import email.message
```

---

## CSV

O módulo csv implementa classes para ler e gravar dados tabulares no formato CSV. Ele permite que os programadores digam “escreva esses dados no formato preferido pelo Excel” ou “leia os dados desse arquivo gerado pelo Excel”, sem conhecer os detalhes precisos do formato CSV usado pelo Excel. Os programadores também podem descrever os formatos CSV entendidos por outros aplicativos ou definir seus próprios formatos CSV para fins especiais.

```
import csv
```

---

## Smtplib

Módulo usado para envios de e-mails

```
import smtplib
```

---

```python
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
```
