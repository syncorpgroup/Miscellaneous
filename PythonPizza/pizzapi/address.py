from .store import Store
from .utils import request_json
from .urls import Urls, COUNTRY_PA

class Address(object):
    """Create an address, for finding stores and placing orders.

    The Address object describes a street address in North America (USA or
    Canada, for now). Callers can use the Address object's methods to find
    the closest or nearby stores from the API.

    Attributes:
        neighborhood (String): Latin America neighborhood. Example: 'Camino Real de Bethania'
        streetname (String): Name of street. Example: 'del Bosque'
        streetnumber (String): House number or Apartment number. Example: '556' or '54-B'
        deliveryinstructions (String): Details of Instruction to Delivery. Example: 'In front of supermarket 99, white House in corner'
        address_type (String): Options here are 'House', 'Apartment' or 'Other'. By default 'House' is selected
        building (String): if address_type is 'Apartment', fill this field with your builing name. Example 'Mystic Park'
        address_province (String): Code province in Panama. Default Panama ='PM'
            address_province options:
                'BO': Bocas del Toro
                'CH': Chiriqui
                'CC': Cocle
                'CO': Colon
                'HE': Herrera
                'LS': Los Santos
                'PM': Panama
                'PO': Panama Oeste
                'VR': Veraguas
        country (String): Country.
    """

    def __init__(self, neighborhood, streetname, streetnumber, deliveryinstructions, address_type='House', building='', address_province='PM', country=COUNTRY_PA, *args):

        self.neighborhood     = neighborhood
        self.streetname       = streetname
        self.streetnumber     = streetnumber
        self.deliveryinstructions = deliveryinstructions
        self.organizationName = address_province + ' - ' + building
        self.street           = streetname + ' ' + streetnumber
        self.address_type     = address_type
        self.address_province = address_province
        self.urls = Urls(country)
        self.country = country

    def nearby_stores(self, service='Delivery'):
        """Query the API to find nearby stores.

        nearby_stores will filter the information we receive from the API
        to exclude stores that are not currently online (!['IsOnlineNow']),
        and stores that are not currently in service (!['ServiceIsOpen']).

        In the original code used decorator line1 and line2. This code replace
        them with longitude and latitud requested in a additional information with
        self.location(X,Y)
        """
        data = request_json(self.urls.find_url(), latitude=self.latitude, longitude=self.longitude, type=service)
        return [Store(x, self.country) for x in data['Stores']
                if x['IsOnlineNow'] and x['ServiceIsOpen'][service]]

    def closest_store(self, service='Delivery'):
        stores = self.nearby_stores(service=service)
        if not stores:
            raise Exception('No local stores are currently open')
        return stores[0]

    def location(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
