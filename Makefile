setup:
	python -m venv venv
	.\venv\Scripts\activate && pip install -r requirements.txt
	.\venv\Scripts\activate && pip install pre-commit
	.\venv\Scripts\activate && pre-commit install

test:
	.\venv\Scripts\activate && pytest
