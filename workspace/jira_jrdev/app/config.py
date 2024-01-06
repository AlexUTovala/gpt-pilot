import os

class Config:
    """Global configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this'
    JIRA_URL = os.environ.get('JIRA_URL')
    JIRA_USER = os.environ.get('JIRA_USER')
    JIRA_PASSWORD = os.environ.get('JIRA_PASSWORD')  // INPUT_REQUIRED {Please replace 'JIRA_PASSWORD' with your JIRA API token or password securely.}

def init_app(app):
    app.config.from_object(Config)
