import tkinter as tk
from tkinter import scrolledtext
import wikipedia
import random

wikipedia.set_lang("en")

# Small talk responses
small_talk = {
    "hi": ["Hello! How are you?", "Hey! How’s it going?", "Hi there!"],
    "hello": ["Hello! How are you?", "Hi! Nice to see you.", "Hey!"],
    "how are you": ["I’m good, thank you! How about you?", "Doing great! And you?"],
    "thanks": ["You’re welcome!", "No problem!", "Anytime!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

# Jokes
jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]

def get_response(user_msg):
    msg_lower = user_msg.lower().strip()

    # Small talk
    for key in small_talk:
        if key in msg_lower:
            return random.choice(small_talk[key])

    if "joke" in msg_lower:
        return random.choice(jokes)

    # Wikipedia factual answer
    try:
        result = wikipedia.summary(user_msg, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your question is ambiguous. Did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.exceptions.PageError:
        return "Hmm, I couldn’t find information on that. Can you rephrase?"
    except:
        return "Sorry, I’m having trouble finding the answer right now."

def send_message(event=None):
    user_msg = entry.get().strip()
    if user_msg == "":
        return
    chat_area.insert(tk.END, "You: " + user_msg + "\n")
    reply = get_response(user_msg)
    chat_area.insert(tk.END, "Bot: " + reply + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("CODTECH Human-like Chatbot")
root.geometry("500x600")

# Optional: Add logo
# from tkinter import PhotoImage
# logo_img = PhotoImage(file="images/logo.png")
# logo_label = tk.Label(root, image=logo_img)
# logo_label.pack(pady=10)

chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=55, height=25, font=("Arial", 12))
chat_area.pack(pady=10)

entry = tk.Entry(root, width=45, font=("Arial", 12))
entry.pack(pady=5)
entry.bind("<Return>", send_message)

send_btn = tk.Button(root, text="Send", command=send_message, width=10, font=("Arial", 12))
send_btn.pack()

root.mainloop()
