# This program exemplifies the use of Dictionaries in the Python language 
# Este programa exemplifica o uso de Dicionários na linguagem Python

person = {"name": "Felipa", "age": 39, "city": "Flores"} # Here 'person' is the dictionary # Aqui 'pessoa' é o Dicionário.

print(person["name"]) # Accesses the value of the key "name" (Felipa) # Acessa o valor da chave "nome" (Fulano)
person["city"] = "Triunfo" # Modify the value of the key "city" # Modifica o valor da chave "cidade"
for key, value in person.items(): # Starts a for loop |  # Inicia um loop for | Defines two variables to store the iterated elements | Define duas varáveis para armazenar os elementos iterados. | Calls the method items() of the dictionaries person | Chama o método items() do dicionário pessoa.     
    print(key, ": ", value) # Print prints these values to the console | # Print imprime estes valores no console.

