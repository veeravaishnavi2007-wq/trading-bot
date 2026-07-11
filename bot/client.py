import os
from binance.client import Client
from dotenv import load_dotenv
from .logging_config import logger

class BinanceTestnetClient:
    """Wrapper for Binance Client specifically targeting Futures Testnet."""

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key or not self.api_secret:
            logger.error("API credentials missing. Please check your .env file.")
            raise ValueError("Missing BINANCE_API_KEY or BINANCE_API_SECRET in environment.")

        # Initialize the python-binance client
        # To use futures testnet, testnet=True parameter must be set
        self.client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
            testnet=True
        )
        logger.info("Initialized Binance Futures Testnet client.")

    def ping(self):
        """Test connectivity to the Futures Testnet API."""
        try:
            res = self.client.futures_ping()
            logger.info("Successfully pinged Futures Testnet API.")
            return res
        except Exception as e:
            logger.error(f"Failed to ping API: {e}")
            raise e
