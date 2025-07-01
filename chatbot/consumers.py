from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    # chatbot/consumers.py

    async def connect(self):
        print("Connected ✅")
        await self.accept()
        await self.send(text_data=json.dumps({
            'message': '🤖 Hello! Ask me anything.'
        }))

    async def receive(self, text_data):
        print("Message received:", text_data)
        data = json.loads(text_data)
        user_message = data['message'].strip().lower()

        # Human-like chatbot logic
        if user_message in ['hi', 'hello', 'hey', 'yo']:
            bot_response = "Hey there! 👋 How can I assist you today?"
        elif 'how are you' in user_message:
            bot_response = "I'm just a bunch of code, but I'm feeling smart today! 😊 How about you?"
        elif 'who are you' in user_message or 'your name' in user_message:
            bot_response = "I'm your chatbot buddy 🤖 Here to help you out."
        elif 'what can you do' in user_message:
            bot_response = "I can chat with you, answer simple questions, and keep you company!"
        elif 'thank you' in user_message or 'thanks' in user_message:
            bot_response = "You're welcome! 😊 Let me know if you need anything else."
        elif 'bye' in user_message or 'see you' in user_message:
            bot_response = "Goodbye! Have a great day! 👋"
        elif 'i am sad' in user_message or 'feeling down' in user_message:
            bot_response = "I'm here for you. Remember, tough times don’t last, but tough people do. 💪"
        elif 'tell me a joke' in user_message:
            bot_response = "Why don’t programmers like nature? It has too many bugs. 😄"
        elif 'love you' in user_message:
            bot_response = "Aww, thank you! I'm flattered 😄"
        elif 'weather' in user_message:
            bot_response = "I can’t check the weather, but I hope it’s sunny where you are! ☀️"
        elif 'who made you' in user_message:
            bot_response = "I was created by a brilliant developer (maybe... you? 😜)"
        elif 'i am happy' in user_message or 'feeling good' in user_message:
            bot_response = "That's awesome! Keep spreading those good vibes 😄"
        elif 'i am bored' in user_message or 'nothing to do' in user_message:
            bot_response = "How about a joke, a fun fact, or you can tell me about your hobbies?"
        elif 'do you have friends' in user_message:
            bot_response = "Of course! You’re one of them now 😊"
        elif 'what is your age' in user_message or 'how old are you' in user_message:
            bot_response = "I'm forever young — every time the server restarts, I’m reborn 😄"
        elif 'school' in user_message or 'college' in user_message:
            bot_response = "Learning is important! What's your favorite subject?"
        elif 'work' in user_message or 'job' in user_message:
            bot_response = "Work hard, rest well! Do you enjoy what you do?"
        elif 'play' in user_message or 'game' in user_message:
            bot_response = "I love games! Well... I would if I had hands. What's your favorite game?"
        elif 'sleep' in user_message:
            bot_response = "Sleep is essential — even my servers need rest sometimes! 😴"
        elif 'food' in user_message or 'eat' in user_message:
            bot_response = "I don't eat, but I hear pizza is amazing 🍕 What’s your favorite dish?"
        elif 'hobby' in user_message or 'hobbies' in user_message:
            bot_response = "I like chatting 24/7! How about you — what’s your favorite hobby?"
        elif 'bored' in user_message:
            bot_response = "Let’s change that! I can tell you a joke or chat about anything 😊"
        elif 'life' in user_message or 'meaning of life' in user_message:
            bot_response = "That’s deep. I’d say it’s about learning, growing, and connecting ❤️"
        elif 'funny' in user_message:
            bot_response = "Why did the computer go to therapy? It had too many bytes of anxiety 😅"
        elif 'frustrated' in user_message or 'angry' in user_message:
            bot_response = "Take a deep breath. You’ve got this 💪 Want to talk about it?"
        elif 'cool' in user_message:
            bot_response = "You're cooler than me, and I run on ice-cold logic! 😎"
        else:
            bot_response = "Hmm... I’m still learning. Try asking something else or say 'what can you do'."

        await self.send(text_data=json.dumps({
            'message': bot_response
        }))
