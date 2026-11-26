# Scramble tab walkthrough — persona A1-Demii (CEFR A1)

26 Nov 2026 · scratch copy `/home/claude/wt/site/index.html` served on port 8101 · Playwright Chromium, 390x844 @2x, mobile + touch, iPhone Safari user agent · typing fallback for every answer (no microphone) · no backend (no request to script.google.com was made; the route was blocked anyway) · progress written only by tapping and typing in the real UI.
Files: `log.json` (48 exchanges, 24 cards, events, layout measurements, 54 checker probes), `shots/01…33`, `run.py` (the script that played her; every answer is in `PLAN`).

## 1. What she did

- Opened `?tab=sc`, read the banner, opened "How Scramble works", tapped **Scramble ▸** (got o1), then went through all 24 cards with **Draw another ▸** / **Draw a card ▸** / **All decks**.
- 52 phrase chips opened (2–3 on most cards), 73 typed answers, 5 taps on **Ask to repeat** (o3, o7, v2, v5, s3) plus one typed "I don't understand" (s7), 7 Hint taps, 4 **Move on** taps (o6-2, v7-1, v8-1, s4-2).
- Extras: debrief formation link (o6 → Formation 3), **Fly this card again** (v7), back from pre-flight, leave mid-card with the confirm (dismiss, then accept; nothing was saved — correct), **↺ Again** tile (o6, o2), Scramble again after all cards were seen (got v6, "second look"), radar on the home.
- Lesson mode: not used (teacher feature; this persona is the student alone).

## 2. Results

| | Cleared | Partial | Not yet |
|---|---|---|---|
| Cards (24) | 9 | 15 | 0 |
| Exchanges (48) | 30 | 17 | 1 |
| Office (avg 70%) | 4 | 4 | 0 |
| Visitors (avg 57%) | 2 | 6 | 0 |
| Social (avg 70%) | 3 | 5 | 0 |

6 answers were bounced as "too short" (never counted as a try). Radar after play (lowest first): Say the plan 0/6 · Ask politely 2/6 · Say what happened 3/7 · Ask a question 5/7 · Suggest 3/4.

Per card (what she typed → app verdict; "miss: x" = objective kinds still open after that try):

| Card | Lvl | Chips | Exchange 1 | Exchange 2 | Card stamp | Score |
|---|---|---|---|---|---|---|
| o1 Who does what? | A1 | 1 | "Hello. Khun Nok check invoice." (ok) = **Cleared** | "Wing Commander Anan sign payment." (ok) = **Cleared** | Cleared | 90% |
| o2 What's in the file? | A1 | 2 | "3" (too short) → "There are three invoice." (ok) = **Cleared** | "Yes. Invoice two date wrong." (ok) = **Cleared** | Cleared | 80% |
| o3 Not ready yet | A1–A2 | 2 | [Ask to repeat] → "Sorry Colonel. Report not finish." (miss: explain) → "Sorry Colonel Hayes, it isn't ready." (ok) = **Partial** | "Tomorow morning." (ok) = **Cleared** | Partial | 67% |
| o4 Check the details | A2 | 3 | "Hello Captain Ellis. You have invoice number?" (ok) = **Cleared** | "4 5 1. Thank you. Is US dollar?" (ok) = **Cleared** | Cleared | 70% |
| o5 Fix the meeting | A2 | 2 | "OK. You come what day?" (ok) = **Cleared** | "Room 204, floor 2. See you Thursday." (ok) = **Cleared** | Cleared | 80% |
| o6 Two more days | A2 | 2 | "Sorry. I not send. Have mistake." (miss: past) → "I'm sorry, I didn't send." (ok) = **Partial** | "I want two more day." (miss: request,time) → [Hint] → "Could I have two more day please?" (miss: time) → [Move on] = **Partial** | Partial | 40% |
| o7 The late payment | A2 | 2 | [Ask to repeat] → "Sorry Mr Mike. Bank detail wrong." (ok) = **Cleared** | "Friday we pay." (miss: plan) → "We will pay Friday." (ok) = **Partial** | Partial | 70% |
| o8 Ask the boss | A2–B1 | 3 | "Excuse me sir. I want signature." (miss: request) → "Could you sign this form please?" (ok) = **Partial** | "Yes sir. Bank close 3 o'clock. Thank you." (ok) = **Cleared** | Partial | 61% |
| v1 Where is the briefing room? | A2 | 2 | "Floor 2, next to lift." (ok) = **Cleared** | "9 am" (too short) → "It start 9 am." (ok) = **Cleared** | Cleared | 80% |
| v2 No booking | A2 | 2 | [Ask to repeat] → "I book three night. Please check again." (miss: explain,request) → "I have booking three night. Can you check?" (ok) = **Partial** | "4729" (too short) → "Yes. Number 4729." (ok) = **Cleared** | Partial | 53% |
| v3 Welcome to the base | A2 | 2 | "Welcome to base. How your flight?" (ok) = **Cleared** | "First go security office." (ok) = **Cleared** | Cleared | 80% |
| v4 Yesterday's meeting | A2 | 3 | "We talk travel budget. Boss say ok." (miss: past) → "Wing Commander Anan approve plan." (ok) = **Partial** | "No. I send today." (miss: plan) → [Hint] → "Not yet. I will send afternoon." (ok) = **Partial** | Partial | 47% |
| v5 Tomorrow's plan | A2 | 2 | "Again please" (too short) → "Tomorrow we go finance office 10 o'clock." (miss: plan) → "Tomorrow we are going to visit finance." (ok) = **Partial** | [Ask to repeat] → "Bring ID card please." (ok) = **Cleared** | Partial | 67% |
| v6 The taxi claim | A2–B1 | 3 | "I want receipt please." (miss: ask) → "How many receipt you have?" (ok) = **Partial** | "OK. You write this form please." (ok) = **Cleared** | Partial | 58% |
| v7 The transfer came back | B1 | 3 | "Sorry. Please send new bank detail today." (miss: plan) → [Hint] → "If you send today, we pay tomorrow." (miss: sorry,plan) → [Move on] = **Partial** | "I call you again." (miss: plan) → [Hint] → [Hint] → "I will call you." (ok) = **Partial** | Partial | 35% |
| v8 Status report | B1 | 3 | "Two payment pay already. One come back." (miss: past,past) → [Hint] → "Two payments were made. One payment return." (miss: past) → [Move on] = **Partial** | "Account number wrong." (ok) = **Cleared** | Partial | 35% |
| s1 What do you do? | A2 | 1 | "I work finance. I am accountant." (ok) = **Cleared** | "He sign payment." (ok) = **Cleared** | Cleared | 90% |
| s2 Welcome dinner | A2 | 2 | "Yes, I like spicy. You like?" (miss: ask) → "Do you like Thai food?" (ok) = **Partial** | "This one not spicy." (ok) = **Cleared** | Partial | 67% |
| s3 Your UK degree | A2 | 2 | [Ask to repeat] → "I study business." (ok) = **Cleared** | "Yes. I like. But very cold." (ok) = **Cleared** | Cleared | 80% |
| s4 Bangkok traffic | A2 | 2 | "I go by BTS. And you?" (ok) = **Cleared** | "Wat Pho very beautiful." (miss: suggest) → "You go Wat Pho." (miss: suggest) → [Move on] = **Not yet** | Partial | 53% |
| s5 Weekend plans | A2 | 2 | "I go home see my mother." (miss: plan) → "I going to visit my mother." (ok) = **Partial** | "You can go Chatuchak market." (ok) = **Cleared** | Partial | 60% |
| s6 A photo, please | A2–B1 | 3 | "Excuse me madam. Photo with you please?" (miss: request) → "Could we take photo with you?" (ok) = **Partial** | "Here, middle please. Thank you madam." (ok) = **Cleared** | Partial | 61% |
| s7 If you had a free week | B1 | 2 | "I don't understand" (repair) → "ไม่เข้าใจค่ะ" (too short) → "I go Chiang Mai." (miss: explain) → [Hint] → "I would go to Chiang Mai." (ok) = **Partial** | "You should go Phuket. Beach beautiful." (ok) = **Cleared** | Partial | 60% |
| s8 Saying goodbye | A2–B1 | 1 | "Thank you very much. Safe flight." (ok) = **Cleared** | "Goodbye" (too short) → "Goodbye. See you again." (ok) = **Cleared** | Cleared | 90% |
## 3. Is the app kind to an A1? Do hints help?

Kind: yes in tone. No red, no "wrong"; a missed turn says "Good start — one more thing" or "Not yet"; Move on gives "Let's keep moving" and the debrief says "You handled it with a little help". Grammar notes never lowered a stamp (verified: o1, s1 Cleared with a Verb -s note). Leaving a card mid-way saves nothing and does not touch the radar. No card ended as Not yet even on the B1 cards (v7 35%, v8 35%).

Not kind enough in four places:
1. One-word answers are bounced and do not count as a try, so **Move on never appears** (section 4, A1).
2. After a miss the coach only repeats the objective label in English ("Still to do: Suggest a place"). On s4-2 she missed twice, got no model, and gave up — although a hint at that point costs nothing (the stamp can no longer be Cleared).
3. Uninflected A1 English ("two more day", "not finish", "come back", "pay", "go" without "to") is rejected again and again, which contradicts "objectives, not exact sentences".
4. The percentage is harsh for a chip user: o4 was Cleared on every objective first time and shows 70%.

Hints: 7 taps in 6 exchanges. They got her through 3 (v4-2, v7-2 with the model, s7-1). They did not help in 3: o6-2 (she copied the frame but wrote "two more day" — rejected for the missing -s), v7-1 (frame "If you send …, we will …"; she dropped "will"), v8-1 (after the frame she wrote "One payment return" — rejected). In shot 13 the two frames run together as one line ("Could I have …, please? … two more days."), which reads like one odd sentence.

Repair: the button works every time and is praised ("Good move"); "I don't understand" typed is also accepted. But the short forms an A1 really uses are not (section 4, A6).

## 4. Where she was wrongly judged

### False negatives (fair A1 answer rejected) — all verified by running

| # | Card / objective | Text that failed | Why |
|---|---|---|---|
| A1 | any turn with one objective: o2-1, v1-2, v2-2, o3-2, s8-2 | "3", "Three.", "9 am", "9", "Nine.", "4729", "Tomorrow.", "Goodbye", "Bye." | `scEval` short test: under 3 words passes only when there are exactly 2 words. Speech recognition often writes a spoken number as digits ("4729"), so this probably hits voice users too (not tested: no microphone). Also `scCommit` does not count a short answer as a try: three one-word answers in a row on o2-1 left Tries: 0 and no Move on (shot 33). |
| A2 | o6-2 time | "I want two more day." / "Could I have two more day please?" / "Can I have two day more please?" | regex needs `days` |
| A3 | o3-1 explain | "Sorry Colonel. Report not finish." / "Not finish yet." | regex has `not finished` only |
| A4 | o6-1 past | "Sorry. I not send. Have mistake." / "Sorry. I forget." | needs did not / found / was |
| A5 | v2-1 explain + request | "I book three night. Please check again." | `book` missing; `please check` not a request here, yet v6-1 accepts "I want receipt please" as "Ask politely" (inconsistent) |
| A6 | repair phrase | "Again please" (run, v5), "Slowly please.", "Sorry?", "What?", "I not understand." (probes) | `SC_REPAIR` needs say/repeat + again, or "I do not understand" |
| A7 | v4-1 decided | "Boss say ok." / "Wing Commander say yes." / "Boss ok." | only `said yes/okay`, `approve…` |
| A8 | v5-1 plan | "Tomorrow we go finance office 10 o'clock." | `go to` required; "go" alone fails |
| A9 | v8-1 both | "Two payment pay already. One come back." / "One payment return." / "Two ok. One come back." | needs paid/made/sent and returned/came back |
| A10 | s4-2, s5-2 suggest | "Wat Pho very beautiful." / "You go Wat Pho." / "Chatuchak market is good." / "Grand Palace." | needs should/can/visit/`go to` |
| A11 | s2-1 ask back | "You like?" | needs do/can/are + you, or "and you" |
| A12 | s6-1, o8-1 request | "Excuse me madam. Photo with you please?" / "Sir, please sign this form." | needs could/would/can; perhaps intended for a senior, but then the coach should say so |
| A13 | Thai typed (s7) | "ไม่เข้าใจค่ะ" | normalises to empty → "A little more, please. Say a full sentence — three words or more." (shot 28) |

By-design strictness that still leaves an A1 at 0/6 on the radar: "Say the plan" needs will / going to (o7-2 "Friday we pay.", s5-1 "I go home see my mother.", v4-2 "No. I send today.", v7). The labels on o7, v5, s5 show the pattern; v4-2 and v7-2 do not.

### False positives (wrong or empty answer accepted) — verified by running scEval (probes in log.json; nothing saved)

| # | Card | Text accepted | Problem |
|---|---|---|---|
| B1 | o2-2 | "No problem. Invoice two ok." → both ✓ | says the opposite; `problem` alone is enough |
| B2 | s4-2 | "I see." → Suggest ✓ | bare `see`; the same regex rejects "You go Wat Pho." |
| B3 | o3-2 | "Yesterday morning." → ✓ | `morning` alone in `SC_DAY` |
| B4 | o1-2 | "I don't know who signs." → ✓ | bare `signs` |
| B5 | v6-1 | "I want receipt please." → Ask politely ✓ (run) | `please … receipt` branch; she also got the "I want → softer" note, so stamp and note disagree |
| B6 | s7-1 | "I want go Japan." → grammar note "Softer with a senior or a visitor: Could I have …" | wrong note: the `i want` slip only skips "want to go", and this is small talk, not a request |

Correctly handled: "Sorry Mr Mike" → Address note (o7); "Colonel Sarah" → name not credited + note; "Khun Nok check" → Verb -s note; "I going to" → Future note.

## 5. Thai line, chips, instructions at A1

- **Thai line**: accurate and natural on all 24 cards, right register (ท่าน for Colonel Hayes on v6), keeps ranks and names in English, and carries the facts she needs (room 204, 4729, Friday). It was the main reason she could answer Office cards. Gaps: (a) it is only on the card face and inside the folded "Situation" on the exchange screen; (b) nothing else is in Thai — objective labels ("Ask politely for more time", "Use the right name for her", "Suggest a place"), coach lines, "pre-flight", "Commit", "debrief", "top score → 90" are all above A1; (c) it never cues the address form (o3, s6, o8), which is the one objective an A1 cannot guess from "Use the right name for her".
- **Chips**: useful and stay available during the exchange (good). Problems: closed chips are blind ("Phrase 1/2/3"), so she pays 10 points to find out what it is; on o3 and o4 the greeting she needs first is chip 3; nothing shows which exchange a chip belongs to; the cost (100 → 70) punishes exactly the help an A1 needs.
- **Instructions**: the 5-step "How Scramble works" is folded at the very bottom of a 3,100 px home page. The banner paragraph is 44 words of B1 English.

## 6. Phone layout at 390 px (measured, `layout` in log.json)

- No horizontal overflow on any screen.
- The global header (logo, title, 5 buttons) takes about 245 px on every Scramble screen. On pre-flight the card face then fills the first screen and the **countdown, chips and I'M READY are below the fold** (page 1,286 px; shot 04 vs 05). On the exchange screen (page 1,259 px) the answer area sits under the person, objectives and chips, so every answer needs a scroll.
- Small tap targets: "⌨ Type instead" and "Move on ▸" 27 px high text links (102 px wide); 🔊 replay in the speech bubble 29x32; "Situation" summary 17 px high; Hint / Ask to repeat / 🔊 model / ↺ Again 36 px; header toggles 33 px. Apple's minimum is 44.
- Small text: stat labels 9.6 px; stamps, score strip, tile sub-lines, "Situation" 11.5–11.8 px; fine print and Hint/Repeat labels 12.5 px.
- Typing is not sticky: after every miss or "too short" the screen returns to the microphone and she must tap "Type instead" again (true on all 73 typed answers). After a typed miss the coach still says "Words on the screen wrong? Tap 'Say again' next time, or type."
- "Scramble ▸" is not a surprise until every card has been seen: it always deals the first unseen card (o1, then o2 …), the same as Draw another (verified: o1→o8 in order).
- Debrief formation link opens the formation, but its back button lands on the Formation Drills home; she has to find the Scramble tab again (verified).

## 7. Recommended improvements (ranked)

### P1 — bugs / unfair checks

1. **One-word answers and Move on** — `scEval` and `scCommit`. Change the short test to `if (w.length < 3 && !r.hits.every(Boolean))` so "3", "4729", "Tomorrow.", "Goodbye" pass when they do the whole job; in `scCommit`'s short/empty branch add `SCP.shorts = (SCP.shorts||0)+1` and show Move on in `scRenderSpeak` when `SCP.tries + SCP.shorts >= 2`. Failing texts verified-by-running; fix from-reading.
2. **o6-2 time**: `2 (more )?days` → `2 (more )?days?|2 days? more`. Verified failing: "Could I have two more day please?".
3. **o3-1 explain**: `not finished` → `not finish\w*`, add `not complete\w*|no ready|can not|not ok`. Verified failing: "Report not finish."
4. **v8-1**: obj 1 add `pay|ok|finish\w*|already` to the verb group (`(2|two)\b.*\b(paid|pay|made|sent|done|completed|ok|finish\w*)`); obj 2 `(returned|came back|…)` → `(return\w*|c[ao]mes? back|sent back|send back|reject\w*|back)`. Verified failing: "Two payment pay already. One come back.", "One payment return."
5. **Suggest regex (s4-2, s5-2, s7-2)**: `go to` → `go( to)?`; add `(is|very|so) (good|nice|beautiful|fun|famous)`; replace bare `see` with `(can|should|must|go|to) see`. Fixes A10 and B2 together. Verified failing/passing texts above.
6. **`SC_REPAIR`**: add `^(sorry|pardon|what|again|slowly)( please)?$|\b(again|slowly|slower|repeat) please\b|\bplease (again|slowly|repeat)\b|\bi (not|no|can not) (understand|hear|catch)\b`, and in `scEval` treat text with Thai characters and an empty norm as its own status with a Thai line ("พิมพ์เป็นภาษาอังกฤษนะคะ — or tap Ask to repeat"). Verified failing: "Again please", "Sorry?", Thai text.
7. **Other A1 forms**: o6-1 past add `(not|no) send|mistake|forg[eo]t`; v2-1 `booking|…` → `book\w*`, request add `please\b.*\bcheck|check\b.*\bplease`; v4-1 add `(says?|said) (yes|ok|okay)|\bok(ay)?\b`; v5-1 `go to` → `go( to)?`; s2-1 add `you like\b`. All failing texts verified-by-running.
8. **False positives**: o2-2 explain — require the hit not to follow "no " (`(^|[^o] )(problem|…)` is awkward without lookbehind; simplest: test `!/\bno (problem|mistake)\b/.test(n)` first); o3-2 drop bare `morning|afternoon` from the time check for this card (use `tomorrow|monday…|in \d+ days?`); o1-2 exclude `do not know`. Verified-by-running (probes).
9. **`i want` slip (SC_SLIPS row 15)**: exclusion `to (go|visit…)` → `(to )?(go|visit|travel|stay|see|eat|try…)`, and skip the note on Social-deck turns whose objective is not `request`. Verified: s7 "I want go Japan."
10. **Polite-request rule is inconsistent**: v6-1 accepts "I want receipt please"; o8-1/s6-1 reject "Sir, please sign this form." Pick one rule. Suggested: `please` + verb counts at the hotel desk (v2); with seniors keep could/would but make the coach say it: "With a senior: Could you …, please?". From-reading + probes.

### P2 — guidance for A1–A2

11. **Free hint after the first miss** — `scCommit`: when a try misses, set `SCP.lad = Math.max(SCP.lad, 1)` so "Start like this" shows at once (the stamp is already Partial at best, so it costs nothing). Would have rescued s4-2. From-reading; the stuck case is verified.
12. **Separate the hint frames** — `scCoachHTML`: one frame per line, each with its objective icon, instead of joining with a space (shot 13).
13. **Keep typing mode** — in `scCommit` (miss / short / repair branches) use `SCP.sub = SCP.typed ? "type" : "ready"`; hide the "Say again" sentence when `SCP.typed`. Verified-by-running (73/73 re-taps).
14. **Thai for the moves** — add a Thai gloss to `SC_KINDS` (ทักทาย, เรียกชื่อให้ถูก, ขออย่างสุภาพ, แนะนำ …) and show it under each objective and in "Still to do"; add a Thai hint for the address form on o3, o8, s6 ("เรียก Colonel Hayes หรือ Ma'am").
15. **Chips**: label closed chips by job ("💬 Greeting", "💬 Say the problem") instead of "Phrase 1", order them by exchange, and do not lower the cap for the first chip on A1/A1–A2 cards (or show the stamp big and the % small: o4 = Cleared on everything, 70%).
16. **Move on** as a real button (same size as Hint) and offered together with the Thai line "ข้ามได้ ไม่เป็นไร".

### P3 — polish

17. Phone header: hide the global header buttons while a card is open, or `scrollIntoView` the card; on pre-flight put the clock and chips above or beside the situation so they are on the first screen.
18. Tap targets to 44 px: `.gs-link`, `.gs-play`, `.sc-sitd summary`, `.dbtn`, `.hbtn`; raise 11–12 px text (`.sc-st`, `.gs-score`, `.sc-tile small`, `.cstat .k`) to 13 px or more.
19. "Scramble ▸": pick at random among unseen open cards (`scPick(null)` currently returns `unseen[0]`) so it differs from Draw a card.
20. Debrief formation link: remember the source and send the formation's back button to the Scramble home.
21. Move "How Scramble works" to the top (three short lines with Thai), shorten the banner paragraph.
