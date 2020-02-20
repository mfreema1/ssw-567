import requests

def getRepos(owner):
    r = requests.get(f'https://api.github.com/users/{owner}/repos')
    return map(lambda info: info['name'], r.json())

def getCommits(owner, repo):
    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    return len(r.json())

def formatOutput(repo, commits):
    return f'Repo: {repo} Number of commits: {commits}'

def getReposAndCommits(owner):
    return [ formatOutput(repo, getCommits(owner, repo)) for repo in getRepos(owner) ]