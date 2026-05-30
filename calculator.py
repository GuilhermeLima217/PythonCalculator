print ("Bem-vindo à minha calculadora!")
print ("% = Resto da divisão")
print ("** = Potenciação")
while True:
	try:
		numero1 = float(input("Digite o número: "))
	
		operacao = input("Digite a operação: (+, -, x, ÷, % ou **): ").lower ()
	
		numero2 = float(input("Digite o número: "))
	
		if operacao == "+":
			print (f"{numero1} + {numero2} = {numero1 + numero2}")
		elif operacao == "-":
			print (f"{numero1} - {numero2} = {numero1 - numero2}")
		elif operacao == "x":
			print (f"{numero1} x {numero2} = {numero1 * numero2}")
		elif operacao =="÷" and numero2 == 0:
			print ("Não é possível dividir um número por zero.")
		elif operacao == "÷":
			print (f"{numero1} ÷ {numero2} = {numero1 / numero2}")
		elif operacao =="%" and numero2 == 0:
			print ("Não é possível dividir um número por zero.")
		elif operacao == "%":
			print (f"{numero1} % {numero2} = {numero1 % numero2}")
		elif operacao == "**":
			print (f"{numero1} ** {numero2} = {numero1 ** numero2}")
		else:
			print ("Operação inválida.")
		continuar = input("Quer continuar? (s/n): ").lower ()
		if continuar != "s":
			break
	except:
		print ("Digite uma opção válida.")