import asyncio, sys, json
from playwright.async_api import async_playwright
URL=sys.argv[1]
async def main():
    async with async_playwright() as p:
        import glob
        b=await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        ctx=await b.new_context(viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True)
        await ctx.route('**/script.google.com/**', lambda r: r.abort())
        pg=await ctx.new_page(); errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.add_init_script("window.speechSynthesis && (speechSynthesis.speak=()=>{});")
        await pg.goto(URL+'?tab=sc'); await pg.wait_for_timeout(800)
        r={}
        r['free']=await pg.evaluate('store.free')
        r['open']=await pg.evaluate('SC_CARDS.filter(scOpen).length')
        r['eval']=await pg.evaluate('''[["o2",0,"3"],["v2",1,"4729"],["o1",0,"Again please"],["o1",0,"ไม่เข้าใจค่ะ"],["o1",0,"Sorry, I not understand."],["o1",0,"Sorry?"]].map(([c,i,t])=>[t,scEval(SC_CARDS.find(x=>x.id==c).turns[i],t).status])''')
        r['models']=await pg.evaluate('''SC_CARDS.flatMap(c=>c.turns.map((t,i)=>{const e=scEval(t,t.model);return e.hits.every(Boolean)&&e.status=="ok"?null:c.id+"-"+(i+1)})).filter(Boolean)''')
        # play o1 by typing: draw specific card
        await pg.evaluate("scBrief(scCard('o2'))"); await pg.wait_for_timeout(400)
        await pg.click('text=I\'M READY'); await pg.wait_for_timeout(500)
        await pg.click('#scType'); await pg.fill('#scTypeIn','hmm'); await pg.click('#scTypeOk'); await pg.wait_for_timeout(300)
        r['sticky_after_short']=await pg.evaluate('!!document.getElementById("scTypeIn")')
        await pg.fill('#scTypeIn','ok'); await pg.click('#scTypeOk'); await pg.wait_for_timeout(300)
        r['moveon_after_2_shorts']=await pg.evaluate('!!document.getElementById("scSkip")')
        await pg.fill('#scTypeIn','There are lots of things.'); await pg.click('#scTypeOk'); await pg.wait_for_timeout(300)
        r['free_hint_after_miss']=await pg.evaluate('SCP.lad')
        await pg.fill('#scTypeIn','3'); await pg.click('#scTypeOk'); await pg.wait_for_timeout(300)
        r['sub_after_pass']=await pg.evaluate('SCP.sub')
        await pg.screenshot(path='/home/claude/test/s1.png')
        await pg.click('#scNext'); await pg.wait_for_timeout(400)
        r['sticky_next_turn']=await pg.evaluate('SCP.sub')
        r['errs']=errs
        # other tabs render
        for t in ['gs','fd','fin','intl','sc']:
            await pg.goto(URL+'?tab='+t); await pg.wait_for_timeout(500)
            r['tab_'+t]=await pg.evaluate('document.querySelectorAll(".tab.on").length')
        r['overflow']=await pg.evaluate('document.documentElement.scrollWidth>innerWidth')
        r['errs2']=errs
        print(json.dumps(r,ensure_ascii=False,indent=0))
        await b.close()
asyncio.run(main())
