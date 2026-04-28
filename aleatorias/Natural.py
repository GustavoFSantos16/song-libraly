import time
import os
from rich.console import Console
from rich.live import Live

console = Console()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def write(text, speed=0.082, cor="white"):
    linha = ""

    with Live("", console=console, refresh_per_second=20, transient=True) as live:
        for letra in text:
            linha += letra
            live.update(f"[{cor}]{linha}[/]")
            time.sleep(speed)

    console.print(f"[bold {cor}]{text}[/]")

def sing():
    clear()

    # 🔥 PRIMEIRA ENTRADA (batida forte)
    write("'Cause you're a natural", 0.078, "yellow")
    time.sleep(0.35)

    write("A beating heart of stone", 0.082, "white")
    time.sleep(0.3)

    write("You gotta be so cold", 0.082, "white")
    time.sleep(0.3)

    write("To make it in this world", 0.082, "white")
    time.sleep(0.45)

    # 💥 SEGUNDA PARTE (mais encaixada ainda)
    write("Yeah, you're a natural", 0.078, "yellow")
    time.sleep(0.3)

    write("Living your life cutthroat", 0.082, "white")
    time.sleep(0.3)

    write("You gotta be so cold", 0.082, "white")
    time.sleep(0.3)

    write("Yeah, you're a natural", 0.078, "yellow")

    time.sleep(1.5)
    clear()

sing()