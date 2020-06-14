#Analisador Léxico
#@authors Pedro Natali, Rafael Pinho and Patrick Feitosa

#adicionado simb_to, erro de funcao escrita errada, adicionado procedure, adicionado constante, concertado simbolo maior
#testes 1* 2 4 5 6 tao ok

#Tabela de simbolos especiais
tab_especiais = [["program","simb_program"], ["begin","simb_begin"], ["end", "simb_end"], ["const","simb_const"], ["var","simb_var"],
	["integer", "simb_tipo"], ["real", "simb_tipo"],["procedure", "simb_procedure"], ["while", "simb_while"], ["for", "simb_for"], ["to", "simb_to"], ["do", "simb_do"], ["read", "simb_read"],
	["write", "simb_write"], ["if", "simb_if"], ["else", "simb_else"], ["then", "simb_then"], ["ident", "simb_ident"]]


#retorna o arquivo texto como uma string
def ler_arquivo(arquivo):           
	arq = open(arquivo,'r')
	text = arq.read()
	arq.close()
	return text


#Automato de ID
def automato_id(text,indice,tabela,verify):
	if(verify):
		#Verifica se o texto do indice atual eh letra
		if ( ord(text[indice]) >= 97 and ord(text[indice]) <= 122 ):
			cadeia = text[indice]
			indice = indice+1
			#Verifica se eh texto ou numero
			for indice in range(indice,len(text)):
				if ord(text[indice]) >= 97 and ord(text[indice]) <= 122:
					cadeia = cadeia+text[indice]
					
				elif ord(text[indice]) >= 48 and ord(text[indice]) <= 57:
					cadeia = cadeia + text[indice]

				elif ord(text[indice]) >= 33 and ord(text[indice]) <= 38:
					cadeia_id = [cadeia, "id"]
					tabela.append(cadeia_id)
					string = "Erro lexico: caractere " + text[indice] + " invalido em id"
					cadeia_falsa = [text[indice], string]
					tabela.append(cadeia_falsa)
					verify = False
					return indice, tabela,verify

				elif ord(text[indice]) >= 63 and ord(text[indice]) <= 64:
					cadeia_id = [cadeia, "id"]
					tabela.append(cadeia_id)
					string = "Erro lexico: caractere " + text[indice] + " invalido em id"
					cadeia_falsa = [text[indice], string]
					tabela.append(cadeia_falsa)
					verify = False
					return indice, tabela,verify

				else:
					#se ja existir, so eh necessario citar novamente
					if(busca_tabela(cadeia, tabela)):
						i = acha_indice(cadeia,tabela)
						tabela.append(tabela[i])
						verify = False
						return indice-1, tabela,verify
					#senao acrescenta na tabela
					elif(busca_tabela(cadeia,tab_especiais)):
						#acha o indice e adiciona ele
						i = acha_indice(cadeia,tab_especiais)
						tabela.append(tab_especiais[i])
						verify = False
						return indice-1,tabela,verify
					elif text[indice] == '(' and tabela[len(tabela)-1] != ["procedure", "simb_procedure"]:
						cadeia_id = [cadeia,"Erro lexico: função inexistente"]
						tabela.append(cadeia_id)
						verify = False
						return indice-1, tabela,verify

					elif tabela[len(tabela)-1] == ["procedure", "simb_procedure"]: 
						cadeia_id = [cadeia,"id_procedure"]
						tabela.append(cadeia_id)
						tab_especiais.append(cadeia_id)
						verify = False
						return indice-1, tabela,verify
					else:
						'''if tabela[len(tabela)-1] == ["var","simb_var"]:
							cadeia_id = [cadeia,"id"]
							tabela.append(cadeia_id)
							tab_especiais.append(cadeia_id)
							return indice, tabela
						else:
							fake_indice = indice-1
							while tabela[fake_indice][1] == "id" or tabela[fake_indice] ==[',', "simb_v"]:
								if tabela[fake_indice] == ["var","simb_var"]:
									cadeia_id = [cadeia,"id"]
									tabela.append(cadeia_id)
									tab_especiais.append(cadeia_id)
									return indice, tabela
								fake_indice = fake_indice - 1
						'''
						cadeia_id = [cadeia, "id"]
						tabela.append(cadeia_id)
						verify = False
						return indice-1, tabela,verify
		else:
			return indice, tabela, verify
	else:
		return indice, tabela, verify


#automato que delimita comentarios
def automato_comentario(text,indice,tabela,verify):
	if(verify):
		if text[indice] == '{':
			indice = indice+1
			cadeia = '{'
			for indice in range(indice,len(text)):
				if text[indice] == '}':
					cadeia = cadeia + '}'
					cadeia_id = [cadeia , "comentario"]
					tabela.append(cadeia_id)
					indice = indice+1
					verify = False
					return indice, tabela,verify
				elif(ord(text[indice]) == 10 or ord(text[indice]) == 12):
					new_indice = indice
					for new_indice in range(new_indice,len(text)):
						if(text[new_indice] == '}'):
							indice = new_indice
							tabela.append([cadeia,"Erro lexico: comentario de varias linhas"])
							verify = False
							return indice+1, tabela, verify
					cadeia_id = [cadeia, "Erro lexico: comentario nao finalizado"]
					tabela.append(cadeia_id)
					#indice = indice+1
					verify = False
					return indice, tabela, verify
				else:
					cadeia = cadeia + text[indice]
		else:
			return indice, tabela, verify
	else:
		return indice, tabela, verify

#automato que delimita os numeros presentes no codigo em P
def automato_numero(text,indice,tabela,verify):
	ponto = 0
	if(verify):
		#verifica se o texto do indice atual eh numero
		if(ord(text[indice]) >= 48 and ord(text[indice]) <= 57):
			cadeia = text[indice]
			indice = indice +1
			#verifica char a char da string analisando se há numeros nessa sequência 
			for indice in range(indice, len(text)):
				if(ord(text[indice]) >= 48 and ord(text[indice]) <= 57):
					cadeia = cadeia + text[indice]
				#Veriica se há ponto (falta colocar erros)	
				elif(ord(text[indice]) == 46):
					cadeia = cadeia + text[indice]
					ponto = 1
				#Erro numero invalido
				elif((ord(text[indice+1]) >= 48 and ord(text[indice+1]) <= 57) or ord(text[indice+1]) == 46):

					cadeia = cadeia + text[indice]
					f = indice+1
					for f in range(f,len(text)):
						if(ord(text[f]) >= 48 and ord(text[f]) <= 57):
							cadeia = cadeia + text[f]	
						elif(ord(text[f]) == 46):
							cadeia = cadeia + text[f]
						else:
							cadeia_id = [cadeia,"Erro lexico: numero invalido"]
							tabela.append(cadeia_id)
							verify = False
							return f, tabela,verify


				#se tem ponto eh float, senao int
				else:
					if(ord(text[indice]) >= 33 and ord(text[indice]) <= 38):
						if (ponto == 0):
							cadeia_id = [cadeia, "num_int"]
							tabela.append(cadeia_id)
						else:
							cadeia_id = [cadeia, "num_float"]
							tabela.append(cadeia_id)
						string = "Erro lexico: caractere " + text[indice+1] + " invalido em id"
						cadeia_falsa = [text[indice+1], string]
						tabela.append(cadeia_falsa)
						verify = False
						return indice,tabela,verify
					elif (ponto == 0):
						cadeia_id = [cadeia, "num_int"]
						tabela.append(cadeia_id)
						verify = False
						return indice,tabela,verify
					else:
						cadeia_id = [cadeia, "num_float"]
						tabela.append(cadeia_id)
						verify = False
						return indice,tabela,verify
		else:
			return indice,tabela,verify
	else:
		return indice, tabela, verify


#autoamto que determina os comparativos do codigo
def automato_comparativos(text, indice, tabela,verify):
	if(verify):
		if(text[indice] == '='):
			tabela.append(['=',"simb_igual"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '>'):
			if(text[indice+1] == '='):
				indice = indice+1
				tabela.append([">=","simb_maior_igual"])
				verify = False
				return indice, tabela,verify
			else:
				tabela.append(['>',"simb_maior"])
				verify = False
				return indice, tabela,verify
		elif(text[indice] == '<'):
			if(text[indice+1] == '='):
				indice = indice+1
				tabela.append(["<=","simb_menor_igual"])
				verify = False
				return indice,tabela,verify
			elif(text[indice+1] == '>'):
				indice = indice+1
				tabela.append(["<>","simb_diferente"])
				verify = False
				return indice,tabela,verify
			else:
				tabela.append(['<',"simb_menor"])
				verify = False
				return indice,tabela,verify
		else:
			return indice,tabela,verify
	else:
		return indice, tabela, verify


def automato_simbolos(text,indice,tabela,verify):
	if(verify):
		if(text[indice] == ':'):
			if(text[indice+1] == '='):
				indice = indice+1
				tabela.append([':=',"simb_atrib"])
				verify = False
				return indice,tabela,verify
			else:
				tabela.append([':',"simb_dp"])
				verify = False
				return indice,tabela,verify
		elif(text[indice] == ';'):
			tabela.append([';',"simb_pv"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '('):
			tabela.append(['(',"simb_apar"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == ')'):
			tabela.append([')',"simb_fpar"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '.'):
			tabela.append(['.',"simb_p"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == ','):
			tabela.append([',',"simb_v"])
			verify = False
			return indice,tabela,verify
		else:
			return indice,tabela,verify
	else:
		return indice, tabela, verify

def automato_operandos(text,indice,tabela,verify):
	if(verify):
		if(text[indice] == '+'):
			tabela.append(['+',"simb_soma"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '-'):
			tabela.append(['-',"simb_sub"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '*'):
			tabela.append(['*',"simb_mult"])
			verify = False
			return indice,tabela,verify
		elif(text[indice] == '/'):
			tabela.append(['/',"simb_div"])
			verify = False
			return indice,tabela,verify
		else:
			return indice,tabela,verify
	else:
		return indice, tabela, verify




#Busca para analisar se ja esta na tabela
def busca_tabela(cadeia, tabela):
	i = 0
	#Busca na tabela
	while (i < len(tabela)):
		#se achou entao retorna true
		if(cadeia == tabela[i][0]):
			return 1
		i = i + 1
	return 0

#usado para encontrar o indice 
def acha_indice(cadeia,tabela):
	i = 0
	#Busca na tabela
	while(i < len(tabela)):
		#se achou, coloca ele na tabela do analisador
		if(cadeia == tabela[i][0]):
			return i
		i = i +1
	



######################################## ANALISADOR SINTÀTICO

##### MELHOR MUDAR AS E CHAMAR A FUNCAO DO JEITO 
###### token, i = program(token, i, text)
	###### Pq dai eu n preciso chamar as funcoes uma dentro da outra necessariamente 

def analisador_sintatico(tabela, i, text):
	tabela, i = nextToken(tabela, i, text)
	token = tabela[len(tabela) - 1][1]

	token, i = program(token,tabela, i, text)	

	token, i = dc_c(token,tabela, i, text)
	token, i = dc_v(token, tabela,i, text)
	token, i = dc_p(token, tabela, i, text)

	if(token == "simb_begin"):
		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == simb_begin):
			#token, i = cmd(token, i, text)
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
			if(token == "simb_p"):
				i = i+1
				tabela, i = nextToken(tabela, i, text)
				token = tabela[len(tabela)-1][1]
				print("Sucess")


	print("Sucess")


def program(token, tabela, i, text):
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
				return token, i

def dc_c(token, tabela, i, text):
	print(token)
	if(token == "simb_const"):
		i = i + 1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]
		print(token)
		if(token == "id"):
			i = i + 1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)

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
							dc_c(token, i, text)
						else:
							print("SAI DO DC_C")
							return token, i
	else:
		print("SAI DO DC_C")
		return token, i

def dc_v(token, tabela, i, text):
	print(token)
	if(token == "simb_var"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]

		print(token)
		if(token == "id"):
			i = i+1
			tabela, i = nextToken(tabela, i, text)
			token = tabela[len(tabela)-1][1]
			print(token)

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
				print(token)

				if(token == "simb_tipo"):
					i = i+1
					tabela, i = nextToken(tabela, i, text)
					token = tabela[len(tabela)-1][1]
					print(token)

					if(token == "simb_pv"):
						i = i +1
						tabela, i = nextToken(tabela, i, text)
						token = tabela[len(tabela)-1][1]
						print(token)

						if(token == "simb_var"):
							print("Mais um Dc_V")
							dc_v(token,tabela, i, text)
						else:
							print("Iria para o dc_p")
							return token, i
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
		return token, i

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

			token, i = corpo_p(token, i, text)
			return token, i



		else:
			pass
	
	else:
		return token, i


def corpo_p(token, tabela, i, text):
	dc_v(token, i, text)
	i = i+1
	tabela, i = nextToken(tabela, i, text)
	token = tabela[len(tabela)-1][1]

	if(token == "simb_begin"):
		i = i+1
		tabela, i = nextToken(tabela, i, text)
		token = tabela[len(tabela)-1][1]

		while(token == "simb_read" or token =="simb_write" or token == "simb_while" or token == "simb_if" or token == "id" or token == simb_begin):
			#token, i = cmd(token, i, text)
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
				return token, i


######################################## FIM 	

def main(arquivo_entrada, arquivo_saida):

	saida = open(arquivo_saida,'w')
	text = ler_arquivo(arquivo_entrada)
	i = 0

	#Criando a tabela 
	tabela = []
	#Enquanto nao terminar o texto, utilize os automatos
	#while(i < len(text)):
	#	tabela,i = nextToken(tabela,i,text)
	#	i = i+1
	#	print(tabela)
	#	print()

	analisador_sintatico(tabela, i, text)

	#Imprimindo a tabela
	a = 0
	while(a < len(tabela)):
		saida.write(tabela[a][0])
		saida.write(", ")
		saida.write(tabela[a][1])
		saida.write("\n")
		a = a + 1

	saida.close()

def nextToken(tabela,i,text):
		verify = True
		tamanho = len(tabela)

		if(i == len(text)):
				return tabela,i

		if(text[i] == "\n" or text[i] == "\t" or text[i] == " "):
			i = i + 1
			if(i == len(text)):
				return tabela,

		a,tabela,verify = automato_comentario(text,i,tabela,verify)
		b,tabela,verify = automato_id(text,a,tabela,verify)
		c,tabela,verify = automato_numero(text,b,tabela,verify)
		d,tabela,verify = automato_comparativos(text,c,tabela,verify)
		e,tabela,verify = automato_simbolos(text,d,tabela,verify)
		f,tabela,verify = automato_operandos(text,e,tabela,verify)

		if(tamanho == len(tabela)):
			if(text[f] != "\n" and text[f] != "\t" and text[f] != " "):
				string = "Erro lexico: caractere" + text[i] + "invalido"
				cadeia_falsa = [text[i], string]

				cadeia_id = [text[f], "Erro lexico: caractere invalido"]
				tabela.append(cadeia_id)

		i = f
		return tabela,i
