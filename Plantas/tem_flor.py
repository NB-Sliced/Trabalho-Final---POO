from Plantas.planta import Planta


class ComFlores(Planta):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self.flores = "sim"
        self.sementes = "sim"



class Gimnospermas(ComFlores):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self.frutos = "não"
        self._caracteristicas = "Vasculares, possuem raízes, caule, folhas e sementes. Sementes são nuas (não há fruto). Não possuem flores verdadeiras. Independem da água para fecundação (surgimento do tubo polínico)"
        self.exemplos = [
            {"nome": "Cica", "caracteristicas": "Palmeirinha comum em praças"},
            {"nome": "Pinheiro-bravo", "caracteristicas": "Única nativa da Caatinga de altitude"},
            {"Infelizmente não temos muitas Gimnospermas porque elas vivem em climas mais frios"}
        ]


class Angiospermas(ComFlores):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self.frutos = "sim"
        self._caracteristicas = "Grupo mais complexo. Possuem vasos, sementes, flores e frutos. O fruto protege a semente. Independem da água para fecundação."
        self.exemplos = [
            {"nome": "Carnaúba", "caracteristicas": "Árvore da Vida do Ceará 8                                              **"},
            {"nome": "Milho","caracteristicas": "Plantado no sertão no São João                                             **"},
            {"nome": "Cana-de-açúcar","caracteristicas": "Cultivada em áreas de várzea e beira de rios                      **"},
            {"nome": "Palma-forrageira","caracteristicas": "Cacto introduzido, essencial para alimentar animais na seca"},
            {"nome": "Orquídea-da-caatinga", "caracteristicas": "Espécie epífita que resiste ao sol forte"},
            {"nome": "Mandacaru", "caracteristicas": "Cacto grande que serve de alimento para o gado                        **"},
            {"nome": "Xique-xique", "caracteristicas": "Cacto com muitos espinhos que cresce em solos pedregosos            **"},
            {"nome": "Juazeiro", "caracteristicas": "Rara árvore que não perde as folhas na seca                            **"},
            {"nome": "Jurema-preta", "caracteristicas": "Árvore com casca escura e grande importância cultural"},
            {"nome": "Angico", "caracteristicas": "Árvore alta com casca que possui propriedades medicinais                 **"}
        ]


class Monocotiledôneas(Angiospermas):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self._caracteristicas = "A semente não abre ao meio (é um grão só). A raiz é aquele monte de fiozinho igual cabelo. A folha tem as linhas todas retinhas, uma do lado da outra."
        self.exemplos = [
            {"nome": "Carnaúba", "caracteristicas": "Árvore da Vida do Ceará                                                **"},
            {"nome": "Milho", "caracteristicas": "Plantado no sertão no São João                                            **"},
            {"nome": "Caroá", "caracteristicas": "Planta com fibras usadas para fazer cordas e artesanato"},
            {"nome": "Macambira", "caracteristicas": "Bromélia de chão com espinhos que protege o solo"},
            {"nome": "Palma-forrageira", "caracteristicas": "Cacto introduzido, essencial para alimentar animais na seca"},
            {"nome": "Capim-panasco", "caracteristicas": "Grama nativa que cresce rápido nas chuvas"},
            {"nome": "Gravatá", "caracteristicas": "Bromélia de flores vistosas e folhas em formato de espada"},
            {"nome": "Palmeira Catolé", "caracteristicas": "Palmeira que ocorre em áreas de baixio na Caatinga"},
            {"nome": "Cana-de-açúcar", "caracteristicas": "Cultivada em áreas de várzea e beira de rios                     **"},
            {"nome": "Orquídea-da-caatinga", "caracteristicas": "Espécie epífita que resiste ao sol forte"},
        ]


class Dicotiledoneas(Angiospermas):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self._caracteristicas = "A semente abre em duas partes (tipo o feijão). A raiz tem uma parte central mais grossa que entra fundo na terra. A folha tem as linhas todas espalhadas como se fossem galhos."
        self.exemplos = [
            {"nome": "Umbuzeiro", "caracteristicas": "Árvore sagrada que armazena água nas raízes"},
            {"nome": "Juazeiro", "caracteristicas": "Rara árvore que não perde as folhas na seca                   **"},
            {"nome": "Catingueira", "caracteristicas": "Árvore que floresce rapidamente após a primeira chuva"},
            {"nome": "Baraúna", "caracteristicas": "Madeira escura e extremamente resistente"},
            {"nome": "Aroeira-do-sertão", "caracteristicas": "Muito usada para fins medicinais e construção"},
            {"nome": "Mandacaru", "caracteristicas": "Cacto grande que serve de alimento para o gado               **"},
            {"nome": "Xique-xique", "caracteristicas": "Cacto com muitos espinhos que cresce em solos pedregosos   **"},
            {"nome": "Mulungu", "caracteristicas": "Possui flores vermelhas intensas e sementes tóxicas"},
            {"nome": "Jurema-preta", "caracteristicas": "Árvore com casca escura e grande importância cultural"},
            {"nome": "Angico", "caracteristicas": "Árvore alta com casca que possui propriedades medicinais        **"}
        ]
