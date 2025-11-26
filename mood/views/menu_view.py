from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

class MenuView:
    def show_menu(self, nama):
        menu = Text()
        menu.append("1. Tambah Mood Baru\n", style="cyan")
        menu.append("2. Lihat Riwayat Mood\n", style="green")
        menu.append("3. Hapus Data Mood\n", style="red")
        menu.append("4. Analisis Mood\n", style="yellow")
        menu.append("5. Keluar\n", style="magenta")

        panel = Panel(
            Align.left(menu),
            title=f"[bold yellow]MENU UTAMA UNTUK {nama.upper()}[/bold yellow]",
            title_align="center",
            border_style="yellow",
            padding=(1, 4),
        )
        console.print(panel)
