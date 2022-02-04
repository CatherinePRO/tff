# MarketDataStreamService

"""
MarketDataStream
Bi-directional стрим предоставления биржевой информации.

Тело запроса — MarketDataRequest

Тело ответа — MarketDataResponse
"""

#########################################################

# MarketDataService

"""
Сервис получения биржевой информации:
1. свечи;
2. стаканы;
3. торговые статусы;
4. лента сделок.
"""
#############################################

# Методы сервиса

"""
GetCandles
Метод запроса исторических свечей по инструменту.

Тело запроса — GetCandlesRequest

Тело ответа — GetCandlesResponse
"""

"""
GetLastPrices
Метод запроса последних цен по инструментам.

Тело запроса — GetLastPricesRequest

Тело ответа — GetLastPricesResponse
"""

"""
GetOrderBook
Метод получения стакана по инструменту.

Тело запроса — GetOrderBookRequest

Тело ответа — GetOrderBookResponse
"""

"""
GetTradingStatus
Метод запроса статуса торгов по инструментам.

Тело запроса — GetTradingStatusRequest

Тело ответа — GetTradingStatusResponse
"""