(function () {
  if (!("speechSynthesis" in window)) return;

  function speak(el) {
    window.speechSynthesis.cancel();
    var utter = new SpeechSynthesisUtterance(el.textContent.trim());
    utter.lang = "en-US";
    utter.rate = 0.9;
    el.classList.add("speaking");
    utter.onend = utter.onerror = function () {
      el.classList.remove("speaking");
    };
    window.speechSynthesis.speak(utter);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("td.word").forEach(function (el) {
      el.addEventListener("click", function () {
        speak(el);
      });
    });
  });
})();
