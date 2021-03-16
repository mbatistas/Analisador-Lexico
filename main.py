from lex import *

entrada = input("Caracteres válidos:\nI.   Números\nII.  Operações (+, -, *, /, **)\nIII. Parênteses\nIV. Comentários (começa com # e pode terminar com #)\n\nImprima a expressão abaixo:\n")
x = gerarTokens(entrada)
imprimirTabelaTokens(x)