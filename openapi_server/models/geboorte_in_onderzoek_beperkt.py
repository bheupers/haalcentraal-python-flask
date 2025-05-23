from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501

class GeboorteInOnderzoekBeperkt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datum_ingang_onderzoek=None, datum=None):  # noqa: E501
        """GeboorteInOnderzoekBeperkt - a model defined in OpenAPI

        :param datum_ingang_onderzoek: The datum_ingang_onderzoek of this GeboorteInOnderzoekBeperkt.  # noqa: E501
        :type datum_ingang_onderzoek: AbstractDatum
        :param datum: The datum of this GeboorteInOnderzoekBeperkt.  # noqa: E501
        :type datum: bool
        """
        self.openapi_types = {
            'datum_ingang_onderzoek': AbstractDatum,
            'datum': bool
        }

        self.attribute_map = {
            'datum_ingang_onderzoek': 'datumIngangOnderzoek',
            'datum': 'datum'
        }

        self._datum_ingang_onderzoek = datum_ingang_onderzoek
        self._datum = datum

    @classmethod
    def from_dict(cls, dikt) -> 'GeboorteInOnderzoekBeperkt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GeboorteInOnderzoekBeperkt of this GeboorteInOnderzoekBeperkt.  # noqa: E501
        :rtype: GeboorteInOnderzoekBeperkt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datum_ingang_onderzoek(self) -> AbstractDatum:
        """Gets the datum_ingang_onderzoek of this GeboorteInOnderzoekBeperkt.


        :return: The datum_ingang_onderzoek of this GeboorteInOnderzoekBeperkt.
        :rtype: AbstractDatum
        """
        return self._datum_ingang_onderzoek

    @datum_ingang_onderzoek.setter
    def datum_ingang_onderzoek(self, datum_ingang_onderzoek: AbstractDatum):
        """Sets the datum_ingang_onderzoek of this GeboorteInOnderzoekBeperkt.


        :param datum_ingang_onderzoek: The datum_ingang_onderzoek of this GeboorteInOnderzoekBeperkt.
        :type datum_ingang_onderzoek: AbstractDatum
        """

        self._datum_ingang_onderzoek = datum_ingang_onderzoek

    @property
    def datum(self) -> bool:
        """Gets the datum of this GeboorteInOnderzoekBeperkt.


        :return: The datum of this GeboorteInOnderzoekBeperkt.
        :rtype: bool
        """
        return self._datum

    @datum.setter
    def datum(self, datum: bool):
        """Sets the datum of this GeboorteInOnderzoekBeperkt.


        :param datum: The datum of this GeboorteInOnderzoekBeperkt.
        :type datum: bool
        """

        self._datum = datum
