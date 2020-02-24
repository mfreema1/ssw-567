class GitHubService():

    def __init__(self, api):
        self.api = api

    def getRepos(self, owner):
        r = self.api.get(f'https://api.github.com/users/{owner}/repos')
        return map(lambda info: info['name'], r.json())

    def getCommits(self, owner, repo):
        r = self.api.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
        return len(r.json())

    def formatOutput(self, repo, commits):
        return f'Repo: {repo} Number of commits: {commits}'

    def getReposAndCommits(self, owner):
        return [ self.formatOutput(repo, self.getCommits(owner, repo)) for repo in self.getRepos(owner) ]