import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from openapi_server.models.foutbericht import Foutbericht  # noqa: E501
from openapi_server.models.personen_query import PersonenQuery  # noqa: E501
from openapi_server.models.personen_query_response import PersonenQueryResponse  # noqa: E501
from openapi_server import util


def personen(body=None):  # noqa: E501
    """Zoek personen

    Zoek personen met één van de onderstaande verplichte combinaties van parameters en vul ze evt. aan met optionele parameters.  1.  Raadpleeg met burgerservicenummer 2.  Zoek met geslachtsnaam en geboortedatum 3.  Zoek met geslachtsnaam, voornamen en gemeente van inschrijving 4.  Zoek met postcode en huisnummer 5.  Zoek met straat, huisnummer en gemeente van inschrijving 6.  Zoek met nummeraanduiding identificatie 7.  Zoek met adresseerbaarobject identificatie  Default krijg je personen terug die nog in leven zijn, tenzij je de inclusiefoverledenpersonen&#x3D;true opgeeft.  Gebruik de fields parameter om alleen die gegevens op te vragen die je nodig hebt en waarvoor je geautoriseerd bent.  # noqa: E501

    :param personen_query: 
    :type personen_query: dict | bytes

    :rtype: Union[PersonenQueryResponse, Tuple[PersonenQueryResponse, int], Tuple[PersonenQueryResponse, int, Dict[str, str]]
    """
    personen_query = body
    if connexion.request.is_json:
        personen_query = PersonenQuery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
