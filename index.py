from pymongo.mongo_client import MongoClient
from bson.objectid import ObjectId  # Importar para converter IDs

#pegando URI do mongo
uri = "mongodb+srv://Kenzo:123@brunao.u01owig.mongodb.net/?retryWrites=true&w=majority&appName=Brunao" 
cliente = MongoClient(uri)

def verificar_digito(info): #verificar se a informacao enviada tem numeros, retorna 1 e 0
    
    if info.isdigit(): 
        return 1 
    else:
        return 0 
    
def verificar_conteudo(conteudo_buscado,conteudo_local): #verifica se o conteudo ja existe no banco de dados, retorna 1 e 0
    if colecao.find_one({conteudo_buscado : conteudo_local}):
        return 1
    else:
        return 0


continuar = 0 #controlador do fluxo
try:
    while continuar != 1:
        def cadastrar_aluno(colecao): 
            nome_aluno = input('NOME COMPLETO DO ALUNO: ')
            while verificar_digito(nome_aluno) == 1: #VERIFICAR DIGITACAO
                print('Nao e possivel cadastrar um aluno com numeros!')
                nome_aluno = input('NOME COMPLETO DO ALUNO: ')
            matricula_aluno = input('MATRICULA: ')  
            while verificar_digito(matricula_aluno) == 0: #VERIFICAR DIGITACAO 
                print('Nao e possivel cadastrar uma matricula com letras!')
                matricula_aluno = input('MATRICULA: ')
            while verificar_conteudo('matricula',matricula_aluno) == 1: #VERIFICAR CONTEUDO
                print('Matricula ja registrada!')
                matricula_aluno = input('MATRICULA: ')
            curso = input('CURSO: ')
            while verificar_digito(curso) == 1: #VERIFICAR DIGITACAO
                print('Nao e possivel cadastrar um curso com numeros')
                curso = input('CURSO: ')
            aluno = {'nome': nome_aluno, 'matricula': matricula_aluno, 'curso': curso} #DICIONARIO PARA ENVIO
            colecao.insert_one(aluno)
            print("Aluno cadastrado com sucesso!")

        def cadastrar_professor(colecao):
            nome_professor = input('NOME COMPLETO DO PROFESSOR: ')
            while verificar_digito(nome_professor) == 1: #VERIFICAR DIGITO
                print('Nao e possivel cadastrar um professor com numeros!')
                nome_professor = input('NOME COMPLETO DO PROFESSOR: ')
            while verificar_conteudo('nome do professor',nome_professor) == 1: #VERIFICAR CONTEUDO
                print('Professor ja registrado!')
                nome_professor = input('NOME COMPLETO DO PROFESSOR: ')
            departamento_professor = input('DEPARTAMENTO DO PROFESSOR: ')
            while verificar_digito(departamento_professor) == 1: #VERIFICAR DIGITO
                print('Nao e possivel cadastrar um departamento com numeros')
                departamento_professor = input('DEPARTAMENTO DO PROFESSOR: ')
            professor = {'nome do professor': nome_professor, 'departamento do professor': departamento_professor} #DICIONARIO PARA ENVIO
            colecao.insert_one(professor)
            print("Professor cadastrado com sucesso!")

        def cadastrar_disciplina(colecao):
            nome_disciplina = input('NOME DA DISCIPLINA: ')
            while verificar_digito(nome_disciplina) == 1: #VD
                print('Nao e possivel cadastrar uma disciplina com numeros')
                nome_disciplina = input('NOME DA DISCIPLINA: ')
            codigo_disciplina = input('CODIGO DA DISCIPLINA: ')
            while verificar_digito(codigo_disciplina) == 0: #VD
                print('Nao e possivel cadastrar um codigo de disciplina com letras')
                codigo_disciplina = input('CODIGO DA DISCIPLINA: ')
            while verificar_conteudo('codigo da disciplina',codigo_disciplina): #VC
                print('Disciplina ja registrado!')
                codigo_disciplina = input('CODIGO DA DISCIPLNA: ')
            professor_responsavel = input('PROFESSOR RESPONSAVEL: ')
            while verificar_digito(professor_responsavel) == 1: #VD
                print('Nao e possivel cadastrar um professor com numeros')
                professor_responsavel = input('PROFESSOR RESPONSAVEL: ')
            disciplina = {'nome da disciplina': nome_disciplina, 'codigo da disciplina': codigo_disciplina, 'professor responsavel': professor_responsavel} #DE
            colecao.insert_one(disciplina)
            print("Disciplina cadastrada com sucesso!")

        def consultar(colecao):
            escolha = input('Qual consulta você deseja fazer? \n (1) ALUNO \n (2) PROFESSOR \n (3) DISCIPLINA (4) TODOS OS REGISTROS \n')
            
            if escolha == '1':
                nome_aluno_consulta = input('NOME COMPLETO DO ALUNO PARA CONSULTA: ')
                aluno_consulta = {'nome': nome_aluno_consulta}
                resultados = colecao.find(aluno_consulta)
                for resultado in resultados:
                    print(f"ID: {resultado['_id']}") #Pegando ID da busca
                    print(f"Nome: {resultado.get('nome', 'N/A')}") #.GET = pegar valores do campo. SE ESTIVER VAZIO vai aparecer N/A!
                    print(f"Matrícula: {resultado.get('matricula', 'N/A')}")
                    print(f"Curso: {resultado.get('curso', 'N/A')}")
                    print("-" * 40)
            
            elif escolha == '2':
                nome_professor_consulta = input('NOME COMPLETO DO PROFESSOR PARA CONSULTA: ')
                professor_consulta = {'nome do professor': nome_professor_consulta}
                resultados = colecao.find(professor_consulta)
                for resultado in resultados:
                    print(f"ID: {resultado['_id']}")
                    print(f"Nome do Professor: {resultado.get('nome do professor', 'N/A')}")
                    print(f"Departamento: {resultado.get('departamento do professor', 'N/A')}")
                    print("-" * 40)
            
            elif escolha == '3':
                nome_disciplina_consulta = input('NOME DA DISCIPLINA PARA CONSULTA: ')
                disciplina_consulta = {'nome da disciplina': nome_disciplina_consulta}
                resultados = colecao.find(disciplina_consulta)
                for resultado in resultados:
                    print(f"ID: {resultado['_id']}")
                    print(f"Nome da Disciplina: {resultado.get('nome da disciplina', 'N/A')}")
                    print(f"Código da Disciplina: {resultado.get('codigo da disciplina', 'N/A')}")
                    print(f"Professor Responsável: {resultado.get('professor responsavel', 'N/A')}")
                    print("-" * 40)
            
            elif escolha == '4':
                todos_registros = colecao.find()
                for registro in todos_registros:
                    print(f"ID: {registro['_id']}")
                    print(f"Nome: {registro.get('nome', 'N/A')}")
                    print(f"Matrícula: {registro.get('matricula', 'N/A')}")
                    print(f"Curso: {registro.get('curso', 'N/A')}")
                    print(f"Nome do Professor: {registro.get('nome do professor', 'N/A')}")
                    print(f"Departamento: {registro.get('departamento do professor', 'N/A')}")
                    print(f"Nome da Disciplina: {registro.get('nome da disciplina', 'N/A')}")
                    print(f"Código da Disciplina: {registro.get('codigo da disciplina', 'N/A')}")
                    print(f"Professor Responsável: {registro.get('professor responsavel', 'N/A')}")
                    print("-" * 40)
            
            else:
                print("Consulta inválida.")

        def remover(colecao):
            id = input('Digite o ID do documento para remover (ex: 60b9b8f8e4b0c54c9e8d25b3): ')
            try:
                object_id = ObjectId(id) #transforma em objetoID
                result = colecao.delete_one({'_id': object_id}) #deletando objeto
                if result.deleted_count > 0: #se deletou..
                    print("Documento removido com sucesso!")
                else:
                    print("Nenhum documento encontrado com o ID fornecido.")
            except Exception as e:
                print(f"Erro ao remover o documento: {e}")

        def update(colecao):
            id = input('Digite o ID do documento para atualizar (ex: 60b9b8f8e4b0c54c9e8d25b3): ')
            try:
                object_id = ObjectId(id)
                resp_update = input('Qual documento deseja atualizar? \n (1) ALUNO \n (2) PROFESSOR \n (3) DISCIPLINA \n')
                if resp_update == '1':
                    novo_nome_aluno = input('NOVO NOME DO ALUNO: ')
                    while verificar_digito(novo_nome_aluno) == 1: #VD
                        print('Nao e possivel cadastrar alunos com numeros! ')
                        novo_nome_aluno = input('NOVO NOME DO ALUNO: ')
                    nova_matricula_aluno = input('NOVA MATRICULA DO ALUNO: ')
                    while verificar_digito(nova_matricula_aluno) == 0: #VD
                        print('Nao e possivel cadastrar uma matricula com letras!')
                        nova_matricula_aluno = input('NOVA MATRICULA DO ALUNO')
                    novo_curso_aluno = input('NOVO CURSO DO ALUNO: ')
                    while verificar_digito(novo_curso_aluno) == 1: #VD
                        print('Nao e possivel cadastrar um curso com numeros!')
                        novo_curso_aluno = input('NOVO CURSO ALUNO :')
                    novo_valor_aluno = {"$set": {'nome': novo_nome_aluno, 'matricula': nova_matricula_aluno, 'curso': novo_curso_aluno}} #DE
                    colecao.update_one({'_id': object_id}, novo_valor_aluno) #passa id como verificador e novo parametro(dicionario)
                    print('Aluno atualizado com sucesso!')
                elif resp_update == '2':
                    novo_nome_professor = input('NOVO NOME DO PROFESSOR: ')
                    while verificar_digito(novo_nome_professor) == 1: #VD
                        print('Nao e possivel cadastrar um professor com numeros!')
                        novo_nome_professor = input('NOVO NOME DO PROFESSOR: ')
                    novo_departamento_professor = input('NOVO DEPARTAMENTO DO PROFESSOR: ')
                    while verificar_digito(novo_departamento_professor) == 1: #VD
                        print('Nao e possivel cadastrar um departamento com numeros!')
                        novo_departamento_professor = input('NOVO DEPARTAMENTO DO PROFESSOR: ')
                    novo_valor_professor = {"$set": {'nome do professor': novo_nome_professor, 'departamento do professor': novo_departamento_professor}} #DE
                    colecao.update_one({'_id': object_id}, novo_valor_professor)
                    print('Professor atualizado com sucesso!')
                elif resp_update == '3':
                    novo_nome_disciplina = input('NOVO NOME DA DISCIPLINA: ')
                    while verificar_digito(novo_nome_disciplina) == 1: #VD
                        print('Nao e possivel cadastrar uma disciplina com numeros!')
                        novo_nome_disciplina = input('NOVO NOME DA DISCIPLINA: ')
                    novo_codigo_disciplina = input('NOVO CODIGO DE DISCIPLINA: ')
                    while verificar_digito(novo_codigo_disciplina) == 0: #VD
                        print('Nao e possivel cadastrar um codigo de disciplina com letras!')
                        novo_codigo_disciplina = input('NOVO CODIGO DE DISCIPLINA: ')
                    novo_professor_responsavel_disciplina = input('NOVO PROFESSOR RESPONSAVEL PELA DISCIPLINA: ')
                    while verificar_digito(novo_professor_responsavel_disciplina) == 1:#VD
                        print('Nao e possivel cadastrar um professor com numeros!')
                        novo_professor_responsavel_disciplina = input('NOVO PROFESSOR RESPONSAVEL PELA DISCIPLINA: ')
                    novo_valor_disciplina = {"$set": {'nome da disciplina': novo_nome_disciplina, 'codigo da disciplina': novo_codigo_disciplina, 'professor responsavel': novo_professor_responsavel_disciplina}}#DE
                    colecao.update_one({'_id': object_id}, novo_valor_disciplina)
                    print('Disciplina atualizada com sucesso!')
                else:
                    print("Documento inválido!")
            except Exception as e:
                print(f'Erro ao atualizar o 2 : {e}')

    # Funções de mapeamento de opções
        def opcao_cadastro_aluno():
            cadastrar_aluno(colecao)

        def opcao_cadastro_professor():
            cadastrar_professor(colecao)

        def opcao_cadastro_disciplina():
            cadastrar_disciplina(colecao)

        def opcao_consulta():
            consultar(colecao)

        def opcao_remover():
            remover(colecao)

        def opcao_update():
            update(colecao)

        # Main
        try:
            meu_banco = cliente['Projeto'] #pegando o banco
            colecao = meu_banco['Registro Escolar'] #pegando a colecao

            print('====CONECTADO AO REGISTRO ESCOLAR==== \n O que pretende fazer?')
            resp = input('1- Cadastro de ALUNO / 2- Cadastro de PROFESSOR / 3- Cadastro de DISCIPLINA / 4- Consulta de ALUNO, PROFESSOR ou DISCIPLINA / 5- Remover ALUNO, PROFESSOR ou DISCIPLINA / 6- Atualizar ALUNO, PROFESSOR ou DISCIPLINA \n')

            switch = { #switch para controlar as opcoes
                '1': opcao_cadastro_aluno,
                '2': opcao_cadastro_professor,
                '3': opcao_cadastro_disciplina,
                '4': opcao_consulta,
                '5': opcao_remover,
                '6': opcao_update
            }

            funcao = switch.get(resp) #.get serve para pegar a opcao do SWITCH CASE
            if funcao: # verifica se funcao nao eh null
                funcao()
            else:
                print("Opção inválida.")
        except Exception as e:
            print(e)

        continuar = int(input('Deseja encerrar o programa? : (1)SIM / (QUALQUER NUMERO INTEIRO)NAO \n'))

except Exception as e:
    print(f'Digito invalido{e}')
