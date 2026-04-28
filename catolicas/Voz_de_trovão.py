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

    # 🌩️ Parte central
    write("O céu se abriu", 0.09, "white")
    time.sleep(0.8)

    write("Ouviu-se o som da Sua voz", 0.085, "white")
    time.sleep(1)

    write("O noivo vem", 0.09, "yellow")
    time.sleep(0.8)

    write("Eu posso ver Seus sinais", 0.085, "white")
    time.sleep(1.2)

    console.print()

    # 🔥 Refrão final
    write("Com voz de trovão", 0.09, "yellow")
    time.sleep(0.7)

    write("Olhos de fogo Ele vem", 0.085, "white")
    time.sleep(1)

    write("Maranata ora vem!", 0.08, "green")
    time.sleep(0.6)

    write("Maranata ora vem!", 0.08, "green")

    time.sleep(2)
    clear()

sing()