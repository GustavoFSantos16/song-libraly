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

    # 🎭 Início (roxo - mais emocional)
    write("Am I crazy?", 0.11, "magenta", 2)
    write("Maybe we could happen, yeah", 0.10, "green", 2)

    console.print()
    time.sleep(1.5)

    write("Will you still be", 0.105, "magenta", 1.5)
    write("With me when the magic's all run out?", 0.10, "green", 2.5)

    console.print()
    time.sleep(2)

    # 🌊 Crescimento
    write("If only I knew what my heart was telling me", 0.085, "green", 1.8)
    write("Don't know what I'm feeling, is this just a dream?", 0.085, "magenta", 2)

    write("Ah, oh", 0.09, "green", 1.5)

    console.print()
    time.sleep(1.5)

    # 💥 Refrão
    write("If only I could read the signs in front of me", 0.078, "magenta", 1.8)
    write("I could find the way to who I'm meant to be", 0.078, "green", 2)

    write("Oh, oh", 0.085, "magenta", 2.5)

    time.sleep(2)
    clear()

sing()