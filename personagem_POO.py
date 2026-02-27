class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida  # atributo protegido

    def atacar(self, outro_personagem):
        print("Ataque básico!")

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nome} agora tem {self._vida} de vida.")

    def esta_vivo(self):
        return self._vida > 0


class Guerreiro(Personagem):
    def atacar(self, outro_personagem):
        dano = 20
        print(f"{self.nome} atacou com espada causando {dano} de dano!")
        outro_personagem.receber_dano(dano)


class Mago(Personagem):
    def atacar(self, outro_personagem):
        dano = 25
        print(f"{self.nome} lançou magia causando {dano} de dano!")
        outro_personagem.receber_dano(dano)


# ---------------- TESTANDO O SISTEMA ----------------

guerreiro = Guerreiro("Aragorn", 100)
mago = Mago("Gandalf", 80)

guerreiro.atacar(mago)
mago.atacar(guerreiro)

print("Guerreiro está vivo?", guerreiro.esta_vivo())
print("Mago está vivo?", mago.esta_vivo())