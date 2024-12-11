import typer
from .composeCraft import app as compose_craft_app
from .container import app as container_app

app = typer.Typer()


@app.callback(invoke_without_command=True)
def default(ctx: typer.Context):
    # Only print help if no subcommand is invoked
    if ctx.invoked_subcommand is None:
        print("""
Dockscribe helps you understand and debug a docker stack.

First you need to login to composecraft.com as it uses this website UI to show you the diagram.
\t$ dockscribe login
Then you can use:
\t$ dockscribe describe

If you need any more help, you can use:
\t$ dockscribe --help
""")

app.add_typer(compose_craft_app)
app.add_typer(container_app)

if __name__ == "__main__":
    app()