from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.personen_query_response import PersonenQueryResponse
from openapi_server.models.persoon import Persoon
from openapi_server import util

from openapi_server.models.personen_query_response import PersonenQueryResponse  # noqa: E501
from openapi_server.models.persoon import Persoon  # noqa: E501

class RaadpleegMetBurgerservicenummerResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, personen=None):  # noqa: E501
        """RaadpleegMetBurgerservicenummerResponse - a model defined in OpenAPI

        :param type: The type of this RaadpleegMetBurgerservicenummerResponse.  # noqa: E501
        :type type: str
        :param personen: The personen of this RaadpleegMetBurgerservicenummerResponse.  # noqa: E501
        :type personen: List[Persoon]
        """
        self.openapi_types = {
            'type': str,
            'personen': List[Persoon]
        }

        self.attribute_map = {
            'type': 'type',
            'personen': 'personen'
        }

        self._type = type
        self._personen = personen

    @classmethod
    def from_dict(cls, dikt) -> 'RaadpleegMetBurgerservicenummerResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The RaadpleegMetBurgerservicenummerResponse of this RaadpleegMetBurgerservicenummerResponse.  # noqa: E501
        :rtype: RaadpleegMetBurgerservicenummerResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this RaadpleegMetBurgerservicenummerResponse.


        :return: The type of this RaadpleegMetBurgerservicenummerResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this RaadpleegMetBurgerservicenummerResponse.


        :param type: The type of this RaadpleegMetBurgerservicenummerResponse.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def personen(self) -> List[Persoon]:
        """Gets the personen of this RaadpleegMetBurgerservicenummerResponse.

        * **geslacht** - wordt gevuld met waarden voor 'Geslacht' in 'tabelwaarden.csv'.   # noqa: E501

        :return: The personen of this RaadpleegMetBurgerservicenummerResponse.
        :rtype: List[Persoon]
        """
        return self._personen

    @personen.setter
    def personen(self, personen: List[Persoon]):
        """Sets the personen of this RaadpleegMetBurgerservicenummerResponse.

        * **geslacht** - wordt gevuld met waarden voor 'Geslacht' in 'tabelwaarden.csv'.   # noqa: E501

        :param personen: The personen of this RaadpleegMetBurgerservicenummerResponse.
        :type personen: List[Persoon]
        """

        self._personen = personen
