from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_gezagsrelatie import AbstractGezagsrelatie
from openapi_server.models.gezag_ouder import GezagOuder
from openapi_server.models.meerderjarige import Meerderjarige
from openapi_server.models.minderjarige import Minderjarige
from openapi_server import util

from openapi_server.models.abstract_gezagsrelatie import AbstractGezagsrelatie  # noqa: E501
from openapi_server.models.gezag_ouder import GezagOuder  # noqa: E501
from openapi_server.models.meerderjarige import Meerderjarige  # noqa: E501
from openapi_server.models.minderjarige import Minderjarige  # noqa: E501

class GezamenlijkGezag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, ouder=None, derde=None, minderjarige=None):  # noqa: E501
        """GezamenlijkGezag - a model defined in OpenAPI

        :param type: The type of this GezamenlijkGezag.  # noqa: E501
        :type type: str
        :param ouder: The ouder of this GezamenlijkGezag.  # noqa: E501
        :type ouder: GezagOuder
        :param derde: The derde of this GezamenlijkGezag.  # noqa: E501
        :type derde: Meerderjarige
        :param minderjarige: The minderjarige of this GezamenlijkGezag.  # noqa: E501
        :type minderjarige: Minderjarige
        """
        self.openapi_types = {
            'type': str,
            'ouder': GezagOuder,
            'derde': Meerderjarige,
            'minderjarige': Minderjarige
        }

        self.attribute_map = {
            'type': 'type',
            'ouder': 'ouder',
            'derde': 'derde',
            'minderjarige': 'minderjarige'
        }

        self._type = type
        self._ouder = ouder
        self._derde = derde
        self._minderjarige = minderjarige

    @classmethod
    def from_dict(cls, dikt) -> 'GezamenlijkGezag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GezamenlijkGezag of this GezamenlijkGezag.  # noqa: E501
        :rtype: GezamenlijkGezag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this GezamenlijkGezag.


        :return: The type of this GezamenlijkGezag.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this GezamenlijkGezag.


        :param type: The type of this GezamenlijkGezag.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def ouder(self) -> GezagOuder:
        """Gets the ouder of this GezamenlijkGezag.


        :return: The ouder of this GezamenlijkGezag.
        :rtype: GezagOuder
        """
        return self._ouder

    @ouder.setter
    def ouder(self, ouder: GezagOuder):
        """Sets the ouder of this GezamenlijkGezag.


        :param ouder: The ouder of this GezamenlijkGezag.
        :type ouder: GezagOuder
        """

        self._ouder = ouder

    @property
    def derde(self) -> Meerderjarige:
        """Gets the derde of this GezamenlijkGezag.


        :return: The derde of this GezamenlijkGezag.
        :rtype: Meerderjarige
        """
        return self._derde

    @derde.setter
    def derde(self, derde: Meerderjarige):
        """Sets the derde of this GezamenlijkGezag.


        :param derde: The derde of this GezamenlijkGezag.
        :type derde: Meerderjarige
        """

        self._derde = derde

    @property
    def minderjarige(self) -> Minderjarige:
        """Gets the minderjarige of this GezamenlijkGezag.


        :return: The minderjarige of this GezamenlijkGezag.
        :rtype: Minderjarige
        """
        return self._minderjarige

    @minderjarige.setter
    def minderjarige(self, minderjarige: Minderjarige):
        """Sets the minderjarige of this GezamenlijkGezag.


        :param minderjarige: The minderjarige of this GezamenlijkGezag.
        :type minderjarige: Minderjarige
        """

        self._minderjarige = minderjarige
