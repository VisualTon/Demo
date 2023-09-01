install:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	sudo npm install -g @mermaid-js/mermaid-cli
run:
	python3 TonBot.py