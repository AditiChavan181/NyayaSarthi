"""Plain-language guides for Kanoon Saathi across all supported Indian languages.

These are starting points for vulnerable and illiterate citizens, farmers, and women.
They name official helplines and legal aid offices (DLSA, 112, 181, 1930, cybercrime.gov.in).
They never tell a person to sign, and they warn against signing blank pages or unread papers.
"""

from __future__ import annotations

import re
from typing import Any

from app.locales import bn, en, gu, hi, kn, ml, mr, pa, ta, te

LOCALES: dict[str, dict[str, Any]] = {
    "hi": hi.DATA,
    "en": en.DATA,
    "ta": ta.DATA,
    "te": te.DATA,
    "kn": kn.DATA,
    "ml": ml.DATA,
    "mr": mr.DATA,
    "pa": pa.DATA,
    "bn": bn.DATA,
    "gu": gu.DATA,
}

DISCLAIMER: dict[str, str] = {k: LOCALES[k]["disclaimer"] for k in LOCALES}
HELP: dict[str, list[dict[str, Any]]] = {k: LOCALES[k]["help"] for k in LOCALES}

EMERGENCY = re.compile(
    "|".join(
        [
            r"\bkill(?:ing|ed)?\b",
            r"\bmurder\b",
            r"\brape[d]?\b",
            r"\bacid\b",
            r"beating me",
            r"attack(?:ing|ed)?",
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
            # Bengali
            r"মেরে ফেল",
            r"খুন",
            r"মারধর",
            r"ধর্ষণ",
            r"দরজা ভাঙ",
            # Gujarati
            r"મારી નાખ",
            r"હુમલો",
            r"હત્યા",
            r"બળાત્કાર",
            r"દરવાજો તોડ",
            # Tamil
            r"கொலை",
            r"தாக்குதல்",
            r"கற்பழிப்பு",
            r"கதவை உடை",
            # Telugu
            r"చంపుతా",
            r"దాడి",
            r"హత్య",
            r"కొడుతున్నారు",
            # Kannada
            r"ಕೊಲ್ಲುತ್ತ",
            r"ಹಲ್ಲೆ",
            r"ಬಡಿಯುತ್ತ",
            r"ಕೊಲೆ",
            # Malayalam
            r"കൊല്ലും",
            r"ആക്രമണം",
            r"തല്ലുന്നു",
            # Marathi
            r"मारून टाक",
            r"हल्ला",
            r"मारहाण",
            r"जीव घे",
            # Punjabi
            r"ਜਾਨੋਂ ਮਾਰ",
            r"ਕੁੱਟ ਰਹੇ",
            r"ਹਮਲਾ",
        ]
    ),
    re.IGNORECASE,
)


def language_key(language: str) -> str:
    code = (language or "hi-IN").strip().lower()
    prefix = code[:2]
    if prefix in LOCALES:
        return prefix
    return "hi"


def is_emergency(text: str) -> bool:
    return bool(EMERGENCY.search(text or ""))


def _where_line(lang_data: dict[str, Any], state_name: str) -> str:
    cleaned = (state_name or "").strip()
    if not cleaned or cleaned.lower() in {"not sure", "not-sure", "पता नहीं"}:
        return str(lang_data.get("state_unknown", ""))
    return str(lang_data.get("state_known", "")).format(state=cleaned)


def _pack(
    lang_code: str,
    full_language: str,
    guide_dict: dict[str, Any],
    state_name: str = "",
    source: str = "guide",
) -> dict[str, Any]:
    lang_data = LOCALES.get(lang_code, LOCALES["hi"])
    where = _where_line(lang_data, state_name)

    spoken_raw = str(guide_dict.get("spoken", ""))
    spoken = spoken_raw.format(where=where) if "{where}" in spoken_raw else spoken_raw

    steps = []
    for s in guide_dict.get("steps", []):
        detail_raw = str(s.get("detail", ""))
        detail = detail_raw.format(where=where) if "{where}" in detail_raw else detail_raw
        steps.append({"title": str(s.get("title", "")), "detail": detail})

    return {
        "urgency": guide_dict.get("urgency", "soon"),
        "title": guide_dict.get("title", ""),
        "spoken": spoken,
        "what_this_is": guide_dict.get("what", ""),
        "steps": steps,
        "checks": list(guide_dict.get("checks", [])),
        "bring": list(guide_dict.get("bring", [])),
        "help": lang_data["help"],
        "disclaimer": lang_data["disclaimer"],
        "source": source,
        "answered_in": full_language or f"{lang_code}-IN",
    }


def emergency_guide(language: str) -> dict[str, Any]:
    lang = language_key(language)
    lang_data = LOCALES.get(lang, LOCALES["hi"])
    return _pack(lang, language, lang_data["emergency"], source="emergency")


def _hits(text: str, words: list[str]) -> int:
    return sum(1 for w in words if w in text)


def _topic(text: str) -> str:
    t = (text or "").lower()
    scores = {
        "land": _hits(
            t,
            [
                # English
                "land", "farmer", "agriculture", "crop", "field", "plot", "boundary",
                "encroach", "illegal occupation", "wall", "patta", "survey", "acres", "bigha",
                # Hindi
                "जमीन", "ज़मीन", "खेत", "किसान", "कब्जा", "कब्ज़ा", "अतिक्रमण", "खसरा", "खतौनी",
                "पट्टा", "बिगाड़ा", "घेरा", "मेढ़", "सीमा", "फसल", "बोया", "दीवार",
                # Bengali
                "জমি", "খামার", "চাষ", "মাঠ", "জমি দখল", "দখল", "খতিয়ান", "পর্চা", "পাট্টা", "সীমানা", "তোলা",
                # Gujarati
                "જમીન", "ખેડૂત", "ખેતર", "કબ્જો", "ગેરકાયદે", "પાક", "દીવાલ", "૭/૧૨", "૮-અ", "હકપત્રક", "ખંડણી",
                # Tamil
                "நிலம்", "விவசாயி", "வயல்", "ஆக்கிரமிப்பு", "பயிர்", "சுவர்", "பட்டா", "சிட்டா", "அடங்கல்",
                # Telugu
                "భూమి", "రైతు", "పొలం", "కబ్జా", "ఆక్రమణ", "పంట", "గోడ", "పట్టా", "అడంగల్", "సర్వే",
                # Kannada
                "ಭೂಮಿ", "ರೈತ", "ಹೊಲ", "ಕಬ್ಜಾ", "ಅತಿಕ್ರಮಣ", "ಬೆಳೆ", "ಗೋಡೆ", "ಖಾತೆ", "ಪಹಣಿ", "ಆರ್ಟಿಸಿ",
                # Malayalam
                "ഭൂമി", "കർഷകൻ", "വയൽ", "കൈയേറ്റം", "കബ്സ", "വിള", "മതിൽ", "പട്ടയം",
                # Marathi
                "जमीन", "शेतकरी", "शेत", "ताबा", "कब्जा", "अतिक्रमण", "पीक", "भिंत", "७/१२", "आठ अ",
                # Punjabi
                "ਜ਼ਮੀਨ", "ਕਿਸਾਨ", "ਖੇਤ", "ਕਬਜ਼ਾ", "ਧੱਕਾ", "ਕੰਧ", "ਫ਼ਸਲ", "ਪਟਵਾਰੀ", "ਜਮ੍ਹਾਂਬੰਦੀ",
            ],
        ),
        "threat": _hits(
            t,
            [
                # English
                "threat", "extort", "extortion", "blackmail", "intimidat", "harass", "money demand",
                "ransom", "social media", "instagram", "facebook", "whatsapp", "photo", "video",
                "morphed", "posts", "leak", "viral", "abusive", "cyber", "scared", "fear",
                # Hindi
                "धमकी", "वसूली", "हफ्ता", "रंगदारी", "ब्लैकमेल", "पैसे मांग", "सोशल", "पोस्ट",
                "मैसेज", "फोटो भेज", "वीडियो", "वायरल", "बदनाम", "अश्लील", "डरा", "सहमी", "डर",
                # Bengali
                "হুমকি", "তোলা", "তোলাবাজি", "ব্ল্যাকমেল", "টাকা দাবি", "সোশ্যাল মিডিয়া", "পোস্ট", "ভিডিও", "ছবি", "ভয়", "ব্লাকমেইল",
                # Gujarati
                "ધમકી", "ખંડણી", "બ્લેકમેઇલ", "પૈસા માંગે", "સોશિયલ મીડિયા", "પોસ્ટ", "ફોટો", "વિડિયો", "ડર", "હેરાન",
                # Tamil
                "மிரட்டல்", "பணம் பறித்தல்", "பயமுறுத்தல்", "வலைத்தளம்", "சமூக ஊடகம்", "பதிவு", "படம்", "பயம்", "தொல்லை",
                # Telugu
                "బెదిరింపు", "దోపిడీ", "బ్లాక్‌మెయిల్", "డబ్బు అడుగు", "సోషల్ మీడియా", "పోస్ట్", "వీడియో", "భయం",
                # Kannada
                "ಬೆದರಿಕೆ", "ಸುಲಿಗೆ", "ಬ್ಲಾಕ್‌ಮೇಲ್", "ಹಣ ಕೇಳು", "ಸಾಮಾಜಿಕ ಜಾಲತಾಣ", "ಪೋಸ್ಟ್", "ವೀಡಿಯೋ", "ಹೆದರಿಕೆ",
                # Malayalam
                "ഭീഷണി", "ബ്ലാക്ക്മെയിൽ", "പണം ചോദിച്ചു", "സോഷ്യൽ മീഡിയ", "പോസ്റ്റ്", "ഫോട്ടോ", "പേടി",
                # Marathi
                "धमकी", "खंडणी", "वसुली", "ब्लॅकमेल", "पैसे मागत", "सोशल मीडिया", "पोस्ट", "फोटो", "भीती",
                # Punjabi
                "ਧਮਕੀ", "ਫਿਰੌਤੀ", "ਉਗਰਾਹੀ", "ਬਲੈਕਮੇਲ", "ਪੈਸੇ ਮੰਗ", "ਸੋਸ਼ਲ ਮੀਡੀਆ", "ਪੋਸਟ", "ਵੀਡੀਓ", "ਡਰ",
            ],
        ),
        "court": _hits(
            t,
            [
                # English
                "court", "summon", "warrant", "case", "hearing", "judge", "peshi", "date",
                "lawyer", "order", "legal notice", "vakalatnama", "injunction", "stay order",
                # Hindi
                "अदालत", "कोर्ट", "सम्मन", "वारंट", "केस", "मुकदमा", "तारीख", "पेशी", "सुनवाई", "आदेश", "नोटिस",
                # Bengali
                "আদালত", "কোর্ট", "সমন", "ওয়ারেন্ট", "মামলা", "তারিখ", "শুনানি", "আইনি নোটিশ", "হাজিরা",
                # Gujarati
                "અદાલત", "કોર્ટ", "સમન્સ", "વોરન્ટ", "કેસ", "તારીખ", "મુદત", "સુનાવણી", "હુકમ",
                # Tamil
                "நீதிமன்றம்", "கோர்ட்", "சமன்ஸ்", "வாரண்ட்", "வழக்கு", "தேதி", "விசாரணை", "நோட்டீஸ்",
                # Telugu
                "కోర్టు", "సమన్స్", "వారెంట్", "కేసు", "తేదీ", "విచారణ", "నోటీసు",
                # Kannada
                "ನ್ಯಾಯಾಲಯ", "ಕೋರ್ಟ್", "ಸಮನ್ಸ್", "ವಾರಂಟ್", "ಪ್ರಕರಣ", "ದಿನಾಂಕ", "ವಿಚಾರಣೆ", "ನೋಟಿಸ್",
                # Malayalam
                "കോടതി", "സമ്മൻസ്", "വാറണ്ട്", "കേസ്", "തീയതി", "വിചാരണ", "നോട്ടീസ്",
                # Marathi
                "न्यायालय", "कोर्ट", "समन्स", "वारंट", "केस", "तारीख", "मुदत", "सुनावणी", "नोटीस",
                # Punjabi
                "ਅਦਾਲਤ", "ਕੋਰਟ", "ਸੰਮਨ", "ਵਾਰੰਟ", "ਕੇਸ", "ਤਾਰੀਖ਼", "ਪੇਸ਼ੀ", "ਸੁਣਵਾਈ", "ਨੋਟਿਸ",
            ],
        ),
        "bill": _hits(
            t,
            [
                # English
                "bill", "electric", "electricity", "power", "meter", "current", "units",
                "water bill", "disconnection", "due date", "consumer number", "discom", "eb bill",
                # Hindi
                "बिजली", "मीटर", "बिल", "यूनिट", "पानी का बिल", "कनेक्शन", "काटने", "उपभोक्ता", "रीडिंग",
                # Bengali
                "বিদ্যুৎ", "কারেন্ট", "বিল", "মিটার", "পানির বিল", "সংযোগ বিচ্ছিন্ন",
                # Gujarati
                "વીજળી", "મીટર", "બિલ", "યુનિટ", "પાણીનું બિલ", "જોડાણ કાપવા", "ગ્રાહક નંબર",
                # Tamil
                "மின்சாரம்", "மின் கட்டணம்", "மீட்டர்", "பில்", "துண்டிப்பு", "தண்ணீர் கட்டணம்",
                # Telugu
                "విద్యుత్", "కరెంట్ బిల్లు", "మీటర్", "బిల్లు", "నీటి బిల్లు", "కనెక్షన్ తొలగింపు",
                # Kannada
                "ವಿದ್ಯುತ್", "ಕರೆಂಟ್ ಬಿಲ್", "ಮೀಟರ್", "ಬಿಲ್ಲು", "ನೀರಿನ ಬಿಲ್", "ಸಂಪರ್ಕ ಕಡಿತ",
                # Malayalam
                "വൈദ്യുതി", "കറന്റ് ബിൽ", "മീറ്റർ", "ബിൽ", "വെള്ളക്കരം", "കണക്ഷൻ വിച്ഛേദിക്കൽ",
                # Marathi
                "वीज", "मीटर", "बिल", "पाणी बिल", "कनेक्शन कापणे", "ग्राहक क्रमांक",
                # Punjabi
                "ਬਿਜਲੀ", "ਮੀਟਰ", "ਬਿੱਲ", "ਪਾਣੀ ਦਾ ਬਿੱਲ", "ਕੁਨੈਕਸ਼ਨ ਕੱਟਣ",
            ],
        ),
        "identity": _hits(
            t,
            [
                # English
                "aadhaar", "aadhar", "voter id", "ration card", "pan card", "identity card", "id proof",
                # Hindi
                "आधार", "वोटर कार्ड", "राशन कार्ड", "पैन कार्ड", "पहचान पत्र", "पहचान कार्ड",
                # Regional
                "আধার", "ভোটার কার্ড", "রেশন কার্ড", "આધાર કાર્ડ", "ચૂંટણી કાર્ડ", "રેશનકાર્ડ",
                "ஆதார்", "வாக்காளர் அட்டை", "ரேஷன் அட்டை", "ఆధార్", "ఓటరు కార్డు", "రేషన్ కార్డు",
                "ಆಧಾರ್", "ಮತದಾರರ ಗುರುತಿನ ಚೀಟಿ", "ರೇಷನ್ ಕಾರ್ಡ್", "ആധാർ", "റേഷൻ കാർഡ്",
            ],
        ),
        "paper": _hits(
            t,
            [
                # English
                "paper", "document", "agreement", "sign", "signature", "thumb impression",
                "stamp paper", "affidavit", "registry", "contract", "deed", "bond", "blank paper",
                # Hindi
                "कागज", "कागज़", "दस्तावेज", "हस्ताक्षर", "दस्तखत", "अंगूठा", "साइन", "सहमति",
                "इकरारनामा", "स्टाम्प", "रजिस्ट्री", "सफेद कागज", "खाली पन्ना", "हलफनामा",
                # Bengali
                "দলিল", "কাগজ", "দস্তাবেজ", "সই", "স্বাক্ষর", "টিপসই", "চুক্তি", "স্ট্যাম্প পেপার",
                # Gujarati
                "કાગળ", "દસ્તાવેજ", "સહી", "અંગૂઠો", "કરાર", "સ્ટેમ્પ પેપર", "ખાલી કાગળ",
                # Tamil
                "காகிதம்", "ஆவணம்", "கையெழுத்து", "கட்டைவிரல்", "ஒப்பந்தம்", "பத்திரம்",
                # Telugu
                "కాగితం", "పత్రం", "సంతకం", "వేలిముద్ర", "ఒప్పందం", "బాండ్ పేపర్",
                # Kannada
                "ಕಾಗದ", "ದಾಖಲೆ", "ಸಹಿ", "ಹೆಬ್ಬೆಟ್ಟು", "ಒಪ್ಪಂದ", "ಸ್ಟ್ಯಾಂಪ್ ಪೇಪರ್",
                # Malayalam
                "കടലാസ്", "രേഖ", "കയ്യൊപ്പ്", "വിരലടയാളം", "കരാർ", "മുദ്രപ്പത്രം",
                # Marathi
                "कागद", "दस्तऐवज", "स्वाक्षरी", "सही", "अंगठा", "करारनामा", "स्टॅम्प पेपर",
                # Punjabi
                "ਕਾਗਜ਼", "ਦਸਤਾਵੇਜ਼", "ਦਸਤਖ਼ਤ", "ਅੰਗੂਠਾ", "ਇਕਰਾਰਨਾਮਾ", "ਅਸ਼ਟਾਮ",
            ],
        ),
    }

    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "general"
    return best


def rule_guide(text: str, language: str, state: str) -> dict[str, Any]:
    if is_emergency(text):
        return emergency_guide(language)
    topic = _topic(text)
    lang = language_key(language)
    lang_data = LOCALES.get(lang, LOCALES["hi"])
    guide_dict = lang_data.get(topic, lang_data["general"])
    return _pack(lang, language, guide_dict, state_name=state)


def document_without_reader(language: str, note: str = "") -> dict[str, Any]:
    """Generates comprehensive plain-language guidance for uploaded documents without vision LLM.

    Interprets user notes or falls back to paper/bill/court/identity/land guidance,
    emphasizing whether they should sign, what free DLSA lawyers should check,
    and explaining that utility bills never convey ownership of land or home.
    """
    lang = language_key(language)
    lang_data = LOCALES.get(lang, LOCALES["hi"])

    topic = _topic(note) if note.strip() else "paper"
    if topic not in {"land", "threat", "court", "bill", "identity", "paper"}:
        topic = "paper"

    guide_dict = lang_data.get(topic, lang_data["paper"])
    packed = _pack(lang, language, guide_dict, source="document_guide")

    no_reader = lang_data.get("no_reader", {})
    if no_reader:
        packed["title"] = no_reader.get("title", packed["title"])
        spoken_prefix = no_reader.get("spoken", "")
        if spoken_prefix:
            packed["spoken"] = f"{spoken_prefix} {packed['spoken']}"

    return packed
