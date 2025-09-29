# Aula 4 – Estruturas Condicionais em Python
# Este programa pede ao usuário uma nota e dá um retorno baseado no valor.

# Aqui pedimos ao usuário para digitar a nota.
# O input sempre retorna texto (string), então usamos float() para converter para número decimal.
nota = float(input("Digite sua nota: "))

# Agora verificamos se a nota é maior ou igual a 9.
# Se for, significa um desempenho excelente.
if nota >= 9:
    print("Excelente! Você mandou muito bem!")

# Se a nota não for >= 9, o Python vem para este elif (senão se).
# Aqui ele verifica se a nota é maior ou igual a 7.
# Nesse caso, consideramos como aprovado.
elif nota >= 7:
    print("Parabéns, você está aprovado.")

# Se nenhuma das condições anteriores for verdadeira (nota < 7),
# o Python cai no bloco else, que cobre todos os outros casos.
# Aqui, a resposta é de reprovação.
else:
    print("Precisamos continuar tentando, não foi dessa vez.")
    