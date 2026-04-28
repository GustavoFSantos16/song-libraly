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

    write("A tumba foi aberta", 0.09, "blue", 1.2)
    write("Tua voz me chamou pra vir pra fora", 0.08, "blue", 1.8)

    console.print()
    time.sleep(1)

    write("Sou como Lázaro, ressuscitado", 0.07, "yellow", 2)

    console.print()
    time.sleep(1.5)

    write("A morte não venceu, Teu amor me salvou", 0.08, "white", 2)

    console.print()
    time.sleep(1)

    write("E agora eu posso cantar", 0.09, "blue", 1)

    write("Que sou como Lázaro, ressuscitado", 0.07, "yellow", 2.5)

    time.sleep(2)
    clear()

sing()