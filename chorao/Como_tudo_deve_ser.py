import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.073, cor="white", pausa=1.0):
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

    # 🎸 Parte 1
    write("É foda ser louco, advogado do mundo, mas", 0.073, "white", 0.7)
    write("Como tudo deve ser?", 0.09, "yellow", 1.5)

    console.print()
    time.sleep(0.7)

    write("É foda ser tachado de doido, vagabundo, mas", 0.073, "white", 0.7)
    write("Como tudo deve ser?", 0.095, "yellow", 1.7)

    console.print()
    time.sleep(1.2)

    # 🌊 Parte 2 (mantém fluida)
    write("Foi quando te encontrei", 0.075, "blue", 0.6)
    write("Ouvindo o som e olhando o mar", 0.075, "white", 0.8)

    write("Foi quando te encontrei", 0.075, "blue", 0.6)
    write("Ouvindo o som do mar rolar", 0.075, "white", 1.5)

    time.sleep(2)
    clear()

sing()