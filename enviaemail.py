import smtplib
import email.message
import pandas as pd
import openpyxl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

lista_clientes = pd.read_excel('C:\\Users\\augus\\Documents\\projetos\\lista_clientes.xlsx')
print(lista_clientes)
cliente = lista_clientes['CLIENTE']
mat_cliente = lista_clientes['MATRÍCULA']
email_cliente = lista_clientes['E-MAIL']

# startando o servidor SMTP
host = 'smtp.gmail.com'
port = '587'
login = 'augustoge71@gmail.com'
senha = 'Getdev1971'
server = smtplib.SMTP(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

# construindo e-mail tipo MIME



