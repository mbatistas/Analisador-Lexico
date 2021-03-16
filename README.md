# Analisador-Lexico
Análise léxica de calculadora baseada em regex.

# Requisitos
Python 3.6+

# Como usar
Execute o arquivo main.py em um compilador Python 3.6 ou superior. O código vai pedir para escrever a expressão. Caracteres válidos são números, operações básicas (+, -, *, /, **), parênteses e comentários (#). Comentáriossão desconsiderados e podem ser encerrados com outra cerquilha (#).
# Exemplo:
__Input:__
```
1+2-3*4/(5**6)#COMENTÁRIO#8+99
```

__Output:__

```
| Lexema  |   Tipo  |    Valor    |
|    1    |  Número |      1      |
|    +    | Operador|     Soma    |
|    2    |  Número |      2      |
|    -    | Operador|  Subtração  |
|    3    |  Número |      3      |
|    *    | Operador|Multiplicação|
|    4    |  Número |      4      |
|    /    | Operador|   Divisão   |
|    (    |Parêntese|Parêntese Esq|
|    5    |  Número |      5      |
|   **    | Operador|  Potência   |
|    6    |  Número |      6      |
|    )    |Parêntese|Parêntese Dir|
|    8    |  Número |      8      |
|    +    | Operador|     Soma    |
|    99    |  Número |      99      |
```

# Como funciona
A função gerarTokens(entrada) tem como input uma string, reconhece os tokens por meio de expressões regulares e retorna uma lista de strings com os tokens em ordem. São reconhecidos números, operações básicas (+,-,*,/,\*\*), parênteses e comentários (abre e fecha comentário com #). Caso haja algum caractere inválido ou comentário não encerrado, a função imprime que houve erro e retorna uma lista vazia.  
A função imprimirTabelaTokens(x) tem como entrada uma lista de strings, imprime a tabela do resultado da análise e não retorna nada. Caso a função anterior tenha dado erro ou o input seja vazio, uma mensagem será impressa.
