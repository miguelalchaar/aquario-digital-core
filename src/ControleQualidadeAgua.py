class ControleQualidadeAgua:
    def __init__(self, ph, temperatura):
        self.ph = ph
        self.temperatura = temperatura

    def verificar_parametros(self):
        if self.ph < 6.8 or self.ph > 7.6:
            print("ALERTA QA: Nível de pH fora do limite ideal!")
            return False

        if self.temperatura < 22.0 or self.temperatura > 28.0:
            print("ALERTA QA: Temperatura fora do limite seguro!")
            return False

        print("STATUS: Parâmetros da água em níveis ideais.")
        return True

agua = ControleQualidadeAgua(7.2, 25.0)
agua.verificar_parametros()