import unittest


def palindrome(cadena):

    inicio = 0
    fin = len (cadena) - 1
    while cadena [inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


def palindromeRecusivo(cadena):
    inicio=0
    fin=-1
    if inicio >= fin:
        return True 
    if cadena [inicio] == cadena[fin]:
        return palindromeRecusivo [cadena,inicio+1,fin-1]
    else :
        return False
