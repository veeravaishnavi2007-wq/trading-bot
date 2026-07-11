# Binance Futures Testnet Trading Bot

A robust, CLI-based Python trading bot designed to interact with the Binance Futures Testnet (USDT-M). This bot emphasizes clear architecture, robust validation, rich logging, and an enhanced user experience using `Typer` and `Rich`.

## Features
- **Supported Orders**: `MARKET`, `LIMIT`, and `STOP_MARKET` (Bonus requirement).
- **Interactive Mode**: A guided prompt-based CLI (Bonus requirement).
- **Rich Output**: Beautiful tables and panels for terminal output.
- **Robust Logging**: Both a file-based log (`bot.log`) and structured console output.
- **Validation**: Strict input validation before API requests are sent.

## Prerequisites
- Python 3.8+
- Binance Futures Testnet Account

## Setup Instructions

1. **Clone or Extract the Project**
   Ensure you are in the `trading_bot` directory.

2. **Install Dependencies**
   It's recommended to use a virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Credentials**
   Rename `.env.example` to `.env` and fill in your Binance Futures Testnet credentials:
   ```bash
   cp .env.example .env
   ```
   Add your keys inside `.env`:
   ```
   BINANCE_API_KEY="your_api_key_here"
   BINANCE_API_SECRET="your_api_secret_here"
   ```

## How to Run (Examples)

You can run the bot using the command-line flags or through the interactive menu.

### Interactive Mode (Recommended)
This mode prompts you for all necessary fields step-by-step.
```bash
python cli.py interactive
```

### CLI Mode
**Place a MARKET Order:**
```bash
python cli.py order --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Place a LIMIT Order:**
```bash
python cli.py order --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.5 --price 3500.0
```

**Place a STOP_MARKET Order (Bonus):**
```bash
python cli.py order --symbol BTCUSDT --side BUY --type STOP_MARKET --quantity 0.01 --stop-price 70000.0
```

### View Help
To see all available commands and options:
```bash
python cli.py --help
python cli.py order --help
```

## Logs
All bot activity, including request payloads, API responses, and potential validation or network errors, are logged to `bot.log` located in the root directory.

## Assumptions & Notes
- This bot is strictly meant for the **Futures Testnet (USDT-M)** (`https://testnet.binancefuture.com`). Do not use this with real funds on the mainnet.
- Error handling includes capturing `BinanceAPIException`, `BinanceRequestException`, and validation `ValueError`s, ensuring graceful failures instead of raw stack traces.
- `typer`, `rich`, and `python-binance` libraries significantly streamline the code, reducing boilerplate while delivering professional UX and API structures.
