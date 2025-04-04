from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server.models.ontbinding_huwelijk_partnerschap_in_onderzoek import OntbindingHuwelijkPartnerschapInOnderzoek
from openapi_server import util

from openapi_server.models.abstract_datum import AbstractDatum  # noqa: E501
from openapi_server.models.ontbinding_huwelijk_partnerschap_in_onderzoek import OntbindingHuwelijkPartnerschapInOnderzoek  # noqa: E501

class OntbindingHuwelijkPartnerschap(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, datum=None, in_onderzoek=None):  # noqa: E501
        """OntbindingHuwelijkPartnerschap - a model defined in OpenAPI

        :param datum: The datum of this OntbindingHuwelijkPartnerschap.  # noqa: E501
        :type datum: AbstractDatum
        :param in_onderzoek: The in_onderzoek of this OntbindingHuwelijkPartnerschap.  # noqa: E501
        :type in_onderzoek: OntbindingHuwelijkPartnerschapInOnderzoek
        """
        self.openapi_types = {
            'datum': AbstractDatum,
            'in_onderzoek': OntbindingHuwelijkPartnerschapInOnderzoek
        }

        self.attribute_map = {
            'datum': 'datum',
            'in_onderzoek': 'inOnderzoek'
        }

        self._datum = datum
        self._in_onderzoek = in_onderzoek

    @classmethod
    def from_dict(cls, dikt) -> 'OntbindingHuwelijkPartnerschap':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OntbindingHuwelijkPartnerschap of this OntbindingHuwelijkPartnerschap.  # noqa: E501
        :rtype: OntbindingHuwelijkPartnerschap
        """
        return util.deserialize_model(dikt, cls)

    @property
    def datum(self) -> AbstractDatum:
        """Gets the datum of this OntbindingHuwelijkPartnerschap.


        :return: The datum of this OntbindingHuwelijkPartnerschap.
        :rtype: AbstractDatum
        """
        return self._datum

    @datum.setter
    def datum(self, datum: AbstractDatum):
        """Sets the datum of this OntbindingHuwelijkPartnerschap.


        :param datum: The datum of this OntbindingHuwelijkPartnerschap.
        :type datum: AbstractDatum
        """

        self._datum = datum

    @property
    def in_onderzoek(self) -> OntbindingHuwelijkPartnerschapInOnderzoek:
        """Gets the in_onderzoek of this OntbindingHuwelijkPartnerschap.


        :return: The in_onderzoek of this OntbindingHuwelijkPartnerschap.
        :rtype: OntbindingHuwelijkPartnerschapInOnderzoek
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek: OntbindingHuwelijkPartnerschapInOnderzoek):
        """Sets the in_onderzoek of this OntbindingHuwelijkPartnerschap.


        :param in_onderzoek: The in_onderzoek of this OntbindingHuwelijkPartnerschap.
        :type in_onderzoek: OntbindingHuwelijkPartnerschapInOnderzoek
        """

        self._in_onderzoek = in_onderzoek
