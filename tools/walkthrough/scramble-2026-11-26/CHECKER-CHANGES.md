# Scramble answer-checker data — changes (cards/index.html, SC_DAY … before SC_REPAIR only)

Harness: node, slices of the file (GS_NUM/gsNorm/gsLCS, FD_FILL, SC_DAY…scEval). No lookbehind used. Nothing from `const SC_REPAIR` on, and nothing above `const SC_DAY`, was touched (diff = 0 lines).

## Counts (before -> after)
- Model answers: 48/48 hit every objective with no grammar note (before and after).
- B1 probes (186): fair answers rejected 80 -> 2 (one of them a "pass?"; both deliberate, below); wrong answers accepted 38 -> 2.
- A2 probes (127): fair rejected 38 -> 11 (all deliberate, below); wrong accepted 25 -> 3 (all "FP?").
- A1 probes (54) + A1 typed run: about 20 fair A1 answers now clear ("Report not finish", "Two more day please", "Sorry. I forget.", "I book three night. Please check again.", "Boss say ok", "Two ok. One come back", "One payment return", "You like?", "Wat Pho very beautiful", "You go Wat Pho", "Grand Palace.", "Chatuchak market is good", "You tired?" ...); 4 wrong ones no longer clear ("No problem. Invoice two ok.", "Yesterday morning.", "I see.", "I don't know who signs."). No answer that passed in the A1 run now fails.

## New helpers (defined after scRe, inside the data region)
SC_DAY2 (SC_DAY + noon, end of the day/week, couple of hours, straight away ...), SC_DK ("don't know / no idea / not sure" guard), SC_NO (SC_DK + will not / can not / would not / never), SC_SENIOR, SC_SUG, SC_SPOT, and scG(guard, re) = guard lookahead at the start + the objective regex. So the negation guard lives in the data; no engine change is needed.

## Objectives changed (card-exchange-objective)
o1-1 explain, o1-2 (now needs Wing Commander / Anan / boss, so "I sign" and "Khun Nok signs" fail), o2-1 (3 must be the answer or 3 invoices, not "three cats"), o2-2 explain, o3-1 name + explain, o3-2, o4-1 ask, o4-2 both, o5-1, o5-2 place, o6-1 past, o6-2 both, o7-2 both, o8-1 request, o8-2 explain, v1-1, v1-2, v2-1 both, v3-1 ask, v3-2, v4-1 decided, v4-2, v5-2, v6-1 request, v6-2, v7-1 plan, v7-2, v8-1 both, v8-2, s1-1, s1-2, s2-1 both, s2-2, s3-1, s3-2 both, s4-1 both, s4-2, s5-1, s5-2, s6-1 both, s6-2 place, s7-1, s7-2, s8-1 bye, s8-2.
Labels changed (to show the required form): o8-1 "Ask politely for his signature — Could you …?", s6-1 "Ask politely for a photo — Could we …?", v4-2 "Offer to send them, and say when — I will … today", v7-2 "Say what you will do then — I will …". No `ex` frames changed.
"Colonel Sarah Hayes" now counts as the right name (o3, s6) and gets no address note; "Colonel Sarah" alone still fails with the note.

## Polite-request rule (now consistent)
- Senior (o8 Wing Commander, s6 Colonel): SC_SENIOR = could / would / may / can + you/I/we, "would it be possible", "is it OK if", "I/we would like". "Please sign", "Photo please", "We want …", "I need … please" do not clear; the label now shows the frame. o8 also needs sign/form/this in the sentence ("could you go away" fails).
- Service / peer (v2 hotel desk, o6 auditor, v6): please + verb counts ("Please check again", "Receipts please, Ma'am", "Two more days please", "I need your receipts"). "I want receipt please" no longer clears v6-1, so stamp and "I want" note agree.

## SC_SLIPS
- False notes removed: "I want go Japan" / "I want a quiet weekend" (also `we want` now covered), "watched/heard/helped … sign" (SC_AUX), "the payment sent on Friday is correct" and "one payment returned to us" (Passive), "if you will kindly" (Conditionals), "Colonel Sarah Hayes" (Address).
- Added: answer starting "It on / It not / It very" (add is), "will ready" (will be), "it start / it close" (Verb -s), "details was" (were), "Miss / Mrs / Ms / Khun Hayes|Sarah", "Good afternoon Sarah" (Address).

## Deliberately left strict
- o7-2, s5-1, v4-2, v7-2 "Say the plan": need will / going to / present continuous ("Friday we pay", "I stay home", "I send now", "I call you" stay Partial) — the card exists for the future form; labels/ex show it.
- v7-1: "if/when/once … will + verb" required ("If you send today, we pay tomorrow" fails) — first conditional is the point.
- s7-1: needs "would" ("I want to go to Japan", "I will go" fail) — the card is the would card.
- o8-1 / s6-1: "Sir, please sign this form", "Colonel, photo please", "We want to take photo", "I need your signature, please" — senior rule above.
- o6-2: "I will send in two days" — the label is "ask politely for more time".
- v4-2: "I will send." — the label asks for when.
- o8-2: "Yes, quite urgent" — does not say why.
- s2-1: "I like it." alone — no question back.
- v5-1 left as it was (accepts "go to / visit / see"; "we go finance office" still needs "to") — not widened further because it is a plan card, not tightened to avoid new rejections.

## Still accepted, not fixed (need more than a regex)
- v1-1 "Where is the briefing room, on the floor?" (near-echo), s2-1 "No. I am tired, are you finished?", v3-2 "We go to the gate.", v5-1 "I will see you at ten.", s2-2 "Tom yum is very hot. You should eat it."
- Grammar notes cannot see the card: "Anan approve the plan" on the past card v4 still gets Verb -s, not Past simple. One-line engine option if wanted: pass the turn to scSlip and prefer the "Past simple" tag when the objective kind is "past".
