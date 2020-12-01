pizzapi - Panama
=======

Description
-----------
It's a port of `the pizzapi node.js module <https://github.com/RIAEvangelist/node-dominos-pizza-api>`_ written by `RIAEvangelist <https://github.com/RIAEvangelist>`_.

This code was based on Magicjarvis on https://github.com/Magicjarvis/pizzapi. It was modified to works in Country Panama.


This is a Python wrapper for the Dominos Pizza API to use it in Country Panama. If your Domino's Pizza store in your country use server order.golo01.dominos.com and GPS coordinate to locate you, this code might work for you.




Quick Start
-----------

Pull the module into your namespace:

.. code-block:: python

    from pizzapi import *

First, construct a ``Customer`` object and set the customer's address:

.. code-block:: python

    customer = Customer('Manuel Amador', 'Guerrero', 'maguerrero@presidencia.gob.pa', '+50766004433')
    address = Address('Brisas del Golf','del Bosque','300','Diagonal a Supermercado 99, calle sin salida, 3ra casa con verjas blancas')
    address.location(9.02308,-79.5289893)

Then, find a store that will be delivered to the address. Unlike original code, you need to pass coordinate.
Function closest_store() use coordinate to find your locate store.

.. code-block:: python

    store = address.closest_store()

You can see which store was assigned adding .__dict__ at the end. Example: if the variable is 'store', then:

.. code-block:: python

    store.__dict__

In order to add items to your order, you'll need the items product code.
To find the codes, get the menu from the store, then search for items you want to add.
You can do this by asking your ``Store`` object for its ``Menu``.
#TODO: print coupons from information requested.

.. code-block:: python

    menu = store.get_menu()

Then search ``menu`` with ``menu.search``. For example, running this command:

.. code-block:: python

    menu.search(Name='Coke')

Should print this to the console:

.. code-block:: text

    20BCOKE    20oz Bottle Coke®        $1.89
    20BDCOKE   20oz Bottle Diet Coke®   $1.89
    D20BZRO    20oz Bottle Coke Zero™   $1.89
    2LDCOKE    2-Liter Diet Coke®       $2.99
    2LCOKE     2-Liter Coke®            $2.99

Another example:

.. code-block:: python

    menu.search(Name='Panamena')

Should print this to the console:

.. code-block:: text

    _12MDPANAM  Pizza Masa Delgada Panamena Mediana $12.99
    _12SPANAME  Pizza estirada a mano Panamena Mediana $12.99
    12MPPP      Pan Pizza Panamena Mediana $12.99
    12OCPANAM   Orilla de Queso Panamena Mediana $12.99
    _14MDPANAM  Pizza Masa Delgada Panamena Familiar $14.99
    _14SPANAME  Pizza estirada a mano Panamena Familiar $14.99

After you've found your items' product codes, you can create an ``Order`` object add add your items:

.. code-block:: python

    order = Order(store, customer, address)
    order.add_coupon('4N1923')   # Coupon: 2 Large 1-5 topping pizzas + 2L soda for $23.99
    order.add_item('_14SPANAME') # Pizza#1
    order.add_item('14SCDELUX')  # Piiza#2
    order.add_item('2LCOKE')     # Coke 2 Litter

.. code-block:: python

    order = Order(store, customer, address)
    order.add_coupon('TARJC10')  # Coupon: Pizza Large 1 Topping + 1LT Soda
    order.add_item('14OCPIZZA')  # Cheese Pizza with border Cheese
    order.add_item('2LCOKE')     # Coke 2 Litter

You can remove items as well!

.. code-block:: python

    order.remove_item('2LCOKE')


Check how much is costing and the items added in the with ``.pay_with`` function.

.. code-block:: python

    order.pay_with()

And that's it! Now you can place your order. If no variable is passed to function order.place(),
the payment option is "cash".

.. code-block:: python

    order.place()


**Note:** Function for Credit card is not working for Visa because redirection to "Verified by Visa". Other credit card payments branches were not tested.

.. code-block:: python

    card = PaymentObject('4100123422343234', '0115', '777', '')
    order.pay_with(card)
    order.place(card)
