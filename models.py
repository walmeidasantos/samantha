class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Wellington",  "wsantos", "tg02069")


usuarios = { usuario1.nickname : usuario1}