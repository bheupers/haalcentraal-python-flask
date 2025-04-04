from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class AbstractGezagsrelatie(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None):  # noqa: E501
        """AbstractGezagsrelatie - a model defined in OpenAPI

        :param type: The type of this AbstractGezagsrelatie.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'type': str
        }

        self.attribute_map = {
            'type': 'type'
        }

        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'AbstractGezagsrelatie':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AbstractGezagsrelatie of this AbstractGezagsrelatie.  # noqa: E501
        :rtype: AbstractGezagsrelatie
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this AbstractGezagsrelatie.


        :return: The type of this AbstractGezagsrelatie.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this AbstractGezagsrelatie.


        :param type: The type of this AbstractGezagsrelatie.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type
