# main.py
from mood.di import create_container
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align

console = Console()

def tampilkan_header():
    console.clear()
    header = Panel(
        Align.center(
            "[bold magenta] SISTEM MANAJEMEN MOOD HARIAN [/bold magenta]"
        ),
        border_style="bright_magenta",
        padding=(1, 2),
    )
    console.print(header)

def main():
    tampilkan_header()
    container = create_container()
    menu_ctrl = container["menu_controller"]

    nama = Prompt.ask("Masukkan nama pengguna")
    menu_ctrl.run(nama)  # controller akan mengatur loop utama

if __name__ == "__main__":
    main()
