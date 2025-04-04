from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.adressering_beperkt import AdresseringBeperkt
from openapi_server.models.geboorte_beperkt import GeboorteBeperkt
from openapi_server.models.naam_persoon_beperkt import NaamPersoonBeperkt
from openapi_server.models.opschorting_bijhouding import OpschortingBijhouding
from openapi_server.models.persoon_in_onderzoek_beperkt import PersoonInOnderzoekBeperkt
from openapi_server.models.rni_deelnemer import RniDeelnemer
from openapi_server.models.verificatie import Verificatie
from openapi_server.models.waardetabel import Waardetabel
import re
from openapi_server import util

from openapi_server.models.adressering_beperkt import AdresseringBeperkt  # noqa: E501
from openapi_server.models.geboorte_beperkt import GeboorteBeperkt  # noqa: E501
from openapi_server.models.naam_persoon_beperkt import NaamPersoonBeperkt  # noqa: E501
from openapi_server.models.opschorting_bijhouding import OpschortingBijhouding  # noqa: E501
from openapi_server.models.persoon_in_onderzoek_beperkt import PersoonInOnderzoekBeperkt  # noqa: E501
from openapi_server.models.rni_deelnemer import RniDeelnemer  # noqa: E501
from openapi_server.models.verificatie import Verificatie  # noqa: E501
from openapi_server.models.waardetabel import Waardetabel  # noqa: E501
import re  # noqa: E501

class PersoonBeperkt(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, burgerservicenummer=None, geboorte=None, geheimhouding_persoonsgegevens=None, geslacht=None, in_onderzoek=None, leeftijd=None, naam=None, opschorting_bijhouding=None, adressering=None, rni=None, verificatie=None):  # noqa: E501
        """PersoonBeperkt - a model defined in OpenAPI

        :param burgerservicenummer: The burgerservicenummer of this PersoonBeperkt.  # noqa: E501
        :type burgerservicenummer: str
        :param geboorte: The geboorte of this PersoonBeperkt.  # noqa: E501
        :type geboorte: GeboorteBeperkt
        :param geheimhouding_persoonsgegevens: The geheimhouding_persoonsgegevens of this PersoonBeperkt.  # noqa: E501
        :type geheimhouding_persoonsgegevens: bool
        :param geslacht: The geslacht of this PersoonBeperkt.  # noqa: E501
        :type geslacht: Waardetabel
        :param in_onderzoek: The in_onderzoek of this PersoonBeperkt.  # noqa: E501
        :type in_onderzoek: PersoonInOnderzoekBeperkt
        :param leeftijd: The leeftijd of this PersoonBeperkt.  # noqa: E501
        :type leeftijd: int
        :param naam: The naam of this PersoonBeperkt.  # noqa: E501
        :type naam: NaamPersoonBeperkt
        :param opschorting_bijhouding: The opschorting_bijhouding of this PersoonBeperkt.  # noqa: E501
        :type opschorting_bijhouding: OpschortingBijhouding
        :param adressering: The adressering of this PersoonBeperkt.  # noqa: E501
        :type adressering: AdresseringBeperkt
        :param rni: The rni of this PersoonBeperkt.  # noqa: E501
        :type rni: List[RniDeelnemer]
        :param verificatie: The verificatie of this PersoonBeperkt.  # noqa: E501
        :type verificatie: Verificatie
        """
        self.openapi_types = {
            'burgerservicenummer': str,
            'geboorte': GeboorteBeperkt,
            'geheimhouding_persoonsgegevens': bool,
            'geslacht': Waardetabel,
            'in_onderzoek': PersoonInOnderzoekBeperkt,
            'leeftijd': int,
            'naam': NaamPersoonBeperkt,
            'opschorting_bijhouding': OpschortingBijhouding,
            'adressering': AdresseringBeperkt,
            'rni': List[RniDeelnemer],
            'verificatie': Verificatie
        }

        self.attribute_map = {
            'burgerservicenummer': 'burgerservicenummer',
            'geboorte': 'geboorte',
            'geheimhouding_persoonsgegevens': 'geheimhoudingPersoonsgegevens',
            'geslacht': 'geslacht',
            'in_onderzoek': 'inOnderzoek',
            'leeftijd': 'leeftijd',
            'naam': 'naam',
            'opschorting_bijhouding': 'opschortingBijhouding',
            'adressering': 'adressering',
            'rni': 'rni',
            'verificatie': 'verificatie'
        }

        self._burgerservicenummer = burgerservicenummer
        self._geboorte = geboorte
        self._geheimhouding_persoonsgegevens = geheimhouding_persoonsgegevens
        self._geslacht = geslacht
        self._in_onderzoek = in_onderzoek
        self._leeftijd = leeftijd
        self._naam = naam
        self._opschorting_bijhouding = opschorting_bijhouding
        self._adressering = adressering
        self._rni = rni
        self._verificatie = verificatie

    @classmethod
    def from_dict(cls, dikt) -> 'PersoonBeperkt':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PersoonBeperkt of this PersoonBeperkt.  # noqa: E501
        :rtype: PersoonBeperkt
        """
        return util.deserialize_model(dikt, cls)

    @property
    def burgerservicenummer(self) -> str:
        """Gets the burgerservicenummer of this PersoonBeperkt.


        :return: The burgerservicenummer of this PersoonBeperkt.
        :rtype: str
        """
        return self._burgerservicenummer

    @burgerservicenummer.setter
    def burgerservicenummer(self, burgerservicenummer: str):
        """Sets the burgerservicenummer of this PersoonBeperkt.


        :param burgerservicenummer: The burgerservicenummer of this PersoonBeperkt.
        :type burgerservicenummer: str
        """
        if burgerservicenummer is not None and not re.search(r'^[0-9]{9}$', burgerservicenummer):  # noqa: E501
            raise ValueError(r"Invalid value for `burgerservicenummer`, must be a follow pattern or equal to `/^[0-9]{9}$/`")  # noqa: E501

        self._burgerservicenummer = burgerservicenummer

    @property
    def geboorte(self) -> GeboorteBeperkt:
        """Gets the geboorte of this PersoonBeperkt.


        :return: The geboorte of this PersoonBeperkt.
        :rtype: GeboorteBeperkt
        """
        return self._geboorte

    @geboorte.setter
    def geboorte(self, geboorte: GeboorteBeperkt):
        """Sets the geboorte of this PersoonBeperkt.


        :param geboorte: The geboorte of this PersoonBeperkt.
        :type geboorte: GeboorteBeperkt
        """

        self._geboorte = geboorte

    @property
    def geheimhouding_persoonsgegevens(self) -> bool:
        """Gets the geheimhouding_persoonsgegevens of this PersoonBeperkt.

        Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen.   # noqa: E501

        :return: The geheimhouding_persoonsgegevens of this PersoonBeperkt.
        :rtype: bool
        """
        return self._geheimhouding_persoonsgegevens

    @geheimhouding_persoonsgegevens.setter
    def geheimhouding_persoonsgegevens(self, geheimhouding_persoonsgegevens: bool):
        """Sets the geheimhouding_persoonsgegevens of this PersoonBeperkt.

        Gegevens mogen niet worden verstrekt aan derden / maatschappelijke instellingen.   # noqa: E501

        :param geheimhouding_persoonsgegevens: The geheimhouding_persoonsgegevens of this PersoonBeperkt.
        :type geheimhouding_persoonsgegevens: bool
        """

        self._geheimhouding_persoonsgegevens = geheimhouding_persoonsgegevens

    @property
    def geslacht(self) -> Waardetabel:
        """Gets the geslacht of this PersoonBeperkt.


        :return: The geslacht of this PersoonBeperkt.
        :rtype: Waardetabel
        """
        return self._geslacht

    @geslacht.setter
    def geslacht(self, geslacht: Waardetabel):
        """Sets the geslacht of this PersoonBeperkt.


        :param geslacht: The geslacht of this PersoonBeperkt.
        :type geslacht: Waardetabel
        """

        self._geslacht = geslacht

    @property
    def in_onderzoek(self) -> PersoonInOnderzoekBeperkt:
        """Gets the in_onderzoek of this PersoonBeperkt.


        :return: The in_onderzoek of this PersoonBeperkt.
        :rtype: PersoonInOnderzoekBeperkt
        """
        return self._in_onderzoek

    @in_onderzoek.setter
    def in_onderzoek(self, in_onderzoek: PersoonInOnderzoekBeperkt):
        """Sets the in_onderzoek of this PersoonBeperkt.


        :param in_onderzoek: The in_onderzoek of this PersoonBeperkt.
        :type in_onderzoek: PersoonInOnderzoekBeperkt
        """

        self._in_onderzoek = in_onderzoek

    @property
    def leeftijd(self) -> int:
        """Gets the leeftijd of this PersoonBeperkt.

        Leeftijd in jaren op het moment van bevragen.   # noqa: E501

        :return: The leeftijd of this PersoonBeperkt.
        :rtype: int
        """
        return self._leeftijd

    @leeftijd.setter
    def leeftijd(self, leeftijd: int):
        """Sets the leeftijd of this PersoonBeperkt.

        Leeftijd in jaren op het moment van bevragen.   # noqa: E501

        :param leeftijd: The leeftijd of this PersoonBeperkt.
        :type leeftijd: int
        """
        if leeftijd is not None and leeftijd > 150:  # noqa: E501
            raise ValueError("Invalid value for `leeftijd`, must be a value less than or equal to `150`")  # noqa: E501
        if leeftijd is not None and leeftijd < 0:  # noqa: E501
            raise ValueError("Invalid value for `leeftijd`, must be a value greater than or equal to `0`")  # noqa: E501

        self._leeftijd = leeftijd

    @property
    def naam(self) -> NaamPersoonBeperkt:
        """Gets the naam of this PersoonBeperkt.


        :return: The naam of this PersoonBeperkt.
        :rtype: NaamPersoonBeperkt
        """
        return self._naam

    @naam.setter
    def naam(self, naam: NaamPersoonBeperkt):
        """Sets the naam of this PersoonBeperkt.


        :param naam: The naam of this PersoonBeperkt.
        :type naam: NaamPersoonBeperkt
        """

        self._naam = naam

    @property
    def opschorting_bijhouding(self) -> OpschortingBijhouding:
        """Gets the opschorting_bijhouding of this PersoonBeperkt.


        :return: The opschorting_bijhouding of this PersoonBeperkt.
        :rtype: OpschortingBijhouding
        """
        return self._opschorting_bijhouding

    @opschorting_bijhouding.setter
    def opschorting_bijhouding(self, opschorting_bijhouding: OpschortingBijhouding):
        """Sets the opschorting_bijhouding of this PersoonBeperkt.


        :param opschorting_bijhouding: The opschorting_bijhouding of this PersoonBeperkt.
        :type opschorting_bijhouding: OpschortingBijhouding
        """

        self._opschorting_bijhouding = opschorting_bijhouding

    @property
    def adressering(self) -> AdresseringBeperkt:
        """Gets the adressering of this PersoonBeperkt.


        :return: The adressering of this PersoonBeperkt.
        :rtype: AdresseringBeperkt
        """
        return self._adressering

    @adressering.setter
    def adressering(self, adressering: AdresseringBeperkt):
        """Sets the adressering of this PersoonBeperkt.


        :param adressering: The adressering of this PersoonBeperkt.
        :type adressering: AdresseringBeperkt
        """

        self._adressering = adressering

    @property
    def rni(self) -> List[RniDeelnemer]:
        """Gets the rni of this PersoonBeperkt.


        :return: The rni of this PersoonBeperkt.
        :rtype: List[RniDeelnemer]
        """
        return self._rni

    @rni.setter
    def rni(self, rni: List[RniDeelnemer]):
        """Sets the rni of this PersoonBeperkt.


        :param rni: The rni of this PersoonBeperkt.
        :type rni: List[RniDeelnemer]
        """

        self._rni = rni

    @property
    def verificatie(self) -> Verificatie:
        """Gets the verificatie of this PersoonBeperkt.


        :return: The verificatie of this PersoonBeperkt.
        :rtype: Verificatie
        """
        return self._verificatie

    @verificatie.setter
    def verificatie(self, verificatie: Verificatie):
        """Sets the verificatie of this PersoonBeperkt.


        :param verificatie: The verificatie of this PersoonBeperkt.
        :type verificatie: Verificatie
        """

        self._verificatie = verificatie
