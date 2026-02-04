#LOOKUP FILE for quotes. needs to be integrated to app.py if you want to use. I used this before making this function agentic

import random
quotes = {
    "affleck": [
        "Tell me, do you bleed? You will.",
        "I’m rich.",
        "Men are still good. We can rebuild. We can do better. We will. We have to.",
        "Twenty years in Gotham, Alfred; how many good guys are left? How many stayed that way?",
        "The world only makes sense if you force it to.",
        "If there’s even a one percent chance that he is our enemy, we have to take it as an absolute certainty.",
        "Save one person. And then you’ll know.",
        "I bought the bank.",
        "We're criminals, Alfred. We've always been criminals. Nothing's changed.",
        "I failed him in life. I won't fail him in death.",
    ],
    "bale": [
        "It's not who I am underneath, but what I do that defines me.",
        "You either die a hero, or you live long enough to see yourself become the villain.",
        "A hero can be anyone, even a man doing something as simple and reassuring as putting a coat around a young boy's shoulders to let him know that the world hadn't ended.",
        "Why do we fall? So we can learn to pick ourselves up.",
        "Theatricality and deception are powerful agents to the uninitiated.",
        "I wear a mask. And that mask, it's not to hide who I am, but to create what I am.",
        "Sometimes the truth isn't good enough, sometimes people deserve more. Sometimes people deserve to havetheir faith rewarded.",
        "I’m whatever Gotham needs me to be.",
        "Swear to me!",
        "I’m not wearing hockey pads!",
        "I won’t kill you, but I don’t have to save you.",
        "Does it come in black?",
        "Sometimes the truth isn't good enough, sometimes people deserve more.",
        "Bats frighten me. It's time my enemies shared my dread."
        ],
    "pattinson": [
        "I am vengeance.",
        "Fear is a tool. When that light hits the sky, it’s not just a call. It’s a warning.",
        "I don’t care what happens to me.",
        "It’s a big city. I can’t be everywhere. But they don’t know where I am.",
        "Our points of view are different, Selina.",
        "Two years of nights have turned me into a nocturnal animal.",
        "I have to force myself to believe that I'm making a difference.",
        "Things will get worse before they get better.",
        "Vengeance won’t change the past. In mine, or anyone else’s. I have to become more.",
    ],
    "darkwing": [
        "The shadow of justice falls!",
        "I am the night that keeps the shadows at bay!",
        "The night is my domain!",
        "Justice never sleeps, and neither do I.",
        "You can't hide from the darkness.",
        "You've made your last mistake in my city.",
        "Fear the wings of justice!",
        "I am the darkness that fights for the light.",
        "This ends now.",
        "The shadows always find the truth."
    ],
    "niteowl": [
        "We were supposed to make the world a better place.",
        "What happened to us? What happened to the American Dream?",
        "I'm not the one who's crazy!",
        "It's a joke. It's all a joke.",
        "You're a monster, Adrian.",
        "Maybe we just don't belong in this world anymore.",
        "I didn't do it for the glory. I did it because it had to be done.",
        "We're out of time.",
        "You really think I'd go back to that?",
        "God help us all."
    ]
}

def get_random_quote(actor):
    actor = actor.lower()
    if actor in quotes:
        return random.choice(quotes[actor])
    return ""
