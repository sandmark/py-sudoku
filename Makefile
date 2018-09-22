REQ = requirements.txt

init:
	pip install -r $(REQ)

freeze:
	pip freeze > $(REQ)

test:
	nosetests -c .noserc tests

.PHONY: init test freeze
