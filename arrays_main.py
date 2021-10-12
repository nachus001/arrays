



# cuantos subarrays se pueden sacar de un array
def get_max_sub(arr):
    n = len(arr)
    return (n * (n + 1)) // 2

# cuantos items impares hay en el array
def get_odd_items_qty(arr):
    odd = 0
    for i in arr:
        if i % 2 != 0:
            odd += 1

    return odd

# cuantos items pares hay en elarray
def get_even_items_qty(arr):
    even = 0
    for i in arr:
        if i % 2 == 0:
            even += 1

    return even




# funcion para determinar la cantidad de sub-arrays que contienen una cantidad impar de numeros impares
def solve_odd_odd(arr):
    # if the len of the array is 0 return 0
    if len(arr) == 0:
        #        print("Len was 0")
        return 0
    # now we know that tha max possible subarrays contained in an array of N size
    # is N(N+1)/2 arrays
    odd = 0  # our momentary odd counter
    total_odd_sa = 0  # outr total odd counter
    #    print(arr)
    #    start = 0
    #    print (len(arr))
    #    for i in arr:
    #        print (is_odd(i))
    for i in range (0, len(arr)): # We have to scan 'i' blocks
        for n in range (0, i+ 1):  # Every block will have 'n' subarrays in the current block
            for r in range(n, len(
                    arr) - i + n):  # every subarray will be scanned starting in n position and ending in len(arr)-i+n
                if arr[r] % 2 != 0:  # is_odd(arr[r]) == True:
                    odd += 1  # if the current item is odd, then we add to the momentary odd counter
            if odd % 2 != 0:  # is_odd(odd) == True: # if the amount of odd numbers in this subarray is odd then we add to out total
                total_odd_sa += 1
            odd = 0  # we reset the subarray odd counter
    #    print (total_odd_sa)
    return total_odd_sa

# funcion para determinar cuantos subarrays con cantidad par de numeros impares
def solve_even_odd(arr):
    # if the len of the array is 0 return 0
    if len(arr) == 0:
        #        print("Len was 0")
        return 0
    # now we know that tha max possible subarrays contained in an array of N size
    # is N(N+1)/2 arrays
    odd = 0  # our momentary odd counter
    total_even_sa = 0  # outr total odd counter
    #    print(arr)
    #    start = 0
    #    print (len(arr))
    #    for i in arr:
    #        print (is_odd(i))
    for i in range(0, len(arr)):  # We have to scan 'i' blocks
        for n in range(0, i + 1):  # Every block will have 'n' subarrays in the current block
            for r in range(n, len(arr) - i + n):  # every subarray will be scanned starting in n position and ending in len(arr)-i+n
                if arr[r] % 2 != 0:  # is_odd(arr[r]) == True:
                    odd += 1  # if the current item is odd, then we add to the momentary odd counter
            if odd % 2 == 0 and odd != 0:  # if the amount of odd numbers in this subarray is even and it's count is NOT zero, then we add to our total
                total_even_sa += 1
            odd = 0  # we reset the subarray odd counter
    #    print (total_odd_sa)
    return total_even_sa


array_1 = [1, 2, 2, 1, 2, 1 , 2,1]


print("el array ", array_1, " contiene ", len(array_1), " elementos, y contiene ", get_max_sub(array_1),  " subarrays")
print("La cantidad de subarrays conteniendo una cantidad impar de numeros impares es", solve_odd_odd(array_1))

#for i in range (0, 256):
#    print(list(bin(i))[2:])

#for i in range (0, 7):
#    lst = [int(x) for x in list('{:03b}'.format(i))]
#    print("La lista", lst, "tiene un tamaño", "par" if len(lst) % 2 == 0 else "impar", "de", len(lst), "elementos, con", get_max_sub(lst), "posibles subarrays, de los cuales", solve_odd_odd(lst), "contienen una cantidad impar de elementos impares,", solve_even_odd(lst), "contienen una cantidad par de elementos impares" )

print("-----ARRAY-----------TAMAÑO-----SUBARRAYS------SA cant IMPAR DE IMPARES ---- SA cant PAR DE IMPARES--------     ")

for i in range (0, 8):
    lst = [int(x) for x in list('{:03b}'.format(i))]
    print(lst, "           ",len(lst), "           ",get_max_sub(lst), "                   ",solve_odd_odd(lst), "                      ",solve_even_odd(lst)  )

