# FastAPI News API

Simple FastAPI application providing a hello endpoint with FastAPI's automatic documentation generation.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Install Dependencies
- Ensure Python 3.12+ is available: `python3 --version`
- Install dependencies: `pip3 install -r requirements.txt` -- takes ~7 seconds to complete
- For development and testing: `pip3 install pytest httpx flake8 black` -- takes ~10 seconds to complete

### Run the Application
- Start the server: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Server starts immediately (under 1 second)
- Access the API at: http://localhost:8000
- View interactive docs at: http://localhost:8000/docs
- View OpenAPI schema at: http://localhost:8000/openapi.json

### Testing
- Run tests: `pytest test_*.py -v` -- takes under 1 second to complete
- For testing API endpoints, install httpx: `pip3 install httpx`
- Test the main endpoint manually: `curl "http://localhost:8000/hello"`
- Test with parameters: `curl "http://localhost:8000/hello?name=TestName"`

### Code Quality and Linting
- Check code style: `flake8 main.py` -- takes under 0.2 seconds
- Format code: `black main.py` -- takes under 0.2 seconds  
- Check formatting without changes: `black --check main.py`
- View formatting diff: `black --diff main.py`
- Compile check: `python3 -m py_compile main.py`

## Validation

### ALWAYS manually validate any new code changes by:
1. Starting the server: `uvicorn main:app --host 0.0.0.0 --port 8000`
2. Testing the hello endpoint: `curl "http://localhost:8000/hello"`
3. Testing with parameters: `curl "http://localhost:8000/hello?name=TestValue"`
4. Verifying docs are accessible: `curl -s "http://localhost:8000/docs" | head -5`
5. Checking OpenAPI schema: `curl -s "http://localhost:8000/openapi.json"`

### Pre-commit validation steps:
- Always run `flake8` and fix any style issues before committing
- Always run `black --check` and format code if needed
- Always manually test the API endpoints after changes
- No CI/CD exists currently, so manual validation is critical

## Repository Structure

### Key files:
- `main.py` -- Main FastAPI application with hello endpoint
- `requirements.txt` -- Contains fastapi and uvicorn dependencies
- `README.md` -- Minimal project description
- `.gitignore` -- Excludes __pycache__/ directory

### Common outputs for reference:

#### Repository root listing:
```
.git/
.gitignore
README.md
main.py
requirements.txt
```

#### requirements.txt content:
```
fastapi
uvicorn
```

#### main.py structure:
- FastAPI app instance
- Single GET endpoint at /hello with optional name parameter
- Returns JSON response with greeting message

## Development Notes

- No build step required - pure Python application
- All operations are very fast (under 10 seconds for any command)
- Server can be stopped with Ctrl+C
- Application runs on localhost:8000 by default
- FastAPI automatically provides interactive docs and OpenAPI schema
- No existing tests in repository, but pytest framework works well
- Current code has minor style issues that flake8 and black will identify

## Common Tasks

### Adding new endpoints:
1. Add route decorator and function to main.py
2. Start server and test endpoint manually
3. Run linting and fix any style issues
4. Test all existing endpoints still work

### Debugging:
- Check server logs in terminal where uvicorn is running
- Use interactive docs at /docs to test endpoints
- Check Python syntax with: `python3 -m py_compile main.py`
- Verify imports work: `python3 -c "from main import app; print('OK')"`