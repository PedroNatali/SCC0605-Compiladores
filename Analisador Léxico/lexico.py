#Analisador Léxico
#@authors Pedro Natali, Rafael Pinho and Patrick Feitosa

#adicionado simb_to, erro de funcao escrita errada, adicionado procedure, adicionado constante, concertado simbolo maior
#testes 1* 2 4 5 6 tao ok

#Tabela de simbolos especiais
tab_especiais = [["program","simb_program"], ["begin","simb_begin"], ["end", "simb_end"], ["const","simb_const"], ["var","simb_var"],
	["integer", "simb_tipo"], ["real", "simb_tipo"],["int","simb_int"],["float","simb_float"],["procedure", "simb_procedure"], ["while", "simb_while"], ["for", "simb_for"], ["to", "simb_to"], ["do", "simb_do"], ["read", "simb_read"],
	["write", "simb_write"], ["if", "simb_if"], ["else", "simb_else"], ["then", "simb_then"], ["ident", "simb_ident"]]


#retorna o arquivo texto como uma string
def ler_arquivo(arquivo):           
	arq = open(arquivo,'r')
	text = arq.read()
	arq.close()
	return text

def ler_arquivo2(arquivo):
	arq = open(arquivo,'r')
	text = arq.readlines()
	arq.close()
	return text


#Automato de ID
def automato_id(text,indice,linha,tabela,verify):
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
					string = "Erro lexico na linha "+ str(linha) +": caractere " + text[indice] + " invalido em id"
					cadeia_falsa = ["erro", string]
					tabela.append(cadeia_falsa)
					verify = False
					return indice, tabela,verify

				elif ord(text[indice]) >= 63 and ord(text[indice]) <= 64:
					cadeia_id = [cadeia, "id"]
					tabela.append(cadeia_id)
					string = "Erro lexico na linha "+ str(linha) +": caractere " + text[indice] + " invalido em id"
					cadeia_falsa = ["erro", string]
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
						cadeia_id = ["erro","Erro lexico na linha "+ str(linha) +": função inexistente"]
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
						cadeia_id = [cadeia, "id"]
						tabela.append(cadeia_id)
						verify = False
						return indice-1, tabela,verify
		else:
			return indice, tabela, verify
	else:
		return indice, tabela, verify


#automato que delimita comentarios
def automato_comentario(text,indice,linha,tabela,verify):
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
							tabela.append(["erro","Erro lexico na linha "+ str(linha) +": comentario de varias linhas"])
							verify = False
							return indice+1, tabela, verify
					cadeia_id = ["erro", "Erro lexico na linha "+ str(linha) +": comentario nao finalizado"]
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
def automato_numero(text,indice,linha,tabela,verify):
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
							cadeia_id = ["erro","Erro lexico na linha "+ str(linha) +": numero invalido"]
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
						string = "Erro lexico na linha "+ str(linha) +": caractere " + text[indice+1] + " invalido em id"
						cadeia_falsa = [erro, string]
						tabela.append(cadeia_falsa)
						verify = False
						return indice,tabela,verify
					elif (ponto == 0):
						cadeia_id = [cadeia, "num_int"]
						tabela.append(cadeia_id)
						verify = False
						return indice-1,tabela,verify
					else:
						cadeia_id = [cadeia, "num_float"]
						tabela.append(cadeia_id)
						verify = False
						return indice-1,tabela,verify
		else:
			return indice,tabela,verify
	else:
		return indice, tabela, verify


#autoamto que determina os comparativos do codigo
def automato_comparativos(text, indice,linha,tabela,verify):
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


def automato_simbolos(text,indice,linha,tabela,verify):
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

def automato_operandos(text,indice,linha,tabela,verify):
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
'''
def nextToken(tabela,i,text):
		verify = True
		tamanho = len(tabela)

		if(i == len(text)):
			return tabela, i

		if(text[i] == "\n" or text[i] == "\t" or text[i] == " "):
			i = i + 1
			if(i == len(text)):
				return tabela, i

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

				cadeia_id = [text[f], "Erro lexico na linha "+ str(linha) +": caractere invalido"]
				tabela.append(cadeia_id)

		i = f
		return tabela,i
'''
def nextToken(tabela,i,linha,text):
		aux = True
		while(aux):
			verify = True
			tamanho = len(tabela)
			if(i == len(text)):
				return tabela, i

			if(text[i] == "\n" or text[i] == "\t" or text[i] == " "):
				if(text[i] == "\n"):
					linha = linha+1
				i = i + 1
				if(i == len(text)):
					return tabela, i

			a,tabela,verify = automato_comentario(text,i,linha,tabela,verify)
			b,tabela,verify = automato_id(text,a,linha,tabela,verify)
			c,tabela,verify = automato_numero(text,b,linha,tabela,verify)
			d,tabela,verify = automato_comparativos(text,c,linha,tabela,verify)
			e,tabela,verify = automato_simbolos(text,d,linha,tabela,verify)
			f,tabela,verify = automato_operandos(text,e,linha,tabela,verify)

			if(tamanho == len(tabela)):
				if(text[f] != "\n" and text[f] != "\t" and text[f] != " "):
					string = "Erro lexico na linha "+ str(linha) +": caractere" + text[i] + "invalido"
					cadeia_falsa = ["erro", string]

					cadeia_id = ["erro", "Erro lexico na linha "+str(linha)+": caractere invalido"]
					tabela.append(cadeia_id)
			i = f
			if(tabela[len(tabela)-1][0] != "erro"):
				aux = False
			else:
				i=i+1
		return tabela,i,linha
