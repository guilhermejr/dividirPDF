Sou usuário do Evernote, e as vezes acumulo muitos documentos para escanear de
uma vez. Só que eu tinha um problema, ou ficava escaneando um por um ou botava
tudo na bandeja e depois ia dividindo manualmente o arquivo gerado pelo
escaneamento em lote.

Até o dia em que tive que escanear uns 40 documentos, todos com uma página só, e
tive a idéia de desenvolver esse "programinha".

Ele é bem simples, o arquivo que você passar como parâmetro será dividido em
vários arquivos, cada um com uma das páginas do arquivo original.

O programa é desenvolvido em python e tem uma única dependência que é o PyPDF2
https://pypi.python.org/pypi/PyPDF2/ 

Como utilizo OS X Mavericks esse Script Python foi desenvolvido e testado para
ele, não sei se vai funcionar em outras versões do OS X nem se vai funcionar 
em alguma distribuição Linux ou no MS Windows.

Para executa-lo::

	$ python dividirPDF.py arquivo.pdf

Depois do processamento será criado arquivos da seghuinte forma::
	
	arquivo-1.pdf
	arquivo-2.pdf
	arquivo-3.pdf
	.
	.
	.

Dúvidas e Sugestões favor mandar um e-mail falecom@guilhermejr.net