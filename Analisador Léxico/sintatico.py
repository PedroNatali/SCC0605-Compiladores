import lexico

######################################## ANALISADOR SINTÀTICO

##### MELHOR MUDAR AS E CHAMAR A FUNCAO DO JEITO 
###### token, i, linha = program(token, i, linha, text)
	###### Pq dai eu n preciso chamar as funcoes uma dentro da outra necessariamente 

def analisador_sintatico(tabela, i, text):
	linha = 1
	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	token = tabela[len(tabela) - 1][1]
	print(token)

	token, i, linha = program(token,tabela, i, linha, text)	
	token, i, linha = dc_c(token,tabela, i, linha, text)
	token, i, linha = dc_v(token, tabela,i, linha, text)
	print("Token dps da dc_v: " + token)
	token, i, linha = dc_p(token, tabela, i, linha, text)

	if(token == "simb_begin"):

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			token, i, linha = cmd(token, tabela, i, linha, text)
			i = i+1
			print(token)
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]

	# 		if(token == "simb_pv"):
	# 			i = i+1
	# 			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	# 			token = tabela[len(tabela)-1][1]
	# 		else:
	# 			print("Erro sintático na linha "+str(linha)+": ; esperado")

	# if(token == "simb_end"):
	# 	i = i+1
	# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	# 	token = tabela[len(tabela)-1][1]
	# else:
	# 	print("Erro sintático na linha "+str(linha)+": end esperado")

	# if(token == "simb_p"):
	# 	i = i+1
	# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	# 	token = tabela[len(tabela)-1][1]
	# 	print("FIM DO PROGRAMA")
	# else:
	# 	print("Erro sintático na linha "+str(linha)+": . esperado")

	print(token)
	print("FIM DO PROGRAMA")


def program(token, tabela, i, linha, text):
	if (token == "simb_program"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "id"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")
			
		if(token == "simb_pv"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			print("saida do program")
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			print("saida do program")
			return token, i, linha

def dc_c(token, tabela, i, linha, text):
	if(token == "simb_const"):
		i = i + 1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "id"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)

		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")

		if(token == "simb_igual"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": = esperado")
			#TALVEZ PRECISE COLOCAR SIMBOLO ESPECIAL PRA INT E FLOAT

		if(token == "simb_int" or token == "simb_float"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": int ou float esperado")

		if(token == "simb_pv"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")

		if(token == "simb_const"):
			print("recursao dc_c")
			dc_c(token, tabela, i, linha, text)
		else:
			print("saida do dc_c")
			return token, i, linha
	else:
		print("saida do dc_c")
		return token, i, linha

def dc_v(token, tabela, i, linha, text):
	if(token == "simb_var"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")

		while(token == "simb_v"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]

			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
			else:
				print("Erro sintático na linha "+str(linha)+": id esperado")

		if (token == "simb_dp"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": esperado")

		if(token == "simb_tipo"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": integer ou real esperado")

		if(token == "simb_pv"):
			i = i +1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")

		if(token == "simb_var"):
			print("recursao dc_v")
			token, i, linha = dc_v(token,tabela, i, linha, text)
			print("saindo da recursao")
			return token, i, linha
		else:
			print("saida do dc_v")
			return token, i, linha

	else:
		print("saida do dc_v")
		return token, i, linha

def dc_p(token, tabela, i, linha, text):
	if(token == "simb_procedure"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "id_procedure"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")


		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")

		if(token != "id"):
			print("Erro sintático na linha "+str(linha)+": id esperado")

		while(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)

			while(token == "simb_v"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				print(token)

				if(token == "id"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
				else:
					print("Erro sintático na linha "+str(linha)+": id esperado")

		if(token == "simb_dp"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": : esperado")
		
		if(token == "simb_tipo"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": integer ou real esperado")

		if (token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")

		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			#Chama corpo_p
			token, i, linha = corpo_p(token, tabela, i, linha, text)
			print(token)
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha)+": ; esperado")
			return token, i, linha

	else:
		return token, i, linha

def corpo_p(token, tabela, i, linha, text):
	token, i, linha = dc_v(token, tabela, i, linha, text)
	print(token)

	if(token == "simb_begin"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			token, i, linha = cmd(token, tabela, i, linha, text)
			print(token + " Iteracao - cmd")
			#i = i+1
			#tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			#token = tabela[len(tabela)-1][1]
			print(token)

			# if(token == "simb_pv"):
			# 	i = i+1
			# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			# 	token = tabela[len(tabela)-1][1]
			# 	print(token)
			# else:
			# 	print("Erro sintático na linha "+str(linha-1)+": ; esperado")

		# if(token == "simb_end"):
		# 	i = i+1
		# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		# 	token = tabela[len(tabela)-1][1]
		# 	print(token)
		# else:
		# 	print("Erro sintático na linha "+str(linha)+": end esperado")

		# if(token == "simb_pv"):
		# 	i = i+1
		# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		# 	token = tabela[len(tabela)-1][1]
		# 	print(token)
		# 	return token, i, linha
		# else:
		# 	print("Erro sintático na linha "+str(linha)+": . esperado")
		# 	return token, i, linha

		return token, i, linha
	else:
		print("Erro sintático na linha "+str(linha)+": begin esperado")
		return token, i, linha

def cmd(token,tabela,i,linha,text):
	print("entrando na CMD com token"+ token)
	#read(<variaveis>) ou write(<variaveis>)
	if(token == "simb_read" or token == "simb_write"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)

		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")

		# <variaveis> = id <mais_var>
		if(token == "id"):
			## <mais_var>
			while(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				print(token)
				if(token == "simb_v"): #  ","
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
					print(token)
				elif(token == "simb_fpar"): # ")"
					break
				else:
					print("Erro sintático na linha "+str(linha)+": , esperado")
		else:
			print("ERRO: id")

		if(token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")

		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			return token, i, linha

	# while(<condicao>) do <cmd>
	elif(token == "simb_while"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")

		token, i, linha = condicao(token, tabela, i, linha, text)
		print(token)

		if(token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")

		if(token == "simb_do"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": do esperado")
		return cmd(token,tabela,i,linha,text)
	#if <condicao> then <cmd> <pfalsa>	
	elif(token == "simb_if"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		
		# <condicao>
		token, i, linha = condicao(token, tabela, i, linha, text)
		print(token+"BBBB")

		if(token =="simb_then"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token+"CCCCC")
		else:
			print("Erro sintático na linha "+str(linha)+": then esperado")

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
			token,i,linha= cmd(token,tabela,i,linha,text)
			print(token)
			if(token == "simb_else"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				print(token)
			elif(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin"):
				continue
			else:
				return token,i,linha
	# begin <comando> end			
	elif(token == "simb_begin"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token + "AAAAAAAAAAAAAAAAAAAAAAA")
		while(token == "simb_read" or token == "simb_write" or token == "simb_if" or token == "simb_while" or token == "id" or token == "simb_for" or token =="simb_begin"):
			token,i,linha = cmd(token,tabela,i,linha,text)
			print(token+"AAAAAAAAA")

		if(token == "simb_end"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
		else:
			print("Erro sintático na linha "+str(linha)+": end esperado")
		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			return token,i,linha
		elif(token == "simb_p"):
			return token,i,linha
		else:
			print("Erro sintático na linha "+str(linha)+": ; esperado")
			return token,i,linha
	#id := <expresao>
	#id <lista_arg>		
	elif(token == "id"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "simb_atrib"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			token, i, linha = expressao(token,tabela,i,linha, text)
			print(token+"AQUIAQUIAQUI")
			if(token == "simb_pv"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				print(token)

		elif(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			print(token)
			if(token == "id"):
				while(token == "id"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
					print(token)
					if(token == "simb_pv"):
						i = i+1
						tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
						token = tabela[len(tabela)-1][1]
						print(token)
					elif(token == "simb_fpar"):
						break
					else:
						print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			else:
				print("ERRO: id")
				print(token)
			if(token == "simb_fpar"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				print(token)
				return token, i, linha 
		else:
			#print(token+": aqui")
			print("Erro sintático na linha "+str(linha)+": := esperado")
			return token, i, linha
	return token, i, linha

#<condicao>
def condicao(token, tabela, i, linha, text):
	print("condicao")
	#<expressao>
	token,i,linha= expressao(token,tabela,i,linha,text)
	
	# igual
	if(token == "simb_igual"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# dif
	elif(token == "simb_diferente"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# maior igual
	elif(token == "simb_maior_igual"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# menor igual
	elif(token == "simb_menor_igual"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# maior
	elif(token == "simb_maior"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# menor
	elif(token == "simb_menor"):
		print(token)
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
	else:
		print("Erro sintatico: Falta de um simbolo de condicao")
	
	#<expressao>
	token, i, linha = expressao(token,tabela,i,linha,text)
	print("fim condicao:"+token)
	return token,i,linha

#<espressao>
def expressao(token,tabela,i,linha,text):
	print("expressao")
	## TALVEZ N PRECISE DISSO, TEM QUE VERIFICAR SE A FUNÇAO
	## QUE CHAMA a expressao JA LEU O TOKEN
	'''
	i = i+1
	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	token = tabela[len(tabela)-1][1]
	'''
	print(token)

	# <termo> - pode ser simb_soma, simb_sub ou lambda
	token, i, linha = termo(token, tabela, i, linha, text)

	# <outros_termos>
	while(token == "simb_soma" or token == "simb_sub"):
		token,i, linha = termo(token, tabela, i, linha, text)
	print("fim expressao")
	return token, i, linha	

#<termo>
def termo(token, tabela, i, linha, text):

	## <op_un>
	if(token == "simb_soma" or token == "simb_sub"):
		print(token)
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	## <fator> ## VERIFICAR SE ESSA CONDICAO PRECISA SER FEITA OU CHAMA FATOR DIRETO
	if(token == "id" or token == "num_int" or token == "num_float" or token == "simb_apar"):
		print(token)
		token, i, linha = fator(token, tabela, i, linha, text)
	else:## erro do fator
		print("Erro sintático na linha "+str(linha)+": fator esperado")

	## <mais_fatores>
	while(token == "simb_mult" or token == "simb_div"):
		#next token
		token, i, linha = fator(token, tabela, i, linha, text)

	return token, i, linha
	
#<fator>
def fator(token, tabela, i, linha, text):

	#<op_mult>
	if(token == "simb_mult" or token == "simb_div"): # "/" or "*"
		print(token)

		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	
	if(token == "id"): # ID
		print(token)
		
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

		
	elif(token == "num_int" or token == "num_float"): # numero real ou int
		print(token)

		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	#(<expressao>)
	elif(token == "simb_apar"): # '('
		print(token)
		
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		#print("expressao")
		
		token, i, linha = expressao(token, tabela, i, linha, text)
		
		if(token == "simb_fpar"): # ')'
			print(token)
			
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": : ')' esperado")
	else:
		## talvez n precise dessa condicao,
		print("Erro sintático na linha "+str(linha)+": expressao esperado")


	return token, i, linha





######################################## FIM 