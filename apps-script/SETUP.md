# Ground School — switching on login + Google Sheets saving

The app works without this (progress stays on the device). These steps take about 5 minutes and add sign-in, online saving across devices, and a log of every spoken attempt.

## 1. Make the Sheet and the script
1. Create a new Google Sheet, for example **Modulation Desk — Progress**.
2. **Extensions → Apps Script**. Delete the sample code and paste all of `Code.gs` from this folder. Save.
3. **Deploy → New deployment →** ⚙️ **Web app**
   - Execute as: **Me**
   - Who has access: **Anyone**
   - **Deploy**, then approve the permissions (Advanced → Go to project).
4. Copy the **Web app URL** (it ends in `/exec`).

## 2. Connect the app (choose one)
- **Permanent (recommended):** in `index.html`, find `const GS_SHEET_URL = "";` and paste the URL between the quotes. Commit, and it goes live on GitHub Pages.
- **Quick link:** send the student this link once. Her browser remembers it:
  `https://pegasus028.github.io/ThoughtModulation2/?api=PASTE_EXEC_URL_HERE&tab=gs`

## 3. First sign-in
On her first visit she sees **Sign in**. She types her first name and a 4-digit PIN, and that creates her account. Next time she uses the same name and PIN, on any device.

## What you get in the Sheet
| Tab | Contents |
|---|---|
| **Users** | Name, PIN hash (never the PIN itself), created, last seen |
| **Progress** | One row per student. **Summary** reads like `g1:92/80/- …` = Script / Gaps / Own-words best % per mission |
| **Log** | Every committed answer: mission, exchange, mode, **what she said**, result (pass / grammar / missing / unclear), the hint note, tries, and whether it was typed |

The Log tab is the useful one before a lesson. Filter by **Result = grammar** to see exactly which forms she struggled with.

**Forgotten PIN:** clear her cell in **Users → PIN hash**. Her next sign-in sets a new PIN and keeps her progress.

**After editing Code.gs:** Deploy → Manage deployments → ✏️ → Version: **New version** → Deploy. Saving alone does not update the live URL.

## iPhone checklist for the student
- Open the app in **Safari**. Chrome on iPhone has no speech input.
- On the first mic tap, allow the microphone. If it's blocked: **aA → Website Settings → Microphone → Allow**.
- If it still fails, check **Settings → Privacy & Security → Speech Recognition** (Safari on), and that Siri or Dictation is on.
- For better voices: **Settings → Accessibility → Spoken Content → Voices → English**, then download an **Enhanced** voice (Serena / Daniel for British, Ava / Evan for American).
- Use earphones. The voices are clearer and the mic hears only her.
- Don't run the app on the same phone as a live video call. The call app holds the microphone, so join the lesson on a laptop or tablet instead.
