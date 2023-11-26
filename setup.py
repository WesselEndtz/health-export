from setuptools import setup, find_packages
import os

env_file_path = ".env"

# List of environment variables to prompt for and their default values (add more as needed)
env_variables_to_prompt = {
    "DEBUG": "True",
    "AUTO_RUN": "True",
    "SECRET_KEY": "232",
}

# Prompt for missing environment variables and update .env file
with open(env_file_path, "w") as env_file:
    for env_var, default_value in env_variables_to_prompt.items():
        if env_var not in os.environ:
            user_input = input(f"Enter value for {env_var} (default: {default_value}): ")
            if not user_input:
                user_input = default_value
            os.environ[env_var] = user_input
        env_file.write(f"{env_var}={os.environ[env_var]}\n")