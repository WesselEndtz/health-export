# Local usage
1. Create virtual environment
    - 'python3.9 -m venv venv'
    - 'source venv/bin/activate'
2. Init GIT
   - `git init`
   - `git add .`
3. Install required packages inside the venv
- `pip install -r requirements.txt`
4. Setup your enviroment settings
   ```bash
   python setup.py
   ```
5. Init Black Linter:
    - `pre-commit install`
    - `pre-commit run --all-files`
6. Run app:
   ```bash
   python main.py
   ```