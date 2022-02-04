# OperationsService

"""
Сервис предназначен для получения:
1. списка операций по счёту;
2. портфеля по счёту;
3. позиций ценных бумаг на счёте;
4. доступного остатка для вывода средств.
"""
#############################################

# Методы сервиса

"""
GetOperations
Метод получения списка операций по счёту.

Тело запроса — OperationsRequest

Тело ответа — OperationsResponse
"""

"""
GetPortfolio
Метод получения портфеля по счёту.

Тело запроса — PortfolioRequest

Тело ответа — PortfolioResponse
"""

"""
GetPositions
Метод получения списка позиций по счёту.

Тело запроса — PositionsRequest

Тело ответа — PositionsResponse
"""

"""
GetWithdrawLimits
Метод получения доступного остатка для вывода средств.

Тело запроса — WithdrawLimitsRequest

Тело ответа — WithdrawLimitsResponse
"""

"""
GetBrokerReport
Тело запроса — BrokerReportRequest

Тело ответа — BrokerReportResponse
"""
