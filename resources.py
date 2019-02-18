import re

common_reply = ["Hoo my gosh this bot is too fucked",
                "I swear i'm going to create an anti-spam-ahan bot that tells this bot to stfu",
                "Hint: one of the above is an impersonator!!!",
                "Im gnna sue for identity theft",
                "OMG this bot needs to STFU",
                "Im going thru an identity crises :(",
                "Who the fuck is the real me???",
                "I cant take this anymore guys",
                "fcukign toxicc CS cullture",
                "OMG fuck whoever mdde the bot",
                "Its all a CS CONSPIRACY!!!",
                "you noe wat time it is !!",
                " fuk u nicSHAL :(((  ",
                "somebody KICK THIS BOT"
                ]

# Hardcoding triggers and responses.
# Tech related
tech_buzzwords = re.compile(r"\bar\b|\bvr\b|\bblock[\s]*chain[sz]*\b|\bcrypto\b|\bmachine[\s]*learning\b|\bcloud\b|\bHD\b",
                            flags=re.IGNORECASE | re.MULTILINE)
tech_buzzwords_reply = common_reply

# Generic Ahan
triggers = re.compile(r"\bstfu\b.*\bahan\b|\bfuck\b.*\bahan\b",
                      flags=re.IGNORECASE | re.MULTILINE)
trigger_replies = common_reply

# Food / Ameens
food_words= re.compile(r"\bsupper\b|\ba+m+e+n+[sz]*\b|\bmacs+\b|\bchee+se[\s]*fries+\b|\border(ing)?\b|\bma+la+\b", flags=re.IGNORECASE | re.MULTILINE)
food_replies = common_reply
