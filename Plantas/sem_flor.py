from Plantas.planta import Planta

class SemFlores(Planta):
    def __init__(self, nome, especie):
        super().__init__(nome,especie)
        self.flores = "não"
        self.frutos = "não"
        self.sementes = "não"



class Briofita(SemFlores):
    def __init__(self,nome,especie):
        super().__init__(nome,especie)
        self._caracteristicas = "Pequeno porte, avasculares (sem vasos condutores), sem sementes, sem flores e sem frutos. Dependem totalmente da água para a fecundação (gametas nadam)."
        self.exemplos = [
            {"nome": "Musgo-de-Pedra", "caracteristicas": "Fica cinza na seca e acorda com a chuva"},
            {"nome": "Musgo-de-Parede", "caracteristicas": "Comum em áreas de sombra nas serras cearenses"},
            {"nome": "Hepática-de-rocha", "caracteristicas": "Planta achatada que cresce em fendas úmidas"},
            {"nome": "Musgo-cabeludo", "caracteristicas": "Aparece sobre troncos de árvores após as chuvas"},
            {"nome": "Riccia-do-sertão", "caracteristicas": "Hepática que surge em solos encharcados temporariamente"},
            {"nome": "Tortula", "caracteristicas": "Musgo especialista em sobreviver a longos períodos sem água"}
        ]




class Pteridofitas(SemFlores):
    def __init__(self, nome, especie):
        super().__init__(nome,especie)
        self._caracteristicas = "Vasculares (presença de xilema e floema), possuem raiz, caule e folhas verdadeiras, mas não possuem sementes, flores ou frutos. Ainda dependem da água para reprodução"
        self.exemplos = [
            {"nome": "Samambaia-paulistinha", "caracteristicas": "Comum em áreas de transição para mata mais úmida"},
            {"nome": "Flor-da-Ressurreição (Selaginela)", "caracteristicas": "Se enrola na seca para sobreviver ao sol"},
            {"nome": "Avenca-comum", "caracteristicas": "Cresce em paredes de poços e riachos sombreados"},
            {"nome": "Cavalinha-do-rio", "caracteristicas": "Encontrada em margens de rios que não secam totalmente"},
            {"nome": "Samambaia-de-rocha", "caracteristicas": "Pequena e resistente, vive entre as pedras"  },
            {"nome": "Trevo-de-quatro-folhas-aquático", "caracteristicas": "Vive em poças que se formam após grandes chuvas"},
        ]








