# Adicionando itens na lista=inventario
inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))  # Append realiza a inserção de elementos na lista
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

# Retornar Elementos
for elemento in inventario:
    print(elemento)
