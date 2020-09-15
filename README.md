# Ahand
![logoahand](Ahand_Logo.png)

Descrição:
    Ahand (Give me a hand) é um programa para otimização de processos que envolvam arquivos PDF. Com Ahand é possível:
    
    Combinar arquivos PDF.
    Extrair páginas de arquivos PDF.
    Dividir arquivos PDF.
    Escanear arquivos PDF através do reconhecimento óptico de caracteres (OCR), transformando em um PDF pesquisável.
    Organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.
    Compactar arquivos PDF contidos em subpastas de uma pasta raiz.
    
Nomenclatura dos arquivos:

Dentro do programa, existem tags, elas são variáveis que abrangem alguns padrões bastante usados na hora de renomear um arquivo. As tags são indicadas por #.
As tags são:
#origin = Nome original do arquivo.
#year = Ano atual.
#month = Mês atual.
#day = Dia atual.
#hour = Hora atual.
#minutes = Minutos atuais.
#seconds = Segundos atuais
#time = Hora, minutos e segundos atuais.
#pages = Página(s) exportadas do arquivo. Disponível apenas para as funções Separar/Dividir e Organizar

Por padrão, caso o campo de nome esteja vazio, os arquivos são salvos com a tag #origin, com exceção da função Separar/Dividir, que utiliza as tags #origin,#pages.
Para utilizar um conjunto de tags, é necessário delimitar por vírgulas.

Veja um exemplo de nomenclatura de um arquivo:
Arquivos de entrada: C:\Downloads\file1.pdf,C:\Downloads\file2.pdf
Extrair página indicada: 3

Diretório de saída: C:\Downloads
Nome do arquivo: #origin,#pages,Contas a pagar,#year,#month,#day
Resultado: C:\Downloads\file1_3_Contas a pagar_2020_10_14,C:\Downloads\file2_3_Contas a pagar_2020_10_14

Note que você pode utilizar tags e texto em conjunto, mas eles devem ser delimitados por vírgula.

Função Organizar arquivos PDF:
Você pode organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.
Suponhamos que você seja um professor e queira organizar os trabalhos enviados por seus alunos por escola, turma, ano, matéria, tema do trabalho e nome do aluno:

- Primeiro, certifique-se de que o documento PDF seja pesquisável, isto é, contenha texto. Caso seja uma imagem escaneada, utilize a função "Escanear arquivos PDF" antes de proceder.
- Importe os arquivos PDF que você deseja organizar.
- Importe um ou mais arquivos CSV com o banco de dados que contém as palavras a pesquisar (você pode gerar o banco de dados com um editor de planilhas, como o Excel).

Alunos.csv
| Nome do aluno                      | Número de chamada | Turma | Escola                          | Munícipio              | Cidade    |
|------------------------------------|-------------------|-------|---------------------------------|------------------------|-----------|
| Bianca Helena Cavalcanti           | 1                 | 2C    | Durvalino Grion Prof            | Adamantina             | São Paulo |
| Catarina Jaqueline Nunes           | 3                 | 1A    | Alice Maciel Sanches Professora | Santo Anastácio        | São Paulo |
| Clara Emanuelly Luiza Carvalho     | 6                 | 2B    | Ferdinando Ienny                | Ouro Verde             | São Paulo |
| Francisco Edson Gonçalves          | 11                | 3D    | Jadyr Salles Professor Etec     | Porto Ferreira         | São Paulo |
| Gabriela Emanuelly Baptista        | 15                | 3E    | Durvalino Grion Prof            | Adamantina             | São Paulo |
| Julio Jorge Aragão                 | 21                | 2F    | Ferdinando Ienny                | Ouro Verde             | São Paulo |
| Pietra Giovanna Joana Almada       | 32                | 1C    | Djalma Forjaz Doutor            | Porto Ferreira         | São Paulo |
| Silvana Stefany Mirella Nascimento | 37                | 1C    | Alice Maciel Sanches Professora | Santo Anastácio        | São Paulo |
| Tânia Allana Monteiro              | 40                | 3C    | Santo Antonio                   | Santo Antônio De Posse | São Paulo |

Matérias.csv
| Tema                       | Matéria    |
|----------------------------|------------|
| Deslocamento escalar       | Cinemática |
| Energia potencial elétrica | Elétrica   |
| Leis de Newton             | Dinâmica   |
| Trajetória                 | Cinemática |
| Lentes convergentes        | Óptica     |
| Movimento e repouso        | Cinemática |
| Campo elétrico             | Elétrica   |

(Todos os dados referentes a alunos foram gerados aleatoriamente).

Licença:
    Código licenciado sob as condições da GPL3.
    https://www.gnu.org/licenses/
    
Documentação:

User interface created with QT Creator.
https://www.qt.io/
Licensed under LGPLv3 conditions.

QT Python binaries by Pyside.
https://www.qt.io/qt-for-python/
Licensed under LGPLv3 conditions.

PySide Base by Wanderson Magalhaes.
https://github.com/Wanderson-Magalhaes/
Licensed under MIT License conditions.

OCR engine by Tesseract.
https://github.com/tesseract-ocr/tesseract/
Licensed under Apache License 2.0 conditions.

Tesseract installer for Windows by UB-Mannheim.
https://github.com/UB-Mannheim/tesseract/

Python-tesseract wrapper by pytesseract.
https://github.com/madmaze/pytesseract/
Licensed under Apache License 2.0 conditions.

Python Imaging Library by Pillow
https://github.com/python-pillow/Pillow/
Licensed under the open source PIL Software License conditions.

Convert PDF to a PIL Image object by pdf2image.
https://github.com/Belval/pdf2image/
Licensed under MIT License conditions.

PDF rendering library by Poppler.
https://poppler.freedesktop.org/
Licensed under GPLv3 conditions.

Poppler Windows binaries by oschwartz10612.
https://github.com/oschwartz10612/poppler-windows/releases/

Python PDF toolkit by PYPDF2.
https://github.com/mstamy2/PyPDF2/
Licensed under BSD License conditions.

Extracts the text from a PDF page by pdfminer.six.
https://github.com/pdfminer/pdfminer.six/
Licensed under MIT License conditions.

Sound-playing interface for Windows by winsound.
https://docs.python.org/3/library/winsound.html

Icons by Flaticon.
https://www.flaticon.com/

Sound Effects by Freesound.
https://freesound.org/

Developed with Python.
https://www.python.org/
Licensed under PSF LICENSE conditions.
