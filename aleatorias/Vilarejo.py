import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.074, cor="white", pausa=1.2):
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

    # 🌸 Parte leve e fluida
    write("Lá o tempo espera", 0.074, "blue", 1)
    write("Lá é primavera", 0.074, "blue", 1)

    write("Portas e janelas", 0.074, "white", 0.8)
    write("Ficam sempre abertas", 0.074, "white", 0.8)
    write("Pra sorte entrar", 0.074, "yellow", 1.5)

    console.print()
    time.sleep(1)

    # 🌼 Continuação (mais conectada)
    write("Em todas as mesas, pão", 0.074, "white", 1)

    write("Flores enfeitando", 0.074, "blue", 0.8)
    write("Os caminhos, os vestidos", 0.074, "white", 0.8)
    write("Os destinos e essa canção", 0.074, "white", 1.2)

    console.print()
    time.sleep(1)

    # 💛 Final (mais destacado)
    write("Tem um verdadeiro amor", 0.072, "yellow", 1)
    write("Para quando você for", 0.072, "yellow", 2)

    time.sleep(2)
    clear()

sing()