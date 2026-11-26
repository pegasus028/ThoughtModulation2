# Scramble tab walkthrough — B1-Demii (26 Nov 2026)

Persona: Ms. Demii at CEFR B1. Polite, varied answers (conditionals, would/could, passives, past and future forms), few chips, names spelled the way speech-to-text would (Erikson, Hays, Mam). Typing fallback only (no microphone in headless Chromium). iPhone 13 viewport 390x844 @2x. Scratch copy at /home/claude/wt/site, no backend; no request left localhost.

Files: `log.json` (every exchange, card results, 186 read-only checker probes), `shots/01…30-*.png` + `shots/extra/` (8 more), `shots/CAPTIONS.md`, `shots/boxes.json`, `plan.py` (what she typed), `fix.py` + `fix_check.json` (the proposed regexes, tested).

## What she did

- All 24 cards, both exchanges (50 exchanges with the v7 second look; 25 card runs; 64 typed answers; run time 138 s, no page errors).
- Drew cards three ways: deck "Draw a card" (9), debrief "Draw another" (14), the Scramble surprise button (v1), and a tile "Again" (v7 second look).
- Chips: 3 opened (o1 pre-flight, v7 pre-flight, s7 during the exchange after a miss). Top score fell to 90 each time, as designed.
- Repair: the "Ask to repeat" button (o3-2), a typed repair that was accepted (v2-2), and a typed polite repair that was not recognised (v2-2, see P1-2).
- Hint ladder and Move on: v7-2, two fair answers refused, Hint 1 (frame), Hint 2 (model), then Move on, "Not yet" stamp.
- Debrief links: formation link (v7 → Formation 10), Draw another, Fly this card again (via tile), All decks. Tools: Slow voice on/off, Voice & mic check opened and closed, "How Scramble works", a real microphone tap (blocked; clear message, typing still offered).
- Lesson mode: on, dealt s8, marked ✓ / ½, fluency 3, grammar note, saved both exchanges, debrief "Scored by the teacher", off again.

## Results per card (C = Cleared, P = Partial, N = Not yet)

| Card | Title | Lvl | Drawn by | Ex1 tries / stamps | Ex2 tries / stamps | Chips | Score | Stamp |
|---|---|---|---|---|---|---|---|---|
| o1 | Who does what? | A1 | Draw a card (office deck) | 1 / C C | 2 / P | 1 | 75% | Partial |
| o2 | What's in the file? | A1 | Draw another | 1 / C | 2 / P C | 0 | 83% | Partial |
| o3 | Not ready yet | A1–A2 | Draw a card (office deck) | 1 / C C | 1 / C | 0 | 100% | Cleared |
| o4 | Check the details | A2 | Draw another | 1 / C C | 1 / C C | 0 | 100% | Cleared |
| o5 | Fix the meeting | A2 | Draw a card (office deck) | 2 / P | 1 / C C | 0 | 83% | Partial |
| o6 | Two more days | A2 | Draw another | 1 / C C | 2 / P C | 0 | 88% | Partial |
| o7 | The late payment | A2 | Draw another | 1 / C C | 1 / C C | 0 | 100% | Cleared |
| o8 | Ask the boss | A2–B1 | Draw another | 1 / C C | 1 / C C | 0 | 100% | Cleared |
| v1 | Where is the briefing room? | A2 | Scramble (surprise) | 1 / C | 1 / C | 0 | 100% | Cleared |
| v2 | No booking | A2 | Draw another | 1 / C C | 2 / P | 0 | 83% | Partial |
| v3 | Welcome to the base | A2 | Draw a card (visitors deck) | 2 / C P | 1 / C | 0 | 83% | Partial |
| v4 | Yesterday's meeting | A2 | Draw another | 2 / C P | 2 / P | 0 | 67% | Partial |
| v5 | Tomorrow's plan | A2 | Draw another | 1 / C C | 1 / C | 0 | 100% | Cleared |
| v6 | The taxi claim | A2–B1 | Draw a card (visitors deck) | 1 / C C | 1 / C | 0 | 100% | Cleared |
| v7 | The transfer came back | B1 | Draw another | 2 / C P | 2 / N | 1 | 45% | Partial |
| v7b | The transfer came back | B1 | tile Again | 1 / C C | 1 / C | 0 | 100% | Cleared |
| v8 | Status report | B1 | Draw a card (visitors deck) | 1 / C C | 2 / P | 0 | 83% | Partial |
| s1 | What do you do? | A2 | Draw a card (social deck) | 1 / C | 1 / C | 0 | 100% | Cleared |
| s2 | Welcome dinner | A2 | Draw another | 1 / C C | 1 / C | 0 | 100% | Cleared |
| s3 | Your UK degree | A2 | Draw another | 1 / C | 1 / C C | 0 | 100% | Cleared |
| s4 | Bangkok traffic | A2 | Draw a card (social deck) | 1 / C C | 1 / C | 0 | 100% | Cleared |
| s5 | Weekend plans | A2 | Draw another | 2 / P | 1 / C | 0 | 75% | Partial |
| s6 | A photo, please | A2–B1 | Draw another | 1 / C C | 1 / C C | 0 | 100% | Cleared |
| s7 | If you had a free week | B1 | Draw a card (social deck) | 2 / P | 1 / C | 1 | 68% | Partial |
| s8 | Saying goodbye | A2–B1 | Draw another | 1 / C C | 1 / C | 0 | 100% | Cleared |

Self-study totals: first runs 13 Cleared, 11 Partial, 0 Not yet; after the v7 second look 14 Cleared / 10 Partial. Objective stamps over all runs: 63 Cleared, 12 Partial, 1 Not yet. Radar at the end: Say the plan 4/8, Ask a question 5/7, Explain 11/15, Say a number 3/4, Ask politely 5/6. One grammar note logged (Conditionals, "if you will", v7 second look). Lesson mode then moved s8 from Cleared to Partial (83%, due in 3 days) because the teacher gave one ½.

## Where she was wrongly judged

### False negatives in the live run (fair B1 answers refused)

Every one of her 11 Partial cards was caused by the checker, not by her English. 14 of 64 typed answers were refused in whole or part although they did the job:

| Card-ex | What she typed | Objective not ticked |
|---|---|---|
| o1-2 | Our commanding officer approves and authorises all the payments. | Say who signs the payments |
| o2-2 | Yes, I'm afraid the date on the second invoice isn't right. | Say there is a problem |
| o5-1 | Sure, Mr Erikson. Are you free on Wednesday or Thursday? | Ask when |
| o6-2 | Would it be possible to have two more days? I'll send them by Friday. | Ask politely for more time |
| v2-2 | Sorry, could you speak a bit more slowly, please? | (repair not recognised; cost a try and the Cleared stamp) |
| v3-1 | Welcome, Flight Lieutenant Hughes. Was your flight okay? | Ask about his journey |
| v4-1 | …Wing Commander Anan gave his approval for the plan. | Say what was decided |
| v4-2 | Not yet, Ma'am. I'll email them to you right after this. | Offer to send them, and say when |
| v7-1 | If you could send us the new bank details today, we would be able to pay again tomorrow. | Say the plan with if |
| v7-2 | In that case, I would phone you so we could check them together. | Say what you will do then |
| v7-2 | Then I'd ask you to confirm the details by email before we pay. | Say what you will do then (→ Move on, Not yet) |
| v8-2 | The bank couldn't accept it because the account number wasn't right. | Say why |
| s5-1 | I'm planning to visit my parents in Ayutthaya on Saturday. | Say your plan |
| s7-1 | I'd probably go to Chiang Mai and spend the week in the mountains. | Say where you would go |

Pattern: the regexes accept will / can / could you, but not the B1 forms the persona is supposed to grow into: would / could conditionals, "would it be possible", "I'm planning to", adverb after would, noun forms (approval), "isn't right". The radar therefore tells a B1 student that "Say the plan" is her weakest move (4/8) when all four misses were correct English. A stronger student is scored lower than an A2 student who repeats the chip.

### False negatives from read-only probes (scEval called, nothing committed)

118 fair answers tested, 77 not accepted in full. With the regexes in `fix.py`, 67 of the 77 pass, all 48 model answers still pass and no extra wrong answer gets through (verified by running). Full list:

| Card-ex | Fair answer | Result now |
|---|---|---|
| o1-2 | Our commanding officer approves them. | missed: Say who signs the payments |
| o1-1 | Good morning, Mr Eriksen. Nok does. | missed: Say who checks the invoices |
| o2-2 | Yes, the date on the second one isn't right. | missed: Say there is a problem |
| o3-1 | Good afternoon, Colonel. I'm afraid I need a little more time. | missed: Say it is not ready |
| o3-1 | Good afternoon, Colonel Hayes. Unfortunately it's taking longer than I expected. | missed: Say it is not ready |
| o3-2 | By the end of the day, Ma'am. | missed: Say when it will be ready |
| o3-2 | In a couple of hours, Ma'am. | missed: Say when it will be ready |
| o3-2 | I can finish it by noon. | missed: Say when it will be ready |
| o4-1 | Hello, Captain Ellis. Which payment is it? Could I have the reference, please? | missed: Ask for the invoice number |
| o4-2 | Invoice four hundred and fifty-one. Is it in US dollars? | missed: Repeat the number to check it |
| o5-1 | Of course. Would Thursday suit you? | missed: Ask when — What day …? / What time …? |
| o5-1 | No problem. What date would you prefer? | missed: Ask when — What day …? / What time …? |
| o5-1 | Sure. How about tomorrow afternoon? | missed: Ask when — What day …? / What time …? |
| o6-2 | Would it be possible to have two more days? | missed: Ask politely for more time |
| o6-2 | I'd be grateful if you could give me until Friday. | missed: Ask politely for more time |
| o6-2 | Is it okay if I send them on Friday? | missed: Ask politely for more time |
| o6-2 | I need a couple more days, if that's all right. | missed: Ask politely for more time; Say how long, or which day |
| o7-2 | We're paying on Friday. | missed: Say the plan — We will … / We're going to … |
| o7-2 | It should be in your account by the end of this week. | missed: Say the plan — We will … / We're going to … |
| o8-1 | Excuse me, Wing Commander. I need your signature on this form, please. | missed: Ask politely for his signature |
| o8-1 | Sorry to disturb you, Sir. Would it be possible to sign this form now? | missed: Ask politely for his signature |
| v2-1 | But I booked three nights. Please check again. | missed: Ask her politely to check again |
| v3-1 | Welcome to the base, Flight Lieutenant Hughes. Was your flight okay? | missed: Ask about his journey |
| v3-1 | Welcome! I hope you had a good journey? | missed: Ask about his journey |
| v3-2 | You need to get a visitor pass first. | missed: Say where to go first |
| v4-1 | We discussed the travel budget and Wing Commander Anan gave his approval. | missed: Say what was decided |
| v4-1 | We talked about the travel budget. The boss was happy with it. | missed: Say what was decided |
| v4-2 | Not yet, Ma'am. I'll email them to you right after this. | missed: Offer to send them, and say when |
| v4-2 | No, Ma'am. I'll do it straight away. | missed: Offer to send them, and say when |
| v4-2 | Not yet. Let me send them to you today. | missed: Offer to send them, and say when |
| v4-2 | I'm sending them this afternoon. | missed: Offer to send them, and say when |
| v6-1 | I need the receipts, Ma'am. How many are there? | missed: Ask politely for the receipts |
| v6-2 | Then you'll have to complete a lost receipt declaration. | missed: Ask her to fill in the form |
| v7-1 | I'm sorry, Captain Ellis. If you could send us the new details today, we would pay again tomorrow. | missed: Say the plan with if |
| v7-1 | I apologise. Once you send the new details, we'll pay again tomorrow. | missed: Say the plan with if |
| v7-1 | Sorry about that. As soon as we get the new bank details, we will transfer it again. | missed: Say the plan with if |
| v7-2 | In that case, I would phone you so we could check them together. | missed: Say what you will do then |
| v7-2 | I'll ring you and we'll go through them together. | missed: Say what you will do then |
| v7-2 | Then I'm going to ask the bank to verify them first. | missed: Say what you will do then |
| v8-1 | Two have been paid and the third was returned. | missed: Say one was returned |
| v8-1 | Two went through last week. The last one bounced. | missed: Say two were made; Say one was returned |
| v8-1 | We paid two last week. The bank returned one. | missed: Say one was returned |
| v8-1 | Two were paid, and the bank sent the other one back. | missed: Say one was returned |
| v8-2 | The account number wasn't right. | missed: Say why |
| v8-2 | There was a typo in the account number. | missed: Say why |
| v8-2 | Because of an invalid account number. | missed: Say why |
| s1-2 | He is responsible for the whole budget. | missed: Say what your boss does |
| s1-2 | He makes the final decisions. | missed: Say what your boss does |
| s2-1 | Of course, I'm Thai! And you? | missed: Answer about yourself |
| s2-1 | Absolutely. What about you? | missed: Answer about yourself |
| s2-2 | The fried rice is safe for you. | missed: Suggest a dish that is not spicy |
| s2-2 | You might like the chicken with cashew nuts. | missed: Suggest a dish that is not spicy |
| s2-2 | Why don't you have the omelette? | missed: Suggest a dish that is not spicy |
| s3-2 | Very much, though I missed Thai food. | missed: Say if you liked it |
| s4-1 | My husband drives me. Is your hotel far from here? | missed: Say how you get to work; Ask him a question back |
| s4-2 | The Grand Palace is worth a look. | missed: Suggest a place |
| s4-2 | Wat Arun is beautiful at sunset. | missed: Suggest a place |
| s4-2 | If I were you, I'd take a boat trip on the river. | missed: Suggest a place |
| s5-1 | I'm planning to visit my parents. | missed: Say your plan — I'm going to … / I will … |
| s5-1 | I'd like to sleep all weekend! | missed: Say your plan — I'm going to … / I will … |
| s5-1 | I'm having dinner with friends on Saturday. | missed: Say your plan — I'm going to … / I will … |
| s5-1 | Nothing special. I might go shopping. | missed: Say your plan — I'm going to … / I will … |
| s5-2 | What about Chatuchak Market? | missed: Suggest something to do |
| s5-2 | If I were you, I'd take a day trip to Ayutthaya. | missed: Suggest something to do |
| s6-1 | Excuse me, Ma'am. Is it OK if we take a photo with you? | missed: Ask politely for a photo |
| s6-1 | Colonel Hayes, we'd love to have a picture with you. | missed: Ask politely for a photo |
| s6-2 | Over there by the window would be perfect. Thank you. | missed: Say where to stand |
| s7-1 | I'd probably go to Chiang Mai. | missed: Say where you would go — I would … |
| s7-1 | I would definitely fly to Japan. | missed: Say where you would go — I would … |
| s7-1 | I would choose Phuket. | missed: Say where you would go — I would … |
| s7-2 | Don't miss Chiang Mai next time. | missed: Suggest something for his next visit |
| s7-2 | Why don't you come in November for Loy Krathong? | missed: Suggest something for his next visit |
| s8-1 | Thank you, it was great. Have a pleasant flight. | missed: Wish him a good journey |
| s8-1 | Thank you so much. I hope you get home safely. | missed: Wish him a good journey |
| s8-2 | So do I. Have a good one. | missed: Say goodbye |
| s8-2 | I'm sure we will. Farewell! | missed: Say goodbye |
| s6-1 | Excuse me, Colonel Sarah Hayes. Could we take a photo with you? | missed: Use the right name for her |

### Repair wordings not recognised (4 of 6)

| Card-ex | Text | Result now |
|---|---|---|
| v2-2 | Sorry, could you speak a bit more slowly, please? | missed: Give the number |
| v2-2 | Sorry, I didn't get that. | missed: Give the number |
| v2-2 | Excuse me, what was that? | missed: Give the number |
| v2-2 | Sorry? | shortmissed: Give the number |

"Sorry?" alone gets "A little more, please" (short); the other three are treated as a wrong answer, use up a try and the NPC is not asked to repeat. That breaks the house rule "repair phrase always valid".

### False positives (wrong or opposite answers accepted): 31 of 34 probes

| Card-ex | Wrong answer | Result now |
|---|---|---|
| o1-2 | I don't know who signs them. | all ticked |
| o1-1 | Hello. I have no idea who checks them. | all ticked |
| o2-1 | I have three cats at home. | all ticked |
| o2-2 | No problem at all. I have two brothers. | all ticked |
| o2-2 | No, there is no problem with any of them, all 2 are fine. | all ticked |
| o3-1 | Good afternoon, Colonel Hayes. Yes, it is not a problem, here you are. | all ticked |
| o3-2 | I don't know, maybe not this week. | all ticked |
| o4-2 | I have 451 dollars. | all ticked |
| o5-1 | I don't know when. | all ticked |
| o5-2 | My office is closed on Thursday. | all ticked |
| o7-2 | I will not pay you today. | all ticked |
| o8-1 | Sir, could you go away, please? | all ticked |
| o8-2 | No, it can wait until after the bank holiday, thanks. | all ticked |
| v1-1 | I don't know, I am right here. | all ticked |
| v1-1 | You're right, it is hard to find. Sorry, I'm new. | all ticked |
| v1-2 | I have nine invoices. | all ticked |
| v2-1 | I don't have a booking. Can you give me a room? | all ticked |
| v3-2 | I don't know which office. | all ticked |
| v4-1 | I did not go to the meeting about the budget. Nobody decided anything. | all ticked |
| v5-2 | No, you don't need an ID. | all ticked |
| v6-2 | You don't need to fill in anything. | all ticked |
| v7-1 | Sorry, I don't know if we can. | all ticked |
| v7-2 | I will not check them again. | all ticked |
| v8-1 | Two were not paid. One of them never came back. | all ticked |
| v8-2 | I don't know what went wrong. | all ticked |
| s1-2 | I don't know what he does, I never see him at work. | all ticked |
| s4-2 | I can not think of anything, sorry. | all ticked |
| s5-2 | I can not help you with that. | all ticked |
| s7-2 | You can not come here again. | all ticked |
| s8-2 | Not again, I hope. | all ticked |
| v1-1 | Where is the briefing room, on the floor? | all ticked |

Known and partly by design (bare keywords pass), but negatives and "I don't know" answers earn a Cleared stamp: "I will not pay you today" (o7-2), "I don't know who signs them" (o1-2), "No, you don't need an ID" (v5-2). The echo guard also has a hole: "Where is the briefing room, on the floor?" passes v1-1.

### Address conventions

- "Colonel Sarah Hayes" (rank + full name, correct) is refused on o3-1 / s6-1 and gets the "Address & register" grammar note meant for "Colonel Sarah". Fix in the list (P1-4).
- "Ms Hayes", "Miss Sarah", "Khun Anan" are correctly not ticked.
- Speech-to-text spellings Hays / Erikson / Mam did no harm: the name objective keys on "colonel" / "mam", and greet objectives do not need the surname.

### Grammar-note false alarms (probes)

- "I watched Wing Commander Anan sign them" → Verb -s note (bare infinitive after watch/see is correct; "watched" is not in SC_AUX).
- "the payment sent on Friday is correct", "one payment returned to us" → Passive note on correct English.
- "I want a quiet weekend" (s5) → "Polite requests" note in small talk where it is not a request.
- "If you will kindly send…" → Conditionals note (polite "will" after if is correct, rare; low priority).

## Confusing UI and phone layout (390 px)

1. The answer area is below the fold. On the exchange screen the app header, tab bar, NPC bubble, objectives, Situation and three chips come first; the microphone, Hint, Ask to repeat and Type instead start at about y = 1050 px, so every exchange needs a scroll (shots 07 → 08). Same on pre-flight: I'M READY is under the chips.
2. The full Modulation Desk header (logo, title, five buttons, about 200 px) stays on top of every card, exchange and debrief screen.
3. Small tap targets (measured): "Type instead" 102x27, NPC replay speaker 29x32, "Situation" and "How Scramble works" summaries 17 px high, Hint / Ask to repeat 36 px high, tools strip buttons 33 px high, Move on is a text link. Apple's guide is 44 px.
4. After a typed miss the coach says "Words on the screen wrong? Tap 'Say again' next time, or type." — irrelevant when she typed; and on a first-try total miss the NPC says "Sorry — I didn't quite catch that. Would you mind repeating that?", which blames her audio for a checker miss and is above A2.
5. The coach names the missing objective but not why a correct sentence was refused; on s7-1 the label "Say where you would go — I would …" does not hint that "I'd probably go" fails only because of the adverb.
6. Formation link from the debrief: Back from the formation lands on the Formation Drills home (store.tab = fd), not on the Scramble debrief or card. She has to find the Scramble tab again and the "Fly this card again" button is gone.
7. Deck tiles after play: formation chips wrap in the middle ("F1 Verb -" / "s", "F8 Polite / requests") and crowd the stamp line (shot 25).
8. Lesson mode marking rows: the objective icon sits on the box edge and long labels wrap under the ✓ ½ ✗ buttons (shot 30). A lesson-mode result silently replaces the self-study stamp (s8 Cleared → Partial with a due date); "best 100%" stays.
9. A card with a "Not yet" objective still shows PARTIAL 45% with "You handled it with a little help" (v7); acceptable, but the tile shows only "Partial".
10. Scramble surprise always deals the first unseen card in deck order (o1, o2 …), so on a first tour it is not a surprise; "Draw another" does the same.

No horizontal overflow on any screen (scrollWidth 390 everywhere). No page errors.

## Recommended improvements, ranked

### P1 — unfair checks and rule breaks

**P1-1. Widen the objective regexes for B1 forms** (SC_CARDS, per card). verified-by-running: `fix.py` holds the exact replacements; index is the objective position in the exchange.

```js
const DAY2 = "(" + SC_DAY.slice(1,-1) + "|noon|midday|lunch(time)?|end of (the )?(day|week)|couple of (hours|days)|few (hours|days|minutes)|right (now|away|after)|straight away|immediately|as soon as)";
const F = {
 "o1-2": [0, /\b(signs?|is signing|signed|signature|approv\w+|authori[sz]\w+)\b|\bwing commander\b|\b(my|our|the) (boss|commander|commanding officer|chief)\b|\bdoes (it|that|them|this)\b/],
 "o2-2": [0, /\b(problem|mistake|error|wrong|not (correct|right)|incorrect)\b/],
 "o3-1": [1, /\b(is not|not ready|not yet|not finished|not done|have not|has not|did not|do not have|(need|take|taking|takes) (a little |some |a bit )?(more time|longer)|will be ready|still (working|finishing|checking)|almost (ready|done|finished))\b/],
 "o3-2": [0, new RegExp("\\b" + DAY2 + "\\b")],
 "o4-1": [1, /\b(invoice|reference)\b.*\bnumber\b|\bnumber\b.*\b(invoice|reference)\b|\bwhich invoice\b|\b(the|your|a) reference\b/],
 "o5-1": [0, /\b(when|what (day|time|date)|which (day|date))\b|\b(are you|would you be) (free|available)\b|\b(would|does|is) \w+ (suit|work for|good for|okay for|convenient)\b|\bhow about \w+/],
 "o6-2r": [0, /\b(could|can|may|would) (i|we|you)\b|\bwould it be possible\b|\bis it (okay|all right|possible) if\b|\bif you could\b|\bdo you mind if\b/],
 "o7-2": [0, /\b(will|going to|can|should)\b|\b(am|are|is) (paying|sending|transferring|making)\b/],
 "o8-1": [1, /\b(could|would|may) (you|i)\b|\bcan (you|i)\b.*\bplease\b|\bplease\b.*\bcan (you|i)\b|\bwould it be possible\b|\b(need|like) your signature\b.*\bplease\b/],
 "v2-1": [1, /\b(could|can|would) you\b|\bplease (check|look|try|search)\b|\b(check|look|try|search) (it )?again\b.*\bplease\b/],
 "v3-1": [1, /\b(how|where|when|what|did|was|were|is|are|hope)\b.*\b(flight|trip|journey|hotel|stay|staying|arrive|travel)\b/],
 "v4-1": [1, /\b(approv\w+|agreed?|decided?|decision|said yes|said okay|accepted?|signed?|happy with)\b|\bplan (is|was) okay\b/],
 "v4-2": [0, new RegExp("\\b(will|can|going to|let me|am sending|am going)\\b.*\\b(" + DAY2 + "|now|soon|later|after lunch|after this)\\b|\\b" + DAY2 + "\\b.*\\b(will|can|going to)\\b")],
 "v7-1": [1, /\b(if|once|when|as soon as)\b.*\b(will|can|would|could|going to)\b|\b(will|can|would|could|going to)\b.*\b(if|once|when|as soon as)\b/],
 "v7-2": [0, /\b(will|can|would|could|going to)\b.*\b(call|check|phone|ring|confirm|verify|email|contact|tell|ask|go through)\b/],
 "v8-1": [1, /\b(1|one|3|the other|the last)\b.*\b(returned|came back|sent back|sent .{1,12} back|rejected|bounced)\b|\b(returned|rejected|sent back)\b.*\b(1|one|the other|the last)\b/],
 "v8-2": [0, /\b(wrong|mistake|incorrect|error|not (correct|right)|typo|invalid)\b/],
 "s1-2": [0, /\b(manag|sign|check|approv|lead|run|work|control|head|command|chief|director|charge|responsib|decid|decision)\w*\b|\bboss of\b/],
 "s2-1": [0, /\b(yes|no|of course|sure|absolutely|definitely|a little|not really|i (do|love|like|eat|can|am))\b/],
 "s2-2": [0, /\b(try|recommend|should|not spicy|not hot|mild|safe|how about|what about|why do not you|would you like|might like|this (1|one|dish|soup))\b/],
 "s4-2": [0, /\b(should|can|could|try|visit|go to|recommend|how about|what about|why do not you|see|worth|would (go|take|visit|see)|beautiful|must)\b/],
 "s5-1": [0, /\b(going to|will|plan(ning)? to|want to|would (like|love) to|might|am (visiting|meeting|staying|going|seeing|having|planning))\b/],
 "s5-2": [0, /\b(should|can|could|try|visit|go to|recommend|how about|what about|see|maybe|why not|why do not you|would (go|take|visit|see))\b/],
 "s6-1n": [0, new RegExp("\\bcolonel\\b(?! sarah\\b(?! hayes))|\\b" + SC_MAAM + "\\b")],
 "s6-1": [1, /\b(could|would|may|can) (we|i|you)\b|\bis it (okay|all right|possible) if\b|\bwe would (love|like)\b/],
 "s6-2": [0, /\b(here|there|next to|middle|centre|center|front|beside|between|left|right|by the)\b/],
 "s7-1": [0, /\bwould (\w+ly |also |just )?(go|visit|travel|stay|like|love|fly|take|see|spend|choose|pick)\b/],
 "s7-2": [0, /\b(should|can|could|try|visit|go to|recommend|see|must|have to|do not miss|why do not you|come (in|back|to))\b/],
 "s8-1": [1, /\b(safe|good|nice|great|pleasant|lovely) (flight|trip|journey|travel\w*)\b|\bsafe(ly)? (home|travels?)\b|\bhome safe(ly)?\b|\bgood luck\b|\ball the best\b|\btake care\b|\bbon voyage\b|\bhave a (good|nice|safe) (1|day|time)\b/],
 "s8-2": [0, /\b(goodbye|bye|farewell|see you|take care|keep in touch|stay in touch|hope so|me too|so do i|again|sure we will)\b/],
};
```

Key ones with the text that failed: v7-1 objs[1] ("If you could send… we would be able to pay"), v7-2 objs[0] ("I would phone you", "I'll ring you"), s7-1 objs[0] ("I'd probably go"), s5-1 objs[0] ("I'm planning to", "I'm having dinner with friends"), o6-2 objs[0] ("Would it be possible…"), v4-1 objs[1] ("gave his approval"), v4-2 and o3-2 (shared time words: add noon, end of the day, right after, straight away to SC_DAY or use DAY2), v8-1 objs[1] ("the third" is dead code because gsNorm turns "third" into 3; also allow "the bank returned one").
Still failing after the fix (need a decision, from-reading): o4-2 "four hundred and fifty-one", o1-1 "Nok does" without Khun, v6-1 "I need the receipts, Ma'am" (arguably not polite enough, keep), v6-2 "complete a declaration" (add `complete|declaration`), v3-2 "get a visitor pass" (add `pass`), s3-2 "Very much" (add `very much|a lot`), s4-1 "drives me… Is your hotel" (add `drives?|is your`), v8-1 "bounced", "sent the other one back".

**P1-2. Repair phrase: accept the common polite variants** (SC_REPAIR). verified-by-running:

```js
const REP2 = new RegExp(SC_REPAIR.source + "|\\b(speak|say (it|that)|talk) (a (bit|little) )?(more )?(slowly|slower)\\b|\\bi (do not|did not) (get|hear) (that|it|you)\\b|\\bwhat was that\\b|\\bcome again\\b");
```

Also let a lone "Sorry?" / "Pardon?" / "Excuse me?" count as repair instead of "short" (in scEval, before the short test: `if (/^(sorry|pardon|excuse me|what)$/.test(n)) status = "repair"`), from-reading.

**P1-3. Do not charge a try when no objective regex could have matched a long, on-topic answer — or at least fix the stamp.** (scCommit) Simplest fair rule, from-reading: an objective met on the second try with no hint and no chip counts as Cleared when the first try was 6+ words; keep Partial for hints. That removes most of the damage from any regex gap that remains.

**P1-4. "Colonel Sarah Hayes" must count** (o3-1, s6-1 name regex and SC_SLIPS last row). verified-by-running: use `\\bcolonel\\b(?! sarah\\b(?! hayes))` in both places.

**P1-5. Stop negatives and "I don't know" from clearing a card** (scEval). from-reading: before testing objectives, if `n` matches `/\b(do not|did not) know\b|\bno idea\b|\bnot sure\b/` return a miss with a kind coach line; and for plan / request objectives reject `will not`, `can not` (e.g. o7-2, v7-2, s4-2, s5-2: change `\b(will|can)\b` to `\b(will|can)\b(?! not)`). 31 of 34 wrong answers passed.

**P1-6. Radar fairness.** (scStamp) from-reading: after P1-1 the radar will be right for B1; until then it reports checker gaps as her weak moves.

### P2 — guidance (matters most for A1–A2)

**P2-1. Put the answer area in view.** (scRender / CSS for `.fd-play`, `.pbar`) from-reading: on `view === "scplay"` hide the big site header, fold the chips into one "💬 Phrases (3)" row, and scroll `#scSpeak` into view after the NPC finishes. Same for I'M READY on pre-flight (make it sticky at the bottom).
**P2-2. Typed misses get typed wording.** (scCoachHTML, scCommit) from-reading: when `SCP.typed`, drop the "Tap Say again" line and do not play GS_CATCH; say "I didn't find: …  Try another way to say it, or tap Hint."
**P2-3. Show the frame on the second miss automatically** (scCommit: `if (SCP.tries >= 2) SCP.lad = Math.max(SCP.lad, 1)`), so a learner who does not notice the Hint button is not stuck. from-reading.
**P2-4. Bigger tap targets**: Type instead, Move on, the replay speaker and the Situation summary to at least 44 px high; make Move on a button. from-reading (sizes measured by running).
**P2-5. Return path from a formation.** (debrief `[data-scfd]` handler, fdBrief back button) from-reading: remember the card id and have Back return to the Scramble home with that card's tile highlighted, or add "↩ Back to Scramble card".

### P3 — polish

**P3-1.** Slip false alarms: add `watched|watch|heard|hear|have|had|helped` to SC_AUX; limit the Passive slip to sentence starts or after "and/but" with no following "on/by/to"; apply the "I want" note only on cards with a `request` objective. from-reading (alarms verified-by-running).
**P3-2.** Echo guard: use a ratio (LCS ≥ 80% of her words) instead of 100%, so "Where is the briefing room, on the floor?" earns nothing. from-reading.
**P3-3.** Tiles: keep formation chips on their own line with `white-space: nowrap`. Lesson mode rows: `min-width:0` on the label and a fixed-width button group. from-reading.
**P3-4.** Scramble surprise: pick a random unseen card across decks instead of the first in order (scPick: `unseen[Math.floor(Math.random()*unseen.length)]` when `!deck`). from-reading.
**P3-5.** Lesson mode: keep the self-study stamp and the lesson stamp separately, or do not set a due date from a live result. from-reading.
**P3-6.** Debrief "PARTIAL" wording when an objective is Not yet: "One objective is still open" instead of "with a little help". from-reading.
