"""Portal settings tests."""
from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "portal-governo"],
            ["plone.email_from_name", "portal-governo"],
            ["plone.smtp_host", "localhost"],
        ],
    )
    def test_setting(self, portal, key: str, expected: str):
        """Test portal title."""
        value = api.portal.get_registry_record(key)
        assert value == expected
