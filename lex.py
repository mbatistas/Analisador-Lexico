import re

#número. aceita grupos de númerais
regexNumero = ("\d+")
#operador +, -, *, ** ou /
regexOperador = ("(\*\*|\*|\/|\+|\-)")
#parêntese, abrindo ou fechando
regexParentese = ("(\(|\))")
#comentário, começa com #, tem número indefinido de caracteres que não seja # ou fim de string e termina com # ou fim de string
regexComentario = ("#[^#]*(#|$)")


#input: string de entrada
#output: lista de tokens
def gerarTokens(entrada):
    tokens = []
    while len(entrada) > 0:
        #testa se o regex existe e começa da posição zero, então atribui a tam
        if re.search(regexNumero, entrada) != None and re.search(regexNumero, entrada).start() == 0:
            tam = re.search(regexNumero, entrada)
            i = tam.end()
            tokens.append(entrada[:i])

        elif re.search(regexOperador, entrada) != None and re.search(regexOperador, entrada).start() == 0:
            #atribui o índice do ultimo caractere do match
            tam = re.search(regexOperador, entrada)
            i = tam.end()
            #insere os caracteres do índice 0 ao i da string na lista de tokens
            tokens.append(entrada[:i])

        elif re.search(regexParentese, entrada) != None and re.search(regexParentese, entrada).start() == 0:
            tam = re.search(regexParentese, entrada)
            i = tam.end()
            tokens.append(entrada[:i])

        elif re.search(regexComentario, entrada) != None and re.search(regexComentario, entrada).start() == 0:
            #comentários não são adicionados à lista de tokens
            tam = re.search(regexComentario, entrada)
            i = tam.end()
        else:
            print("ERRO: CARACTERE INVÁLIDO! ", entrada[0])
            return []
        #remove o token da string
        entrada = entrada[i:]
    
    return tokens


#input: lista de tokens
#output: ---
def imprimirTabelaTokens(tokens):
    if len(tokens) == 0:
        print("Não há texto a ser analizado.")
        return
    
    #imprime cabeçalho
    print("| Lexema  |   Tipo  |    Valor    |")
    #percorre a lista de tokens
    for item in tokens:
        #testa os regex em cada item e imprime na tela
        if re.search(regexNumero, item) != None:
            print("|   ", item, "   |  Número |     ", item, "     |")
        
        elif re.search(regexOperador, item) != None:
            if item == "+":
                print("|   ", item, "   | Operador|     Soma    |")
            elif item == "-":
                print("|   ", item, "   | Operador|  Subtração  |")
            elif item == "*":
                print("|   ", item, "   | Operador|Multiplicação|")
            elif item == "/":
                print("|   ", item, "   | Operador|   Divisão   |")
            elif item == "**":
                print("|  ", item, "   | Operador|  Potência   |")
        
        elif re.search(regexParentese, item) != None:
            if item == "(":
                print("|   ", item, "   |Parêntese|Parêntese Esq|")
            elif item == ")":
                print("|   ", item, "   |Parêntese|Parêntese Dir|")

    return