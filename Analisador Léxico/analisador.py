#Analisador Léxico
#@authors Pedro Natali, Rafael Pinho and Patrick Feitosa

#Tabela de simbolos especiais
tab_especiais = [["program","simb_program"], ["begin","simb_begin"], ["end", "simb_end"], ["var","simb_var"],
	["integer", "simb_tipo"], ["real", "simb_tipo"], ["while", "simb_while"], ["for", "simb_for"], ["do", "simb_do"], ["read", "simb_read"],
	["write", "simb_write"], ["if", "simb_if"], ["else", "simb_else"], ["then", "simb_then"], ["ident", "simb_ident"]]



#retorna o arquivo texto como uma string
def ler_arquivo(arquivo):           
	arq = open(arquivo,'r')
	text = arq.read()
	arq.close()
	return text


#Automato de ID
def automato_id(text,indice,saida,tabela):
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
			else:
				#se ja existir, so eh necessario citar novamente
				if(busca_tabela(cadeia, tabela)):
					i = acha_indice(cadeia,tabela)
					tabela.append(tabela[i])
					return indice, tabela
				#senao acrescenta na tabela
				elif(busca_tabela(cadeia,tab_especiais)):
					#acha o indice e adiciona ele
					i = acha_indice(cadeia,tab_especiais)
					tabela.append(tab_especiais[i])
					return indice,tabela

				else:
					cadeia_id = [cadeia, "id"]
					tabela.append(cadeia_id)
					return indice, tabela
	else:
		return indice, tabela


#automato que delimita comentarios
def automato_comentario(text,indice,saida,tabela):
	if text[indice] == '{':
		indice = indice+1
		cadeia = '{'
		for indice in range(indice,len(text)):
			if text[indice] == '}':
				cadeia_id = [cadeia , "comentario"]
				tabela.append(cadeia_id)
				return indice, tabela
			else:
				cadeia = cadeia + text[indice]
	else:
		return indice, tabela

#automato que delimita os numeros presentes no codigo em P
def automato_numero(text,indice,saida,tabela):
	ponto = 0
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
			#se tem ponto eh float, senao int
			else:
				if (ponto == 0):
					cadeia_id = [cadeia, "num_int"]
					tabela.append(cadeia_id)
					return indice, tabela
				else:
					cadeia_id = [cadeia, "num_float"]
					tabela.append(cadeia_id)
					return indice, tabela
	else:
		return indice,tabela


#autoamto que determina os comparativos do codigo
def automato_comparativos(text, indice, tabela):
	if(text[indice] == '='):
		tabela.append(['=',"simb_igual"])
		return indice,tabela
	elif(text[indice] == '>'):
		if(text[indice+1] == '='):
			indice = indice+1
			tabela.append([">=","simb_maior_igual"])
			return indice, tabela
		else:
			tabela.append(['>',"simb_maior"])
	elif(text[indice] == '<'):
		if(text[indice+1] == '='):
			indice = indice+1
			tabela.append(["<=","simb_menor_igual"])
			return indice,tabela
		elif(text[indice+1] == '>'):
			indice = indice+1
			tabela.append(["<>","simb_diferente"])
			return indice,tabela
		else:
			tabela.append(['<',"simb_menor"])
			return indice,tabela
	else:
		return indice,tabela


def automato_simbolos(text,indice,tabela):
	if(text[indice] == ':'):
		if(text[indice+1] == '='):
			indice = indice+1
			tabela.append([':=',"simb_atrib"])
			return indice,tabela
		else:
			tabela.append([':',"simb_dp"])
			return indice,tabela
	elif(text[indice] == ';'):
		tabela.append([';',"simb_pv"])
		return indice,tabela
	elif(text[indice] == '('):
		tabela.append(['(',"simb_apar"])
		return indice,tabela
	elif(text[indice] == ')'):
		tabela.append([')',"simb_fpar"])
		return indice,tabela
	else:
		return indice,tabela

def automato_operandos(text,indice,tabela):
	if(text[indice] == '+'):
		tabela.append(['+',"simb_soma"])
		return indice,tabela
	elif(text[indice] == '-'):
		tabela.append(['-',"simb_sub"])
		return indice,tabela
	elif(text[indice] == '*'):
		tabela.append(['*',"simb_mult"])
		return indice,tabela
	elif(text[indice] == '/'):
		tabela.append(['/',"simb_div"])
		return indice,tabela
	else:
		return indice,tabela




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
	

def main(arquivo_entrada, arquivo_saida):

	saida = open(arquivo_saida,'w')
	text = ler_arquivo(arquivo_entrada)
	i = 0

	#Criando a tabela 
	tabela = []
	
	#Enquanto nao terminar o texto, utilize os automatos
	while(i < len(text)):
		i,tabela = automato_comentario(text,i,saida,tabela)
		i,tabela = automato_id(text,i,saida,tabela)
		i,tabela = automato_numero(text,i,saida,tabela)
		i,tabela = automato_comparativos(text,i,tabela)
		i,tabela = automato_simbolos(text,i,tabela)
		i,tabela = automato_operandos(text,i,tabela)
		i = i+1

	#Imprimindo a tabela
	a = 0
	while(a < len(tabela)):
		saida.write(tabela[a][0])
		saida.write(", ")
		saida.write(tabela[a][1])
		saida.write("\n")
		a = a + 1

	saida.close()