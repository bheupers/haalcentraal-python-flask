from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
import re
from openapi_server import util

import re  # noqa: E501

class PersoonIndicatieGezagMinderjarige(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code=None, omschrijving=None):  # noqa: E501
        """PersoonIndicatieGezagMinderjarige - a model defined in OpenAPI

        :param code: The code of this PersoonIndicatieGezagMinderjarige.  # noqa: E501
        :type code: str
        :param omschrijving: The omschrijving of this PersoonIndicatieGezagMinderjarige.  # noqa: E501
        :type omschrijving: str
        """
        self.openapi_types = {
            'code': str,
            'omschrijving': str
        }

        self.attribute_map = {
            'code': 'code',
            'omschrijving': 'omschrijving'
        }

        self._code = code
        self._omschrijving = omschrijving

    @classmethod
    def from_dict(cls, dikt) -> 'PersoonIndicatieGezagMinderjarige':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Persoon_indicatieGezagMinderjarige of this PersoonIndicatieGezagMinderjarige.  # noqa: E501
        :rtype: PersoonIndicatieGezagMinderjarige
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this PersoonIndicatieGezagMinderjarige.


        :return: The code of this PersoonIndicatieGezagMinderjarige.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this PersoonIndicatieGezagMinderjarige.


        :param code: The code of this PersoonIndicatieGezagMinderjarige.
        :type code: str
        """
        if code is not None and not re.search(r'^[a-zA-Z0-9 \.]+$', code):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9 \.]+$/`")  # noqa: E501

        self._code = code

    @property
    def omschrijving(self) -> str:
        """Gets the omschrijving of this PersoonIndicatieGezagMinderjarige.


        :return: The omschrijving of this PersoonIndicatieGezagMinderjarige.
        :rtype: str
        """
        return self._omschrijving

    @omschrijving.setter
    def omschrijving(self, omschrijving: str):
        """Sets the omschrijving of this PersoonIndicatieGezagMinderjarige.


        :param omschrijving: The omschrijving of this PersoonIndicatieGezagMinderjarige.
        :type omschrijving: str
        """
        if omschrijving is not None and not re.search(r'^[a-zA-Z0-9À-ž \'\,\(\)\.\-]{1,200}$', omschrijving):  # noqa: E501
            raise ValueError(r"Invalid value for `omschrijving`, must be a follow pattern or equal to `/^[a-zA-Z0-9À-ž \'\,\(\)\.\-]{1,200}$/`")  # noqa: E501

        self._omschrijving = omschrijving
