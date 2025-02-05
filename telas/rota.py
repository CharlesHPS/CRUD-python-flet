from telas.direciona import Direciona
from telas.tela_inicio import inicio
from telas.tela_criar_colab import criar_colab
from telas.tela_criar_outras import criar_funcoes,criar_razao,criar_coordenador,criar_treina
from telas.tela_criar_proj import criar_projeto
from telas.tela_add_colab_proj import add_colab_projeto
from telas.tela_listar_colab import listar_colab
from telas.tela_listar_proj import listar_proj
from telas.tela_listar_funcoes import listar_funcoes
from telas.tela_listar_razao import listar_razao
from telas.tela_listar_coordenador import listar_coordenador
from telas.tela_listar_treina import listar_treina
from tela_login import login

router = Direciona()

router.direc = {

  "login" : login,
  
  "/inicio": inicio,

  "/criarColab": criar_colab,
  "/criarProj": criar_projeto,
  "/addColabProj": add_colab_projeto,
  "/criarTreina": criar_treina,
  "/criarRazao": criar_razao,
  "/criarFuncoes": criar_funcoes,
  "/criarCoordenador": criar_coordenador,

  "/listarColab": listar_colab,
  "/listarProj": listar_proj,
  "/listarFuncoes": listar_funcoes,
  "/listarRazao": listar_razao,
  "/listarCoordenador": listar_coordenador,
  "/listarTreina": listar_treina,
  
  
}