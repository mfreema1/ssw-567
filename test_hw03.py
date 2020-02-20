import unittest
import hw03

KNOWN_USER = 'mfreema1'
KNOWN_REPO = 'cs115'
KNOWN_COMMITS = 10
KNOWN_FORMAT = hw03.formatOutput(KNOWN_REPO, KNOWN_COMMITS)

class Test(unittest.TestCase):

    def test_repos(self):
        actual = hw03.getRepos(KNOWN_USER)
        self.assertTrue(KNOWN_REPO in actual)

    def test_commits(self):
        actual = hw03.getCommits(KNOWN_USER, KNOWN_REPO)
        self.assertEqual(KNOWN_COMMITS, actual)

    def test_output(self):
        actual = hw03.getReposAndCommits(KNOWN_USER)
        self.assertTrue(KNOWN_FORMAT in actual)
        