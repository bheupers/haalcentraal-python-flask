from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.invalid_params import InvalidParams
import re
from openapi_server import util

from openapi_server.models.invalid_params import InvalidParams  # noqa: E501
import re  # noqa: E501

class BadRequestFoutbericht(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, title=None, status=None, detail=None, instance=None, code=None, invalid_params=None):  # noqa: E501
        """BadRequestFoutbericht - a model defined in OpenAPI

        :param type: The type of this BadRequestFoutbericht.  # noqa: E501
        :type type: str
        :param title: The title of this BadRequestFoutbericht.  # noqa: E501
        :type title: str
        :param status: The status of this BadRequestFoutbericht.  # noqa: E501
        :type status: int
        :param detail: The detail of this BadRequestFoutbericht.  # noqa: E501
        :type detail: str
        :param instance: The instance of this BadRequestFoutbericht.  # noqa: E501
        :type instance: str
        :param code: The code of this BadRequestFoutbericht.  # noqa: E501
        :type code: str
        :param invalid_params: The invalid_params of this BadRequestFoutbericht.  # noqa: E501
        :type invalid_params: List[InvalidParams]
        """
        self.openapi_types = {
            'type': str,
            'title': str,
            'status': int,
            'detail': str,
            'instance': str,
            'code': str,
            'invalid_params': List[InvalidParams]
        }

        self.attribute_map = {
            'type': 'type',
            'title': 'title',
            'status': 'status',
            'detail': 'detail',
            'instance': 'instance',
            'code': 'code',
            'invalid_params': 'invalidParams'
        }

        self._type = type
        self._title = title
        self._status = status
        self._detail = detail
        self._instance = instance
        self._code = code
        self._invalid_params = invalid_params

    @classmethod
    def from_dict(cls, dikt) -> 'BadRequestFoutbericht':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BadRequestFoutbericht of this BadRequestFoutbericht.  # noqa: E501
        :rtype: BadRequestFoutbericht
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this BadRequestFoutbericht.

        Link naar meer informatie over deze fout  # noqa: E501

        :return: The type of this BadRequestFoutbericht.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this BadRequestFoutbericht.

        Link naar meer informatie over deze fout  # noqa: E501

        :param type: The type of this BadRequestFoutbericht.
        :type type: str
        """

        self._type = type

    @property
    def title(self) -> str:
        """Gets the title of this BadRequestFoutbericht.

        Beschrijving van de fout  # noqa: E501

        :return: The title of this BadRequestFoutbericht.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this BadRequestFoutbericht.

        Beschrijving van de fout  # noqa: E501

        :param title: The title of this BadRequestFoutbericht.
        :type title: str
        """
        if title is not None and not re.search(r'^[a-zA-Z0-9À-ž \.\-]{1,80}$', title):  # noqa: E501
            raise ValueError(r"Invalid value for `title`, must be a follow pattern or equal to `/^[a-zA-Z0-9À-ž \.\-]{1,80}$/`")  # noqa: E501

        self._title = title

    @property
    def status(self) -> int:
        """Gets the status of this BadRequestFoutbericht.

        Http status code  # noqa: E501

        :return: The status of this BadRequestFoutbericht.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status: int):
        """Sets the status of this BadRequestFoutbericht.

        Http status code  # noqa: E501

        :param status: The status of this BadRequestFoutbericht.
        :type status: int
        """
        if status is not None and status > 600:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `600`")  # noqa: E501
        if status is not None and status < 100:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `100`")  # noqa: E501

        self._status = status

    @property
    def detail(self) -> str:
        """Gets the detail of this BadRequestFoutbericht.

        Details over de fout  # noqa: E501

        :return: The detail of this BadRequestFoutbericht.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail: str):
        """Sets the detail of this BadRequestFoutbericht.

        Details over de fout  # noqa: E501

        :param detail: The detail of this BadRequestFoutbericht.
        :type detail: str
        """
        if detail is not None and not re.search(r'^[a-zA-Z0-9À-ž \.\-\(\)\,]{1,200}$', detail):  # noqa: E501
            raise ValueError(r"Invalid value for `detail`, must be a follow pattern or equal to `/^[a-zA-Z0-9À-ž \.\-\(\)\,]{1,200}$/`")  # noqa: E501

        self._detail = detail

    @property
    def instance(self) -> str:
        """Gets the instance of this BadRequestFoutbericht.

        Uri van de aanroep die de fout heeft veroorzaakt  # noqa: E501

        :return: The instance of this BadRequestFoutbericht.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance: str):
        """Sets the instance of this BadRequestFoutbericht.

        Uri van de aanroep die de fout heeft veroorzaakt  # noqa: E501

        :param instance: The instance of this BadRequestFoutbericht.
        :type instance: str
        """

        self._instance = instance

    @property
    def code(self) -> str:
        """Gets the code of this BadRequestFoutbericht.

        Systeemcode die het type fout aangeeft  # noqa: E501

        :return: The code of this BadRequestFoutbericht.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this BadRequestFoutbericht.

        Systeemcode die het type fout aangeeft  # noqa: E501

        :param code: The code of this BadRequestFoutbericht.
        :type code: str
        """
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501
        if code is not None and not re.search(r'^[a-zA-Z0-9]{1,25}$', code):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z0-9]{1,25}$/`")  # noqa: E501

        self._code = code

    @property
    def invalid_params(self) -> List[InvalidParams]:
        """Gets the invalid_params of this BadRequestFoutbericht.

        Foutmelding per fout in een parameter. Alle gevonden fouten worden één keer teruggemeld.  # noqa: E501

        :return: The invalid_params of this BadRequestFoutbericht.
        :rtype: List[InvalidParams]
        """
        return self._invalid_params

    @invalid_params.setter
    def invalid_params(self, invalid_params: List[InvalidParams]):
        """Sets the invalid_params of this BadRequestFoutbericht.

        Foutmelding per fout in een parameter. Alle gevonden fouten worden één keer teruggemeld.  # noqa: E501

        :param invalid_params: The invalid_params of this BadRequestFoutbericht.
        :type invalid_params: List[InvalidParams]
        """

        self._invalid_params = invalid_params
