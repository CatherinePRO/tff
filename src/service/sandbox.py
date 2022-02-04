# SandboxService
"""
Сервис для работы с песочницей TINKOFF INVEST API
"""
###################################

# Методы сервиса

"""
OpenSandboxAccount
Метод регистрации счёта в песочнице.

Тело запроса — OpenSandboxAccountRequest

Тело ответа — OpenSandboxAccountResponse
"""

"""
GetSandboxAccounts
Метод получения счетов в песочнице.

Тело запроса — GetAccountsRequest

Тело ответа — GetAccountsResponse
"""

"""
CloseSandboxAccount
Метод закрытия счёта в песочнице.

Тело запроса — CloseSandboxAccountRequest

Тело ответа — CloseSandboxAccountResponse
"""

"""
PostSandboxOrder
Метод выставления торгового поручения в песочнице.

Тело запроса — PostOrderRequest

Тело ответа — PostOrderResponse
"""

"""
GetSandboxOrders
Метод получения списка активных заявок по счёту в песочнице.

Тело запроса — GetOrdersRequest

Тело ответа — GetOrdersResponse
"""

"""
CancelSandboxOrder
Метод отмены торгового поручения в песочнице.

Тело запроса — CancelOrderRequest

Тело ответа — CancelOrderResponse
"""

"""
GetSandboxOrderState
Метод получения статуса заявки в песочнице.

Тело запроса — GetOrderStateRequest

Тело ответа — OrderState
"""

"""
GetSandboxPositions
Метод получения позиций по виртуальному счёту песочницы.

Тело запроса — PositionsRequest

Тело ответа — PositionsResponse
"""

"""
GetSandboxOperations
Метод получения операций в песочнице по номеру счёта.

Тело запроса — OperationsRequest

Тело ответа — OperationsResponse
"""

"""
GetSandboxPortfolio
Метод получения портфолио в песочнице.

Тело запроса — PortfolioRequest

Тело ответа — PortfolioResponse
"""

"""
SandboxPayIn
Метод пополнения счёта в песочнице.

Тело запроса — SandboxPayInRequest

Тело ответа — SandboxPayInResponse
"""