Antes de executar o programa, primeiramente é necessário criar um arquivo de teste (nomeie como preferir) 
no formato .txt no mesmo diretório do programa, contendo as coordenadas dos retangulos a serem 
mosaicados na seguinte forma, um em cada linha:

xSuperiorEsquerdo ySuperiorEsquerdo xInferiorDireito yInferiorDireito

Além disso, para que o programa seja capaz de desenhar os resultados na tela, é
necessário instalar a biblioteca pygame na sua máquina (para fazer isso é necessário ter o pip instalado), 
com o seguinte comando na linha de comando:

python -m pip install -U pygame --user

Após criar o arquivo, para executar o programa, execute o seguinte comando na linha de comando:

python mosaico.py <caminho> <opcao de desenho>

Substituindo <caminho> pelo caminho do sistema para o arquivo de teste criado anteriormente
e <opcao de desenho> por "True" ou "true" para desenhar os resultados na tela, ou deixar em branco para 
não desenhar (Se por algum motivo a instalação do pygame não funcionar, execute com esse parâmetro em branco).

Independente de desenhar ou não, serão escritos na saída padrão as coordenadas dos resultados