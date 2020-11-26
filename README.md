# Bubbles

Programas requisitados:
- Pycharm
- XAMPP Control Panel

# Inicialmente todos os arquivos presentes nesse repositório com exceção do lista.c devem estar na mesma pasta enquanto o programa estiver sendo rodado.

# Guia de como utilizar o banco de dados com o Pycharm

1- Abra o Pycharm e crie um projeto (Você pode optar por utilizar um projeto já existente).

2- No canto superior esquerdo clique em "file", depois em "Settings...".  Uma nova aba será aberta com opções de configuração.

3- Na nova aba clique em "Project: (<nome do seu projeto>)" e depois clique em "project interpreter".

4- Nessa área é possível instalar pacotes para utilizar junto ao Python. Dê um double clique em "pip" e depois clique em "install package", após instalar feche a aba dos pacotes "pip".

5- Dê double clique em "setuptools". Dessa vez pesquise por "PyMySQL" e o instale, após instalar "PyMySQL" pesquise na barra de busca por "PyMysqlDB" e o instale.

6- Quando tiver instalado os três pacotes (pip, PyMySQL, PyMysqlDB) feche as abas extras.

7- Abra o "XAMPP Control Panel" e clique em "Start" nos módulos "Apache" e "MySQL".

8- Após o "Service" ficar verde o código está pronto para rodar.
 
9- Para visualizar as atualizações dos dados clique em "Admin" do módulo "MySQL" e isso abrirá no navegador o phpMyAdmin para ter acesso ao banco de dados.




# Guia de como Importar um banco de dados no phpMyAdmin

1- Crie um banco de dados vazio com o nome "bubbles" (É necessário que o nome seja "bubbles" para o código funcionar).

2- Clique no banco de dados e abra ele, após abrir clique na opção "Import".

3- Essa opção permitira importar um arquivo. Clique em "Escolher arquivo" e selecionar o arquivo bubbles.zip que foi disponibilizado.

4- Após a seleção clique em executar e o banco de dados estará no seu local host phpMyAdmin.
