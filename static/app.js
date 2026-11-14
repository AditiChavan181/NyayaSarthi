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
    urgency: { now: "अभी कॉल कीजिए", soon: "इस हफ़्ते किसी से मिलिए", learn: "समझने का समय है" },
    welcomeSpeech: "नमस्ते। मैं कानून साथी हूँ। मैं वकील नहीं हूँ। मैं आसान शब्दों में बताती हूँ कि पुलिस या वकील के पास जाने से पहले आपके पास कौन से रास्ते हैं। बोलिए कि क्या हुआ, या कागज़ की फ़ोटो दिखाइए। अगर अभी जान का खतरा है, तो 112 पर कॉल कीजिए।",
    examples: [
      ["पड़ोसी मेरी ज़मीन पर कब्ज़ा कर रहा है", "पड़ोसी मेरी ज़मीन पर कब्ज़ा कर रहा है"],
      ["कोई सोशल मीडिया पर धमकी दे रहा है", "कोई सोशल मीडिया पर धमकी दे रहा है और मुझे डर लग रहा है"],
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
    urgency: { now: "Call now", soon: "See someone this week", learn: "You have time to understand" },
    welcomeSpeech: "Hello. I am Kanoon Saathi. I am not a lawyer. I explain, in plain words, what you can do before you go to the police or a lawyer. Say what happened, or show a photo of the paper. If you are in danger right now, call 112.",
    examples: [
      ["A neighbour has taken my land", "A neighbour has occupied my land and I do not know what to do"],
      ["Threats on social media", "Someone is threatening me on social media and I feel scared"],
      ["I cannot understand this bill", "I cannot understand this electricity bill. Does it ask me to sign away my house?"],
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

const player = $("player");

function uiLang() {
  return language.startsWith("en") ? "en" : "hi";
}

function copy() {
  return COPY[uiLang()];
}

function renderChrome() {
  const c = copy();
  document.documentElement.lang = language.startsWith("en") ? "en" : "hi";
  $("headline").textContent = c.headline;
  $("lede").textContent = c.lede;
  $("lang-label").textContent = c.lang;
  $("state-label").textContent = c.state;
  $("mic-label").textContent = recording ? c.stop : c.mic;
  $("hint").textContent = c.hint;
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
  document.querySelectorAll("#langs button").forEach((button) => {
    button.setAttribute("aria-checked", button.dataset.lang === language ? "true" : "false");
  });
  const voice = status.gnani ? `Gnani · ${status.voice}` : (uiLang() === "hi" ? "इस फ़ोन की आवाज़" : "This phone's voice");
  const model = status.model
    ? (uiLang() === "hi" ? "कागज़ पढ़ सकती हूँ" : "Can read a paper")
    : (uiLang() === "hi" ? "कागज़ की फ़ोटो के लिए मॉडल की चाबी जोड़ें" : "Add a model key to read a photo");
  $("status").textContent = `${voice} · ${model}`;
}

function fillLanguages() {
  const box = $("langs");
  LANGS.forEach(([code, name]) => {
    const button = document.createElement("button");
    button.type = "button";
    button.role = "radio";
    button.dataset.lang = code;
    button.textContent = name;
    button.addEventListener("click", () => {
      language = code;
      localStorage.setItem("ks-lang", code);
      renderChrome();
    });
    box.appendChild(button);
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
    await speak(data.spoken, data.answered_in || language);
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
  rec.onerror = () => showError(uiLang() === "hi" ? "आवाज़ समझ नहीं आई। लिख कर पूछिए।" : "I could not hear that. Type it instead.");
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
        showError(uiLang() === "hi" ? "बहुत छोटा था। फिर बोलिए।" : "That was too short. Please speak again.");
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
  await speak(data.spoken, data.answered_in || language);
}

$("mic").addEventListener("click", () => {
  toggleMic().catch((error) => showError(error.message));
});
$("ask").addEventListener("click", () => ask($("text").value));
$("welcome").addEventListener("click", () => speak(copy().welcomeSpeech, language));
$("photo").addEventListener("click", () => $("file").click());
$("file").addEventListener("change", () => {
  const file = $("file").files[0];
  $("file").value = "";
  if (file) explainFile(file).catch((error) => showError(error.message));
});

fillLanguages();
fillStates();
renderChrome();
loadStatus();
