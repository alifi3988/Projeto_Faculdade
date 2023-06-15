# importações
import json
import os
import time

from click import pause


from Arquivos.db.petsDB import insercaoDadosPets, recuperacaoDadosTodos, recuperarDadosEspecificos

# criação das das funções com as 'telas'
def menuPrincipal():

    while True:
        os.system("cls")
        print("=+"*35)
        print("* * * M E N U  P R I N C I P A L * * *")
        print("=+"*35)
        print("[1] - Adicionar Pet")
        print("[2] - Relatório de Pet")
        print("[3] - Relatório de Pet por Espécie")
        print("[4] - Exportar Dados")
        print("[0] - Sair")
        print("-"*35)
        while True:
            resposta = int(input("Informe a resposta: "))
            if resposta < 0 or resposta > 4:
                print("Erro na resposta informada! Tente novamente!")
                time.sleep(3)
            else:
                break
        
        if resposta == 1:
            # adicionando PET
            adicionarPet()
            
        elif resposta == 2:
            # realizando o relatório total
            relatorioPet()
            
        elif resposta == 3:
            # realizando o relatório por espécie
            relatorioPetEspecie()
            
        elif resposta == 4:
            # realizando a expostação de dados
            exportarDadosBD()
            
        elif resposta == 0:
            # saindo do sistema
            os.system("cls")
            print("Saindo do sistema...")
            time.sleep(3)
            exit()

# REALIZANDO A INSERÇÃO DE PETS
def adicionarPet():
    while True:
        os.system("cls")
        print("=+"*35)
        print("* * * C A D A S T R O  D E  P E T S * * *")
        print("=+"*35)
        print("Informe os dados conforme pedido.\nPara cancelar, digite [0].")
        print("-"*32)
        nome = input("Nome: ")
        if nome == '0': break
        especie = input("Espécie [Cão | Gato]: ")
        if especie == '0': break
        raca = input("Raça: ")
        if raca == '0': break
        dataNascimento = input("Data Nascimento [DD/MM/YYYY]: ")
        if dataNascimento == '0': break
        sexo = input("Sexo [M/F]: ").strip().upper()
        if sexo == '0': break
        print("-"*32)
        resultado = insercaoDadosPets(nome, especie, raca, dataNascimento, sexo)
        
        if resultado != True:
            print("Não foi realizado a inserção dos dados. Verifique!")
            print(resultado)
            time.sleep(4)
            
        print(f"Dados foram inseridos com sucesso!\nPet {nome}, foi adicionado com sucesso!")
        time.sleep(2)
        print("-"*32)
        resposta = input("Deseja inserir outro? [S/N]").strip().upper()
        if resposta != 'S':
            break
            
    print("Voltando ao Menu...")
    time.sleep(2)

# REALIZANDO O RELATÓRIO DOS PETS
def relatorioPet():
    while True:
        os.system("cls")
        print("=+"*35)
        print("* * * R E L A T Ó R I O  P E T S * * *")
        print("=+"*35)
        print("Será mostrado todos os pets...")
        time.sleep(2)
        recuperacao = recuperacaoDadosTodos()
        if recuperacao == False:
            print("Erro na recuperação dos dados!")
            time.sleep(3)
        
        tamanho = len(recuperacao)
        cont = 0
        
        print("Pet{ ")
        for i in recuperacao:
            print(f"'ID': '{i[0]}', 'Nome':'{i[1]}', 'Especie': '{i[2]}', 'Raça': '{i[3]}', 'Data Nascimento': '{i[4]}', 'Sexo':'{i[5]}'", end="")
            cont = cont + 1
            if tamanho < cont:
                print(",\n")
            if tamanho == cont:
                print("\n}")
        pause()
        break

# REALIZANDO O RELATÓRIO DOS PETS POR ESPÉCIE
def relatorioPetEspecie():
    while True:
        os.system("cls")
        print("=+"*35)
        print("* * * R E L A T Ó R I O  P E T S  E S P É C I E S * * *")
        print("=+"*35)
        print("Será mostrado todos os pets. Selecione o tipo:")
        print("[1] - Cães   [2] - Gatos")
        
        resposta = int(input(">> "))
        if resposta == 1:
            os.system("cls")
            print("=+"*35)
            print("* * * R E L A T Ó R I O  P E T S  C Ã E S * * *")
            print("=+"*35)
            resultado = recuperarDadosEspecificos('Cão')
            if resultado == False:
                print("Erro na recuperação de dados!")
                time.sleep(3)
                
        if resposta == 2:
            os.system("cls")
            print("=+"*35)
            print("* * * R E L A T Ó R I O  P E T S  G A T O S * * *")
            print("=+"*35)
            resultado = recuperarDadosEspecificos('Gato')
            if resultado == False:
                print("Erro na recuperação de dados!")
                time.sleep(3)
        
        else:
            print("Resposta não confere! ")
            time.sleep(2)
            break
        
        tamanho = len(resultado)
        cont = 0
        
        print("Pet{ ")
        for i in resultado:
            print(f"'ID': '{i[0]}', 'Nome':'{i[1]}', 'Especie': '{i[2]}', 'Raça': '{i[3]}', 'Data Nascimento': '{i[4]}', 'Sexo':'{i[5]}'", end="")
            cont = cont + 1
            if tamanho < cont:
                print(",\n")
            if tamanho == cont:
                print("\n}")
        pause()
        break

# REALIZANDO A EXPORTAÇÃO EM FORMATO JSON

# criação do diretório para exportação do JSON
def criarDiretorioProjetoJson():
    try:
        os.makedirs
        dir = os.path.join(os.sep, "c:\\", 'PETS')
        dr2 = os.path.join(os.sep, "c:\\PETS", 'json')
        
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(dr2):
            os.makedirs(dr2)

            
        print(f"Diretórios criados: {dir} | {dr2}")
        time.sleep(3)
        
        return True
    except:
        print("Erro: menu/criarDiretorioProjeto()")
        time.sleep(3)
        return False

# exportação dos dados
def exportarDadosBD():
    os.system("cls")
    print("=+"*35)
    print("* * * E X P O R T A R  D A D O S  J S O N * * *")
    print("=+"*35)
    criacaoJSON()

# criação do JSON 
def criacaoJSON():
    criarDiretorioProjetoJson() # criação dos diretórios
    petsJSON = {'PETS CAES': [], 'PETS GATOS':[]}
     
    recuperacaoCaes = recuperarDadosEspecificos('Cão')
    recuperacaoGatos = recuperarDadosEspecificos('Gato')
     
    if recuperacaoCaes != False:
         
        for i in recuperacaoCaes:
             petsJSON['PETS CAES'].append(
                 {
                     'ID':i[0],
                     'Nome': i[1],
                     'Especie': i[2],
                     'Raca':i[3],
                     'Data nascimento':i[4],
                     'Sexo':i[5]
                 }
             )
    if recuperacaoGatos != False:
        for i in recuperacaoGatos:
             petsJSON['PETS GATOS'].append(
                 {
                     'ID':i[0],
                     'Nome': i[1],
                     'Especie': i[2],
                     'Raca':i[3],
                     'Data nascimento':i[4],
                     'Sexo':i[5]
                 }
             )
             
    else:  
        print("ERRO PARA RECUPERAÇÃO DE DADOS!".center(52))
        time.sleep(3)
        # finalização
    
    try:
        # realizando a conversão para Json
        with open("c:\\PETS\\json\\jsonbancoPets.json", "w") as arquivo:     
            json.dump(petsJSON, arquivo, indent=4)
        print("Arquivo Criado!".center(52))
        time.sleep(3)
    
    except:
        print("Houve erro! Verifique! [menu/importarJSON()]")
        time.sleep(3)

