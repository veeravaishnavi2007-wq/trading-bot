from typing import Optional

def validate_symbol(symbol: str) -> str:
    """Validate and format the trading symbol."""
    return symbol.upper().strip()

def validate_side(side: str) -> str:
    """Validate trading side."""
    side = side.upper().strip()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be either 'BUY' or 'SELL'.")
    return side

def validate_order_type(order_type: str) -> str:
    """Validate order type."""
    order_type = order_type.upper().strip()
    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Order type must be 'MARKET', 'LIMIT', or 'STOP_MARKET'.")
    return order_type

def validate_price_quantity(
    order_type: str, quantity: float, price: Optional[float], stop_price: Optional[float]
) -> None:
    """Validate price and quantity based on order type."""
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")
    
    if order_type == "LIMIT":
        if price is None or price <= 0:
            raise ValueError("LIMIT orders require a price strictly greater than 0.")
    elif order_type == "STOP_MARKET":
        if stop_price is None or stop_price <= 0:
            raise ValueError("STOP_MARKET orders require a stop price strictly greater than 0.")
