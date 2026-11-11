# Login exercise

## Setup and commands
- Run commands from `viikko3/login`, not the repository root. This is an independent uv project requiring Python >=3.14.
- `uv sync` installs Flask and the default dev group (Robot Framework, Browser, BrowserBatteries, requests).
- After setup, run `uv run rfbrowser install` to install Playwright browsers. BrowserBatteries is included, so use `install`, not the separate-Node setup command `init`.
- Start Flask in a separate terminal: `uv run python src/index.py`. Check `http://localhost:5001/ping` for `Pong`; Robot does not start the server.

## Tests
- the app needs to be running test to work it can be done with  `uv run python src/index.py`.
- Full suite: `uv run robot --pythonpath src --variable HEADLESS:true src/tests`.
- Focus one suite: `uv run robot --pythonpath src --variable HEADLESS:true src/tests/register.robot`. Add `--test "Exact Test Name"` before the path to select one case.
- `src/tests/resource.robot` defaults to headed Chromium with a 500ms delay. Its headless branch compares against the literal string `true`, hence `HEADLESS:true`.
- Robot writes `output.xml`, `log.html`, and `report.html` in the working directory. Use `--outputdir <directory>` to avoid overwriting existing local reports; these reports and `playwright-log.txt` are ignored.
- Both `src/tests/resource.robot` and `src/AppLibrary.py` target port 5001. Overriding Robot's `SERVER` alone does not redirect the Python helper.
- Tests reset shared application state via `POST /tests/reset`; do not run suites concurrently against the same server.

## Wiring
- `src/index.py` starts the app; `src/app.py` defines routes and connects the singleton service in `src/services/user_service.py` to the in-memory repository in `src/repositories/user_repository.py`. No database or migrations are needed.
- Robot imports `src/AppLibrary.py` through the shared resource. Its setup keywords create users over HTTP and reset the server repository, rather than modifying local Python objects.
- `uv.lock` and `.venv/` are ignored, not tracked; an existing local lock is not a shared reproducibility guarantee.
