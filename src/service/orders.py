# OrdersStreamService

"""
TradesStream
Stream сделок пользователя

Тело запроса — TradesStreamRequest

Тело ответа — TradesStreamResponse
"""

#########################################################

# OrdersService

"""
Сервис предназначен для работы с торговыми поручениями:
1. выставление;
2. отмена;
3. получение статуса;
4. расчёт полной стоимости;
5. получение списка заявок.
"""
##########################################################

# Методы сервиса

"""
PostOrder
Метод выставления заявки.

Тело запроса — PostOrderRequest

Тело ответа — PostOrderResponse
"""

"""
CancelOrder
Метод отмены биржевой заявки.

Тело запроса — CancelOrderRequest

Тело ответа — CancelOrderResponse
"""

"""
GetOrderState
Метод получения статуса торгового поручения.

Тело запроса — GetOrderStateRequest

Тело ответа — OrderState
"""

"""
GetOrders
Метод получения списка активных заявок по счёту.

Тело запроса — GetOrdersRequest

Тело ответа — GetOrdersResponse
"""

