#Compilador
#@authors Pedro Natali, Rafael Pinho and Patrick Feitosa

import lexico
import sintatico

arquivo_entrada = "./entrada/in_teste2.txt"
arquivo_saida = "./saida/saida.txt"
arquivo_lexico = "./saida/saida_lexico.txt"

if __name__ == '__main__':
	saida = open(arquivo_saida,'w')
	saida_lexico = open(arquivo_lexico,'w')
	text = lexico.ler_arquivo(arquivo_entrada)
	i = 0

	#Criando a tabela 
	tabela = []


	#Chama o Compilador (Sintático rege as chamadas do Léxico)
	sintatico.analisador_sintatico(tabela, i, text)

	#Imprimindo a tabela
	a = 0
	while(a < len(tabela)):
		saida_lexico.write(tabela[a][0])
		saida_lexico.write(", ")
		saida_lexico.write(tabela[a][1])
		saida_lexico.write("\n")
		if(tabela[a][0] == "erro"):
			saida.write(tabela[a][1]+"\n")
		a = a + 1

	saida.close()
	saida_lexico.close()