#Analisador Sintático
#@authors Pedro Natali, Rafael Pinho and Patrick Feitosa 

import lexico


#program := simb_program id; <dc> begin <cmd> end.
def analisador_sintatico(tabela, i, text):
	linha = 1
	#Encontra o primeiro token
	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	token = tabela[len(tabela) - 1][1]
	

	#Analisa se é o program
	if (token == "simb_program"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		if(token == "id"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			
		if(token == "simb_pv"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
	

	#Passa para o dc_c
	token, i, linha = dc_c(token,tabela, i, linha, text)
	#Passa para o dc_v
	token, i, linha = dc_v(token, tabela,i, linha, text)
	#Passa para o dc_p
	token, i, linha = dc_p(token, tabela, i, linha, text)

	#Se o token apos a declaracao for simb_begin
	if(token == "simb_begin"):
		#Rode o CMD enquanto precisar
		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin" or token =="id_procedure" or token == "simb_for"):
			token, i, linha = cmd(token, tabela, i, linha, text)
			i = i+1
			
			if(token == "simb_p"):
				break
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
	else:
		print("Erro sintático na linha "+str(linha)+": begin esperadooioioioioioi")
		string = "Erro sintático na linha "+str(linha)+": begin esperado"
		tabela.append(["erro", string])
		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
			token = tabela[len(tabela)-1][1]

	print()
	print("Os erros foram printados corretamente no arquivo saida.txt")

#declaracao de constante := simb_const id = simb_tipo;
def dc_c(token, tabela, i, linha, text):
	if(token == "simb_const"):
		i = i + 1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		

		if(token == "id"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			

		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_igual"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": = esperado")
			string = "Erro sintático na linha "+str(linha)+": = esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			#TALVEZ PRECISE COLOCAR SIMBOLO ESPECIAL PRA INT E FLOAT

		if(token == "simb_int" or token == "simb_float"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": int ou float esperado")
			string = "Erro sintático na linha "+str(linha)+": int ou float esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_pv"):
			i = i + 1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_const"):
			dc_c(token, tabela, i, linha, text)
		else:
			return token, i, linha
	else:
		return token, i, linha

#declaracao de variavel := var x(,y) : integer|float;
def dc_v(token, tabela, i, linha, text):
	if(token == "simb_var"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		

		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

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
				string = "Erro sintático na linha "+str(linha)+": id esperado"
				tabela.append(["erro", string])
				if(token == "id"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
					token = tabela[len(tabela)-1][1]

		if (token == "simb_dp"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": : esperado")
			string = "Erro sintático na linha "+str(linha)+": : esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_tipo"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": integer ou real esperado")
			string = "Erro sintático na linha "+str(linha)+": integer ou real esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_pv"):
			i = i +1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_var"):
			token, i, linha = dc_v(token,tabela, i, linha, text)
			return token, i, linha
		else:
			return token, i, linha

	else:
		print("saida do dc_v")
		return token, i, linha

#declaracao de procedure: simb_procedure id_procedure ( id(,id) : simb_tipo ); <corpo_p>
def dc_p(token, tabela, i, linha, text):
	if(token == "simb_procedure"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		

		if(token == "id_procedure"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": id esperado")
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]


		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")
			string = "Erro sintático na linha "+str(linha)+": ( esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token != "id"):
			print("Erro sintático na linha "+str(linha)+": id esperado")
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		while(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			

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
					string = "Erro sintático na linha "+str(linha)+": id esperado"
					tabela.append(["erro", string])
					if(token == "id"):
						i = i+1
						tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
						token = tabela[len(tabela)-1][1]

		if(token == "simb_dp"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": : esperado")
			string = "Erro sintático na linha "+str(linha)+": : esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		
		if(token == "simb_tipo"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": integer ou real esperado")
			string = "Erro sintático na linha "+str(linha)+": integer ou real esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if (token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")
			string = "Erro sintático na linha "+str(linha)+": ) esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			#Chama corpo_p
			token, i, linha = corpo_p(token, tabela, i, linha, text)
			
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token, i, linha

	else:
		return token, i, linha


#Corpo_p :=  <cmd> {se o primeiro simbolo for begin}
def corpo_p(token, tabela, i, linha, text):
	token, i, linha = dc_v(token, tabela, i, linha, text)
	

	if(token == "simb_begin"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin" or token == "simb_for"):
			token, i, linha = cmd(token, tabela, i, linha, text)
			#i = i+1
			#tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			#token = tabela[len(tabela)-1][1]
			

			# if(token == "simb_pv"):
			# 	i = i+1
			# 	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			# 	token = tabela[len(tabela)-1][1]
			# 	
			# else:
			# 	print("Erro sintático na linha "+str(linha-1)+": ; esperado")

		if(token == "simb_end"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": end esperado")
			string = "Erro sintático na linha "+str(linha)+": end esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token, i, linha
		return token, i, linha
	else:
		print("Erro sintático na linha "+str(linha)+": begin esperado")
		string = "Erro sintático na linha "+str(linha)+": begin esperado"
		tabela.append(["erro", string])
		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
			token = tabela[len(tabela)-1][1]
		return token, i, linha

def cmd(token,tabela,i,linha,text):
	#read(<variaveis>) ou write(<variaveis>)
	if(token == "simb_read" or token == "simb_write"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		

		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")
			string = "Erro sintático na linha "+str(linha)+": ( esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		# <variaveis> = id <mais_var>
		if(token == "id"):
			## <mais_var>
			while(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				
				if(token == "simb_v"): #  ","
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
					
				elif(token == "simb_fpar"): # ")"
					break
				else:
					print("Erro sintático na linha "+str(linha)+": , esperado")
					string = "Erro sintático na linha "+str(linha)+": , esperado"
					tabela.append(["erro", string])
					if(token == "id"):
						i = i+1
						tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
						token = tabela[len(tabela)-1][1]
		else:
			string = "Erro sintático na linha "+str(linha)+": id esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")
			string = "Erro sintático na linha "+str(linha)+": ) esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token, i, linha

	# while(<condicao>) do <cmd>
	elif(token == "simb_while"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ( esperado")
			string = "Erro sintático na linha "+str(linha)+": ( esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		token, i, linha = condicao(token, tabela, i, linha, text)
		

		if(token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")
			string = "Erro sintático na linha "+str(linha)+": ) esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		if(token == "simb_do"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": do esperado")
			string = "Erro sintático na linha "+str(linha)+": do esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		return cmd(token,tabela,i,linha,text)
	#if <condicao> then <cmd> <pfalsa>	
	elif(token == "simb_if"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		
		# <condicao>
		token, i, linha = condicao(token, tabela, i, linha, text)

		if(token =="simb_then"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": then esperado")
			string = "Erro sintático na linha "+str(linha)+": then esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin" or token == "simb_for"):
			token,i,linha= cmd(token,tabela,i,linha,text)
			
			if(token == "simb_else"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				
			elif(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == "simb_begin" or token == "simb_for"):
				continue
			else:
				return token,i,linha
	# begin <comando> end			
	elif(token == "simb_begin"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		while(token == "simb_read" or token == "simb_write" or token == "simb_if" or token == "simb_while" or token == "id" or token == "simb_for" or token =="simb_begin" or token =="id_procedure" or token == "simb_for"):
			token,i,linha = cmd(token,tabela,i,linha,text)

		if(token == "simb_end"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": end esperado")
			string = "Erro sintático na linha "+str(linha)+": end esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			return token,i,linha
		elif(token == "simb_p"):
			return token,i,linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token,i,linha
	#id := <expresao>
	#id <lista_arg>		
	elif(token == "id"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		if(token == "simb_atrib"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			token, i, linha = expressao(token,tabela,i,linha, text)
			if(token == "simb_pv"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				
				return token,i,linha
			else:
				return token,i,linha
		elif(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
			if(token == "id"):
				while(token == "id"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
					
					if(token == "simb_pv"):
						i = i+1
						tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
						token = tabela[len(tabela)-1][1]
						
					elif(token == "simb_fpar"):
						break
					else:
						print("Erro sintático na linha "+str(linha-1)+": ; esperado")
						string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
						tabela.append(["erro", string])
						if(token == "id"):
							i = i+1
							tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
							token = tabela[len(tabela)-1][1]
			else:
				string = "Erro sintático na linha "+str(linha)+": id esperado"
				tabela.append(["erro", string])
				if(token == "id"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
					token = tabela[len(tabela)-1][1]
				
			if(token == "simb_fpar"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				
				return token, i, linha 
		else:
			#print(token+": aqui")
			print("Erro sintático na linha "+str(linha)+": := esperado")
			string = "Erro sintático na linha "+str(linha)+": := esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token, i, linha
	elif(token == "id_procedure"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		if(token == "simb_apar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha-1)+": ( esperado")
			string = "Erro sintático na linha "+str(linha)+": ( esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		if(token == "id"):
			while(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
				token = tabela[len(tabela)-1][1]
				
				if(token == "simb_pv"):
					i = i+1
					tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
					token = tabela[len(tabela)-1][1]
					
				elif(token == "simb_fpar"):
					continue
				else:
					print("Erro sintático na linha "+str(linha-1)+": , esperado")
					string = "Erro sintático na linha "+str(linha)+": , esperado"
					tabela.append(["erro", string])
					if(token == "id"):
						i = i+1
						tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
						token = tabela[len(tabela)-1][1]
		if(token == "simb_fpar"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			
		else:
			print("Erro sintático na linha "+str(linha)+": ) esperado")
			string = "Erro sintático na linha "+str(linha)+": ) esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
		if(token == "simb_pv"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
			return token, i, linha
		else:
			print("Erro sintático na linha "+str(linha-1)+": ; esperado")
			string = "Erro sintático na linha "+str(linha-1)+": ; esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
			return token, i, linha
	elif(token == "simb_for"):
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		
		token, i, linha = cmd(token,tabela,i,linha,text)
		
		if(token == "simb_to"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": to esperado")
			string = "Erro sintático na linha "+str(linha)+": to esperado"
			tabela.append(["erro", string])
		if(token == "id" or token == "num_int" or token == "num_float"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": id ou tipo esperado")
			string = "Erro sintático na linha "+str(linha)+": valor invalido em for"
			tabela.append(["erro", string])
		if(token == "simb_do"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": do esperado")
			string = "Erro sintático na linha "+str(linha)+": do esperado"
			tabela.append(["erro", string])
		return cmd(token,tabela,i,linha,text)
	return token, i, linha

#<condicao>
def condicao(token, tabela, i, linha, text):
	#<expressao>
	token,i,linha= expressao(token,tabela,i,linha,text)
	
	# igual
	if(token == "simb_igual"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# dif
	elif(token == "simb_diferente"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# maior igual
	elif(token == "simb_maior_igual"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# menor igual
	elif(token == "simb_menor_igual"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# maior
	elif(token == "simb_maior"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	# menor
	elif(token == "simb_menor"):
		
		# next_token	
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
	else:
		print("Erro sintatico: Falta de um simbolo de condicao")
		string = "Erro sintático na linha "+str(linha)+": Falta de um simbolo de condição"
		tabela.append(["erro", string])
		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
			token = tabela[len(tabela)-1][1]
	
	#<expressao>
	token, i, linha = expressao(token,tabela,i,linha,text)
	return token,i,linha

#<espressao>
def expressao(token,tabela,i,linha,text):
	## TALVEZ N PRECISE DISSO, TEM QUE VERIFICAR SE A FUNÇAO
	## QUE CHAMA a expressao JA LEU O TOKEN
	'''
	i = i+1
	tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
	token = tabela[len(tabela)-1][1]
	'''
	

	# <termo> - pode ser simb_soma, simb_sub ou lambda
	token, i, linha = termo(token, tabela, i, linha, text)

	# <outros_termos>
	while(token == "simb_soma" or token == "simb_sub"):
		token,i, linha = termo(token, tabela, i, linha, text)
	return token, i, linha	

#<termo>
def termo(token, tabela, i, linha, text):

	## <op_un>
	if(token == "simb_soma" or token == "simb_sub"):
		
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	## <fator> ## VERIFICAR SE ESSA CONDICAO PRECISA SER FEITA OU CHAMA FATOR DIRETO
	if(token == "id" or token == "num_int" or token == "num_float" or token == "simb_apar"):
		
		token, i, linha = fator(token, tabela, i, linha, text)
	else:## erro do fator
		print("Erro sintático na linha "+str(linha)+": fator esperado")
		string = "Erro sintático na linha "+str(linha)+": fator esperado"
		tabela.append(["erro", string])
		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
			token = tabela[len(tabela)-1][1]

	## <mais_fatores>
	while(token == "simb_mult" or token == "simb_div"):
		#next token
		token, i, linha = fator(token, tabela, i, linha, text)

	return token, i, linha
	
#<fator>
def fator(token, tabela, i, linha, text):

	#<op_mult>
	if(token == "simb_mult" or token == "simb_div"): # "/" or "*"
		

		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	
	if(token == "id"): # ID
		
		
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

		
	elif(token == "num_int" or token == "num_float"): # numero real ou int
		

		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]

	#(<expressao>)
	elif(token == "simb_apar"): # '('
		
		
		i = i+1
		tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
		token = tabela[len(tabela)-1][1]
		#print("expressao")
		
		token, i, linha = expressao(token, tabela, i, linha, text)
		
		if(token == "simb_fpar"): # ')'
			
			
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela, i, linha, text)
			token = tabela[len(tabela)-1][1]
		else:
			print("Erro sintático na linha "+str(linha)+": : ')' esperado")
			string = "Erro sintático na linha "+str(linha)+": ) esperado"
			tabela.append(["erro", string])
			if(token == "id"):
				i = i+1
				tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
				token = tabela[len(tabela)-1][1]
	else:
		## talvez n precise dessa condicao,
		print("Erro sintático na linha "+str(linha)+": expressao esperado")
		string = "Erro sintático na linha "+str(linha)+": expressao esperado"
		tabela.append(["erro", string])
		if(token == "id"):
			i = i+1
			tabela, i, linha = lexico.nextToken(tabela,i,linha,text)
			token = tabela[len(tabela)-1][1]


	return token, i, linha





######################################## FIM 