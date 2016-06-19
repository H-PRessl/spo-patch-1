from unittest import TestCase

from client.client_context import ClientContext
from client.runtime.auth.authentication_context import AuthenticationContext
from examples.settings import settings


class SPTestCase(TestCase):
    """SharePoint specific test case base class"""

    @classmethod
    def setUpClass(cls):
        ctx_auth = AuthenticationContext(url=settings['url'])
        ctx_auth.acquire_token_for_user(username=settings['username'], password=settings['password'])
        cls.context = ClientContext(settings['url'], ctx_auth)



