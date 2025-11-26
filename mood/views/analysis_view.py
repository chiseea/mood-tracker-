from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.align import Align
import time

console = Console()

class AnalysisView:
    def show_analysis(self, rows, avg):
        if not rows:
            console.print(Panel.fit("[yellow]Belum ada data untuk dianalisis.[/yellow]", border_style="yellow"))
            return

        for _ in track(range(30), description="Menganalisis mood...", transient=True):
            time.sleep(0.03)

        if avg >= 8:
            mood_msg = "Kamu sangat bahagia akhir-akhir ini!"
            color = "bold green"
        elif avg >= 5:
            mood_msg = "Mood kamu cukup stabil."
            color = "bold yellow"
        else:
            mood_msg = "Mood kamu sedang menurun, coba istirahat ya."
            color = "bold red"

        panel_content = (
            f"[white]Rata-rata Mood: [bold cyan]{avg:.2f}/10[/bold cyan]\n\n"
            f"{mood_msg}\n\nTotal Data: [bold magenta]{len(rows)} hari[/bold magenta]"
        )
        console.print(Panel(Align.left(panel_content), title="Hasil Analisis", border_style=color))
