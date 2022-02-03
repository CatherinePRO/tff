import sys
from datetime import datetime, timedelta

from tinkoff.invest import CandleInterval, Client
from tokenIT.token_v2 import token


def main() -> int:
    with Client(token) as client:
        for candle in client.get_all_candles(
            figi="BBG004730N88",
            from_=datetime.utcnow() - timedelta(days=365),
            interval=CandleInterval.CANDLE_INTERVAL_HOUR,
        ):
            print(candle)

    return 0


if __name__ == "__main__":
    sys.exit(main())
