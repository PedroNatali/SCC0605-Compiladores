import lexico

######################################## ANALISADOR SINTÀTICO

##### MELHOR MUDAR AS E CHAMAR A FUNCAO DO JEITO 
###### token, i = program(token, i, text)
	###### Pq dai eu n preciso chamar as funcoes uma dentro da outra necessariamente 

def analisador_sintatico(tabela, i, text):
	tabela, i = lexico.nextToken(tabela, i, text)
	token = tabela[len(tabela) - 1][1]
	print(token)
	token, i = program(token,tabela, i, text)	
	token, i = dc_c(token,tabela, i, text)
	token, i = dc_v(token, tabela,i, text)
	token, i = dc_p(token, tabela, i, text)

	if(token == "simb_begin"):
		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			token, i = cmd(token, tabela, i, text)
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			if(token == "simb_pv"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_end"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			if(token == "simb_p"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				print("Sucess")


	print("Sucess (prévio)")


def program(token, tabela, i, text):
	if (token == "simb_program"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "id"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: id esperado")
			
		if(token == "simb_pv"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			print("saida do program")
			return token, i
		else:
			print("Erro sintático: ; esperado")
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			print("saida do program")
			return token, i

def dc_c(token, tabela, i, text):
	if(token == "simb_const"):
		i = i + 1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "id"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)

		else:
			print("Erro sintático: id esperado")

		if(token == "simb_igual"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: = esperado")
			#TALVEZ PRECISE COLOCAR SIMBOLO ESPECIAL PRA INT E FLOAT

		if(token == "simb_tipo"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: int ou float esperado")

		if(token == "simb_pv"):
			i = i + 1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: ; esperado")

		if(token == "simb_const"):
			print("recursao dc_c")
			dc_c(token, i, text)
		else:
			print("saida do dc_c")
			return token, i
	else:
		print("saida do dc_c")
		return token, i

def dc_v(token, tabela, i, text):
	if(token == "simb_var"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "id"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: id esperado")

		while(token == "simb_v"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]

			if(token == "id"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
			else:
				print("Erro sintático: id esperado")

		if (token == "simb_dp"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: esperado")

		if(token == "simb_tipo"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: integer ou real esperado")

		if(token == "simb_pv"):
			i = i +1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: ; esperado")

		if(token == "simb_var"):
			print("recursao dc_v")
			dc_v(token,tabela, i, text)
		else:
			print("saida do dc_v")
			return token, i

	else:
		print("saida do dc_v")
		return token, i

def dc_p(token, tabela, i, text):
	if(token == "simb_procedure"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "simb_apar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: ( esperado")

		if(token != "id"):
			print("Erro sintático: id esperado")

		while(token == "id"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)

			while(token == "simb_v"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				print(token)

				if(token == "id"):
					i = i+1
					tabela, i = lexico.nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
				else:
					print("Erro sintático: id esperado")

		if(token == "simb_dp"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: : esperado")
		
		if(token == "simb_tipo"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: integer ou real esperado")

		if(token == "simb_pv"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: ; esperado")

		if (token == "simb_fpar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: ) esperado")
		if(token == "simb_pv"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			#Chama corpo_p
			token, i = corpo_p(token, i, text)
			print(token)
			return token, i
		else:
			print("Erro sintático: ; esperado")
			return token, i

	else:
		return token, i


def corpo_p(token, tabela, i, text):
	dc_v(token, i, text)
	i = i+1
	tabela, i = lexico.nextToken(tabela, i, text)
	token = tabela[len(tabela)-1][1]
	print(token)

	if(token == "simb_begin"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			#token, i = cmd(token, i, text)
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)

			if(token == "simb_pv"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				print(token)
			else:
				print("Erro sintático: ; esperado")

		if(token == "simb_end"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático: end esperado")

		if(token == "simb_pv"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			return token, i
		else:
			print("Erro sintático: . esperado")
			return token, i
	else:
		print("Erro sintático: begin esperado")
		return token, i


def cmd(token,tabela,i,text):
	print(token)
	if(token == "simb_read" or token == "simb_write"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "simb_apar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: ( esperado")
		print(token)
		if(token == "id"):
			while(token == "id"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				if(token == "simb_v"):
					print(token)
					i = i+1
					tabela, i = lexico.nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					print(token)
				elif(token == "simb_fpar"):
					break
				else:
					print("Erro sintático: , esperado")
		else:
			print("ERRO: id")
		if(token == "simb_fpar"):
			print(token)
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: ) esperado")
		print(token)
		if(token == "simb_pv"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			return token, i
		else:
			print("Erro sintático: ; esperado")
			return token, i
	elif(token == "simb_while"):
		print("oi1")
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "simb_apar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: ( esperado")
		#token, i = condicao()
		print(token)
		if(token == "simb_fpar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: ) esperado")
		print(token)
		if(token == "simb_do"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: do esperado")
		return cmd(token,tabela,i,text)
	elif(token == "simb_if"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		#token, i = condicao(token, tabela, i, text)
		print(token)
		if(token =="simb_then"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: then esperado")
		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			token,i = cmd(token,tabela,i,text)
			print(token)
			if(token == "simb_else"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
			elif(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
				continue
			else:
				return token,i
	elif(token == "simb_begin"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		if(token == "simb_read" or token == "simb_write" or token == "simb_if" or token == "simb_while" or token == "id" or token == "simb_for"):
			token,i = cmd(token,tabela,i,text)
			print(token+" oi")
			if(token == "simb_pv"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
			else:
				print("Erro sintático: ; esperado")
			print(token)
			if(token == "simb_end"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				return token,i
			else:
				print("Erro sintático: end esperado")
				return token,i
	elif(token == "id"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "simb_atrib"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			#token, i = expressao(token,tabela,i, text)
		elif(token == "simb_apar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			if(token == "id"):
				while(token == "id"):
					i = i+1
					tabela, i = lexico.nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					print(token)
					if(token == "simb_pv"):
						i = i+1
						tabela, i = lexico.nextToken(tabela, i, text)
						token = tabela[len(tabela)-1][1]
					elif(token == "simb_fpar"):
						break
					else:
						print("Erro sintático: ; esperado")
			else:
				print("ERRO: id")
				print(token)
			if(token == "simb_fpar"):
				i = i+1
				tabela, i = lexico.nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				return token, i 
		else:
			print("Erro sintático: := esperado")
			return token, i
	return token, i


def expressao(token,tabela,i, text):
	print(token)
	if(token == "simb_soma" or token == "simb_sub"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
	if(token == "id"):
		print("token")
	elif(token == "simb_apar"):
		i = i+1
		tabela, i = lexico.nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print("expressao")
		#token, i = expressao(token,tabela,i, text)
		if(token == "simb_fpar"):
			i = i+1
			tabela, i = lexico.nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático: := esperado")
	else:
		print("Erro sintático: expressao esperado")



######################################## FIM 	