from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501

class AangaanHuwelijkPartnerschapInOnderzoek(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datum_ingang_onderzoek=None, datum=None, land=None, plaats=None):  # noqa: E501
        """AangaanHuwelijkPartnerschapInOnderzoek - a model defined in OpenAPI

        :param datum_ingang_onderzoek: The datum_ingang_onderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.  # noqa: E501
        :type datum_ingang_onderzoek: AbstractDatum
        :param datum: The datum of this AangaanHuwelijkPartnerschapInOnderzoek.  # noqa: E501
        :type datum: bool
        :param land: The land of this AangaanHuwelijkPartnerschapInOnderzoek.  # noqa: E501
        :type land: bool
        :param plaats: The plaats of this AangaanHuwelijkPartnerschapInOnderzoek.  # noqa: E501
        :type plaats: bool
        """
        self.openapi_types = {
            'datum_ingang_onderzoek': AbstractDatum,
            'datum': bool,
            'land': bool,
            'plaats': bool
        }

        self.attribute_map = {
            'datum_ingang_onderzoek': 'datumIngangOnderzoek',
            'datum': 'datum',
            'land': 'land',
            'plaats': 'plaats'
        }

        self._datum_ingang_onderzoek = datum_ingang_onderzoek
        self._datum = datum
        self._land = land
        self._plaats = plaats

    @classmethod
    def from_dict(cls, dikt) -> 'AangaanHuwelijkPartnerschapInOnderzoek':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AangaanHuwelijkPartnerschapInOnderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.  # noqa: E501
        :rtype: AangaanHuwelijkPartnerschapInOnderzoek
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datum_ingang_onderzoek(self) -> AbstractDatum:
        """Gets the datum_ingang_onderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.


        :return: The datum_ingang_onderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.
        :rtype: AbstractDatum
        """
        return self._datum_ingang_onderzoek

    @datum_ingang_onderzoek.setter
    def datum_ingang_onderzoek(self, datum_ingang_onderzoek: AbstractDatum):
        """Sets the datum_ingang_onderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.


        :param datum_ingang_onderzoek: The datum_ingang_onderzoek of this AangaanHuwelijkPartnerschapInOnderzoek.
        :type datum_ingang_onderzoek: AbstractDatum
        """

        self._datum_ingang_onderzoek = datum_ingang_onderzoek

    @property
    def datum(self) -> bool:
        """Gets the datum of this AangaanHuwelijkPartnerschapInOnderzoek.


        :return: The datum of this AangaanHuwelijkPartnerschapInOnderzoek.
        :rtype: bool
        """
        return self._datum

    @datum.setter
    def datum(self, datum: bool):
        """Sets the datum of this AangaanHuwelijkPartnerschapInOnderzoek.


        :param datum: The datum of this AangaanHuwelijkPartnerschapInOnderzoek.
        :type datum: bool
        """

        self._datum = datum

    @property
    def land(self) -> bool:
        """Gets the land of this AangaanHuwelijkPartnerschapInOnderzoek.


        :return: The land of this AangaanHuwelijkPartnerschapInOnderzoek.
        :rtype: bool
        """
        return self._land

    @land.setter
    def land(self, land: bool):
        """Sets the land of this AangaanHuwelijkPartnerschapInOnderzoek.


        :param land: The land of this AangaanHuwelijkPartnerschapInOnderzoek.
        :type land: bool
        """

        self._land = land

    @property
    def plaats(self) -> bool:
        """Gets the plaats of this AangaanHuwelijkPartnerschapInOnderzoek.


        :return: The plaats of this AangaanHuwelijkPartnerschapInOnderzoek.
        :rtype: bool
        """
        return self._plaats

    @plaats.setter
    def plaats(self, plaats: bool):
        """Sets the plaats of this AangaanHuwelijkPartnerschapInOnderzoek.


        :param plaats: The plaats of this AangaanHuwelijkPartnerschapInOnderzoek.
        :type plaats: bool
        """

        self._plaats = plaats
