import json, glob, sys, time
from playwright.sync_api import sync_playwright

OUT = "/home/claude/wt/A1"
URL = "http://localhost:8101/?tab=sc"
H = "HINT"   # marker: tap Hint before the next typed answer

# persona plan: chips to open, per exchange a list of steps
# step = text to type | H | "REPAIRBTN"
PLAN = {
 "o1": dict(chips=[0], t=[["Hello. Khun Nok check invoice."], ["Wing Commander Anan sign payment."]]),
 "o2": dict(chips=[0, 2], t=[["3", "There are three invoice."], ["Yes. Invoice two date wrong."]]),
 "o3": dict(chips=[0, 1], t=[["REPAIRBTN", "Sorry Colonel. Report not finish.", "Sorry Colonel Hayes, it isn't ready."], ["Tomorow morning."]]),
 "o4": dict(chips=[0, 1, 2], t=[["Hello Captain Ellis. You have invoice number?"], ["4 5 1. Thank you. Is US dollar?"]]),
 "o5": dict(chips=[0, 1], t=[["OK. You come what day?"], ["Room 204, floor 2. See you Thursday."]]),
 "o6": dict(chips=[0, 2], t=[["Sorry. I not send. Have mistake.", "I'm sorry, I didn't send."], ["I want two more day.", H, "Could I have two more day please?"]]),
 "o7": dict(chips=[0, 1], t=[["REPAIRBTN", "Sorry Mr Mike. Bank detail wrong."], ["Friday we pay.", "We will pay Friday."]]),
 "o8": dict(chips=[0, 1, 2], t=[["Excuse me sir. I want signature.", "Could you sign this form please?"], ["Yes sir. Bank close 3 o'clock. Thank you."]]),
 "v1": dict(chips=[0, 1], t=[["Floor 2, next to lift."], ["9 am", "It start 9 am."]]),
 "v2": dict(chips=[0, 2], t=[["REPAIRBTN", "I book three night. Please check again.", "I have booking three night. Can you check?"], ["4729", "Yes. Number 4729."]]),
 "v3": dict(chips=[0, 1], t=[["Welcome to base. How your flight?"], ["First go security office."]]),
 "v4": dict(chips=[0, 1, 2], t=[["We talk travel budget. Boss say ok.", "Wing Commander Anan approve plan."], ["No. I send today.", H, "Not yet. I will send afternoon."]]),
 "v5": dict(chips=[0, 2], t=[["Again please", "Tomorrow we go finance office 10 o'clock.", "Tomorrow we are going to visit finance."], ["REPAIRBTN", "Bring ID card please."]]),
 "v6": dict(chips=[0, 1, 2], t=[["I want receipt please.", "How many receipt you have?"], ["OK. You write this form please."]]),
 "v7": dict(chips=[0, 1, 2], t=[["Sorry. Please send new bank detail today.", H, "If you send today, we pay tomorrow."], ["I call you again.", H, H, "I will call you."]]),
 "v8": dict(chips=[0, 1, 2], t=[["Two payment pay already. One come back.", H, "Two payments were made. One payment return."], ["Account number wrong."]]),
 "s1": dict(chips=[0], t=[["I work finance. I am accountant."], ["He sign payment."]]),
 "s2": dict(chips=[0, 1], t=[["Yes, I like spicy. You like?", "Do you like Thai food?"], ["This one not spicy."]]),
 "s3": dict(chips=[0, 2], t=[["REPAIRBTN", "I study business."], ["Yes. I like. But very cold."]]),
 "s4": dict(chips=[0, 1], t=[["I go by BTS. And you?"], ["Wat Pho very beautiful.", "You go Wat Pho."]]),
 "s5": dict(chips=[0, 2], t=[["I go home see my mother.", "I going to visit my mother."], ["You can go Chatuchak market."]]),
 "s6": dict(chips=[0, 1, 2], t=[["Excuse me madam. Photo with you please?", "Could we take photo with you?"], ["Here, middle please. Thank you madam."]]),
 "s7": dict(chips=[0, 1], t=[["I don't understand", "ไม่เข้าใจค่ะ", "I go Chiang Mai.", H, "I would go to Chiang Mai."], ["You should go Phuket. Beach beautiful."]]),
 "s8": dict(chips=[1], t=[["Thank you very much. Safe flight."], ["Goodbye", "Goodbye. See you again."]]),
}
ORDER = list(PLAN.keys())

log = {"persona": "A1-Demii", "level": "A1", "started": time.strftime("%Y-%m-%d %H:%M:%S"), "viewport": "390x844@2x mobile touch",
       "input": "typing fallback (no microphone in headless Chromium)", "exchanges": [], "cards": [], "events": [], "layout": {}, "console": [], "blocked": []}
shotn = [0]

with sync_playwright() as pw:
    exe = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux*/chrome"))[0]
    br = pw.chromium.launch(executable_path=exe, headless=True)
    ctx = br.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")
    ctx.route("**/*", lambda r: (log["blocked"].append(r.request.url), r.abort())[1] if ("script.google.com" in r.request.url or "googleusercontent" in r.request.url) else r.continue_())
    ctx.add_init_script("""
      try { if (window.speechSynthesis) { speechSynthesis.speak = function(u){ setTimeout(function(){ try{ u.onend && u.onend({}); }catch(e){} }, 20); }; speechSynthesis.cancel = function(){}; } } catch(e){}
      try { HTMLMediaElement.prototype.play = function(){ var a=this; setTimeout(function(){ try{ a.dispatchEvent(new Event('ended')); }catch(e){} }, 20); return Promise.resolve(); }; } catch(e){}
    """)
    pg = ctx.new_page()
    pg.on("console", lambda m: log["console"].append(m.type + ": " + m.text[:200]) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: log["console"].append("pageerror: " + str(e)[:300]))
    dialogs = {"mode": "dismiss", "seen": []}
    def on_dialog(d):
        dialogs["seen"].append(d.message)
        d.accept() if dialogs["mode"] == "accept" else d.dismiss()
    pg.on("dialog", on_dialog)
    pg.goto(URL); pg.wait_for_timeout(1200)

    def shot(name, sel=None, top=False):
        if sel:
            try: pg.locator(sel).first.scroll_into_view_if_needed(timeout=1500)
            except Exception: pass
        if top: pg.evaluate("window.scrollTo(0,0)")
        pg.wait_for_timeout(650)
        shotn[0] += 1
        p = f"{OUT}/shots/{shotn[0]:02d}-{name}.png"
        pg.screenshot(path=p)
        return p
    def ev(msg, **kw):
        log["events"].append(dict(msg=msg, **kw)); print("EV", msg, kw, flush=True)
    def tap(sel):
        pg.locator(sel).first.click(timeout=4000); pg.wait_for_timeout(120)
    def has(sel): return pg.locator(sel).count() > 0
    def layout(name):
        log["layout"][name] = pg.evaluate("""() => {
          const out = {overflowX: document.documentElement.scrollWidth - window.innerWidth, pageH: document.documentElement.scrollHeight, items: []};
          const sels = ['.tabs .tab','.cbanner h2','.cbanner p','.cstat .v','.cstat .k','.gs-strip .hbtn','.gs-mic','#scAny','.fd-review small','[data-scdraw]','.sc-dd','.sc-tile b','.sc-tile small','.sc-tile .dbtn','.sc-tile .chip','.gr-row','.gs-radar p',
            '#scBack','.pbar h2','.bdg','.sc-sit','.sc-th','.sc-obj','.sc-forms','.sc-forms .chip','.sc-clock small','.gs-fine','.sc-chip','.sc-chip small','#scGo',
            '.gs-bub','.gs-play','.sc-ob','.sc-sitd summary','.gs-score','.gs-mictxt','.gs-mictxt small','.gs-micbtn','#scHint','#scRepeat','#scType','#scSkip','#scTypeIn','#scTypeOk','#scBackMic','.gs-c','.gs-c small','.fd-frame','.gs-note','.sc-st','#scNext','#scModel',
            '.gs-resv','.gs-resh b','.gs-resh small','.sc-dbq','.sc-links .btn','#scMore','#scRetry','#scHome','[data-scm]','.gs-said'];
          for (const s of sels) { const els = [...document.querySelectorAll(s)].filter(e => e.offsetParent !== null); if (!els.length) continue; const e = els[0], r = e.getBoundingClientRect(), cs = getComputedStyle(e);
            out.items.push({sel: s, n: els.length, font: +parseFloat(cs.fontSize).toFixed(1), w: Math.round(r.width), h: Math.round(r.height), color: cs.color, right: Math.round(r.right)}); }
          return out; }""")
    def sc(): return pg.evaluate("() => JSON.parse(JSON.stringify(gs.sc || {}))")
    def scp(): return pg.evaluate("() => SCP ? {id: SCP.card.id, ti: SCP.ti, phase: SCP.phase, sub: SCP.sub, tries: SCP.tries, lad: SCP.lad, hits: SCP.hits, first: SCP.first, repairs: SCP.repairs, issue: SCP.issue, chips: SCP.chips, slip: SCP.slip, res: SCP.res} : null")
    def coach():
        return pg.evaluate("() => { const e = document.querySelector('.gs-coach'); return e ? e.innerText.trim() : ''; }")

    # ---------- home ----------
    ev("home loaded", title=pg.title(), sc=sc(), mic=pg.evaluate("() => document.querySelector('.gs-mic') ? document.querySelector('.gs-mic').innerText : ''"),
       free=pg.evaluate("() => !!store.free"), user=pg.evaluate("() => typeof USER === 'undefined' ? null : (USER ? 'yes' : 'none')"))
    layout("home-before")
    shot("tab-home", top=True)
    shot("home-decks", sel=".sc-deck")
    tap("details.vocab summary"); shot("home-how-it-works", sel="details.vocab")
    tap("details.vocab summary")
    ev("unseen tiles have no button", unseenButtons=pg.evaluate("() => document.querySelectorAll('.sc-tile.new button').length"), tiles=pg.evaluate("() => document.querySelectorAll('.sc-tile').length"))

    SHOTS = {  # (card, stage) -> name
      ("o1", "pre"): "card-face-o1", ("o1", "prechip"): "preflight-chip-open-o1", ("o1", "stage"): "exchange-npc-o1", ("o1", "typed0"): "typed-answer-o1", ("o1", "pass0"): "feedback-cleared-o1", ("o1", "debrief"): "debrief-cleared-o1",
      ("o2", "after0-0"): "too-short-3-o2",
      ("o3", "repair0"): "repair-button-o3", ("o3", "after0-1"): "false-negative-not-finish-o3",
      ("o6", "after1-0"): "i-want-miss-o6", ("o6", "hint1"): "hint-frames-o6", ("o6", "after1-2"): "move-on-visible-o6", ("o6", "pass1"): "moved-on-feedback-o6", ("o6", "debrief"): "debrief-partial-o6",
      ("v2", "after1-0"): "too-short-4729-v2",
      ("v5", "after0-0"): "again-please-not-repair-v5",
      ("v7", "hint1-2"): "hint-model-v7", ("v7", "debrief"): "debrief-v7",
      ("v8", "pre"): "card-face-v8-b1", ("v8", "debrief"): "debrief-not-yet-v8",
      ("s4", "after1-1"): "stuck-no-guidance-s4",
      ("s7", "after0-0"): "dont-understand-repair-s7", ("s7", "after0-1"): "thai-typed-s7",
    }
    def cshot(cid, stage, **kw):
        if (cid, stage) in SHOTS: shot(SHOTS[(cid, stage)], **kw)

    def play(cid, expect=True, stop_after_first=False):
        plan = PLAN[cid]
        cur = scp()
        if cur is None or cur["id"] != cid:
            ev("UNEXPECTED CARD", wanted=cid, got=cur and cur["id"])
            if cur is None: return None
            cid = cur["id"]; plan = PLAN[cid]
        face = pg.evaluate("() => ({kick: document.querySelector('.sc-cardface .kick').innerText, clock: document.querySelector('#scClock').innerText})")
        cshot(cid, "pre", top=True)
        if cid == "o1": layout("preflight")
        for i in plan["chips"]:
            tap(f'[data-scchip="{i}"]')
        if plan["chips"]: cshot(cid, "prechip", sel="#scGo")
        pre_left = pg.evaluate("() => SCP.left")
        tap("#scGo"); pg.wait_for_timeout(250)
        card_ex = []
        for ti, steps in enumerate(plan["t"]):
            st0 = scp()
            assert st0["ti"] == ti, (cid, ti, st0)
            if ti == 0: cshot(cid, "stage", top=True)
            if cid == "o1" and ti == 0: layout("exchange-ready")
            entry = {"card": cid, "exchange": ti + 1, "npc": pg.evaluate("() => scTurn().npc"), "objectives": pg.evaluate("() => scTurn().objs.map(o => o.k + ': ' + o.lab)"),
                     "chips_opened": [pg.evaluate(f"() => SCP.card.chips[{i}]") for i in plan["chips"]], "attempts": [], "hints": 0, "repairs": 0, "moved_on": False}
            hints = 0; ai = 0
            for step in steps:
                if scp()["sub"] == "passed": break
                if step == "REPAIRBTN":
                    tap("#scRepeat"); pg.wait_for_timeout(300)
                    entry["repairs"] += 1
                    entry["attempts"].append({"action": "tapped 'Ask to repeat'", "app": coach(), "tries_after": scp()["tries"]})
                    cshot(cid, f"repair{ti}", sel="#scSpeak")
                    continue
                if step == H:
                    if has("#scHint:not([disabled])"):
                        tap("#scHint"); hints += 1; entry["hints"] = hints
                        entry["attempts"].append({"action": f"tapped Hint (level {hints})", "app": coach()})
                        cshot(cid, f"hint{ti}" + ("" if hints == 1 else f"-{hints}"), sel=".gs-coach")
                        if cid == "o6": layout("hint")
                    continue
                # type an answer
                pre = pg.evaluate("(a) => { const e = scEval(scTurn(), a); return {status: e.status, hits: e.hits, slip: e.slip, norm: e.norm}; }", step)
                needed_type_tap = has("#scType")
                if needed_type_tap: tap("#scType")
                pg.locator("#scTypeIn").fill(step)
                if ai == 0 and ti == 0:
                    cshot(cid, "typed0", sel="#scTypeOk")
                    if cid == "o1": layout("typing")
                tap("#scTypeOk"); pg.wait_for_timeout(250)
                s = scp()
                objs = pg.evaluate("() => scTurn().objs.map(o => o.k)")
                a = {"typed": step, "norm": pre["norm"], "status": pre["status"], "hit_this_try": [o for o, h in zip(objs, pre["hits"]) if h], "missed_this_try": [o for o, h in zip(objs, pre["hits"]) if not h],
                     "slip": pre["slip"], "tries_after": s["tries"], "passed": s["sub"] == "passed", "app": coach() if s["sub"] != "passed" else pg.evaluate("() => document.querySelector('.gs-pass').innerText.trim()"),
                     "move_on_visible": has("#scSkip"), "had_to_tap_type_instead": needed_type_tap}
                entry["attempts"].append(a)
                if s["sub"] != "passed": cshot(cid, f"after{ti}-{ai}", sel="#scSpeak")
                ai += 1
            s = scp()
            if s["sub"] != "passed":
                guard = 0
                while not has("#scSkip") and guard < 4:   # stuck with no Move on: she types "I don't know"
                    guard += 1
                    if has("#scType"): tap("#scType")
                    pg.locator("#scTypeIn").fill("I don't know"); tap("#scTypeOk"); pg.wait_for_timeout(200)
                    entry["attempts"].append({"typed": "I don't know", "note": "no Move on button yet", "tries_after": scp()["tries"], "app": coach()})
                    if scp()["sub"] == "passed": break
                if scp()["sub"] != "passed":
                    tap("#scSkip"); pg.wait_for_timeout(250); entry["moved_on"] = True
            s = scp()
            R = s["res"][ti]
            entry["tries"] = R["tries"]; entry["stamps"] = dict(zip(pg.evaluate("() => scTurn().objs.map(o => o.k + ': ' + o.lab)"), R["st"]))
            entry["stamp"] = "Cleared" if all(x == "c" for x in R["st"]) else ("Not yet" if all(x == "m" for x in R["st"]) else "Partial")
            entry["slip_kept"] = R["slip"]
            entry["feedback"] = pg.evaluate("() => document.querySelector('.gs-pass').innerText.trim()")
            cshot(cid, f"pass{ti}", sel="#scNext")
            if cid == "o1" and ti == 0: layout("feedback")
            log["exchanges"].append(entry); card_ex.append(entry)
            print(cid, ti + 1, entry["stamp"], [(a.get("typed"), a.get("status")) for a in entry["attempts"] if "typed" in a], flush=True)
            if stop_after_first: return None
            tap("#scNext"); pg.wait_for_timeout(350)
        rec = sc()["c"].get(cid)
        deb = pg.evaluate("() => ({score: document.querySelector('.gs-resv').innerText, tier: document.querySelector('.gs-resh .kick').innerText, line: document.querySelector('.gs-resh b').innerText, small: document.querySelector('.gs-resh small').innerText, note: (document.querySelector('.gs-resbox > .gs-c') || {}).innerText || '', links: [...document.querySelectorAll('.sc-links button')].map(b => b.innerText), buttons: [...document.querySelectorAll('.gs-resbox > .gs-acts button')].map(b => b.innerText)})")
        cshot(cid, "debrief", top=True)
        if cid in ("o1", "o6"): layout("debrief-" + cid)
        card = {"card": cid, "title": pg.evaluate("(i) => scCard(i).title", cid), "level": pg.evaluate("(i) => scCard(i).lvl", cid), "chips": len(plan["chips"]), "preflight_secs_used": 20 - pre_left,
                "final_stamp": {"c": "Cleared", "p": "Partial", "m": "Not yet"}[rec["s"]], "score": deb["score"], "best": rec["best"], "due": rec["due"], "debrief": deb, "face": face}
        log["cards"].append(card)
        print("  ->", cid, card["final_stamp"], card["score"], flush=True)
        return card

    # ---------- run ----------
    tap("#scAny"); pg.wait_for_timeout(300)
    ev("Scramble surprise draw", got=scp()["id"])
    for idx, cid in enumerate(ORDER):
        if idx > 0 and scp() is None:
            deck = {"o": "office", "v": "visitors", "s": "social"}[cid[0]]
            tap(f'[data-scdraw="{deck}"]'); pg.wait_for_timeout(300)
            ev("Draw a card", deck=deck, got=scp()["id"])
        play(cid)
        nxt = ORDER[idx + 1] if idx + 1 < len(ORDER) else None
        # debrief links
        if cid == "o6":
            shot("debrief-links-o6", sel=".sc-links")
            tap(".sc-links [data-scfd]"); pg.wait_for_timeout(500)
            ev("debrief formation link", view=pg.evaluate("() => view"), tab=pg.evaluate("() => store.tab"), heading=pg.evaluate("() => (document.querySelector('.pbar h2')||{}).innerText || ''"),
               backBtn=pg.evaluate("() => (document.querySelector('.pbar button')||{}).innerText || ''"))
            shot("formation-link-target", top=True)
            tap(".pbar button"); pg.wait_for_timeout(400)
            ev("back from formation", view=pg.evaluate("() => view"), tabOn=pg.evaluate("() => (document.querySelector('.tabs .tab.on')||{}).innerText || ''"))
            tap('[data-tab="sc"]'); pg.wait_for_timeout(400)
            layout("home-mid"); shot("home-after-office-6", sel='[data-scdraw="office"]')
            continue
        if cid == "v7":
            tap("#scRetry"); pg.wait_for_timeout(300)
            ev("Fly this card again", got=scp()["id"], kick=pg.evaluate("() => document.querySelector('.sc-cardface .kick').innerText"))
            tap("#scBack"); pg.wait_for_timeout(300)
            ev("back from pre-flight (no confirm expected)", dialogs=list(dialogs["seen"]), view=pg.evaluate("() => view"))
            continue
        if cid in ("o8", "v8"):
            tap("#scHome"); pg.wait_for_timeout(300)
            if cid == "o8": shot("home-office-done", sel=".sc-deck")
            continue
        if nxt:
            tap("#scMore"); pg.wait_for_timeout(300)
            ev("Draw another", after=cid, got=scp()["id"])
    tap("#scHome"); pg.wait_for_timeout(400)

    # ---------- after play ----------
    layout("home-after")
    shot("home-after-top", top=True)
    shot("radar-after-play", sel=".gs-radar")
    shot("home-social-deck-after", sel=".sc-deck:nth-of-type(3)")
    log["radar"] = pg.evaluate("() => [...document.querySelectorAll('.gs-radar .gr-row')].map(r => r.innerText.replace(/\\n/g,' '))")
    log["kinds"] = sc()["k"]
    log["review_banner"] = pg.evaluate("() => document.querySelector('.fd-review').innerText")
    # Scramble button once everything has been seen
    tap("#scAny"); pg.wait_for_timeout(300)
    ev("Scramble after all seen", got=scp()["id"], status=sc()["c"][scp()["id"]]["s"], kick=pg.evaluate("() => document.querySelector('.sc-cardface .kick').innerText"))
    shot("second-look-card-face", top=True)
    tap("#scBack"); pg.wait_for_timeout(300)
    # replay via Again tile, then leave mid-card (confirm)
    before = json.dumps(sc()["c"]["o6"])
    tap('[data-scgo="o6"]'); pg.wait_for_timeout(300)
    tap("#scGo"); pg.wait_for_timeout(200)
    tap("#scType"); pg.locator("#scTypeIn").fill("Sorry. I not send yet."); tap("#scTypeOk"); pg.wait_for_timeout(250)
    ev("replay o6 e1", typed="Sorry. I not send yet.", state=scp())
    if scp()["sub"] == "passed": tap("#scNext"); pg.wait_for_timeout(250)
    dialogs["mode"] = "dismiss"; tap("#scBack"); pg.wait_for_timeout(250)
    ev("leave mid-card: dismissed confirm", dialog=dialogs["seen"][-1:] , stillOn=scp() and scp()["id"])
    dialogs["mode"] = "accept"; tap("#scBack"); pg.wait_for_timeout(300)
    ev("leave mid-card: accepted", view=pg.evaluate("() => view"), o6_unchanged=(json.dumps(sc()["c"]["o6"]) == before), kinds_changed=(sc()["k"] != log["kinds"]))
    # no Move on after only short answers (o2 e1): type one word three times
    tap('[data-scgo="o2"]'); pg.wait_for_timeout(250); tap("#scGo"); pg.wait_for_timeout(200)
    stuck = []
    for w in ["Three", "3", "Three."]:
        if has("#scType"): tap("#scType")
        pg.locator("#scTypeIn").fill(w); tap("#scTypeOk"); pg.wait_for_timeout(200)
        stuck.append({"typed": w, "tries": scp()["tries"], "move_on": has("#scSkip"), "coach": coach()})
    ev("one-word answers never open Move on", steps=stuck)
    shot("short-loop-no-move-on", sel="#scSpeak")
    dialogs["mode"] = "accept"; tap("#scBack"); pg.wait_for_timeout(300)
    ev("final home", view=pg.evaluate("() => view"), dialogs=dialogs["seen"])

    # ---------- checker probes (read-only scEval, nothing saved) ----------
    probes = [
      ("o2", 1, "No problem. Invoice two ok."), ("o2", 0, "Three."), ("o3", 0, "Sorry Colonel Sarah. Not ready."), ("o3", 0, "Sorry madam. Report not finish."), ("o3", 0, "Sorry madam. Not finish yet."),
      ("o3", 1, "Tomorrow."), ("o3", 1, "Yesterday morning."), ("o5", 0, "When you free?"), ("o6", 1, "Can I have two day more please?"), ("o6", 1, "Two more day please."),
      ("o6", 0, "Sorry. I forget."), ("o7", 1, "Pay on Friday."), ("o7", 1, "Friday."), ("o8", 0, "Sir, please sign this form."), ("o8", 0, "Excuse me sir. Please sign."),
      ("v1", 1, "9"), ("v1", 1, "Nine."), ("v1", 1, "At 9."), ("v2", 0, "I book room. Please check again."), ("v2", 1, "4 7 2 9"), ("v2", 1, "four seven two nine"),
      ("v3", 0, "Hello. Welcome. You tired?"), ("v4", 0, "Travel budget. Boss ok."), ("v4", 0, "We talk budget. Wing Commander say yes."), ("v4", 1, "Not yet. I send today."), ("v4", 1, "I will send."),
      ("v5", 0, "Tomorrow go to finance office at 10."), ("v6", 1, "No problem."), ("v6", 0, "Receipt please. How many?"), ("v7", 1, "I call you."), ("v8", 0, "Two paid. One returned."), ("v8", 0, "Two ok. One come back."),
      ("s2", 0, "No. And you?"), ("s2", 1, "No problem."), ("s3", 1, "No."), ("s4", 1, "Grand Palace."), ("s4", 1, "I see."), ("s5", 0, "I stay home."), ("s5", 0, "I sleep."), ("s5", 1, "Chatuchak market is good."),
      ("s6", 0, "Madam, photo please."), ("s7", 0, "I want go Japan."), ("s7", 0, "Chiang Mai."), ("s8", 1, "Bye."), ("s8", 1, "Bye bye."), ("s8", 0, "Thank you. Good luck."),
      ("o1", 0, "Sorry?"), ("o1", 0, "Slowly please."), ("o1", 0, "Again please."), ("o1", 0, "Say again please."), ("o1", 0, "What?"), ("o1", 0, "I not understand."), ("o1", 0, "Hello. I check."), ("o1", 1, "I don't know who signs."),
    ]
    log["probes"] = [dict(card=c, exchange=t + 1, typed=a, **pg.evaluate("([c,t,a]) => { const T = scCard(c).turns[t], e = scEval(T, a); return {status: e.status, hits: T.objs.map((o,i) => o.k + (e.hits[i] ? '✓' : '–')).join(' '), slip: e.slip ? e.slip.tag : null}; }", [c, t, a])) for c, t, a in probes]
    log["final_state"] = sc()
    br.close()

# ---------- summary ----------
ex = log["exchanges"]; cards = log["cards"]
log["summary"] = {
  "cards_played": len(cards), "exchanges": len(ex),
  "cards": {k: sum(1 for c in cards if c["final_stamp"] == k) for k in ("Cleared", "Partial", "Not yet")},
  "exchanges_by_stamp": {k: sum(1 for e in ex if e["stamp"] == k) for k in ("Cleared", "Partial", "Not yet")},
  "by_deck": {d: {k: sum(1 for c in cards if c["card"][0] == d[0] and c["final_stamp"] == k) for k in ("Cleared", "Partial", "Not yet")} for d in ("office", "visitors", "social")},
  "avg_score_by_deck": {d: round(sum(c["best"] for c in cards if c["card"][0] == d[0]) / max(1, sum(1 for c in cards if c["card"][0] == d[0]))) for d in ("office", "visitors", "social")},
  "typed_answers": sum(1 for e in ex for a in e["attempts"] if "typed" in a),
  "too_short": sum(1 for e in ex for a in e["attempts"] if a.get("status") in ("short", "empty")),
  "repairs_button": sum(e["repairs"] for e in ex), "hints": sum(e["hints"] for e in ex), "moved_on": sum(1 for e in ex if e["moved_on"]),
  "chips_opened": sum(c["chips"] for c in cards), "screenshots": shotn[0],
}
log["finished"] = time.strftime("%Y-%m-%d %H:%M:%S")
json.dump(log, open(OUT + "/log.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(log["summary"], indent=1))
print("console:", log["console"][:10], "blocked:", log["blocked"][:5])
