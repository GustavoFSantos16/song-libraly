import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.08, cor="white", pausa=1.5):
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

    # 🌊 Entrada (fora do tempo - livre)
    write("Me leva...", 0.18, "blue", 1.8)
    write("a esse lugar...", 0.18, "blue", 2.2)

    console.print()
    time.sleep(1.5)

    # 🎵 Entra no ritmo (batida começa a encaixar)
    write("Me leva...", 0.12, "blue", 1.2)
    write("a esse lugar...", 0.11, "blue", 1.5)

    console.print()
    time.sleep(1)

    # 🔥 Refrão em padrão (ritmo constante)
    write("Onde o fogo não se apaga", 0.085, "white", 1.1)
    write("Onde o fogo não se apaga", 0.085, "white", 1.1)
    write("Onde o fogo não se apaga, e não se apagará jamais", 0.08, "yellow", 2.2)

    console.print()
    time.sleep(1.5)

    # 💥 Parte forte (encaixada na batida)
    write("Esse fogo que me consumiu", 0.08, "white", 1.2)
    write("Essa chama que não se apagou", 0.08, "white", 1.2)

    console.print()
    time.sleep(1)

    write("Como oferta entregue no altar", 0.08, "blue", 1.2)
    write("Devorada pelo fogo abrasador", 0.075, "yellow", 2)

    time.sleep(2)
    clear()

sing()