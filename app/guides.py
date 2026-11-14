"""Plain-language guides for the situations Kanoon Saathi can explain without a model.

These are starting points for India. They name offices and helplines. They do not
invent section numbers, and they do not tell a person to sign.
"""

from __future__ import annotations

import re

DISCLAIMER = {
    "hi": (
        "कानून साथी वकील नहीं है और आपका मामला तय नहीं करता। "
        "कानून राज्य के हिसाब से बदलता है। दस्तखत या अंगूठा लगाने से पहले "
        "ज़िला कानूनी सहायता के वकील से कागज़ पढ़वाइए।"
    ),
    "en": (
        "Kanoon Saathi is not a lawyer and does not decide your case. "
        "The law depends on your state. Before you sign or give a thumb impression, "
        "ask a District Legal Services Authority lawyer to read the paper."
    ),
}

HELP = {
    "hi": [
        {
            "name": "आपातकाल",
            "phone": "112",
            "url": None,
            "note": "मारपीट, घुसपैठ, या अभी का खतरा। पुलिस और एम्बुलेंस।",
        },
        {
            "name": "महिला हेल्पलाइन",
            "phone": "181",
            "url": None,
            "note": "धमकी, हिंसा, या डर। फ़ोन पर बात हो सकती है।",
        },
        {
            "name": "साइबर क्राइम हेल्पलाइन",
            "phone": "1930",
            "url": "https://cybercrime.gov.in",
            "note": "ऑनलाइन धोखा या पैसे। शिकायत घर से cybercrime.gov.in पर भी होती है।",
        },
        {
            "name": "मुफ़्त कानूनी सहायता",
            "phone": None,
            "url": "https://nalsa.gov.in",
            "note": "ज़िला अदालत में District Legal Services Authority। कॉमन सर्विस सेंटर पर Tele-Law भी पूछिए।",
        },
    ],
    "en": [
        {
            "name": "Emergency",
            "phone": "112",
            "url": None,
            "note": "Violence, a break-in, or danger today. Police and ambulance.",
        },
        {
            "name": "Women helpline",
            "phone": "181",
            "url": None,
            "note": "Threats, violence, or fear. You can talk on the phone.",
        },
        {
            "name": "Cyber crime helpline",
            "phone": "1930",
            "url": "https://cybercrime.gov.in",
            "note": "Online cheating or money. You can also report from home at cybercrime.gov.in.",
        },
        {
            "name": "Free legal help",
            "phone": None,
            "url": "https://nalsa.gov.in",
            "note": "District Legal Services Authority, at the district court. You can also ask for Tele-Law at a Common Service Centre.",
        },
    ],
}

EMERGENCY = re.compile(
    "|".join(
        [
            r"\bkill(?:ing|ed)?\b",
            r"\brape[d]?\b",
            r"\bacid\b",
            r"beating me",
            r"breaking (?:the |my )?door",
            r"बलात्कार",
            r"रेप",
            r"एसिड",
            r"मार डाल",
            r"जान से मार",
            r"पीट रहा",
            r"पीट रही",
            r"अभी मार",
            r"दरवाजा तोड़",
            r"दरवाज़ा तोड़",
        ]
    ),
    re.IGNORECASE,
)


def language_key(language: str) -> str:
    code = (language or "hi-IN").lower()
    if code.startswith("en"):
        return "en"
    return "hi"


def is_emergency(text: str) -> bool:
    return bool(EMERGENCY.search(text or ""))


def _pack(lang: str, *, urgency: str, title: str, spoken: str, what: str, steps: list, bring: list, checks: list | None = None, source: str = "guide") -> dict:
    return {
        "urgency": urgency,
        "title": title,
        "spoken": spoken,
        "what_this_is": what,
        "steps": steps,
        "checks": checks or [],
        "bring": bring,
        "help": HELP[lang],
        "disclaimer": DISCLAIMER[lang],
        "source": source,
        "answered_in": "en-IN" if lang == "en" else "hi-IN",
    }


def emergency_guide(language: str) -> dict:
    lang = language_key(language)
    if lang == "en":
        return _pack(
            lang,
            urgency="now",
            title="Call for help now",
            spoken=(
                "This sounds dangerous right now. Call 112 and stay on the phone. "
                "If you are a woman and you are afraid, also call 181. "
                "Ask a person you trust to come near you. "
                "Kanoon Saathi will wait. Call first. When you are safe, you can speak again."
            ),
            what="You may be getting hurt, or someone is forcing their way in. That is an emergency.",
            steps=[
                {"title": "Call 112", "detail": "Say where you are, what is happening, and whether you need the police or an ambulance."},
                {"title": "Call 181 if you are a woman in danger", "detail": "Tell them if you are afraid for someone to come to the house, and ask what help they can give on the phone."},
                {"title": "Move toward people", "detail": "A neighbour, a shop, or a family member you trust. Leave the argument."},
            ],
            bring=[],
        )
    return _pack(
        lang,
        urgency="now",
        title="अभी मदद लीजिए",
        spoken=(
            "अभी खतरा लग रहा है। 112 पर कॉल कीजिए और फ़ोन रखिए मत। "
            "अगर आप महिला हैं और डर लग रहा है, तो 181 पर भी कॉल कीजिए। "
            "किसी भरोसेमंद व्यक्ति को पास बुलाइए। "
            "कानून साथी इंतज़ार करेगी। पहले कॉल कीजिए। सुरक्षित होने के बाद फिर बोलिए।"
        ),
        what="आपको चोट लग सकती है, या कोई ज़बरदस्ती अंदर आ रहा है। यह आपातकाल है।",
        steps=[
            {"title": "112 पर कॉल कीजिए", "detail": "बताइए आप कहाँ हैं, क्या हो रहा है, और पुलिस चाहिए या एम्बुलेंस।"},
            {"title": "खतरे में हैं तो 181 पर कॉल कीजिए", "detail": "कहिए कि घर पर किसी को भेजना ठीक है या नहीं। फ़ोन पर क्या मदद मिलेगी, यह पूछिए।"},
            {"title": "लोगों की तरफ़ जाइए", "detail": "पड़ोसी, दुकान, या भरोसे का व्यक्ति। बहस छोड़िए।"},
        ],
        bring=[],
    )


def _topic(text: str) -> str:
    t = (text or "").lower()
    scores = {
        "land": _hits(t, ["जमीन", "ज़मीन", "खेत", "कब्जा", "कब्ज़ा", "encroach", "land", "खसरा", "plot", "पट्टा", "patta", "बिगाड़ा", "घेरा"]),
        "threat": _hits(t, ["धमकी", "threat", "instagram", "facebook", "whatsapp", "सोशल", "blackmail", "ब्लैकमेल", "अश्लील", "morphed", "posts", "पोस्ट", "message", "मैसेज", "photo bhej", "फोटो भेज", "वसूली", "extort", "फिरौती"]),
        "court": _hits(t, ["अदालत", "कोर्ट", "court", "summon", "सम्मन", "वारंट", "warrant", "केस", "case no", "hearing"]),
        "bill": _hits(t, ["बिजली", "electric", "bijli", "bill", "बिल", "meter", "मीटर", "पानी का बिल", "water bill"]),
        "paper": _hits(t, ["दस्तावेज", "कागज", "कागज़", "हस्ताक्षर", "sign", "अंगूठा", "thumb", "रजिस्ट्री", "इकरार", "agreement", "deed", "notice", "नोटिस"]),
    }
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "general"
    return best


def _hits(text: str, words: list[str]) -> int:
    return sum(1 for w in words if w in text)


def rule_guide(text: str, language: str, state: str) -> dict:
    if is_emergency(text):
        return emergency_guide(language)
    topic = _topic(text)
    lang = language_key(language)
    state_name = (state or "").strip()
    if topic == "land":
        return _land(lang, state_name)
    if topic == "threat":
        return _threat(lang)
    if topic == "court":
        return _court(lang)
    if topic == "bill":
        return _bill(lang)
    if topic == "paper":
        return _paper(lang)
    return _general(lang)


def _state_line(lang: str, state_name: str) -> str:
    if not state_name or state_name in {"not-sure", "पता नहीं"}:
        if lang == "en":
            return "Tell the office which state the land is in. The record has a different name in each state."
        return "दफ़्तर में अपना राज्य बताइए। रिकॉर्ड का नाम हर राज्य में अलग होता है।"
    if lang == "en":
        return f"Say that the land is in {state_name}. Ask them to open the record for that state."
    return f"बताइए कि ज़मीन {state_name} में है। उसी राज्य का रिकॉर्ड खुलवाइए।"


def _land(lang: str, state_name: str) -> dict:
    where = _state_line(lang, state_name)
    if lang == "en":
        return _pack(
            lang,
            urgency="soon",
            title="Someone is using your land",
            spoken=(
                "If a neighbour is using your land without your permission, this can be serious. "
                "If they are hitting you or threatening you right now, call 112. "
                "Do not sign a paper, a blank page, or put your thumb impression. "
                "Ask someone you trust to write the date, what happened, and who saw it. "
                "Keep photos of the land, any new wall, and any crop they planted. Keep your old papers safe. "
                f"{where} "
                "At the tehsil office, ask whose name is on the land record. Take a person you trust. "
                "Free legal help sits at the district court. Ask how soon you must file to stop new building. Waiting can make it harder."
            ),
            what=(
                "Using your land without permission can be a land-record problem and a civil court problem. "
                "It can also be a police matter if there was force or a threat. "
                "Which form and which office apply depends on your state."
            ),
            steps=[
                {"title": "Do not sign anything", "detail": "No thumb impression on a blank page. No paper you have not heard, read aloud, in words you understand."},
                {"title": "Keep a record of what happened", "detail": "Date, time, what they built or planted, and the names of people who saw it. Photos help."},
                {"title": "Keep your old land papers", "detail": "The paper that shows the land in your name. People call it khata, khatauni, patta, 7/12, pahani, or RTC. The name changes with the state."},
                {"title": "Ask the revenue office", "detail": where + " Ask them to show the owner's name. Ask for a copy if they allow it."},
                {"title": "Ask for a free lawyer", "detail": "District Legal Services Authority, at the district court. Ask whether you need a court order to stop construction."},
                {"title": "Do not use force yourself", "detail": "A fight can be turned against you. Let the office and the lawyer take the next step."},
            ],
            bring=["Old land papers, even if incomplete", "Photos of the land and any new building", "Any notice they gave you", "An identity paper, if you have one"],
        )
    return _pack(
        lang,
        urgency="soon",
        title="कोई आपकी ज़मीन इस्तेमाल कर रहा है",
        spoken=(
            "अगर पड़ोसी आपकी ज़मीन बिना इजाज़त इस्तेमाल कर रहा है, तो यह गंभीर बात हो सकती है। "
            "अभी मार रहा है या धमका रहा है, तो 112 पर कॉल कीजिए। "
            "कोई कागज़, खाली पन्ना, या अंगूठा मत लगाइए। "
            "भरोसे के व्यक्ति से तारीख, क्या हुआ, और किसने देखा, लिखवा लीजिए। "
            "ज़मीन, नई दीवार, और उनकी बोई फसल की फ़ोटो रखिए। पुराने कागज़ संभाल कर रखिए। "
            f"{where} "
            "तहसील दफ़्तर में पूछिए कि रिकॉर्ड में नाम किसका है। साथ में अपना व्यक्ति ले जाइए। "
            "ज़िला अदालत में मुफ़्त वकील मिलता है। पूछिए कि नई इमारत रोकने के लिए कितनी जल्दी अर्ज़ी लगानी है। इंतज़ार से मामला मुश्किल हो सकता है।"
        ),
        what=(
            "बिना इजाज़त ज़मीन पर कब्ज़ा राजस्व रिकॉर्ड का मामला भी हो सकता है और अदालत का भी। "
            "मारपीट या धमकी हुई हो तो पुलिस का मामला भी बन सकता है। "
            "कौन सा फ़ॉर्म और कौन सा दफ़्तर, यह आपके राज्य पर निर्भर है।"
        ),
        steps=[
            {"title": "कुछ भी दस्तखत मत कीजिए", "detail": "खाली पन्ने पर अंगूठा नहीं। जो कागज़ आपकी भाषा में सुनाया न गया हो, उस पर दस्तखत नहीं।"},
            {"title": "जो हुआ वह लिखवाइए", "detail": "तारीख, समय, उन्होंने क्या बनाया या बोया, और देखने वालों के नाम। फ़ोटो काम आती है।"},
            {"title": "पुराने कागज़ संभालिए", "detail": "जिस कागज़ पर ज़मीन आपके नाम है। लोग इसे खाता, खतौनी, पट्टा, 7/12, पाहणी या RTC कहते हैं। नाम राज्य के साथ बदलता है।"},
            {"title": "राजस्व दफ़्तर में पूछिए", "detail": where + " मालिक का नाम दिखाने को कहिए। कॉपी मिले तो ले आइए।"},
            {"title": "मुफ़्त वकील से पूछिए", "detail": "ज़िला अदालत की कानूनी सहायता। नई इमारत रोकने के लिए अदालती आदेश चाहिए या नहीं, यह पूछिए।"},
            {"title": "खुद ताकत मत इस्तेमाल कीजिए", "detail": "मारपीट आपके खिलाफ़ भी हो सकती है। अगला कदम दफ़्तर और वकील उठाएँ।"},
        ],
        bring=["पुराने ज़मीन के कागज़, अधूरे हों तब भी", "ज़मीन और नई इमारत की फ़ोटो", "उन्होंने कोई नोटिस दिया हो तो वह", "पहचान पत्र, अगर हो"],
    )


def _threat(lang: str) -> dict:
    if lang == "en":
        return _pack(
            lang,
            urgency="soon",
            title="Someone is threatening you online",
            spoken=(
                "If posts or messages are making you afraid, you can get advice before you walk into a police station. "
                "If you might be hurt today, call 181 or 112 first. "
                "Do not delete the messages. Take screenshots that show the name, the date, and the words. Save the link. "
                "After the proof is saved, block the person. Tell one person you trust. "
                "You can report from home at cybercrime.gov.in. If money was taken, call 1930. "
                "Before you go to a police station, you can call 181 and ask what a complaint involves. "
                "A free lawyer at the district court can sit with you and explain it in plain words. "
                "You do not have to meet the person who threatened you."
            ),
            what=(
                "Threats, abuse, and posts that make you afraid can be reported. "
                "Saving the proof comes first. You can ask a helpline what a police complaint would involve before you share your whole story at a station."
            ),
            steps=[
                {"title": "If you might be hurt today, call first", "detail": "181 if you are a woman and afraid. 112 if someone is coming to harm you."},
                {"title": "Save the proof before you delete anything", "detail": "Screenshots with the name, date, and words. The link of the post. A photo of the screen also works if you cannot tap screenshot."},
                {"title": "Then block the person", "detail": "On the app where the message came. Tell one person you trust."},
                {"title": "Report from home if you want", "detail": "cybercrime.gov.in. For money cheated online, call 1930 quickly."},
                {"title": "Ask what a complaint looks like", "detail": "Call 181, or sit with a District Legal Services lawyer, before you decide to give a full statement at a police station."},
            ],
            bring=["Screenshots and links", "The phone where the messages are, if it is safe to carry", "A person you trust"],
        )
    return _pack(
        lang,
        urgency="soon",
        title="कोई ऑनलाइन धमकी दे रहा है",
        spoken=(
            "अगर पोस्ट या मैसेज से डर लग रहा है, तो थाने जाने से पहले सलाह ले सकते हैं। "
            "आज चोट लगने का डर हो, तो पहले 181 या 112 पर कॉल कीजिए। "
            "मैसेज मिटाइए मत। नाम, तारीख और शब्द के साथ स्क्रीनशॉट रखिए। लिंक भी सेव कीजिए। "
            "सबूत बचाने के बाद उस व्यक्ति को ब्लॉक कीजिए। एक भरोसेमंद व्यक्ति को बताइए। "
            "घर से cybercrime.gov.in पर शिकायत हो सकती है। पैसे ठगे गए हों तो 1930 पर कॉल कीजिए। "
            "थाने जाने से पहले 181 पर पूछ सकते हैं कि शिकायत में क्या होता है। "
            "ज़िला अदालत का मुफ़्त वकील आपके साथ बैठकर आसान शब्दों में समझा सकता है। "
            "धमकी देने वाले से मिलना ज़रूरी नहीं है।"
        ),
        what=(
            "धमकी, गाली, और डराने वाली पोस्ट की शिकायत हो सकती है। "
            "पहले सबूत बचता है। थाने में पूरी बात बताने से पहले हेल्पलाइन से पूछ सकते हैं कि शिकायत में होता क्या है।"
        ),
        steps=[
            {"title": "आज खतरा हो तो पहले कॉल कीजिए", "detail": "डर हो और आप महिला हैं तो 181। कोई नुकसान पहुँचाने आ रहा हो तो 112।"},
            {"title": "मिटाने से पहले सबूत रखिए", "detail": "नाम, तारीख और शब्द दिखें ऐसा स्क्रीनशॉट। पोस्ट का लिंक। स्क्रीनशॉट न बन पाए तो स्क्रीन की फ़ोटो भी चलती है।"},
            {"title": "फिर ब्लॉक कीजिए", "detail": "जिस ऐप पर मैसेज आया। एक भरोसेमंद व्यक्ति को बताइए।"},
            {"title": "घर से शिकायत हो सकती है", "detail": "cybercrime.gov.in। ऑनलाइन पैसे ठगे गए हों तो जल्दी 1930 पर कॉल कीजिए।"},
            {"title": "शिकायत कैसी होती है, पूछ लीजिए", "detail": "थाने में पूरी बात कहने का फैसला करने से पहले 181 पर बात कीजिए, या ज़िला कानूनी सहायता के वकील के साथ बैठिए।"},
        ],
        bring=["स्क्रीनशॉट और लिंक", "वह फ़ोन जिसमें मैसेज हैं, अगर ले जाना सुरक्षित हो", "एक भरोसेमंद व्यक्ति"],
    )


def _court(lang: str) -> dict:
    if lang == "en":
        return _pack(
            lang,
            urgency="soon",
            title="This looks like a court paper",
            spoken=(
                "A court paper usually has a date. Missing that date can hurt your side. "
                "Do not ignore it because you are afraid or because you cannot read it. "
                "Ask someone you trust to read the date aloud. "
                "Take the paper to the free lawyer at the district court before that date. "
                "Do not sign a reply you do not understand. The lawyer can tell you what the other person is asking."
            ),
            what="Court papers ask you to appear or to answer. The date on the paper matters. A free legal-aid lawyer can read it with you.",
            steps=[
                {"title": "Find the date", "detail": "Ask someone to point to the date you must go, or the date a reply is due."},
                {"title": "Go before that date", "detail": "District Legal Services Authority, at the district court. Carry the paper and any old papers about the same matter."},
                {"title": "Do not sign a reply yet", "detail": "A reply can accept things you do not mean. Hear it in your language first."},
            ],
            bring=["The court paper", "The envelope, if you still have it", "Old papers about the same land, house, or dispute"],
            checks=["Which date do I have to follow?", "Who filed this?", "What do they want from me?", "What happens if I reach after the date?"],
        )
    return _pack(
        lang,
        urgency="soon",
        title="यह अदालत का कागज़ लग रहा है",
        spoken=(
            "अदालत के कागज़ पर अक्सर एक तारीख होती है। वह तारीख छूट गई तो आपके पक्ष को नुकसान हो सकता है। "
            "डर के मारे या पढ़ न पाने के कारण इसे नज़रअंदाज़ मत कीजिए। "
            "भरोसे के व्यक्ति से तारीख ज़ोर से पढ़वाइए। "
            "उस तारीख से पहले कागज़ ज़िला अदालत के मुफ़्त वकील को दिखाइए। "
            "जो जवाब समझ न आए, उस पर दस्तखत मत कीजिए। वकील बताएगा कि दूसरा पक्ष क्या माँग रहा है।"
        ),
        what="अदालत का कागज़ हाज़िर होने या जवाब देने को कहता है। उस पर की तारीख ज़रूरी है। मुफ़्त कानूनी वकील इसे आपके साथ पढ़ सकता है।",
        steps=[
            {"title": "तारीख ढूँढिए", "detail": "किसी से कहिए कि जिस दिन जाना है, या जिस दिन जवाब देना है, वह तारीख उँगली से दिखाये।"},
            {"title": "उस तारीख से पहले जाइए", "detail": "ज़िला अदालत की कानूनी सहायता। यह कागज़ और उसी मामले के पुराने कागज़ ले जाइए।"},
            {"title": "अभी जवाब पर दस्तखत मत कीजिए", "detail": "जवाब में ऐसी बात मान ली जा सकती है जो आप कहना नहीं चाहते। पहले अपनी भाषा में सुनिए।"},
        ],
        bring=["अदालत का कागज़", "लिफ़ाफ़ा, अगर अब भी हो", "उसी ज़मीन, घर, या विवाद के पुराने कागज़"],
        checks=["मुझे कौन सी तारीख माननी है?", "यह किसने लगाया?", "मुझसे क्या माँग रहे हैं?", "तारीख के बाद पहुँची तो क्या होगा?"],
    )


def _bill(lang: str) -> dict:
    if lang == "en":
        return _pack(
            lang,
            urgency="learn",
            title="This is a bill, not a sale of your house",
            spoken=(
                "An electricity or water bill asks you to pay for what was used. "
                "It is not a paper that sells your house or your land. "
                "Check the name, the address, the meter number, the amount, and the last date to pay. "
                "If the amount looks wrong, ask the electricity office for a fresh meter reading before you pay a very large sum. "
                "A disconnection notice should not be ignored. Ask someone to read the last date aloud. "
                "Signing a bill to say you received it is different from signing a form that changes whose name is on the meter."
            ),
            what="A bill is a demand for money for a service. A notice can warn that the supply will stop. Neither one, by itself, transfers your house.",
            steps=[
                {"title": "Hear five things", "detail": "Name, address, meter or consumer number, amount, and the last date to pay."},
                {"title": "Compare with an old bill", "detail": "If you have one. A sudden very large amount is a reason to ask for a reading, not a reason to sign a new form."},
                {"title": "Ask the office if the amount looks wrong", "detail": "Take the bill. Ask them to explain the units. Take a person who can read."},
                {"title": "Keep disconnection dates", "detail": "If the paper says the supply will stop, ask a lawyer or the office what to do before that date."},
            ],
            bring=["This bill", "An older bill, if you have one", "The meter number written from the meter itself"],
            checks=["Is my name spelled right?", "Is this my meter number?", "What is the last date?", "Does any line change the name on the connection?", "Are there blank spaces near the signature?"],
        )
    return _pack(
        lang,
        urgency="learn",
        title="यह बिल है, घर बेचने का कागज़ नहीं",
        spoken=(
            "बिजली या पानी का बिल इस्तेमाल का पैसा माँगता है। "
            "यह वह कागज़ नहीं है जो आपका घर या ज़मीन बेच दे। "
            "नाम, पता, मीटर नंबर, रकम, और आखिरी तारीख सुन लीजिए। "
            "रकम बहुत ज़्यादा लगे तो बड़ी रकम भरने से पहले बिजली दफ़्तर से मीटर दोबारा पढ़ने को कहिए। "
            "कनेक्शन काटने वाली नोटिस को नज़रअंदाज़ मत कीजिए। आखिरी तारीख ज़ोर से पढ़वाइए। "
            "बिल पाने का दस्तखत अलग बात है। मीटर का नाम बदलने वाले फ़ॉर्म पर दस्तखत अलग और बड़ी बात है।"
        ),
        what="बिल सेवा का पैसा माँगता है। नोटिस कह सकती है कि आपूर्ति रुक जाएगी। अकेले इनसे घर का मालिक नहीं बदलता।",
        steps=[
            {"title": "पाँच बातें सुनिए", "detail": "नाम, पता, मीटर या उपभोक्ता नंबर, रकम, और भुगतान की आखिरी तारीख।"},
            {"title": "पुराने बिल से मिलाइए", "detail": "पुराना बिल हो तो। अचानक बहुत बड़ी रकम हो तो नया फ़ॉर्म दस्तखत करने की नहीं, रीडिंग माँगने की बात है।"},
            {"title": "रकम गलत लगे तो दफ़्तर जाइए", "detail": "बिल ले जाइए। यूनिट समझाने को कहिए। पढ़ने वाला व्यक्ति साथ ले जाइए।"},
            {"title": "काटने की तारीख संभालिए", "detail": "कागज़ कहे कि कनेक्शन कटेगा, तो उस तारीख से पहले दफ़्तर या वकील से पूछिए।"},
        ],
        bring=["यह बिल", "पुराना बिल, अगर हो", "मीटर पर लिखा मीटर नंबर"],
        checks=["नाम सही लिखा है?", "मीटर नंबर मेरा है?", "आखिरी तारीख क्या है?", "कोई लाइन कनेक्शन का नाम तो नहीं बदल रही?", "दस्तखत के पास खाली जगह तो नहीं?"],
    )


def _paper(lang: str) -> dict:
    if lang == "en":
        return _pack(
            lang,
            urgency="soon",
            title="Hear the paper before you sign",
            spoken=(
                "Do not sign yet. Ask someone you trust to read the whole paper aloud, slowly. "
                "Listen for your name, the land or house, any money, and any line that says you give something up. "
                "Blank spaces near a signature are a reason to stop. "
                "A thumb impression is the same as a signature. "
                "If the paper gives away land, money, a house, or a court case, a free lawyer at the district court should read it before you sign. "
                "You can say: I will answer after a lawyer has read this."
            ),
            what="A signature or a thumb impression can agree to what is written, including blank spaces that someone else fills later.",
            steps=[
                {"title": "Get it read aloud", "detail": "In your language. The reader should not be the person who is asking you to sign, if you can help it."},
                {"title": "Stop if these appear", "detail": "Your land, your house, a court case you are dropping, a large sum, or a blank space."},
                {"title": "Take it to legal aid", "detail": "District Legal Services Authority. Ask: what do I lose if I sign, and what happens if I wait?"},
            ],
            bring=["The full paper, every page", "Your old papers about the same property", "A person you trust who is not asking you to sign"],
            checks=["Is my name right?", "Which land or house is this?", "How much money?", "Do I give up a claim or a case?", "Are there blank lines?", "Who keeps the original?"],
        )
    return _pack(
        lang,
        urgency="soon",
        title="दस्तखत से पहले कागज़ सुनिए",
        spoken=(
            "अभी दस्तखत मत कीजिए। भरोसे के व्यक्ति से पूरा कागज़ धीरे-धीरे ज़ोर से पढ़वाइए। "
            "अपना नाम सुनिए, ज़मीन या घर सुनिए, पैसा सुनिए, और कोई लाइन जिसमें आप कुछ छोड़ रहे हों। "
            "दस्तखत के पास खाली जगह हो तो रुकिए। "
            "अंगूठा भी दस्तखत जितना ही होता है। "
            "कागज़ ज़मीन, पैसा, घर, या अदालती मामला छोड़ता हो, तो दस्तखत से पहले ज़िला अदालत का मुफ़्त वकील इसे पढ़े। "
            "आप कह सकते हैं: वकील पढ़ लें, उसके बाद जवाब दूँ।"
        ),
        what="दस्तखत या अंगूठा लिखी हुई बात मान लेता है। खाली जगह बाद में कोई और भर सकता है।",
        steps=[
            {"title": "ज़ोर से पढ़वाइए", "detail": "अपनी भाषा में। हो सके तो पढ़ने वाला वह व्यक्ति न हो जो दस्तखत माँग रहा है।"},
            {"title": "ये दिखें तो रुकिए", "detail": "आपकी ज़मीन, आपका घर, कोई केस छोड़ना, बड़ी रकम, या खाली जगह।"},
            {"title": "कानूनी सहायता में ले जाइए", "detail": "ज़िला कानूनी सहायता। पूछिए: दस्तखत से मैं क्या खोऊँगी, और इंतज़ार किया तो क्या होगा?"},
        ],
        bring=["पूरा कागज़, हर पन्ना", "उसी संपत्ति के पुराने कागज़", "भरोसे का व्यक्ति, जो दस्तखत न माँग रहा हो"],
        checks=["नाम सही है?", "कौन सी ज़मीन या घर है?", "कितना पैसा है?", "क्या मैं कोई हक़ या केस छोड़ रही हूँ?", "खाली लाइनें हैं?", "असली कागज़ किसके पास रहेगा?"],
    )


def _general(lang: str) -> dict:
    if lang == "en":
        return _pack(
            lang,
            urgency="learn",
            title="Tell me what happened",
            spoken=(
                "I can tell you the first steps in plain words. I am not your lawyer. "
                "Say what happened, which state you are in, and whether you are safe today. "
                "If someone is hurting you now, call 112. If you are a woman and you are afraid, call 181. "
                "You can also show a photo of the paper. "
                "For land, threats, a court date, or a bill, say it in one or two sentences."
            ),
            what="Kanoon Saathi explains options and papers before you go to a lawyer or the police. It does not file a case and it does not decide whether you should sign.",
            steps=[
                {"title": "Say if you are safe today", "detail": "Danger today means call 112 or 181 before anything else."},
                {"title": "Say what happened, in any words", "detail": "Land, a threat, a bill, or a court paper. Your state matters for land."},
                {"title": "Or show the paper", "detail": "A photo of every page. Have it read aloud before you sign."},
            ],
            bring=[],
        )
    return _pack(
        lang,
        urgency="learn",
        title="बताइए क्या हुआ",
        spoken=(
            "मैं आसान शब्दों में पहले कदम बता सकती हूँ। मैं आपकी वकील नहीं हूँ। "
            "बोलिए क्या हुआ, आप किस राज्य में हैं, और आज आप सुरक्षित हैं या नहीं। "
            "अभी कोई मार रहा हो तो 112 पर कॉल कीजिए। आप महिला हैं और डर लग रहा है तो 181 पर कॉल कीजिए। "
            "कागज़ की फ़ोटो भी दिखा सकते हैं। "
            "ज़मीन, धमकी, अदालत की तारीख, या बिल हो तो एक-दो वाक्यों में कहिए।"
        ),
        what="कानून साथी वकील या पुलिस के पास जाने से पहले रास्ते और कागज़ समझाती है। यह केस दर्ज नहीं करती और यह नहीं कहती कि दस्तखत कर दीजिए।",
        steps=[
            {"title": "बताइए आज सुरक्षित हैं या नहीं", "detail": "आज खतरा हो तो बाकी बात से पहले 112 या 181।"},
            {"title": "जो हुआ वह अपने शब्दों में कहिए", "detail": "ज़मीन, धमकी, बिल, या अदालत का कागज़। ज़मीन के लिए राज्य ज़रूरी है।"},
            {"title": "या कागज़ दिखाइए", "detail": "हर पन्ने की फ़ोटो। दस्तखत से पहले ज़ोर से सुनिए।"},
        ],
        bring=[],
    )


def document_without_reader(language: str) -> dict:
    """Used when a photo arrives and no vision model is configured."""
    guide = _paper(language_key(language))
    if language_key(language) == "en":
        guide["title"] = "I need the model key to read this photo"
        guide["spoken"] = (
            "The photo is not saved. I cannot read the words in the picture until a language-model key is added. "
            "Until then, ask someone you trust to read it aloud, or tell me: who sent it, does it ask for money, and does it ask for a signature. "
            + guide["spoken"]
        )
    else:
        guide["title"] = "इस फ़ोटो को पढ़ने के लिए मॉडल की चाबी चाहिए"
        guide["spoken"] = (
            "फ़ोटो सेव नहीं हुई। चित्र के शब्द मैं तभी पढ़ सकती हूँ जब भाषा मॉडल की चाबी लगी हो। "
            "तब तक भरोसे के व्यक्ति से कागज़ ज़ोर से पढ़वाइए, या मुझे बताइए: किसने भेजा, पैसे माँगे हैं या नहीं, और दस्तखत माँगे हैं या नहीं। "
            + guide["spoken"]
        )
    guide["source"] = "guide"
    return guide
