from pathlib import Path

import yfinance as yf


DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def download_prices(
    tickers: list[str],
    start: str = "2018-01-01",
    end: str | None = None,
):
    """Download adjusted daily prices and save them as CSV."""

    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False,
    )

    if data.empty:
        raise ValueError("No data was downloaded.")

    # We only need closing prices for the first version.
    prices = data["Close"].copy()

    output_path = DATA_DIR / "prices.csv"
    prices.to_csv(output_path)

    print(f"Saved {len(prices):,} rows to {output_path}")
    print()
    print(prices.head())

    return prices


if __name__ == "__main__":
    download_prices(["KO", "PEP"])