#!/usr/bin/python

class Sort:
    # Constructor
    # def __init__(self):    

    def bubble(self):
        '''
        Método de la burbuja

        se puede implementar directamente con el siguiente método:

        arr.sort() # Ordena de menor a mayor
        arr.sort(reverse = True) # Ordena de mayor a menor
        arr.sort(key = str.lower) # Ordena alfabeticamente
        arr.sorted(arr_b) # Ordena en una copia (arr_b)
        '''

        n = len(arr)

        for i in range(n):
            for j in range(n - i - 1):
                if arr[j][1] > arr[j + 1][1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr
