import sys

from tinkoff.invest import Client
from tokenIT.token_v2 import token

def main() -> int:
    with Client(token) as client:
        print(client.users.get_accounts())

    return 0


if __name__ == "__main__":
    sys.exit(main())