# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import flashcards-api-client
from flashcards-api-client.paths.tags_ import get  # noqa: E501
from flashcards-api-client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTags(ApiTestMixin, unittest.TestCase):
    """
    Tags unit test stubs
        Get Tags  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
