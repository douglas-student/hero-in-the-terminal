import curses

# Classe Heroi com as propriedades e método atacar
class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"
        
        return f"o {self.tipo} atacou usando {ataque}"

# Função principal que cria a interface de terminal com curses
def main(stdscr):
    # Limpar tela
    curses.curs_set(0)  # Esconde o cursor
    stdscr.clear()

    # Iniciar cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)  # Branco no fundo vermelho

    # Criando heróis
    herois = [
        Heroi("Aragorn", 30, "guerreiro"),
        Heroi("Merlin", 50, "mago"),
        Heroi("Bruce", 25, "monge"),
        Heroi("Kage", 20, "ninja")
    ]

    # Mostrar informações dos heróis
    stdscr.addstr(0, 0, "Escolha o herói para atacar:")
    for idx, heroi in enumerate(herois):
        stdscr.addstr(idx + 1, 0, f"{idx + 1}. {heroi.nome} - {heroi.tipo}")

    # Aguardar a entrada do usuário para selecionar um herói
    stdscr.refresh()
    selecionado = None
    while selecionado is None:
        key = stdscr.getch()
        if key == ord('1') or key == ord('2') or key == ord('3') or key == ord('4'):
            selecionado = int(chr(key)) - 1

    # Exibir ataque do herói selecionado com fundo vermelho e texto branco
    heroi_selecionado = herois[selecionado]
    stdscr.clear()
    stdscr.addstr(0, 0, f"Você escolheu o herói {heroi_selecionado.nome}!")

    # Ativar o par de cores (fundo vermelho e texto branco)
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr(2, 0, f"{heroi_selecionado.atacar()}")  # Exibe o ataque
    stdscr.attroff(curses.color_pair(1))  # Desativa o par de cores
    stdscr.addstr(4, 0, "Pressione qualquer tecla para sair...")
    stdscr.refresh()

    # Aguardar o usuário pressionar uma tecla para sair
    stdscr.getch()

# Inicializando a interface curses
if __name__ == "__main__":
    curses.wrapper(main)
