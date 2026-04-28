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

    # 🌵 Entrada (livre, fora do tempo)
    write("E o meu coração deseja Te encontrar", 0.12, "blue", 2.8)

    console.print()
    time.sleep(1.8)

    # 🌧️ Começa a encaixar no ritmo
    write("Como a terra seca anseia pela chuva", 0.095, "white", 2.5)

    console.print()
    time.sleep(1.5)

    # 🙏 Parte curta (mais lenta e destacada)
    write("Vem me saciar", 0.11, "blue", 2.2)

    console.print()
    time.sleep(1.5)

    # 🔥 Agora entra no pulso da música
    write("Pois eu descobri", 0.09, "white", 1.5)

    write("Que aqui é o meu lugar", 0.085, "yellow", 2.8)

    time.sleep(2)
    clear()

sing()