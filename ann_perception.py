 # -*- coding: utf-8 -*-
import numpy as np
use_bias = 1

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


class Perceptron:

    def __init__(self, ni, nh, no, epocas):
        """
            Inicializa todas as variaveis
        """
        self.input = ni
        self.hidden = nh
        self.output = no
        self.limiar = 1
        self.epocas = epocas
        
         # Inserindo Dados de entradas
        #self.amostras = np.ones((3,4))
        print("AMOSTRA")
        self.amostras = np.array([[0,0],
                                   [0,1],
                                   [1,0],
                                   [1,1]])
        # Inserindo Bias
        self.amostras = np.insert(self.amostras, 0, 1, axis=1)

        print(self.amostras)
        
        # Inserindo Pesos
        # self.pesos = np.random.randn(self.input, self.hidden )
        print("PESOS")
        self.pesos = np.zeros((3,3)) 
        # Inserindo Bias
        self.pesos = np.insert(self.pesos, 0, 1, axis=1)
        print(self.pesos)
        #np.insert(self.pesos, 0, 1, axis=0)
        
        
    def forward_propagate(self):
        """
            Inicializa a propagacao
        """
        for self.epocas in range(0, self.epocas):
            self.set_input(self.amostras)
            # self.set_hidden(self.amostras)


            
    def set_input(self, amostras):
            print("SOMA DE CADA")
            somaSinapse0 = np.dot(amostras, self.pesos)
            print(somaSinapse0)
            print("ATIVACAO")
            camadaOculta = sigmoid(somaSinapse0)
            print(camadaOculta)


    def backpropagation(self):
        pass
        

def demo():
    # the AND function
    ann = Perceptron(2, 3, 1, 1)
    ann.forward_propagate()
    # ann.update_error_output(targets[i])
    # ann.backpropagation(targets[i])
    # ann.update_weights()

    

if __name__ == '__main__':
    demo()

    """
        tipos de ativacao
        Fazer a camada intermediária
        Fazer o Backpropagation
        atualizar o peso
        atualizar o bias
        Erro
        erro para duas saidas
        treinamento
        momento
    """
    
    
            
