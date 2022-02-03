#from itertools import count
import sys

from tinkoff.invest import Client
from tokenIT.token_v2 import token
#from tinkoff.invest.schemas import GetAccountsResponse

def main() -> int:
    with Client(token) as client:
        accounts = client.users.get_accounts().accounts
        for i in accounts:
            account_id = i.id
            #print(i)
            print(account_id)
            print(client.users.get_margin_attributes(account_id = account_id))

    return 0
       
if __name__ == "__main__":
    sys.exit(main())