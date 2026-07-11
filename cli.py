import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, FloatPrompt
from bot.orders import OrderManager

app = typer.Typer(help="Binance Futures Testnet Trading Bot CLI", no_args_is_help=True)
console = Console()

@app.command()
def order(
    symbol: str = typer.Option(..., "--symbol", "-s", help="Trading pair symbol (e.g., BTCUSDT)"),
    side: str = typer.Option(..., "--side", "-S", help="Order side: BUY or SELL"),
    type: str = typer.Option(..., "--type", "-t", help="Order type: MARKET, LIMIT, or STOP_MARKET"),
    quantity: float = typer.Option(..., "--quantity", "-q", help="Order quantity"),
    price: float = typer.Option(None, "--price", "-p", help="Price (required for LIMIT orders)"),
    stop_price: float = typer.Option(None, "--stop-price", "-sp", help="Stop Price (required for STOP_MARKET orders)")
):
    """Place a new order on Binance Futures Testnet."""
    
    console.print(Panel.fit(f"[bold blue]Trading Bot - Order Request[/bold blue]\n\n"
                            f"Symbol:   [bold]{symbol.upper()}[/bold]\n"
                            f"Side:     [bold]{side.upper()}[/bold]\n"
                            f"Type:     [bold]{type.upper()}[/bold]\n"
                            f"Quantity: [bold]{quantity}[/bold]\n"
                            f"Price:    [bold]{price if price else 'N/A'}[/bold]\n"
                            f"Stop Px:  [bold]{stop_price if stop_price else 'N/A'}[/bold]",
                            title="Summary"))

    try:
        manager = OrderManager()
    except Exception as e:
        console.print(f"[bold red]Initialization Error:[/bold red] {e}")
        raise typer.Exit(1)
        
    with console.status("[bold green]Placing order...") as status:
        response = manager.place_order(
            symbol=symbol,
            side=side,
            order_type=type,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )
    
    if response:
        table = Table(title="Order Response Details", show_header=True, header_style="bold magenta")
        table.add_column("Key", style="cyan")
        table.add_column("Value", style="green")
        
        # Display key fields
        keys_to_show = ["orderId", "status", "symbol", "side", "type", "executedQty", "avgPrice", "clientOrderId"]
        for k in keys_to_show:
            val = response.get(k, "N/A")
            table.add_row(k, str(val))
            
        console.print(table)
        console.print("[bold green]Order placed successfully![/bold green]")
    else:
        console.print("[bold red]Failed to place order. Check the bot.log for details.[/bold red]")

@app.command()
def interactive():
    """Interactive mode for placing an order with prompts."""
    console.print("[bold cyan]Welcome to the Interactive Order Menu![/bold cyan]")
    
    symbol = Prompt.ask("Enter trading symbol", default="BTCUSDT")
    side = Prompt.ask("Enter side", choices=["BUY", "SELL"])
    order_type = Prompt.ask("Enter order type", choices=["MARKET", "LIMIT", "STOP_MARKET"])
    quantity = FloatPrompt.ask("Enter quantity")
    
    price = None
    if order_type == "LIMIT":
        price = FloatPrompt.ask("Enter limit price")
        
    stop_price = None
    if order_type == "STOP_MARKET":
        stop_price = FloatPrompt.ask("Enter stop price")
        
    # Execute the order logic by invoking the function directly
    order(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price, stop_price=stop_price)

if __name__ == "__main__":
    app()
