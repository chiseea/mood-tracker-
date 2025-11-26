from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align

class MenuController:
    def __init__(self, menu_view, mood_controller, analysis_controller):
        self.menu_view = menu_view
        self.mood_controller = mood_controller
        self.analysis_controller = analysis_controller
        self.console = None

    def run(self, nama):
        from rich.console import Console
        self.console = Console()
        while True:
            self.menu_view.show_menu(nama)
            pilihan = Prompt.ask("Pilih menu [1-5]", choices=["1","2","3","4","5"], default="5")
            if pilihan == "1":
                self.console.print(Panel("[bold cyan]TAMBAH DATA MOOD[/bold cyan]", border_style="cyan"))
                self.mood_controller.add_mood_interactive(nama)
            elif pilihan == "2":
                self.console.print(Panel("[bold magenta]RIWAYAT MOOD[/bold magenta]", border_style="magenta"))
                self.mood_controller.list_moods(nama)
            elif pilihan == "3":
                self.console.print(Panel("[bold red]HAPUS DATA MOOD[/bold red]", border_style="red"))
                self.mood_controller.delete_mood(nama)
            elif pilihan == "4":
                self.console.print(Panel("[bold yellow]ANALISIS MOOD[/bold yellow]", border_style="yellow"))
                self.analysis_controller.analyze(nama)
            elif pilihan == "5":
                self.console.print(Panel.fit(Align.center("[bold red]Terima kasih sudah menggunakan sistem ini![/bold red]\n[cyan]Sampai jumpa lagi![/cyan]"), border_style="bright_red"))
                break

