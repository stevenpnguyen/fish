.PHONY: build serve clean install run

PORT ?= 8000

install:
	pip install -r requirements.txt

run:
	pgzrun game.py

build: install
	python -m pygbag --build .
	cp CNAME build/web/CNAME

serve: install
	@exec python -m pygbag .

clean:
	rm -rf build/
