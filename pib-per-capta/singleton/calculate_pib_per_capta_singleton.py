import pandas as pd
from abc import ABC, abstractclassmethod

#Implementar a abstração completa CalculatePibPerCapta
#Diagrama UML CalculatePibPerCapta

class Config:
    _base_file = "data/base.xlsx"
    _region    = "UF_Regiao"

#Uma classe abstrata representa um contrato com regras, com regras, assinaturas e tipo de retorno
#No exemplo abaixo AbstractCalculaPib
#Quantos contratos temos: 1
#Quantas regras temos: 4
#Quantas assinaturas: 4
#Como podemos violar o contrato de AbstractCalculaPib: Não implementando todos os metodos da classe
#Obriga a utilizar o metodo no código
class AbstractCalculaPib(ABC):
    @abstractclassmethod
    def get_instance():
        raise RuntimeError('Metodo ainda não implementado')

    @abstractclassmethod
    def load_file(self):
        #Caso não seja implementado abaixo
        raise RuntimeError('Metodo ainda não implementado')

    @abstractclassmethod
    def load_uf_by_region(self):
        #Caso não seja implementado abaixo
        raise RuntimeError('Metodo ainda não implementado')

    @abstractclassmethod
    def print_all_content(self):
        #Caso não seja implementado abaixo
        raise RuntimeError('Metodo ainda não implementado')

    
    @abstractclassmethod
    def get_state_by_region(self, state):
        #Caso não seja implementado abaixo
        raise RuntimeError('Metodo ainda não implementado')
    
class CalculatePibPerCaptaSingleton(AbstractCalculaPib):
    # atributos da classe 
    _instance = None
    raw_data  = None
    current_content = None


    # Métodos

    # Construtor da classe
    def __init__(self):
        # Estamos lançando uma exception em 
        # tempo de execução
        raise RuntimeError('Singleton!!')

    @classmethod
    def get_instance(cls):
        # 1 - Criar um Singleton para o projeto pib-per-capta
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            return cls._instance
        else:
            return cls._instance

    @classmethod
    def load_file(self):
        print("Inicio do script de PIB x Percapta")
        self.raw_data = pd.ExcelFile(Config._base_file)
        return self.raw_data

    @classmethod
    def load_uf_by_region(self):
        self.current_content = pd.read_excel(self.raw_data, Config._region )
        return self.current_content

    @classmethod
    def print_all_content(self):
        print(self.current_content)

    
    def get_state_by_region(self, state):
        satates = self.current_content[self.current_content['Regiao'] == state]
        print(satates)

    def get_region_by_state(self, state):
        region = self.current_content[self.current_content['Estado'] == state]
        print(region)

    def state_for(self, state):
        lista = []
        for index, row in self.current_content.iterrows():
            if (row['Regiao'] == state):
                lista.append(row['Estado'])
        print(lista)

    def region_for(self, state):
        lista2 = []
        for index, row in self.current_content.iterrows():
            if (row['Estado'] == state):
                lista2.append(row['Regiao'])
        print(lista2)

    def data_frame_for_state(self, state):
        for c, row in self.current_content.iterrows():
            if (row['Regiao'] == state):
                print(self.current_content.loc[c:c])

    def data_frame_for_region(self, state):
        for c, row in self.current_content.iterrows():
            if (row['Estado'] == state):
                print(self.current_content.loc[c:c])

    def tot_state(self):
        for c, row in self.current_content.iterrows():
            tot = c + 1
        print('Total de Estados:',tot)

    def tot_region(self):
        tot = self.current_content['Regiao'].value_counts()
        print('Total de regiões e estados por regiões\n',tot)

    def first_region(self):
        first = self.current_content[['Regiao', 'Estado']].loc[0:0]
        print(first)

    def last_region(self):
        last = self.current_content[['Regiao', 'Estado']].loc[26:26]
        print(last)
