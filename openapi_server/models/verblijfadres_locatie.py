from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.verblijfadres_locatie_in_onderzoek import VerblijfadresLocatieInOnderzoek
from openapi_server import util

from openapi_server.models.verblijfadres_locatie_in_onderzoek import VerblijfadresLocatieInOnderzoek  # noqa: E501

class VerblijfadresLocatie(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, locatiebeschrijving=None, in_onderzoek=None):  # noqa: E501
        """VerblijfadresLocatie - a model defined in OpenAPI

        :param locatiebeschrijving: The locatiebeschrijving of this VerblijfadresLocatie.  # noqa: E501
        :type locatiebeschrijving: str
        :param in_onderzoek: The in_onderzoek of this VerblijfadresLocatie.  # noqa: E501
        :type in_onderzoek: VerblijfadresLocatieInOnderzoek
        """
        self.openapi_types = {
            'locatiebeschrijving': str,
            'in_onderzoek': VerblijfadresLocatieInOnderzoek
        }

        self.attribute_map = {
            'locatiebeschrijving': 'locatiebeschrijving',
            'in_onderzoek': 'inOnderzoek'
        }

        self._locatiebeschrijving = locatiebeschrijving
        self._in_onderzoek = in_onderzoek

    @classmethod
    def from_dict(cls, dikt) -> 'VerblijfadresLocatie':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VerblijfadresLocatie of this VerblijfadresLocatie.  # noqa: E501
        :rtype: VerblijfadresLocatie
        """
        return util.deserialize_model(dikt, cls)

    @property
    def locatiebeschrijving(self) -> str:
        """Gets the locatiebeschrijving of this VerblijfadresLocatie.

        Omschrijving van de ligging van een verblijfsobject, standplaats of ligplaats.   # noqa: E501

        :return: The locatiebeschrijving of this VerblijfadresLocatie.
        :rtype: str
        """
        return self._locatiebeschrijving

    @locatiebeschrijving.setter
    def locatiebeschrijving(self, locatiebeschrijving: str):
        """Sets the locatiebeschrijving of this VerblijfadresLocatie.

        Omschrijving van de ligging van een verblijfsobject, standplaats of ligplaats.   # noqa: E501

        :param locatiebeschrijving: The locatiebeschrijving of this VerblijfadresLocatie.
        :type locatiebeschrijving: str
        """
        if locatiebeschrijving is not None and len(locatiebeschrijving) > 35:
            raise ValueError("Invalid value for `locatiebeschrijving`, length must be less than or equal to `35`")  # noqa: E501

        self._locatiebeschrijving = locatiebeschrijving

    @property
    def in_onderzoek(self) -> VerblijfadresLocatieInOnderzoek:
        """Gets the in_onderzoek of this VerblijfadresLocatie.


        :return: The in_onderzoek of this VerblijfadresLocatie.
        :rtype: VerblijfadresLocatieInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek: VerblijfadresLocatieInOnderzoek):
        """Sets the in_onderzoek of this VerblijfadresLocatie.


        :param in_onderzoek: The in_onderzoek of this VerblijfadresLocatie.
        :type in_onderzoek: VerblijfadresLocatieInOnderzoek
        """

        self._in_onderzoek = in_onderzoek
