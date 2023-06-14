# Importações
import io
import sqlite3
import time

#from bs4 import BeautifulSoup

# Realizando a criação de um banco de dados local (abrindo e fechando)
def criacaoBD():
    try:
        conn = sqlite3.connect('PetShop.db')
        conn.close()
        return True
    except sqlite3.Error as er:
        print(er)
        return False

# Criação automática de tables uteis na aplicação
def criacaoTabelasDB(sql):
    # verificando a criação do BD
    conn = sqlite3.connect('PetShop.db')

    # Criando através de Scripts
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        # Fechando a conexão com o banco de dados
        conn.close()
        return True
    except sqlite3.Error as er:
        conn.close()
        return er
        
# inserção no banco de dados
def insercaoDadosTabelas(sqlScript):
    try:
        # conexão com o bd
        conn = sqlite3.connect('PetShop.db')
        cursor = conn.cursor()
        cursor.execute(sqlScript)
        
        # gravando no bd
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as er:
        conn.close()
        return er

# buscando os dados da table e retornando em forma de lista
def recuperarDados(sql):
        # coneção com o banco de dados
        conn = sqlite3.connect('PetShop.db')
        cursor = conn.cursor()
        try:
            # executando sql
            cursor.execute(sql)
            
            # criando uma lista para armazenar o resultado
            listaDados = list()
            # passando os dados para um objeto
            for linha in cursor.fetchall():
                listaDados.append(linha)
            # fechando a conexão
            conn.close()
            # retornando uma lista com um dado só, no caso o usuário com o login informado
            if len(listaDados) == 0:
                return False
            return listaDados
        except sqlite3.Error as er:
            return False
   
# modificar table        
def modificacaoTable(sql):
        # coneção com o banco de dados
        conn = sqlite3.connect('PetShop.db')
        cursor = conn.cursor()
        try:
            # executando sql
            cursor.execute(sql)

            # salvando a alteração
            conn.commit()
            
            # fechando a conexão
            conn.close()
            
            return True
        
        except sqlite3.Error as er:
            print("Erro na modificação dos dados.")
            print(f"Erro: {er}")
            return False
     
# BKP bd
def BKPBancoDeDados():
    
    try:
        conn = sqlite3.connect('PetShop.db')
        
        # Open() function 
        with open("backupdatabase.sql", 'w') as p: 
                
            # iterdump() function
            for line in conn.iterdump(): 
                p.write('%s\n' % line)
            
        print(' Backup realizado com sucesso!'.center(52))   
        time.sleep(3) 
        conn.close() 
        return True
    
    except sqlite3.Error as er:
        print("Erro para realizar o BKP do Banco de dados")
        print(f"Erro: {er}")
        time.sleep(3)
        return False

# recuperar BD
def RecuperarBancoDeDados(nome):
    try:
        conn = sqlite3.connect('PetShop.db')
        cursor = conn.cursor()
        
        nomeArquivo = f"{nome}"

        f = io.open(nomeArquivo, 'r')
        sql = f.read()
        cursor.executescript(sql)

        print('Banco de dados recuperado com sucesso.')
        conn.close()
        return True
    except sqlite3.Error as er:
        print("Erro na recuperação. Ou o Banco e as tabelas já existem!")
        print(f"Mensagem: {er}")
        time.sleep(3)
        return False

# ================================================================================
# ================================================================================

# Referência https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html#conectando-e-desconectando-do-banco
