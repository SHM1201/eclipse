from nltk.chat.util import Chat,reflections

pairs = [
    [

        r"my name is (,*)",["Hello %1, how are you today",]
    ],
    [

        r"what is your name?",["Chatty",]
    ],[

        r"How are you?",["Im good how about you",]
    ]
]

def chatty():
    print("welcome")
    chat=Chat(pairs,reflections)
    chat.converse()

chatty()