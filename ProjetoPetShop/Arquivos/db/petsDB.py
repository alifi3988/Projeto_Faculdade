from Arquivos.db.conexaoDB import criacaoTabelasDB, insercaoDadosTabelas, recuperarDados

# criação da table pets
def criacaoTablePets():
    # criação da query 
    query = """CREATE TABLE tb_pets (
        id              INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome            VARCHAR(255) NOT NULL,
        especie         VARCHAR(255),
        raca            VARCHAR(255) NOT NULL,
        dataNascimento  DATE NOT NULL,
        sexo            VARCHAR(2) NOT NULL
    );  """
    
    # realizando a criação no banco de dados
    return criacaoTabelasDB(query)

# inserção de dados na table pets
def insercaoDadosPets(nome, especie, raca, nascimento, sexo):
    query = f'''INSERT INTO tb_pets(nome, especie, raca, dataNascimento, sexo) 
    VALUES('{nome}', '{especie}', '{raca}', '{nascimento}', '{sexo}')'''
    return insercaoDadosTabelas(query)

# recuperação de todos os dados ordenados por nome
def recuperacaoDadosTodos():
    query = "SELECT * FROM tb_pets ORDER BY nome"
    return recuperarDados(query)

def recuperarDadosEspecificos(especie):
    query = f"SELECT * FROM tb_pets WHERE especie = '{especie}' ORDER BY nome"
    return recuperarDados(query)