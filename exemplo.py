class TarefaLogica():
    def __init__(self):
        pass

    def listarTarefas(self, Usuario):
        lista = [
            {
                email: "fernando@eu.com",
                nome: "Fernando",
                senha: "123"
            },
            {
                email: "fulano@eu.com",
                nome: "Fulano",
                senha: "456"
            }
        ]
        return lista

class UsuarioLogica():
    def __init__(self):
        pass

    def registrarUsuario(self, nome, email, senha):
        return ""


    def autenticarUsuario(self, email, senha):
        pass

logica = UsuarioLogica()
logica.registrarUsuario('Fernando Passos', "fernando@email.com", '123')
