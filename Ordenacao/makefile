# Nome do arquivo principal
#file_test = './instancias-numericas/instancias-num/num.1000.1.in'
MAIN = Ordenacao.py
INSTANCE ?= [3,1,2,5,4]
num_instance = 12


# Executar o método principal com o python3, definindo quantas instâncias deseja que sejam comparadas entre o selection_sorte e o insertion_sort, definodo por default como 12(total de instâncias)
run3:
	python3 $(MAIN) $(num_instance)

# Realizar testes do selection_sort utilizando uma instância fornecida via parâmetro, podendo esta ser representada por um array ou pelo path de um arquivo.
selection:
	python3 $(MAIN) selection $(INSTANCE)

# Realizar testes do insertion_sort utilizando uma instância fornecida via parâmetro, podendo esta ser representada por um array ou pelo path de um arquivo.
insertion:
	python3 $(MAIN) insertion "$(INSTANCE)"

