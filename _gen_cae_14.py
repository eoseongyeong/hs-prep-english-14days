#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all 14 days for the CAE (Cambridge C1 Advanced) course, output to docs/cae/."""
from __future__ import annotations

import html as H
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs" / "cae"
OUT.mkdir(parents=True, exist_ok=True)

LEVEL = "CAE(C1) · Cambridge Advanced 대비"
BRAND = "CAE 14일 핵심"

DATA = json.loads((ROOT / "_cae_data.json").read_text(encoding="utf-8"))
WORDS = {int(k): v for k, v in DATA["words"].items()}       # day -> [(word,pos,mean,ex), ...]
TRANS = {int(k): v for k, v in DATA["trans"].items()}       # day -> [kr, ...]
GRAMMAR = {int(k): v for k, v in DATA["grammar"].items()}   # day -> [dict(title,body,practice,answers), ...]

DAY_TOPICS = {
    1: "도치 강조구문 · 분열문(Cleft) · 명사화",
    2: "혼합 가정법 · 가정법 현재(that+원형) · 양보(albeit/notwithstanding)",
    3: "복합 분사구문 · 독립분사구문 · 생략과 대용",
    4: "조동사+완료 심화 · 수동 보고구문 · 사역동사 심화",
    5: "전치사 관계절(whereby/wherein) · 강조 도치(so...that) · the비교급~the비교급",
    6: "담화표지(hence/thereby/whereas) · 완곡 표현(hedging) · 전치사 연어",
    7: "화법 심화 · 격식체 구동사 · 관용표현",
    8: "고급 수동태(get-passive) · 전치 강조(Fronting) · 병렬구조",
    9: "미래시제 뉘앙스(be to/be about to) · 완료진행 심화 · 시간절 심화",
    10: "한정사·수량사 심화 · 관사 고급 · 가산/불가산 뉘앙스",
    11: "접속부사(nonetheless/notwithstanding) · 양보·대조절 · 복문 결합",
    12: "동사 패턴 의미차 · 형용사+전치사 연어 · 동사+전치사 연어",
    13: "부가의문·간접의문 격식체 · what/all 강조구문 · 부정어 도치 심화",
    14: "격식/비격식 전환 · 요약문 작성법 · 14일 종합",
}

DAY_CHECKS = {
    1: ["단어 30개 확인", "도치 강조구문", "분열문", "명사화"],
    2: ["단어 30개 확인", "혼합 가정법", "가정법 현재", "양보 구문"],
    3: ["단어 30개 확인", "복합 분사구문", "독립분사구문", "생략과 대용"],
    4: ["단어 30개 확인", "조동사+완료", "수동 보고구문", "사역동사"],
    5: ["단어 30개 확인", "전치사 관계절", "강조 도치", "the비교급 the비교급"],
    6: ["단어 30개 확인", "담화표지", "완곡 표현", "전치사 연어"],
    7: ["단어 30개 확인", "화법 심화", "격식체 구동사", "관용표현"],
    8: ["단어 30개 확인", "고급 수동태", "전치 강조", "병렬구조"],
    9: ["단어 30개 확인", "미래시제 뉘앙스", "완료진행 심화", "시간절 심화"],
    10: ["단어 30개 확인", "한정사·수량사", "관사 고급", "가산/불가산"],
    11: ["단어 30개 확인", "접속부사", "양보·대조절", "복문 결합"],
    12: ["단어 30개 확인", "동사 패턴 의미차", "형용사+전치사", "동사+전치사"],
    13: ["단어 30개 확인", "부가·간접의문", "what/all 강조", "부정어 도치"],
    14: ["단어 30개 확인", "격식전환", "요약문 작성", "14일 종합"],
}


def validate():
    seen = set()
    for day in range(1, 15):
        rows = WORDS[day]
        assert len(rows) == 30, f"day {day}: {len(rows)} words"
        words = [r[0] for r in rows]
        assert len(set(words)) == 30, f"day {day}: duplicate words"
        for w in words:
            assert w not in seen, f"cross-day duplicate: {w}"
            seen.add(w)
        assert len(TRANS[day]) == 30, f"day {day}: {len(TRANS[day])} translations"
        assert len(GRAMMAR[day]) == 3, f"day {day}: {len(GRAMMAR[day])} grammar points"
    assert len(seen) == 420


def build_words(day: int) -> list[tuple]:
    rows = WORDS[day]
    trans = TRANS[day]
    out = []
    for i, ((w, pos, mean, ex), tr) in enumerate(zip(rows, trans), 1):
        out.append((i, w, pos, mean, ex, tr))
    return out


def make_quiz_a(day: int) -> list[tuple[str, str, str]]:
    rng = random.Random(day * 2000 + 1)
    rows = WORDS[day]
    picks = rows[:4]
    all_means = [r[2] for r in rows]
    out = []
    for w, pos, mean, ex in picks:
        wrong = [m for m in all_means if m != mean]
        rng.shuffle(wrong)
        opts = wrong[:2] + [mean]
        rng.shuffle(opts)
        labels = ["(a)", "(b)", "(c)"]
        opt_str = " ".join(f"{labels[i]} {opts[i]}" for i in range(3))
        ans = ["a", "b", "c"][opts.index(mean)]
        out.append((w, opt_str, ans))
    return out


def make_quiz_b(day: int) -> list[tuple[str, str]]:
    rows = WORDS[day]
    picks = rows[4:8]
    out = []
    for w, pos, mean, ex in picks:
        short_mean = mean.split(",")[0].split(";")[0].strip()
        blank = re.sub(re.escape(w), "__________", ex, count=1, flags=re.I)
        if blank == ex:
            blank = f"Please consider the __________ carefully. ({short_mean})"
        else:
            blank = f"{blank} ({short_mean})"
        out.append((blank, w))
    return out


def build_day(n: int) -> dict:
    return dict(
        title=f"Day {n}",
        topic=DAY_TOPICS[n],
        words=build_words(n),
        quiz_a=make_quiz_a(n),
        quiz_b=make_quiz_b(n),
        grammar=GRAMMAR[n],
        checks=DAY_CHECKS[n],
    )


def word_table_html(words):
    rows = []
    for n, w, pos, mean, ex, tr in words:
        rows.append(
            "<tr>"
            f"<td>{n}</td>"
            f"<td class='word'>{H.escape(w)}</td>"
            f"<td class='pos'>{H.escape(pos)}</td>"
            f"<td>{H.escape(mean)}</td>"
            f"<td class=\"ex\" style=\"font-family:var(--font-en)\">{H.escape(ex)}</td>"
            f"<td class=\"trans\">{H.escape(tr)}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr><th>No.</th><th>Word</th><th>품사</th><th>뜻</th>"
        "<th>예문</th><th>해석</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def md_inline_to_html(text: str) -> str:
    lines = text.strip().splitlines()
    out = []
    table_rows = []

    def flush_table():
        nonlocal table_rows
        if not table_rows:
            return
        html_rows = []
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if i == 1 and all(set(c) <= set("-: ") for c in cells):
                continue
            tag = "th" if i == 0 else "td"
            html_rows.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("<table>" + "".join(html_rows) + "</table>")
        table_rows.clear()

    def inline(s: str) -> str:
        s = H.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    for line in lines:
        if line.strip().startswith("|"):
            table_rows.append(line)
            continue
        flush_table()
        if line.startswith("> "):
            out.append(f"<div class='example'>{inline(line[2:])}</div>")
        elif line.strip() == "":
            out.append("")
        elif re.match(r"^\d+\)\s", line.strip()) or line.strip().startswith("- "):
            content = re.sub(r"^\d+\)\s", "", line.strip()) if not line.strip().startswith("- ") else line.strip()[2:]
            out.append(f"<li>{inline(content)}</li>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    flush_table()
    html = "\n".join(out)
    return re.sub(r"(?:<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", html, flags=re.S)


def render_html(n: int, d: dict, total_days: int = 14) -> str:
    quiz_a = "".join(f"<li>{H.escape(w)} — {H.escape(opts)}</li>" for w, opts, _ in d["quiz_a"])
    quiz_b = "".join(f"<li>{H.escape(q)}</li>" for q, _ in d["quiz_b"])
    quiz_ans_a = " ".join(f"{i}-({a})" for i, (*_, a) in enumerate(d["quiz_a"], 1))
    quiz_ans_b = " · ".join(f"{i}. {H.escape(a)}" for i, (*_, a) in enumerate(d["quiz_b"], 5))
    grammar_html = []
    for gi, g in enumerate(d["grammar"], 1):
        prac = "".join(f"<li>{H.escape(p)}</li>" for p in g["practice"])
        grammar_html.append(
            f"""
    <section class="card">
      <h2>{H.escape(g['title'])}</h2>
      <div class="grammar-box">{md_inline_to_html(g['body'])}</div>
      <h3>연습 {gi}</h3>
      <ol>{prac}</ol>
      <details class="answer"><summary>정답</summary>{H.escape(g['answers']).replace(chr(10), '<br>')}</details>
    </section>"""
        )
    nav = '<a href="index.html">CAE 홈</a>' + "".join(
        f'<a href="day{i}.html"' + (' class="active"' if i == n else "") + f">Day {i}</a>"
        for i in range(1, total_days + 1)
    ) + '<a href="../index.html">메인 코스</a>'
    prev = f"day{n-1}.html" if n > 1 else None
    nxt = f"day{n+1}.html" if n < total_days else None
    prev_btn = f'<a class="btn ghost" href="{prev}">← 이전</a>' if prev else "<span></span>"
    next_btn = f'<a class="btn" href="{nxt}">다음 →</a>' if nxt else '<a class="btn" href="index.html">CAE 홈으로</a>'
    checks = "".join(f"<li>☐ {H.escape(c)}</li>" for c in d["checks"])
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{BRAND} — {d['title']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Noto+Sans+KR:wght@400;600;700&family=Source+Serif+4:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
  <div class="wrap">
    <nav class="site-nav">{nav}</nav>
    <header class="hero">
      <p class="brand">{BRAND}</p>
      <p>{d['title']} — {H.escape(d['topic'])}</p>
      <div class="meta">
        <span class="chip">단어 30</span>
        <span class="chip">문법 3</span>
        <span class="chip">{LEVEL}</span>
      </div>
    </header>

    <section class="card" id="words">
      <h2>오늘의 단어 (30)</h2>
      {word_table_html(d['words'])}
    </section>

    <section class="card quiz" id="quiz">
      <h2>단어 확인 퀴즈</h2>
      <h3>A. 뜻 고르기</h3>
      <ol>{quiz_a}</ol>
      <h3>B. 빈칸 채우기</h3>
      <ol start="5">{quiz_b}</ol>
      <details class="answer"><summary>정답 보기</summary>A: {quiz_ans_a}<br>B: {quiz_ans_b}</details>
    </section>

    {''.join(grammar_html)}

    <section class="card">
      <h2>오늘 복습 체크</h2>
      <ul class="checks">{checks}</ul>
    </section>

    <div class="footer-nav">{prev_btn}{next_btn}</div>
  </div>
  <script src="../speak.js"></script>
</body>
</html>
"""


def write_index():
    cards = []
    for i, n in enumerate(range(1, 15)):
        delay = 0.03 * i
        cards.append(
            f"""
      <a class="index-card" href="day{n}.html" style="animation-delay:{delay:.2f}s">
        <p class="day">Day {n}</p>
        <p>{H.escape(DAY_TOPICS[n])}</p>
      </a>"""
        )
    html = f"""<!DOCTYPE html>
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
      <p>{LEVEL} 영어 단어·문법 집중 코스. 하루 단어 30개 + 문법 3포인트.</p>
      <div class="meta">
        <span class="chip">14 Days</span>
        <span class="chip">단어 420</span>
        <span class="chip">문법 42</span>
      </div>
    </header>

    <section class="card">
      <h2>학습 안내</h2>
      <ol>
        <li>단어와 예문을 클릭해 발음을 듣고 따라 말합니다.</li>
        <li>단어 퀴즈를 풀어 확인합니다.</li>
        <li>문법 설명을 본 뒤 연습 문제를 풉니다.</li>
        <li>정답은 각 항목의 '정답 보기'에서 확인합니다.</li>
      </ol>
      <p class="muted">고등예비영문 14일 핵심 과정을 마친 학습자를 위한 CAE(C1) 심화 코스입니다.</p>
    </section>

    <div class="index-grid">
      {''.join(cards)}
    </div>
  </div>
  <script src="../speak.js"></script>
</body>
</html>
"""
    (OUT / "index.html").write_text(html, encoding="utf-8")


def main():
    validate()
    for n in range(1, 15):
        d = build_day(n)
        (OUT / f"day{n}.html").write_text(render_html(n, d), encoding="utf-8")
        print(f"wrote docs/cae/day{n}.html")
    write_index()
    print("done — CAE 14 html files generated in docs/cae/")


if __name__ == "__main__":
    main()
