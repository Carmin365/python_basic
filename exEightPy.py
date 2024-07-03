# This program exemplifies the use of Dictionaries in the Python language 
# Este programa exemplifica o uso de Dicionários na linguagem Python

# Line 1 >> # Here 'person' is the dictionary # Aqui 'pessoa' é o Dicionário.
person = {"name": "Felipa", "age": 39, "city": "Flores"} 

# Line 2 >> Accesses the value of the key "name" (Felipa) # Acessa o valor da chave "nome" (Fulano)
# Line 3 >> Modify the value of the key "city" # Modifica o valor da chave "cidade"
# Line 4 >> Starts a for loop |  # Inicia um loop for | Defines two variables to store the iterated elements | Define duas varáveis para armazenar os elementos iterados. | Calls the method items() of the dictionaries person | Chama o método items() do dicionário pessoa.
# Line 5 >> Print prints these values to the console | # Print imprime estes valores no console.
print(person["name"])  
person["city"] = "Triunfo"  
for key, value in person.items():       
    print(key, ": ", value) 

