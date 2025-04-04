from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.personen_query_response import PersonenQueryResponse
from openapi_server.models.persoon_beperkt import PersoonBeperkt
from openapi_server import util

from openapi_server.models.personen_query_response import PersonenQueryResponse  # noqa: E501
from openapi_server.models.persoon_beperkt import PersoonBeperkt  # noqa: E501

class ZoekMetPostcodeEnHuisnummerResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, personen=None):  # noqa: E501
        """ZoekMetPostcodeEnHuisnummerResponse - a model defined in OpenAPI

        :param type: The type of this ZoekMetPostcodeEnHuisnummerResponse.  # noqa: E501
        :type type: str
        :param personen: The personen of this ZoekMetPostcodeEnHuisnummerResponse.  # noqa: E501
        :type personen: List[PersoonBeperkt]
        """
        self.openapi_types = {
            'type': str,
            'personen': List[PersoonBeperkt]
        }

        self.attribute_map = {
            'type': 'type',
            'personen': 'personen'
        }

        self._type = type
        self._personen = personen

    @classmethod
    def from_dict(cls, dikt) -> 'ZoekMetPostcodeEnHuisnummerResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ZoekMetPostcodeEnHuisnummerResponse of this ZoekMetPostcodeEnHuisnummerResponse.  # noqa: E501
        :rtype: ZoekMetPostcodeEnHuisnummerResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ZoekMetPostcodeEnHuisnummerResponse.


        :return: The type of this ZoekMetPostcodeEnHuisnummerResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ZoekMetPostcodeEnHuisnummerResponse.


        :param type: The type of this ZoekMetPostcodeEnHuisnummerResponse.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def personen(self) -> List[PersoonBeperkt]:
        """Gets the personen of this ZoekMetPostcodeEnHuisnummerResponse.

        * **geslacht** - wordt gevuld met waarden voor 'Geslacht' in 'tabelwaarden.csv'.   # noqa: E501

        :return: The personen of this ZoekMetPostcodeEnHuisnummerResponse.
        :rtype: List[PersoonBeperkt]
        """
        return self._personen

    @personen.setter
    def personen(self, personen: List[PersoonBeperkt]):
        """Sets the personen of this ZoekMetPostcodeEnHuisnummerResponse.

        * **geslacht** - wordt gevuld met waarden voor 'Geslacht' in 'tabelwaarden.csv'.   # noqa: E501

        :param personen: The personen of this ZoekMetPostcodeEnHuisnummerResponse.
        :type personen: List[PersoonBeperkt]
        """

        self._personen = personen
