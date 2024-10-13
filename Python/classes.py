class Pessoa:
    nome: str
    _idade: int
    __cidade: str
    # não definindo o tipo, ele implementa any

    def __init__(self, nome: str, idade: int, cidade: str):
        """Construtor da classe"""
        self.nome = nome
        self._idade = idade # protected
        self.__cidade = cidade # private

    def __str__(self):
        """Método especial para conversão para string"""
        return f'{self.nome}, {self._idade} anos, mora em {self.__cidade}.'
    
    def get_cidade(self):
        return self.__cidade
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

# Exemplo de uso
p1 = Pessoa("Ana", 30, "São Paulo")
p2 = Pessoa("Carlos", 25, "Rio de Janeiro")

# Exibindo os objetos
# print(p1)  # Saída: Ana, 30 anos, mora em São Paulo.
# print(p2)  # Saída: Carlos, 25 anos, mora em Rio de Janeiro.


# Herança

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cidade, salario):
        super().__init__(nome, idade, cidade)
        self.salario = salario

    def __str__(self):
        return f'{self.nome} ganha {self.salario}'

vendedor = Funcionario("pedro", 29, "SP", 500)
# print(vendedor)

# Módulos e lib para tipagem e simplificação

from dataclasses import dataclass

@dataclass # implementa um __init__ e um __str__
class Pessoa:
    nome: str
    idade: int
    cidade: str

p = Pessoa("Carlos", 25, "Rio de Janeiro")
# print(p)  # Saída: Pessoa(nome='Carlos', idade=25, cidade='Rio de Janeiro')

# from pydantic import BaseModel # lib para validação automatica

# class Pessoa(BaseModel):
#     nome: str
#     idade: int
#     cidade: str


# Interface e método abstrato
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def som(self):
        """Esse método deve ser implementado pelas subclasses"""
        pass

    @abstractmethod
    def movimento(self):
        """Esse método deve ser implementado pelas subclasses"""
        pass

# Implementação da interface na classe concreta
class Cachorro(Animal):
    def som(self):
        return "Latido"

    def movimento(self):
        return "Corre"

class Gato(Animal):
    def som(self):
        return "Miau"

    def movimento(self):
        return "Salta"

c = Cachorro()
g = Gato()

print(c.som())  # Saída: Latido
print(g.movimento())  # Saída: Salta


# Outros
# Args opcionais
class Calculadora:
    def soma(self, a, b=0, c=0):
        return a + b + c

calc = Calculadora()
print(calc.soma(5))         # Saída: 5
print(calc.soma(5, 10))      # Saída: 15
print(calc.soma(5, 10, 15))  # Saída: 30

# Quantidade variável
class Calculadora:
    def soma(self, *args):
        return sum(args)

calc = Calculadora()
print(calc.soma(5))          # Saída: 5
print(calc.soma(5, 10))       # Saída: 15
print(calc.soma(5, 10, 15))   # Saída: 30
