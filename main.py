from Plantas.sem_flor import Briofita,Pteridofitas
from Plantas.tem_flor import Gimnospermas , Angiospermas , Dicotiledoneas, Monocotiledôneas

class PlantaExotica:
    def __init__(self,nome,especie):
        self.nome = nome
        self.especie = especie
        self.frutas = ""
        self.frutos = ""
        self.sementes = ""
        self.caracteristicas = ""

def s_n(mensagem):
    while True:
        resposta = input(mensagem).lower()
        if resposta in ['s', 'n']:
            return resposta
        print(" Resposta inválida, Digite s ou n.")

Armario_plantas = []

exemplo1 = Gimnospermas("Cica", "Gimnospermas")
exemplo2 = Angiospermas("Mandacaru", "Angiospermas")
exemplo21 = Dicotiledoneas("Cica", "Angiospermas")
exemplo22 = Monocotiledôneas("cu", "Angiospermas")
exemplo3 = Briofita("Musgo de Parede ou pedra", "Briófitas")
exemplo4 = Pteridofitas("Samambaia", "Pteridofitas")

Armario_plantas.append(exemplo1)
Armario_plantas.append(exemplo2)
Armario_plantas.append(exemplo21)
Armario_plantas.append(exemplo22)
Armario_plantas.append(exemplo3)
Armario_plantas.append(exemplo4)

while True:

    print("""
    * MENU PLANTAS & PLANTAS *
    
    1 - descubra o tipo de planta que está observando.
    2 - Ver os tipos de plantas cadastrados e seus exemplos.
    3 - adicione uma especie de planta personalizada.
    0 - sair do programa.
    
    """)

    escolha = input("Digite o numero para selecionar uma opção: ")

    if escolha == "0":
        print("Encerrando o programa...")
        break
    if escolha == "1":
        print("")
        print("* Vamos Descobrir... * ")
        print("")

        apelido = input("Diga um nome qualquer para a planta que esta vendo: \n")

        p1 = s_n("- a planta possuem flores ? digite s/n:\n").lower()
        if p1 == "s":

            p2 = s_n("- a planta possui algum fruto ? digite s/n:\n").lower()
            if p2 == "s":
                print("")
                print(" == Sua Planta é uma Angiosperma  == ")
                print("")

                p3 = s_n("- Gostaria de descobrir se ela é Monocotileodoneas ou Dicotiledoneas ? digite s/n:\n").lower()
                if p3 == "s":

                    print("pegue uma folha da planta a sua frente e rasgue de uma ponta a outra")
                    p4 = s_n("-Ao rasga-la a folha seguiu um corte reto ? tipo uma fita ? digite s/n:\n").lower()
                    if p4 == "s":
                        print(f" == a planta que você chamou de {apelido} é uma Angiosperma do grupo das Monocotileodoneas == ")
                        planta_descoberta = Monocotiledôneas(f"{apelido}" , "Angiospermas")
                    else:
                        print(f" == a planta que você chamou de {apelido} é uma Angiosperma do grupo das Dicotiledoneas == ")
                        planta_descoberta = Dicotiledoneas(f"{apelido}","Angiospermas")

                else:
                    print(f" == a planta que você chamou de {apelido} é uma Angiosperma == ")
                    planta_descoberta = Angiospermas(f"{apelido}","Angiospermas")

            else:
                print(f" == a planta que você chamou de {apelido} é uma Gimnosperma == ")
                planta_descoberta = Gimnospermas(f"{apelido}", "Gimnosperma")

        else:
            p6 = s_n("A Planta é mais alta que sua canela ? digite s/n:\n")
            if p6 == "s":
                print(f"== a planta que você chamou de {apelido} é uma Pteridofita == ")
                planta_descoberta = Pteridofitas(f"{apelido}", "Pteridofita")
            else:
                print("")
                print(f"Muito Provável que {apelido} seja uma Briófita mas...")
                print(f"{apelido} pode ser uma Pteridofita que não cresceu ainda")
                print("")
                print("vamos para ultima pergunta decisória")
                print("")
                p5 = s_n("- A planta forma um tapete baixo, parecendo um veludo ou um lodo verde ? digite (s/n):\n").lower()
                if p5 == "s":
                    planta_descoberta = Briofita(f"{apelido}", "Briofita")
                    print(f" == a planta que você chamou de {apelido} é uma Briofita == ")

                else:
                    planta_descoberta = Pteridofitas(f"{apelido}","Pteridofitas")
                    print(f" == a planta que você chamou de {apelido} é uma Pteridófita  == ")

        Armario_plantas.append(planta_descoberta)

    if escolha == "2":
        print("")
        print("*** VAMOS VER OS TIPOS DE PLANTAS ***")

        print("")

        for p in Armario_plantas:
            if isinstance(p,Gimnospermas):
                print(f"## GIMNOSPERMAS ##")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")

            elif isinstance(p,Dicotiledoneas):
                print(f"## DICOTILEDONEAS ##")
                print(f"- Espécie: {p.especie}")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")

            elif isinstance(p,Monocotiledôneas):
                print(f"## MONOCOTILEDÕNIAS ##")
                print(f"- Espécie: {p.especie}")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")


            elif isinstance(p,Angiospermas):
                print(f"## ANGIOSPERMAS ##")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")

            elif isinstance(p,Briofita):
                print(f"## BRIOFITAS ##")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")

            elif isinstance(p,Pteridofitas):
                print(f"## PTERIDOFITAS ##")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p._caracteristicas}")

                print("")

            elif isinstance(p,PlantaExotica):
                print(f"## {p.especie.upper()} ##")
                print(f" nome da planta: {p.nome}")
                print(f"- Possuem Frutos: {p.frutos}")
                print(f"- Possuem Flores: {p.flores}  ")
                print(f"- Possuem Sementes: {p.sementes} ")
                print(f"- Características: {p.caracteristicas}")



                print("")



        print("""
        - ESCOLHA UMA ESPECIE PARA VER OS EXEMPLOS DA NOSSA CAATINGA-
        
        1 - Giminospermas
        2 - Angiospermas
        3 - Briofita
        4 - Pteridofitas
        5 - Não olhar exemplos
                            
        """)
        ver_plantas = int(input("Gostaria de ver exemplos de Qual espécie presente na nossa Caatinga ?\n"))

        if ver_plantas == 1:
            print("---Exemplos de Gimnospermas---")
            print("")
            g = Gimnospermas("x", "Gimnospermas")
            print(g.exemplos[0]["nome"], ",", g.exemplos[0]["caracteristicas"])
            print(g.exemplos[1]["nome"], ",", g.exemplos[1]["caracteristicas"])
            print(g.exemplos[2])

        if ver_plantas == 2:
            print("")
            print("---Exemplos de Angiospermas---")
            print("")
            a = Angiospermas("nada", "Angiospermas")
            print(a.exemplos[0]["nome"], ",", a.exemplos[0]["caracteristicas"])
            print(a.exemplos[1]["nome"], ",", a.exemplos[1]["caracteristicas"])
            print(a.exemplos[2]["nome"], ",", a.exemplos[2]["caracteristicas"])
            print(a.exemplos[3]["nome"], ",", a.exemplos[3]["caracteristicas"])
            print(a.exemplos[4]["nome"], ",", a.exemplos[4]["caracteristicas"])
            print(a.exemplos[5]["nome"], ",", a.exemplos[5]["caracteristicas"])
            print(a.exemplos[6]["nome"], ",", a.exemplos[6]["caracteristicas"])
            print(a.exemplos[7]["nome"], ",", a.exemplos[7]["caracteristicas"])
            print(a.exemplos[8]["nome"], ",", a.exemplos[8]["caracteristicas"])
            print(a.exemplos[9]["nome"], ",", a.exemplos[9]["caracteristicas"])

            print("")

            print("---Exemplos de Monocotileodoneas---")
            print("")
            m = Monocotiledôneas("nada", "Monocotileodoneas")
            print(m.exemplos[0]["nome"], ",", m.exemplos[0]["caracteristicas"])
            print(m.exemplos[1]["nome"], ",", m.exemplos[1]["caracteristicas"])
            print(m.exemplos[2]["nome"], ",", m.exemplos[2]["caracteristicas"])
            print(m.exemplos[3]["nome"], ",", m.exemplos[3]["caracteristicas"])
            print(m.exemplos[4]["nome"], ",", m.exemplos[4]["caracteristicas"])
            print(m.exemplos[5]["nome"], ",", m.exemplos[5]["caracteristicas"])
            print(m.exemplos[6]["nome"], ",", m.exemplos[6]["caracteristicas"])
            print(m.exemplos[7]["nome"], ",", m.exemplos[7]["caracteristicas"])
            print(m.exemplos[8]["nome"], ",", m.exemplos[8]["caracteristicas"])
            print(m.exemplos[9]["nome"], ",", m.exemplos[9]["caracteristicas"])

            print("")

            print("---Exemplos de Dicotiledoneas---")
            print("")
            d = Dicotiledoneas("nada", "Dicotiledoneas")
            print(d.exemplos[0]["nome"], ",", d.exemplos[0]["caracteristicas"])
            print(d.exemplos[1]["nome"], ",", d.exemplos[1]["caracteristicas"])
            print(d.exemplos[2]["nome"], ",", d.exemplos[2]["caracteristicas"])
            print(d.exemplos[3]["nome"], ",", d.exemplos[3]["caracteristicas"])
            print(d.exemplos[4]["nome"], ",", d.exemplos[4]["caracteristicas"])
            print(d.exemplos[5]["nome"], ",", d.exemplos[5]["caracteristicas"])
            print(d.exemplos[6]["nome"], ",", d.exemplos[6]["caracteristicas"])
            print(d.exemplos[7]["nome"], ",", d.exemplos[7]["caracteristicas"])
            print(d.exemplos[8]["nome"], ",", d.exemplos[8]["caracteristicas"])
            print(d.exemplos[9]["nome"], ",", d.exemplos[9]["caracteristicas"])

        if ver_plantas == 3:
            print("---Exemplos de Briofitas---")
            print("")
            b = Briofita("nada", "Briofitas")
            print(b.exemplos[0]["nome"], ",", b.exemplos[0]["caracteristicas"])
            print(b.exemplos[1]["nome"], ",", b.exemplos[1]["caracteristicas"])
            print(b.exemplos[2]["nome"], ",", b.exemplos[2]["caracteristicas"])
            print(b.exemplos[3]["nome"], ",", b.exemplos[3]["caracteristicas"])
            print(b.exemplos[4]["nome"], ",", b.exemplos[4]["caracteristicas"])
            print(b.exemplos[5]["nome"], ",", b.exemplos[5]["caracteristicas"])

        if ver_plantas == 4:
            print("---Exemplos de Pteridofitas---")
            print("")
            p = Pteridofitas("nada","Pteridofitas")
            print(p.exemplos[0]["nome"], ",", p.exemplos[0]["caracteristicas"])
            print(p.exemplos[1]["nome"], ",", p.exemplos[1]["caracteristicas"])
            print(p.exemplos[2]["nome"], ",", p.exemplos[2]["caracteristicas"])
            print(p.exemplos[3]["nome"], ",", p.exemplos[3]["caracteristicas"])
            print(p.exemplos[4]["nome"], ",", p.exemplos[4]["caracteristicas"])
            print(p.exemplos[5]["nome"], ",", p.exemplos[5]["caracteristicas"])

    if escolha == "3":
        print("")
        print(" VAMOS ADICIONAR UMA ESPECIE PERSONALIZADA E CRIADA POR VOCÊ ")
        print("")
        especie = input("- digite um nome para sua Especie:")
        print("")
        nome = input("- agora escolha um nome para sua Planta:")

        c3 = s_n("- Ela vai possuir frutos ? digite s/n:")
        c4 = s_n("- Ela vai possuir flores ? digite s/n:")
        c5 = s_n("- Ela vai possuir sementes ? digite s/n:")

        if c3 == "s":
         frutos = "sim"
        else:
         frutos = "não"

        if c4 == "s":
         flores = "sim"
        else:
         flores = "não"

        if c5 == "s":
         sementes = "sim"
        else:
         sementes = "não"
        print("")
        caracteristicas = input("Digite as Caracteristicas da sua Planta:")

        planta_personalizada = PlantaExotica(nome , especie)

        planta_personalizada.frutos = frutos
        planta_personalizada.flores = flores
        planta_personalizada.sementes = sementes
        planta_personalizada.caracteristicas = caracteristicas

        Armario_plantas.append(planta_personalizada)

        print("")
        print("Sua planta foi registrada com sucesso")

