# This example presents the use of Flow Control Structures in Python
# Este exemplo apresenta o uso de Estruturas de Controle de Fluxo em Python

# Line 1 >> Declaration of the variable 'num' and assignment of the value to it. # Declaração da variável 'num' e atribuição de valor a ela.
num = 40  

# Line 2 >> This is the start of an if statement. If is a keyword used to control conditional execution of code blocks. The condition to check is num % 2 == 0. # Este é o início de uma instrução if. If é uma palavra-chave  usada para controlar a execução condicional de blocos de código. A condição a ser verificada é num % 2 == 0.
# Line 3 >> This line is within the if block, meaning it will only be executed if the condition num % 2 == 0 is True. This function print(num, "it's even") shows the value inside the parentheses in the console. # Esta linha está dentro do bloco if, ou seja, só será executada se a condição num % 2 == 0 for Verdadeira. A função print(numero, "é par") mostra no console o valor entre parênteses.
# Line 4 >> This keyword marks the start of the else block. The else block is executed only when the condition in the preceding if statement is evaluated to False. In this case, the else block will be executed if num % 2 != 0, meaning if number is not exactly divisible by 2 (it means, odd). # Esta palavra-chave marca o início do bloco else. O bloco else é executado somente quando a condiçao da instrução if anterior é avaliada como False. Neste caso, o bloco else será executado se num % 2 != 0, ou seja se número não for exatamente divisível por 2 (ou seja, ímpar).
# Line 5 >> This line in inside the else block and will only be executed when the num is the odd. The function print, shows the text "is odd". # Esta linha está dentro do bloco else e só será executada quando o num for ímpar. A função print mostra o texto "é impar".
if num % 2 == 0:  
    print(num, "it's even") 
else:    
    print(num, "it's odd")   


