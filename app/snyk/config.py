import os
from json import loads

snyk_config = loads("""{
    "OrginisationMap": [
        { "Name": "FirstChecked-Org", "Matcher": "1-*" },
        { "Name": "SecondChecked-Org", "Matcher": "2-*" },
        { "Name": "CatchAll-Org", "Matcher": "*" }
    ]
}""")

def get_snyk_token():
    return os.environ.get('SECRET_SNYK_API_TOKEN')

def get_config_settings():
    return snyk_config