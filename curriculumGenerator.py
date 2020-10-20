
# *************************************************************************************************
# FUNÇÕES

def cabecalho():
    curriculo = open('curriculo.html', 'a', -1, 'utf-8')
    curriculo.write("<!DOCTYPE html>\n")
    curriculo.write("<html lang=\"pt-br\">\n\n")
    curriculo.write("<head>\n")
    curriculo.write("\t<meta charset=\"UTF-8\">\n")
    curriculo.write("\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\n")
    curriculo.write("\t<title>Currículo</title>\n")
    curriculo.write("\t<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n")
    curriculo.write("\t<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css\" integrity=\"sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO\" crossorigin=\"anonymous\">\n")
    curriculo.write("</head>\n\n")
    curriculo.close()

# *************************************************************************************************

def dadosPessoais():
    curriculo = open('curriculo.html', 'a', -1, 'utf-8')
    # Pegando dados do usuário.
    print("\n === Dados Pessoais === ")
    nome = input("Insira seu nome completo: ")
    idade = input("Insira sua idade: ")
    celular = input("Insira seu número de celular: ")
    endereco = input("Insira seu endereço: ")
    email = input("Insira seu email: ")
    nacionalidade = input("Insira sua nacionalidade: ")
    estadoCivil = input("Insira seu estado civil: ")
    foto = input("Digite o caminho/link de uma imagem para foto de perfil: ")
    print("\n")

    curriculo.write("<body>\n")
    curriculo.write("\t<div class=\"container\">\n")
    curriculo.write("\t\t<h2 id=\"titulo\">CURRICULUM VITAE</h2>\n")
    curriculo.write("\t\t<hr/>\n")
    curriculo.write("\t\t<div class=\"row\">\n")
    curriculo.write("\t\t\t<div class=\"col-md-6\">\n")
    curriculo.write("\t\t\t\t<div class=\"foto\">\n")
    curriculo.write("\t\t\t\t\t<img src=\""+foto+"\" alt=\"Foto de Perfil\">\n")
    curriculo.write("\t\t\t\t</div>\n")
    curriculo.write("\t\t\t</div>\n")
    curriculo.write("\t\t\t<div class=\"col-md-6\">\n")
    curriculo.write("\t\t\t\t<div class=\"dados-pessoais\">\n")
    curriculo.write("\t\t\t\t\t<h4>DADOS PESSOAIS</h4>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Nome: </strong>"+nome+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Idade: </strong>"+idade+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Celular: </strong>"+celular+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Endereço: </strong>"+endereco+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>E-mail: </strong>"+email+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Nacionalidade: </strong>"+nacionalidade+"</p>\n")
    curriculo.write("\t\t\t\t\t<p><strong>Estado Cívil: </strong>"+estadoCivil+"</p>\n")
    curriculo.write("\t\t\t\t</div>\n")
    curriculo.write("\t\t\t</div>\n")
    curriculo.write("\t\t</div>\n")
    curriculo.write("\t\t<hr/>\n\n")
    curriculo.close()

# *************************************************************************************************

def formacaoAcademica():
    curriculo = open('curriculo.html', 'a', -1, 'utf-8')

    print(" === Ensino Superior === ")
    perguntaEnsinoSuperior = input("Você faz ou já fez o ensino superior? (1-Sim, 2-Não)")
    if perguntaEnsinoSuperior == '1':
        faculdade = input('Digite o nome da faculdade: ')
        curso = input("Digite o nome do curso: ")
        situacao = input("Digite a situação (Andamento ou Concluído): ")
        inicioFaculdade = input("Digite o ano que começou: ")
        fimFaculdade = input("Digite o ano que terminou ou vai terminar: ")
    else:
        faculdade = " "
        curso = " "
        situacao = " "
        inicioFaculdade = " "
        fimFaculdade = " "
    print("\n")

    print(" === Ensino Médio === ")
    perguntaEnsinoMedio = input("Você faz ou já fez o ensino médio? (1-Sim, 2-Não)")
    if perguntaEnsinoMedio == '1':
        escolaEnsinoMedio = input("Digite o nome da escola: ")
        situacaoEnsinoMedio = input("Digite a situação (Andamento ou Concluído): ")
        inicioEnsinoMedio = input("Digite o ano que começou: ")
        fimEnsinoMedio = input("Digite o ano que terminou ou vai terminar: ")
    else:
        escolaEnsinoMedio = " "
        situacaoEnsinoMedio = " "
        inicioEnsinoMedio = " "
        fimEnsinoMedio = " "
    print("\n")

    print(" === Ensino Fundamental === ")
    perguntaEnsinoFundamental = input("Você faz ou já fez o ensino fundamental? (1-Sim, 2-Não)")
    if perguntaEnsinoFundamental == '1':
        escolaEnsinoFundamental = input("Digite o nome da escola: ")
        situacaoEnsinoFundamental = input("Digite a situação (Andamento ou Concluído): ")
        inicioEnsinoFundamental = input("Digite o ano que começou: ")
        fimEnsinoFundamental = input("Digite o ano que terminou ou vai terminar: ")
    else:
        escolaEnsinoFundamental = " "
        situacaoEnsinoFundamental = " "
        inicioEnsinoFundamental = " "
        fimEnsinoFundamental = " "
    print("\n")

    curriculo.write("\t\t<div class=\"formacao-academica\">\n")
    curriculo.write("\t\t\t<h4>FORMAÇÃO ACADÊMICA</h4>\n\n")
    curriculo.write("\t\t\t<div class=\"row\">\n")
    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"ensino-superior\">\n")
    curriculo.write("\t\t\t\t\t\t<h5>ENSINO SUPERIOR</h5>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Nome da faculdade: </strong>"+faculdade+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Nome do curso: </strong>"+curso+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Situação do curso: </strong>"+situacao+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Início do curso: </strong>"+inicioFaculdade+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Fim do curso: </strong>"+fimFaculdade+"</p>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n\n")

    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"ensino-medio\">\n")
    curriculo.write("\t\t\t\t\t\t<h5>ENSINO MÉDIO</h5>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Nome da escola: </strong>"+escolaEnsinoMedio+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Situação: </strong>"+situacaoEnsinoMedio+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Data de início: </strong>"+inicioEnsinoMedio+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Data do fim: </strong>"+fimEnsinoMedio+"</p>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n\n")

    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"ensino-fundamental\">\n")
    curriculo.write("\t\t\t\t\t\t<h5>ENSINO FUNDAMENTAL</h5>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Nome da escola: </strong>"+escolaEnsinoFundamental+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Situação: </strong>"+situacaoEnsinoFundamental+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Data de início: </strong>"+inicioEnsinoFundamental+"</p>\n")
    curriculo.write("\t\t\t\t\t\t<p><strong>Data do fim: </strong>"+fimEnsinoFundamental+"</p>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n")
    curriculo.write("\t\t\t</div>\n")
    curriculo.write("\t\t</div>\n")
    curriculo.write("\t\t<hr/>\n\n")
    curriculo.close()

# *************************************************************************************************

def areasInteresse():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    continuar = 1
    
    print(" === Áreas de Interesse === ")
    curriculo.write("\t\t<div class=\"informacoes-complementares\">\n")
    curriculo.write("\t\t\t<div class=\"row\">\n")
    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"areas-interesse\">\n")
    curriculo.write("\t\t\t\t\t\t<h4>ÁREAS DE INTERESSE</h4>\n")
    curriculo.write("\t\t\t\t\t\t<ul>\n")

    while (continuar == 1):
        areaInteresse = input("Adicione uma área de interesse: ")
        curriculo.write("\t\t\t\t\t\t\t<li>"+areaInteresse+"</li>\n")
        continuar = int(input("Deseja continuar adicionando? (1-Sim 2-Não)"))

    print("\n")
    curriculo.write("\t\t\t\t\t\t</ul>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n\n")
    curriculo.close()

# *************************************************************************************************

def competenciasEhabilidades():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    continuar = 1
    
    print(" === Competências e Habilidades === ")
    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"competencias-habilidades\">\n")
    curriculo.write("\t\t\t\t\t\t<h4>COMPETÊNCIAS E HABILIDADES</h4>\n")
    curriculo.write("\t\t\t\t\t\t<ul>\n")

    while (continuar == 1):
        competenciasEhabilidades = input("Adicione uma competência e/ou habilidade: ")
        curriculo.write("\t\t\t\t\t\t\t<li>"+competenciasEhabilidades+"</li>\n")
        continuar = int(input("Deseja continuar adicionando? (1-Sim 2-Não)"))

    print("\n")
    curriculo.write("\t\t\t\t\t\t</ul>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n\n")
    curriculo.close()

# *************************************************************************************************

def idiomas():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    continuar = 1
    
    print(" === Idiomas === ")
    curriculo.write("\t\t\t\t<div class=\"col-md-4\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"idiomas\">\n")
    curriculo.write("\t\t\t\t\t\t<h4>IDIOMAS</h4>\n")
    curriculo.write("\t\t\t\t\t\t<ul>\n")

    while (continuar == 1):
        idiomas = input("Adicione um idioma: ")
        nivel = input("Qual o nível nesse idioma? (Básico, Intermediário ou Fluente): ")
        curriculo.write("\t\t\t\t\t\t\t<li>"+idiomas+" - Nível: "+nivel+"</li>\n")
        continuar = int(input("Deseja continuar adicionando? (1-Sim 2-Não)"))

    print("\n")
    curriculo.write("\t\t\t\t\t\t</ul>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n")
    curriculo.write("\t\t\t</div>\n")
    curriculo.write("\t\t</div>\n")
    curriculo.write("\t\t<hr/>\n\n")
    curriculo.close()

# *************************************************************************************************

def projetos():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    continuar = 1
    
    print(" === Projetos === ")
    curriculo.write("\t\t<div class=\"carreira\">\n")
    curriculo.write("\t\t\t<div class=\"row\">\n")
    curriculo.write("\t\t\t\t<div class=\"col-md-6\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"projetos\">\n")
    curriculo.write("\t\t\t\t\t\t<h4>PROJETOS</h4>\n")
    curriculo.write("\t\t\t\t\t\t<ul>\n")

    while (continuar == 1):
        projetos = input("Adicione um projeto que você participou: ")
        curriculo.write("\t\t\t\t\t\t\t<li>"+projetos+"</li>\n")
        continuar = int(input("Deseja continuar adicionando? (1-Sim 2-Não)"))

    print("\n")
    curriculo.write("\t\t\t\t\t\t</ul>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n\n")
    curriculo.close()

# *************************************************************************************************

def trabalhos():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    continuar = 1
    
    print(" === Trabalhos === ")
    curriculo.write("\t\t\t\t<div class=\"col-md-6\">\n")
    curriculo.write("\t\t\t\t\t<div class=\"trabalhos\">\n")
    curriculo.write("\t\t\t\t\t\t<h4>TRABALHOS</h4>\n")
    curriculo.write("\t\t\t\t\t\t<ul>\n")

    while (continuar == 1):
        trabalhos = input("Adicione um lugar em que você trabalhou: ")
        funcao = input("Qual a sua função nesse trabalho: ")
        salario = input("Qual era seu salario: ")
        curriculo.write("\t\t\t\t\t\t\t<li>"+trabalhos+" - "+funcao+" - "+salario+"</li>\n")
        continuar = int(input("Deseja continuar adicionando? (1-Sim 2-Não)"))

    print("\n")
    curriculo.write("\t\t\t\t\t\t</ul>\n")
    curriculo.write("\t\t\t\t\t</div>\n")
    curriculo.write("\t\t\t\t</div>\n")
    curriculo.write("\t\t\t</div>\n")
    curriculo.write("\t\t</div>\n\n")
    curriculo.write("\t</div>\n\n")
    curriculo.close()

# *************************************************************************************************
def fechamento():
    curriculo = open('curriculo.html','a', -1, 'utf-8')
    curriculo.write("</body>\n")
    curriculo.write("</html>")
    curriculo.close()

# *************************************************************************************************
# PROGRAMA PRINCIPAL

cabecalho()
dadosPessoais()
formacaoAcademica()
areasInteresse()
competenciasEhabilidades()
idiomas()
projetos()
trabalhos()
fechamento()

# *************************************************************************************************
