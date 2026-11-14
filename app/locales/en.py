from app.locales.shape import guide, step

DATA = {
    "disclaimer": (
        "Kanoon Saathi is not a lawyer and does not decide your case. "
        "The law depends on your state. Before you sign or give a thumb impression, "
        "ask a District Legal Services Authority lawyer to read the paper."
    ),
    "help": [
        {"name": "Emergency", "phone": "112", "url": None, "note": "Violence, a break-in, or danger today. Police and ambulance."},
        {"name": "Women helpline", "phone": "181", "url": None, "note": "Threats, violence, or fear. You can talk on the phone."},
        {"name": "Cyber crime helpline", "phone": "1930", "url": "https://cybercrime.gov.in", "note": "Online cheating or money. You can also report from home at cybercrime.gov.in."},
        {"name": "Free legal help", "phone": None, "url": "https://nalsa.gov.in", "note": "District Legal Services Authority, at the district court. You can also ask for Tele-Law at a Common Service Centre."},
    ],
    "state_unknown": "Tell the office which state the land is in. The record has a different name in each state.",
    "state_known": "Say that the land is in {state}. Ask them to open the record for that state.",
    "no_reader": {
        "title": "I need the model key to read this photo",
        "spoken": (
            "The photo is not saved. I cannot read the words in the picture until a language-model key is added. "
            "Until then, ask someone you trust to read it aloud, or tell me who sent it, whether it asks for money, and whether it asks for a signature."
        ),
    },
    "emergency": guide(
        "now",
        "Call for help now",
        "This sounds dangerous right now. Call 112 and stay on the phone. If you are a woman and you are afraid, also call 181. Ask a person you trust to come near you. Kanoon Saathi will wait. Call first. When you are safe, you can speak again.",
        "You may be getting hurt, or someone is forcing their way in. That is an emergency.",
        [
            step("Call 112", "Say where you are, what is happening, and whether you need the police or an ambulance."),
            step("Call 181 if you are a woman in danger", "Tell them if you are afraid for someone to come to the house, and ask what help they can give on the phone."),
            step("Move toward people", "A neighbour, a shop, or a family member you trust. Leave the argument."),
        ],
    ),
    "land": guide(
        "soon",
        "Someone is using your land",
        "If a neighbour is using your land without your permission, this can be serious. If they are hitting you or threatening you right now, call 112. Do not sign a paper, a blank page, or put your thumb impression. Ask someone you trust to write the date, what happened, and who saw it. Keep photos of the land, any new wall, and any crop they planted. Keep your old papers safe. {where} At the tehsil office, ask whose name is on the land record. Take a person you trust. Free legal help sits at the district court. Ask how soon you must file to stop new building. Waiting can make it harder.",
        "Using your land without permission can be a land-record problem and a civil court problem. It can also be a police matter if there was force or a threat. Which form and which office apply depends on your state.",
        [
            step("Do not sign anything", "No thumb impression on a blank page. No paper you have not heard, read aloud, in words you understand."),
            step("Keep a record of what happened", "Date, time, what they built or planted, and the names of people who saw it. Photos help."),
            step("Keep your old land papers", "The paper that shows the land in your name. People call it khata, khatauni, patta, 7/12, pahani, or RTC. The name changes with the state."),
            step("Ask the revenue office", "{where} Ask them to show the owner's name. Ask for a copy if they allow it."),
            step("Ask for a free lawyer", "District Legal Services Authority, at the district court. Ask whether you need a court order to stop construction."),
            step("Do not use force yourself", "A fight can be turned against you. Let the office and the lawyer take the next step."),
        ],
        ["Old land papers, even if incomplete", "Photos of the land and any new building", "Any notice they gave you", "An identity paper, if you have one"],
    ),
    "threat": guide(
        "soon",
        "Someone is threatening you online",
        "If posts or messages are making you afraid, you can get advice before you walk into a police station. If you might be hurt today, call 181 or 112 first. Do not delete the messages. Take screenshots that show the name, the date, and the words. Save the link. After the proof is saved, block the person. Tell one person you trust. You can report from home at cybercrime.gov.in. If money was taken, call 1930. Before you go to a police station, you can call 181 and ask what a complaint involves. A free lawyer at the district court can sit with you and explain it in plain words. You do not have to meet the person who threatened you.",
        "Threats, abuse, and posts that make you afraid can be reported. Saving the proof comes first. You can ask a helpline what a police complaint would involve before you share your whole story at a station.",
        [
            step("If you might be hurt today, call first", "181 if you are a woman and afraid. 112 if someone is coming to harm you."),
            step("Save the proof before you delete anything", "Screenshots with the name, date, and words. The link of the post. A photo of the screen also works if you cannot tap screenshot."),
            step("Then block the person", "On the app where the message came. Tell one person you trust."),
            step("Report from home if you want", "cybercrime.gov.in. For money cheated online, call 1930 quickly."),
            step("Ask what a complaint looks like", "Call 181, or sit with a District Legal Services lawyer, before you decide to give a full statement at a police station."),
        ],
        ["Screenshots and links", "The phone where the messages are, if it is safe to carry", "A person you trust"],
    ),
    "court": guide(
        "soon",
        "This looks like a court paper",
        "A court paper usually has a date. Missing that date can hurt your side. Do not ignore it because you are afraid or because you cannot read it. Ask someone you trust to read the date aloud. Take the paper to the free lawyer at the district court before that date. Do not sign a reply you do not understand. The lawyer can tell you what the other person is asking.",
        "Court papers ask you to appear or to answer. The date on the paper matters. A free legal-aid lawyer can read it with you.",
        [
            step("Find the date", "Ask someone to point to the date you must go, or the date a reply is due."),
            step("Go before that date", "District Legal Services Authority, at the district court. Carry the paper and any old papers about the same matter."),
            step("Do not sign a reply yet", "A reply can accept things you do not mean. Hear it in your language first."),
        ],
        ["The court paper", "The envelope, if you still have it", "Old papers about the same land, house, or dispute"],
        ["Which date do I have to follow?", "Who filed this?", "What do they want from me?", "What happens if I reach after the date?"],
    ),
    "bill": guide(
        "learn",
        "This is a bill, not a sale of your house",
        "An electricity or water bill asks you to pay for what was used. It is not a paper that sells your house or your land. Check the name, the address, the meter number, the amount, and the last date to pay. If the amount looks wrong, ask the electricity office for a fresh meter reading before you pay a very large sum. A disconnection notice should not be ignored. Ask someone to read the last date aloud. Signing a bill to say you received it is different from signing a form that changes whose name is on the meter.",
        "A bill is a demand for money for a service. A notice can warn that the supply will stop. Neither one, by itself, transfers your house.",
        [
            step("Hear five things", "Name, address, meter or consumer number, amount, and the last date to pay."),
            step("Compare with an old bill", "If you have one. A sudden very large amount is a reason to ask for a reading, not a reason to sign a new form."),
            step("Ask the office if the amount looks wrong", "Take the bill. Ask them to explain the units. Take a person who can read."),
            step("Keep disconnection dates", "If the paper says the supply will stop, ask a lawyer or the office what to do before that date."),
        ],
        ["This bill", "An older bill, if you have one", "The meter number written from the meter itself"],
        ["Is my name spelled right?", "Is this my meter number?", "What is the last date?", "Does any line change the name on the connection?", "Are there blank spaces near the signature?"],
    ),
    "identity": guide(
        "learn",
        "This shows who you are. It does not sell your land.",
        "Aadhaar, a voter card, a ration card, or PAN shows your name. It does not sell your house or your land. Do not give the original to a neighbour, an agent, or a person promising a scheme. A thumb impression on a form that comes with the card can give away money or land. Ask someone you trust to read every attached page aloud. If you hear land, a loan, a blank line, or a signature, take it to the free lawyer at the district court before you sign. You can cover the number when you only need to show the card.",
        "An identity card proves your name. A form given with it can ask for much more. Those are two different papers.",
        [
            step("Keep the original with you", "Give a photocopy only when an office asks, and watch what they do with it."),
            step("Hear every page that came with it", "Land, a loan, money, a blank line, or a thumb impression means stop."),
            step("Ask legal aid before you sign that form", "District Legal Services Authority. Ask what you give up if you sign."),
        ],
        ["The card", "Every page that was given with it", "A person you trust who is not asking you to sign"],
        ["Is this only to prove my name?", "Does any line mention land, a loan, or money?", "Are there blank spaces?", "Who keeps the original?"],
    ),
    "paper": guide(
        "soon",
        "Hear the paper before you sign",
        "Do not sign yet. Ask someone you trust to read the whole paper aloud, slowly. Listen for your name, the land or house, any money, and any line that says you give something up. Blank spaces near a signature are a reason to stop. A thumb impression is the same as a signature. If the paper gives away land, money, a house, or a court case, a free lawyer at the district court should read it before you sign. You can say: I will answer after a lawyer has read this.",
        "A signature or a thumb impression can agree to what is written, including blank spaces that someone else fills later.",
        [
            step("Get it read aloud", "In your language. The reader should not be the person who is asking you to sign, if you can help it."),
            step("Stop if these appear", "Your land, your house, a court case you are dropping, a large sum, or a blank space."),
            step("Take it to legal aid", "District Legal Services Authority. Ask: what do I lose if I sign, and what happens if I wait?"),
        ],
        ["The full paper, every page", "Your old papers about the same property", "A person you trust who is not asking you to sign"],
        ["Is my name right?", "Which land or house is this?", "How much money?", "Do I give up a claim or a case?", "Are there blank lines?", "Who keeps the original?"],
    ),
    "general": guide(
        "learn",
        "Tell me what happened",
        "I can tell you the first steps in plain words. I am not your lawyer. Say what happened, which state you are in, and whether you are safe today. If someone is hurting you now, call 112. If you are a woman and you are afraid, call 181. You can also show a photo of the paper. For land, threats, a court date, a bill, or an identity card, say it in one or two sentences.",
        "Kanoon Saathi explains options and papers before you go to a lawyer or the police. It does not file a case and it does not decide whether you should sign.",
        [
            step("Say if you are safe today", "Danger today means call 112 or 181 before anything else."),
            step("Say what happened, in any words", "Land, a threat, a bill, a court paper, or an identity card. Your state matters for land."),
            step("Or show the paper", "A photo of every page. Have it read aloud before you sign."),
        ],
    ),
}
