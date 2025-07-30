# File Name: get_projects.py
# Owner: Andrew Holland (@SilicaStormSiam)
# Purpose: Retrieves project names from the GitHub Projects tab for SilicaStormSiam using the GitHub API for the CPM - Chat Bot project.
# Version Control:
#   - Version 1.0 (2025-07-24): Initial script to fetch project names using GitHub API with token from .env.
#   - Version 0.2 (2025-07-23): Planned API integration.
#   - Version 0.1 (2025-07-23): Conceptualized script for project name retrieval.

import requests
import sys
from dotenv import load_dotenv
import os

load_dotenv()

def get_github_projects(username):
    """
    Fetches project names for a given GitHub user using the GitHub API.
    Args:
        username (str): GitHub username (e.g., 'silicastormsiam').
    Returns:
        list: List of project names or empty list if an error occurs.
    """
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN not set in .env file", file=sys.stderr)
        return []
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/users/{username}/projects"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        projects = response.json()
        project_names = [project["name"] for project in projects]
        return project_names
    except requests.exceptions.RequestException as e:
        print(f"Error fetching projects: {e}", file=sys.stderr)
        return []

if __name__ == "__main__":
    username = "silicastormsiam"
    projects = get_github_projects(username)
    if projects:
        print("SilicaStormSiam's Projects:")
        for i, name in enumerate(projects, 1):
            print(f"{i}) {name}")
    else:
        print("No projects found or error occurred.")
