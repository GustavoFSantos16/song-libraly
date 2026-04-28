import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.075, cor="white", pausa=1.2):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")
    time.sleep(pausa)

def sing():
    clear()

    # 💔 Parte inicial (explicativa, leve pausa)
    write("Não tem mais eu e você", 0.075, "white", 1)
    write("Tá fácil de entender", 0.075, "white", 1)

    write("Você me deu aula de como aprender te esquecer", 0.073, "blue", 1.8)

    console.print()
    time.sleep(1.2)

    # 🔥 Refrão (mais marcado e sofrido)
    write("Foi, mas não é mais a minha notificação preferida", 0.072, "yellow", 1.5)

    write("Já foi, mas não é mais a número um da minha vida", 0.072, "yellow", 1.8)

    console.print()
    time.sleep(1)

    # 💭 Final (mais calmo e direto)
    write("Sinto em te dizer", 0.078, "white", 1)

    write("Mas eu já superei você", 0.075, "blue", 2.2)

    time.sleep(2)
    clear()

sing()