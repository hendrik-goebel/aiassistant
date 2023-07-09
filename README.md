# Chat GPT code helper
AI helper which is aware of your current codebase as context.

- uses the OpenAI Api, so an API key is needed
- Does not work on large code bases since since the context size is limited.


## SETUP

1. Install:
```
pip3 install -r requirements.txt
```

2. set open ai key in .env

3. Set path to codebase in .env

4. Activate virtual env:

```
. venv/bin/activate
````

5. Ask a question about the configured code base:

```
python3 chat.py "What does the code do?"
```


## TODO:
- store conversation history