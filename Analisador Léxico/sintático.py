#@authors Pedro Natali, Rafael Pinho, Patrick Feitosa


def declare_variable(token, i):

	if(token == "simb_var"):
		i = i+1
		print(tabela[i][1])
		token = tabela[i][1]

		if(token == "id"):
			i = i+1
			token = tabela[i][1]

			while(token == "simb_v"):
				i = i+1
				token = tabela[i][1]
				if(token == "id"):
					i = i+1
					token = tabela[i][1]
				else:
					print("Erro sintático: 'id' esperado")

			if (token == "simb_dp"):
				i = i+1
				token = tabela[i][1]

				if(token == "num_int" or token == "num_float"):
					i = i+1
					token = tabela[i][1]

					if(token == "simb_pv"):
						return True
						token = tabela[i][1]

					else:
						print("Erro sintático: ';' esperado")

				else:
					print ("Erro sintático: 'tipo' esperado")

			#PROBLEMA AQUI, VEM x@ --> ELE considera os tokens id/erro (O token ERRO fode com o rolê, deveria dar o erro sem estar nos tokens a ser visto!)
			else:
				print ("Erro sintático: ':' ou ',' esperado")

		else:
			print ("Erro sintático: 'id' esperado")

	else:
		return "Saindo"

	

	if(token == "simb_var"):
		declare_variable(token, i)


# --> Problema do condition atual é que comeca em ID sendo que vários outros também comecam. O problema é que leria o próximo token desconsiderando o ID
# --> Solucao eh retroceder o i para encontrar o mesmo ID quando for rodar em outra aplicação 

# def condition(token, i):
# 	if(token == "id"):
# 		nextToken()
# 		if (token == ("+" or "-" or "/" or "*") ):
# 			nextToken()
# 			if(token == "id"):
# 				nextToken()
# 				if (token == "comparativos"):
# 					nextToken()
# 					if(token == "id"):
# 						condition(token, i)
# 					else:
# 						return "sucesso"
# 				else:
# 					return "sucesso"
# 			else:
# 				return "Erro sintático, segundo termo esperado"
# 		else:
# 			return "sucesso"
# 	else:
# 		return "saindo"	

### TEM QUE COLOCAR CONST_ID NO CÓDIGO DO ANALISADOR LEXICO, NAO TINHA ISSO ANTES 
# def declare_constant(token, i):
# 	if (token == "const_ID"):
# 		if(token == ":"):
# 			if(token == "num_int" or token == "num_float"):
# 				if(token == "simb_pv"):
# 					print("Sucess")
# 				else:
# 					print("Erro sintático: ';' esperado")
# 			else:
# 				print("Erro sintático, tipo esperado")
# 		else:
# 			print("Erro sintático, ':' esperado")
# 	else:
# 		return



# def corpo_p(token, id):
# 	declare_variable()

# 	if(token == "begin"):
# 		token = nextToken()
# 		#INICIO PROGRAMA

# 		#comandos
# 		CMD()


# 		#FIM PROGRAMA
# 		if (token == "end"):
# 			token = nextToken()
# 			if(token == "."):
# 				print("Sucess")
# 			else:
# 				print("Erro sintático, '.' esperado")
# 		else:
# 			print("Erro sintático, 'end' esperado")
# 	else:
# 		print("Erro sintático, 'begin' esperado")



#retorna o arquivo texto como uma string
def ler_arquivo(arquivo):           
	arq = open(arquivo,'r')
	text = arq.read()
	arq.close()
	return text


if __name__ == '__main__':
	arquivo_entrada = "saida.txt"
	arquivo_saida = "saida2.txt"
	saida = open(arquivo_saida,'w')

	text = ler_arquivo(arquivo_entrada)

	tabela = []
	tabela = (["var", "simb_var"], ["x", "id"], ["@", "erro(caractere não permitido)"], [":", "simb_dp"], ["integer", "num_int"], [";", "simb_pv"])

	i = 0
	#Enquanto nao terminar o texto, utilize os automatos
	while(i < len(tabela)):
		token = tabela[i][1]
		
		declare_variable(token, i)
		i = i+1



	saida.close()

