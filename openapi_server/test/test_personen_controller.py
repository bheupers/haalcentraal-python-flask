import unittest

from flask import json

from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from openapi_server.models.foutbericht import Foutbericht  # noqa: E501
from openapi_server.models.personen_query import PersonenQuery  # noqa: E501
from openapi_server.models.personen_query_response import PersonenQueryResponse  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPersonenController(BaseTestCase):
    """PersonenController integration test stubs"""

    @unittest.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
    def test_personen(self):
        """Test case for personen

        Zoek personen
        """
        personen_query = openapi_server.PersonenQuery()
        headers = { 
            'Accept': 'application/problem+json',
            'Content-Type': 'application/json; charset=utf-8',
        }
        response = self.client.open(
            '/haalcentraal/api/brp/personen',
            method='POST',
            headers=headers,
            data=json.dumps(personen_query),
            content_type='application/json; charset=utf-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
