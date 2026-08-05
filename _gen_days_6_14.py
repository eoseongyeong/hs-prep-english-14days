#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Day 6-14 markdown + HTML for 고등예비영문 course."""
from pathlib import Path
import html as H

ROOT = Path(__file__).resolve().parent
MD = ROOT / "md"
HTML = ROOT / "html"
MD.mkdir(exist_ok=True)
HTML.mkdir(exist_ok=True)

def W(*rows):
    return rows

DAYS = {}

DAYS[6] = dict(
    title="Day 6",
    topic="현재완료 심화 · 현재완료진행 · 과거완료",
    words=W(
        (1,"absorb","v.","흡수하다; 몰두하다","Plants absorb water."),
        (2,"adapt","v.","적응하다","Animals adapt to climate."),
        (3,"analyze","v.","분석하다","Analyze the data carefully."),
        (4,"approach","v./n.","접근하다; 접근법","She approached the problem."),
        (5,"assume","v.","가정하다","Don't assume too much."),
        (6,"conclude","v.","결론을 내리다","We concluded the meeting."),
        (7,"contribute","v.","기여하다","Everyone contributed ideas."),
        (8,"define","v.","정의하다","Define the key terms."),
        (9,"demonstrate","v.","입증하다; 시연하다","This demonstrates the rule."),
        (10,"estimate","v./n.","추정하다; 추정","Estimate the cost."),
        (11,"identify","v.","확인하다; 식별하다","Identify the main idea."),
        (12,"indicate","v.","나타내다","The sign indicates danger."),
        (13,"interpret","v.","해석하다","How do you interpret this?"),
        (14,"observe","v.","관찰하다","Scientists observe animals."),
        (15,"predict","v.","예측하다","Can you predict the result?"),
        (16,"complex","a.","복잡한","It is a complex issue."),
        (17,"constant","a.","끊임없는; 일정한","Keep a constant speed."),
        (18,"flexible","a.","유연한","Be flexible in your plans."),
        (19,"logical","a.","논리적인","Give a logical reason."),
        (20,"obvious","a.","분명한","The answer is obvious."),
        (21,"precise","a.","정확한","Need a precise measurement."),
        (22,"relevant","a.","관련된","Stay relevant to the topic."),
        (23,"sufficient","a.","충분한","We have sufficient time."),
        (24,"theory","n.","이론","Test the theory."),
        (25,"evidence","n.","증거","Find strong evidence."),
        (26,"factor","n.","요인","Many factors matter."),
        (27,"feature","n./v.","특징; 특징으로 하다","Safety is a key feature."),
        (28,"function","n./v.","기능; 기능하다","What is its function?"),
        (29,"range","n./v.","범위; 이르다","A wide range of topics."),
        (30,"source","n.","출처; 원천","Check the source."),
    ),
    quiz_a=[
        ("absorb","(a) 적응하다 (b) 흡수하다 (c) 분석하다","b"),
        ("predict","(a) 예측하다 (b) 관찰하다 (c) 정의하다","a"),
        ("relevant","(a) 충분한 (b) 관련된 (c) 분명한","b"),
        ("evidence","(a) 이론 (b) 요인 (c) 증거","c"),
    ],
    quiz_b=[
        ("Plants __________ sunlight. (흡수하다)","absorb"),
        ("Please __________ the results. (분석하다)","analyze"),
        ("We need __________ information. (충분한)","sufficient"),
        ("What is the __________ of this tool? (기능)","function"),
    ],
    grammar=[
        dict(title="문법 1. 현재완료 심화 (already / yet / just / ever / never / for / since)",
             body="""**형태:** have/has + p.p.

| 표현 | 의미 | 예 |
|------|------|----|
| already | 이미 (긍정) | I **have already finished**. |
| yet | 아직 (부정·의문) | **Have** you finished **yet**? |
| just | 방금 | She **has just arrived**. |
| ever / never | 경험 | **Have** you **ever** tried this? |
| for + 기간 | ~동안 | He **has lived** here **for** 3 years. |
| since + 시점 | ~이래로 | She **has studied** English **since** 2020. |

**주의:** ago는 단순과거와 함께 — I met her **two years ago**. (현재완료+ago ❌)""",
             practice=[
                 "She __________ (already / analyze) the report.",
                 "__________ you __________ (identify) the problem yet?",
                 "They have lived here __________ 2019. (since/for)",
                 "I have known him __________ ten years. (since/for)",
             ],
             answers="1 has already analyzed · 2 Have / identified · 3 since · 4 for"),
        dict(title="문법 2. 현재완료진행 (have been -ing)",
             body="""**형태:** have/has been + -ing  
**쓰임:** 과거부터 지금까지 **계속**되는 동작 강조

> I **have been studying** for two hours.  
> It **has been raining** since morning.

- 완료·결과·경험 → 현재완료  
- 계속·진행 강조 → 현재완료진행""",
             practice=[
                 "She __________ (wait) for an hour. (계속)",
                 "We __________ (observe) the birds all morning.",
                 "He looks tired. He __________ (work) hard.",
                 "I __________ (know) her since childhood. (상태→현재완료)",
             ],
             answers="1 has been waiting · 2 have been observing · 3 has been working · 4 have known"),
        dict(title="문법 3. 과거완료 (had + p.p.)",
             body="""**형태:** had + 과거분사 · 과거보다 **더 이전**(대과거)

> When I arrived, the train **had left**.  
> By the time we arrived, they **had already started**.

**과거완료진행:** had been + -ing  
> He **had been waiting** for an hour when she came.""",
             practice=[
                 "After he __________ (analyze) the data, he wrote a report.",
                 "By the time we got there, the show __________ (start).",
                 "She said she __________ (never / see) such evidence.",
                 "They __________ (wait) for 20 minutes when the bus came.",
             ],
             answers="1 had analyzed · 2 had started · 3 had never seen · 4 had been waiting"),
    ],
    checks=["단어 30개 확인", "현재완료 신호어", "현재완료진행", "과거완료"],
)

DAYS[7] = dict(
    title="Day 7",
    topic="간접화법 · 간접의문문 · 시제 일치",
    words=W(
        (1,"announce","v.","발표하다","They announced the winner."),
        (2,"claim","v./n.","주장하다; 주장","He claimed he was right."),
        (3,"confirm","v.","확인하다","Please confirm your email."),
        (4,"convince","v.","설득하다","She convinced me to join."),
        (5,"declare","v.","선언하다","They declared independence."),
        (6,"deny","v.","부인하다","He denied the rumor."),
        (7,"inform","v.","알리다","Inform me of any change."),
        (8,"insist","v.","주장하다, 고집하다","She insisted on leaving."),
        (9,"persuade","v.","설득하다","I persuaded him to stay."),
        (10,"propose","v.","제안하다","He proposed a new plan."),
        (11,"recommend","v.","추천하다","I recommend this book."),
        (12,"remind","v.","상기시키다","Remind me to call."),
        (13,"reply","v./n.","대답하다; 답장","She replied to my letter."),
        (14,"request","v./n.","요청하다; 요청","He requested more time."),
        (15,"warn","v.","경고하다","They warned us of danger."),
        (16,"brief","a./n.","짧은; 요약","Give a brief summary."),
        (17,"clear","a.","명확한","Be clear in your reply."),
        (18,"direct","a./v.","직접적인; 지시하다","Ask a direct question."),
        (19,"formal","a.","공식적인","Use formal language."),
        (20,"honest","a.","정직한","Give an honest answer."),
        (21,"polite","a.","공손한","Be polite to others."),
        (22,"reliable","a.","믿을 수 있는","He is a reliable source."),
        (23,"sincere","a.","진실한","Her apology was sincere."),
        (24,"conversation","n.","대화","We had a long conversation."),
        (25,"discussion","n.","토론","Join the discussion."),
        (26,"message","n.","메시지","Leave a message."),
        (27,"opinion","n.","의견","Share your opinion."),
        (28,"statement","n.","진술, 성명","Read the statement."),
        (29,"speech","n.","연설; 말","He gave a short speech."),
        (30,"truth","n.","진실","Tell the truth."),
    ),
    quiz_a=[
        ("deny","(a) 부인하다 (b) 발표하다 (c) 추천하다","a"),
        ("persuade","(a) 경고하다 (b) 설득하다 (c) 확인하다","b"),
        ("reliable","(a) 공손한 (b) 짧은 (c) 믿을 수 있는","c"),
        ("opinion","(a) 의견 (b) 진실 (c) 메시지","a"),
    ],
    quiz_b=[
        ("Please __________ your reservation. (확인하다)","confirm"),
        ("She __________ me to study harder. (설득하다)","persuaded/convinced"),
        ("He made a __________ statement. (공식적인)","formal"),
        ("What is your __________ on this issue? (의견)","opinion"),
    ],
    grammar=[
        dict(title="문법 1. 간접화법 (Reported Speech)",
             body="""직접화법 → 간접화법: 따옴표 없이 내용 전달

> He said, “I am busy.” → He said (that) he **was** busy.

전달 동사가 과거면 시제 후진: am→was, will→would, can→could, have→had, 현재완료→과거완료  
대명사·시간 부사도 조정 (today→that day, tomorrow→the next day).""",
             practice=[
                 "She said, “I need more time.” → She said she __________ more time.",
                 "He said, “I will reply tomorrow.” → He said he __________ the next day.",
                 "They said, “We have finished.” → They said they __________ .",
                 "She said, “I can help you.” → She said she __________ help me.",
             ],
             answers="1 needed · 2 would reply · 3 had finished · 4 could"),
        dict(title="문법 2. 간접의문문",
             body="""의문문을 전달할 때 **평서문 어순**(주어+동사)

> Tell me **what you want**. / I wonder **where she is**.  
> Ask him **if/whether he is ready**.

do/does/did는 간접의문에서 제거: What did he say? → what he said""",
             practice=[
                 "Where does he live? → Do you know where __________ ?",
                 "What time is it? → Tell me what time __________ .",
                 "Did she confirm it? → I asked if she __________ it.",
                 "Why are they late? → I wonder why __________ .",
             ],
             answers="1 he lives · 2 it is · 3 confirmed · 4 they are late"),
        dict(title="문법 3. say / tell / ask · 명령문 전달",
             body="""- **say** (to 사람) that… / **tell** + 사람 that…  
- **tell/ask** + 사람 + **to V**  
- 부정 명령: tell 사람 **not to V**

> She told me **to wait**. / He told me **not to go**.""",
             practice=[
                 "He (said / told) me the truth.",
                 "She asked me __________ open the window.",
                 "“Don’t be late,” he said. → He told me __________ late.",
                 "Tell me __________ you are free. (whether/if)",
             ],
             answers="1 told · 2 to · 3 not to be · 4 whether/if"),
    ],
    checks=["단어 30개 확인", "간접화법 시제", "간접의문 어순", "say/tell/ask"],
)

DAYS[8] = dict(
    title="Day 8",
    topic="관계부사 · whose · 계속적 용법",
    words=W(
        (1,"locate","v.","위치를 찾다; 위치하다","Locate the nearest station."),
        (2,"occupy","v.","차지하다","Books occupy the shelf."),
        (3,"occur","v.","발생하다","Accidents occur suddenly."),
        (4,"surround","v.","둘러싸다","Trees surround the park."),
        (5,"travel","v./n.","여행하다; 여행","They travel abroad."),
        (6,"visit","v./n.","방문하다; 방문","Visit the museum."),
        (7,"wander","v.","거닐다, 헤매다","We wandered around town."),
        (8,"abandon","v.","버리다, 포기하다","Don't abandon your dream."),
        (9,"arrive","v.","도착하다","We arrived at noon."),
        (10,"depart","v.","출발하다","The train departs soon."),
        (11,"explore","v.","탐험하다","Explore new places."),
        (12,"remain","v.","남다","Little time remains."),
        (13,"return","v./n.","돌아가다; 복귀","Return home safely."),
        (14,"settle","v.","정착하다; 해결하다","They settled in Seoul."),
        (15,"spread","v.","퍼지다","News spread quickly."),
        (16,"distant","a.","먼","a distant village"),
        (17,"local","a./n.","지역의; 현지인","local food"),
        (18,"rural","a.","시골의","rural areas"),
        (19,"urban","a.","도시의","urban life"),
        (20,"vast","a.","광대한","a vast ocean"),
        (21,"crowded","a.","붐비는","a crowded street"),
        (22,"familiar","a.","익숙한","a familiar place"),
        (23,"foreign","a.","외국의","a foreign country"),
        (24,"destination","n.","목적지","a popular destination"),
        (25,"direction","n.","방향","Ask for directions."),
        (26,"distance","n.","거리","Keep your distance."),
        (27,"location","n.","위치","a perfect location"),
        (28,"path","n.","길, 경로","Follow the path."),
        (29,"region","n.","지역","a mountain region"),
        (30,"route","n.","경로, 노선","the shortest route"),
    ),
    quiz_a=[
        ("occur","(a) 발생하다 (b) 탐험하다 (c) 정착하다","a"),
        ("abandon","(a) 도착하다 (b) 버리다 (c) 퍼지다","b"),
        ("urban","(a) 시골의 (b) 먼 (c) 도시의","c"),
        ("destination","(a) 목적지 (b) 거리 (c) 방향","a"),
    ],
    quiz_b=[
        ("Where did the accident __________? (발생하다)","occur"),
        ("They __________ for a better life. (정착하다)","settled"),
        ("She prefers __________ areas to cities. (시골의)","rural"),
        ("What is the best __________ to the airport? (경로)","route"),
    ],
    grammar=[
        dict(title="문법 1. 관계부사 (where / when / why / how)",
             body="""| 관계부사 | 예 |
|----------|----|
| where | the place **where** we met (= in which) |
| when | the day **when** I arrived (= on which) |
| why | the reason **why** he left |
| how | This is **how** it works. (the way how ❌) |""",
             practice=[
                 "This is the town __________ I grew up.",
                 "I remember the day __________ we first met.",
                 "Tell me the reason __________ you were late.",
                 "That is __________ they settled here.",
             ],
             answers="1 where · 2 when · 3 why · 4 how"),
        dict(title="문법 2. whose (소유격 관계대명사)",
             body="""**whose** = ~의 (사람·사물)

> a writer **whose** books are famous  
> a house **whose** roof is red""",
             practice=[
                 "I met a teacher __________ method is unique.",
                 "They live in a building __________ walls are thin.",
                 "She is the scientist __________ research is famous.",
                 "This is a company __________ products are reliable.",
             ],
             answers="1~4 whose"),
        dict(title="문법 3. 제한적 vs 계속적 용법",
             body="""- **제한적:** 콤마 없음 · 선행사 한정 — Students **who study hard** succeed.  
- **계속적:** 콤마 있음 · 추가 정보 — My father, **who is a teacher**, loves books.  
- 계속적 용법에서 **that 불가**, which/who ≈ and he/it""",
             practice=[
                 "My sister who lives in Busan called me. (자매 여럿) 콤마 필요? (Y/N)",
                 "My sister, who lives in Busan, called me. (자매 한 명) 올바름? (Y/N)",
                 "Seoul, that is the capital, is crowded. → Seoul, __________ is the capital…",
                 "He showed me his car, __________ he bought last week.",
             ],
             answers="1 N · 2 Y · 3 which · 4 which"),
    ],
    checks=["단어 30개 확인", "관계부사", "whose", "제한적/계속적"],
)

DAYS[9] = dict(
    title="Day 9",
    topic="가정법 과거 · 가정법 과거완료 · I wish / as if",
    words=W(
        (1,"appreciate","v.","고마워하다; 감상하다","I appreciate your help."),
        (2,"blame","v.","탓하다","Don't blame others."),
        (3,"doubt","v./n.","의심하다; 의심","I doubt his story."),
        (4,"forgive","v.","용서하다","Please forgive me."),
        (5,"hesitate","v.","망설이다","Don't hesitate to ask."),
        (6,"imagine","v.","상상하다","Imagine a better world."),
        (7,"strive","v.","노력하다, 애쓰다","Strive for excellence."),
        (8,"regret","v./n.","후회하다; 유감","I regret my decision."),
        (9,"suppose","v.","가정하다","Suppose you were rich."),
        (10,"suspect","v.","의심하다","I suspect a mistake."),
        (11,"tolerate","v.","참다, 용인하다","I can't tolerate lies."),
        (12,"trust","v./n.","신뢰하다; 신뢰","Trust your friends."),
        (13,"wish","v./n.","바라다; 소원","I wish you success."),
        (14,"worry","v./n.","걱정하다; 걱정","Don't worry too much."),
        (15,"wonder","v./n.","궁금하다; 놀라움","I wonder why."),
        (16,"anxious","a.","불안한; 열망하는","She feels anxious."),
        (17,"aware","a.","알고 있는","Be aware of risks."),
        (18,"confident","a.","자신 있는","Stay confident."),
        (19,"curious","a.","호기심 많은","Kids are curious."),
        (20,"grateful","a.","감사하는","I'm grateful for support."),
        (21,"jealous","a.","질투하는","Don't be jealous."),
        (22,"nervous","a.","긴장한","He looked nervous."),
        (23,"optimistic","a.","낙관적인","Stay optimistic."),
        (24,"regretful","a.","후회하는","He felt regretful."),
        (25,"condition","n.","조건; 상태","under this condition"),
        (26,"desire","n./v.","욕망; 갈망하다","a strong desire"),
        (27,"emotion","n.","감정","control your emotions"),
        (28,"fear","n./v.","두려움; 두려워하다","face your fear"),
        (29,"hope","n./v.","희망; 희망하다","never lose hope"),
        (30,"reality","n.","현실","face reality"),
    ),
    quiz_a=[
        ("regret","(a) 후회하다 (b) 용서하다 (c) 상상하다","a"),
        ("hesitate","(a) 탓하다 (b) 망설이다 (c) 신뢰하다","b"),
        ("grateful","(a) 질투하는 (b) 긴장한 (c) 감사하는","c"),
        ("reality","(a) 현실 (b) 감정 (c) 조건","a"),
    ],
    quiz_b=[
        ("I __________ your kindness. (고마워하다)","appreciate"),
        ("Don't __________ to ask questions. (망설이다)","hesitate"),
        ("She is __________ about the future. (낙관적인)","optimistic"),
        ("We must face __________. (현실)","reality"),
    ],
    grammar=[
        dict(title="문법 1. 가정법 과거 (현재 사실의 반대)",
             body="""**If + 주어 + 과거동사, 주어 + would/could/might + 원형**

> If I **were** rich, I **would travel** more.  
> If she **studied** harder, she **could pass**.

be동사는 인칭 무관 **were** 선호(격식).""",
             practice=[
                 "If I __________ (be) you, I would apologize.",
                 "If he __________ (have) time, he would help us.",
                 "If it __________ (not / rain), we could go out.",
                 "What __________ you do if you won the lottery? (would)",
             ],
             answers="1 were · 2 had · 3 did not rain · 4 would"),
        dict(title="문법 2. 가정법 과거완료 (과거 사실의 반대)",
             body="""**If + 주어 + had + p.p., 주어 + would/could/might + have + p.p.**

> If I **had known**, I **would have called**.  
> If she **had left** earlier, she **might have arrived** on time.""",
             practice=[
                 "If you __________ (tell) me, I would have helped.",
                 "If they __________ (not / miss) the bus, they would have been here.",
                 "She would have passed if she __________ (study) more.",
                 "I __________ (could / finish) it if I had had more time.",
             ],
             answers="1 had told · 2 had not missed · 3 had studied · 4 could have finished"),
        dict(title="문법 3. I wish / as if (though)",
             body="""**I wish + 가정법**
- 현재 유감: I wish I **knew** the answer.  
- 과거 유감: I wish I **had studied** harder.

**as if / as though**
> He talks **as if** he **were** an expert.  
> She looked **as if** she **had seen** a ghost.""",
             practice=[
                 "I wish I __________ (can) speak French. (현재)",
                 "I wish I __________ (not / say) that. (과거 유감)",
                 "He acts as if he __________ (own) the place.",
                 "She treated me as if she __________ (never / meet) me.",
             ],
             answers="1 could · 2 had not said · 3 owned/owned(were the owner) · 4 had never met"),
    ],
    checks=["단어 30개 확인", "가정법 과거", "가정법 과거완료", "I wish / as if"],
)

DAYS[10] = dict(
    title="Day 10",
    topic="분사 · 분사구문 · with 분사구문",
    words=W(
        (1,"amaze","v.","놀라게 하다","The news amazed us."),
        (2,"amuse","v.","즐겁게 하다","The joke amused me."),
        (3,"annoy","v.","짜증 나게 하다","Noise annoys neighbors."),
        (4,"astonish","v.","깜짝 놀라게 하다","His skill astonished us."),
        (5,"bore","v.","지루하게 하다","Long talks bore me."),
        (6,"confuse","v.","혼란스럽게 하다","The map confused us."),
        (7,"disappoint","v.","실망시키다","Don't disappoint them."),
        (8,"embarrass","v.","당황하게 하다","His mistake embarrassed him."),
        (9,"excite","v.","흥분시키다","The game excited fans."),
        (10,"frighten","v.","겁주게 하다","Thunder frightens dogs."),
        (11,"inspire","v.","고무하다","Teachers inspire students."),
        (12,"interest","v./n.","흥미롭게 하다; 관심","Science interests her."),
        (13,"satisfy","v.","만족시키다","The result satisfied us."),
        (14,"shock","v./n.","충격 주다; 충격","The news shocked me."),
        (15,"tire","v.","지치게 하다","Hard work tires me."),
        (16,"amazing","a.","놀라운 (능동 느낌)","an amazing story"),
        (17,"amazed","a.","놀란 (수동 느낌)","I was amazed."),
        (18,"boring","a.","지루한","a boring lecture"),
        (19,"bored","a.","지루해하는","I felt bored."),
        (20,"exciting","a.","흥미로운 (사물)","an exciting game"),
        (21,"excited","a.","흥분한 (사람)","excited students"),
        (22,"interesting","a.","재미있는 (사물)","an interesting book"),
        (23,"interested","a.","관심 있는 (사람)","interested in art"),
        (24,"tiring","a.","피곤하게 하는","a tiring day"),
        (25,"tired","a.","피곤한","a tired worker"),
        (26,"audience","n.","청중","The audience clapped."),
        (27,"expression","n.","표현; 표정","a facial expression"),
        (28,"impression","n.","인상","a good impression"),
        (29,"reaction","n.","반응","a quick reaction"),
        (30,"scene","n.","장면","an exciting scene"),
    ),
    quiz_a=[
        ("inspire","(a) 고무하다 (b) 짜증 나게 하다 (c) 실망시키다","a"),
        ("embarrass","(a) 즐겁게 하다 (b) 당황하게 하다 (c) 만족시키다","b"),
        ("bored","(a) 지루한(사물) (b) 흥미로운 (c) 지루해하는(사람)","c"),
        ("impression","(a) 인상 (b) 청중 (c) 장면","a"),
    ],
    quiz_b=[
        ("The movie __________ the audience. (놀라게 하다)","amazed"),
        ("Don't __________ your parents. (실망시키다)","disappoint"),
        ("I am __________ in history. (관심 있는)","interested"),
        ("That was a __________ journey. (피곤하게 하는)","tiring"),
    ],
    grammar=[
        dict(title="문법 1. 현재분사 · 과거분사",
             body="""- **현재분사 (-ing):** 능동·진행 / 감정을 **일으키는** 쪽  
- **과거분사 (p.p.):** 수동·완료 / 감정을 **느끼는** 쪽  

> an **exciting** game / **excited** fans  
> a **broken** window / the window **broken** yesterday""",
             practice=[
                 "The lecture was __________ (bore).",
                 "I felt __________ (bore) during the lecture.",
                 "Look at the __________ (sleep) baby.",
                 "Please throw away the __________ (break) cup.",
             ],
             answers="1 boring · 2 bored · 3 sleeping · 4 broken"),
        dict(title="문법 2. 분사구문",
             body="""분사구문 = 접속사·주어 생략한 부사절 압축

> **Walking** along the street, I met her.  
> (= While I was walking…)  
> **Written** in simple English, the book is easy.  
> (= Because it is written…)

**부정:** Not knowing the answer, I was silent.  
**완료:** Having finished homework, he went out.""",
             practice=[
                 "__________ (feel) tired, she went to bed early.",
                 "__________ (not / know) what to do, he called me.",
                 "__________ (finish) the test, they left the room. (완료)",
                 "__________ (build) in 1900, the house is historic.",
             ],
             answers="1 Feeling · 2 Not knowing · 3 Having finished · 4 Built"),
        dict(title="문법 3. with + 명사 + 분사 / 독립분사구문",
             body="""**with + 명사 + -ing/p.p.**  
> He sat **with his arms folded**.  
> She walked **with her dog following** her.

**독립분사구문** (주어가 다를 때)  
> **The weather being** fine, we went out.""",
             practice=[
                 "He fell asleep with the TV __________ (turn) on.",
                 "She listened with her eyes __________ (close).",
                 "__________ (It / be) rainy, we stayed home. → The weather being rainy… 또는 __________ rainy…",
                 "The teacher entered with students __________ (talk).",
             ],
             answers="1 turned · 2 closed · 3 Being · 4 talking"),
    ],
    checks=["단어 30개 확인", "-ing vs p.p. 형용사", "분사구문", "with 분사구문"],
)

DAYS[11] = dict(
    title="Day 11",
    topic="명사절 · It 가주어/강조 · 도치 입문",
    words=W(
        (1,"accept","v.","받아들이다","Accept the offer."),
        (2,"admit","v.","인정하다","He admitted his fault."),
        (3,"approve","v.","승인하다","Parents approved the plan."),
        (4,"concentrate","v.","집중하다","Concentrate on studying."),
        (5,"determine","v.","결정하다; 알아내다","Determine the cause."),
        (6,"emphasize","v.","강조하다","Emphasize key points."),
        (7,"evaluate","v.","평가하다","Evaluate your progress."),
        (8,"focus","v./n.","집중하다; 초점","Focus on the goal."),
        (9,"ignore","v.","무시하다","Don't ignore warnings."),
        (10,"mention","v.","언급하다","He mentioned the rule."),
        (11,"notice","v./n.","알아차리다; 공지","Did you notice that?"),
        (12,"overlook","v.","간과하다","Don't overlook details."),
        (13,"recognize","v.","알아보다; 인정하다","I recognize that face."),
        (14,"reveal","v.","드러내다","The test revealed gaps."),
        (15,"stress","v./n.","강조하다; 스트레스","Stress the main idea."),
        (16,"apparent","a.","명백한","It is apparent that…"),
        (17,"certain","a.","확실한","I'm certain of success."),
        (18,"crucial","a.","결정적인","a crucial moment"),
        (19,"essential","a.","필수적인","Essential skills matter."),
        (20,"likely","a.","~할 것 같은","She is likely to win."),
        (21,"particular","a.","특정한","a particular reason"),
        (22,"probable","a.","있을 법한","a probable result"),
        (23,"remarkable","a.","놀라운, 주목할 만한","a remarkable change"),
        (24,"fact","n.","사실","a scientific fact"),
        (25,"emphasis","n.","강조","put emphasis on practice"),
        (26,"issue","n.","문제, 쟁점","a social issue"),
        (27,"point","n.","요점","What's your point?"),
        (28,"priority","n.","우선순위","Health is a priority."),
        (29,"topic","n.","주제","today's topic"),
        (30,"view","n./v.","견해; 보다","in my view"),
    ),
    quiz_a=[
        ("admit","(a) 인정하다 (b) 무시하다 (c) 평가하다","a"),
        ("overlook","(a) 강조하다 (b) 간과하다 (c) 집중하다","b"),
        ("crucial","(a) 있을 법한 (b) 특정한 (c) 결정적인","c"),
        ("priority","(a) 우선순위 (b) 주제 (c) 사실","a"),
    ],
    quiz_b=[
        ("Please __________ on the lesson. (집중하다)","concentrate/focus"),
        ("Don't __________ small mistakes. (간과하다)","overlook"),
        ("Sleep is __________ for health. (필수적인)","essential"),
        ("Education is our top __________. (우선순위)","priority"),
    ],
    grammar=[
        dict(title="문법 1. 명사절 (that / whether / 의문사절)",
             body="""명사절 = 문장 속에서 명사 역할(주어·목적어·보어)

> **That** she passed surprised us. (주어)  
> I know **that** he is honest. (목적어)  
> The question is **whether** we should go.  
> I don't know **what** he wants.""",
             practice=[
                 "__________ he lied is clear. (That)",
                 "I wonder __________ she will accept. (whether/if)",
                 "Tell me __________ you need.",
                 "The point is __________ we must act now. (that)",
             ],
             answers="1 That · 2 whether/if · 3 what · 4 that"),
        dict(title="문법 2. It 가주어 · It 강조 구문",
             body="""**가주어 It**  
> **It** is important **to focus**.  
> **It** is clear **that** he is right.  
> **It** takes time **to improve**.

**강조 구문:** It is/was + 강조부분 + that/who…  
> **It was** John **who** called.  
> **It is** practice **that** matters.""",
             practice=[
                 "__________ is essential to sleep well.",
                 "__________ seems that she is busy.",
                 "It was yesterday __________ I met her.",
                 "It is honesty __________ I value most.",
             ],
             answers="1 It · 2 It · 3 that · 4 that"),
        dict(title="문법 3. 도치 입문 (부정어구 앞)",
             body="""부정·제한 부사구가 문두 → 조동사/be + 주어

> **Never have I** seen such a view.  
> **Not only did she** study, but she also taught.  
> **Only then did** I realize the truth.

so/neither 도치: So do I. / Neither can she.""",
             practice=[
                 "I have never seen it. → Never __________ I seen it.",
                 "She does not only sing. She also dances. → Not only __________ she sing…",
                 "I like coffee. (나도) → So __________ I.",
                 "He can't swim. (나도) → Neither __________ I.",
             ],
             answers="1 have · 2 does · 3 do · 4 can"),
    ],
    checks=["단어 30개 확인", "명사절", "It 가주어/강조", "도치 입문"],
)

DAYS[12] = dict(
    title="Day 12",
    topic="전치사 핵심 · 형용사+전치사 · 구동사",
    words=W(
        (1,"accuse","v.","고발하다 (+of)","They accused him of theft."),
        (2,"apologize","v.","사과하다 (+for)","Apologize for being late."),
        (3,"apply","v.","신청하다 (+for)","Apply for a visa."),
        (4,"belong","v.","속하다 (+to)","This belongs to me."),
        (5,"consist","v.","구성되다 (+of)","The team consists of 5."),
        (6,"depend","v.","의존하다 (+on)","It depends on you."),
        (7,"differ","v.","다르다 (+from)","A differs from B."),
        (8,"insist","v.","고집하다 (+on)","He insisted on going."),
        (9,"participate","v.","참여하다 (+in)","Participate in class."),
        (10,"recover","v.","회복하다 (+from)","Recover from illness."),
        (11,"refer","v.","언급하다 (+to)","Refer to the notes."),
        (12,"rely","v.","의지하다 (+on)","Rely on your team."),
        (13,"result","v.","결과로서 생기다 (+in/from)","Hard work results in success."),
        (14,"search","v.","찾다 (+for)","Search for the key."),
        (15,"succeed","v.","성공하다 (+in)","Succeed in the exam."),
        (16,"afraid","a.","두려워하는 (+of)","afraid of heights"),
        (17,"aware","a.","알고 있는 (+of)","aware of the risk"),
        (18,"capable","a.","할 수 있는 (+of)","capable of leading"),
        (19,"famous","a.","유명한 (+for)","famous for food"),
        (20,"fond","a.","좋아하는 (+of)","fond of music"),
        (21,"proud","a.","자랑스러운 (+of)","proud of you"),
        (22,"responsible","a.","책임이 있는 (+for)","responsible for safety"),
        (23,"similar","a.","비슷한 (+to)","similar to mine"),
        (24,"tired","a.","싫증 난 (+of) / 피곤한","tired of excuses"),
        (25,"advantage","n.","이점 (+of/over)","advantage of bikes"),
        (26,"attitude","n.","태도 (+toward/to)","attitude toward work"),
        (27,"cause","n.","원인 (+of)","cause of the fire"),
        (28,"effect","n.","영향 (+on)","effect on health"),
        (29,"reason","n.","이유 (+for)","reason for leaving"),
        (30,"solution","n.","해결책 (+to)","solution to the problem"),
    ),
    quiz_a=[
        ("consist","(a) ~로 구성되다 (b) 의지하다 (c) 참여하다","a"),
        ("rely","(a) 다르다 (b) 의지하다 (c) 회복하다","b"),
        ("capable","(a) 유명한 (b) 비슷한 (c) 할 수 있는","c"),
        ("solution","(a) 해결책 (b) 원인 (c) 이점","a"),
    ],
    quiz_b=[
        ("Success depends __________ effort. (전치사)","on"),
        ("She is proud __________ her team.","of"),
        ("He apologized __________ the mistake.","for"),
        ("There is no easy solution __________ this issue.","to"),
    ],
    grammar=[
        dict(title="문법 1. 핵심 전치사 뉘앙스",
             body="""| 전치사 | 핵심 | 예 |
|--------|------|----|
| in/on/at | 장소·시간 | in 2024 / on Monday / at 3 |
| by | ~까지; ~옆에; ~에 의해 | by Friday / by car / by him |
| for | 목적·기간·대상 | for health / for 2 hours |
| of | 소유·구성 | a friend of mine |
| with/without | 함께/없이 | with care |
| about/on | ~에 관하여 | a book on history |""",
             practice=[
                 "I'll finish it __________ Friday. (기한)",
                 "She was born __________ 2010.",
                 "We met __________ noon.",
                 "He went to school __________ foot.",
             ],
             answers="1 by · 2 in · 3 at · 4 on"),
        dict(title="문법 2. 형용사·명사 + 전치사",
             body="""자주 틀리는 결합을 암기:

afraid **of** / interested **in** / good **at** / similar **to**  
responsible **for** / famous **for** / proud **of** / capable **of**  
reason **for** / solution **to** / effect **on** / attitude **toward**""",
             practice=[
                 "She is interested __________ science.",
                 "He is good __________ math.",
                 "What is the reason __________ delay?",
                 "Smoking has a bad effect __________ lungs.",
             ],
             answers="1 in · 2 at · 3 for · 4 on"),
        dict(title="문법 3. 구동사 기초 (Phrasal Verbs)",
             body="""| 구동사 | 뜻 | 예 |
|--------|----|----|
| give up | 포기하다 | Don't give up. |
| look after | 돌보다 | look after kids |
| look for | 찾다 | look for keys |
| put off | 미루다 | put off a meeting |
| take off | 이륙하다; 벗다 | The plane took off. |
| turn down | 거절하다; 줄이다 | turn down an offer |
| find out | 알아내다 | find out the truth |
| go on | 계속하다 | go on speaking |""",
             practice=[
                 "Never __________ __________ your dream. (포기)",
                 "Please __________ __________ the baby. (돌보다)",
                 "They __________ __________ the picnic because of rain. (미루다)",
                 "I need to __________ __________ why he left. (알아내다)",
             ],
             answers="1 give up · 2 look after · 3 put off · 4 find out"),
    ],
    checks=["단어 30개 확인", "전치사 뉘앙스", "형용사+전치사", "구동사"],
)

DAYS[13] = dict(
    title="Day 13",
    topic="수일치 · 관사 · 대명사·수량사",
    words=W(
        (1,"add","v.","더하다","Add some sugar."),
        (2,"calculate","v.","계산하다","Calculate the total."),
        (3,"count","v.","세다","Count the votes."),
        (4,"decrease","v./n.","감소하다; 감소","Prices decreased."),
        (5,"double","v./a.","두 배로 하다; 이중의","Double the amount."),
        (6,"measure","v./n.","측정하다; 조치","Measure the length."),
        (7,"multiply","v.","곱하다","Multiply by three."),
        (8,"reduce","v.","줄이다","Reduce waste."),
        (9,"remain","v.","남다","Little remains."),
        (10,"total","v./a./n.","합계하다; 전체의; 합계","Total the scores."),
        (11,"amount","n.","양 (불가산)","a large amount of water"),
        (12,"average","n./a.","평균; 평균의","above average"),
        (13,"half","n./a.","절반","half of the class"),
        (14,"majority","n.","대다수","the majority of students"),
        (15,"number","n.","수 (가산)","a number of books"),
        (16,"percent","n.","퍼센트","20 percent of…"),
        (17,"portion","n.","부분, 몫","a large portion"),
        (18,"quantity","n.","수량","a small quantity"),
        (19,"several","a.","몇몇의","several options"),
        (20,"single","a.","단 하나의","a single mistake"),
        (21,"whole","a.","전체의","the whole day"),
        (22,"enough","a./ad.","충분한; 충분히","enough time"),
        (23,"extra","a.","여분의","extra money"),
        (24,"few","a.","거의 없는 (가산)","few people"),
        (25,"little","a.","거의 없는 (불가산)","little water"),
        (26,"many","a.","많은 (가산)","many students"),
        (27,"much","a.","많은 (불가산)","much time"),
        (28,"plenty","n.","많음","plenty of food"),
        (29,"pair","n.","한 쌍","a pair of shoes"),
        (30,"series","n.","연속, 시리즈","a series of events"),
    ),
    quiz_a=[
        ("decrease","(a) 감소하다 (b) 곱하다 (c) 더하다","a"),
        ("majority","(a) 절반 (b) 대다수 (c) 양","b"),
        ("few","(a) 많은 (b) 여분의 (c) 거의 없는(가산)","c"),
        ("series","(a) 시리즈 (b) 한 쌍 (c) 퍼센트","a"),
    ],
    quiz_b=[
        ("Please __________ the cost. (계산하다)","calculate"),
        ("A large __________ of water was used. (양)","amount"),
        ("There is __________ hope left. (거의 없는·불가산)","little"),
        ("__________ of the students agree. (대다수)","The majority / A majority"),
    ],
    grammar=[
        dict(title="문법 1. 수일치 (Subject-Verb Agreement)",
             body="""- 주어가 단수면 동사 단수, 복수면 복수  
- **every/each/one of** + 복수명사 → 단수 동사  
- **a number of** + 복수 → 복수 / **the number of** + 복수 → 단수  
- **people, police** → 복수  
- 시간·금액·거리 → 단수로 취급하는 경우 많음: Ten dollars **is** enough.""",
             practice=[
                 "Each of the students __________ (have) a book.",
                 "A number of books __________ (be) missing.",
                 "The number of students __________ (be) increasing.",
                 "Everyone __________ (want) success.",
             ],
             answers="1 has · 2 are · 3 is · 4 wants"),
        dict(title="문법 2. 관사 (a/an/the) · 무관사",
             body="""- **a/an:** 불특정 단수 가산  
- **the:** 특정·유일한·이미 나온 대상 / the sun, the best  
- 무관사: 복수·불가산 일반론, 고유명사(원칙), 운동·식사·학문 등 일부

> **Education** is important.  
> She goes to **school**. (학생으로서) / go to **the school** (건물)""",
             practice=[
                 "She bought __________ umbrella. (an)",
                 "__________ sun rises in the east.",
                 "I play __________ tennis every weekend.",
                 "Open __________ window, please. (특정)",
             ],
             answers="1 an · 2 The · 3 (무관사) · 4 the"),
        dict(title="문법 3. 대명사·수량사 (some/any/few/little)",
             body="""| | 가산 | 불가산 |
|--|------|--------|
| 많은 | many | much |
| 거의 없는(부정) | few | little |
| 조금 있는(긍정) | a few | a little |

- some: 긍정 / any: 부정·의문(요청·권유는 some)  
- another + 단수 / other + 복수 / the other(나머지 하나)""",
             practice=[
                 "There are __________ apples left. Just two. (a few/few)",
                 "There is __________ water. Not enough. (little/a little)",
                 "Would you like __________ tea? (some/any)",
                 "I have two pens. One is blue, __________ is black.",
             ],
             answers="1 a few · 2 little · 3 some · 4 the other"),
    ],
    checks=["단어 30개 확인", "수일치", "관사", "수량사 few/little"],
)

DAYS[14] = dict(
    title="Day 14",
    topic="독해 신호어 · 문장 압축 복습 · 14일 종합",
    words=W(
        (1,"summarize","v.","요약하다","Summarize the paragraph."),
        (2,"compare","v.","비교하다","Compare A with B."),
        (3,"contrast","v./n.","대조하다; 대조","Contrast the two ideas."),
        (4,"infer","v.","추론하다","Infer the meaning."),
        (5,"imply","v.","암시하다","What does this imply?"),
        (6,"support","v./n.","지지하다; 근거","Support your claim."),
        (7,"oppose","v.","반대하다","Some oppose the plan."),
        (8,"organize","v.","조직하다; 정리하다","Organize your ideas."),
        (9,"outline","v./n.","개요를 잡다; 개요","Outline the essay."),
        (10,"paraphrase","v.","다른 말로 바꾸다","Paraphrase the sentence."),
        (11,"quote","v./n.","인용하다; 인용","Quote the author."),
        (12,"review","v./n.","검토하다; 복습","Review the notes."),
        (13,"scan","v.","훑어보다","Scan for keywords."),
        (14,"skim","v.","대충 읽다","Skim the article."),
        (15,"underline","v.","밑줄 치다","Underline key words."),
        (16,"main","a.","주요한","the main idea"),
        (17,"specific","a.","구체적인","specific examples"),
        (18,"general","a.","일반적인","a general rule"),
        (19,"detailed","a.","상세한","a detailed report"),
        (20,"overall","a./ad.","전반적인; 전반적으로","overall meaning"),
        (21,"therefore","ad.","그러므로","therefore we conclude"),
        (22,"however","ad.","그러나","however, it failed"),
        (23,"moreover","ad.","게다가","moreover, it is cheap"),
        (24,"nevertheless","ad.","그럼에도","nevertheless, try"),
        (25,"argument","n.","주장, 논증","a strong argument"),
        (26,"conclusion","n.","결론","draw a conclusion"),
        (27,"context","n.","맥락","in this context"),
        (28,"passage","n.","글, 지문","read the passage"),
        (29,"summary","n.","요약","write a summary"),
        (30,"theme","n.","주제","the theme of the story"),
    ),
    quiz_a=[
        ("infer","(a) 추론하다 (b) 인용하다 (c) 반대하다","a"),
        ("paraphrase","(a) 훑어보다 (b) 다른 말로 바꾸다 (c) 요약하다","b"),
        ("however","(a) 그러므로 (b) 게다가 (c) 그러나","c"),
        ("passage","(a) 지문 (b) 주제 (c) 맥락","a"),
    ],
    quiz_b=[
        ("__________ the main idea in one sentence. (요약하다)","Summarize"),
        ("What does the author __________? (암시하다)","imply"),
        ("__________, the plan was successful. (전반적으로)","Overall"),
        ("Read the __________ carefully. (지문)","passage"),
    ],
    grammar=[
        dict(title="문법 1. 독해 신호어 (Transition Words)",
             body="""| 기능 | 신호어 |
|------|--------|
| 추가 | and, also, moreover, in addition |
| 대조 | but, however, on the other hand, nevertheless |
| 원인·결과 | because, therefore, as a result, so |
| 예시 | for example, for instance, such as |
| 순서 | first, then, finally, next |
| 강조 | indeed, in fact, especially |
| 결론 | in conclusion, to sum up, overall |""",
             practice=[
                 "He was tired; __________, he finished the work. (대조)",
                 "It rained; __________, the game was canceled. (결과)",
                 "__________, renewable energy is essential. (결론)",
                 "Many fruits, __________ apples and pears, are healthy. (예시)",
             ],
             answers="1 however/nevertheless · 2 therefore/as a result · 3 In conclusion/Overall · 4 such as/for example"),
        dict(title="문법 2. 문장 압축 복습 (관계사·분사·접속사)",
             body="""긴 문장을 짧게 바꾸는 핵심 도구:

1) 관계사절 → 분사/형용사  
> people **who live** here → people **living** here  

2) 부사절 → 분사구문  
> **Because she was** tired → **Being** tired  

3) so…that / too…to / enough to  
> He is **so** tall **that** he can reach it.  
> He is tall **enough to** reach it.""",
             practice=[
                 "Students who study hard succeed. → Students __________ hard succeed.",
                 "Because he was confused, he asked again. → __________ confused, he asked again.",
                 "The box is so heavy that I can't lift it. → The box is too heavy __________ .",
                 "She left early so that she could arrive on time. → She left early __________ arrive on time.",
             ],
             answers="1 studying · 2 Being · 3 to lift · 4 to"),
        dict(title="문법 3. 14일 종합 미니테스트",
             body="""A~C를 풀어 14일 핵심을 점검하세요.""",
             practice=[
                 "[오류] If I am you, I would study more. → __________",
                 "[태] Someone has solved the problem. → The problem __________ .",
                 "[간접] Where does she live? → Do you know where __________ ?",
                 "[비교] This book is (useful) than that one. → __________",
                 "[전치사] She is interested ___ science / good ___ English.",
                 "[영작] 나는 그가 정직하다고 생각한다.",
                 "[영작] 비가 왔더라면, 우리는 집에 머물렀을 것이다.",
                 "[독해신호] 빈칸: The evidence is weak; _____, the claim is doubtful. (결과)",
             ],
             answers="""1 If I **were** you… · 2 has been solved · 3 she lives · 4 more useful · 5 in / at · 6 I think (that) he is honest. · 7 If it had rained, we would have stayed home. · 8 therefore/thus/as a result"""),
    ],
    checks=["단어 30개 확인", "독해 신호어", "문장 압축", "14일 종합 테스트"],
)


def md_escape_cell(s):
    return s.replace("|", "\\|")


def render_md(n, d):
    lines = []
    lines.append(f"# 고등예비영문 14일 핵심 — {d['title']}")
    lines.append("")
    lines.append(f"**주제:** {d['topic']}  ")
    lines.append("**분량:** 단어 30개 + 문법 3포인트")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 오늘의 단어 (30)")
    lines.append("")
    lines.append("| No. | Word | 품사 | 뜻 | 예문 |")
    lines.append("|-----|------|------|----|------|")
    for no, w, pos, mean, ex in d["words"]:
        lines.append(f"| {no} | {w} | {pos} | {md_escape_cell(mean)} | {md_escape_cell(ex)} |")
    lines.append("")
    lines.append("### 단어 확인 퀴즈")
    lines.append("")
    lines.append("**A. 뜻 고르기**")
    lines.append("")
    for i, (w, opts, _) in enumerate(d["quiz_a"], 1):
        lines.append(f"{i}. {w} — {opts}  ")
    lines.append("")
    lines.append("**B. 빈칸 채우기**")
    lines.append("")
    for i, (q, _) in enumerate(d["quiz_b"], 5):
        lines.append(f"{i}. {q}  ")
    lines.append("")
    lines.append("---")
    lines.append("")
    quiz_ans_a = " ".join(f"{i}-({a})" for i, (*_, a) in enumerate(d["quiz_a"], 1))
    quiz_ans_b = " · ".join(f"{i}. {a}" for i, (*_, a) in enumerate(d["quiz_b"], 5))
    for gi, g in enumerate(d["grammar"], 1):
        lines.append(f"## {g['title']}")
        lines.append("")
        lines.append(g["body"])
        lines.append("")
        lines.append(f"### 연습 {gi}")
        lines.append("")
        for i, p in enumerate(g["practice"], 1):
            lines.append(f"{i}. {p}  ")
        lines.append("")
        lines.append("---")
        lines.append("")
    lines.append(f"## {d['title']} 정답")
    lines.append("")
    lines.append("**단어 퀴즈**  ")
    lines.append(f"A: {quiz_ans_a}  ")
    lines.append(f"B: {quiz_ans_b}")
    lines.append("")
    for gi, g in enumerate(d["grammar"], 1):
        lines.append(f"**연습 {gi}**  ")
        lines.append(g["answers"])
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 오늘 복습 체크")
    lines.append("")
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


def md_inline_to_html(text):
    """Very small markdown subset to HTML for grammar bodies."""
    import re
    lines = text.strip().splitlines()
    out = []
    in_table = False
    table_rows = []
    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            return
        html_rows = []
        for i, row in enumerate(table_rows):
            cells = [c.strip() for c in row.strip("|").split("|")]
            tag = "th" if i == 0 else "td"
            if i == 1 and all(set(c) <= set("-: ") for c in cells):
                continue
            html_rows.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>")
        out.append("<table>" + "".join(html_rows) + "</table>")
        table_rows = []
        in_table = False

    def inline(s):
        s = H.escape(s)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        return s

    for line in lines:
        if line.strip().startswith("|"):
            in_table = True
            table_rows.append(line)
            continue
        else:
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
    # wrap consecutive li
    html = "\n".join(out)
    html = re.sub(r"(?:<li>.*?</li>\n?)+", lambda m: "<ul>" + m.group(0) + "</ul>", html, flags=re.S)
    return html


def render_html(n, d, total_days=14):
    quiz_a = "".join(f"<li>{H.escape(w)} — {H.escape(opts)}</li>" for w, opts, _ in d["quiz_a"])
    quiz_b = "".join(f"<li>{H.escape(q)}</li>" for q, _ in d["quiz_b"])
    quiz_ans_a = " ".join(f"{i}-({a})" for i, (*_, a) in enumerate(d["quiz_a"], 1))
    quiz_ans_b = " · ".join(f"{i}. {H.escape(a)}" for i, (*_, a) in enumerate(d["quiz_b"], 5))

    grammar_html = []
    for gi, g in enumerate(d["grammar"], 1):
        prac = "".join(f"<li>{H.escape(p)}</li>" for p in g["practice"])
        grammar_html.append(f"""
    <section class="card">
      <h2>{H.escape(g['title'])}</h2>
      <div class="grammar-box">{md_inline_to_html(g['body'])}</div>
      <h3>연습 {gi}</h3>
      <ol>{prac}</ol>
      <details class="answer"><summary>정답</summary>{H.escape(g['answers']).replace(chr(10), '<br>')}</details>
    </section>""")

    nav = '<a href="index.html">홈</a>' + "".join(
        f'<a href="day{i}.html"' + (' class="active"' if i == n else '') + f'>Day {i}</a>'
        for i in range(1, total_days + 1)
    )
    prev = f'day{n-1}.html' if n > 1 else None
    nxt = f'day{n+1}.html' if n < total_days else None
    prev_btn = f'<a class="btn ghost" href="{prev}">← 이전</a>' if prev else '<span></span>'
    next_btn = f'<a class="btn" href="{nxt}">다음 →</a>' if nxt else '<a class="btn" href="index.html">홈으로</a>'
    checks = "".join(f"<li>☐ {H.escape(c)}</li>" for c in d["checks"])

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>고등예비영문 14일 핵심 — {d['title']}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Noto+Sans+KR:wght@400;600;700&family=Source+Serif+4:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="wrap">
    <nav class="site-nav">{nav}</nav>
    <header class="hero">
      <p class="brand">고등예비영문 14일 핵심</p>
      <p>{d['title']} — {H.escape(d['topic'])}</p>
      <div class="meta">
        <span class="chip">단어 30</span>
        <span class="chip">문법 3</span>
        <span class="chip">중3→고1</span>
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


TOPICS_1_5 = [
    (1, "품사 · 문장 성분 · 5형식"),
    (2, "현재 · 과거 · 미래 표현"),
    (3, "조동사 · 수동태 · 현재완료"),
    (4, "to부정사 · 동명사 · 관계대명사"),
    (5, "접속사 · 비교 · 종합 테스트"),
]


def update_existing_day_nav():
    """Update Day1-5 HTML brand/nav to 14 days."""
    import re
    for i in range(1, 6):
        path = HTML / f"day{i}.html"
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        text = text.replace("고등예비영문 14일 핵심", "고등예비영문 14일 핵심")
        # rebuild nav
        nav = '<a href="index.html">홈</a>' + "".join(
            f'<a href="day{j}.html"' + (' class="active"' if j == i else '') + f'>Day {j}</a>'
            for j in range(1, 15)
        )
        text = re.sub(r'<nav class="site-nav">.*?</nav>', f'<nav class="site-nav">{nav}</nav>', text, flags=re.S)
        # fix next on day5
        if i == 5:
            text = text.replace('href="index.html">홈으로</a>', 'href="day6.html">다음 →</a>')
            # if ghost pattern different
            text = text.replace('<a class="btn" href="index.html">홈으로</a>', '<a class="btn" href="day6.html">다음 →</a>')
        path.write_text(text, encoding="utf-8")
        print("updated nav", path.name)


def write_index():
    cards = []
    all_topics = TOPICS_1_5 + [(n, DAYS[n]["topic"]) for n in range(6, 15)]
    for i, (n, topic) in enumerate(all_topics):
        delay = 0.03 * i
        cards.append(f"""
      <a class="index-card" href="day{n}.html" style="animation-delay:{delay:.2f}s">
        <p class="day">Day {n}</p>
        <p>{H.escape(topic)}</p>
      </a>""")
    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>고등예비영문 14일 핵심</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;600;700&family=Noto+Sans+KR:wght@400;600;700&family=Source+Serif+4:wght@600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <p class="brand">고등예비영문 14일 핵심</p>
      <p>중3→고1을 위한 영어 단어·문법 집중 코스. 하루 단어 30개 + 문법 3포인트.</p>
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
      <p class="muted">1–5일: 기초 문법 · 6–14일: 심화·독해·종합</p>
    </section>

    <div class="index-grid">
      {''.join(cards)}
    </div>
  </div>
</body>
</html>
"""
    (HTML / "index.html").write_text(html, encoding="utf-8")
    print("wrote index.html")


def main():
    for n in range(6, 15):
        d = DAYS[n]
        (MD / f"day{n}.md").write_text(render_md(n, d), encoding="utf-8")
        (HTML / f"day{n}.html").write_text(render_html(n, d), encoding="utf-8")
        print(f"wrote day{n}.md / day{n}.html")
    update_existing_day_nav()
    write_index()
    # light CSS tweak for more nav items
    css = HTML / "styles.css"
    text = css.read_text(encoding="utf-8")
    if "site-nav a" in text and "font-size: 0.8rem" not in text:
        text = text.replace("font-size: 0.9rem;", "font-size: 0.8rem;")
        css.write_text(text, encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
