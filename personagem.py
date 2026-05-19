import random
import time  # Importado para criar o efeito de animação

'''Criação da classe logo que será herdada pela classe personagem de naruto'''
class Anime:
    def __init__(self):
        self.__logo= "Naruto Shippuden"
    
    def get_logo(self):
        return self.__logo

'''Criação da classe personagem de naruto'''
class PersonagemNaruto(Anime):
    def __init__(self, nome = " ", qi = 0 , taijutsu = 0, ninjutsu = 0, genjutsu = 0):
        self.__nome = nome
        self.__qi = qi
        self.__taijutsu = taijutsu
        self.__ninjutsu = ninjutsu
        self.__genjutsu = genjutsu
        super().__init__()

    #Getters

    def get_nome(self):
        return self.__nome
    def get_qi(self):
        return self.__qi
    def get_taijutsu(self):
        return self.__taijutsu
    def get_ninjutsu(self):
        return self.__ninjutsu
    def get_genjutsu(self):
        return self.__genjutsu
    
    #Setters

    def set_nome(self, nome):
        self.__nome = nome
    def set_qi(self, qi):
        self.__qi = qi
    def set_taijutsu(self, taijutsu):
        self.__taijutsu = taijutsu
    def set_ninjutsu(self, ninjutsu):
        self.__ninjutsu = ninjutsu
    def set_genjutsu(self, genjutsu):
        self.__genjutsu = genjutsu

    #Exibir cartas
    def exibir(self):
        print(f"== {self.__nome} ==")
        print(f"- QI: {self.__qi} -")
        print(f"- Taijutsu: {self.__taijutsu} -")
        print(f"- Ninjutsu: {self.__ninjutsu} -")
        print(f"- Genjutsu: {self.__genjutsu} -")
        print(f"- Logo: {self.get_logo()} -",)

    #Exibir cartas para o inicio do jogo
    def exibir_carta_jogo(self, dono):
        # Efeito de digitação rápida para os atributos da carta
        linhas = [
            f"== CARTA DO {dono}: {self.__nome} ==",
            f" QI: {self.__qi}",
            f" Taijutsu: {self.__taijutsu}",
            f" Ninjutsu: {self.__ninjutsu}",
            f" Genjutsu: {self.__genjutsu}",
            f"- Logo: {self.get_logo()} -",
            "-" * 30
        ]
        for linha in linhas:
            print(linha)
            time.sleep(0.15)  # Pequena pausa entre cada linha do card
    