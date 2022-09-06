""" 1. Dada as seguintes informações: Pessoa, cpf, nome e idade, crie uma classe onde teremos o retorno do documento, o retorno do nome e 
verificação de tipo de pessoa, onde um método irá receber como parâmetro “F” ou “N” para trazer fumante ou não fumante. Feito isso, 
crie uma instância e retorne esses valores. """

class Person:
      def __init__(self, cpf, name, age):
            self.cpf = cpf
            self.name = name
            self.age = age
            
      def get_name(self):
            return f'Name: {self.name}'
      
      def get_cpf(self):
            return f'CPF: {self.cpf}'
      
      def get_smoker(self, f_or_n):
            if f_or_n == 'f':
                  return f'{self.name} is a smoker'
            elif f_or_n == 'n':
                  return f'{self.name} is not a smoker'
            else:
                  return 'Invalid option'

name = Person(12345678912, 'Mayara Muniz Milanesi', 28).get_name()
cpf = Person(12345678912, 'Mayara Muniz Milanesi', 28).get_cpf()
smoker = Person(12345678912, 'Mayara Muniz Milanesi', 28).get_smoker('m')

print(name)
print(cpf)
print(smoker)
      
