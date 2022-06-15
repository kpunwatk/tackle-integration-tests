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
from swagger_client.api.list_api import ListApi  # noqa: E501
from swagger_client.rest import ApiException


class TestListApi(unittest.TestCase):
    """ListApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.list_api.ListApi()  # noqa: E501
        c = self.api.api_client.configuration
        c.host = 'http://192.168.39.186/hub/'
        c.api_key[
            'Authorization'] = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJCbTExU0tzbzMwRExDdFljSHFBeWxXbFcwZC15STZvLUdOQmNyYV9Db1AwIn0.eyJleHAiOjE2NTUzMjAyOTQsImlhdCI6MTY1NTMxOTk5NCwianRpIjoiMThmNmI5OWMtMDM3Ny00MzM0LTg4MWMtNTYzODY5Y2RjMDMyIiwiaXNzIjoiaHR0cDovLzE5Mi4xNjguMzkuMTg2L2F1dGgvcmVhbG1zL3RhY2tsZSIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3NzQ5Y2Y4YS1iYjhhLTQzYzctYTY4OS04MGM5MGU2MDIzZWIiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ0YWNrbGUtdWkiLCJzZXNzaW9uX3N0YXRlIjoiZjA5ZTk5ZWUtZTVmYi00ZDg4LWIzMDQtOWYxNmMxNjg5ZmRhIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJhZG1pbiIsInRhY2tsZS1hZG1pbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoidm9sdW1lczpnZXQgZGVwZW5kZW5jaWVzOmRlbGV0ZSBkZXBlbmRlbmNpZXM6Z2V0IGltcG9ydHM6ZGVsZXRlIHRhc2tzOmRlbGV0ZSBhZGRvbnM6cG9zdCB0YXNrczpwdXQgdGFnczpnZXQgYnVzaW5lc3NzZXJ2aWNlczpkZWxldGUgc3Rha2Vob2xkZXJzOmdldCBhc3Nlc3NtZW50czpkZWxldGUgaWRlbnRpdGllczpwb3N0IGFzc2Vzc21lbnRzOmdldCByZXZpZXdzOmdldCBhc3Nlc3NtZW50czpwYXRjaCBhZGRvbnM6ZGVsZXRlIHN0YWtlaG9sZGVyczpwb3N0IHByb2ZpbGUgdGFndHlwZXM6ZGVsZXRlIHRhZ3M6cHV0IGlkZW50aXRpZXM6cHV0IGFwcGxpY2F0aW9uczpnZXQgZGVwZW5kZW5jaWVzOnB1dCBhZGRvbnM6cHV0IHRhZ3R5cGVzOnB1dCBidXNpbmVzc3NlcnZpY2VzOnBvc3QgdGFza3M6Z2V0IGpvYmZ1bmN0aW9uczpkZWxldGUgdGFnczpwb3N0IHRhZ3M6ZGVsZXRlIHByb3hpZXM6cG9zdCBzdGFrZWhvbGRlcmdyb3VwczpwdXQgc2V0dGluZ3M6cHV0IGRlcGVuZGVuY2llczpwb3N0IGJ1c2luZXNzc2VydmljZXM6Z2V0IGFzc2Vzc21lbnRzOnB1dCBhcHBsaWNhdGlvbnM6cHV0IHZvbHVtZXM6cHV0IGFwcGxpY2F0aW9uczpwb3N0IGlkZW50aXRpZXM6ZGVsZXRlIHN0YWtlaG9sZGVyZ3JvdXBzOmdldCB0YWd0eXBlczpnZXQgc2V0dGluZ3M6Z2V0IHByb3hpZXM6cHV0IGltcG9ydHM6cG9zdCBhc3Nlc3NtZW50czpwb3N0IHJldmlld3M6cHV0IGpvYmZ1bmN0aW9uczpnZXQgdGFza3M6cG9zdCBzdGFrZWhvbGRlcnM6ZGVsZXRlIHNldHRpbmdzOmRlbGV0ZSBzdGFrZWhvbGRlcmdyb3VwczpkZWxldGUgcHJveGllczpnZXQgYWRkb25zOmdldCBhZG9wdGlvbnBsYW5zOnBvc3QgZW1haWwgcHJveGllczpkZWxldGUgdm9sdW1lczpwb3N0IGpvYmZ1bmN0aW9uczpwdXQgc3Rha2Vob2xkZXJncm91cHM6cG9zdCBpZGVudGl0aWVzOmdldCB0YWd0eXBlczpwb3N0IGltcG9ydHM6Z2V0IGpvYmZ1bmN0aW9uczpwb3N0IHNldHRpbmdzOnBvc3QgYnVzaW5lc3NzZXJ2aWNlczpwdXQgYXBwbGljYXRpb25zOmRlbGV0ZSBzdGFrZWhvbGRlcnM6cHV0IGltcG9ydHM6cHV0IHJldmlld3M6ZGVsZXRlIHJldmlld3M6cG9zdCIsInNpZCI6ImYwOWU5OWVlLWU1ZmItNGQ4OC1iMzA0LTlmMTZjMTY4OWZkYSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWRtaW4ifQ.G5WPPdhd2sa_uEdhg8UPVmlEQ6AS8WrXR-IBVERXqXdqKz0C0zqytLLGSvGMV4FlEV8XO4G0fIfW7ldABVx0E7n5Exs19kUzDYozD3ujYZdhT0xPdm-DH7GzrO5isplacDv8R1BRar5DsMGRenheACJNo_x2HfctJjFDTMjBHL1lIYRhbBqcgDeI3YPEC_JfaUBm_ZzLdlJhxT1tdmHVSSieVy6x0Dd5dQwHmTrHsAPZe5-NWum_GFB5P0Q41RNs9TYfSw4YbAWJ6OjVMQ4-62rWNySXTlr2wP6ErbHBvPi6jKn8tf7zhlUR_VTUxh9WNt5Ns1Q-sEIrUlasNGOGbQ'
        c.api_key_prefix['Authorization'] = 'Bearer'
        d = self.api.tags_get()
        pass

    def tearDown(self):
        pass

    def test_application_inventory_application_import_get(self):
        """Test case for application_inventory_application_import_get

        List imports.  # noqa: E501
        """
        pass

    def test_application_inventory_import_summary_get(self):
        """Test case for application_inventory_import_summary_get

        List import summaries.  # noqa: E501
        """
        pass

    def test_applications_get(self):
        """Test case for applications_get

        List all applications.  # noqa: E501
        """
        pass

    def test_businessservices_get(self):
        """Test case for businessservices_get

        List all business services.  # noqa: E501
        """
        pass

    def test_dependencies_get(self):
        """Test case for dependencies_get

        List all dependencies.  # noqa: E501
        """
        pass

    def test_settings_get(self):
        """Test case for settings_get

        List all settings.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
