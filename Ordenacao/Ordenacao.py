import os
from io import open
import timeit
import sys

folder = './instancias-numericas/instancias-num'

def load_file_instances(folder):
    list_name_file = os.listdir(folder)
    list_path_file = []
    for name_file in list_name_file:
        list_path_file.append(folder+"/"+name_file)
    return list_path_file

def selection_sort(array, show_result=False):
    size = len(array)
    if size <= 1:
        return array
    for i in range(size):
        lowest  = i
        for j in range(i+1,size):
            if(array[lowest] > array[j]):
                lowest = j
        if i != lowest:
            aux = array[i]
            array[i]=array[lowest]
            array[lowest] = aux
    if show_result:
        print(array)
    return array

def insertion_sort(array, show_result=False):
    for i in range(1, len(array)):
        aux = array[i]
        j = i
        while((j > 0) and (aux < array[j-1])):
            array[j] = array[j-1]
            j=j-1
        array[j] = aux
    if show_result:
        print(array)
    return array

def main(num_instance):
    print(f" Instancia          selection_sort      insertion_sort" )
    files = load_file_instances(folder)
    for file in files[0:int(num_instance)]:
        file_array = []
        with open(file, "r", encoding="utf-8") as arquivo:
            content = arquivo.read()
            file_array = [int(x) for x in content.split()]
            
        time_selection = timeit.timeit(stmt="selection_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        time_insertion = timeit.timeit(stmt="insertion_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        
        print(f" {file.split('/')[-1]}      {time_selection:.4f}s             {time_insertion:.4f}s")

if(len(sys.argv)>2): 
    method = sys.argv[1]
    array_test = sys.argv[2]
    if method == "selection" or method == "insertion":
        if(not(sys.argv[2][-2]).isnumeric()):
            file = array_test
            print(file)
            with open(file, "r", encoding="utf-8") as arquivo:
                content = arquivo.read()
                array_test = [int(x) for x in content.split()]
        if(method == "selection"):
            time_ = timeit.timeit(stmt="selection_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
        else:
            time_ = timeit.timeit(stmt="selection_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
        print(f"\n{method} : {time_:.4f}s ") 

elif __name__ == "__main__":
    main(sys.argv[1])
