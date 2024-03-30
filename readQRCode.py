#Importação das bibliotecas

import pyqrcode
import png
from pyqrcode import QRCode

#String que representa o Código QR
STR_QRCODE = str(input("Digite o link: "))

# Gerar código QR
link = pyqrcode.create(STR_QRCODE)

#Criar e salvar o ficheiro svg
link.svg("mylink.svg", scale=8)

#Criando e salvando em ficheiro png
link.png("mylinked.png", scale=6)