import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.065, cor="white"):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")

def sing():
    clear()

    # ⚡ Entrada do refrão (mais espaçado)
    write("Oh, oh, oh", 0.08, "magenta")
    time.sleep(0.4)

    write("Oh, oh, oh", 0.08, "magenta")
    time.sleep(0.5)

    # 💥 Entra no beat
    write("Don't stop 'cause I need this feeling", 0.065, "yellow")
    time.sleep(0.6)

    # 🔁 Segunda volta (mais encaixada)
    write("Oh, oh, oh", 0.075, "magenta")
    time.sleep(0.3)

    write("Oh, oh, oh", 0.075, "magenta")
    time.sleep(0.4)

    write("Don't stop 'cause I need this feeling", 0.065, "yellow")

    time.sleep(1.5)
    clear()

sing()