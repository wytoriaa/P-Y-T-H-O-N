# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:
    #no init foi criado os tributos da bola
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    #no metodo trocaCor, eu passei pelo parametro a cor que foi chamada no init
    #no metodo mostraCor, eu retornei o self que é assegura as informações da bola
    #e retornei o self cor
    #ou seja, o trocaCor e o mostraCor estão unidos pelo return que exibe o self.cor

    def trocaCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        return self.cor

#aqui, declarei bola como o 'item' que vai receber as informações da classe
#chamando o bola.trocaCor, poderei mudar a cor e chamada no print atras do mostraCor

bola = Bola('rosa', 5, 'plastico')
print(bola.mostraCor())
bola.trocaCor('vermelho')
print(bola.mostraCor())
