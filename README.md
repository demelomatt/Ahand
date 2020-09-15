# Ahand
![logoahand](Ahand_Logo.png)

Descrição:
    Ahand (Give me a hand) é um programa para otimização de processos que envolvam arquivos PDF. Com Ahand é possível:
    
    Unir arquivos PDF.
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
#pages = Página(s) exportadas do arquivo. Disponível apenas para as funções Separar/Dividir e Organizar(caso a caixa de seleção "Mover apenas páginas esteja marcada").

Por padrão, caso o campo de nome esteja vazio, os arquivos são salvos com a tag #origin, com exceção da função Separar/Dividir, que utiliza as tags #origin,#pages.
Para utilizar um conjunto de tags, é necessário delimitar por vírgulas.

Veja um exemplo de nomenclatura de um arquivo:
Arquivos de entrada: C:\Downloads\file1.pdf,C:\Downloads\file2.pdf
Extrair página indicada: 3

Diretório de saída: C:\Downloads
Nome do arquivo: #origin,#pages,Contas a pagar,#year,#month,#day
Resultado: C:\Downloads\file1_3_Contas a pagar_2020_10_14,C:\Downloads\file2_3_Contas a pagar_2020_10_14

Note que você pode utilizar tags e texto em conjunto, mas eles devem ser delimitados por vírgula.

Unir arquivos PDF:
Exemplo:
Arquivos de entrada: C:\Downloads\file1.pdf,C:\Downloads\file2.pdf
Diretório de saída: C:\Downloads\
Nome do arquivo: merged
Resultado: C:\Downloads\merged.pdf

Extrair páginas ou dividir arquivos PDF:
Lista - Páginas indicadas: Extrair ou dividir nas páginas indicadas.
Lista - A cada n páginas: Extrair ou dividir a cada "n" páginas.
Caixa de seleção - Dividir arquivo: Através de um arquivo, outros são gerados, os dividindo nas páginas indicadas.
Caixa de seleção - Extrair no mesmo arquivo: As páginas indicadas são extraídas em um mesmo arquivo.

Exemplos:
Arquivo de entrada: C:\Downloads\file.pdf
Diretório de saída: C:\Downloads\
Nome do arquivo: #origin,#pages

Exemplo 1:
Lista = Páginas indicadas
Caixa de seleção = Dividir arquivo
Páginas = 3,7-8,11-16
Resultado: C:\Downloads\file_3.pdf,C:\Downloads\file_7-8.pdf,C:\Downloads\file_11-16.pdf

Exemplo 2:
Lista = Páginas indicadas
Caixa de seleção = Extrair no mesmo arquivo
Páginas = 3,7-8,11-16
Resultado: C:\Downloads\file_3,7-8,11-16.pdf

Exemplo 3:
Lista = A cada n páginas
Caixa de seleção = Dividir arquivo
Páginas = 4
Resultado: C:\Downloads\file_1-4.pdf,C:\Downloads\file_5-8.pdf,C:\Downloads\file_9-12.pdf,C:\Downloads\file_13-16.pdf

Exemplo 4:
Lista = A cada n páginas
Caixa de seleção = Extrair no mesmo arquivo
Páginas = 4
Resultado: C:\Downloads\file_4,8,12,16.pdf

Escanear arquivos PDF (OCR):
Exemplo:
Arquivos de entrada: C:\Downloads\file1.pdf,C:\Downloads\file2.pdf
Diretório de saída: C:\Downloads\
Nome do arquivo: #origin,OCR
DPI: 200
Resultado: C:\Downloads\file1_OCR.pdf,C:\Downloads\file2_OCR.pdf

Note que quanto maior o DPI, maior o tamanho da imagem.
Caso o reconhecimento óptico de caracteres (OCR) não atinja um resultado satisfatório, experimente alterar o DPI.


Função Organizar arquivos PDF:
Você pode organizar arquivos PDF de acordo com as frases ou palavras encontradas dentro do arquivo.
Suponhamos que você seja um professor e queira organizar os trabalhos enviados por seus alunos por escola, turma, ano atual, matéria, tema do trabalho e nome do aluno:

- Primeiro, certifique-se de que o documento PDF seja pesquisável, isto é, contenha texto. Caso seja uma imagem escaneada, utilize a função "Escanear arquivos PDF" antes de proceder.
- Importe os arquivos PDF que você deseja organizar.
- Selecione o diretório de saída. Como exemplo será "C:Desktop\"
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
(Todos os dados referentes a alunos foram gerados aleatoriamente).

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

Iremos procurar pelo nome de todos os alunos, que se encontra na tabela Alunos coluna 1, junto a todos os temas de trabalho, que se encontra na tabela Matérias coluna 1.
Então temos a definição tabela:coluna

Sendo assim, o campo "Procurar por expressões" recebe o seguinte valor: Alunos:1,Matérias:1
Se houver mais de um conjunto tabela:coluna, eles devem ser delimitados por vírgulas, como no exemplo acima.

Note que se o valor de uma linha for localizado, temos acesso a todos os valores das outras colunas adjacentes nessa tabela.
Como por exemplo, se dentro do arquivo conter o nome "Bianca Helena Cavalcanti", podemos pedir para o programa retornar o valor da coluna 3, que para essa linha é "2C".
Dessa forma, temos acesso a valores que não necessariamente precisam estar dentro do arquivo.

Com isso em mente:
Iremos informar o destino que queremos exportar o arquivo caso as condições forem satisfeitas:
Queremos criar uma árvore de diretório nesse modelo: diretório_de_saída\ano_atual\escola\turma\matéria\tema_do_trabalho\

Então iremos informar em qual tabela e coluna esses valores se encontram.
Sendo assim, o campo "Criar subpastas" recebe o seguinte valor: #year,Alunos:4,Alunos:3,Matérias:2,Matérias:1

Caso as condições não sejam satisfeitas dentro de um arquivo, podemos indicar um diretório para movê-lo.
Sendo assim, o campo "Se não encontrar mover para pasta" recebe o seguinte valor: Não encontrado
Caso vazio, os arquivos em que não foram encontradas todas as palavras não serão movidos.

Agora, iremos informar o nome do arquivo, neste caso queremos o nome do aluno.
Sendo assim, o campo "Nome do arquivo" recebe o seguinte valor: Alunos:1

Há ainda algumas caixas de seleção:

Mover apenas páginas: Se marcado, irá procurar pelas palavras dentro de cada página e exporta-la caso os requisitos sejam satisfeitos. Útil quando cada página representa um arquivo, como uma nota fiscal. Caso contrário, as palavras serão pesquisadas dentro de todo o arquivo.
Ignorar primeira linha: Marcar caso a primeira linha seja cabeçalho e você não queira pesquisa-la dentro do arquivo.
Ignorar acentos: Realizar pesquisa desconsiderando acentos. Marcar para maior precisão.
Ignorar pontuação: Realizar pesquisa desconsiderando pontuação tais como ".,;/?!". Marcar para maior precisão.
Ignorar espaços: Realizar pesquisa desconsiderando espaços. Marcar para maior precisão.

Para este exemplo, iremos desmarcar apenas a opção "Mover apenas páginas".

Então, como exemplo de resultado, caso ambas as palavras "Bianca Helena Cavalcanti" e "Deslocamento escalar" sejam encontradas no arquivo, temos:
C:Desktop\2020\Durvalino Grion Prof\2C\Cinemática\Deslocamento escalar\Bianca Helena Cavalcanti.pdf

Se em vez de criar uma árvore de diretório quisessemos apenas renomear o arquivo, bastava informar os valores no campo "Nome do arquivo" e deixar o campo "Criar subpastas" vazio.

Então, como exemplo de resultado, temos:
C:Desktop\2020_Durvalino Grion Prof_2C_Cinemática_Deslocamento escalar_Bianca Helena Cavalcanti.pdf

Criar ficheiro ZIP de arquivos PDF:
Exemplo:
Diretório raiz: C:\Downloads\root\
Subpastas contidas no diretório raiz: Janeiro,Fevereiro,Março
Diretório de saída: C:\Downloads\output\
Nome do arquivo ZIP: #origin,#year
Resultado: C:\Downloads\output\Janeiro_2020.zip,C:\Downloads\output\Fevereiro_2020.zip,C:\Downloads\output\Março_2020.zip

Portanto, todos os arquivos PDF contidos nas subpastas Janeiro,Fevereiro,Março serão compactados.

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
