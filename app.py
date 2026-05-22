# Exibe um cabeçalho decorativo e amigável no console para o usuário
print("--- Bem-vindo à Calculadora de IMC ---")

# Solicita o peso do usuário, converte o texto digitado (string) para um número decimal (float) e armazena na variável 'peso'
peso = float(input("Digite o seu peso em kg (ex: 70.5): "))

# Solicita a altura do usuário, converte para número decimal (float) e armazena na variável 'altura'
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Calcula o IMC dividindo o peso pela altura elevada ao quadrado e armazena o resultado na variável 'imc'
imc = peso / (altura ** 2)

# Imprime uma linha em branco ("\n") seguida de 30 caracteres "=" para criar uma linha divisória visual
print("\n" + "="*30)

# Exibe o valor do IMC calculado, usando uma f-string para formatar o número com apenas duas casas decimais (:.2f)
print(f"Seu IMC atual é: {imc:.2f}")

# Verifica se o IMC é menor que 18.5. Se for verdadeiro, executa o bloco abaixo e ignora os outros
if imc < 18.5:
    print("Classificação: Abaixo do peso")

# Se a condição anterior for falsa, verifica se o IMC está entre 18.5 (inclusive) e menos que 25.0
elif 18.5 <= imc < 25.0:
    print("Classificação: Peso normal (Parabéns!)")

# Se as anteriores forem falsas, verifica se o IMC está entre 25.0 (inclusive) e menos que 30.0
elif 25.0 <= imc < 30.0:
    print("Classificação: Sobrepeso")

# Se as anteriores forem falsas, verifica se o IMC está entre 30.0 (inclusive) e menos que 35.0
elif 30.0 <= imc < 35.0:
    print("Classificação: Obesidade Grau I")

# Se as anteriores forem falsas, verifica se o IMC está entre 35.0 (inclusive) e menos que 40.0
elif 35.0 <= imc < 40.0:
    print("Classificação: Obesidade Grau II (Severa)")

# Se o IMC não se encaixou em NENHUMA das condições anteriores (ou seja, é 40.0 ou mais), executa este bloco
else:
    print("Classificação: Obesidade Grau III (Mórbida)")

# Imprime outra linha divisória com 30 caracteres "=" para fechar o bloco visual do resultado
print("="*30)

# Exibe uma mensagem final de orientação e aviso importante para o usuário
print("Dica: Lembre-se de que o IMC é apenas um indicador geral e não substitui uma avaliação médica profissional.")