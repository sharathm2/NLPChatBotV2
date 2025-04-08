
# NLPChatBot



## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


## Authors

- [@sharathm2](https://www.github.com/sharathm2)


## Installation

- HOW TO RUN THIS BOT

- Clone Repo
- Create python 3.11 virtual environment
- Run pip install for requirements.txt
- Run "python -m spacy download en_core_web_sm" in the virtual environment
- Run "python scripts/train_transfomers.py"
- Run "python main.py"


- If you want to deploy the API, just run "uvicorn app.main:app --reload"

- In order to run the frontend, cd into the frontend repo and run "npm run dev" and navigate to "localhost:5173".

- ## REMEMBER, THE BACKEND SHOULD BE RUN FROM WITHIN THE ACTIVATED VENV, THE FRONTEND SHOULD BE RUN FROM OUTSIDE THE VENV IN THE FRONTEND DIR


- The bot should work locally if run from the terminal, since I have yet to add all of the changes which store user information(chat history etc) in supabase
- Eventually, the code for this bot will be open source, however I plan on deploying it to production, meaning you will need to create your own .env files to store your secrets(supabase keys, url etc) and connect it to your own database when the time comes
- I will open source my Supabase config as well meaning you will get access to all of the RLS policies I have currently implemented
    
