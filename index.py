from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
from nltk import word_tokenize, sent_tokenize

# Download required NLTK resources
nltk.download('punkt')

# Create a new instance of the ChatBot class.
bot = ChatBot("V",
               storage_adapter='chatterbot.storage.SQLStorageAdapter',
               logic_adapters=[
                   'chatterbot.logic.BestMatch',
                   'chatterbot.logic.MathematicalEvaluation',
                   'chatterbot.logic.TimeLogicAdapter',
               ],
               database_uri='sqlite:///database.sqlite3'
              )

# Create a trainer for the chatbot
trainer = ListTrainer(bot)

# JSON data as a Python dictionary
conversation_data_json = [
    # Fill in responses for missing entries
    {"User_Query": "What life path should I choose?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "In Cyberpunk, there are three main life paths: Nomad, Street Kid, and Corpo. Each path gives a unique background and influences your experience in Night City."},
    {"User_Query": "Is there a best life path to choose?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "The best life path depends on your preferred playstyle. Nomad offers freedom, Street Kid is tied to the city’s underbelly, and Corpo deals with corporate intrigue."},
    {"User_Query": "Which life path is the most fun?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "The fun factor depends on what kind of gameplay you enjoy. If you like freedom and exploration, Nomad might be fun. If you prefer high-stakes corporate drama, Corpo is for you."},
    {"User_Query": "What life path should I start with?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "Start with the Nomad if you want a grounded perspective, the Street Kid if you want to dive into the city’s underbelly, or Corpo for a taste of corporate power and manipulation."},
    {"User_Query": "Which life path is the easiest for beginners?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "The Street Kid path may be the easiest for beginners as it offers more familiar urban interactions and access to useful contacts."},
    {"User_Query": "What’s the best life path for combat-focused play?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "The Corpo path might offer a strong combat experience as it emphasizes tactical thinking and accessing powerful resources."},
    {"User_Query": "What life path is best for a story-rich experience?", "Intent": "CharacterBuild", "Mission_name": "", "Response": "The Nomad path provides a story-rich experience with deep narrative elements tied to family and the outside world of Night City."},
    {"User_Query": "Can you tell me about the Nomad path?", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "This path is about the outsider, living in the desert-outside world of night city, called the badlands, they are drifters that have strong family ties and are not understood or cared about by the people of the cities."},
    {"User_Query": "What is the Nomad life path?", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "You just start out as an outcast of the Nomad life that looks to make a name for themselves in Night City."},
    {"User_Query": "How does the Nomad path work?", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "The Nomad path offers freedom, a family-oriented backstory, and a different view of Night City. It’s ideal for players seeking an outsider’s perspective."},
    {"User_Query": "What’s unique about the Nomad path?", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "As a Nomad, you have access to exclusive dialogue options, interactions, and story elements that reflect your background as a wanderer and someone with a deep understanding of life outside urban society. This path is ideal for players who want a grounded, outsider view on the events unfolding in Night City."},
    {"User_Query": "What does it mean to choose the Nomad life path?", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "The Nomad path is unique because it starts your character as an outsider to Night City, someone who values freedom, family bonds, and independence. You begin in the vast, open Badlands, giving you a unique perspective on the bustling city."},
    {"User_Query": "Explain the Nomad path in Cyberpunk.", "Intent": "CharacterBuild", "Mission_name": "The Nomad", "Response": "The Nomad path gives you a different perspective on the game world, focusing on survival, family loyalty, and the challenges faced by outsiders."},
    {"User_Query": "Can you tell me about the Corpo path?", "Intent": "CharacterBuild", "Mission_name": "The Corpo-Rat", "Response": "Corpo is about being a corporate worker in Night City, who lost faith in the corporations and chose to make a name for themselves in the underworld."},
    {"User_Query": "What is the Corpo life path?", "Intent": "CharacterBuild", "Mission_name": "The Corpo-Rat", "Response": "It’s about having the experience, and the know-how to navigate the city, money, power, and respect, while earning more than the next."},
    {"User_Query": "How does the Corpo path work?", "Intent": "CharacterBuild", "Mission_name": "The Corpo-Rat", "Response": "Corpo is for those who enjoy corporate power and intrigue. You start as a high-ranking employee, giving you a unique perspective and access to insider connections."},
    {"User_Query": "What’s unique about the Corpo path?", "Intent": "CharacterBuild", "Mission_name": "The Corpo-Rat", "Response": "Corpo lets you experience Night City’s corporate life with insider access to powerful circles. It’s a path for players drawn to intrigue and manipulation."},
    {"User_Query": "What does it mean to choose the Corpo life path?", "Intent": "CharacterBuild", "Mission_name": "The Corpo-Rat", "Response": "The Corpo path is centered on high-stakes business and espionage within powerful corporations, perfect for players interested in manipulation and insider knowledge."},
    {"User_Query": "Can you tell me about the StreetKid path?", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Street Kid is focused on living in the grittier streets of Night City."},
    {"User_Query": "What is the StreetKid life path?", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Street Kid gives you insider knowledge of the city’s gangs and hidden layers. You'll have access to special contacts and dialogue that fit this urban background."},
    {"User_Query": "How does the StreetKid path work?", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Street Kid’s connections to Night City’s gangs provide a gritty, realistic take on urban life. Perfect for those wanting to dive into the city’s underbelly."},
    {"User_Query": "What’s unique about the StreetKid path?", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Street Kid offers a deep connection to the underworld of Night City, with insider access to gang knowledge and city secrets."},
    {"User_Query": "What does it mean to choose the StreetKid life path?", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Choosing the StreetKid path means embracing life on the streets, knowing everyone and everything in the urban underworld, making your way by dealing with gangs and the city's corrupt systems."},
    {"User_Query": "Explain the StreetKid path in Cyberpunk.", "Intent": "CharacterBuild", "Mission_name": "The Street Kid", "Response": "Having lived a life in the streets fighting off 'badges' and navigating around gangs, Street Kids have a wealth of knowledge about the city, knowing every street and just about everyone who lives there."}
]

# Add the conversation data to the trainer
trainer.train([item['User_Query'] + ", " + item['Response'] for item in conversation_data_json])

# Function to continue training the bot with new data
def continue_training(new_data):
    trainer.train(new_data)

# Interaction loop
while True:
    try:
        user_input = input("You: ")  # Prompt user for input
        
        if user_input.lower() == "train":
            new_phrases = input("Enter new phrases to train the bot (format: 'user phrase, bot response'): ")
            new_phrases_list = [phrase.strip() for phrase in new_phrases.split(',')]
            # Ensure that the input has pairs
            if len(new_phrases_list) % 2 == 0:
                training_data = list(zip(new_phrases_list[0::2], new_phrases_list[1::2]))
                continue_training(training_data)
                print("Bot has been trained with the new phrases.")
            else:
                print("Please enter an even number of phrases (pairs of user input and bot response).")
            continue  # Continue to the next iteration of the loop
        
        bot_response = bot.get_response(user_input)
        print(f"V: {bot_response}")
        
        
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
