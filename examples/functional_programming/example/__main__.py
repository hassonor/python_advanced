from itertools import takewhile

from customer import Customer
from order import Order
from order_item import OrderItem


def main():
    HoG = Customer('Heart of Gold', 'The Milky Way Galaxy', False)
    Millis = Customer('Milliways Restaurant', 'Magrathea', True)
    Arthur = Customer('Arthur Dent', 'Earth', False)
    drive = OrderItem('Infinite Improbability Drive', 42, 1, 100, True)
    Trillian = OrderItem('Date with Trillian', 43, 42, 1000000, True)
    choc = OrderItem('Chocolate', 44, 200, 250, False)

    ord1 = Order(1, 'Terra', False, False, HoG, (drive,))
    ord2 = Order(2, 'Heart of Gold', True, False, Arthur, (Trillian, choc))
    ord3 = Order(3, 'Magrathea', True, False, Millis, (choc,))

    Order.orders = (ord1, ord2, ord3)
    Order.notify_backordered(Order.orders, "backordered items")
    
    print('\nMark item as backordered')
    Order.orders = Order.mark_backordered(Order.orders, 3, 44)
    Order.notify_backordered(Order.orders, "backordered items")    
    assert(Order.orders[1].order_items[0].backordered)

    Order.orders = (ord1, ord2, ord3)

    # Option 1: For loop
    for oi in Order.get_order_details(Order.orders):
        if oi.orderid > 2: break
        print(f'{oi.customer}: {oi.item} at ${oi.total_price}')

    # Option 2: For loop using takewhile
    for oi in takewhile(lambda oi: oi.orderid < 3, Order.get_order_details(Order.orders)):
        print(f'{oi.customer}: {oi.item} at ${oi.total_price}')
 
    # Option 3: Print using iterable unpacking
    print(*map(lambda oi: f'{oi.customer}: {oi.item} at ${oi.total_price}\n',
            takewhile(lambda oi: oi.orderid < 3, Order.get_order_details(Order.orders))))
    
    # Option 4: Use consume with map, print and takewhile
    
    from collections import deque
    def consume(it):
        deque(it, maxlen=0)

    consume(map(lambda oi: print(f'{oi.customer}: {oi.item} at ${oi.total_price}'), 
        takewhile(lambda oi: oi.orderid < 3, Order.get_order_details(Order.orders))))

main()
