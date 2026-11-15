const LANGS = [
  ["hi-IN", "हिन्दी"],
  ["en-IN", "English"],
  ["ta-IN", "தமிழ்"],
  ["te-IN", "తెలుగు"],
  ["kn-IN", "ಕನ್ನಡ"],
  ["ml-IN", "മലയാളം"],
  ["mr-IN", "मराठी"],
  ["pa-IN", "ਪੰਜਾਬੀ"],
  ["bn-IN", "বাংলা"],
  ["gu-IN", "ગુજરાતી"],
];

const STATES = [
  "Not sure",
  "Andhra Pradesh",
  "Arunachal Pradesh",
  "Assam",
  "Bihar",
  "Chhattisgarh",
  "Goa",
  "Gujarat",
  "Haryana",
  "Himachal Pradesh",
  "Jharkhand",
  "Karnataka",
  "Kerala",
  "Madhya Pradesh",
  "Maharashtra",
  "Manipur",
  "Meghalaya",
  "Mizoram",
  "Nagaland",
  "Odisha",
  "Punjab",
  "Rajasthan",
  "Sikkim",
  "Tamil Nadu",
  "Telangana",
  "Tripura",
  "Uttar Pradesh",
  "Uttarakhand",
  "West Bengal",
  "Delhi",
];

const COPY = {
  hi: {
    headline: "बोलिए। पहले रास्ते जानिए।",
    lede: "वकील या पुलिस के पास जाने से पहले, आसान शब्दों में सुनिए कि आपके पास कौन से विकल्प हैं। कागज़ की फ़ोटो भी दिखाइए।",
    lang: "भाषा",
    state: "राज्य",
    mic: "बोलिए",
    stop: "रोकिए",
    hint: "बटन दबाएँ, बात कहें, फिर दोबारा दबाएँ।",
    photo: "कागज़ की फ़ोटो",
    welcome: "पहले सुनिए",
    write: "या यहाँ लिखिए",
    ask: "इसी पर बताइए",
    again: "दोबारा सुनिए",
    slow: "धीमे बोलिए",
    said: "आपने कहा",
    steps: "कदम",
    checks: "दस्तखत से पहले ये सुनिए",
    bring: "साथ ले जाइए",
    privacy: "आपकी फ़ोटो सेव नहीं होती। बातचीत भी सेव नहीं होती। कानून साथी वकील नहीं है।",
    phoneVoice: "इस फ़ोन की आवाज़",
    canReadPaper: "कागज़ पढ़ सकती हूँ",
    noModelKey: "कागज़ की फ़ोटो के लिए मॉडल की चाबी जोड़ें",
    hearError: "आवाज़ समझ नहीं आई। लिख कर पूछिए।",
    tooShort: "बहुत छोटा था। फिर बोलिए।",
    urgency: { now: "अभी कॉल कीजिए", soon: "इस हफ़्ते किसी से मिलिए", learn: "समझने का समय है" },
    welcomeSpeech: "नमस्ते। मैं कानून साथी हूँ। मैं वकील नहीं हूँ। मैं आसान शब्दों में बताती हूँ कि पुलिस या वकील के पास जाने से पहले आपके पास कौन से रास्ते हैं। बोलिए कि क्या हुआ, या कागज़ की फ़ोटो दिखाइए। अगर अभी जान का खतरा है, तो 112 पर कॉल कीजिए।",
    examples: [
      ["पड़ोसी मेरी ज़मीन पर कब्ज़ा कर रहा है", "पड़ोसी मेरी ज़मीन पर जबरन कब्ज़ा कर रहा है और वसूली मांग रहा है"],
      ["कोई सोशल मीडिया पर धमकी दे रहा है", "कोई सोशल मीडिया पर धमकी दे रहा है और पैसे मांग रहा है, मुझे डर लग रहा है"],
      ["बिजली का बिल समझ नहीं आ रहा", "बिजली का बिल समझ नहीं आ रहा। क्या इस पर दस्तखत करना है?"],
    ],
  },
  en: {
    headline: "Speak first. Know your options.",
    lede: "Before you go to a lawyer or the police, hear the choices in plain words. You can also show a photo of a paper.",
    lang: "Language",
    state: "State",
    mic: "Speak",
    stop: "Stop",
    hint: "Tap once, talk, then tap again.",
    photo: "Photo of a paper",
    welcome: "Hear this first",
    write: "Or type here",
    ask: "Explain this",
    again: "Hear again",
    slow: "Speak slower",
    said: "You said",
    steps: "Steps",
    checks: "Hear this before you sign",
    bring: "Carry these",
    privacy: "Your photo is not saved. The conversation is not saved. Kanoon Saathi is not a lawyer.",
    phoneVoice: "This phone's voice",
    canReadPaper: "Can read a paper",
    noModelKey: "Add a model key to read a photo",
    hearError: "I could not hear that. Type it instead.",
    tooShort: "That was too short. Please speak again.",
    urgency: { now: "Call now", soon: "See someone this week", learn: "You have time to understand" },
    welcomeSpeech: "Hello. I am Kanoon Saathi. I am not a lawyer. I explain, in plain words, what you can do before you go to the police or a lawyer. Say what happened, or show a photo of the paper. If you are in danger right now, call 112.",
    examples: [
      ["A neighbour is extorting my land", "My neighbour is illegally occupying my farmland and extorting money from me"],
      ["Threats on social media", "Someone is threatening and blackmailing me on social media, I feel scared to go to police directly"],
      ["I cannot understand this bill", "I cannot understand this electricity bill. Does it ask me to sign away my house?"],
    ],
  },
  ta: {
    headline: "பேசுங்கள். உங்கள் உரிமைகளை அறியுங்கள்.",
    lede: "வழக்கறிஞர் அல்லது காவல்துறையிடம் செல்வதற்கு முன், எளிய சொற்களில் உங்கள் வழிகளைக் கேளுங்கள். காகிதத்தின் படத்தையும் காட்டலாம்.",
    lang: "மொழி",
    state: "மாநிலம்",
    mic: "பேசுங்கள்",
    stop: "நிறுத்துங்கள்",
    hint: "ஒருமுறை அழுத்தவும், பேசவும், பின் மீண்டும் அழுத்தவும்.",
    photo: "காகிதத்தின் படம்",
    welcome: "முதலில் கேளுங்கள்",
    write: "அல்லது இங்கே எழுதுங்கள்",
    ask: "விளக்குங்கள்",
    again: "மீண்டும் கேளுங்கள்",
    slow: "மெதுவாகப் பேசுங்கள்",
    said: "நீங்கள் கூறியது",
    steps: "நடவடிக்கைகள்",
    checks: "கையெழுத்துக்கு முன் இவற்றைச் சரிபாருங்கள்",
    bring: "எடுத்துச் செல்ல வேண்டியவை",
    privacy: "உங்கள் படம் சேமிக்கப்படுவதில்லை. உரையாடலும் சேமிக்கப்படுவதில்லை. கானூன் சாத்தி வழக்கறிஞர் அல்ல.",
    phoneVoice: "தொலைபேசியின் குரல்",
    canReadPaper: "காகிதத்தைப் படிக்க முடியும்",
    noModelKey: "படத்தைப் படிக்க மாதிரி சாவி தேவை",
    hearError: "குரல் புரியவில்லை. எழுதிப் பார்க்கவும்.",
    tooShort: "மிகக் குறுகியது. மீண்டும் பேசவும்.",
    urgency: { now: "இப்போதே அழையுங்கள்", soon: "இந்த வாரம் ஒருவரை சந்தியுங்கள்", learn: "புரிந்துகொள்ள நேரம் உள்ளது" },
    welcomeSpeech: "வணக்கம். நான் கானூன் சாத்தி. நான் வழக்கறிஞர் அல்ல. காவல்துறை அல்லது வழக்கறிஞரிடம் செல்வதற்கு முன் உங்கள் வழிகளை எளிய சொற்களில் விளக்குகிறேன். என்ன நடந்தது என்று சொல்லுங்கள், அல்லது காகிதத்தைக் காட்டுங்கள். இப்போது ஆபத்து என்றால் 112-க்கு அழையுங்கள்.",
    examples: [
      ["பக்கத்து வீட்டுக்காரர் நிலத்தை ஆக்கிரமிக்கிறார்", "பக்கத்து வீட்டுக்காரர் என் விவசாய நிலத்தை ஆக்கிரமித்து மிரட்டுகிறார்"],
      ["சமூக ஊடகத்தில் மிரட்டல்", "சமூக ஊடகத்தில் யாரோ மிரட்டி பணம் பறிக்கிறார்கள், எனக்கு பயமாக இருக்கிறது"],
      ["மின் கட்டணம் அல்லது ஆவணம்", "இந்த ஆவணம் அல்லது மின் கட்டணம் புரியவில்லை. இதில் கையெழுத்திட வேண்டுமா?"],
    ],
  },
  te: {
    headline: "మాట్లాడండి. మీ హక్కులు తెలుసుకోండి.",
    lede: "లాయర్ లేదా పోలీసు వద్దకు వెళ్లేముందు, మీకున్న మార్గాలను సరళమైన మాటల్లో వినండి. కాగితం ఫోటో కూడా చూపించవచ్చు.",
    lang: "భాష",
    state: "రాష్ట్రం",
    mic: "మాట్లాడండి",
    stop: "ఆపండి",
    hint: "బటన్ నొక్కండి, మాట్లాడండి, మళ్లీ నొక్కండి.",
    photo: "కాగితం ఫోటో",
    welcome: "ముందుగా వినండి",
    write: "లేదా ఇక్కడ రాయండి",
    ask: "వివరించండి",
    again: "మళ్లీ వినండి",
    slow: "నెమ్మదిగా చెప్పండి",
    said: "మీరు చెప్పినది",
    steps: "చేయవలసిన పనులు",
    checks: "సంతకం పెట్టేముందు ఇవి సరిచూడండి",
    bring: "తీసుకెళ్లవలసినవి",
    privacy: "మీ ఫోటో భద్రపరచబడదు. సంభాషణ కూడా సేవ్ అవ్వదు. కానూన్ సాథీ లాయర్ కాదు.",
    phoneVoice: "ఫోన్ స్వరం",
    canReadPaper: "కాగితం చదవగలను",
    noModelKey: "ఫోటో చదవడానికి మోడల్ కీ కావాలి",
    hearError: "గొంతు అర్థం కాలేదు. రాసి అడగండి.",
    tooShort: "చాలా చిన్నదిగా ఉంది. మళ్లీ మాట్లాడండి.",
    urgency: { now: "ఇప్పుడే కాల్ చేయండి", soon: "ఈ వారం ఎవరినైనా కలవండి", learn: "అర్థం చేసుకోవడానికి సమయం ఉంది" },
    welcomeSpeech: "నమస్కారం. నేను కానూన్ సాథీని. నేను లాయర్ని కాదు. పోలీసు లేదా లాయర్ వద్దకు వెళ్లేముందు మీకున్న మార్గాలను సులభమైన మాటల్లో వివరిస్తాను. ఏమి జరిగిందో చెప్పండి లేదా కాగితం ఫోటో చూపించండి. ప్రాణాపాయం ఉంటే 112 కి కాల్ చేయండి.",
    examples: [
      ["పొరుగువాడు నా భూమిని కబ్జా చేస్తున్నాడు", "పొరుగువాడు నా వ్యవసాయ భూమిని అక్రమంగా కబ్జా చేసి బెదిరిస్తున్నాడు"],
      ["సోషల్ మీడియాలో బెదిరింపులు", "సోషల్ మీడియాలో ఎవరో బెదిరిస్తూ డబ్బు డిమాండ్ చేస్తున్నారు, నాకు భయంగా ఉంది"],
      ["కరెంట్ బిల్లు లేదా పత్రం", "ఈ కాగితం లేదా కరెంట్ బిల్లు అర్థం కావడం లేదు. దీనిపై సంతకం చేయవచ్చా?"],
    ],
  },
  kn: {
    headline: "ಮಾತನಾಡಿ. ಮೊದಲು ನಿಮ್ಮ ಹಕ್ಕುಗಳನ್ನು ತಿಳಿಯಿರಿ.",
    lede: "ವಕೀಲರು ಅಥವಾ ಪೊಲೀಸರ ಬಳಿ ಹೋಗುವ ಮೊದಲು, ನಿಮ್ಮ ಆಯ್ಕೆಗಳನ್ನು ಸರಳ ಮಾತುಗಳಲ್ಲಿ ಕೇಳಿ. ಕಾಗದದ ಫೋಟೋವನ್ನು ತೋರಿಸಬಹುದು.",
    lang: "ಭಾಷೆ",
    state: "ರಾಜ್ಯ",
    mic: "ಮಾತನಾಡಿ",
    stop: "ನಿಲ್ಲಿಸಿ",
    hint: "ಬಟನ್ ಒತ್ತಿ, ಮಾತನಾಡಿ, ನಂತರ ಮತ್ತೆ ಒತ್ತಿ.",
    photo: "ಕಾಗದದ ಫೋಟೋ",
    welcome: "ಮೊದಲು ಕೇಳಿ",
    write: "ಅಥವಾ ಇಲ್ಲಿ ಬರೆಯಿರಿ",
    ask: "ವಿವರಿಸಿ",
    again: "ಮತ್ತೆ ಕೇಳಿ",
    slow: "ನಿಧಾನವಾಗಿ ಹೇಳಿ",
    said: "ನೀವು ಹೇಳಿದ್ದು",
    steps: "ಕ್ರಮಗಳು",
    checks: "ಸಹಿ ಮಾಡುವ ಮೊದಲು ಇವುಗಳನ್ನು ಕೇಳಿ",
    bring: "ಜೊತೆಯಲ್ಲಿ ಕೊಂಡೊಯ್ಯಿರಿ",
    privacy: "ನಿಮ್ಮ ಫೋಟೋ ಉಳಿಯುವುದಿಲ್ಲ. ಸಂಭಾಷಣೆ ಉಳಿಯುವುದಿಲ್ಲ. ಕಾನೂನ್ ಸಾಥಿ ವಕೀಲರಲ್ಲ.",
    phoneVoice: "ಫೋನ್ ಧ್ವನಿ",
    canReadPaper: "ಕಾಗದ ಓದಬಲ್ಲೆ",
    noModelKey: "ಫೋಟೋ ಓದಲು ಮಾದರಿ ಕೀ ಅಗತ್ಯವಿದೆ",
    hearError: "ಧ್ವನಿ ಅರ್ಥವಾಗಲಿಲ್ಲ. ಬರೆದು ಕೇಳಿ.",
    tooShort: "ತುಂಬಾ ಚಿಕ್ಕದಾಗಿದೆ. ಮತ್ತೆ ಮಾತನಾಡಿ.",
    urgency: { now: "ಈಗಲೇ ಕರೆ ಮಾಡಿ", soon: "ಈ ವಾರ ಯಾರನ್ನಾದರೂ ಭೇಟಿ ಮಾಡಿ", learn: "ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು ಸಮಯವಿದೆ" },
    welcomeSpeech: "ನಮಸ್ಕಾರ. ನಾನು ಕಾನೂನ್ ಸಾಥಿ. ನಾನು ವಕೀಲರಲ್ಲ. ಪೊಲೀಸ್ ಅಥವಾ ವಕೀಲರ ಬಳಿ ಹೋಗುವ ಮೊದಲು ನಿಮ್ಮ ಆಯ್ಕೆಗಳನ್ನು ಸರಳ ಪದಗಳಲ್ಲಿ ವಿವರಿಸುತ್ತೇನೆ. ಏನಾಯಿತು ಎಂದು ಹೇಳಿ, ಅಥವಾ ಕಾಗದದ ಫೋಟೋ ತೋರಿಸಿ. ಅಪಾಯವಿದ್ದರೆ 112 ಕರೆ ಮಾಡಿ.",
    examples: [
      ["ನೆರೆಹೊರೆಯವರು ಭೂಮಿ ಕಬ್ಜಾ ಮಾಡಿದ್ದಾರೆ", "ನೆರೆಹೊರೆಯವರು ನನ್ನ ಜಮೀನು ಅಕ್ರಮವಾಗಿ ಕಬ್ಜಾ ಮಾಡಿ ಸುಲಿಗೆ ಮಾಡುತ್ತಿದ್ದಾರೆ"],
      ["ಸಾಮಾಜಿಕ ಜಾಲತಾಣದಲ್ಲಿ ಬೆದರಿಕೆ", "ಯಾರೋ ಸಾಮಾಜಿಕ ಜಾಲತಾಣದಲ್ಲಿ ಬೆದರಿಕೆ ಹಾಕಿ ಹಣ ಕೇಳುತ್ತಿದ್ದಾರೆ, ನನಗೆ ಭಯವಾಗುತ್ತಿದೆ"],
      ["ಕರೆಂಟ್ ಬಿಲ್ ಅಥವಾ ದಾಖಲೆ", "ಈ ದಾಖಲೆ ಅಥವಾ ಕರೆಂಟ್ ಬಿಲ್ ಅರ್ಥವಾಗುತ್ತಿಲ್ಲ. ನಾನು ಸಹಿ ಮಾಡಬೇಕೆ ಅಥವಾ ಬೇಡವೇ?"],
    ],
  },
  ml: {
    headline: "സംസാരിക്കൂ. നിങ്ങളുടെ അവകാശങ്ങൾ അറിയൂ.",
    lede: "വക്കീലിന്റെയോ പോലീസിന്റെയോ അടുത്ത് പോകുന്നതിന് മുൻപ് നിങ്ങളുടെ വഴികൾ ലളിതമായി കേൾക്കൂ. രേഖകളുടെ ഫോട്ടോയും കാണിക്കാം.",
    lang: "ഭാഷ",
    state: "സംസ്ഥാനം",
    mic: "സംസാരിക്കൂ",
    stop: "നിർത്തൂ",
    hint: "ബട്ടൺ അമർത്തൂ, സംസാരിക്കൂ, വീണ്ടും അമർത്തൂ.",
    photo: "രേഖയുടെ ഫോട്ടോ",
    welcome: "ആദ്യം കേൾക്കൂ",
    write: "അല്ലെങ്കിൽ ഇവിടെ എഴുതൂ",
    ask: "വിശദീകരിക്കൂ",
    again: "വീണ്ടും കേൾക്കൂ",
    slow: "പതുക്കെ പറയൂ",
    said: "നിങ്ങൾ പറഞ്ഞത്",
    steps: "നടപടികൾ",
    checks: "ഒപ്പിടുന്നതിന് മുൻപ് ശ്രദ്ധിക്കേണ്ടവ",
    bring: "കരുതേണ്ട രേഖകൾ",
    privacy: "നിങ്ങളുടെ ഫോട്ടോ സൂക്ഷിക്കില്ല. സംഭാഷണവും സൂക്ഷിക്കില്ല. കാനൂൻ സാഥി വക്കീലല്ല.",
    phoneVoice: "ഫോൺ ശബ്ദം",
    canReadPaper: "രേഖ വായിക്കാം",
    noModelKey: "ഫോട്ടോ വായിക്കാൻ മോഡൽ കീ ചേർക്കൂ",
    hearError: "ശബ്ദം വ്യക്തമായില്ല. ടൈപ്പ് ചെയ്യൂ.",
    tooShort: "വളരെ ചെറുതായിരുന്നു. വീണ്ടും പറയൂ.",
    urgency: { now: "ഉടൻ വിളിക്കൂ", soon: "ഈ ആഴ്ച ആരെയെങ്കിലും കാണൂ", learn: "മനസ്സിലാക്കാൻ സമയമുണ്ട്" },
    welcomeSpeech: "നമസ്കാരം. ഞാൻ കാനൂൻ സാഥി. ഞാൻ വക്കീലല്ല. പോലീസിന്റെയോ വക്കീലിന്റെയോ അടുത്ത് പോകുന്നതിന് മുൻപ് നിങ്ങളുടെ വഴികൾ ലളിതമായി പറഞ്ഞുതരാം. എന്താണ് സംഭവിച്ചതെന്ന് പറയൂ. ജീവന് ഭീഷണിയുണ്ടെങ്കിൽ 112 വിളിക്കൂ.",
    examples: [
      ["അയൽവാസി സ്ഥലം കൈയേറുന്നു", "അയൽവാസി എന്റെ കൃഷിസ്ഥലം അനധികൃതമായി കൈയേറി ഭീഷണിപ്പെടുത്തുന്നു"],
      ["സോഷ്യൽ മീഡിയയിൽ ഭീഷണി", "സോഷ്യൽ മീഡിയയിൽ ആരോ ഭീഷണിപ്പെടുത്തി പണം തട്ടാൻ ശ്രമിക്കുന്നു, പേടിയാകുന്നു"],
      ["കറന്റ് ബില്ലോ രേഖയോ", "ഈ രേഖയോ കറന്റ് ബില്ലോ മനസ്സിലാകുന്നില്ല. ഞാൻ ഇതിൽ ഒപ്പിടണമോ വേണ്ടയോ?"],
    ],
  },
  mr: {
    headline: "बोला. आधी तुमचे मार्ग जाणून घ्या.",
    lede: "वकील किंवा पोलिसांकडे जाण्यापूर्वी तुमचे पर्याय सोप्या शब्दांत ऐका. कागदपत्रांचा फोटोही दाखवू शकता.",
    lang: "भाषा",
    state: "राज्य",
    mic: "बोला",
    stop: "थांबवा",
    hint: "बटन दाबा, बोला, पुन्हा दाबा.",
    photo: "कागदाचा फोटो",
    welcome: "आधी ऐका",
    write: "किंवा येथे लिहा",
    ask: "यावर सांगा",
    again: "पुन्हा ऐका",
    slow: "हळू बोला",
    said: "तुम्ही म्हणालात",
    steps: "पायऱ्या",
    checks: "स्वाक्षरीपूर्वी हे तपासा",
    bring: "सोबत न्या",
    privacy: "तुमचा फोटो सेव्ह होत नाही. संभाषण सेव्ह होत नाही. कानून साथी वकील नाही.",
    phoneVoice: "या फोनचा आवाज",
    canReadPaper: "कागद वाचू शकते",
    noModelKey: "फोटो वाचण्यासाठी मॉडेल की आवश्यक",
    hearError: "आवाज समजला नाही. लिहून विचारा.",
    tooShort: "खूप लहान होते. पुन्हा बोला.",
    urgency: { now: "आत्ताच कॉल करा", soon: "या आठवड्यात कोणालातरी भेटा", learn: "समजून घेण्यास वेळ आहे" },
    welcomeSpeech: "नमस्ते. मी कानून साथी आहे. मी वकील नाही. पोलीस किंवा वकिलांकडे जाण्याआधी तुमच्याकडे कोणते कायदेशीर मार्ग आहेत हे मी सोप्या भाषेत सांगते. काय घडले ते सांगा किंवा कागदाचा फोटो दाखवा. धोका असल्यास 112 वर कॉल करा.",
    examples: [
      ["शेजारी जमिनीवर ताबा मारत आहे", "शेजारी माझ्या शेतीवर बेकायदेशीर ताबा मिळवून खंडणी मागत आहे"],
      ["सोशल मीडियावर धमकी", "सोशल मीडियावर कोणीतरी धमकावून पैसे मागत आहे, मला भीती वाटते"],
      ["कागदपत्र किंवा वीज बिल", "हे कागदपत्र किंवा वीज बिल मला समजत नाही. यावर मी सही करावी का?"],
    ],
  },
  pa: {
    headline: "ਬੋਲੋ। ਪਹਿਲਾਂ ਆਪਣੇ ਰਸਤੇ ਜਾਣੋ।",
    lede: "ਵਕੀਲ ਜਾਂ ਪੁਲਿਸ ਕੋਲ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ, ਸੌਖੇ ਸ਼ਬਦਾਂ ਵਿੱਚ ਸੁਣੋ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਕਿਹੜੇ ਰਾਹ ਹਨ। ਕਾਗਜ਼ ਦੀ ਫ਼ੋਟੋ ਵੀ ਦਿਖਾ ਸਕਦੇ ਹੋ।",
    lang: "ਭਾਸ਼ਾ",
    state: "ਸੂਬਾ",
    mic: "ਬੋਲੋ",
    stop: "ਰੋਕੋ",
    hint: "ਬਟਨ ਦਬਾਓ, ਗੱਲ ਕਰੋ, ਫਿਰ ਦੁਬਾਰਾ ਦਬਾਓ।",
    photo: "ਕਾਗਜ਼ ਦੀ ਫ਼ੋਟੋ",
    welcome: "ਪਹਿਲਾਂ ਸੁਣੋ",
    write: "ਜਾਂ ਇੱਥੇ ਲਿਖੋ",
    ask: "ਇਸ ਬਾਰੇ ਦੱਸੋ",
    again: "ਦੁਬਾਰਾ ਸੁਣੋ",
    slow: "ਹੌਲੀ ਬੋਲੋ",
    said: "ਤੁਸੀਂ ਕਿਹਾ",
    steps: "ਕਦਮ",
    checks: "ਦਸਤਖ਼ਤ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਸੁਣੋ",
    bring: "ਨਾਲ ਲੈ ਕੇ ਜਾਓ",
    privacy: "ਤੁਹਾਡੀ ਫ਼ੋਟੋ ਸੇਵ ਨਹੀਂ ਹੁੰਦੀ। ਗੱਲਬਾਤ ਸੇਵ ਨਹੀਂ ਹੁੰਦੀ। ਕਾਨੂੰਨ ਸਾਥੀ ਵਕੀਲ ਨਹੀਂ ਹੈ।",
    phoneVoice: "ਇਸ ਫ਼ੋਨ ਦੀ ਆਵਾਜ਼",
    canReadPaper: "ਕਾਗਜ਼ ਪੜ੍ਹ ਸਕਦੀ ਹਾਂ",
    noModelKey: "ਫ਼ੋਟੋ ਪੜ੍ਹਨ ਲਈ ਮਾਡਲ ਕੁੰਜੀ ਦੀ ਲੋੜ ਹੈ",
    hearError: "ਆਵਾਜ਼ ਸਮਝ ਨਹੀਂ ਆਈ। ਲਿਖ ਕੇ ਪੁੱਛੋ।",
    tooShort: "ਬਹੁਤ ਛੋਟਾ ਸੀ। ਦੁਬਾਰਾ ਬੋਲੋ।",
    urgency: { now: "ਹੁਣੇ ਕਾਲ ਕਰੋ", soon: "ਇਸ ਹਫ਼ਤੇ ਕਿਸੇ ਨੂੰ ਮਿਲੋ", learn: "ਸਮਝਣ ਦਾ ਸਮਾਂ ਹੈ" },
    welcomeSpeech: "ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ। ਮੈਂ ਕਾਨੂੰਨ ਸਾਥੀ ਹਾਂ। ਮੈਂ ਵਕੀਲ ਨਹੀਂ ਹਾਂ। ਮੈਂ ਸੌਖੇ ਸ਼ਬਦਾਂ ਵਿੱਚ ਦੱਸਦੀ ਹਾਂ ਕਿ ਪੁਲਿਸ ਜਾਂ ਵਕੀਲ ਕੋਲ ਜਾਣ ਤੋਂ ਪਹਿਲਾਂ ਤੁਹਾਡੇ ਕੋਲ ਕਿਹੜੇ ਰਸਤੇ ਹਨ। ਦੱਸੋ ਕੀ ਹੋਇਆ, ਜਾਂ ਕਾਗਜ਼ ਦੀ ਫ਼ੋਟੋ ਦਿਖਾਓ। ਜੇ ਖ਼ਤਰਾ ਹੈ ਤਾਂ 112 'ਤੇ ਕਾਲ ਕਰੋ।",
    examples: [
      ["ਗੁਆਂਢੀ ਮੇਰੀ ਜ਼ਮੀਨ 'ਤੇ ਕਬਜ਼ਾ ਕਰ ਰਿਹਾ ਹੈ", "ਗੁਆਂਢੀ ਮੇਰੀ ਖੇਤੀ ਵਾਲੀ ਜ਼ਮੀਨ 'ਤੇ ਨਾਜਾਇਜ਼ ਕਬਜ਼ਾ ਕਰਕੇ ਫਿਰੌਤੀ ਮੰਗ ਰਿਹਾ ਹੈ"],
      ["ਸੋਸ਼ਲ ਮੀਡੀਆ 'ਤੇ ਧਮਕੀ", "ਕੋਈ ਸੋਸ਼ਲ ਮੀਡੀਆ 'ਤੇ ਧਮਕੀ ਦੇ ਕੇ ਪੈਸੇ ਮੰਗ ਰਿਹਾ ਹੈ, ਮੈਨੂੰ ਡਰ ਲੱਗ ਰਿਹਾ ਹੈ"],
      ["ਦਸਤਾਵੇਜ਼ ਜਾਂ ਬਿਜਲੀ ਦਾ ਬਿੱਲ", "ਇਹ ਕਾਗਜ਼ ਜਾਂ ਬਿਜਲੀ ਦਾ ਬਿੱਲ ਸਮਝ ਨਹੀਂ ਆ ਰਿਹਾ। ਕੀ ਮੈਨੂੰ ਇਸ 'ਤੇ ਦਸਤਖ਼ਤ ਕਰਨੇ ਚਾਹੀਦੇ ਹਨ?"],
    ],
  },
  bn: {
    headline: "বলুন। আগে আপনার পথ জানুন।",
    lede: "উকিল বা পুলিশের কাছে যাওয়ার আগে সহজ ভাষায় শুনুন আপনার কাছে কী কী আইনি বিকল্প আছে। কাগজের ছবিও দেখাতে পারেন।",
    lang: "ভাষা",
    state: "রাজ্য",
    mic: "বলুন",
    stop: "থামান",
    hint: "বোতাম টিপুন, কথা বলুন, আবার বোতাম টিপুন।",
    photo: "কাগজের ছবি",
    welcome: "আগে শুনুন",
    write: "অথবা এখানে লিখুন",
    ask: "এটি ব্যাখ্যা করুন",
    again: "আবার শুনুন",
    slow: "ধীরে বলুন",
    said: "আপনি বলেছেন",
    steps: "পদক্ষেপ",
    checks: "সই করার আগে এগুলো শুনুন",
    bring: "সাথে রাখবেন",
    privacy: "আপনার ছবি সংরক্ষণ করা হয় না। কথোপকথন সংরক্ষণ হয় না। কানুন সাথী উকিল নয়।",
    phoneVoice: "ফোনের কণ্ঠস্বর",
    canReadPaper: "কাগজ পড়তে পারি",
    noModelKey: "ছবি পড়তে মডেল কী যুক্ত করুন",
    hearError: "কণ্ঠস্বর বোঝা যায়নি। লিখে জিজ্ঞাসা করুন।",
    tooShort: "খুব ছোট ছিল। আবার বলুন।",
    urgency: { now: "এখনই কল করুন", soon: "এই সপ্তাহে কারও সাথে দেখা করুন", learn: "বোঝার সময় আছে" },
    welcomeSpeech: "নমস্কার। আমি কানুন সাথী। আমি উকিল নই। পুলিশ বা উকিলের কাছে যাওয়ার আগে আপনার কাছে কী কী পথ আছে তা আমি সহজ ভাষায় বুঝিয়ে দিই। কী হয়েছে বলুন, বা কাগজের ছবি দেখান। তাৎক্ষণিক বিপদ থাকলে ১১২ নম্বরে ফোন করুন।",
    examples: [
      ["প্রতিবেশী জমি দখল করছে", "প্রতিবেশী আমার চাষের জমি দখল করে তোলা আদায় করছে"],
      ["সোশ্যাল মিডিয়ায় হুমকি", "সোশ্যাল মিডিয়ায় কেউ হুমকি দিয়ে ব্ল্যাকমেল করছে, আমি ভয় পাচ্ছি"],
      ["দলিল বা বিদ্যুৎ বিল", "এই দলিল বা বিদ্যুৎ বিল বুঝতে পারছি না। আমার কি এতে সই করা উচিত?"],
    ],
  },
  gu: {
    headline: "બોલો. પહેલાં તમારા રસ્તા જાણો.",
    lede: "વકીલ કે પોલીસ પાસે જતાં પહેલાં, સરળ શબ્દોમાં સાંભળો કે તમારી પાસે કયા કાનૂની વિકલ્પો છે. કાગળનો ફોટો પણ બતાવી શકો છો.",
    lang: "ભાષા",
    state: "રાજ્ય",
    mic: "બોલો",
    stop: "રોકો",
    hint: "બટન દબાવો, વાત કરો, ફરી દબાવો.",
    photo: "કાગળનો ફોટો",
    welcome: "પહેલાં સાંભળો",
    write: "અથવા અહીં લખો",
    ask: "આ સમજાવો",
    again: "ફરી સાંભળો",
    slow: "ધીમે બોલો",
    said: "તમે કહ્યું",
    steps: "પગલાં",
    checks: "સહી કરતાં પહેલાં આ સાંભળો",
    bring: "સાથે રાખવાના કાગળો",
    privacy: "તમારો ફોટો સેવ થતો નથી. વાતચીત સેવ થતી નથી. કાનૂન સાથી વકીલ નથી.",
    phoneVoice: "આ ફોનનો અવાજ",
    canReadPaper: "કાગળ વાંચી શકું છું",
    noModelKey: "ફોટો વાંચવા મોડેલ કી ઉમેરો",
    hearError: "અવાજ સમજાયો નહીં. લખીને પૂછો.",
    tooShort: "ખૂબ ટૂંકું હતું. ફરી બોલો.",
    urgency: { now: "હમણાં જ કૉલ કરો", soon: "આ અઠવાડિયે કોઈને મળો", learn: "સમજવા માટે સમય છે" },
    welcomeSpeech: "નમસ્તે. હું કાનૂન સાથી છું. હું વકીલ નથી. પોલીસ કે વકીલ પાસે જતાં પહેલાં તમારી પાસે કયા રસ્તા છે તે હું સરળ શબ્દોમાં સમજાવું છું. શું બન્યું છે તે કહો અથવા કાગળનો ફોટો બતાવો. જોખમ હોય તો 112 પર કૉલ કરો.",
    examples: [
      ["પડોશી મારી જમીન પર કબ્જો કરી રહ્યો છે", "પડોશી મારી ખેતીની જમીન પર ગેરકાયદે કબ્જો કરી ખંડણી માંગી રહ્યો છે"],
      ["સોશિયલ મીડિયા પર ધમકી", "કોઈ સોશિયલ મીડિયા પર ધમકી આપી બ્લેકમેઇલ કરી રહ્યું છે, મને ડર લાગે છે"],
      ["દસ્તાવેજ કે વીજળીનું બિલ", "આ દસ્તાવેજ કે વીજળી બિલ સમજાતું નથી. મારે આમાં સહી કરવી જોઈએ કે નહીં?"],
    ],
  },
};

const $ = (id) => document.getElementById(id);
let language = localStorage.getItem("ks-lang") || "hi-IN";
let status = { gnani: false, model: false };
let recording = null;
let slow = false;
let lastSpoken = "";
let lastVoice = language;
let voiceGuidance = localStorage.getItem("ks-voice") === "on";

const player = $("player");

function uiLang() {
  const prefix = (language || "hi-IN").slice(0, 2).toLowerCase();
  return COPY[prefix] ? prefix : "hi";
}

function copy() {
  return COPY[uiLang()];
}

function renderChrome() {
  const c = copy();
  document.documentElement.lang = uiLang();
  $("headline").textContent = c.headline;
  $("lede").textContent = c.lede;
  $("state-label").textContent = c.state;
  $("mic-label").textContent = recording ? c.stop : c.mic;
  $("photo").textContent = c.photo;
  $("welcome").textContent = c.welcome;
  $("write-label").textContent = c.write;
  $("ask").textContent = c.ask;
  $("privacy").textContent = c.privacy;
  $("examples").innerHTML = "";
  c.examples.forEach(([label, text]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = label;
    button.addEventListener("click", () => {
      $("text").value = text;
      ask(text);
    });
    $("examples").appendChild(button);
  });
  $("language").value = language;
  const voice = status.gnani ? `Gnani · ${status.voice}` : (c.phoneVoice || "Phone voice");
  const model = status.model
    ? (c.canReadPaper || "Can read a paper")
    : (c.noModelKey || "Add a model key to read a photo");
  $("status").textContent = `${voice} · ${model}`;
  $("voice-toggle").checked = voiceGuidance;
  $("voice-state").textContent = voiceGuidance ? "On" : "Off";
}

function fillLanguages() {
  const select = $("language");
  LANGS.forEach(([code, name]) => {
    const option = document.createElement("option");
    option.value = code;
    option.textContent = name;
    select.appendChild(option);
  });
  select.value = language;
  select.addEventListener("change", () => {
    language = select.value;
    localStorage.setItem("ks-lang", language);
    renderChrome();
  });
}

function fillStates() {
  const select = $("state");
  const saved = localStorage.getItem("ks-state") || "Not sure";
  STATES.forEach((name) => {
    const option = document.createElement("option");
    option.value = name;
    option.textContent = name;
    select.appendChild(option);
  });
  select.value = saved;
  select.addEventListener("change", () => localStorage.setItem("ks-state", select.value));
}

function showError(message) {
  const node = $("error");
  if (!message) {
    node.hidden = true;
    node.textContent = "";
    return;
  }
  node.hidden = false;
  node.textContent = message;
}

async function loadStatus() {
  try {
    status = await (await fetch("/api/status")).json();
  } catch {
    status = { gnani: false, model: false };
  }
  renderChrome();
}

async function ask(text) {
  const cleaned = (text || "").trim();
  if (!cleaned) return;
  showError("");
  $("ask").disabled = true;
  try {
    const response = await fetch("/api/guide", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: cleaned, language, state: $("state").value }),
    });
    if (!response.ok) throw new Error("The guide could not answer. Please try again.");
    const data = await response.json();
    renderAnswer(data, cleaned);
    if (voiceGuidance) await speak(data.spoken, data.answered_in || language);
  } catch (error) {
    showError(error.message);
  } finally {
    $("ask").disabled = false;
  }
}

function renderAnswer(data, said) {
  const c = copy();
  const box = $("answer");
  box.hidden = false;
  box.className = `answer ${data.urgency || "learn"}`;
  const calls = (data.help || [])
    .map((item) => {
      const href = item.phone ? `tel:${item.phone}` : item.url;
      if (!href) {
        return `<div class="call"><span>${escapeHtml(item.name)}<small>${escapeHtml(item.note || "")}</small></span></div>`;
      }
      const extra = item.phone ? item.phone : "";
      return `<a class="call ${data.urgency === "now" ? "emergency" : ""}" href="${href}"><span>${escapeHtml(item.name)}<small>${escapeHtml(item.note || "")}</small></span><strong>${escapeHtml(extra)}</strong></a>`;
    })
    .join("");
  const steps = (data.steps || [])
    .map((step) => `<li><strong>${escapeHtml(step.title)}</strong><span>${escapeHtml(step.detail || "")}</span></li>`)
    .join("");
  const checks = (data.checks || []).map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  const bring = (data.bring || []).map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  box.innerHTML = `
    <div class="urgency ${data.urgency}">${escapeHtml(c.urgency[data.urgency] || "")}</div>
    <h2>${escapeHtml(data.title || "")}</h2>
    ${data.language_note ? `<p class="note">${escapeHtml(data.language_note)}</p>` : ""}
    <p class="spoken">${escapeHtml(data.spoken || "")}</p>
    <div class="tools">
      <button class="again" id="again" type="button">${escapeHtml(c.again)}</button>
      <button class="again" id="slow" type="button">${escapeHtml(c.slow)}</button>
    </div>
    <div class="calls">${calls}</div>
    ${said ? `<p class="note">${escapeHtml(c.said)}: ${escapeHtml(said)}</p>` : ""}
    <p>${escapeHtml(data.what_this_is || "")}</p>
    ${steps ? `<h3>${escapeHtml(c.steps)}</h3><ol>${steps}</ol>` : ""}
    ${checks ? `<h3>${escapeHtml(c.checks)}</h3><ul class="checks">${checks}</ul>` : ""}
    ${bring ? `<h3>${escapeHtml(c.bring)}</h3><ul class="checks">${bring}</ul>` : ""}
    <p class="disclaimer">${escapeHtml(data.disclaimer || "")}</p>
  `;
  lastSpoken = data.spoken || "";
  lastVoice = data.answered_in || language;
  $("again").addEventListener("click", () => {
    slow = false;
    speak(lastSpoken, lastVoice);
  });
  $("slow").addEventListener("click", () => {
    slow = true;
    speak(lastSpoken, lastVoice);
  });
  box.scrollIntoView({ behavior: "smooth", block: "start" });
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function stopSpeaking() {
  player.pause();
  player.removeAttribute("src");
  if (window.speechSynthesis) speechSynthesis.cancel();
}

async function speak(text, voiceLanguage) {
  if (!text) return;
  stopSpeaking();
  if (status.gnani) {
    try {
      const response = await fetch("/api/speak", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: text.slice(0, 1100), language: voiceLanguage }),
      });
      if (response.ok) {
        const blob = await response.blob();
        player.src = URL.createObjectURL(blob);
        player.playbackRate = slow ? 0.86 : 1;
        await player.play();
        return;
      }
    } catch {
      /* fall through to the phone voice */
    }
  }
  if (!window.speechSynthesis) return;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = voiceLanguage || language;
  utterance.rate = slow ? 0.75 : 0.9;
  speechSynthesis.speak(utterance);
}

async function toggleMic() {
  if (recording) {
    recording.stop();
    return;
  }
  showError("");
  if (!status.gnani && (window.SpeechRecognition || window.webkitSpeechRecognition)) {
    browserListen();
    return;
  }
  try {
    recording = await startWavRecorder();
    $("mic").classList.add("live");
    $("mic-label").textContent = copy().stop;
  } catch (error) {
    recording = null;
    showError(error.message || "Microphone is not available.");
  }
}

function browserListen() {
  const Recognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const rec = new Recognition();
  rec.lang = language;
  rec.interimResults = false;
  rec.maxAlternatives = 1;
  $("mic").classList.add("live");
  $("mic-label").textContent = copy().stop;
  recording = { stop: () => rec.stop(), browser: true };
  rec.onresult = (event) => {
    const text = event.results[0][0].transcript;
    $("text").value = text;
    ask(text);
  };
  rec.onerror = () => showError(copy().hearError || "I could not hear that. Type it instead.");
  rec.onend = () => {
    recording = null;
    $("mic").classList.remove("live");
    $("mic-label").textContent = copy().mic;
  };
  rec.start();
}

async function startWavRecorder() {
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  const context = new AudioContext();
  const source = context.createMediaStreamSource(stream);
  const processor = context.createScriptProcessor(4096, 1, 1);
  const chunks = [];
  processor.onaudioprocess = (event) => {
    chunks.push(new Float32Array(event.inputBuffer.getChannelData(0)));
  };
  source.connect(processor);
  processor.connect(context.destination);
  const started = Date.now();
  const timer = setTimeout(() => recording && recording.stop(), 28000);
  return {
    async stop() {
      clearTimeout(timer);
      processor.disconnect();
      source.disconnect();
      stream.getTracks().forEach((track) => track.stop());
      const samples = mix(chunks);
      const wav = encodeWav(downsample(samples, context.sampleRate, 16000), 16000);
      await context.close();
      recording = null;
      $("mic").classList.remove("live");
      $("mic-label").textContent = copy().mic;
      if (Date.now() - started < 600) {
        showError(copy().tooShort || "That was too short. Please speak again.");
        return;
      }
      await sendAudio(wav);
    },
  };
}

async function sendAudio(blob) {
  const body = new FormData();
  body.append("audio", blob, "speech.wav");
  body.append("language", language);
  const response = await fetch("/api/listen", { method: "POST", body });
  if (!response.ok) {
    const detail = await response.json().catch(() => ({}));
    if (window.SpeechRecognition || window.webkitSpeechRecognition) {
      browserListen();
      return;
    }
    throw new Error(detail.detail || "Could not transcribe.");
  }
  const data = await response.json();
  $("text").value = data.transcript;
  if (data.detected_language && LANGS.some(([code]) => code === data.detected_language)) {
    language = data.detected_language;
    localStorage.setItem("ks-lang", language);
    renderChrome();
  }
  await ask(data.transcript);
}

function mix(chunks) {
  const length = chunks.reduce((sum, chunk) => sum + chunk.length, 0);
  const mixed = new Float32Array(length);
  let offset = 0;
  chunks.forEach((chunk) => {
    mixed.set(chunk, offset);
    offset += chunk.length;
  });
  return mixed;
}

function downsample(samples, fromRate, toRate) {
  if (fromRate === toRate) return samples;
  const ratio = fromRate / toRate;
  const length = Math.round(samples.length / ratio);
  const result = new Float32Array(length);
  for (let i = 0; i < length; i++) {
    const start = Math.floor(i * ratio);
    const end = Math.min(samples.length, Math.floor((i + 1) * ratio));
    let total = 0;
    for (let j = start; j < end; j++) total += samples[j];
    result[i] = total / Math.max(1, end - start);
  }
  return result;
}

function encodeWav(samples, sampleRate) {
  const buffer = new ArrayBuffer(44 + samples.length * 2);
  const view = new DataView(buffer);
  const write = (offset, text) => {
    for (let i = 0; i < text.length; i++) view.setUint8(offset + i, text.charCodeAt(i));
  };
  write(0, "RIFF");
  view.setUint32(4, 36 + samples.length * 2, true);
  write(8, "WAVE");
  write(12, "fmt ");
  view.setUint32(16, 16, true);
  view.setUint16(20, 1, true);
  view.setUint16(22, 1, true);
  view.setUint32(24, sampleRate, true);
  view.setUint32(28, sampleRate * 2, true);
  view.setUint16(32, 2, true);
  view.setUint16(34, 16, true);
  write(36, "data");
  view.setUint32(40, samples.length * 2, true);
  let offset = 44;
  for (let i = 0; i < samples.length; i++, offset += 2) {
    const sample = Math.max(-1, Math.min(1, samples[i]));
    view.setInt16(offset, sample < 0 ? sample * 0x8000 : sample * 0x7fff, true);
  }
  return new Blob([buffer], { type: "audio/wav" });
}

async function compressImage(file) {
  const bitmap = await createImageBitmap(file);
  const scale = Math.min(1, 1600 / Math.max(bitmap.width, bitmap.height));
  const canvas = document.createElement("canvas");
  canvas.width = Math.round(bitmap.width * scale);
  canvas.height = Math.round(bitmap.height * scale);
  canvas.getContext("2d").drawImage(bitmap, 0, 0, canvas.width, canvas.height);
  const blob = await new Promise((resolve) => canvas.toBlob(resolve, "image/jpeg", 0.82));
  return blob || file;
}

async function explainFile(file) {
  showError("");
  const image = await compressImage(file);
  const body = new FormData();
  body.append("image", image, "paper.jpg");
  body.append("language", language);
  body.append("state", $("state").value);
  body.append("note", $("text").value.trim());
  const response = await fetch("/api/document", { method: "POST", body });
  if (!response.ok) {
    const detail = await response.json().catch(() => ({}));
    showError(detail.detail || "Could not read the photo.");
    return;
  }
  const data = await response.json();
  renderAnswer(data, $("text").value.trim());
  if (voiceGuidance) await speak(data.spoken, data.answered_in || language);
}

$("mic").addEventListener("click", () => {
  toggleMic().catch((error) => showError(error.message));
});
$("ask").addEventListener("click", () => ask($("text").value));
$("welcome").addEventListener("click", () => speak(copy().welcomeSpeech, language));
$("welcome-audio").addEventListener("click", () => speak(copy().welcomeSpeech, language));
$("photo").addEventListener("click", () => $("file").click());
$("voice-toggle").addEventListener("change", () => {
  voiceGuidance = $("voice-toggle").checked;
  localStorage.setItem("ks-voice", voiceGuidance ? "on" : "off");
  $("voice-state").textContent = voiceGuidance ? "On" : "Off";
});
$("font-toggle").addEventListener("click", () => {
  const enabled = document.body.classList.toggle("large-text");
  $("font-toggle").setAttribute("aria-pressed", String(enabled));
});
$("contrast-toggle").addEventListener("click", () => {
  const enabled = document.body.classList.toggle("high-contrast");
  $("contrast-toggle").setAttribute("aria-pressed", String(enabled));
});
document.querySelectorAll(".feature-trigger").forEach((button) => {
  button.addEventListener("click", () => {
    $("text").value = button.dataset.prompt;
    ask(button.dataset.prompt);
  });
});
$("file").addEventListener("change", () => {
  const file = $("file").files[0];
  $("file").value = "";
  if (file) explainFile(file).catch((error) => showError(error.message));
});

fillLanguages();
fillStates();
renderChrome();
loadStatus();
