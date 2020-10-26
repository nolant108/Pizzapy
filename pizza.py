from pizzapi import *

customer = Customer('Nolan', 'Trapp', 'officialstackemup@gmail.com', '9513034347')
address = Address('HOUSE Addreess', 'City', 'State', 'ZIP')

store = address.closest_store()
menu = store.get_menu()

#menu.search(Name='Sprite')

order = Order(store, customer, address)
order.add_item('12SCREEN') # add a 12-inch cheese pizza
order.add_item('2LSPRITE') # add a 2-Liter Sprite

#order.Coupon('')

#card = PaymentObject('CARDNUM', 'EXP', 'SEC', 'ZIP')

#order.place(card)

print("Order Placed!")