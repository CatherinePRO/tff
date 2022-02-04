# InstrumentsService
"""
Сервис предназначен для получения:
1. информации об инструментах;
2. расписания торговых сессий;
3. календаря выплат купонов по облигациям;
4. размера гарантийного обеспечения по фьючерсам;
5. дивидендов по ценной бумаге.
"""
##################################################

# Методы сервиса

"""
TradingSchedules
Метод получения расписания торгов торговых площадок.

Тело запроса — TradingSchedulesRequest

Тело ответа — TradingSchedulesResponse
"""

"""
BondBy
Метод получения облигации по её идентификатору.

Тело запроса — InstrumentRequest

Тело ответа — BondResponse
"""

"""
Bonds
Метод получения списка облигаций.

Тело запроса — InstrumentsRequest

Тело ответа — BondsResponse
"""

"""
CurrencyBy
Метод получения валюты по её идентификатору.

Тело запроса — InstrumentRequest

Тело ответа — CurrencyResponse
"""

"""
Currencies
Метод получения списка валют.

Тело запроса — InstrumentsRequest

Тело ответа — CurrenciesResponse
"""

"""
EtfBy
Метод получения инвестиционного фонда по его идентификатору.

Тело запроса — InstrumentRequest

Тело ответа — EtfResponse
"""

"""
Etfs
Метод получения списка инвестиционных фондов.

Тело запроса — InstrumentsRequest

Тело ответа — EtfsResponse
"""

"""
FutureBy
Метод получения фьючерса по его идентификатору.

Тело запроса — InstrumentRequest

Тело ответа — FutureResponse
"""

"""
Futures
Метод получения списка фьючерсов.

Тело запроса — InstrumentsRequest

Тело ответа — FuturesResponse
"""

"""
ShareBy
Метод получения акции по её идентификатору.

Тело запроса — InstrumentRequest

Тело ответа — ShareResponse
"""

"""
Shares
Метод получения списка акций.

Тело запроса — InstrumentsRequest

Тело ответа — SharesResponse
"""

"""
GetAccruedInterests
Метод получения накопленного купонного дохода по облигации.

Тело запроса — GetAccruedInterestsRequest

Тело ответа — GetAccruedInterestsResponse
"""

"""
GetFuturesMargin
Метод получения размера гарантийного обеспечения по фьючерсам.

Тело запроса — GetFuturesMarginRequest

Тело ответа — GetFuturesMarginResponse
"""

"""
GetInstrumentBy
Метод получения основной информации об инструменте.

Тело запроса — InstrumentRequest

Тело ответа — InstrumentResponse
"""

"""
GetDividends
Метод для получения событий выплаты дивидендов по инструменту.

Тело запроса — GetDividendsRequest

Тело ответа — GetDividendsResponse
"""

