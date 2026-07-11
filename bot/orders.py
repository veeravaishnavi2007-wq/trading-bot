from typing import Optional, Dict, Any
from .client import BinanceTestnetClient
from .validators import validate_symbol, validate_side, validate_order_type, validate_price_quantity
from .logging_config import logger
from binance.exceptions import BinanceAPIException, BinanceRequestException

class OrderManager:
    def __init__(self):
        self.client_wrapper = BinanceTestnetClient()
        self.client = self.client_wrapper.client

    def place_order(
        self,
        symbol: str,
        side: str,
        order_type: str,
        quantity: float,
        price: Optional[float] = None,
        stop_price: Optional[float] = None,
    ) -> Optional[Dict[str, Any]]:
        """Place an order on the Binance Futures Testnet."""
        
        try:
            # Validate Inputs
            symbol = validate_symbol(symbol)
            side = validate_side(side)
            order_type = validate_order_type(order_type)
            validate_price_quantity(order_type, quantity, price, stop_price)
            
            logger.info(f"Attempting to place {side} {order_type} order for {quantity} {symbol}")
            
            order_params = {
                "symbol": symbol,
                "side": side,
                "type": order_type,
                "quantity": quantity,
            }

            if order_type == "LIMIT":
                order_params["price"] = price
                order_params["timeInForce"] = "GTC" # Good Till Cancelled
            elif order_type == "STOP_MARKET":
                order_params["stopPrice"] = stop_price
                order_params["closePosition"] = False # Simple STOP_MARKET entry/exit
            
            logger.debug(f"Order parameters: {order_params}")
            
            # Place the order via Futures API
            response = self.client.futures_create_order(**order_params)
            
            logger.info(f"Order successfully placed! Order ID: {response.get('orderId')}")
            logger.debug(f"API Response: {response}")
            
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Exception: Status Code: {e.status_code}, Message: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Binance Request Exception: Network error or invalid request - {e}")
        except ValueError as e:
            logger.error(f"Validation Error: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            
        return None
