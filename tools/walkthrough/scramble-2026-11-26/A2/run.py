import json, time, sys
from playwright.sync_api import sync_playwright
OUT="/home/claude/wt/A2"; URL="http://localhost:8102/?tab=sc"
P={ # id: (chip index or None, [attempts e1], [attempts e2])
"o1":(None,["Good morning Mr Eriksen. Khun Nok check the invoices."],["Wing Commander Anan sign the payments."]),
"o2":(0,["Hello Mr Turner. There is three invoices in the file."],["Yes, invoice number two have wrong date."]),
"o3":(None,["Good afternoon Colonel Sarah. Sorry, the report not finish yet.","Sorry Ma'am. The report is not ready yet."],["It will ready tomorrow morning Ma'am."]),
"o4":(1,["Hello Captain Ellis. What is your invoice number please?"],["@repair","451, thank you. It is US dollar?"]),
"o5":(None,["Yes Mr Eriksen. Which day you want to come?"],["Please come to room 204 on second floor. See you Thursday."]),
"o6":(2,["Sorry Mr Eriksen, I didn't sent them. Yesterday I find a mistake."],["Could I have two more day please? I will send on Friday."]),
"o7":(None,["I am sorry Mr Mike. The bank details was wrong."],["We pay on Friday.","We will pay on Friday."]),
"o8":(0,["Excuse me Sir. Can you sign this form?","Can you sign this form please Sir?"],["Yes Sir, because the bank close at three o'clock. Thank you Sir."]),
"v1":(None,["It on the second floor, next to the lift."],["It start at nine o'clock."]),
"v2":(1,["Good evening. I booked a room for three nights. Could you check again please?"],["Yes, my number is 4729."]),
"v3":(None,["Welcome to Thailand Mr Hughes. How about your flight?"],["First we go to security office. Please follow me."]),
"v4":(1,["We talk about travel budget Ma'am. Wing Commander Anan approve the plan."],["Not yet Ma'am. I will send to you this afternoon."]),
"v5":(None,["Tomorrow we going to visit the finance office at ten."],["Yes, you must bring ID card."]),
"v6":(0,["Could you give me the receipt please Ma'am? How much receipts do you have?"],["No problem Ma'am. Please fill this form for the lost one."]),
"v7":(None,["I am sorry Captain. Please send new bank details today and we pay again tomorrow.","@hint","If you send new bank details today, we will pay tomorrow."],["I will call you and check again."]),
"v8":(0,["Two payments were made last week. One payment the bank return because wrong account number.","One payment come back from the bank.","@skip"],["Because the account number is wrong."]),
"s1":(None,["I work at finance division. I am accountant."],["He is Wing Commander. He sign the document."]),
"s2":(1,["Yes, I like spicy food very much. Do you like Thai food?"],["You can eat this soup. It not spicy."]),
"s3":(None,["I study business in UK."],["Yes, I like it. But weather is so cold."]),
"s4":(0,["I take the BTS. And you? Where you stay?"],["You should go to Wat Pho. It is very beautiful."]),
"s5":(None,["I will go to Chiang Mai with my friend."],["Sorry, I not understand.","@repair","You can go to Chatuchak market."]),
"s6":(None,["Excuse me Colonel Sarah. Can we take a photo with you?","Excuse me Colonel Hayes."],["Pardon?","Please stand here in the middle. Thank you Ma'am."]),
"s7":(None,["I want to go to Japan.","I will go to Japan with my family.","@skip"],["Next time I take you to Chiang Mai.","@hint","You should visit Chiang Mai."]),
"s8":(1,["Thank you for everything Mr Tom. Have a safe flight."],["See you again. Goodbye."]),
}
SHOT={"n":0}; log={"persona":"A2-Demii","exchanges":[],"cards":{},"events":[],"layout":{},"console":[],"blocked":[]}
def shot(page,name,wait=650):
    page.wait_for_timeout(wait); SHOT["n"]+=1
    page.screenshot(path=f"{OUT}/shots/{SHOT['n']:02d}-{name}.png")
def ev(m,**k): log["events"].append(dict(msg=m,**k)); print("EV",m,k,flush=True)
ST="""()=>SCP?{id:SCP.card.id,ti:SCP.ti,phase:SCP.phase,sub:SCP.sub,tries:SCP.tries,hits:SCP.hits,first:SCP.first,issue:SCP.issue,lad:SCP.lad,repairs:SCP.repairs,slip:SCP.slip,chips:SCP.chips,res:SCP.res,live:SCP.live}:null"""
LAY="""()=>{const sw=document.scrollingElement.scrollWidth,vw=window.innerWidth;const small=[];document.querySelectorAll('button,select,summary,textarea').forEach(b=>{const r=b.getBoundingClientRect();if(r.width&&r.height&&(r.height<40||r.width<40)){small.push((b.id||b.className||b.tagName)+':'+Math.round(r.width)+'x'+Math.round(r.height)+':'+(b.textContent||'').trim().slice(0,24))}});const over=[];document.querySelectorAll('#app *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width&&r.right>vw+2)over.push((e.className||e.tagName)+':'+Math.round(r.right))});return {sw,vw,small:[...new Set(small)].slice(0,25),over:[...new Set(over)].slice(0,10),docH:document.scrollingElement.scrollHeight}}"""
def lay(page,key):
    if key not in log["layout"]: log["layout"][key]=page.evaluate(LAY)
def setup(ctx,page):
    page.on("console",lambda m: log["console"].append(m.type+": "+m.text[:200]) if m.type in("error","warning") else None)
    page.on("pageerror",lambda e: log["console"].append("pageerror: "+str(e)[:300]))
    page.on("dialog",lambda d:(ev("dialog",text=d.message),d.accept()))
def st(page): return page.evaluate(ST)
def type_answer(page,text,shotname=None):
    if page.query_selector("#scType"): page.click("#scType")
    page.wait_for_selector("#scTypeIn"); page.fill("#scTypeIn","")
    page.type("#scTypeIn",text,delay=4)
    if shotname: shot(page,shotname)
    page.click("#scTypeOk"); page.wait_for_timeout(250)
def play(page,cid,plan,shots={},how=""):
    chip,*turns=plan; s=st(page); assert s and s["id"]==cid and s["phase"]=="pre",(s,cid)
    card=page.evaluate("id=>{const c=scCard(id);return {title:c.title,lvl:c.lvl,turns:c.turns.map(t=>({npc:t.npc,objs:t.objs.map(o=>o.k+':'+o.lab),model:t.model}))}}",cid)
    lay(page,"preflight")
    if "face" in shots: shot(page,shots["face"])
    chips=[]
    if chip is not None:
        page.click(f'#scChipBox [data-scchip="{chip}"]'); chips.append(page.evaluate("i=>SCP.card.chips[i]",chip))
        if "chip" in shots:
            page.evaluate("document.querySelector('#scChipBox').scrollIntoView({block:'center'})"); shot(page,shots["chip"])
    if "timeout" in shots:
        page.wait_for_timeout(21000); shot(page,shots["timeout"])
    page.click("#scGo"); page.wait_for_timeout(300)
    for ti,attempts in enumerate(turns):
        lay(page,"exchange")
        if f"ready{ti}" in shots: shot(page,shots[f"ready{ti}"])
        rec={"card":cid,"exchange":ti+1,"npc":card["turns"][ti]["npc"],"objectives":card["turns"][ti]["objs"],"chips_opened":chips,"how_drawn":how,"attempts":[]}
        seq=list(attempts); fb=False
        while True:
            s=st(page)
            if s["sub"]=="passed": break
            if not seq:
                fb=True; ev("fallback: plan exhausted, using hints then model",card=cid,ex=ti+1)
                seq=["@hint","@hint","MODEL"]
            a=seq.pop(0)
            if a=="@repair":
                page.click("#scRepeat"); page.wait_for_timeout(300); s2=st(page)
                rec["attempts"].append({"action":"tap 'Ask to repeat'","status":"repair","coach":page.inner_text(".gs-coach")[:160],"repairs":s2["repairs"],"tries":s2["tries"]})
                if f"repair{ti}" in shots: shot(page,shots[f"repair{ti}"])
            elif a=="@hint":
                page.click("#scHint"); page.wait_for_timeout(300)
                rec["attempts"].append({"action":"tap Hint","coach":page.inner_text(".gs-coach")[:300],"lad":st(page)["lad"]})
                if f"hint{ti}" in shots:
                    page.evaluate("document.querySelector('#scSpeak').scrollIntoView({block:'start'})"); shot(page,shots[f"hint{ti}"])
            elif a=="@skip":
                ok=page.query_selector("#scSkip") is not None
                if f"moveon{ti}" in shots:
                    page.evaluate("document.querySelector('#scSpeak').scrollIntoView({block:'start'})"); shot(page,shots[f"moveon{ti}"])
                if ok: page.click("#scSkip"); page.wait_for_timeout(300)
                rec["attempts"].append({"action":"tap Move on","available":ok})
            else:
                text=a if a!="MODEL" else card["turns"][ti]["model"].lower()
                pre=page.evaluate("([id,ti,t])=>{const e=scEval(scCard(id).turns[ti],t);return {status:e.status,hits:e.hits,slip:e.slip,norm:e.norm}}",[cid,ti,text])
                type_answer(page,text,shots.get(f"typed{ti}") if len(rec["attempts"])==0 else None)
                s2=st(page)
                at={"typed":text,"after_model":a=="MODEL","status":pre["status"],"hits_this_answer":pre["hits"],"slip":pre["slip"],"norm":pre["norm"],"hits_total":s2["hits"],"tries":s2["tries"],"sub":s2["sub"]}
                if s2["sub"]!="passed":
                    c=page.query_selector(".gs-coach"); at["coach"]=c.inner_text()[:260] if c else ""
                    k=f"miss{ti}"
                    if k in shots:
                        page.evaluate("document.querySelector('#scSpeak').scrollIntoView({block:'start'})"); shot(page,shots.pop(k))
                rec["attempts"].append(at)
        s=st(page); R=s["res"][ti]
        rec.update({"stamps":R["st"],"tries":R["tries"],"repairs":R["repairs"],"slip_kept":R["slip"],"fallback":fb,"feedback":page.inner_text("#scSpeak")[:300]})
        lay(page,"passed")
        if f"pass{ti}" in shots:
            page.evaluate("document.querySelector('#scSpeak').scrollIntoView({block:'start'})"); shot(page,shots[f"pass{ti}"])
        log["exchanges"].append(rec)
        page.click("#scNext"); page.wait_for_timeout(350)
    r=page.evaluate("id=>gs.sc.c[id]",cid)
    deb={"score":page.inner_text(".gs-resv"),"tier":page.inner_text(".gs-resh .kick"),"line":page.inner_text(".gs-resh small"),
         "note":(page.inner_text(".gs-resbox .gs-c") if page.query_selector(".gs-resbox>.gs-c") else ""),
         "links":[b.inner_text() for b in page.query_selector_all("[data-scfd]")],"rec":r,"chips":chips,"how_drawn":how}
    log["cards"].setdefault(cid,[]).append(deb); lay(page,"debrief")
    if "debrief" in shots: shot(page,shots["debrief"])
    if "debrief2" in shots:
        page.evaluate("window.scrollTo(0,document.body.scrollHeight)"); shot(page,shots["debrief2"])
    print(cid,deb["score"],deb["tier"],r,flush=True)
SH={
"o1":{"face":"04-card-face-o1","ready0":"05-exchange-ready-o1","typed0":"06-typing-answer-o1","pass0":"07-feedback-cleared-o1","debrief":"08-debrief-cleared-o1"},
"o2":{"chip":"09-preflight-chip-open-o2"},
"o3":{"miss0":"10-miss-coach-colonel-sarah-o3","debrief":"11-debrief-partial-o3"},
"o4":{"repair1":"12-repair-button-o4"},
"o8":{"miss0":"13-miss-no-please-o8"},
"v7":{"hint0":"14-hint-frame-v7"},
"v8":{"moveon0":"15-move-on-offered-v8","pass0":"16-after-move-on-v8","debrief2":"17-debrief-links-v8"},
"s5":{"miss1":"18-typed-repair-not-recognised-s5"},
"s7":{"debrief":"19-debrief-not-yet-s7"},
"s1":{"timeout":"20-preflight-time-up-s1"},
}
def rename_fix(): pass
with sync_playwright() as pw:
    b=pw.chromium.launch(executable_path="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome",args=["--no-sandbox"])
    ctx=b.new_context(viewport={"width":390,"height":844},device_scale_factor=2,is_mobile=True,has_touch=True,
        user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1")
    ctx.route("**/*",lambda r:(log["blocked"].append(r.request.url),r.abort()) if ("script.google" in r.request.url or not r.request.url.startswith("http://localhost")) else r.continue_())
    page=ctx.new_page(); setup(ctx,page)
    page.goto(URL); page.wait_for_timeout(1200)
    log["start"]=page.evaluate("()=>({view:typeof view!=='undefined'?view:null,user:typeof USER!=='undefined'?USER:null,sr:!!GS_SR,mic:gsMicStatus(),free:store.free,today:fdToday(),h:document.querySelector('#app').innerText.slice(0,300)})")
    print(log["start"],flush=True)
    lay(page,"home"); shot(page,"01-tab-home")
    page.evaluate("document.querySelector('details.vocab').open=true;document.querySelector('details.vocab').scrollIntoView({block:'start'})"); shot(page,"02-how-scramble-works")
    page.evaluate("document.querySelector('details.vocab').open=false;document.querySelector('.sc-deck').scrollIntoView({block:'start'})"); shot(page,"03-deck-view-unseen")
    order=list(P.keys())
    for i,cid in enumerate(order):
        m=i%3
        if i==0: page.evaluate("window.scrollTo(0,0)"); page.click("#scAny"); how="Scramble button"
        elif m==1 and page.query_selector("#scMore"): page.click("#scMore"); how="Draw another (debrief)"
        else:
            if page.query_selector("#scHome"): page.click("#scHome"); page.wait_for_timeout(200)
            if m==0: page.click("#scAny"); how="Scramble button"
            else:
                deck=page.evaluate("id=>scCard(id).deck",cid); page.click(f'[data-scdraw="{deck}"]'); how="Draw a card ("+deck+" deck)"
        page.wait_for_timeout(300)
        got=st(page)["id"]
        if got!=cid: ev("draw gave a different card than expected",expected=cid,got=got,how=how); cid=got
        play(page,cid,P[cid],dict(SH.get(cid,{})),how)
    page.click("#scHome"); page.wait_for_timeout(300)
    log["after_run"]={"sc":page.evaluate("()=>JSON.parse(JSON.stringify(gs.sc))"),"errs":page.evaluate("()=>gs.errs||{}"),"stats":page.inner_text(".cstats"),"review":page.inner_text(".fd-review"),"radar":(page.inner_text(".gs-radar") if page.query_selector(".gs-radar") else None),"tab":page.inner_text(".tab.sc-tab")}
    lay(page,"home_after")
    shot(page,"21-home-after-run")
    page.evaluate("document.querySelector('.sc-deck').scrollIntoView({block:'start'})"); shot(page,"22-deck-tiles-after-run")
    page.evaluate("document.querySelector('.gs-radar').scrollIntoView({block:'center'})"); shot(page,"23-objective-radar")
    # Scramble after everything seen (no due today): what does it draw?
    page.evaluate("window.scrollTo(0,0)"); picks=[]
    for _ in range(4):
        page.click("#scAny"); page.wait_for_timeout(200); s=st(page); picks.append([s["id"],page.evaluate("id=>gs.sc.c[id].s",s["id"])]); page.click("#scBack"); page.wait_for_timeout(200)
    log["scramble_after_all_seen"]=picks
    # retry o8 from its tile, leave test, then clear it
    page.click('[data-scgo="o8"]'); page.wait_for_timeout(300)
    log["second_look_label"]=page.inner_text(".sc-cardface .kick")
    page.click("#scGo"); page.wait_for_timeout(300)
    type_answer(page,"Excuse me Sir. Could you sign this form please?"); page.click("#scNext"); page.wait_for_timeout(300)
    page.once("dialog",lambda d:None)
    page.click("#scBack"); page.wait_for_timeout(300)   # dialog accepted by handler -> leaves
    log["leave_midcard"]={"scp_after":st(page),"o8_after_leave":page.evaluate("()=>gs.sc.c.o8"),"radar_k_request":page.evaluate("()=>gs.sc.k.request")}
    page.click('[data-scgo="o8"]'); page.wait_for_timeout(300)
    play(page,"o8",(None,["Excuse me Sir. Could you sign this form please?"],["Yes Sir. The bank close at three today. Thank you Sir."]),{},"tile ↺ Again (retry)")
    page.click("#scHome"); page.wait_for_timeout(300)
    # ---------- LESSON MODE ----------
    page.click("#scLive"); page.wait_for_timeout(300); lay(page,"lesson_home")
    shot(page,"24-lesson-mode-home")
    LM={"o3":[(["c","p"],2,"Negatives"),(["c"],2,"")],"v7":[(["c","p"],1,"Conditionals"),(["p"],2,"")],
        "v8":[(["c","m"],1,"Passive"),(["c"],2,"")],"s6":[(["c","c"],3,"Address & register"),(["c","c"],3,"")]}
    log["lesson"]={}
    for li,(cid,marks) in enumerate(LM.items()):
        page.click(f'[data-scgo="{cid}"]'); page.wait_for_timeout(300)
        L={"pre_text":page.inner_text(".sc-preside")[:300],"turns":[]}
        if li==0: shot(page,"25-lesson-preflight-o3")
        page.click("#scGo"); page.wait_for_timeout(300)
        for ti,(mk,flu,tag) in enumerate(marks):
            T={"save_disabled_before":page.evaluate("()=>document.querySelector('#scTSave').disabled"),"tag_options":page.evaluate("()=>[...document.querySelectorAll('#scTag option')].map(o=>o.textContent)")}
            if li==0 and ti==0:
                lay(page,"lesson_exchange"); shot(page,"26-lesson-exchange-top-o3")
                page.evaluate("document.querySelector('.fd-tbox').scrollIntoView({block:'center'})"); shot(page,"27-lesson-teacher-box-o3")
                T["tbox_buttons"]=page.evaluate("()=>[...document.querySelectorAll('.fd-tbox button')].map(b=>{const r=b.getBoundingClientRect();return (b.textContent.trim()||b.getAttribute('aria-label'))+' '+Math.round(r.width)+'x'+Math.round(r.height)})")
            if tag: page.select_option("#scTag",label=tag)
            for i,v in enumerate(mk): page.click(f'[data-sct="{i}:{v}"]'); page.wait_for_timeout(80)
            page.click(f'[data-scflu="{flu}"]'); page.wait_for_timeout(80)
            T["tag_kept_after_rerender"]=page.evaluate("()=>document.querySelector('#scTag').value")
            if li==1 and ti==0:
                page.click("#scHint"); page.wait_for_timeout(200); T["hint_text"]=page.inner_text(".gs-coach")[:200]
                page.evaluate("document.querySelector('.fd-tbox').scrollIntoView({block:'center'})"); shot(page,"28-lesson-marked-with-hint-v7")
            page.click("#scTSave"); page.wait_for_timeout(300)
            s=st(page); T["res"]=s["res"][ti]; T["passed_text"]=page.inner_text("#scSpeak")[:260]
            if li==0 and ti==0:
                page.evaluate("document.querySelector('#scSpeak').scrollIntoView({block:'start'})"); shot(page,"29-lesson-saved-o3")
            L["turns"].append(T); page.click("#scNext"); page.wait_for_timeout(300)
        L["debrief"]={"score":page.inner_text(".gs-resv"),"tier":page.inner_text(".gs-resh .kick"),"line":page.inner_text(".gs-resh small"),"note":(page.inner_text(".gs-resbox>.gs-c") if page.query_selector(".gs-resbox>.gs-c") else ""),"rec":page.evaluate("id=>gs.sc.c[id]",cid)}
        if li==1: shot(page,"30-lesson-debrief-v7")
        log["lesson"][cid]=L; page.click("#scHome"); page.wait_for_timeout(300)
    # desktop (Zoom share) look
    page.set_viewport_size({"width":1280,"height":720}); page.wait_for_timeout(300)
    page.click('[data-scgo="s8"]'); page.wait_for_timeout(300); page.screenshot(path=f"{OUT}/shots/31-lesson-zoom-1280-preflight.png")
    page.click("#scGo"); page.wait_for_timeout(700); page.screenshot(path=f"{OUT}/shots/32-lesson-zoom-1280-exchange.png")
    log["lesson"]["zoom_exchange_layout"]=page.evaluate("()=>{const t=document.querySelector('.fd-tbox').getBoundingClientRect(),s=document.querySelector('#scStage').getBoundingClientRect();return {tbox:[t.left,t.top,t.right,t.bottom].map(Math.round),stage:[s.left,s.top,s.right,s.bottom].map(Math.round),docH:document.scrollingElement.scrollHeight,npcFont:getComputedStyle(document.querySelector('.fd-ubub')).fontSize}}")
    page.click("#scBack"); page.wait_for_timeout(300)
    page.set_viewport_size({"width":390,"height":844}); page.wait_for_timeout(300)
    page.click("#scLive"); page.wait_for_timeout(300)
    log["after_lesson"]={"sc":page.evaluate("()=>JSON.parse(JSON.stringify(gs.sc))"),"errs":page.evaluate("()=>gs.errs||{}"),"stats":page.inner_text(".cstats"),"radar":page.inner_text(".gs-radar")}
    page.evaluate("document.querySelector('.gs-radar').scrollIntoView({block:'center'})"); shot(page,"33-radar-after-lesson-mode")
    page.close()
    # ---------- SPACED REVIEW: move the clock ----------
    def tpage(days):
        p=ctx.new_page(); setup(ctx,p)
        p.add_init_script("(()=>{const off=%d*86400000,_D=Date;class D2 extends _D{constructor(...a){if(a.length===0)super(_D.now()+off);else super(...a)}static now(){return _D.now()+off}};window.Date=D2})()"%days)
        p.goto(URL); p.wait_for_timeout(1000); return p
    log["spaced"]={}
    for days in (1,2,3):
        p=tpage(days)
        S={"today":p.evaluate("fdToday()"),"due":p.evaluate("()=>SC_CARDS.filter(scDue).map(c=>c.id+':'+gs.sc.c[c.id].s+':'+gs.sc.c[c.id].due)"),"stats":p.inner_text(".cstats"),"review":p.inner_text(".fd-review"),"tab":p.inner_text(".tab.sc-tab"),"due_badges":len(p.query_selector_all(".fd-due"))}
        if days in (1,3): shot(p,f"3{4 if days==1 else 6}-clock-plus{days}-home")
        p.click("#scAny"); p.wait_for_timeout(300); S["scramble_draws"]=st(p)["id"]; S["face_kick"]=p.inner_text(".sc-cardface .kick")
        if days==1: shot(p,"35-clock-plus1-due-card-drawn")
        p.click("#scBack"); p.wait_for_timeout(200)
        S["deck_draws"]={}
        for d in ("office","visitors","social"):
            p.click(f'[data-scdraw="{d}"]'); p.wait_for_timeout(200); S["deck_draws"][d]=st(p)["id"]; p.click("#scBack"); p.wait_for_timeout(200)
        S["scpick_x5"]=p.evaluate("()=>[1,2,3,4,5].map(()=>scPick(null).id)")
        log["spaced"][f"+{days}"]=S; p.close()
    p=tpage(1)
    p.click("#scAny"); p.wait_for_timeout(300); cid=st(p)["id"]
    play(p,cid,(None,["I would go to Japan with my family."],["You should visit Chiang Mai."]),{}, "Scramble button, clock +1 day (due card)")
    p.click("#scHome"); p.wait_for_timeout(300)
    log["spaced"]["+1_after_replay"]={"card":cid,"rec":p.evaluate("id=>gs.sc.c[id]",cid),"stats":p.inner_text(".cstats"),"review":p.inner_text(".fd-review"),"next_scramble":p.evaluate("()=>scPick(null).id")}
    shot(p,"37-clock-plus1-after-replay-home")
    log["final_sc"]=p.evaluate("()=>JSON.parse(JSON.stringify(gs.sc))")
    p.close(); b.close()
json.dump(log,open(OUT+"/raw.json","w"),ensure_ascii=False,indent=1)
print("DONE")
