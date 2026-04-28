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

def merge_sort(array, show_result=False):
    if len(array) > 1:
        middle =  len(array) // 2
        array_left= array[:middle]
        array_right = array[middle:]
        
        merge_sort(array_left)
        merge_sort(array_right)
        
        i=0
        j=0
        k=0
        
        while i < len(array_left) and j < len(array_right):
            if array_left[i] < array_right[j]:
                array[k] = array_left[i]
                i += 1
            else: 
                array[k] = array_right[j]
                j += 1
            k += 1
            
        while i < len(array_left):
            array[k] = array_left[i]
            i += 1
            k += 1
        
        while j < len(array_right):
            array[k] = array_right[j]
            j += 1 
            k += 1
    if show_result:
        print(array)
    return array

def partition(array, start, end):
    pivo = array[end - 1]
    for i in range(start, end):
        if array[i] <= pivo:
            array[i], array[start] = array[start], array[i]
            start +=1
    return start - 1

def quick_sort(array, start=0, end=None, show_result=False):
    end = end if end is not None else len(array)
    if start < end:
        partition_ = partition(array, start, end)
        quick_sort(array, start, partition_)
        quick_sort(array, partition_+1, end)
    if show_result:
        print(array)
    return array

def main(num_instance):
    print(f" Instancia          selection_sort      insertion_sort      merge_sort      quick_sort" )
    files = load_file_instances(folder)
    for file in files[0:int(num_instance)]:
        file_array = []
        with open(file, "r", encoding="utf-8") as arquivo:
            content = arquivo.read()
            file_array = [int(x) for x in content.split()]
            
        time_selection = timeit.timeit(stmt="selection_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        time_insertion = timeit.timeit(stmt="insertion_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        time_merge = timeit.timeit(stmt="merge_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        time_quick = timeit.timeit(stmt="quick_sort(lista.copy())", globals=globals(), number=1, setup=f"lista = {file_array}")
        
        print(f" {file.split('/')[-1]}      {time_selection:.4f}s             {time_insertion:.4f}s             {time_merge:.4f}s           {time_quick:.4f}s")

if(len(sys.argv)>2): 
    method = sys.argv[1]
    array_test = sys.argv[2]
    if method == "selection" or method == "insertion" or method == "merge" or method == "quick":
        if(not(sys.argv[2][-2]).isnumeric()):
            file = array_test
            print(file)
            with open(file, "r", encoding="utf-8") as arquivo:
                content = arquivo.read()
                array_test = [int(x) for x in content.split()]
        if(method == "selection"):
            time_ = timeit.timeit(stmt="selection_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
        elif(method == "insertion"):
            time_ = timeit.timeit(stmt="selection_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
        elif(method == "merge"):
            time_ = timeit.timeit(stmt="merge_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
        elif(method == "quick"):
            time_ = timeit.timeit(stmt="quick_sort(lista.copy(), True)", globals=globals(), number=1, setup=f"lista = {array_test}")
            
        print(f"\n{method} : {time_:.4f}s ") 

elif __name__ == "__main__":
    main(sys.argv[1])

