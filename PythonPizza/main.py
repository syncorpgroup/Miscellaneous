from pizzapi import *
import pprint

input("""Bienvenidos, esta es una prueba del código Pizzapi Panamá.

para ver el código, haga clic en el archivo main.py del menú de la izquierda.

Este código solo funciona en horarios 11:30 am - 7:00 pm GMT-5.

El cliente "Amador Amador Guerrero":
- email: mguerrero@gob.pa
- número: +507 6600-4433
- Barriada: Brisas del Golf
- Calle: Del Bosque
- Casa: 300
- Instrucciones de dirección: Diagonal a Supermercado 99, calle sin salida, 3ra casa con verjas blancas
- Ubicación por GPS: 9.02308, -79.5289893

Desea ordenar promo de 2 Pizza con 2 Litros de soda  ($23.99):
- Pizza Panameña
- Pizza Deluxe
- 2 Litros Soda Coca cola

Veamos el proceso paso a paso:

**Nota**: Por simplicidad, no se imprimirá todos los datos guardados.

[Presione Enter para continuar]

""")

# Guardando información
customer = Customer(
  'Manuel Amador',
  'Guerrero',
  'mguerrero@gob.pa',
  '+50766004433')
address = Address(
  'Brisas del Golf',
  'del Bosque',
  '300',
  'Diagonal a Supermercado 99, calle sin salida, 3ra casa con verjas blancas'
)
address.location(9.02308, -79.5289893)



input("""Guardando datos del usuario...
- Nombre: {nombre} {apellido}
- Email: {correo}
- GPS:
 - Longitud: {longitud}
 - Latitud: {latitud}

[Presione Enter para continuar]""".format(nombre=customer.first_name, apellido=customer.last_name, correo = customer.email, longitud = address.longitude, latitud= address.latitude))

print("Obteniendo ubicacion más cercana...")

store = address.closest_store()


input("""El local más cercano sería:
- Local: {local}
- Calle: {calle}
- Teléfono: {telefono}
- Dirección: {direccion}

[Presione Enter para continuar]""".format(local= store.data['StoreName'], calle= store.data['StreetName'], telefono = store.data['Phone'], direccion= store.data['AddressDescription']))

print("\nSolicitando el menú ...")

menu = store.get_menu()

print("\nMenu obtenido. Viendo opciones de Coca Cola y Pizzas:")
menu.search(Name='Coca')


print("\nOpciones de Pizzas Panameñas familiares:")
menu.search(Name='Panamena Familiar')

print("\nOpciones de Pizzas Deluxe familiares:")
menu.search(Name='Deluxe Familiar')

print("\nSe selecciona los siguientes: _14SPANAME, 14SCDELUX y 2LCOKE")

order = Order(store, customer, address)
order.add_item('_14SPANAME') # Pizza#1
order.add_item('14SCDELUX')  # Piiza#2
order.add_item('2LCOKE')     # Coke 2 Litter


input("Items guardados...[Presiona enter para continuar]")

print("Ver precio de la orden...")

pprint.pprint(order.pay_with())

input("Mmm... falta aplicar el cupón. Agreguemos el cupón 4N1923 para aplicar promoción. [Presione Enter]\n")

order.add_coupon('4N1923')   # Coupon: 2 Large 1-5 topping pizzas + 2L soda for $23.99

input("Cupón agregado. Veamos nuevamente la orden... [Presione Enter]")

pprint.pprint(order.pay_with())


print("Fin de Demo...")
