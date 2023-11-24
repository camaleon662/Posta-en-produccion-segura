#Importamos librerias
import fibo
import unittest

#Definimos la clase para el test
class Test():
    listaFibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1.597, 2.584, 4.181, 6.765, 10.946, 17.711, 28.657, 46.368]
    #Creamos la funcion
    def testUnitarioFibo(numero):
        #Asignamos
        testFibo = unittest.TestCase()
        testFibo.assertEqual(
            Test.listaFibo[numero], 
            fibo.fibonacci(numero))

Test.testUnitarioFibo(4)