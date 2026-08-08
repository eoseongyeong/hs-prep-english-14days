(function () {
  if (!("speechSynthesis" in window)) return;

  var voices = [];
  function loadVoices() {
    voices = window.speechSynthesis.getVoices();
  }
  loadVoices();
  window.speechSynthesis.onvoiceschanged = loadVoices;

  // Web Speech API doesn't expose voice gender directly, so we match by
  // name hints. Covers Chrome/Android ("Google UK English Female"),
  // Windows ("Hazel", "Sonia", "Libby", "Susan"), and macOS/iOS
  // ("Kate", "Serena", "Martha", "Samantha", "Victoria", "Fiona", "Karen").
  var FEMALE_HINTS = [
    "female", "hazel", "susan", "kate", "serena", "martha", "sonia", "libby",
    "samantha", "victoria", "fiona", "karen", "moira", "tessa", "allison", "ava", "zoe"
  ];
  var MALE_HINTS = [
    "male", "daniel", "arthur", "george", "ryan", "rishi", "oliver",
    "aaron", "alex", "fred", "gordon", "james", "thomas"
  ];

  function isFemale(v) {
    var name = v.name.toLowerCase();
    for (var i = 0; i < FEMALE_HINTS.length; i++) {
      if (name.indexOf(FEMALE_HINTS[i]) !== -1) return true;
    }
    return false;
  }

  function isMale(v) {
    var name = v.name.toLowerCase();
    for (var i = 0; i < MALE_HINTS.length; i++) {
      if (name.indexOf(MALE_HINTS[i]) !== -1) return true;
    }
    return false;
  }

  function pickVoice() {
    if (!voices.length) return null;

    // 1. en-GB female
    var gbFemale = voices.filter(function (v) { return v.lang === "en-GB" && isFemale(v); });
    if (gbFemale.length) return gbFemale[0];

    // 2. Samantha (default female English voice on iOS/macOS)
    var samantha = voices.filter(function (v) { return v.name.toLowerCase().indexOf("samantha") !== -1; });
    if (samantha.length) return samantha[0];

    // 3. en-US / en-AU / en-IE female
    var otherEnglishFemale = voices.filter(function (v) {
      return (v.lang === "en-US" || v.lang === "en-AU" || v.lang === "en-IE") && isFemale(v);
    });
    if (otherEnglishFemale.length) return otherEnglishFemale[0];

    // 4. any other English female voice
    var anyEnglishFemale = voices.filter(function (v) {
      return v.lang && v.lang.indexOf("en") === 0 && isFemale(v);
    });
    if (anyEnglishFemale.length) return anyEnglishFemale[0];

    // last resort: any English voice that isn't clearly male
    var anyEnglishNotMale = voices.filter(function (v) {
      return v.lang && v.lang.indexOf("en") === 0 && !isMale(v);
    });
    if (anyEnglishNotMale.length) return anyEnglishNotMale[0];

    var anyEnglish = voices.filter(function (v) { return v.lang && v.lang.indexOf("en") === 0; });
    return anyEnglish[0] || null;
  }

  function fire(el) {
    window.speechSynthesis.cancel();
    var utter = new SpeechSynthesisUtterance(el.textContent.trim());
    var voice = pickVoice();
    if (voice) {
      utter.voice = voice;
      utter.lang = voice.lang;
    } else {
      utter.lang = "en-GB";
    }
    utter.rate = 0.9;
    el.classList.add("speaking");
    utter.onend = utter.onerror = function () {
      el.classList.remove("speaking");
    };
    window.speechSynthesis.speak(utter);
  }

  function speak(el) {
    loadVoices(); // iOS sometimes hasn't fired voiceschanged yet; refresh right before picking
    if (!voices.length) {
      // Some mobile browsers (e.g. Chrome on iOS) populate the voice list
      // asynchronously even after getVoices() is called. Give it one short
      // retry before falling back to the browser's default voice.
      window.speechSynthesis.getVoices();
      setTimeout(function () {
        loadVoices();
        fire(el);
      }, 200);
      return;
    }
    fire(el);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("td.word, td.ex, .fc-word, .fc-ex").forEach(function (el) {
      el.addEventListener("click", function () {
        speak(el);
      });
    });
  });
})();
