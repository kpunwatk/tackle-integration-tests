# coding: utf-8

"""
    tackle2.0 api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.copy_api import CopyApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCopyApi(unittest.TestCase):
    """CopyApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.copy_api.CopyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reviews_copy_post(self):
        """Test case for reviews_copy_post

        Copy a review from one application to others.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()