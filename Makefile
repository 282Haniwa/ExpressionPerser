PROJECT = ExpressionPerser
TARGET	= Example

ZIP_FILE	= $(PROJECT).zip

CLEAN_FILE	= *.pyc $(ZIP_FILE)

all: test

test:
	python $(TARGET).py

clean:
	find . -type d -name __pycache__ -print0 | xargs -0 rm -rf
	-rm -rf  $(CLEAN_FILE)

zip: clean
	zip -r $(ZIP_FILE) ./
