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

    # 🌊 Flow contínuo (sem pausas)
    write("Ah, quando um abraço apertado se encaixa", 0.088, "blue")

    write("É como se o mundo parasse ali, é como se a vida acabasse", 0.085, "white")

    write("Sei lá...", 0.095, "blue")

    # 🔁 Repetição direta
    write("Quando um abraço apertado se encaixa", 0.088, "blue")

    write("É como se o mundo parasse ali, é como se a vida acabasse", 0.085, "white")

    write("Sei lá...", 0.095, "blue")

    time.sleep(1.5)
    clear()

sing()