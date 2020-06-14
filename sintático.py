

######################################## ANALISADOR SINTÀTICO

##### MELHOR MUDAR AS E CHAMAR A FUNCAO DO JEITO 
###### token, tabela, i = program(token, tabela, i, text)
###### Pq dai eu n preciso chamar as funcoes uma dentro da outra necessariamente 

def analisador_sintatico(tabela, i, text):
	tabela, i = nextToken(tabela, i, text)
	token = tabela[len(tabela) - 1][1]
	token, tabela, i = program(token, tabela, i, text)	
	print(tabela)
	token, tabela, i = dc_c(token, tabela, i, text)
	print(tabela)
	token, tabela, i = dc_v(token, tabela, i, text)


def program(token, tabela, i, text):
	print(token)
	if (token == "simb_program"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "id"):
			i = i + 1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			if(token == "simb_pv"):
				i = i + 1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				print("Sai do PROGRAM")
				return token, tabela, i

def dc_c(token, tabela, i, text):
	if(token == "simb_const"):
		i = i + 1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		if(token == "simb_igual"):
			i = i + 1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			#TALVEZ PRECISE COLOCAR SIMBOLO ESPECIAL PRA INT E FLOAT
			if(token == "simb_tipo"):
				i = i + 1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				if(token == "simb_pv"):
					i = i + 1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					if(token == "simb_const"):
						print("MAIS UM C")
						dc_c(token, tabela, i, text)
					else:
						print("SAI DO DC_C")
						return token, tabela, i
	else:
		print("SAI DO DC_C")
		return token, tabela, i

def dc_v(token, tabela, i, text):
	if(token == "simb_var"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]

		if(token == "id"):
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]

			while(token == "simb_v"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]

				if(token == "id"):
					i = i+1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
				else:
					print("Erro sintático: 'id' esperado")

			if (token == "simb_dp"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]

				if(token == "num_int" or token == "num_float"):
					i = i+1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]

					if(token == "simb_pv"):
						i = i +1
						tabela, i = nextToken(tabela, i, text)
						token = tabela[len(tabela)-1][1]
						if(token == "simb_var"):
							print("Mais um Dc_V")
							dc_v(token, tabela, i, text)
						else:
							print("Iria para o dc_p")
							return token, tabela, i
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
		print("Iria para o dc_p")
		return token, tabela, i

def dc_p(token, tabela, i, text):
	if(token == "simb_procedure"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		if(token == "simb_apar"):
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]

			while(token == "id"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				while(token == "simb_v"):
					i = i+1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					if(token == "id"):
						i = i+1
						tabela, i = nextToken(tabela, i, text)
						token = tabela[len(tabela)-1][1]
					else:
						pass

				if(token == "simb_dp"):
					i = i+1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					if(token == "simb_tipo"):
						i = i+1
						tabela, i = nextToken(tabela, i, text)
						token = tabela[len(tabela)-1][1]
						if(token == "simb_pv"):
							i = i+1
							tabela, i = nextToken(tabela, i, text)
							token = tabela[len(tabela)-1][1]

			if (token == "simb_fpar"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]


		if(token == "simb_pv"):
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]

			token, tabela, i = corpo_p(token, tabela, i, text)
			return token, tabela, i



		else:
			pass
	
	else:
		return token, tabela, i


def corpo_p(token, tabela, i, text):
	dc_v(token, tabela, i, text)
	i = i+1
	tabela, i = nextToken(tabela, i, text)
	token = tabela[len(tabela)-1][1]

	if(token == "simb_begin"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == simb_begin):
			#token, tabela, i = cmd(token, tabela, i, text)
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			if(token == "simb_pv"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_end"):
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			if(token == "simb_pv"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				return token, tabela, i


######################################## FIM 