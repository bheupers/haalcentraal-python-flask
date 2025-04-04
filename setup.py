import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="BRP API Personen",
    author_email="",
    url="",
    keywords=["OpenAPI", "BRP API Personen"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    API voor het bevragen van personen uit de basisregistratie personen (BRP), inclusief de registratie niet-ingezeten (RNI). Met deze API kun je personen zoeken en actuele gegevens over personen, kinderen, partners en ouders raadplegen.  Gegevens die er niet zijn of niet actueel zijn krijg je niet terug. Had een persoon bijvoorbeeld een verblijfstitel die nu niet meer geldig is, dan wordt die verblijfstitel niet opgenomen. In partners wordt alleen de actuele of de laatst ontbonden partner geleverd.  Zie de [Features overzicht](https://brp-api.github.io/Haal-Centraal-BRP-bevragen/v2/features-overzicht) en [Getting started](https://brp-api.github.io/Haal-Centraal-BRP-bevragen/v2/getting-started) voor nadere toelichting. 
    """
)

