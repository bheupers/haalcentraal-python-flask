from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
import re
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501
import re  # noqa: E501

class JaarMaandDatum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, lang_formaat=None, jaar=None, maand=None):  # noqa: E501
        """JaarMaandDatum - a model defined in OpenAPI

        :param type: The type of this JaarMaandDatum.  # noqa: E501
        :type type: str
        :param lang_formaat: The lang_formaat of this JaarMaandDatum.  # noqa: E501
        :type lang_formaat: str
        :param jaar: The jaar of this JaarMaandDatum.  # noqa: E501
        :type jaar: int
        :param maand: The maand of this JaarMaandDatum.  # noqa: E501
        :type maand: int
        """
        self.openapi_types = {
            'type': str,
            'lang_formaat': str,
            'jaar': int,
            'maand': int
        }

        self.attribute_map = {
            'type': 'type',
            'lang_formaat': 'langFormaat',
            'jaar': 'jaar',
            'maand': 'maand'
        }

        self._type = type
        self._lang_formaat = lang_formaat
        self._jaar = jaar
        self._maand = maand

    @classmethod
    def from_dict(cls, dikt) -> 'JaarMaandDatum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The JaarMaandDatum of this JaarMaandDatum.  # noqa: E501
        :rtype: JaarMaandDatum
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this JaarMaandDatum.


        :return: The type of this JaarMaandDatum.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this JaarMaandDatum.


        :param type: The type of this JaarMaandDatum.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def lang_formaat(self) -> str:
        """Gets the lang_formaat of this JaarMaandDatum.


        :return: The lang_formaat of this JaarMaandDatum.
        :rtype: str
        """
        return self._lang_formaat

    @lang_formaat.setter
    def lang_formaat(self, lang_formaat: str):
        """Sets the lang_formaat of this JaarMaandDatum.


        :param lang_formaat: The lang_formaat of this JaarMaandDatum.
        :type lang_formaat: str
        """
        if lang_formaat is None:
            raise ValueError("Invalid value for `lang_formaat`, must not be `None`")  # noqa: E501
        if lang_formaat is not None and not re.search(r'^[a-z0-9 ]{1,17}$', lang_formaat):  # noqa: E501
            raise ValueError(r"Invalid value for `lang_formaat`, must be a follow pattern or equal to `/^[a-z0-9 ]{1,17}$/`")  # noqa: E501

        self._lang_formaat = lang_formaat

    @property
    def jaar(self) -> int:
        """Gets the jaar of this JaarMaandDatum.


        :return: The jaar of this JaarMaandDatum.
        :rtype: int
        """
        return self._jaar

    @jaar.setter
    def jaar(self, jaar: int):
        """Sets the jaar of this JaarMaandDatum.


        :param jaar: The jaar of this JaarMaandDatum.
        :type jaar: int
        """
        if jaar is None:
            raise ValueError("Invalid value for `jaar`, must not be `None`")  # noqa: E501
        if jaar is not None and jaar > 9999:  # noqa: E501
            raise ValueError("Invalid value for `jaar`, must be a value less than or equal to `9999`")  # noqa: E501
        if jaar is not None and jaar < 1:  # noqa: E501
            raise ValueError("Invalid value for `jaar`, must be a value greater than or equal to `1`")  # noqa: E501

        self._jaar = jaar

    @property
    def maand(self) -> int:
        """Gets the maand of this JaarMaandDatum.


        :return: The maand of this JaarMaandDatum.
        :rtype: int
        """
        return self._maand

    @maand.setter
    def maand(self, maand: int):
        """Sets the maand of this JaarMaandDatum.


        :param maand: The maand of this JaarMaandDatum.
        :type maand: int
        """
        if maand is None:
            raise ValueError("Invalid value for `maand`, must not be `None`")  # noqa: E501
        if maand is not None and maand > 12:  # noqa: E501
            raise ValueError("Invalid value for `maand`, must be a value less than or equal to `12`")  # noqa: E501
        if maand is not None and maand < 1:  # noqa: E501
            raise ValueError("Invalid value for `maand`, must be a value greater than or equal to `1`")  # noqa: E501

        self._maand = maand
