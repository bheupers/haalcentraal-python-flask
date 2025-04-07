
import re
import connexion
from pathlib import Path
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from openapi_server.models.foutbericht import Foutbericht  # noqa: E501
from openapi_server.models.invalid_params import InvalidParams
from openapi_server.models.personen_query import PersonenQuery  # noqa: E501
from openapi_server.models.personen_query_response import PersonenQueryResponse  # noqa: E501
from openapi_server import util

from openapi_server.data.data_controller import DataController
from openapi_server.models.persoon import Persoon
from openapi_server.models.raadpleeg_met_burgerservicenummer import RaadpleegMetBurgerservicenummer
from openapi_server.models.raadpleeg_met_burgerservicenummer_response import RaadpleegMetBurgerservicenummerResponse


all_data = DataController(Path.cwd() / "test-data.json")

def personen(body=None):  # noqa: E501
    """Zoek personen

    Zoek personen met één van de onderstaande verplichte combinaties van parameters en vul ze evt. aan met optionele parameters.  
    1.  Raadpleeg met burgerservicenummer 
    2.  Zoek met geslachtsnaam en geboortedatum 
    3.  Zoek met geslachtsnaam, voornamen en gemeente van inschrijving 
    4.  Zoek met postcode en huisnummer 
    5.  Zoek met straat, huisnummer en gemeente van inschrijving 
    6.  Zoek met nummeraanduiding identificatie 
    7.  Zoek met adresseerbaarobject identificatie 
    Default krijg je personen terug die nog in leven zijn, tenzij je de inclusiefoverledenpersonen&#x3D;true opgeeft.  
    Gebruik de fields parameter om alleen die gegevens op te vragen die je nodig hebt en waarvoor je geautoriseerd bent.  # noqa: E501

    :param personen_query: 
    :type personen_query: dict | bytes

    :rtype: Union[PersonenQueryResponse, Tuple[PersonenQueryResponse, int], Tuple[PersonenQueryResponse, int, Dict[str, str]]
    """
    personen_query = body
    if connexion.request.is_json:
        request_json = connexion.request.get_json()
        type =  request_json["type"]
        match type:
            case "RaadpleegMetBurgerservicenummer":
                query = None
                invalid_params = []
                try:
                    query = RaadpleegMetBurgerservicenummer(**request_json)
                except TypeError as te:
                    if m := re.search(r"got an unexpected keyword argument '(\w+)'", repr(te)):
                        invalid_params.append(InvalidParams(name=m.group(1), code="unknownParam", reason="Parameter is niet verwacht."))
                    
                if "burgerservicenummer" not in request_json:
                    # {"invalidParams":[{"name":"burgerservicenumme","code":"unknownParam","reason":"Parameter is niet verwacht."},
                    # {"name":"burgerservicenummer","code":"required","reason":"Parameter is verplicht."}],
                    invalid_params.append(InvalidParams(name="burgerservicenummer", code="required", reason="Parameter is verplicht." ))
                    # "type":"https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.1"
                    # "title":"Een of meerdere parameters zijn niet correct.","status":400,
                    # "detail":"De foutieve parameter(s) zijn: burgerservicenumme, burgerservicenummer.","instance":"/haalcentraal/api/brp/personen","code":"paramsValidation"}
                
                if invalid_params:
                    response = BadRequestFoutbericht(type="https://datatracker.ietf.org/doc/html/rfc7231#section-6.5.1",
                                                     title="Een of meerdere parameters zijn niet correct.", 
                                                     status=400, 
                                                     detail="De foutieve parameter(s) zijn: burgerservicenumme, burgerservicenummer.",
                                                     instance= "/haalcentraal/api/brp/personen",
                                                     code="paramsValidation",
                                                     invalid_params=[invalid_params]
                                                     )
                    return response
                fields = request_json.pop("fields")
                results = all_data.search({"burgerservicenummer": query.burgerservicenummer[0]})
                results = [{f: result[f] for f in fields} for result in results]
                personen = [Persoon.from_dict(result) for result in results]
                response = RaadpleegMetBurgerservicenummerResponse(type, personen)
                return response
            case _:
                personen_query = PersonenQuery.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!' 

