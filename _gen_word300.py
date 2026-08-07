#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 중학필수 영단어 300 flashcard course (30 days x 10 words), output to docs/word300/."""
from __future__ import annotations

import html as H
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs" / "word300"
OUT.mkdir(parents=True, exist_ok=True)

BRAND = "초등필수 영단어 300"
TOTAL_DAYS = 30

WORDS = {int(k): v for k, v in json.loads((ROOT / "_word300_data.json").read_text(encoding="utf-8")).items()}

DAY_TOPICS = {
    1: "인사·소개", 2: "가족", 3: "학교생활", 4: "하루 일과", 5: "음식",
    6: "숫자·시간", 7: "날씨·계절", 8: "취미·운동", 9: "감정", 10: "신체·건강",
    11: "동물", 12: "색깔·모양", 13: "집·방", 14: "옷", 15: "교통수단",
    16: "동네·장소", 17: "직업", 18: "자연", 19: "기술·기기", 20: "쇼핑",
    21: "일상 동사 1", 22: "일상 동사 2", 23: "형용사·반의어", 24: "전치사·방향", 25: "요일·월",
    26: "여행", 27: "의사소통", 28: "감정 심화", 29: "학교 과목", 30: "종합 복습",
}


def validate():
    seen = set()
    for day in range(1, TOTAL_DAYS + 1):
        rows = WORDS[day]
        assert len(rows) == 10, f"day {day}: {len(rows)} words"
        for w, *_ in rows:
            assert w not in seen, f"cross-day duplicate: {w}"
            seen.add(w)
    assert len(seen) == 300


def card_html(word, pos, mean, ex, tr):
    return f"""
    <section class="fc-card">
      <p class="fc-word">{H.escape(word)}</p>
      <p class="fc-meta"><span class="fc-pos">{H.escape(pos)}</span><span class="fc-mean">{H.escape(mean)}</span></p>
      <div class="fc-example-box">
        <p class="fc-ex">{H.escape(ex)}</p>
        <p class="fc-tr">{H.escape(tr)}</p>
      </div>
      <p class="fc-hint">🔊 단어나 예문을 탭하면 발음이 나와요</p>
    </section>"""


def render_day(n: int) -> str:
    rows = WORDS[n]
    cards = "".join(card_html(*r) for r in rows)
    dots = "".join(f'<button aria-label="{i+1}번 단어"></button>' for i in range(len(rows)))
    prev_day = f'<a class="fc-btn ghost" href="day{n-1}.html">← Day {n-1}</a>' if n > 1 else '<a class="fc-btn ghost" href="index.html">← 목록</a>'
    next_day = f'<a class="fc-btn" href="day{n+1}.html">Day {n+1} →</a>' if n < TOTAL_DAYS else '<a class="fc-btn" href="index.html">목록으로 →</a>'
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" />
  <title>{BRAND} — Day {n}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Noto+Sans+KR:wght@400;600;700&family=Source+Serif+4:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="stylesheet" href="word300.css" />
</head>
<body class="fc-body">
  <header class="fc-topbar">
    <a class="fc-home" href="index.html">← 목록</a>
    <span class="fc-daylabel">Day {n} · {H.escape(DAY_TOPICS[n])}</span>
    <span class="fc-counter" id="counter">1 / {len(rows)}</span>
  </header>

  <div class="fc-track" id="track">{cards}
  </div>

  <div class="fc-dots" id="dots">{dots}</div>

  <div class="fc-nav">
    <button class="fc-btn arrow ghost" id="prevCard" aria-label="이전 단어">‹</button>
    <button class="fc-btn arrow ghost" id="nextCard" aria-label="다음 단어">›</button>
  </div>

  <div class="fc-daynav">
    {prev_day}
    {next_day}
  </div>

  <script src="../speak.js"></script>
  <script src="word300.js"></script>
</body>
</html>
"""


def render_index() -> str:
    cards = []
    for i, n in enumerate(range(1, TOTAL_DAYS + 1)):
        delay = 0.02 * i
        cards.append(
            f"""
      <a class="index-card" href="day{n}.html" style="animation-delay:{delay:.2f}s">
        <p class="day">Day {n}</p>
        <p>{H.escape(DAY_TOPICS[n])}</p>
      </a>"""
        )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{BRAND}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Noto+Sans+KR:wght@400;600;700&family=Source+Serif+4:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <div class="wrap">
    <nav class="site-nav"><a href="../index.html">메인 코스</a></nav>
    <header class="hero">
      <p class="brand">{BRAND}</p>
      <p>스마트폰으로 가볍게 훑는 초등 필수 영단어. 하루 10개, 30일이면 300개 완성.</p>
      <div class="meta">
        <span class="chip">30 Days</span>
        <span class="chip">단어 300</span>
        <span class="chip">플래시카드</span>
      </div>
    </header>

    <section class="card">
      <h2>코스 선택</h2>
      <div class="course-grid">
        <div class="course-card current">
          <span class="chip">현재 코스</span>
          <p class="day">초등필수 영단어 300</p>
          <p>초등 필수 영단어 300개, 문법 없이 플래시카드로.</p>
        </div>
        <a class="course-card" href="../midword300/index.html">
          <span class="chip">기초</span>
          <p class="day">중학필수 영단어 300</p>
          <p>중학 필수 영단어 300개, 문법 없이 플래시카드로.</p>
        </a>
        <a class="course-card" href="../index.html">
          <span class="chip">심화</span>
          <p class="day">고등예비영문 14일 핵심</p>
          <p>고1~고2 · 수능 기초 심화. 단어 420 + 문법 42.</p>
        </a>
        <a class="course-card" href="../cae/index.html">
          <span class="chip">최상위</span>
          <p class="day">CAE(C1) 14일 핵심</p>
          <p>케임브리지 CAE 대비. 단어 420 + 문법 42.</p>
        </a>
      </div>
    </section>

    <section class="card">
      <h2>학습 안내</h2>
      <ol>
        <li>카드를 좌우로 넘기며 하루 10단어를 훑어봅니다.</li>
        <li>단어와 예문을 탭하면 발음을 들을 수 있습니다.</li>
        <li>한글 뜻과 해석은 카드 안에 바로 나와 있습니다.</li>
      </ol>
      <p class="muted">문법 설명 없이 단어만 가볍게 익히는 코스입니다. 취미로 영어를 공부하는 분께 추천합니다.</p>
    </section>

    <div class="index-grid">
      {''.join(cards)}
    </div>
  </div>
</body>
</html>
"""


def main():
    validate()
    for n in range(1, TOTAL_DAYS + 1):
        (OUT / f"day{n}.html").write_text(render_day(n), encoding="utf-8")
        print(f"wrote docs/word300/day{n}.html")
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")
    print("done — word300 30 html files generated in docs/word300/")


if __name__ == "__main__":
    main()
