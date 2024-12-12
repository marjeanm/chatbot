# chatbot

# Cyberpunk Life Path Chatbot

This Python-based chatbot is designed to simulate conversations around the various life paths in the **Cyberpunk 2077** game. It uses the `ChatterBot` library to create an interactive chatbot that can respond to a variety of queries regarding the game's life paths, such as **Nomad**, **Street Kid**, and **Corpo**.

## Prerequisites

To run this chatbot, you will need the following:

- Python 3.x
- Required Python libraries:
  - `chatterbot`
  - `chatterbot_corpus`
  - `nltk`

Install the required dependencies using `pip`:

```bash
pip install chatterbot
pip install nltk

## Setup and Configuration
- NLTK Setup: The nltk library is used to download required resources for tokenization. When the bot runs, it will automatically download the necessary data using the following command:
- nltk.download('punkt')
- Chatbot Initialization: The chatbot is initialized with specific logic adapters and a database URI to store conversation data:
     - bot = ChatBot("V",
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=[
                  'chatterbot.logic.BestMatch',
                  'chatterbot.logic.MathematicalEvaluation',
                  'chatterbot.logic.TimeLogicAdapter',
              ],
              database_uri='sqlite:///database.sqlite3')
- The SQLStorageAdapter stores conversation data in a local SQLite database (database.sqlite3).

- Training the Bot: The chatbot is pre-trained with conversation data related to Cyberpunk's life paths. This data is in the format:

[
    {"User_Query": "What life path should I choose?", "Intent": "CharacterBuild", "Response": "In Cyberpunk, there are three main life paths: Nomad, Street Kid, and Corpo."},
    ...
]
- The chatbot is trained on this data to respond intelligently to user queries.

Training New Data: You can continue training the bot with new data during runtime. The bot will accept new phrases from the user in a specific format:

user phrase, bot response

Ensure that the input contains an even number of phrases (pairs of user input and bot response). For example:


- What life path is best for beginners?, The Street Kid path may be the easiest for beginners.

Run the script, and you will be prompted to interact with the bot:
- python chatbot.py
Basic Interaction
-You can ask the bot various questions related to the life paths in Cyberpunk 2077. Example questions include:
-"What life path should I choose?"
-"Can you tell me about the Nomad path?"
-"What is the best life path for combat?"
-Training Mode
-You can train the bot with new phrases during interaction. To enter training mode, type:


train
Then input pairs of user phrases and bot responses. The bot will learn from the new data immediately.
You: What is the best life path for beginners?
Bot: The Street Kid path may be the easiest for beginners.

Code Structure
1. ChatBot Initialization:
Creates a new instance of the ChatBot class and configures it with specific adapters for conversation.
2. Trainer Setup:
Initializes a ListTrainer to train the bot on the provided conversation data.
3. Conversation Data:
Includes a set of predefined queries and responses related to Cyberpunk life paths.
4. Training Function:
continue_training function allows the chatbot to learn from new data provided by the user.
5. Interaction Loop:
The main interaction loop listens for user input and responds based on the trained data.
License
This project is licensed under the MIT License - see the LICENSE file for details.
