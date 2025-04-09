# Run Gemini 1.5 Flash from your CLI
cus why not

note: for any other llm, may have to replace request/response format (which here is uniqure for gemini)

## Setup
1: clone repo to your directory

2: to avoid conflicts with OS python packages, consider running this in a Virtual Environment
```
python3 -m venv .venv
source .venv/bin/activate
```
3: Install Dependancy (Important)
```
pip install -r requirements.txt
```
4: create a .env file with your llm api key(check .env.example for format if unsure)
```
nano .env
API_KEY=your-llm-api-key-here
```
5: make the script executable
```
chmod +x gemini_cli.py
```
6: Rename and move to Global Path
```
mv gemini_cli.py llm
mkdir -p ~/.local/bin
mv llm ~/.local/bin/
```
7: Add ``~/.local/bin`` to path 
```
export PATH="$HOME/.local/bin:$PATH"
source ~/.bashrc  # or source ~/.zshrc
```

## Use through CLI from anywhere now <3
```
llm "say yes if you agree kito is cool"
```
