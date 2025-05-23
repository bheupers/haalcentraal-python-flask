from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_gezagsrelatie import AbstractGezagsrelatie
from openapi_server.models.meerderjarige import Meerderjarige
from openapi_server.models.minderjarige import Minderjarige
from openapi_server import util

from openapi_server.models.abstract_gezagsrelatie import AbstractGezagsrelatie  # noqa: E501
from openapi_server.models.meerderjarige import Meerderjarige  # noqa: E501
from openapi_server.models.minderjarige import Minderjarige  # noqa: E501

class Voogdij(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, derden=None, minderjarige=None):  # noqa: E501
        """Voogdij - a model defined in OpenAPI

        :param type: The type of this Voogdij.  # noqa: E501
        :type type: str
        :param derden: The derden of this Voogdij.  # noqa: E501
        :type derden: List[Meerderjarige]
        :param minderjarige: The minderjarige of this Voogdij.  # noqa: E501
        :type minderjarige: Minderjarige
        """
        self.openapi_types = {
            'type': str,
            'derden': List[Meerderjarige],
            'minderjarige': Minderjarige
        }

        self.attribute_map = {
            'type': 'type',
            'derden': 'derden',
            'minderjarige': 'minderjarige'
        }

        self._type = type
        self._derden = derden
        self._minderjarige = minderjarige

    @classmethod
    def from_dict(cls, dikt) -> 'Voogdij':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Voogdij of this Voogdij.  # noqa: E501
        :rtype: Voogdij
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this Voogdij.


        :return: The type of this Voogdij.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Voogdij.


        :param type: The type of this Voogdij.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def derden(self) -> List[Meerderjarige]:
        """Gets the derden of this Voogdij.


        :return: The derden of this Voogdij.
        :rtype: List[Meerderjarige]
        """
        return self._derden

    @derden.setter
    def derden(self, derden: List[Meerderjarige]):
        """Sets the derden of this Voogdij.


        :param derden: The derden of this Voogdij.
        :type derden: List[Meerderjarige]
        """
        if derden is not None and len(derden) > 2:
            raise ValueError("Invalid value for `derden`, number of items must be less than or equal to `2`")  # noqa: E501
        if derden is not None and len(derden) < 0:
            raise ValueError("Invalid value for `derden`, number of items must be greater than or equal to `0`")  # noqa: E501

        self._derden = derden

    @property
    def minderjarige(self) -> Minderjarige:
        """Gets the minderjarige of this Voogdij.


        :return: The minderjarige of this Voogdij.
        :rtype: Minderjarige
        """
        return self._minderjarige

    @minderjarige.setter
    def minderjarige(self, minderjarige: Minderjarige):
        """Sets the minderjarige of this Voogdij.


        :param minderjarige: The minderjarige of this Voogdij.
        :type minderjarige: Minderjarige
        """

        self._minderjarige = minderjarige
