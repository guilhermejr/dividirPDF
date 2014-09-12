#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
	from PyPDF2 import PdfFileWriter, PdfFileReader
	modulo = True
except ImportError:
	modulo = False

import sys
import os

def main():

	# --- Verifica se o módulo foi instalado ---
	if (not modulo):
 		os.system('clear')
 		print("Módulo PyPDF2 não instalado.\nAcesse https://pypi.python.org/pypi/PyPDF2/ e instale o módulo para poder usar esse Script Python.")
 		sys.exit(1)

	# --- Verifica a quantidade de parâmetros ---
	if (len(sys.argv) != 2):
		print("Uso: python dividirPDF.py arquivo.pdf")
		sys.exit(1)

	# --- Nome do arquivo a ser dividido ---
	arquivo = sys.argv[1]

	# --- Verifica se o arquivo realmente existe ---
	if (not os.path.isfile(arquivo)):
		print("Não foi possível encontrar o arquivo \"%s\"." % arquivo)
		sys.exit(1)

	# --- Verifica se o arquivo é realmente um pdf ---
	if (arquivo.split('.')[-1].lower() != "pdf"):
		print("O arquivo passado como parâmetro parece não ser um PDF.")
		sys.exit(1)

	# --- Abre arquivo ---
	entrada = PdfFileReader(open(arquivo, "rb"))

	# --- Verifica se o arquivo só tem uma página ---
	numPaginas = entrada.numPages
	if (numPaginas <= 1):
		print("O arquivo só tem uma página.")
		sys.exit(1)

	# --- Divide o arquivo ---
	for i in xrange(numPaginas):
		saida = PdfFileWriter()
		saida.addPage(entrada.getPage(i))
		outputStream = file("%s-%s%s" % (arquivo[:-4], i+1, arquivo[-4:]), "wb")
		saida.write(outputStream)
		outputStream.close()

if __name__ == "__main__":
    main()