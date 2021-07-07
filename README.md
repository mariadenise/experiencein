# experiencein
Projeto de PI2 Rede Social
Projeto de rede social da disciplina Programação para Internet 2 do curso de Instituto Federal de Brasília 
23/06/2021 - Execução do Modulo 4  - Alteracao na experiencein/perfis/models.py para definição do esquema do banco(criação de um modelo),propagação do modelo pelos comandos makemigrations e migrate, criação, alteração e persistencia, busca, deleção e filtro de instância (metodos, create, save(), .get,.delete, filter).
26/06/2021 - Modulo 5 - Alterados os arquivos perfis/templates/index.html e perfis/views.py para construir uma 'li' (lista) dos perfis, renderizando a lista com template tag e tamplete de acesso às propriedades de objeto.
28/o6/2021 -MODULO 6 - Alteração dos arquivos: (i) experiencein/perfis/views.py, com uma função de view 'convidar' que delegará, para o método convidar, da classe Perfil, a responsabilidade de realizar um convite. Será retornado o objeto completo do 'id' convidado; (ii)arquivo experiencein/perfis/urls.py com a nova rota também alterado o (iii)template experiencein/perfis/templates/perfil.html para exibir apenas o nome do perfil e um link para convidá-lo; (iv) arquivo  experiencein/perfis/templates/perfil.html, adicionado um botão 'âncora' que fornecerá o link para convite; (v)arquivo experiencein/perfis/models.py incluído o método convite e criado um relacionamento entre o Perfil e os convidados e implementando os campos 'solicitante' e 'convidado' na Classe convite.
29/06/2021 -MODULO 7 - Criação de arquivo e template base com a inclusão da pasta 'static' em experiencein/perfis, importação dos arquivos do Bootstrap, adequação do arquivo experiencein/perfis/templates/index.html;Criada a página (arquivo) 'base.html' em perfis/template/base.html, para servir de modelo base para as demais (index.html e perfil.html podem herdar da base.html);Adequados os arquivo templates/index.html  e templates/perfil.html para inserir todo o conteúdo de index.html e perfil.ntml  herdando de base.html
29/06/2021 -MODULO 8 - para exibir os convites recebidos foram adequados os arquivos perfis/template/index.html com o link "aceitar" para cada convite e o arquivo  perfil/views.py com o perfil_logado a fim de simular o convite recebido.Enviados convites por meio do shell, então foi adequado o arquivo /perfis/templates/base.html de forma a exibir o nome do perfil logado; O arquivo perfis/templates/index.html foi adequado com a inclusão da tag with e variável {{ perfil_logado.convites_recebidos.count }}  e também o filtro '|pluralize' para obter o total de convites de um perfil.
MODULO 9 - Adequado o arquivo experiencein/perfis/views.py, com a função de view 'aceitar', para aceitar o convite feito e declarada a rota dessa função no arquivo experiencein/perfis/urls.py; e  o link aceitar de index.html, para que chame a rota nova. Função de view aceitar editada no arquivo perfis/views.py para  procurar o convite no banco de dados através de seu ID,e  aceitá-lo e  em seguida redirecionar o usuário para index.html(página principal da aplicação); Foram utilizados os comandos makemigrations e depois migrate para sincronizar as alterações realizadas com o Banco. Editada a index.html para exibir painel com todos os contatos do perfil. Então foi feita a renderização condicional com a inclusão da variável  'ja_e_contato' na experiencein/perfis/views.py e a adequação do arquivo experiencein/perfis/perfil.html com uma condição '{% if ja_e_contato %} para condicionar a exibição dos contatos conectados, ou não ao perfil.
