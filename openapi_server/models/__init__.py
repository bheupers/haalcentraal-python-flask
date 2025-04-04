# flake8: noqa
# import models into model package
from openapi_server.models.aangaan_huwelijk_partnerschap import AangaanHuwelijkPartnerschap
from openapi_server.models.aangaan_huwelijk_partnerschap_in_onderzoek import AangaanHuwelijkPartnerschapInOnderzoek
from openapi_server.models.aanschrijfwijze import Aanschrijfwijze
from openapi_server.models.abstract_datum import AbstractDatum
from openapi_server.models.abstract_gezagsrelatie import AbstractGezagsrelatie
from openapi_server.models.abstract_nationaliteit import AbstractNationaliteit
from openapi_server.models.abstract_verblijfplaats import AbstractVerblijfplaats
from openapi_server.models.adellijke_titel_predicaat_soort import AdellijkeTitelPredicaatSoort
from openapi_server.models.adellijke_titel_predicaat_type import AdellijkeTitelPredicaatType
from openapi_server.models.adres import Adres
from openapi_server.models.adres_all_of_datum_ingang_geldigheid import AdresAllOfDatumIngangGeldigheid
from openapi_server.models.adres_in_onderzoek import AdresInOnderzoek
from openapi_server.models.adressering import Adressering
from openapi_server.models.adressering_basis import AdresseringBasis
from openapi_server.models.adressering_beperkt import AdresseringBeperkt
from openapi_server.models.adressering_in_onderzoek import AdresseringInOnderzoek
from openapi_server.models.adressering_in_onderzoek_beperkt import AdresseringInOnderzoekBeperkt
from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht
from openapi_server.models.behandeld_als_nederlander import BehandeldAlsNederlander
from openapi_server.models.bijzonder_nederlanderschap_in_onderzoek import BijzonderNederlanderschapInOnderzoek
from openapi_server.models.datum_onbekend import DatumOnbekend
from openapi_server.models.eenhoofdig_ouderlijk_gezag import EenhoofdigOuderlijkGezag
from openapi_server.models.europees_kiesrecht import EuropeesKiesrecht
from openapi_server.models.foutbericht import Foutbericht
from openapi_server.models.geboorte import Geboorte
from openapi_server.models.geboorte_basis import GeboorteBasis
from openapi_server.models.geboorte_beperkt import GeboorteBeperkt
from openapi_server.models.geboorte_in_onderzoek import GeboorteInOnderzoek
from openapi_server.models.geboorte_in_onderzoek_beperkt import GeboorteInOnderzoekBeperkt
from openapi_server.models.gezag_niet_te_bepalen import GezagNietTeBepalen
from openapi_server.models.gezag_ouder import GezagOuder
from openapi_server.models.gezag_persoon_beperkt import GezagPersoonBeperkt
from openapi_server.models.gezamenlijk_gezag import GezamenlijkGezag
from openapi_server.models.immigratie import Immigratie
from openapi_server.models.immigratie_in_onderzoek import ImmigratieInOnderzoek
from openapi_server.models.in_onderzoek import InOnderzoek
from openapi_server.models.invalid_params import InvalidParams
from openapi_server.models.jaar_datum import JaarDatum
from openapi_server.models.jaar_maand_datum import JaarMaandDatum
from openapi_server.models.kind import Kind
from openapi_server.models.kind_in_onderzoek import KindInOnderzoek
from openapi_server.models.locatie import Locatie
from openapi_server.models.locatie_all_of_datum_ingang_geldigheid import LocatieAllOfDatumIngangGeldigheid
from openapi_server.models.locatie_in_onderzoek import LocatieInOnderzoek
from openapi_server.models.meerderjarige import Meerderjarige
from openapi_server.models.minderjarige import Minderjarige
from openapi_server.models.naam_basis import NaamBasis
from openapi_server.models.naam_gerelateerde import NaamGerelateerde
from openapi_server.models.naam_in_onderzoek import NaamInOnderzoek
from openapi_server.models.naam_persoon import NaamPersoon
from openapi_server.models.naam_persoon_beperkt import NaamPersoonBeperkt
from openapi_server.models.naam_persoon_in_onderzoek import NaamPersoonInOnderzoek
from openapi_server.models.naam_persoon_in_onderzoek_beperkt import NaamPersoonInOnderzoekBeperkt
from openapi_server.models.nationaliteit_bekend import NationaliteitBekend
from openapi_server.models.nationaliteit_bekend_in_onderzoek import NationaliteitBekendInOnderzoek
from openapi_server.models.nationaliteit_onbekend import NationaliteitOnbekend
from openapi_server.models.nationaliteit_onbekend_in_onderzoek import NationaliteitOnbekendInOnderzoek
from openapi_server.models.ontbinding_huwelijk_partnerschap import OntbindingHuwelijkPartnerschap
from openapi_server.models.ontbinding_huwelijk_partnerschap_in_onderzoek import OntbindingHuwelijkPartnerschapInOnderzoek
from openapi_server.models.opschorting_bijhouding import OpschortingBijhouding
from openapi_server.models.opschorting_bijhouding_basis import OpschortingBijhoudingBasis
from openapi_server.models.ouder import Ouder
from openapi_server.models.ouder_in_onderzoek import OuderInOnderzoek
from openapi_server.models.overlijden import Overlijden
from openapi_server.models.overlijden_in_onderzoek import OverlijdenInOnderzoek
from openapi_server.models.partner import Partner
from openapi_server.models.partner_in_onderzoek import PartnerInOnderzoek
from openapi_server.models.personen_query import PersonenQuery
from openapi_server.models.personen_query_response import PersonenQueryResponse
from openapi_server.models.persoon import Persoon
from openapi_server.models.persoon_beperkt import PersoonBeperkt
from openapi_server.models.persoon_in_onderzoek import PersoonInOnderzoek
from openapi_server.models.persoon_in_onderzoek_beperkt import PersoonInOnderzoekBeperkt
from openapi_server.models.persoon_indicatie_gezag_minderjarige import PersoonIndicatieGezagMinderjarige
from openapi_server.models.raadpleeg_met_burgerservicenummer import RaadpleegMetBurgerservicenummer
from openapi_server.models.raadpleeg_met_burgerservicenummer_response import RaadpleegMetBurgerservicenummerResponse
from openapi_server.models.rni_deelnemer import RniDeelnemer
from openapi_server.models.staatloos import Staatloos
from openapi_server.models.staatloos_in_onderzoek import StaatloosInOnderzoek
from openapi_server.models.tijdelijk_geen_gezag import TijdelijkGeenGezag
from openapi_server.models.tweehoofdig_ouderlijk_gezag import TweehoofdigOuderlijkGezag
from openapi_server.models.uitsluiting_kiesrecht import UitsluitingKiesrecht
from openapi_server.models.vastgesteld_niet_nederlander import VastgesteldNietNederlander
from openapi_server.models.verblijfadres_binnenland import VerblijfadresBinnenland
from openapi_server.models.verblijfadres_binnenland_in_onderzoek import VerblijfadresBinnenlandInOnderzoek
from openapi_server.models.verblijfadres_buitenland import VerblijfadresBuitenland
from openapi_server.models.verblijfadres_buitenland_in_onderzoek import VerblijfadresBuitenlandInOnderzoek
from openapi_server.models.verblijfadres_locatie import VerblijfadresLocatie
from openapi_server.models.verblijfadres_locatie_in_onderzoek import VerblijfadresLocatieInOnderzoek
from openapi_server.models.verblijfplaats_buitenland import VerblijfplaatsBuitenland
from openapi_server.models.verblijfplaats_buitenland_all_of_datum_ingang_geldigheid import VerblijfplaatsBuitenlandAllOfDatumIngangGeldigheid
from openapi_server.models.verblijfplaats_buitenland_in_onderzoek import VerblijfplaatsBuitenlandInOnderzoek
from openapi_server.models.verblijfplaats_onbekend import VerblijfplaatsOnbekend
from openapi_server.models.verblijfplaats_onbekend_all_of_datum_ingang_geldigheid import VerblijfplaatsOnbekendAllOfDatumIngangGeldigheid
from openapi_server.models.verblijfplaats_onbekend_in_onderzoek import VerblijfplaatsOnbekendInOnderzoek
from openapi_server.models.verblijfstitel import Verblijfstitel
from openapi_server.models.verblijfstitel_in_onderzoek import VerblijfstitelInOnderzoek
from openapi_server.models.verificatie import Verificatie
from openapi_server.models.volledige_datum import VolledigeDatum
from openapi_server.models.voogdij import Voogdij
from openapi_server.models.waardetabel import Waardetabel
from openapi_server.models.zoek_met_adresseerbaar_object_identificatie import ZoekMetAdresseerbaarObjectIdentificatie
from openapi_server.models.zoek_met_adresseerbaar_object_identificatie_response import ZoekMetAdresseerbaarObjectIdentificatieResponse
from openapi_server.models.zoek_met_geslachtsnaam_en_geboortedatum import ZoekMetGeslachtsnaamEnGeboortedatum
from openapi_server.models.zoek_met_geslachtsnaam_en_geboortedatum_response import ZoekMetGeslachtsnaamEnGeboortedatumResponse
from openapi_server.models.zoek_met_naam_en_gemeente_van_inschrijving import ZoekMetNaamEnGemeenteVanInschrijving
from openapi_server.models.zoek_met_naam_en_gemeente_van_inschrijving_response import ZoekMetNaamEnGemeenteVanInschrijvingResponse
from openapi_server.models.zoek_met_nummeraanduiding_identificatie import ZoekMetNummeraanduidingIdentificatie
from openapi_server.models.zoek_met_nummeraanduiding_identificatie_response import ZoekMetNummeraanduidingIdentificatieResponse
from openapi_server.models.zoek_met_postcode_en_huisnummer import ZoekMetPostcodeEnHuisnummer
from openapi_server.models.zoek_met_postcode_en_huisnummer_response import ZoekMetPostcodeEnHuisnummerResponse
from openapi_server.models.zoek_met_straat_huisnummer_en_gemeente_van_inschrijving import ZoekMetStraatHuisnummerEnGemeenteVanInschrijving
from openapi_server.models.zoek_met_straat_huisnummer_en_gemeente_van_inschrijving_response import ZoekMetStraatHuisnummerEnGemeenteVanInschrijvingResponse
