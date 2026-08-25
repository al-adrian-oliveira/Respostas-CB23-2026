# Questão 1
classes base:
- pessoa
- iguaria (comida)
- restaurante

subclasses de pessoa:
- funcionario

subclasse de funcionário:
- chefe de cozinha
- gerente 
- garçom

subclasses de iguaria:
- bolo
- pizza

subclasses de restaurante:
- pizzaria

Todas as subclasses herdam todos os atributo e métodos.

# Questão 2
Como um restaurante tem várias comidas, um objeto da classe restaurante deve ter várias comidas. Pensando de maneira otimizada, o ideal será implementar um dicionário cujas chaves são o nome da comida e os valores são um objeto do tipo iguaria. Nesse caso não há herança.


# Questão 3

- Argumento 1: 
- Argumento 2:
- Argumento 3: Instância da classe funcionário. Visto que o gerente precisa saber qual funcionário deve ser demitido.