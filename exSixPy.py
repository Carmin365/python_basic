# This program exemplifies the use of functions in the Python language
# Este programa exemplifica o uso das funções na linguagem Python 

def somar(number_one, number_two): # Defines the word 'add', and the content inside the parentheses are two parameters that are being assigned to the function. The colon (:) after closing the parentheses signals the beginning of the function body. # Define a palavra 'somar', e o conteúdo que está dentro dos parênteses são dois parâmetros que estão sendo atribuídos à função. Os dois pontos (:) após o fechamento dos parênteses, sinalizam para o começo do corpo da função.
    resultado = number_one + number_two # Declaration of variable 'result' and assigning two values together with the sum of them. The result of the operation is stored in the 'result' variable. # Declaração da variável 'resultado' e atribuição de dois valores juntamente com a soma dos mesmos. O resultado da operação é armazenado na variável 'resultado'.  
    return resultado # Returns the value of the variable 'result' out of the function. # Retorna o valor da variável 'resultado' para fora da função.

    soma_total = somar(10, 20) # Declaration of variable 'sum_total' and assigning a value to it. # Declaração da variável 'soma_total' e atribuição de um valor à ela. 
    print(soma_total) # Print(sum_total) displays the value inside the parentheses in the control, in this case, the result of the operation performed on the previous line.  # Print(soma_total) exibe no console o valor que está dentro dos parênteses, neste caso, o resultado da operação realizada na linha anterior.

