import lexico
import sintatico


arquivo_entrada = "programa.txt"
arquivo_saida = "saida.txt"


if __name__ == '__main__':
	saida = open(arquivo_saida,'w')
	text = lexico.ler_arquivo(arquivo_entrada)
	i = 0

	#Criando a tabela 
	tabela = []
	#Enquanto nao terminar o texto, utilize os automatos
	while(i < len(text)):
		tabela,i = lexico.nextToken(tabela,i,text)
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