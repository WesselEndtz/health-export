
# Setting the init version
1. Delete Readme about project setup
2. Initialize git and add origin:
```bash
git init
git add .
git commit -am 'Init API'
git remote add origin git@bitbucket.org:{{cookiecutter.bitbucket_workspace_name}}/{{cookiecutter.project_name}}.git
git push -u origin develop
```

# Local usage
1. Create virtual environment
    - 'python3.9 -m venv venv'
    - 'source venv/bin/activate'
2. Init GIT
   - `git init`
   - `git add .`
3. Install required packages inside the venv
- `pip install -r requirements.txt`
4. Setup .env file for local environment
   ```bash
   cp .env.example .env
   ```
5. Init Black Linter:
    - `pre-commit install`
    - `pre-commit run --all-files`
6. Run app:
   - `python3.9 main.py`