import asyncio, json, sys, time, os, shutil
sys.path.insert(0, "/home/claude/wt/B1")
from plan import PLAN, ORDER
from playwright.async_api import async_playwright
OUT = "/home/claude/wt/B1"; TMP = OUT + "/shots_raw"; os.makedirs(TMP, exist_ok=True)
UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1"
shots = {}; log = []; cards = {}; notes = []; layout = []
T0 = time.time()
async def main():
  async with async_playwright() as p:
    b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium")
    ctx = await b.new_context(viewport={"width":390,"height":844}, device_scale_factor=2, is_mobile=True, has_touch=True, user_agent=UA)
    blocked = []
    async def rt(r):
        if "localhost:8103" in r.request.url: await r.continue_()
        else: blocked.append(r.request.url); await r.abort()
    await ctx.route("**/*", rt)
    pg = await ctx.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)[:300]))
    pg.on("dialog", lambda d: asyncio.ensure_future(d.accept()))
    await pg.goto("http://localhost:8103/?tab=sc"); await pg.wait_for_timeout(1200)
    ev = pg.evaluate
    async def st():
        return await ev("() => SCP ? {id:SCP.card.id, ti:SCP.ti, phase:SCP.phase, sub:SCP.sub, tries:SCP.tries, hits:SCP.hits, issue:SCP.issue, lad:SCP.lad, repairs:SCP.repairs, chips:SCP.chips, micErr:SCP.micErr, res:SCP.res, live:SCP.live} : null")
    async def shot(key, caption, sel=None, scroll="box", nth=0):
        await ev("() => { if (!document.getElementById('noth')) { const s = document.createElement('style'); s.id='noth'; s.textContent='[lang=\"th\"]{display:none!important}'; document.head.appendChild(s); } }")
        if scroll == "top": await ev("() => window.scrollTo(0,0)")
        elif scroll == "box" and sel:
            await ev("([s,n]) => { const e = document.querySelectorAll(s)[n]; if (e) e.scrollIntoView({block:'center'}); }", [sel, nth])
        elif isinstance(scroll, int): await ev("y => window.scrollTo(0,y)", scroll)
        elif scroll and scroll.startswith("el:"):
            await ev("s => { const e = document.querySelector(s); if (e) { const y = e.getBoundingClientRect().top + scrollY - 12; window.scrollTo(0, y); } }", scroll[3:])
        await pg.wait_for_timeout(650)
        hidden = await ev("""() => { const out = []; const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
          while ((n = w.nextNode())) { if (!/[\\u0E00-\\u0E7F]/.test(n.nodeValue)) continue; const e = n.parentElement; if (!e) continue; const r = e.getBoundingClientRect();
            if (r.width && r.height && r.bottom > 0 && r.top < innerHeight && getComputedStyle(e).visibility !== 'hidden') { out.push(e.tagName + '.' + e.className + ': ' + n.nodeValue.slice(0,30)); e.style.setProperty('display','none','important'); } } return out; }""")
        if hidden: await pg.wait_for_timeout(200)
        box = None
        if sel:
            box = await ev("([s,n]) => { const e = document.querySelectorAll(s)[n]; if (!e) return null; const r = e.getBoundingClientRect(); return {x:Math.round(r.x*10)/10, y:Math.round(r.y*10)/10, width:Math.round(r.width*10)/10, height:Math.round(r.height*10)/10}; }", [sel, nth])
        m = await ev("() => ({sw: document.documentElement.scrollWidth, sy: Math.round(scrollY), sh: document.documentElement.scrollHeight})")
        await pg.screenshot(path=f"{TMP}/{key}.png")
        shots[key] = {"caption": caption, "box": box, "sel": sel, "thaiHidden": hidden, "scrollWidth": m["sw"], "pageHeight": m["sh"]}
        if m["sw"] > 390: layout.append(f"{key}: horizontal overflow, scrollWidth {m['sw']}")
    async def sizes(tag):
        r = await ev("""() => Array.from(document.querySelectorAll('#app button, #app summary, #app select')).filter(e => e.offsetParent).map(e => { const r = e.getBoundingClientRect(); return [e.id || e.className, (e.textContent||'').trim().slice(0,22), Math.round(r.width), Math.round(r.height)]; }).filter(x => x[3] < 40 || x[2] < 40)""")
        if r: layout.append({"screen": tag, "small_targets(<40px)": r})
    async def home():
        if await ev("() => view") != "home":
            for s in ["#scHome", "#scBack"]:
                if await pg.query_selector(s): await pg.click(s); break
            await pg.wait_for_timeout(300)
    async def say(text):
        if not await pg.query_selector("#scTypeIn"):
            await pg.click("#scType"); await pg.wait_for_timeout(150)
        await pg.fill("#scTypeIn", text)
    async def play(key, shotset):
        plan = PLAN[key]; cid = key[:2]; want = plan["draw"]
        v = await ev("() => view")
        if want == "more" and await pg.query_selector("#scMore"): await pg.click("#scMore"); how = "debrief: Draw another"
        else:
            await home()
            if want == "any":
                if "any_home" in shotset: await shot("scramble_btn", "The Scramble! strip on the tab home: one tap deals a surprise card from any deck (cards that are due come first).", "#scAny")
                await pg.click("#scAny"); how = "home: Scramble (surprise)"
            elif want == "tile": await pg.click(f'[data-scgo="{cid}"]'); how = "home: tile Again"
            else:
                d = await ev("id => SC_CARDS.find(c => c.id === id).deck", cid)
                await pg.click(f'[data-scdraw="{d}"]'); how = f"home: Draw a card ({d} deck)"
        await pg.wait_for_timeout(300)
        s = await st()
        if s["id"] != cid: notes.append(f"expected {cid} from '{how}' but got {s['id']}"); cid = s["id"]
        card = await ev("id => { const c = SC_CARDS.find(c => c.id === id); return {title:c.title, lvl:c.lvl, npc:c.npc, turns:c.turns.map(t => ({npc:t.npc, labs:t.objs.map(o => o.lab), kinds:t.objs.map(o => o.k)}))}; }", cid)
        if "pre" in shotset:
            await shot("card_face", "Card face: who you will talk to, the situation, the objective icons for this card and the formations (grammar) it uses.", ".sc-cardface", "top")
            await shot("preflight", "Pre-flight: a 20-second countdown to plan the first sentence, three closed phrase chips and the I'M READY button.", ".sc-clock", "el:.sc-preside")
            await sizes("pre-flight")
        if "any_card" in shotset:
            await shot("scramble_card", "The surprise card dealt by Scramble: a new situation from another deck (Visitors), with no warning which one.", ".sc-cardface .kick", "top")
        if "second" in shotset:
            await shot("second_look", "Flying a card again from its tile: the card face now says 'second look'.", ".sc-cardface .kick", "top")
        chips_opened = []
        for i in plan.get("pre_chips", []):
            await pg.click(f'#scChipBox [data-scchip="{i}"]'); chips_opened.append({"chip": i, "when": "pre-flight", "text": await ev("([id,i]) => SC_CARDS.find(c => c.id === id).chips[i]", [cid, i])})
            await pg.wait_for_timeout(200)
            if "pre" in shotset: await shot("chip_open", "A phrase chip opened in pre-flight: it shows and reads a starter phrase, and the top score for this card drops from 100 to 90.", "#scChipBox .sc-chip.open", "el:.sc-preside")
        await pg.wait_for_timeout(900)
        pre_left = await ev("() => SCP.left")
        await pg.click("#scGo"); await pg.wait_for_timeout(300)
        centry = {"key": key, "card": cid, "title": card["title"], "level": card["lvl"], "npc": card["npc"], "drawn_by": how, "chips_opened": chips_opened, "exchanges": []}
        for ti, acts in enumerate(plan["turns"]):
            s = await st(); assert s["ti"] == ti and s["phase"] == "talk", s
            if "talk" in shotset and ti == 0:
                await shot("exchange", "The exchange screen: the person's line (tap the speaker to replay), your objectives for this exchange, and the microphone with Hint, Ask to repeat and Type instead.", ".sc-todo", "top")
                await shot("speak_controls", "Answer controls: the big microphone, plus Hint, Ask to repeat and Type instead for when the mic is not possible.", "#scType", "el:#scSpeak")
                await sizes("exchange (ready)")
            ex = {"card": cid, "exchange": ti+1, "npc_line": card["turns"][ti]["npc"], "objectives": card["turns"][ti]["labs"], "attempts": [], "chips_opened_here": [], "hints": 0, "moved_on": False}
            for a in acts:
                s = await st()
                if s["sub"] == "passed": break
                if a[0] == "mic":
                    await pg.click("#scMic"); await pg.wait_for_timeout(1800); s2 = await st()
                    ex["attempts"].append({"action": "tapped microphone (no mic available)", "app": {"sub": s2["sub"], "micErr": s2["micErr"], "shown": await ev("() => { const e = document.querySelector('.gs-err, .gs-mictxt'); return e ? e.textContent.trim().slice(0,200) : ''; }")}})
                    if "mic" in shotset: await shot("mic_fail", "What she sees when the microphone cannot start: an on-screen message, and Type instead stays available.", ".gs-mictxt", "el:#scSpeak")
                    if s2["sub"] == "rec": await pg.click("#scMic"); await pg.wait_for_timeout(500)
                elif a[0] == "chip":
                    await pg.click(f'#scChipBox2 [data-scchip="{a[1]}"]'); await pg.wait_for_timeout(250)
                    tx = await ev("([id,i]) => SC_CARDS.find(c => c.id === id).chips[i]", [cid, a[1]])
                    ex["chips_opened_here"].append({"chip": a[1], "text": tx}); chips_opened.append({"chip": a[1], "when": f"exchange {ti+1}", "text": tx})
                    if "chip_talk" in shotset: await shot("chip_in_talk", "Phrase chips are still there during the exchange: opening one after a miss shows a starter phrase (top score now 90).", "#scChipBox2 .sc-chip.open")
                elif a[0] == "hint":
                    await pg.click("#scHint"); await pg.wait_for_timeout(250); ex["hints"] += 1
                    s2 = await st()
                    if "hint" in shotset:
                        if s2["lad"] == 1: await shot("hint1", "Hint, step 1: 'Start like this' gives a sentence frame for the objective still to do.", ".gs-coach .fd-frame", "el:#scSpeak")
                        else: await shot("hint2", "Hint, step 2: the full model answer is shown and read aloud; she can still answer in her own words.", ".gs-coach .gs-c:last-child", "el:#scSpeak")
                elif a[0] == "skip":
                    if "hint" in shotset: await shot("move_on", "Move on: after two tries the link appears, so she is never stuck on one exchange.", "#scSkip")
                    await pg.click("#scSkip"); await pg.wait_for_timeout(250); ex["moved_on"] = True
                    if "hint" in shotset: await shot("moved_on_result", "After Move on: a soft 'Let's keep moving' panel with a Not yet stamp and one good answer to listen to.", ".gs-pass .sc-stamps", "el:#scSpeak")
                elif a[0] == "repairbtn":
                    await pg.click("#scRepeat"); await pg.wait_for_timeout(300); s2 = await st()
                    ex["attempts"].append({"action": "tapped 'Ask to repeat' button", "app": {"status": "repair", "issue": s2["issue"], "tries": s2["tries"], "repairs": s2["repairs"]}})
                    if "repair" in shotset: await shot("repair", "Repair in action: after 'Ask to repeat' the coach says 'Good move', the person repeats more slowly, and no try is used (Tries: 0).", ".gs-coach .gs-c", "el:#scSpeak")
                else:
                    text = a[1]
                    pre = await ev("([id,ti,tx]) => { const t = SC_CARDS.find(c => c.id === id).turns[ti]; const e = scEval(t, tx); return {status:e.status, hits:e.hits, slip:e.slip, norm:e.norm}; }", [cid, ti, text])
                    await say(text)
                    if "talk" in shotset and ti == 0 and not ex["attempts"]:
                        await shot("typed", "Type instead: her own answer typed in the box (names spelled the way speech-to-text would), ready to check.", "#scTypeIn")
                        await shot("commit", "CHECK sends the typed answer (after speaking, the same step is 'Check - is this what you said?' with Say again / COMMIT).", "#scTypeOk")
                    await pg.click("#scTypeOk"); await pg.wait_for_timeout(300)
                    s2 = await st()
                    labs = card["turns"][ti]["labs"]
                    att = {"typed": text, "app": {"status": pre["status"], "objectives_hit_this_try": [l for l, h in zip(labs, pre["hits"]) if h], "objectives_missed_this_try": [l for l, h in zip(labs, pre["hits"]) if not h],
                           "slip_note": (pre["slip"]["tag"] + ": " + pre["slip"]["msg"] + " (heard: " + pre["slip"]["said"] + ")") if pre["slip"] else None,
                           "tries_after": s2["tries"], "screen": s2["sub"], "coach": await ev("() => { const e = document.querySelector('.gs-coach'); return e ? e.textContent.trim().replace(/\\s+/g,' ').slice(0,220) : ''; }")}}
                    ex["attempts"].append(att)
                    if s2["sub"] == "passed":
                        if "talk" in shotset and ti == 0: await shot("npc_reaction", "Result of the exchange: 'Cleared!', one stamp per objective, one good answer to compare (with audio) and what she said. NEXT goes to exchange 2.", ".gs-pass", "el:#scSpeak"); await shot("objectives_ticked", "Top of the same screen: the objectives are now ticked green.", ".sc-todo", "top")
                    else:
                        if "miss" in shotset and "miss" not in shots: await shot("miss", "A fair paraphrase that the checker did not recognise: the coach names what is still to do and offers another try. Nothing is lost.", ".gs-coach .gs-c", "el:#scSpeak")
                        if "repair_typed" in shotset and pre["status"] == "repair": await shot("repair_typed", "The repair phrase typed or spoken in her own words is also accepted: 'Good move', then the person repeats.", ".gs-coach .gs-c", "el:#scSpeak")
            s = await st()
            if s["sub"] != "passed":
                notes.append(f"{key} exchange {ti+1}: plan exhausted, used Hint then Move on"); 
                while (await st())["tries"] < 2: await say("I am not sure what to say here."); await pg.click("#scTypeOk"); await pg.wait_for_timeout(200)
                await pg.click("#scSkip"); await pg.wait_for_timeout(200); ex["moved_on"] = True; s = await st()
            R = s["res"][ti]
            ex["tries"] = R["tries"]; ex["stamps"] = dict(zip(card["turns"][ti]["labs"], [{"c":"Cleared","p":"Partial","m":"Not yet"}[x] for x in R["st"]])); ex["repairs"] = R["repairs"]
            ex["slip_recorded"] = (R["slip"]["tag"] + " — " + R["slip"]["said"]) if R["slip"] else None
            centry["exchanges"].append(ex); log.append(ex)
            if "partial" in shotset and ti == 1: await shot("partial", "Second-try pass: 'Good - you got there' with a Partial stamp, because the objective was met on a later try.", ".gs-pass", "el:#scSpeak")
            await pg.click("#scNext"); await pg.wait_for_timeout(350)
        rec = await ev("id => gs.sc.c[id]", cid)
        hdr = await ev("() => { const e = document.querySelector('.gs-resh'); return e ? e.textContent.trim().replace(/\\s+/g,' ') : ''; }")
        links = await ev("() => Array.from(document.querySelectorAll('.sc-links button')).map(b => b.textContent.trim())")
        gram = await ev("() => { const e = Array.from(document.querySelectorAll('.gs-resbox .gs-c')).find(x => /grammar note/.test(x.textContent)); return e ? e.textContent.trim() : null; }")
        centry.update(final_stamp={"c":"Cleared","p":"Partial","m":"Not yet"}[rec["s"]], best=rec["best"], due=rec["due"], debrief_header=hdr, formation_links=links, grammar_note=gram, runs_on_card=rec["n"], preflight_seconds_left=pre_left)
        cards[key] = centry
        if "debrief" in shotset:
            await pg.wait_for_timeout(500)
            await shot("debrief_top", "Debrief (top): the card score, the overall stamp and, for each exchange, a stamp per objective, what she said and one good answer.", ".gs-resh", "top")
            await shot("debrief_bottom", "Debrief (scrolled): exchange 2, the formation links that help with this card, and the buttons Draw another, Fly this card again and All decks.", ".gs-resbox > .gs-acts", "box")
            await sizes("debrief")
        if "fdlink" in shotset:
            await shot("debrief_notyet", "Debrief after a Move on: the missed objective is stamped Not yet, and the card is scheduled to come back.", ".sc-stamps", "top", 1)
            await shot("formation_link", "Formation link in the debrief: one tap opens the Formation Drill that trains the grammar this card needs (here Formation 10, If + plan).", ".sc-links button")
            await pg.click(".sc-links button"); await pg.wait_for_timeout(700)
            await shot("formation_open", "Where the link goes: the Formation Drill briefing for that grammar point, ready to practise before flying the card again.", ".goalbig", "top")
            centry["formation_link_opened"] = await ev("() => (document.querySelector('.pbar h2')||{}).textContent")
            await pg.click("#fdBack"); await pg.wait_for_timeout(400)
            centry["after_fdBack_tab"] = await ev("() => store.tab + ' / ' + view")
            await pg.click('[data-tab="sc"]'); await pg.wait_for_timeout(400)
        if "slip" in shotset:
            await shot("grammar_note", "One grammar note in the debrief: the slip she made ('if you will') is quoted and explained, not marked down, with a link to the matching formation.", ".gs-resbox .gs-c")
        return centry

    # ---------- tour start: tab home ----------
    await shot("home", "Scramble tab home: the banner explains the idea, with counters for Cleared, Cards flown and Due today.", ".sc-banner .cstats", "top")
    await shot("home_tools", "Tools strip and the Scramble! surprise draw: microphone status, Voice & mic check, Slow voice, Lesson mode.", ".gs-strip", "el:.gs-strip")
    await shot("decks", "The three decks (Office, Visitors, Social): each has a Draw a card button and eight face-down cards showing level and grammar formations.", '[data-scdraw="office"]', "el:.sc-grid")
    await sizes("home")
    await pg.click("details.vocab summary"); await shot("how_it_works", "How Scramble works: the five steps (draw, pre-flight, answer, repair phrase, debrief) in a fold-out at the bottom of the home.", "details.vocab", "el:details.vocab")
    await pg.click("details.vocab summary")
    await pg.click("#scSlow"); await pg.wait_for_timeout(200); slow_on = await ev("() => gs.slow"); await pg.click("#scSlow"); await pg.wait_for_timeout(200)
    notes.append(f"Slow voice toggle: on={slow_on}, then off={await ev('() => gs.slow')}")
    await pg.click("#scVoiceChk"); await pg.wait_for_timeout(500)
    notes.append("Voice & mic check opened: " + str(await ev("() => { const e = document.querySelector('#refBox'); return e ? e.textContent.trim().slice(0,120) : null; }")))
    await pg.screenshot(path=f"{TMP}/_voicecheck.png")
    closed = await ev("() => { const m = document.querySelector('#refBox'); let e = m; while (e && e !== document.body) { const b = e.querySelector('button[id*=lose], .close, [data-close]'); if (b) { b.click(); return b.id || b.className; } e = e.parentElement; } return null; }")
    notes.append(f"voice check closed via: {closed}")
    await pg.wait_for_timeout(300)
    if await ev("() => { const m = document.querySelector('#refBox'); return !!(m && m.offsetParent); }"):
        await pg.keyboard.press("Escape"); await pg.wait_for_timeout(200)
        if await ev("() => { const m = document.querySelector('#refBox'); return !!(m && m.offsetParent); }"):
            notes.append("voice check modal did not close with its button or Escape; reloaded page"); await pg.goto("http://localhost:8103/?tab=sc"); await pg.wait_for_timeout(800)

    SETS = {"o1": {"pre","talk","miss","partial","debrief"}, "o2": {"mic"}, "o3": {"repair"}, "v1": {"any_home","any_card"}, "v2": {"repair_typed"}, "v7": {"hint","fdlink"}, "v7b": {"second","slip"}, "s7": {"chip_talk"}}
    for k in ORDER:
        try:
            await play(k, SETS.get(k, set()))
        except Exception as e:
            notes.append(f"ERROR on {k}: {e!r}"); await pg.screenshot(path=f"{TMP}/_err_{k}.png"); 
            await pg.goto("http://localhost:8103/?tab=sc"); await pg.wait_for_timeout(800)
        if k == "o8":
            await home(); 
    await home(); await pg.wait_for_timeout(300)
    state_before_lesson = await ev("() => JSON.parse(JSON.stringify({c: gs.sc.c, k: gs.sc.k, runs: gs.sc.runs, errs: gs.errs || {}}))")
    await shot("home_after", "Tab home after play: the counters now show how many cards are cleared and flown.", ".sc-banner .cstats", "top")
    await shot("tiles_after", "A deck after play: every card now shows its title, its stamp (Cleared / Partial) and best score, with an Again button.", ".sc-tile .sc-st", "el:.sc-grid")
    await shot("radar", "Objective radar: first-try rate for each kind of move (ask politely, say the plan, explain ...), lowest first - what to practise next.", ".gs-radar", "el:.gs-radar")
    radar = await ev("() => Array.from(document.querySelectorAll('.gs-radar .gr-row')).map(r => r.textContent.trim().replace(/\\s+/g,' '))")
    # ---------- lesson mode ----------
    await pg.click("#scLive"); await pg.wait_for_timeout(300)
    await shot("lesson_home", "Lesson mode switched on: a note explains that the teacher shares the screen, deals any card and marks each objective.", ".fd-livenote", "el:.gs-strip")
    await pg.click('[data-scgo="s8"]'); await pg.wait_for_timeout(300)
    await pg.click("#scGo"); await pg.wait_for_timeout(300)
    lesson = {"card": "s8", "marks": []}
    for ti in range(2):
        n = await ev("() => scTurn().objs.length")
        for i in range(n): await pg.click(f'[data-sct="{i}:{"c" if not (ti == 0 and i == 1) else "p"}"]')
        await pg.click('[data-scflu="3"]')
        opts = await ev("() => Array.from(document.querySelectorAll('#scTag option')).map(o => o.textContent)")
        if ti == 0:
            await pg.select_option("#scTag", index=1)
            await shot("lesson_mark", "Lesson mode screen: no microphone. The teacher marks each objective (tick, half, cross), gives fluency 1-3, picks a grammar note and saves.", ".fd-tbox", "el:#scSpeak")
            await sizes("lesson mode marking")
        lesson["marks"].append({"exchange": ti+1, "tm": await ev("() => SCP.tm"), "flu": 3, "tags": opts[:4]})
        await pg.click("#scTSave"); await pg.wait_for_timeout(300); await pg.click("#scNext"); await pg.wait_for_timeout(400)
    lesson["debrief"] = await ev("() => document.querySelector('.gs-resh').textContent.trim().replace(/\\s+/g,' ')")
    lesson["rec"] = await ev("() => gs.sc.c.s8")
    await shot("lesson_debrief", "Lesson-mode debrief: the score comes from the teacher's marks ('Scored by the teacher').", ".gs-resh", "top")
    await pg.click("#scHome"); await pg.wait_for_timeout(300); await pg.click("#scLive"); await pg.wait_for_timeout(300)
    lesson["live_after"] = await ev("() => !!gs.sc.live")
    final = await ev("() => JSON.parse(JSON.stringify({c: gs.sc.c, k: gs.sc.k, runs: gs.sc.runs, errs: gs.errs || {}}))")
    json.dump({"shots": shots, "log": log, "cards": cards, "notes": notes, "layout": layout, "state_before_lesson": state_before_lesson, "final": final, "radar": radar, "lesson": lesson, "pageerrors": errs, "blocked": sorted(set(blocked)), "secs": round(time.time() - T0)}, open(OUT + "/raw.json", "w"), ensure_ascii=False, indent=1)
    await b.close()
asyncio.run(main())
