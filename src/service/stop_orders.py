# StopOrdersService

"""
Сервис предназначен для работы со стоп-заявками:
1. выставление;
2. отмена;
3. получение списка стоп-заявок.
"""
##########################################################

# Методы сервиса

"""
PostStopOrder
Метод выставления стоп-заявки.

Тело запроса — PostStopOrderRequest

Тело ответа — PostStopOrderResponse
"""

"""
GetStopOrders
Метод получения списка активных стоп заявок по счёту.

Тело запроса — GetStopOrdersRequest

Тело ответа — GetStopOrdersResponse
"""

"""
CancelStopOrder
Метод отмены стоп-заявки.

Тело запроса — CancelStopOrderRequest

Тело ответа — CancelStopOrderResponse
"""