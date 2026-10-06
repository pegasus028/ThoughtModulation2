/**
 * Modulation Desk — login + progress backend (Google Apps Script, bound to a Google Sheet)
 *
 * Sheets (created automatically on first use):
 *   Users     — one row per student: name key, display name, PIN hash, created, last seen
 *   Progress  — one row per student: whole-app progress as JSON + a readable summary
 *   Log       — one row per spoken attempt: what she said, result, hint note, tries
 *
 * Deploy: Deploy → New deployment → type "Web app" → Execute as: Me → Who has access: Anyone → Deploy.
 * After ANY change to this file: Deploy → Manage deployments → ✏️ → Version: New version → Deploy
 * (saving alone does not update the live /exec URL).
 *
 * Forgotten PIN: in the Users sheet, clear that student's "PIN hash" cell. Her next sign-in
 * with the same name sets the new PIN, and her progress is kept.
 */
const SH_USERS = 'Users', SH_PROGRESS = 'Progress', SH_LOG = 'Log';

function doGet() {
  return json_({ ok: true, app: 'Modulation Desk', time: new Date().toISOString() });
}

function doPost(e) {
  const lock = LockService.getScriptLock();
  try { lock.waitLock(20000); } catch (err) { return json_({ ok: false, error: 'Server busy — try again.' }); }
  try {
    const req = JSON.parse((e && e.postData && e.postData.contents) || '{}');
    const name = String(req.name || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    const key = name.toLowerCase();
    const h = String(req.h || '');
    if (!key) return json_({ ok: false, error: 'Please type your name.' });
    if (!/^[a-f0-9]{16,64}$/.test(h)) return json_({ ok: false, error: 'Invalid PIN.' });

    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const users = sheet_(ss, SH_USERS, ['Name key', 'Name', 'PIN hash', 'Created', 'Last seen']);
    const row = findRow_(users, key);
    const now = new Date();

    if (req.action === 'login') {
      if (!row) {
        users.appendRow([key, name, h, now, now]);
        return json_({ ok: true, created: true, name: name, data: null });
      }
      const stored = String(users.getRange(row, 3).getValue() || '');
      if (!stored) users.getRange(row, 3).setValue(h);               // teacher cleared the PIN → set a new one
      else if (stored !== h) return json_({ ok: false, error: 'That PIN does not match this name.' });
      users.getRange(row, 5).setValue(now);
      return json_({ ok: true, created: false, name: String(users.getRange(row, 2).getValue() || name), data: readProgress_(ss, key) });
    }

    if (!row || String(users.getRange(row, 3).getValue()) !== h) return json_({ ok: false, error: 'Not signed in.' });

    if (req.action === 'save') {
      const prog = sheet_(ss, SH_PROGRESS, ['Name key', 'Name', 'Updated', 'Summary', 'Desk JSON', 'Ground School JSON', 'Updated (ms)']);
      const desk = JSON.stringify(req.desk || {}), gs = JSON.stringify(req.gs || {});
      if (desk.length > 49000 || gs.length > 49000) return json_({ ok: false, error: 'Progress too large to save.' });
      const vals = [key, name, now, String(req.summary || '').slice(0, 1000), desk, gs, Number(req.t) || now.getTime()];
      const pr = findRow_(prog, key);
      if (pr) prog.getRange(pr, 1, 1, vals.length).setValues([vals]); else prog.appendRow(vals);
      const logs = Array.isArray(req.logs) ? req.logs.slice(0, 60) : [];
      if (logs.length) {
        const log = sheet_(ss, SH_LOG, ['Time', 'Name', 'Mission', 'Exchange', 'Mode', 'What she said', 'Result', 'Note', 'Tries', 'Typed?']);
        const rows = logs.map(function (r) {
          return [now, name, String(r.m || ''), String(r.t || ''), String(r.mode || ''), String(r.said || '').slice(0, 500),
                  String(r.res || ''), String(r.note || '').slice(0, 300), r.tries === '' ? '' : Number(r.tries) || '', r.typed ? 'typed' : ''];
        });
        log.getRange(log.getLastRow() + 1, 1, rows.length, rows[0].length).setValues(rows);
      }
      users.getRange(row, 5).setValue(now);
      return json_({ ok: true });
    }
    return json_({ ok: false, error: 'Unknown action.' });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

function readProgress_(ss, key) {
  const prog = ss.getSheetByName(SH_PROGRESS);
  if (!prog) return null;
  const r = findRow_(prog, key);
  if (!r) return null;
  const v = prog.getRange(r, 1, 1, 7).getValues()[0];
  const parse = function (s) { try { return JSON.parse(s || '{}'); } catch (e) { return {}; } };
  return { desk: parse(v[4]), gs: parse(v[5]), t: Number(v[6]) || 0 };
}

function sheet_(ss, name, header) {
  let sh = ss.getSheetByName(name);
  if (!sh) {
    sh = ss.insertSheet(name);
    sh.getRange(1, 1, 1, header.length).setValues([header]).setFontWeight('bold');
    sh.setFrozenRows(1);
  }
  return sh;
}

function findRow_(sh, key) {
  const n = sh.getLastRow();
  if (n < 2) return 0;
  const keys = sh.getRange(2, 1, n - 1, 1).getValues();
  for (let i = 0; i < keys.length; i++) if (String(keys[i][0]) === key) return i + 2;
  return 0;
}

function json_(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
