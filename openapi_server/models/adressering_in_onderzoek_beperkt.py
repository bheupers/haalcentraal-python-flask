from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501

class AdresseringInOnderzoekBeperkt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, adresregel1=None, adresregel2=None, adresregel3=None, land=None, datum_ingang_onderzoek_verblijfplaats=None):  # noqa: E501
        """AdresseringInOnderzoekBeperkt - a model defined in OpenAPI

        :param adresregel1: The adresregel1 of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :type adresregel1: bool
        :param adresregel2: The adresregel2 of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :type adresregel2: bool
        :param adresregel3: The adresregel3 of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :type adresregel3: bool
        :param land: The land of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :type land: bool
        :param datum_ingang_onderzoek_verblijfplaats: The datum_ingang_onderzoek_verblijfplaats of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :type datum_ingang_onderzoek_verblijfplaats: AbstractDatum
        """
        self.openapi_types = {
            'adresregel1': bool,
            'adresregel2': bool,
            'adresregel3': bool,
            'land': bool,
            'datum_ingang_onderzoek_verblijfplaats': AbstractDatum
        }

        self.attribute_map = {
            'adresregel1': 'adresregel1',
            'adresregel2': 'adresregel2',
            'adresregel3': 'adresregel3',
            'land': 'land',
            'datum_ingang_onderzoek_verblijfplaats': 'datumIngangOnderzoekVerblijfplaats'
        }

        self._adresregel1 = adresregel1
        self._adresregel2 = adresregel2
        self._adresregel3 = adresregel3
        self._land = land
        self._datum_ingang_onderzoek_verblijfplaats = datum_ingang_onderzoek_verblijfplaats

    @classmethod
    def from_dict(cls, dikt) -> 'AdresseringInOnderzoekBeperkt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AdresseringInOnderzoekBeperkt of this AdresseringInOnderzoekBeperkt.  # noqa: E501
        :rtype: AdresseringInOnderzoekBeperkt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def adresregel1(self) -> bool:
        """Gets the adresregel1 of this AdresseringInOnderzoekBeperkt.


        :return: The adresregel1 of this AdresseringInOnderzoekBeperkt.
        :rtype: bool
        """
        return self._adresregel1

    @adresregel1.setter
    def adresregel1(self, adresregel1: bool):
        """Sets the adresregel1 of this AdresseringInOnderzoekBeperkt.


        :param adresregel1: The adresregel1 of this AdresseringInOnderzoekBeperkt.
        :type adresregel1: bool
        """

        self._adresregel1 = adresregel1

    @property
    def adresregel2(self) -> bool:
        """Gets the adresregel2 of this AdresseringInOnderzoekBeperkt.


        :return: The adresregel2 of this AdresseringInOnderzoekBeperkt.
        :rtype: bool
        """
        return self._adresregel2

    @adresregel2.setter
    def adresregel2(self, adresregel2: bool):
        """Sets the adresregel2 of this AdresseringInOnderzoekBeperkt.


        :param adresregel2: The adresregel2 of this AdresseringInOnderzoekBeperkt.
        :type adresregel2: bool
        """

        self._adresregel2 = adresregel2

    @property
    def adresregel3(self) -> bool:
        """Gets the adresregel3 of this AdresseringInOnderzoekBeperkt.


        :return: The adresregel3 of this AdresseringInOnderzoekBeperkt.
        :rtype: bool
        """
        return self._adresregel3

    @adresregel3.setter
    def adresregel3(self, adresregel3: bool):
        """Sets the adresregel3 of this AdresseringInOnderzoekBeperkt.


        :param adresregel3: The adresregel3 of this AdresseringInOnderzoekBeperkt.
        :type adresregel3: bool
        """

        self._adresregel3 = adresregel3

    @property
    def land(self) -> bool:
        """Gets the land of this AdresseringInOnderzoekBeperkt.


        :return: The land of this AdresseringInOnderzoekBeperkt.
        :rtype: bool
        """
        return self._land

    @land.setter
    def land(self, land: bool):
        """Sets the land of this AdresseringInOnderzoekBeperkt.


        :param land: The land of this AdresseringInOnderzoekBeperkt.
        :type land: bool
        """

        self._land = land

    @property
    def datum_ingang_onderzoek_verblijfplaats(self) -> AbstractDatum:
        """Gets the datum_ingang_onderzoek_verblijfplaats of this AdresseringInOnderzoekBeperkt.


        :return: The datum_ingang_onderzoek_verblijfplaats of this AdresseringInOnderzoekBeperkt.
        :rtype: AbstractDatum
        """
        return self._datum_ingang_onderzoek_verblijfplaats

    @datum_ingang_onderzoek_verblijfplaats.setter
    def datum_ingang_onderzoek_verblijfplaats(self, datum_ingang_onderzoek_verblijfplaats: AbstractDatum):
        """Sets the datum_ingang_onderzoek_verblijfplaats of this AdresseringInOnderzoekBeperkt.


        :param datum_ingang_onderzoek_verblijfplaats: The datum_ingang_onderzoek_verblijfplaats of this AdresseringInOnderzoekBeperkt.
        :type datum_ingang_onderzoek_verblijfplaats: AbstractDatum
        """

        self._datum_ingang_onderzoek_verblijfplaats = datum_ingang_onderzoek_verblijfplaats
