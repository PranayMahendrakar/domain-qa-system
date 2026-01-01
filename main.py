#!/usr/bin/env python3
"""Domain QA System - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import AnswerGenerator

console = Console()
qa = AnswerGenerator()

def main():
    console.print(Panel("❓ DOMAIN QA SYSTEM ❓\nAsk Questions About Your Subject", style="bold orange1"))
    domain = Prompt.ask("What subject/domain?", default="General")
    qa.system_prompt = f"You are an expert in {domain}. Answer questions accurately."
    
    console.print(f"[green]Ready to answer {domain} questions. Type 'quit' to exit.[/green]\n")
    
    while True:
        question = Prompt.ask("[bold]Question[/bold]")
        if question.lower() == 'quit': break
        answer = qa.process(question)
        console.print(Panel(Markdown(answer), title="Answer", border_style="orange1"))

if __name__ == "__main__": main()
