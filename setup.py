from setuptools import setup, find_packages
import os

# List of environment variables to prompt for and their default values (add more as needed)
env_variables_to_prompt = {
    "SECRET_KEY": "your_default_secret_key",
    "DATABASE_URL": "your_default_database_url"
}

for env_var, default_value in env_variables_to_prompt.items():
    if env_var not in os.environ:
        user_input = input(f"Enter value for {env_var} (default: {default_value}): ")
        if not user_input:
            user_input = default_value
        os.environ[env_var] = user_input
