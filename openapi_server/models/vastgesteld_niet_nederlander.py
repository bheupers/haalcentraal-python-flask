from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server.models.abstract_nationaliteit import AbstractNationaliteit
from openapi_server.models.bijzonder_nederlanderschap_in_onderzoek import BijzonderNederlanderschapInOnderzoek
from openapi_server.models.waardetabel import Waardetabel
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501
from openapi_server.models.abstract_nationaliteit import AbstractNationaliteit  # noqa: E501
from openapi_server.models.bijzonder_nederlanderschap_in_onderzoek import BijzonderNederlanderschapInOnderzoek  # noqa: E501
from openapi_server.models.waardetabel import Waardetabel  # noqa: E501

class VastgesteldNietNederlander(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, reden_opname=None, datum_ingang_geldigheid=None, in_onderzoek=None):  # noqa: E501
        """VastgesteldNietNederlander - a model defined in OpenAPI

        :param type: The type of this VastgesteldNietNederlander.  # noqa: E501
        :type type: str
        :param reden_opname: The reden_opname of this VastgesteldNietNederlander.  # noqa: E501
        :type reden_opname: Waardetabel
        :param datum_ingang_geldigheid: The datum_ingang_geldigheid of this VastgesteldNietNederlander.  # noqa: E501
        :type datum_ingang_geldigheid: AbstractDatum
        :param in_onderzoek: The in_onderzoek of this VastgesteldNietNederlander.  # noqa: E501
        :type in_onderzoek: BijzonderNederlanderschapInOnderzoek
        """
        self.openapi_types = {
            'type': str,
            'reden_opname': Waardetabel,
            'datum_ingang_geldigheid': AbstractDatum,
            'in_onderzoek': BijzonderNederlanderschapInOnderzoek
        }

        self.attribute_map = {
            'type': 'type',
            'reden_opname': 'redenOpname',
            'datum_ingang_geldigheid': 'datumIngangGeldigheid',
            'in_onderzoek': 'inOnderzoek'
        }

        self._type = type
        self._reden_opname = reden_opname
        self._datum_ingang_geldigheid = datum_ingang_geldigheid
        self._in_onderzoek = in_onderzoek

    @classmethod
    def from_dict(cls, dikt) -> 'VastgesteldNietNederlander':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VastgesteldNietNederlander of this VastgesteldNietNederlander.  # noqa: E501
        :rtype: VastgesteldNietNederlander
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this VastgesteldNietNederlander.


        :return: The type of this VastgesteldNietNederlander.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this VastgesteldNietNederlander.


        :param type: The type of this VastgesteldNietNederlander.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def reden_opname(self) -> Waardetabel:
        """Gets the reden_opname of this VastgesteldNietNederlander.


        :return: The reden_opname of this VastgesteldNietNederlander.
        :rtype: Waardetabel
        """
        return self._reden_opname

    @reden_opname.setter
    def reden_opname(self, reden_opname: Waardetabel):
        """Sets the reden_opname of this VastgesteldNietNederlander.


        :param reden_opname: The reden_opname of this VastgesteldNietNederlander.
        :type reden_opname: Waardetabel
        """

        self._reden_opname = reden_opname

    @property
    def datum_ingang_geldigheid(self) -> AbstractDatum:
        """Gets the datum_ingang_geldigheid of this VastgesteldNietNederlander.


        :return: The datum_ingang_geldigheid of this VastgesteldNietNederlander.
        :rtype: AbstractDatum
        """
        return self._datum_ingang_geldigheid

    @datum_ingang_geldigheid.setter
    def datum_ingang_geldigheid(self, datum_ingang_geldigheid: AbstractDatum):
        """Sets the datum_ingang_geldigheid of this VastgesteldNietNederlander.


        :param datum_ingang_geldigheid: The datum_ingang_geldigheid of this VastgesteldNietNederlander.
        :type datum_ingang_geldigheid: AbstractDatum
        """

        self._datum_ingang_geldigheid = datum_ingang_geldigheid

    @property
    def in_onderzoek(self) -> BijzonderNederlanderschapInOnderzoek:
        """Gets the in_onderzoek of this VastgesteldNietNederlander.


        :return: The in_onderzoek of this VastgesteldNietNederlander.
        :rtype: BijzonderNederlanderschapInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek: BijzonderNederlanderschapInOnderzoek):
        """Sets the in_onderzoek of this VastgesteldNietNederlander.


        :param in_onderzoek: The in_onderzoek of this VastgesteldNietNederlander.
        :type in_onderzoek: BijzonderNederlanderschapInOnderzoek
        """

        self._in_onderzoek = in_onderzoek
