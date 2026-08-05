#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate all 14 days (고1~고2 · 수능 기초 심화) for 고등예비영문 course."""
from __future__ import annotations

import html as H
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT / "md"
HTML = ROOT / "html"
LEVEL = "고1~고2 · 수능 기초 심화"
BRAND = "고등예비영문 14일 핵심"

MD.mkdir(exist_ok=True)
HTML.mkdir(exist_ok=True)

VOCAB = json.loads((ROOT / "_vocab420.json").read_text(encoding="utf-8"))
DAY_WORDS = {int(k): v for k, v in VOCAB["day_words"].items()}
META = VOCAB["meta"]

DAY_TOPICS = {
    1: "어휘 형성 · SVOC · 5형식 목적격보어 심화",
    2: "상태동사·시제 뉘앙스 · 과거 시제 선택 · 미래완료·완료진행",
    3: "조동사 추측·의무 · 수동태 확장 · 준조동·that절 should",
    4: "toV vs V-ing 의미차 · 동명사·부정사 결합 · 관계사 심화",
    5: "상관접속·접속부사 · 비교 구문 심화 · 중간 종합",
    6: "현재완료 신호어 심화 · 완료진행 · 과거완료·시제 일치",
    7: "간접화법 시제·부사 · 간접의문 · 명령·제안 전달",
    8: "관계부사 · whose·of which · 제한·계속적·which절전체",
    9: "가정법과거 · 가정법과거완료·혼합가정 · wish·as if·It's time",
    10: "감정분사 쌍 · 분사구문·완료분사 · with독립분사",
    11: "명사절 · It가주어·강조구문 · 부정어 도치",
    12: "전치사 뉘앙스 · 형·명+전치사 · 구동사·예문",
    13: "수일치 함정 · 관사 고급 · 수량사·부분 표현",
    14: "독해 신호어 · 문장 압축·바꿔쓰기 · 14일 고난도 종합",
}

DAY_CHECKS = {
    1: ["단어 30개 확인", "접두·접미사 형성", "SVOC·5형식 보어", "목적격보어 to V / p.p."],
    2: ["단어 30개 확인", "상태동사 시제", "과거 시제 선택", "미래완료·완료진행"],
    3: ["단어 30개 확인", "조동사 추측·의무", "수동태 확장", "준조동·should that절"],
    4: ["단어 30개 확인", "to V vs V-ing", "동명사·부정사 결합", "관계사 심화"],
    5: ["단어 30개 확인", "상관접속사", "비교 구문 심화", "1~5일 중간 종합"],
    6: ["단어 30개 확인", "현재완료 신호어", "현재완료진행", "과거완료·시제 일치"],
    7: ["단어 30개 확인", "간접화법 시제·부사", "간접의문 어순", "명령·제안 전달"],
    8: ["단어 30개 확인", "관계부사", "whose·of which", "계속적·which절 전체"],
    9: ["단어 30개 확인", "가정법 과거", "가정법 과거완료·혼합", "wish·as if·It's time"],
    10: ["단어 30개 확인", "감정분사 쌍", "분사구문·완료분사", "with·독립분사"],
    11: ["단어 30개 확인", "명사절", "It 가주어·강조", "부정어 도치"],
    12: ["단어 30개 확인", "전치사 뉘앙스", "형·명+전치사", "구동사"],
    13: ["단어 30개 확인", "수일치 함정", "관사 고급", "수량사·부분 표현"],
    14: ["단어 30개 확인", "독해 신호어", "문장 압축·바꿔쓰기", "14일 고난도 종합"],
}

GRAMMAR = {
    1: [
        dict(
            title="문법 1. 어휘 형성 (접두·접미사)",
            body="""**접두사(의미 변화)**
| 접두 | 의미 | 예 |
|------|------|----|
| ab-/abs- | ~에서 떨어져 | **ab**normal, **abs**tract |
| ad-/ac- | ~쪽으로 | **ad**here, **ac**quire |
| com-/con- | 함께·강조 | **com**ply, **con**stitute |
| de-/dis- | 반대·제거 | **de**duce, **dis**seminate |
| ex-/e- | 밖으로 | **ex**acerbate, **e**radicate |
| pre-/pro- | 앞·앞서 | **pre**mise, **pro**long |

**접미사(품사 변화)**
| 접미 | 품사 | 예 |
|------|------|----|
| -tion/-sion | 명사 | abolition, expansion |
| -ive/-able | 형용사 | cumulative, adaptable |
| -ize/-ify | 동사 | categorize, amplify |
| -ment | 명사 | development, argument |

> **abandon** (a+bandon) · **accumulate** (ad+cumulus) · **contradict** (contra+dict)""",
            practice=[
                "The policy will __________ (abolish) outdated regulations.",
                "Scholars __________ (derive) new theories from data.",
                "The report __________ (elaborate) on methodological limits.",
                "Inflation may __________ (exacerbate) income inequality.",
            ],
            answers="1 abolish · 2 derive · 3 elaborates · 4 exacerbate",
        ),
        dict(
            title="문법 2. SVOC (주·동·목·목적격보어)",
            body="""**SVOC** = S + V + O + C(목적격보어)  
목적어(O)를 설명·판단하는 C가 **목적어 바로 뒤**에 온다.

| 유형 | 패턴 | 예 |
|------|------|----|
| 명사 보어 | V + O + N | They **elected** him **president**. |
| 형용사 보어 | V + O + A | The news **left** us **speechless**. |
| to부정사 | V + O + to V | The evidence **led** researchers **to revise** the model. |
| 현재분사 | V + O + -ing | I **found** him **reading** the report. |
| 과거분사 | V + O + p.p. | We **consider** the claim **unsubstantiated**. |

**자주 쓰이는 SVOC 동사:** make, find, consider, think, call, appoint, leave, keep, want, expect, prove, render""",
            practice=[
                "The committee __________ the proposal __________ (approve).",
                "Critics __________ the argument __________ (flaw).",
                "The data __________ scientists __________ (reconsider) their hypothesis.",
                "We __________ the manuscript __________ (publish) next month.",
            ],
            answers="1 approved / approved(approved the proposal) · 2 found / flawed · 3 led / to reconsider · 4 expect / to be published",
        ),
        dict(
            title="문법 3. 5형식 목적격보어 심화 (to V vs p.p. vs 원형)",
            body="""**5형식** = S + V + O + OC

| 보어 | 의미 차 | 예 |
|------|---------|----|
| **원형** | O가 OC 행위 **수행** | I **saw** him **cross** the street. |
| **to V** | O에게 OC **하게 하다/되게** | The judge **ordered** him **to testify**. |
| **p.p.** | O가 OC **당함(수동)** | We **want** the issue **resolved**. |
| **형용사** | O의 **상태** | They **declared** the treaty **void**. |

**주의:** consider/find/think + O + **to be** + A/N (to be 생략 가능)  
> I **consider** him **(to be)** reliable.  
> The court **found** the defendant **guilty**.""",
            practice=[
                "The board __________ the CEO __________ (resign).",
                "Regulators __________ the firm __________ (violate) safety rules.",
                "Historians __________ the treaty __________ (significance) to regional peace.",
                "The panel __________ the evidence __________ (insufficient) for conviction.",
            ],
            answers="1 wants / to resign · 2 found / to have violated · 3 consider / significant · 4 deemed / insufficient",
        ),
    ],
    2: [
        dict(
            title="문법 1. 상태동사와 시제 뉘앙스",
            body="""**상태동사(stative verbs)** 는 진행형(-ing)에 잘 쓰이지 않는다.

| 그룹 | 예 | 진행형 |
|------|----|--------|
| 인지·감각 | know, believe, understand, see(이해) | ❌ I am knowing |
| 감정·태도 | love, hate, prefer, want | ❌ I am wanting |
| 소유·관계 | belong, own, contain, resemble | ❌ It is resembling |
| 상태 | seem, appear, remain, resemble | ❌ She is seeming |

**예외(의도·변화 강조):** I **am thinking** about your offer. / She **is resembling** her mother more.  
**have** = 소유 → ❌ having · **have** = 경험·행사 → ✅ having a meeting""",
            practice=[
                "I __________ (know) her since we met at the conference.",
                "The two theories closely __________ (resemble) each other.",
                "Prices __________ (fluctuate) more than wages in recent years.",
                "She __________ (think) about changing her major. (숙고)",
            ],
            answers="1 have known · 2 resemble · 3 have fluctuated / fluctuate · 4 is thinking",
        ),
        dict(
            title="문법 2. 과거 시제 선택 (단순·과거완료·과거진행)",
            body="""| 시제 | 쓰임 | 예 |
|------|------|----|
| **단순과거** | 완료된 과거·습관 | He **resigned** in 2020. |
| **과거진행** | 과거 특정 시점 **진행** | While I **was reading**, she called. |
| **과거완료** | 과거보다 **더 이전**(대과거) | By 2019, she **had published** three books. |
| **used to** | 과거 **습관·상태**(지금은 아님) | He **used to live** abroad. |

**when/while/before/after/by the time** + 과거 → 과거완료 연습  
> After the evidence **had emerged**, the jury **deliberated**.""",
            practice=[
                "By the time negotiations __________ (conclude), both sides __________ (exhaust).",
                "While analysts __________ (speculate), markets __________ (subside).",
                "She __________ (chronicle) the war for a decade before the book __________ (publish).",
                "He __________ (use) to defer decisions, but now he acts promptly.",
            ],
            answers="1 concluded / had exhausted · 2 were speculating / subsided · 3 had chronicled / was published · 4 used",
        ),
        dict(
            title="문법 3. 미래완료 · 미래완료진행",
            body="""**미래완료:** will have + p.p. → **미래 시점까지 완료**  
> By next June, I **will have completed** the thesis.

**미래완료진행:** will have been + -ing → **미래까지 계속**  
> By December, they **will have been negotiating** for six months.

**by + 미래 시점** → 미래완료(진행) 신호  
**현재완료 vs 미래완료:** I **have lived** here for 5 years. / By 2030, I **will have lived** here for 20 years.""",
            practice=[
                "By the deadline, we __________ (submit) all required documents.",
                "Next month, she __________ (work) here for ten years.",
                "By 2030, scientists __________ (observe) the region for three decades.",
                "They __________ (negotiate) for hours when the agreement is signed tonight.",
            ],
            answers="1 will have submitted · 2 will have been working · 3 will have been observing · 4 will have been negotiating",
        ),
    ],
    3: [
        dict(
            title="문법 1. 조동사 추측·의무",
            body="""| 조동사 | 추측(현재) | 추측(과거) | 의무 |
|--------|------------|------------|------|
| must | ~임에 틀림 | must have p.p. | ~해야(강) |
| may/might | ~일지도 | may/might have p.p. | ~해도 됨 |
| can't | ~일 리 없다 | can't have p.p. | — |
| should | ~일 것(추정) | should have p.p. | ~해야(약) |
| ought to | — | ought to have p.p. | ~해야 |
| have to | — | — | ~해야(외부) |

> He **must be** tired. / He **must have missed** the train.  
> You **should have submitted** the form earlier.""",
            practice=[
                "The door is open; someone __________ (must / enter) while we were out.",
                "You __________ (should / notify) us before the deadline.",
                "She __________ (can't / finish) the report — it's only been an hour.",
                "Citizens __________ (oblige) to abide by constitutional law.",
            ],
            answers="1 must have entered · 2 should have notified · 3 can't have finished · 4 are obliged",
        ),
        dict(
            title="문법 2. 수동태 확장 (4~5형식·지각·사역)",
            body="""**4형식 수동:** 간접목적어 → 주어  
> They **gave** me a chance. → I **was given** a chance.

**5형식 수동:** 목적어 + 보어 → 주어 + be p.p. + 보어  
> People **consider** him honest. → He **is considered** honest.

**지각동사 수동:** see/hear/watch + O + V → O + be seen + to V  
> He **was seen to enter** the building.

**사역동사:** make + O + V → O + be made **to V**  
> She **was made to testify**.""",
            practice=[
                "The committee __________ (allocate) funds to priority projects last week.",
                "He __________ (consider) the most reliable witness.",
                "The suspect __________ (see) to leave through the rear exit.",
                "Workers __________ (require) to submit safety reports monthly.",
            ],
            answers="1 was allocated · 2 is considered · 3 was seen · 4 are required",
        ),
        dict(
            title="문법 3. 준조동사 · that절 should",
            body="""**준조동사 + that + 주어 + (should) + 원형**  
insist / suggest / recommend / demand / propose / require / urge / mandate …

> The law **requires** that every citizen **(should) pay** taxes.  
> I **insist** that he **(should) be** present.

**should 생략** 가능(미국·격식 영어)  
**suggest + -ing / suggest + that** (that절에서 ❌ suggest him to go)""",
            practice=[
                "The board __________ (recommend) that the CEO __________ (resign).",
                "Regulations __________ (stipulate) that data __________ (protect).",
                "The judge __________ (urge) that witnesses __________ (refrain) from speculation.",
                "It is essential that every applicant __________ (submit) transcripts.",
            ],
            answers="1 recommended / (should) resign · 2 stipulate / (should) be protected · 3 urged / (should) refrain · 4 (should) submit",
        ),
    ],
    4: [
        dict(
            title="문법 1. to V vs V-ing 의미 차",
            body="""| 동사 | to V | V-ing |
|------|------|-------|
| remember | 미래 기억 | 과거 기억 |
| forget | 미래 잊음 | 과거 잊음 |
| regret | ~할 것을 후회 | ~한 것을 후회 |
| try | ~하려 시도 | 시도·실험 |
| mean | ~하려 함 | ~을 의미 |
| stop | ~하기 위해 멈춤 | ~하던 것을 멈춤 |

> I **regret to inform** you… / I **regret informing** him.  
> He **tried to open** the door. / He **tried using** another key.""",
            practice=[
                "She __________ (remember / lock) the door before leaving.",
                "I __________ (regret / say) that the application was rejected.",
                "They __________ (mean / propose) a complete policy overhaul.",
                "He stopped __________ (smoke) to improve his health.",
            ],
            answers="1 remembered to lock · 2 regret to say · 3 mean to propose · 4 smoking",
        ),
        dict(
            title="문법 2. 동명사·부정사 결합",
            body="""**동명사만:** enjoy, avoid, deny, risk, postpone, quit, resist, tolerate, merit …  
**to부정사만:** attempt, endeavor, decide, intend, propose, refuse, venture …  
**둘 다(의미 같음):** like, love, hate, prefer, begin, start, continue …  
**둘 다(의미 다름):** remember, forget, regret, try, mean, stop …

**전치사 + V-ing:** insist **on** going · refrain **from** commenting · object **to** being …  
**It is + adj + to V / V-ing:** It is risky **to venture** … / It is no use **trying** …""",
            practice=[
                "He denied __________ (omit) critical data from the report.",
                "The plan merits __________ (consider) by the full committee.",
                "She objected to __________ (waive) her contractual rights.",
                "It is difficult __________ (resist) the temptation to speculate.",
            ],
            answers="1 omitting · 2 consideration / being considered · 3 waiving · 4 to resist",
        ),
        dict(
            title="문법 3. 관계사 심화 (what / whatever / whoever)",
            body="""**what** = the thing(s) which · 선행사 포함  
> **What** he said surprised everyone.

**whatever / whoever / whichever** = anything/anyone that  
> **Whatever** decision you make, support it.  
> **Whoever** violates the rule will be penalized.

**the way (that/in which)** · **the reason (that/why)** · **the time (that/when)**  
> This is **the way** (that/in which) we **facilitate** learning.""",
            practice=[
                "__________ he proposed was rejected by the board.",
                "__________ attempts to breach security will be prosecuted.",
                "That is the reason __________ the meeting was postponed.",
                "I will support __________ candidate you recommend.",
            ],
            answers="1 What · 2 Whoever / Anyone who · 3 why / that · 4 whichever / whatever",
        ),
    ],
    5: [
        dict(
            title="문법 1. 상관접속사",
            body="""**앞뒤 문법 구조가 대칭**이어야 한다.

| 상관접속 | 의미 |
|----------|------|
| both A and B | A와 B 모두 |
| not only A but also B | A뿐 아니라 B도 |
| either A or B | A 또는 B |
| neither A nor B | A도 B도 아닌 |
| whether A or B | A이든 B이든 |
| not A but B | A가 아니라 B |

> **Not only** did she **condemn** the act, **but she also** proposed reforms.  
> **Either** you **comply** with the rules **or** you face penalties.""",
            practice=[
                "__________ the evidence __________ the testimony supports the claim.",
                "__________ did he __________ the plan, but he also implemented it.",
                "She is __________ talented __________ diligent.",
                "__________ you accept the offer __________ decline it, notify us by Friday.",
            ],
            answers="1 Both / and · 2 Not only / endorse(approve) · 3 not only / but also · 4 Whether / or",
        ),
        dict(
            title="문법 2. 비교 구문 심화",
            body="""**원급:** as + 형/부 + as · not so/as … as  
**비교급:** -er / more … than · the -er, the -er  
**최상급:** the -est / the most … · one of the + 최상급 + 복수명사

**수식어 위치:**  
> **Much** more significant **than** expected.  
> **By far the most** controversial issue.

**비교 대상 일치:** Her research is more rigorous **than that of** her peers. (❌ than her peers)  
**the + 비교급, the + 비교급:** **The more** you read, **the better** you write.""",
            practice=[
                "This policy is __________ (significant) than the previous one.",
                "She is __________ (talented) student in the cohort.",
                "The __________ (hard) you work, the __________ (likely) you succeed.",
                "His argument is as __________ (compelling) as __________ of the lead author.",
            ],
            answers="1 more significant · 2 the most talented · 3 harder / more likely · 4 compelling / that",
        ),
        dict(
            title="문법 3. 중간 종합 (Day 1~5)",
            body="""1~5일 핵심을 혼합한 고난도 문제입니다.""",
            practice=[
                "[5형식] The court __________ him __________ (sentence) to five years.",
                "[조동사] You __________ (should / inform) us earlier about the breach.",
                "[to V/V-ing] He quit __________ (smoke) and attempted __________ (resume) training.",
                "[관계] __________ was enacted last year has already been amended.",
                "[비교] Her analysis is far __________ (rigorous) than __________ of her critics.",
                "[수동] Employees __________ (require) to comply with safety protocols.",
            ],
            answers="1 sentenced / to serve( sentenced him to five years) · 2 should have informed · 3 smoking / to resume · 4 What · 5 more rigorous / that · 6 are required",
        ),
    ],
    6: [
        dict(
            title="문법 1. 현재완료 신호어 심화",
            body="""**have/has + p.p.**

| 신호 | 의미 | 예 |
|------|------|----|
| already, yet, just, ever, never | 경험·완료 | She **has just published** a paper. |
| for / since | 계속 | He **has researched** here **since** 2018. |
| so far, up to now, until now | 지금까지 | **So far**, results **have validated** the model. |
| recently, lately | 최근 | Markets **have fluctuated** recently. |
| this week/month/year | 포함 현재 | We **have compiled** three reports **this month**. |

**❌** I have met her **two years ago**. → I **met** her two years ago.""",
            practice=[
                "Researchers __________ (already / corroborate) the initial findings.",
                "__________ you ever __________ (hypothesize) about such a link?",
                "The team __________ (investigate) the case for six months.",
                "So far, no study __________ (refute) the central claim.",
            ],
            answers="1 have already corroborated · 2 Have / hypothesized · 3 has been investigating / has investigated · 4 has refuted",
        ),
        dict(
            title="문법 2. 현재완료진행",
            body="""**have/has been + -ing** → 과거부터 **지금까지 계속**

> I **have been examining** the data all morning.  
> It **has been raining** since dawn.

**현재완료 vs 현재완료진행**  
- 결과·경험·완료 → 현재완료  
- **지속·반복·미완료** 강조 → 현재완료진행  
> She **has written** three books. (완료)  
> She **has been writing** all day. (계속)""",
            practice=[
                "We __________ (observe) the phenomenon since the experiment began.",
                "He looks exhausted. He __________ (work) on the thesis for hours.",
                "How long __________ you __________ (investigate) this case?",
                "I __________ (know) her since we collaborated on the project.",
            ],
            answers="1 have been observing · 2 has been working · 3 have / been investigating · 4 have known",
        ),
        dict(
            title="문법 3. 과거완료 · 시제 일치",
            body="""**had + p.p.** = 과거보다 더 이전  
**과거완료진행:** had been + -ing

> When the audit **started**, officials **had already verified** the accounts.  
> By the time she **arrived**, they **had been negotiating** for hours.

**시제 일치(간접화법·명사절):**  
주절 과거 → 종속절 **과거·과거완료**  
> He said he **had finished** the report.""",
            practice=[
                "After scientists __________ (formulate) the hypothesis, they designed trials.",
                "By 2020, the lab __________ (publish) over fifty papers.",
                "She explained that she __________ (not / receive) the notification.",
                "When we arrived, the committee __________ (debate) the issue for two hours.",
            ],
            answers="1 had formulated · 2 had published · 3 had not received · 4 had been debating",
        ),
    ],
    7: [
        dict(
            title="문법 1. 간접화법 시제·부사 변화",
            body="""**직접 → 간접:** say/tell + (that) + **시제 후진**

| 직접 | 간접 |
|------|------|
| am/is/are | was/were |
| do/does | did |
| will/can/may | would/could/might |
| have/has | had |
| am/is/are doing | was/were doing |
| have p.p. | had p.p. |

**시간·장소 부사:** now→then, today→that day, tomorrow→the next/following day, yesterday→the day before, here→there, this→that""",
            practice=[
                "“I **will disclose** the findings tomorrow,” she said. → She said she __________ the findings the next day.",
                "“We **are negotiating** now,” they replied. → They replied they __________ then.",
                "“I **have never witnessed** such fraud,” he testified. → He testified he __________ such fraud.",
                "“The policy **was enacted** last year,” the memo **purports**. → The memo purports the policy __________ the previous year.",
            ],
            answers="1 would disclose · 2 were negotiating · 3 had never witnessed · 4 had been enacted",
        ),
        dict(
            title="문법 2. 간접의문문",
            body="""**의문문 → 평서문 어순** (의문사 + 주어 + 동사)

> Do you know **where he lives**?  
> I wonder **whether the court will uphold** the ruling.  
> Tell me **what time the session adjourns**.

**간접의문에서 do/does/did 제거**  
> What **did** he say? → what he said  
> Where **does** she work? → where she works""",
            practice=[
                "“Where does the evidence originate?” → The judge asked where __________ .",
                "“Has the witness testified?” → I asked whether the witness __________ .",
                "“Why were they forewarned?” → Do you know why __________ ?",
                "“When will the board convene?” → Please notify me when __________ .",
            ],
            answers="1 the evidence originated / originates · 2 had testified · 3 they had been forewarned / they were forewarned · 4 the board would convene",
        ),
        dict(
            title="문법 3. 명령·제안·요청 전달",
            body="""| 유형 | 패턴 |
|------|------|
| 명령 | tell/order + O + **to V** / **not to V** |
| 요청 | ask/request + O + **to V** |
| 제안 | suggest + **-ing** / suggest + that + (should) |
| 금지 | warn + O + **not to V** / forbid + O + **to V** |

> “**Submit** the report.” → He **told** me **to submit** the report.  
> “**Don't divulge** secrets.” → She **warned** us **not to divulge** secrets.  
> “**Let's convene** early.” → He **suggested convening** early.""",
            practice=[
                "“Please refrain from speculation.” → The chair __________ us __________ from speculation.",
                "“Broach the topic carefully.” → She advised him __________ the topic carefully.",
                "“Let's petition for reform.” → They suggested __________ for reform.",
                "“Do not mislead the public.” → Officials warned journalists __________ the public.",
            ],
            answers="1 asked / to refrain · 2 to broach · 3 petitioning · 4 not to mislead",
        ),
    ],
    8: [
        dict(
            title="문법 1. 관계부사 (where / when / why / how)",
            body="""| 관계부사 | 선행사 | = 전치사+which |
|----------|--------|----------------|
| where | place | in/at which |
| when | time | on/in which |
| why | reason | for which |
| how | way/method | in which (the way how ❌) |

> This is the region **where** migrants **sojourn** temporarily.  
> I remember the day **when** the treaty **was abrogated**.  
> Tell me the reason **why** they **evacuated** the city.""",
            practice=[
                "That is the village __________ he __________ (exile) for decades.",
                "Spring is the season __________ birds __________ (migrate) north.",
                "Do you know the reason __________ they __________ (relocate) headquarters?",
                "This is __________ researchers __________ (excavate) ancient artifacts.",
            ],
            answers="1 where / was exiled · 2 when / migrate · 3 why / relocated · 4 where / excavate",
        ),
        dict(
            title="문법 2. whose · of which · of whom",
            body="""**whose** = ~의 (사람·사물)  
> a nation **whose** borders **demarcate** ethnic divisions

**of which / of whom** (격식·사물)  
> the treaty, **the terms of which** were disputed  
> three scholars, **one of whom** **sojourned** abroad

**a/an/the + N + of which/whom** · **some/many/few + of which/whom**""",
            practice=[
                "They inhabit a region __________ water resources __________ (permeate) every valley.",
                "The report cited three studies, the conclusions __________ __________ (support) our view.",
                "She met diplomats __________ credentials __________ (verify) by the embassy.",
                "We visited ten sites, two __________ __________ (excavate) last summer.",
            ],
            answers="1 whose / permeate · 2 of which / supported · 3 whose / were verified · 4 of which / were excavated",
        ),
        dict(
            title="문법 3. 제한적 · 계속적 · which절 전체",
            body="""**제한적(콤마 ❌):** 선행사 **한정**  
> Students **who adhere** to guidelines succeed.

**계속적(콤마 ⭕):** **부가 정보**, that ❌  
> Seoul, **which hosts** global summits, attracts millions.

**which = 앞 절 전체**  
> The treaty **was abrogated**, **which** **provoked** international criticism.  
> (= and this provoked …)""",
            practice=[
                "My colleague who specializes in migration called. (동료 여럿) 콤마? (Y/N)",
                "The policy was enacted, __________ immediately __________ (provoke) debate.",
                "He failed to vacate the premises, __________ __________ (lead) to eviction.",
                "Scientists __________ research intersects with ours will collaborate.",
            ],
            answers="1 N · 2 which / provoked · 3 which / led · 4 whose",
        ),
    ],
    9: [
        dict(
            title="문법 1. 가정법 과거",
            body="""**If + 주어 + 과거, 주어 + would/could/might + 원형**  
(현재 사실과 **반대**)

> If I **were** in your position, I **would resign**.  
> If the law **mandated** disclosure, firms **could not** hide risks.

**be → were**(격식) · **If it were not for** = ~가 없다면  
> **If it were not for** evidence, the case **would collapse**.""",
            practice=[
                "If she __________ (know) the truth, she __________ (not / remain) silent.",
                "If governments __________ (enforce) the treaty, pollution __________ (decrease).",
                "If I __________ (be) you, I __________ (not / spurn) the offer.",
                "If it __________ (not / be) for your help, we __________ (fail).",
            ],
            answers="1 knew / would not remain · 2 enforced / would decrease · 3 were / would not spurn · 4 were not / would have failed",
        ),
        dict(
            title="문법 2. 가정법 과거완료 · 혼합 가정법",
            body="""**If + had p.p., would/could/might + have p.p.** (과거 사실 반대)  
> If they **had evacuated** earlier, fewer lives **would have been lost**.

**혼합:** if절(과거) + 주절(과거완료) 또는 반대  
> If he **were** more careful, he **would not have made** the error.  
> If you **had studied** law, you **would understand** the ruling now.""",
            practice=[
                "If the witness __________ (testify) truthfully, the verdict __________ (differ).",
                "If she __________ (not / brood) over setbacks, she __________ (achieve) more by now.",
                "If they __________ (empathize) with voters, they __________ (not / lose) the election.",
                "If I __________ (be) rich, I __________ (donate) to charity years ago.",
            ],
            answers="1 had testified / would have differed · 2 had not brooded / would have achieved · 3 had empathized / would not have lost · 4 were / would have donated",
        ),
        dict(
            title="문법 3. wish · as if · It's (high) time",
            body="""**I wish + 가정법**  
- 현재 유감: I wish I **knew** …  
- 과거 유감: I wish I **had known** …

**as if / as though** + 가정법  
> He talks **as if** he **owned** the company.  
> She looked **as if** she **had seen** a ghost.

**It's (high/about) time + 과거** (지금 하기 늦음)  
> It's high time we **took** action.""",
            practice=[
                "I wish I __________ (can) __________ (sympathize) more deeply.",
                "I wish they __________ (not / condemn) the proposal so harshly.",
                "He spends money as if he __________ (be) a billionaire.",
                "It's time the committee __________ (convene) an emergency session.",
            ],
            answers="1 could / sympathize · 2 had not condemned · 3 were · 4 convened",
        ),
    ],
    10: [
        dict(
            title="문법 1. 감정분사 쌍 (-ing vs -ed)",
            body="""| -ing (능동·일으킴) | -ed (수동·느낌) |
|---------------------|-----------------|
| a **bewildering** puzzle | a **bewildered** student |
| an **exasperating** delay | **exasperated** commuters |
| a **captivating** speech | **captivated** listeners |

**동사 → 분사 형용사:** amaze→amazing/amazed · perplex→perplexing/perplexed  
> The **mesmerizing** performance left us **mesmerized**.""",
            practice=[
                "The __________ (perplex) instructions left users __________ (perplex).",
                "An __________ (electrify) goal sent the crowd into __________ (electrify) cheers.",
                "She felt __________ (mortify) after the __________ (mortify) error.",
                "The __________ (fascinate) lecture kept students __________ (fascinate).",
            ],
            answers="1 perplexing / perplexed · 2 electrifying / electrified · 3 mortified / mortifying · 4 fascinating / fascinated",
        ),
        dict(
            title="문법 2. 분사구문 · 완료분사구문",
            body="""**분사구문** = 접속사+주어 생략, 부사적 역할

> **Having finished** the audit, they submitted the report.  
> **Not knowing** the rules, he violated protocol.  
> **Written** in plain language, the law is accessible.

**완료분사구문:** Having + p.p. (앞 절보다 **먼저**)  
> **Having been warned**, residents evacuated.""",
            practice=[
                "__________ (Agitate) by the news, investors sold shares.",
                "__________ (not / anticipate) the backlash, the firm apologized.",
                "__________ (Examine) thoroughly, the evidence was deemed insufficient.",
                "__________ (Complete) the survey, researchers analyzed the data.",
            ],
            answers="1 Agitated · 2 Not having anticipated · 3 (When) Examined / Having been examined · 4 Having completed",
        ),
        dict(
            title="문법 3. with + 명사 + 분사 · 독립분사구문",
            body="""**with + O + -ing/p.p./adj/prep**  
> He listened **with his eyes closed**.  
> She walked **with her assistant following** her.

**독립분사구문** (주어 다를 때)  
> **The weather being** fine, we continued the excavation.  
> **All things considered**, the policy succeeded.""",
            practice=[
                "He read the verdict with his hands __________ (tremble).",
                "She entered with reporters __________ (besiege) the entrance.",
                "__________ (Time / be) limited, we prioritized key questions.",
                "The treaty was signed with both nations __________ (satisfy).",
            ],
            answers="1 trembling · 2 besieging · 3 Time being · 4 satisfied",
        ),
    ],
    11: [
        dict(
            title="문법 1. 명사절 (that / whether / wh-)",
            body="""명사절 = 주어·목적어·보어 역할

> **That** inequality persists worries economists. (주어)  
> The data **indicate that** reforms **work**. (목적어)  
> The question is **whether** we **should intervene**. (보어)

**wh-절:** what / who / where / why / how · **평서 어순**  
> I don't understand **why** he **resigned**.""",
            practice=[
                "__________ the committee will convene remains uncertain.",
                "The report clarifies __________ caused the breach.",
                "Experts disagree on __________ the policy should be amended.",
                "It is obvious __________ he __________ (distort) the facts.",
            ],
            answers="1 Whether / When · 2 what · 3 whether · 4 that / distorted",
        ),
        dict(
            title="문법 2. It 가주어 · It 강조 구문",
            body="""**It + be + adj/n + to V / that절 / wh- to V**  
> **It** is crucial **to clarify** assumptions.  
> **It** surprised us **that** sales **declined**.

**It is/was + 강조부분 + that/who + …**  
> **It was** in 2020 **that** the law **was enacted**.  
> **It is** through evidence **that** claims **are vindicated**.""",
            practice=[
                "__________ is essential to annotate sources accurately.",
                "__________ appears that the assertion lacks support.",
                "It was the witness __________ __________ (testify) that changed the trial.",
                "It is by scrutinizing data __________ scientists __________ (refute) errors.",
            ],
            answers="1 It · 2 It · 3 who / testified · 4 that / refute",
        ),
        dict(
            title="문법 3. 부정어 도치",
            body="""**부정·제한 부사(구) 문두 → 조동사/be + 주어**

| 부정어 | 예 |
|--------|-----|
| never, seldom, rarely | **Never have I** witnessed such bias. |
| not only | **Not only did** she **summarize**, but she also critiqued. |
| only + 부사구 | **Only then did** I **realize** the flaw. |
| little | **Little did** he **know** the consequences. |
| no sooner | **No sooner had** I **left** than it rained. |

**So/Neither 도치:** So do I. / Neither can she.""",
            practice=[
                "I have never seen such rhetoric. → Never __________ I __________ such rhetoric.",
                "She did not only outline the thesis. → Not only __________ she __________ the thesis.",
                "I cannot affirm the claim. → Neither __________ I __________ the claim.",
                "Hardly had the session begun when protesters __________ (accost) delegates.",
            ],
            answers="1 have / seen · 2 did / outline · 3 can / affirm · 4 accosted",
        ),
    ],
    12: [
        dict(
            title="문법 1. 전치사 뉘앙스 심화",
            body="""| 전치사 | 핵심 뉘앙스 | 예 |
|--------|-------------|-----|
| by | ~까지; ~에 의해; ~옆 | by Friday / by experts |
| for | 목적·기간·대상 | for research / for years |
| of | 소유·속성·구성 | a scholar of renown |
| in/on/at | 시간·장소·상태 | in 2024 / on Monday / at risk |
| with/without | 동반·수단 | with caution |
| against | 대립·저항 | against the ruling |
| amid | ~속에서 | amid controversy |""",
            practice=[
                "The treaty was abrogated __________ mutual consent.",
                "She succeeded __________ persevering through setbacks.",
                "The findings were published __________ a peer-reviewed journal.",
                "Protests erupted __________ the proposed amendment.",
            ],
            answers="1 by / without · 2 by / through · 3 in · 4 against / over",
        ),
        dict(
            title="문법 2. 형용사·명사 + 전치사",
            body="""**자주 출제되는 결합**

| 형용사/명사 | 전치사 |
|-------------|--------|
| accord with | conform **to/with** |
| ascribe A **to** B | impute A **to** B |
| resort **to** | subscribe **to** |
| entrust A **to** B | consign A **to** B |
| affiliate **with** | collude **with** |
| succumb **to** | acquiesce **in/to** |""",
            practice=[
                "Historians ascribe the decline __________ poor governance.",
                "Critics assail the plan __________ lacking evidence.",
                "Many subscribe __________ the view that reform is urgent.",
                "He succumbed __________ pressure and resigned.",
            ],
            answers="1 to · 2 for · 3 to · 4 to",
        ),
        dict(
            title="문법 3. 구동사 (Phrasal Verbs)",
            body="""| 구동사 | 뜻 | 예 |
|--------|----|----|
| bring about | 야기하다 | Reforms **brought about** change. |
| call off | 취소하다 | They **called off** the summit. |
| carry out | 수행하다 | **Carry out** the audit. |
| come up with | 생각해내다 | **Come up with** a solution. |
| rule out | 배제하다 | **Rule out** fraud. |
| live up to | ~에 부응하다 | **Live up to** expectations. |
| run into | 마주치다 | **Run into** obstacles. |
| set forth | 제시·출발 | **Set forth** guidelines. |""",
            practice=[
                "Investigators could not __________ __________ bribery entirely.",
                "The panel __________ __________ a comprehensive proposal.",
                "Leaders must __________ __________ __________ their promises.",
                "Talks were __________ __________ due to security concerns.",
            ],
            answers="1 rule out · 2 came up with · 3 live up to · 4 called off",
        ),
    ],
    13: [
        dict(
            title="문법 1. 수일치 함정",
            body="""**단수 취급:** each/every/either/neither + 단수  
**one of + 복수 + who/that → 복수 동사** (선행사 one of those)  
> He is one of the scholars **who publish** widely.

**a number of + 복수 → 복수** / **the number of + 복수 → 단수**  
**more than one / many a → 단수**  
**시간·거리·금액·수량 단위 → 단수:** Ten dollars **is** enough.  
**집합명사:** the majority of + 복수 → 복수(사람) / 단수(전체)""",
            practice=[
                "Each of the reports __________ (contain) detailed appendices.",
                "A number of students __________ (petition) for reform.",
                "The number of applicants __________ (exceed) capacity.",
                "More than one expert __________ (contend) the data are flawed.",
            ],
            answers="1 contains · 2 have petitioned / petition · 3 exceeds · 4 contends",
        ),
        dict(
            title="문법 2. 관사 고급",
            body="""**the:** 유일·특정·알려진·악기· 상위/최상  
> **the** Internet · **the** poor · **the** United Nations

**무관사:** 추상·불가산 일반·학문·식사·운동·by+교통  
> **Education** matters. · by **train** · play **tennis**

**a/an:** 단수 가산 불특정 · **a university** (유음) · **an hour** (모음)  
**the vs 무관사:** go to **school**(학생) / go to **the school**(건물)""",
            practice=[
                "She holds __________ PhD in economics from __________ prestigious university.",
                "__________ majority voted in favor, but __________ minority dissented.",
                "He plays __________ violin and studies __________ law.",
                "After __________ brief adjournment, __________ session resumed.",
            ],
            answers="1 a / a · 2 The / the · 3 the / (무관사) · 4 a / the",
        ),
        dict(
            title="문법 3. 수량사 · 부분 표현",
            body="""| | 가산 | 불가산 |
|--|------|--------|
| 많은 | many, a number of | much, a great deal of |
| 거의 없는 | few, a few | little, a little |
| 비율 | a fraction of, a proportion of | an amount of |
| 전체 | all (the), the whole | all (the) |

**a few**(몇몇) vs **few**(거의 없음) · **a little** vs **little**  
**half of / two-thirds of + the + N**""",
            practice=[
                "Only __________ fraction of respondents supported the measure.",
                "There is __________ little evidence to substantiate the claim.",
                "__________ proportion of the budget was allocated to research.",
                "__________ few scholars dissent from the prevailing view.",
            ],
            answers="1 a · 2 very / too · 3 A large · 4 A",
        ),
    ],
    14: [
        dict(
            title="문법 1. 독해 신호어 (Transition Words)",
            body="""| 기능 | 신호어 |
|------|--------|
| 추가 | moreover, furthermore, in addition, likewise |
| 대조 | however, nevertheless, nonetheless, conversely |
| 원인 | because, since, owing to, due to |
| 결과 | therefore, thus, hence, consequently, as a result |
| 예시 | for instance, such as, namely |
| 양보 | although, even though, despite, in spite of |
| 결론 | in conclusion, to sum up, overall |""",
            practice=[
                "The evidence is weak; __________, the assertion remains popular.",
                "Renewable costs fell; __________, adoption accelerated.",
                "__________, the author critiques three competing theories.",
                "Many factors matter; __________, funding and governance stand out.",
            ],
            answers="1 however / nevertheless · 2 therefore / consequently · 3 In this excerpt / For instance · 4 for example / namely",
        ),
        dict(
            title="문법 2. 문장 압축 · 바꿔쓰기",
            body="""**긴 문 → 짧게**

1) **부사절 → 분사구문**  
Because he **was** tired → **Being** tired …

2) **관계절 → 분사/전치사구**  
students **who study** hard → students **studying** hard

3) **so…that / too…to / enough to**  
so complex that … → too complex **to** …

4) **명사화**  
The committee **decided** → The committee's **decision**""",
            practice=[
                "Because the data were incomplete, researchers postponed publication. → __________ incomplete, researchers postponed publication.",
                "The argument that he presented was compelling. → The argument __________ __________ was compelling.",
                "The passage is so dense that beginners cannot parse it. → The passage is too dense __________ __________ beginners.",
                "Although the rhetoric was polished, the logic was flawed. → __________ polished rhetoric, the logic was flawed.",
            ],
            answers="1 The data being / With the data being · 2 (that) he presented · 3 for / to parse · 4 Despite / Notwithstanding",
        ),
        dict(
            title="문법 3. 14일 고난도 종합",
            body="""14일 핵심 문법·어휘 종합 테스트입니다.""",
            practice=[
                "[가정] If I __________ (know) the outcome, I __________ (act) differently.",
                "[수동] The claim __________ (refute) by several independent studies.",
                "[간접] “Why did they evacuate?” → Do you know why __________ ?",
                "[관계] The treaty, __________ terms were disputed, was eventually abrogated.",
                "[도치] Never __________ researchers __________ such contradictory data.",
                "[영작] 그녀는 증언이 진실임을 단언했다.",
                "[영작] 비록 증거가 부족했지만, 배심원단은 유죄 판결을 내렸다.",
                "[독해] The inference is weak; __________, the conclusion is doubtful. (결과)",
            ],
            answers="""1 had known / would have acted · 2 has been refuted / was refuted · 3 they evacuated · 4 whose · 5 have / observed · 6 She avowed that the testimony was true. · 7 Although the evidence was insufficient, the jury returned a guilty verdict. · 8 therefore / thus / hence""",
        ),
    ],
}


def validate_vocab():
    seen = set()
    for day, words in sorted(DAY_WORDS.items()):
        assert len(words) == 30, f"Day {day}: {len(words)} words"
        assert len(set(words)) == 30, f"Day {day}: duplicates"
        for w in words:
            assert w not in seen, f"Day {day}: cross-day dup {w}"
            assert w in META, f"Day {day}: missing meta for {w}"
            seen.add(w)
    assert len(seen) == 420


def build_words(day: int) -> list[tuple]:
    rows = []
    for i, w in enumerate(DAY_WORDS[day], 1):
        pos, mean, ex = META[w]
        rows.append((i, w, pos, mean, ex))
    return rows


def make_quiz_a(day: int, words: list[str]) -> list[tuple[str, str, str]]:
    rng = random.Random(day * 1000)
    picks = words[:4]
    all_means = [META[w][1] for w in words]
    out = []
    for w in picks:
        correct = META[w][1]
        wrong = [m for m in all_means if m != correct]
        rng.shuffle(wrong)
        opts = wrong[:2] + [correct]
        rng.shuffle(opts)
        labels = ["(a)", "(b)", "(c)"]
        opt_str = " ".join(f"{labels[i]} {opts[i]}" for i in range(3))
        ans = ["a", "b", "c"][opts.index(correct)]
        out.append((w, opt_str, ans))
    return out


def make_quiz_b(day: int, words: list[str]) -> list[tuple[str, str]]:
    picks = words[4:8]
    out = []
    for w in picks:
        mean = META[w][1].split(";")[0].split("·")[0].strip()
        ex = META[w][2]
        blank = re.sub(re.escape(w), "__________", ex, count=1, flags=re.I)
        if blank == ex:
            blank = f"Please __________ the issue carefully. ({mean})"
        else:
            blank = f"{blank} ({mean})"
        out.append((blank, w))
    return out


def build_day(n: int) -> dict:
    words = build_words(n)
    word_list = DAY_WORDS[n]
    return dict(
        title=f"Day {n}",
        topic=DAY_TOPICS[n],
        words=words,
        quiz_a=make_quiz_a(n, word_list),
        quiz_b=make_quiz_b(n, word_list),
        grammar=GRAMMAR[n],
        checks=DAY_CHECKS[n],
    )


DAYS = {n: build_day(n) for n in range(1, 15)}


def md_escape_cell(s: str) -> str:
    return s.replace("|", "\\|")


def render_md(n: int, d: dict) -> str:
    lines = [
        f"# {BRAND} — {d['title']}",
        "",
        f"**주제:** {d['topic']}  ",
        "**분량:** 단어 30개 + 문법 3포인트",
        "",
        "---",
        "",
        "## 오늘의 단어 (30)",
        "",
        "| No. | Word | 품사 | 뜻 | 예문 |",
        "|-----|------|------|----|------|",
    ]
    for no, w, pos, mean, ex in d["words"]:
        lines.append(f"| {no} | {w} | {pos} | {md_escape_cell(mean)} | {md_escape_cell(ex)} |")
    lines += ["", "### 단어 확인 퀴즈", "", "**A. 뜻 고르기**", ""]
    for i, (w, opts, _) in enumerate(d["quiz_a"], 1):
        lines.append(f"{i}. {w} — {opts}  ")
    lines += ["", "**B. 빈칸 채우기**", ""]
    for i, (q, _) in enumerate(d["quiz_b"], 5):
        lines.append(f"{i}. {q}  ")
    lines += ["", "---", ""]
    for gi, g in enumerate(d["grammar"], 1):
        lines += [f"## {g['title']}", "", g["body"], "", f"### 연습 {gi}", ""]
        for i, p in enumerate(g["practice"], 1):
            lines.append(f"{i}. {p}  ")
        lines += ["", "---", ""]
    quiz_ans_a = " ".join(f"{i}-({a})" for i, (*_, a) in enumerate(d["quiz_a"], 1))
    quiz_ans_b = " · ".join(f"{i}. {a}" for i, (*_, a) in enumerate(d["quiz_b"], 5))
    lines += [f"## {d['title']} 정답", "", "**단어 퀴즈**  ", f"A: {quiz_ans_a}  ", f"B: {quiz_ans_b}", ""]
    for gi, g in enumerate(d["grammar"], 1):
        lines += [f"**연습 {gi}**  ", g["answers"], ""]
    lines += ["---", "", "## 오늘 복습 체크", ""]
    for c in d["checks"]:
        lines.append(f"- [ ] {c}  ")
    lines.append("")
    return "\n".join(lines)


def word_table_html(words):
    rows = []
    for n, w, pos, mean, ex in words:
        rows.append(
            "<tr>"
            f"<td>{n}</td>"
            f"<td class='word'>{H.escape(w)}</td>"
            f"<td class='pos'>{H.escape(pos)}</td>"
            f"<td>{H.escape(mean)}</td>"
            f"<td style=\"font-family:var(--font-en)\">{H.escape(ex)}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr><th>No.</th><th>Word</th><th>품사</th><th>뜻</th><th>예문</th></tr></thead>"
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
        elif line.startswith("- "):
            out.append(f"<li>{inline(line[2:])}</li>")
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
    nav = '<a href="index.html">홈</a>' + "".join(
        f'<a href="day{i}.html"' + (' class="active"' if i == n else "") + f">Day {i}</a>"
        for i in range(1, total_days + 1)
    )
    prev = f"day{n-1}.html" if n > 1 else None
    nxt = f"day{n+1}.html" if n < total_days else None
    prev_btn = f'<a class="btn ghost" href="{prev}">← 이전</a>' if prev else "<span></span>"
    next_btn = f'<a class="btn" href="{nxt}">다음 →</a>' if nxt else '<a class="btn" href="index.html">홈으로</a>'
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
  <link rel="stylesheet" href="styles.css" />
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
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="wrap">
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
        <li>단어를 읽고 예문을 소리 내어 말합니다.</li>
        <li>단어 퀴즈를 풀어 확인합니다.</li>
        <li>문법 설명을 본 뒤 연습 문제를 풉니다.</li>
        <li>정답은 각 항목의 ‘정답 보기’에서 확인합니다.</li>
      </ol>
      <p class="muted">1–5일: 핵심 문법 심화 · 6–14일: 수능형 문법·독해·종합</p>
    </section>

    <div class="index-grid">
      {''.join(cards)}
    </div>
  </div>
</body>
</html>
"""
    (HTML / "index.html").write_text(html, encoding="utf-8")


def update_readme():
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("중3→고1 예비 학습용", f"{LEVEL} 학습용")
    table = """| Day | 문법 | 단어 초점 |
|-----|------|-----------|
| 1 | 어휘 형성 · SVOC · 5형식 보어 | 학술·접두접미 동사 |
| 2 | 상태동사·시제 · 과거선택 · 미래완료 | 시간·지속 동사 |
| 3 | 조동사·수동·준조동 should | 의무·규범 동사 |
| 4 | to V vs V-ing · 관계사 | 의지·태도 동사 |
| 5 | 상관접속·비교 · 중간 종합 | 사회·가치 동사 |
| 6 | 현재완료·완료진행·과거완료 | 분석·연구 동사 |
| 7 | 간접화법·간접의문·명령 전달 | 발표·증언 동사 |
| 8 | 관계부사·whose·계속적 | 이동·공간 동사 |
| 9 | 가정법·wish·as if | 감정·태도 동사 |
| 10 | 감정분사·분사구문 | 감정 유발·수동 |
| 11 | 명사절·It강조·도치 | 논증·묘사 동사 |
| 12 | 전치사·구동사 | 전치사 결합 |
| 13 | 수일치·관사·수량사 | 수량·측정 |
| 14 | 독해 신호어·압축·종합 | 독해·논증 어휘 |"""
    if "## 14일 구성" in text:
        text = re.sub(r"\| Day \| 문법.*?(?=\n## )", table + "\n", text, flags=re.S)
    path.write_text(text, encoding="utf-8")


def main():
    validate_vocab()
    for n in range(1, 15):
        d = DAYS[n]
        (MD / f"day{n}.md").write_text(render_md(n, d), encoding="utf-8")
        (HTML / f"day{n}.html").write_text(render_html(n, d), encoding="utf-8")
        print(f"wrote day{n}.md / day{n}.html")
    write_index()
    update_readme()
    css = HTML / "styles.css"
    if css.exists():
        text = css.read_text(encoding="utf-8")
        if "font-size: 0.8rem" not in text and "font-size: 0.9rem;" in text:
            css.write_text(text.replace("font-size: 0.9rem;", "font-size: 0.8rem;"), encoding="utf-8")
    print("done — 14 md + 14 html generated")


if __name__ == "__main__":
    main()
