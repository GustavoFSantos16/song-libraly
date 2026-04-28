import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.085, cor="white"):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")

def sing():
    clear()

    # 🔥 Parte inicial (lenta e forte)
    write("Fogo santo", 0.10, "yellow")
    time.sleep(1)

    write("Poderoso Deus", 0.095, "white")
    time.sleep(1)

    write("Vem, ó defensor", 0.095, "white")
    time.sleep(1)

    write("Tua noiva está aqui", 0.095, "blue")
    time.sleep(1.5)

    console.print()

    # 🔁 Repetição (mais firme)
    write("Fogo santo", 0.095, "yellow")
    time.sleep(0.8)

    write("Poderoso Deus", 0.09, "white")
    time.sleep(1)

    write("Arde outra vez", 0.09, "yellow")
    time.sleep(1)

    write("Tua noiva está aqui", 0.095, "blue")
    time.sleep(1.5)

    console.print()

    # 🌊 Parte final (declaração)
    write("A verdadeira glória do Céu descerá", 0.085, "white")
    time.sleep(1.2)

    write("Os filhos de Maria vão então declarar", 0.085, "white")
    time.sleep(1.2)

    write("Que como a mãe Deus foi toda Tua", 0.085, "green")
    time.sleep(1.2)

    write("Eu sou todo Teu, meu Deus!", 0.08, "yellow")

    time.sleep(2)
    clear()

sing()