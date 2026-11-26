# A2 persona — regex-relevant findings (condensed by lead from the A2 agent's report)

First run: 16 Cleared, 7 Partial, 1 Not yet (24 cards). Probes in probes.json (120).

## False negatives (verified by running)
- o3-1 explain: "Sorry, the report not finish yet." / "I not finish it." refused. Add not finish(ed)?, not complete(d)?, still doing. Also stop "it is ready … is not a problem" passing.
- v8-1 obj 2: "One payment the bank return…", "One payment come back from the bank.", "One is return from bank." → `\b(1|one|the other|the third|the last|another)\b.*\b(return(ed|s)?|c[ao]mes? back|sen[dt] back|reject(ed)?|bounced?|fail(ed)?)\b`
- o5-1: "Okay. Are you free on Thursday?" refused.
- o6-2: "Please give me two more days." / "I need two more days please." refused (request).
- o8-1: "Excuse me Sir, please sign this form." / "Sir, I would like your signature please." / "Can you sign this form?" refused (keep stricter for a commanding officer: could/would/may, or can … please, or please + verb, or I would like).
- v2-1: "I have reservation three night. Please check again." refused.
- v3-1: "Welcome. Was your trip good?" / "Your flight is ok?" refused.
- v4-1: "Wing Commander Anan say ok." refused. v4-2: "Nobody send. I send now." refused (plan — may stay strict).
- v6-1: "I need your receipts Ma'am. How many do you have?" refused.
- v7-1: "When you send the new bank details, we will pay again." refused (needs if). v7-2 "I call you." refused (plan; may stay strict).
- v8-2: "The number is not right." refused → add not right|different.
- s1-1: "I am officer in air force." refused → officer|air force. s1-2: "He is the boss." → \bboss\b.
- s3-2: "I enjoy it. London is nice." refused → enjoy|nice|fun|good|great.
- s4-1: "You stay where?" / "Is your hotel far?" refused. s4-2 "Wat Arun is beautiful." refused.
- s5-1: "I stay home and sleep." / "Maybe I go shopping with my mom." refused (plan; maybe keep strict with ex frame). s5-2 "Chatuchak market is good." refused.
- s6-1: "Excuse me Ma'am. We want to take photo with you." refused.
- s7-1: "I want to go to Japan." / "I will go to Japan" refused (needs would; known). s7-2 "Please come to Chiang Mai." refused.

## False positives (verified)
- Negations: o3-1 "Yes Colonel Hayes, it is ready. Is not a problem."; o2-2 "No problem. Two invoices are ok."; o7-2 "I can not pay today."; o8-2 "No Sir, not today. Thank you."; v4-1 "The travel plan is not approved."; v4-2 "I can not send them today."; v5-2 "No. You don't need ID."; v6-2 "I can not sign for you."; v7-2 "We will not call you."; s2-2 "I don't recommend anything."; s4-2 "I can not think."; s5-2 "I can not see you on Sunday."; s8-2 "No, never again."
- Wrong content: o1-1 "Hello. I don't know who checks."; o1-2 "I sign the payments." / "Khun Nok signs the payments." (require anan|wing commander|boss); o2-1 "I have three questions for you." (require 3 invoices?|there (is|are) 3); v1-1 "I don't know. Ask the right person." (matches right); v7-1 "Sorry. If the bank can."; s1-2 "I don't know his work."; s3-1 "I studied hard."

## Grammar notes
- Wrong: v4-1 "Wing Commander Anan approve the plan" gets Verb -s; on past cards should be Past simple.
- Missed slips: "It on the second floor", "It start at nine", "It will ready tomorrow", "It not spicy", "We talk about…" (past card), "have wrong date", "The bank details was wrong". Suggested SC_SLIPS additions: `\b(it|he|she) (on|in|at|next|not|very|ready)\b` → add is; `\bwill (ready|late|finished|free)\b` → will be; `\bit (start|close|open|finish|have)\b` → Verb -s; `\b(details|invoices|payments|receipts) was\b` → were.
- Address: "Good afternoon Sarah / Miss Hayes" refused with no note → add `\b(miss|mrs|ms|khun) (hayes|sarah)\b|\bgood (morning|afternoon) sarah\b` to the address slip.
