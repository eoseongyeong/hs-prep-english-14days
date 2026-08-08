(function () {
  if (!("speechSynthesis" in window)) return;

  var voices = [];
  function loadVoices() {
    voices = window.speechSynthesis.getVoices();
  }
  loadVoices();
  window.speechSynthesis.onvoiceschanged = loadVoices;

  // Web Speech API doesn't expose voice gender directly, so we score by
  // name hints. This covers common female/male-labeled voices across
  // Chrome/Android ("Google UK English Female"), Windows ("Hazel", "Sonia",
  // "Libby", "Susan"), and macOS/iOS ("Kate", "Serena", "Martha").
  var FEMALE_HINTS = ["female", "hazel", "susan", "kate", "serena", "martha", "sonia", "libby"];
  var MALE_HINTS = ["male", "daniel", "arthur", "george", "ryan", "rishi", "oliver"];

  function scoreVoice(v) {
    var name = v.name.toLowerCase();
    for (var i = 0; i < FEMALE_HINTS.length; i++) {
      if (name.indexOf(FEMALE_HINTS[i]) !== -1) return 2;
    }
    for (var i = 0; i < MALE_HINTS.length; i++) {
      if (name.indexOf(MALE_HINTS[i]) !== -1) return 0;
    }
    return 1;
  }

  function pickBritishVoice() {
    var candidates = voices.filter(function (v) { return v.lang === "en-GB"; });
    if (!candidates.length) {
      candidates = voices.filter(function (v) { return v.lang && v.lang.indexOf("en-GB") === 0; });
    }
    if (!candidates.length) return null;
    candidates.sort(function (a, b) { return scoreVoice(b) - scoreVoice(a); });
    return candidates[0];
  }

  function speak(el) {
    window.speechSynthesis.cancel();
    loadVoices(); // refresh in case voices loaded after page load without firing onvoiceschanged
    var utter = new SpeechSynthesisUtterance(el.textContent.trim());
    utter.lang = "en-GB";
    var voice = pickBritishVoice();
    if (voice) utter.voice = voice;
    utter.rate = 0.9;
    el.classList.add("speaking");
    utter.onend = utter.onerror = function () {
      el.classList.remove("speaking");
    };
    window.speechSynthesis.speak(utter);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("td.word, td.ex, .fc-word, .fc-ex").forEach(function (el) {
      el.addEventListener("click", function () {
        speak(el);
      });
    });
  });
})();
