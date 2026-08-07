(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var track = document.getElementById("track");
    var cards = Array.prototype.slice.call(track.querySelectorAll(".fc-card"));
    var dots = Array.prototype.slice.call(document.querySelectorAll("#dots button"));
    var counter = document.getElementById("counter");
    var prevBtn = document.getElementById("prevCard");
    var nextBtn = document.getElementById("nextCard");
    var current = 0;

    function goTo(i) {
      i = Math.max(0, Math.min(cards.length - 1, i));
      cards[i].scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }

    function setActive(i) {
      current = i;
      counter.textContent = (i + 1) + " / " + cards.length;
      dots.forEach(function (d, di) {
        d.classList.toggle("active", di === i);
      });
      prevBtn.disabled = i === 0;
      nextBtn.disabled = i === cards.length - 1;
    }

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && entry.intersectionRatio > 0.6) {
            var idx = cards.indexOf(entry.target);
            if (idx !== -1) setActive(idx);
          }
        });
      },
      { root: track, threshold: [0.6] }
    );
    cards.forEach(function (c) { io.observe(c); });

    dots.forEach(function (d, i) {
      d.addEventListener("click", function () { goTo(i); });
    });
    prevBtn.addEventListener("click", function () { goTo(current - 1); });
    nextBtn.addEventListener("click", function () { goTo(current + 1); });

    document.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") goTo(current - 1);
      if (e.key === "ArrowRight") goTo(current + 1);
    });

    setActive(0);
  });
})();
