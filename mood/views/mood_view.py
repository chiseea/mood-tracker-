from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich import box

console = Console()

class MoodView:
    def show_added(self, tanggal):
        console.print(Panel.fit(f"[green]Data mood untuk {tanggal} berhasil ditambahkan![/green]", border_style="green"))

    def show_list(self, rows, user):
        if not rows:
            console.print(Panel.fit("[red]Belum ada data mood tersimpan![/red]", border_style="red"))
            return

        table = Table(
            title=f"Data Mood [{user}]",
            box=box.HEAVY_HEAD,
            header_style="bold white on blue",
            border_style="bright_black",
            show_lines=True,
        )
        table.add_column("ID", justify="center", style="bright_cyan", width=6)
        table.add_column("Tanggal", justify="center", style="green", width=14)
        table.add_column("Mood", justify="center", style="yellow", width=8)
        table.add_column("Aktivitas", style="white", width=24)
        table.add_column("Catatan", style="bright_magenta", width=30)
        table.add_column("Event Spesial", justify="center", style="bright_cyan", width=20)

        for r in rows:
            table.add_row(str(r[0]), r[1], str(r[2]), r[3], r[4], r[5])

        console.print(Panel(Align.left(table), title="Data Tersimpan", border_style="magenta", padding=(1,1)))

    def show_deleted(self, mood_id):
        console.print(Panel.fit(f"[red]Data dengan ID {mood_id} berhasil dihapus.[/red]", border_style="red"))
