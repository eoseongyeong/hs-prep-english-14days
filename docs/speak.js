(function () {
  if (!("speechSynthesis" in window)) return;

  var voices = [];
  function loadVoices() {
    voices = window.speechSynthesis.getVoices();
  }
  loadVoices();
  window.speechSynthesis.onvoiceschanged = loadVoices;

  var PREFERRED_NAMES = [
    "Google UK English Female",
    "Google UK English Male",
    "Serena",
    "Stephanie",
    "Arthur",
  ];

  function pickBritishVoice() {
    for (var i = 0; i < PREFERRED_NAMES.length; i++) {
      var found = voices.find(function (v) { return v.name === PREFERRED_NAMES[i]; });
      if (found) return found;
    }
    return (
      voices.find(function (v) { return v.lang === "en-GB" && v.name.indexOf("Daniel") === -1; }) ||
      voices.find(function (v) { return v.lang === "en-GB"; }) ||
      voices.find(function (v) { return v.lang && v.lang.indexOf("en-GB") === 0; }) ||
      null
    );
  }

  function speak(el) {
    window.speechSynthesis.cancel();
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
    document.querySelectorAll("td.word, td.ex").forEach(function (el) {
      el.addEventListener("click", function () {
        speak(el);
      });
    });
  });
})();
