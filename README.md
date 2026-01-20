#Explicação

Este projeto final é um sistema em Python que classifica plantas de acordo com suas características,
como presença de flores, frutos e sementes.


#Estrutura

Sua estrutura foi feita através de pacotes para melhor organização e para atender aos requisitos do professor.

O projeto roda no main.py e lá é feita a chamada das classes que estão nos outros pacotes, 
como por exemplo os pacotes "tem_flor" e "Sem_flor", que são "filhas" da superclasse que está presente no Planta.py.


# como funciona o código e suas funcionalidades

Basicamente o usuário vai responder perguntas e o sistema identifica qual é o tipo da planta, que pode ser:
-Briófita
-Pteridófita
-Gimnosperma
-Angiosperma
-Monocotiledôneas
-Dicotiledôneas

Que vai ser identificada conforme as respostas do usuário.

Foi implementada também uma funcionalidade para você ver os tipos de plantas, suas características e exemplos,
onde o usuário consegue ver detalhes de cada espécie e exemplos que são próprios da nossa Caatinga.

E além disso foi implementada uma função de você criar sua própria espécie, com o nome que você quiser,
com características de seu interesse e com detalhes escolhidos. Ao final da criação você pode consultar novamente
os tipos de espécies existentes e ele vai estar lá presente com os tipos de plantas conhecidos,
que são as Angios, Gimnos, Pteri e etc.


#Implementação dos conceitos de POO

Com isso todo código foi feito usando os conceitos de POO, por exemplo:

-Abstração: está presente na classe Planta que representa o conceito geral de plantas  
-Herança: nas classes de espécie, tipo Briofitas e Pteridófitas que são "filhas" da superclasse "Planta"  
-Encapsulamento: pode ser visto em atributos que estão protegidos, como por exemplo "_caracteristicas"  
-Polimorfismo: diferentes tipos de plantas são tratadas dentro da mesma lista, ou seja os objetos de classes 
diferentes respondendo ao mesmo metodo

