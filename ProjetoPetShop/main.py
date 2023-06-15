# função principal da aplicação

from Arquivos.db.conexaoDB import criacaoBD
from Arquivos.db.petsDB import criacaoTablePets
from Arquivos.views.menuPrincipal import menuPrincipal

def principal():
    # criação incial do banco de dados
    criacaoBD()
    criacaoTablePets()
    menuPrincipal()
    

if __name__ == "__main__":
    principal()
