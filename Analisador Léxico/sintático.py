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
						token = input()

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

