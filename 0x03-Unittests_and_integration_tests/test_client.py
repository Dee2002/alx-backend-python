#!/usr/bin/env python3
"""
Unit and integration tests for client module
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from utils import get_json
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test GithubOrgClient.org"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test/repos"
        }
        client = GithubOrgClient("test")
        self.assertEqual(
            client._public_repos_url, "https://api.github.com/orgs/test/repos"
        )

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos"""
        mock_public_repos_url.return_value = (
            "https://api.github.com/orgs/test/repos"
        )
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("test")
        self.assertEqual(
            client.public_repos(), [{"name": "repo1"}, {"name": "repo2"}]
        )
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test/repos"
        )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license"""
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload, "repos_payload": repos_payload,
        "expected_repos": expected_repos, "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = [
            Mock(**{"json.return_value": cls.org_payload}),
            Mock(**{"json.return_value": cls.repos_payload})
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class after integration tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos"""
        client = GithubOrgClient("test")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos with license"""
        client = GithubOrgClient("test")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
