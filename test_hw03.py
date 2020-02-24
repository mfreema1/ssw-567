import unittest
import hw03

from unittest.mock import Mock

repo = {
    'https://api.github.com/users/test/repos': [
        { 'name': 'foo' },
        { 'name': 'bar' }
    ],
    'https://api.github.com/repos/test/foo/commits': [
        {}, {}, {}
    ],
    'https://api.github.com/repos/test/bar/commits': [
        {}
    ]
}

def mockCall(url):
    return Mock(
        json=Mock(
            return_value=repo[url]
        )
    )

class Test(unittest.TestCase):

    @classmethod
    def setUpClass(clazz):
        clazz.service = hw03.GitHubService(
            Mock(
                get=mockCall
            )
        )

    def test_repos(self):
        actual = self.service.getRepos('test')
        self.assertTrue('foo' in actual)

    def test_commits(self):
        actual = self.service.getCommits('test', 'foo')
        self.assertEqual(3, actual)

    def test_output(self):
        actual = self.service.getReposAndCommits('test')
        self.assertTrue(self.service.formatOutput('foo', 3) in actual)
        