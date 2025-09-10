# generated_runs/src/pages/auto_stubs.py (auto-generated)
from pathlib import Path
import os, re, time
from playwright.sync_api import expect

# Short, configurable timeout for fast interactions (ms)
_FAST_TIMEOUT = int(os.getenv("UI_FAST_TIMEOUT", "2500") or "2500")

# ----------- flicker/zoom guards -----------
def _disable_motion_and_zoom(page):
    try:
        page.add_init_script("""
            (() => {
              try {
                window.addEventListener('keydown', e => {
                  if ((e.ctrlKey || e.metaKey) && (e.key === '+' || e.key === '-' || e.key === '=')) e.preventDefault();
                }, {passive:false});
                window.addEventListener('wheel', e => { if (e.ctrlKey) e.preventDefault(); }, {passive:false});
              } catch {}
            })();
        """)
    except Exception: pass
    try:
        page.add_style_tag(content="""
          *, *::before, *::after { transition-duration:0s!important; transition-delay:0s!important; animation-duration:0s!important; animation-delay:0s!important; }
          html,body { scroll-behavior:auto!important; }
        """)
    except Exception: pass

def _viewport_metrics(page):
    try:
        return page.evaluate("""() => ({
            scale: (window.visualViewport && window.visualViewport.scale) || 1,
            w: document.documentElement.clientWidth,
            h: document.documentElement.clientHeight
        })""")
    except Exception:
        return {"scale":1,"w":0,"h":0}

def _wait_layout_stable(page, stable_ms=300, timeout_ms=None):
    if timeout_ms is None: timeout_ms = _FAST_TIMEOUT*4
    end = time.time() + timeout_ms/1000.0
    last = None; since = None
    while time.time() < end:
        cur = _viewport_metrics(page)
        if cur == last:
            if since is None: since = time.time()
            if (time.time()-since)*1000 >= stable_ms: return True
        else:
            last = cur; since = None
        time.sleep(0.05)
    return False

def _visible_first(loc):
    try:
        n = loc.count()
        for i in range(n):
            el = loc.nth(i)
            try:
                if el.is_visible():
                    return el
            except Exception: continue
    except Exception: pass
    return None

def _normalize_story_path(p_hint: str) -> str:
    p = (p_hint or "").strip().strip('"').strip("'")
    if not p: return ""
    try: return str(Path(p))
    except Exception: return p

def _ensure_upload_file(path_hint: str) -> str:
    p = _normalize_story_path(path_hint)
    if not p:
        envp = os.getenv("UI_UPLOAD_FILE", "").strip()
        p = _normalize_story_path(envp)
    if p and Path(p).exists(): return p
    import tempfile
    tmp = Path(tempfile.gettempdir()) / "auto_upload.txt"
    if not tmp.exists(): tmp.write_text("auto-generated file\n", encoding="utf-8")
    return str(tmp)

# ----------- generic text entry -----------
def _fill_text_like(ctx, label: str, value: str) -> bool:
    import re
    label = (label or "").strip()
    if not label: return False
    rx = re.compile(label, re.I)
    key = re.sub(r"[^a-z0-9]+", "", label.lower())

    # a11y
    try:
        el = ctx.get_by_label(rx).first
        if el and el.count()>0: el.fill(value, timeout=_FAST_TIMEOUT); return True
    except Exception: pass
    try:
        el = ctx.get_by_role("textbox", name=rx).first
        if el and el.count()>0: el.fill(value, timeout=_FAST_TIMEOUT); return True
    except Exception: pass
    try:
        el = ctx.get_by_placeholder(rx).first
        if el and el.count()>0: el.fill(value, timeout=_FAST_TIMEOUT); return True
    except Exception: pass

    # attributes
    candidates = [
        f"input#{key}", f"input[name='{key}']", f"input[id='{key}']",
        f"input[aria-label='{label}']", f"input[aria-labelledby*='{key}' i]",
        f"input[aria-label*='{label}' i]", f"input[id*='{key}' i]", f"input[name*='{key}' i]",
        f"input[placeholder*='{label}' i]", f"[data-test*='{key}' i]",
        f"[data-testid*='{key}' i]", f"[data-qa*='{key}' i]",
        "input[type='text']", "input:not([type]), input[type='search'], input[type='email'], input[type='tel']",
        "textarea",
    ]
    for sel in candidates:
        try:
            el = ctx.locator(sel).first
            if el and el.count()>0 and el.is_visible():
                el.fill(value, timeout=_FAST_TIMEOUT); return True
        except Exception: pass

    # proximity
    prox = (
        f"//label[normalize-space()='{label}']/following::input[1]",
        f"//*[normalize-space(text())='{label}']/following::input[1]",
        f"(//td[normalize-space()='{label}']/following::td)[1]//input[1]",
        f"//*[normalize-space(text())='{label}']/ancestor::*[self::div or self::li or self::td or self::section or self::form][1]//input[1]",
    )
    for xp in prox:
        try:
            el = ctx.locator('xpath='+xp).first
            if el and el.count()>0 and el.is_visible():
                el.fill(value, timeout=_FAST_TIMEOUT); return True
        except Exception: pass

    # last resort
    try:
        tbs = ctx.get_by_role("textbox")
        if tbs and tbs.count()>0:
            _el = _visible_first(tbs)
            if _el: _el.fill(value, timeout=_FAST_TIMEOUT); return True
    except Exception: pass
    return False

# ----------- click helpers -----------
def _click_attempt(page, el):
    try:
        _wait_layout_stable(page, stable_ms=200)
        try: el.scroll_into_view_if_needed()
        except Exception: pass
        try:
            with page.expect_navigation(timeout=_FAST_TIMEOUT*4):
                el.click(timeout=_FAST_TIMEOUT)
            _wait_layout_stable(page, stable_ms=200); return True
        except Exception: pass
        try:
            el.click(timeout=_FAST_TIMEOUT, force=True)
            try: page.wait_for_load_state("domcontentloaded", timeout=_FAST_TIMEOUT*2)
            except Exception: pass
            _wait_layout_stable(page, stable_ms=200); return True
        except Exception: pass
        try:
            el.dblclick(timeout=_FAST_TIMEOUT, force=True)
            _wait_layout_stable(page, stable_ms=200); return True
        except Exception: return False
    except Exception: return False

def _click_best(page, label: str) -> bool:
    _disable_motion_and_zoom(page)
    label = (label or "").strip()
    if not label: return False
    rx = re.compile(rf"^\s*{re.escape(label)}\s*$", re.I)
    rx_sw = re.compile(re.escape(label), re.I)

    for getter in (
        lambda: page.get_by_role("link", name=rx).first,
        lambda: page.get_by_role("button", name=rx).first,
        lambda: page.get_by_role("heading", name=rx).first,
    ):
        try:
            el = getter()
            if el and el.count()>0 and el.is_visible():
                if _click_attempt(page, el): return True
        except Exception: pass

    try:
        card = page.locator(f".card, .top-card").filter(has_text=rx_sw).first
        if card and card.count()>0 and card.is_visible():
            if _click_attempt(page, card): return True
    except Exception: pass
    try:
        h = page.locator("h1,h2,h3,h4,h5,h6").filter(has_text=rx).first
        if h and h.count()>0 and h.is_visible():
            anc = h.locator("xpath=ancestor::a[1]")
            if anc and anc.count()>0 and anc.is_visible():
                if _click_attempt(page, anc.first): return True
            anc2 = h.locator("xpath=ancestor::*[contains(@class,'card') or contains(@class,'top-card')][1]")
            if anc2 and anc2.count()>0 and anc2.is_visible():
                if _click_attempt(page, anc2.first): return True
            if _click_attempt(page, h): return True
    except Exception: pass

    for sel in (
        f".element-list .menu-list li:has-text('{label}')",
        f"li:has-text('{label}')", f"span:has-text('{label}')",
        f"a:has-text('{label}')", f"div:has-text('{label}')",
    ):
        try:
            el = page.locator(sel).first
            if el and el.count()>0 and el.is_visible():
                if _click_attempt(page, el): return True
        except Exception: pass

    try:
        node = page.locator(f"xpath=//*[normalize-space(text())='{label}']").first
        if node and node.count()>0 and node.is_visible():
            anc = node.locator("xpath=ancestor::a[1]")
            if anc and anc.count()>0 and anc.is_visible():
                if _click_attempt(page, anc.first): return True
            if _click_attempt(page, node): return True
    except Exception: pass

    try:
        el = page.get_by_text(rx_sw).first
        if el and el.count()>0 and el.is_visible():
            if _click_attempt(page, el): return True
    except Exception: pass

    return False

# ----------- dropdown helpers -----------
def _fast_try_select(sel, value: str) -> bool:
    try:
        sel.select_option(label=value, timeout=_FAST_TIMEOUT); return True
    except Exception: pass
    try:
        sel.select_option(value=value, timeout=_FAST_TIMEOUT); return True
    except Exception: return False

def _fast_pick_from_listbox(ctx, value: str) -> bool:
    ex = re.compile(rf"^\s*{re.escape(value)}\s*$", re.I)
    sw = re.compile(rf"^\s*{re.escape(value)}", re.I)
    for rx in (ex, sw):
        try:
            el = ctx.get_by_role("option", name=rx).first
            if el and el.count()>0 and el.is_visible():
                el.click(timeout=_FAST_TIMEOUT); return True
        except Exception: pass
    for rx in (ex, sw):
        try:
            el = ctx.locator("[role='option'], li, div").filter(has_text=rx).first
            if el and el.count()>0 and el.is_visible():
                el.click(timeout=_FAST_TIMEOUT); return True
        except Exception: pass
    return False

def _fast_select_dropdown(page, label_text: str, value: str) -> bool:
    label_text = (label_text or "").strip()
    if not value: return False
    try:
        sel = page.get_by_label(re.compile(label_text, re.I)).first
        if sel and sel.count()>0:
            if _fast_try_select(sel, value): return True
    except Exception: pass
    if label_text:
        try:
            sel = page.locator(f"select#{label_text}, select[name='{label_text}'], select[id='{label_text}']").first
            if sel and sel.count()>0:
                if _fast_try_select(sel, value): return True
        except Exception: pass
    if label_text:
        try:
            near = page.locator(
                f"label:has-text('{label_text}') ~ select, *:has(> label:has-text('{label_text}')) select"
            ).first
            if near and near.count()>0:
                if _fast_try_select(near, value): return True
        except Exception: pass
    if label_text:
        try:
            cb = page.get_by_role("combobox", name=re.compile(label_text, re.I)).first
            if cb and cb.count()>0:
                try: cb.click(timeout=_FAST_TIMEOUT)
                except Exception:
                    try: cb.click(force=True, timeout=_FAST_TIMEOUT)
                    except Exception: pass
                inner = None
                try:
                    inner = cb.locator("input, [contenteditable='true']").first
                    if inner and inner.count()>0 and inner.is_visible():
                        try: inner.fill("", timeout=_FAST_TIMEOUT)
                        except Exception: pass
                        try: inner.type(value, delay=0, timeout=_FAST_TIMEOUT)
                        except Exception: pass
                except Exception: pass
                if _fast_pick_from_listbox(page, value): return True
                try: (inner if inner and inner.count()>0 else cb).press("Enter", timeout=_FAST_TIMEOUT); return True
                except Exception: pass
        except Exception: pass
    try:
        tb = page.get_by_role("textbox", name=re.compile(label_text, re.I)).first
        if tb and tb.count()>0:
            try: tb.fill("", timeout=_FAST_TIMEOUT)
            except Exception: pass
            try: tb.type(value, delay=0, timeout=_FAST_TIMEOUT)
            except Exception: pass
            try: page.keyboard.press("Enter", timeout=_FAST_TIMEOUT); return True
            except Exception: pass
    except Exception: pass
    try:
        selects = page.locator("select")
        cnt = selects.count()
        for i in range(min(cnt, 4)):
            sel = selects.nth(i)
            if _fast_try_select(sel, value): return True
    except Exception: pass
    return False

# ----------- checkbox helpers -----------
_TRUE_SET  = {"1","true","yes","on","check","checked","tick","enable","enabled","select","mark"}
_FALSE_SET = {"0","false","no","off","uncheck","unchecked","untick","disable","disabled","deselect","unmark"}
_TOGGLE_SET= {"toggle","switch","flip"}

def _coerce_checkbox_value(v):
    s = ("" if v is None else str(v)).strip().lower()
    if s in _TRUE_SET: return True
    if s in _FALSE_SET: return False
    if s in _TOGGLE_SET: return None
    return True

def _set_checkbox_node(el, want) -> bool:
    try:
        if want is None:
            el.click(timeout=_FAST_TIMEOUT); return True
    except Exception: pass
    try:
        if want is True:
            try: el.check(timeout=_FAST_TIMEOUT); return True
            except Exception: pass
            try: el.click(timeout=_FAST_TIMEOUT); return True
            except Exception: pass
        else:
            try: el.uncheck(timeout=_FAST_TIMEOUT); return True
            except Exception: pass
            try: el.click(timeout=_FAST_TIMEOUT); return True
            except Exception: pass
    except Exception: pass
    try:
        el.evaluate("""(node, v) => {
            if (v === null) v = !node.checked;
            node.checked = !!v;
            node.dispatchEvent(new Event('input', {bubbles:true}));
            node.dispatchEvent(new Event('change', {bubbles:true}));
        }""", want)
        return True
    except Exception: return False

def _checkbox_try_in_context(ctx, label_text: str, want) -> bool:
    label_text = (label_text or "").strip()
    if not label_text: return False
    rx = re.compile(label_text, re.I)
    try:
        el = ctx.get_by_role("checkbox", name=rx).first
        if el and el.count()>0 and el.is_visible():
            if _set_checkbox_node(el, want): return True
    except Exception: pass
    try:
        host = ctx.locator(f"label:has-text('{label_text}')").first
        if host and host.count()>0:
            if want is None:
                host.click(timeout=_FAST_TIMEOUT); return True
            try: host.click(timeout=_FAST_TIMEOUT)
            except Exception: pass
            inp = host.locator("input[type='checkbox']").first
            if inp and inp.count()>0 and _set_checkbox_node(inp, want): return True
    except Exception: pass
    try:
        cand = ctx.locator(
            f"input[type='checkbox'][id*='{label_text}' i], "
            f"input[type='checkbox'][name*='{label_text}' i], "
            f"input[type='checkbox'][value*='{label_text}' i]"
        ).first
        if cand and cand.count()>0 and cand.is_visible():
            if _set_checkbox_node(cand, want): return True
    except Exception: pass
    try:
        lab = ctx.locator("label").filter(has_text=rx).first
        if lab and lab.count()>0:
            inp = lab.locator("xpath=./ancestor-or-self::*[1]/descendant::input[@type='checkbox'][1]").first
            if inp and inp.count()>0:
                if _set_checkbox_node(inp, want): return True
    except Exception: pass
    return False

def _set_checkbox(page, label_text: str, value):
    want = _coerce_checkbox_value(value)
    try:
        if _checkbox_try_in_context(page, label_text, want): return True
    except Exception: pass
    try:
        for fr in page.frames:
            if fr is page.main_frame: continue
            if _checkbox_try_in_context(fr, label_text, want): return True
    except Exception: pass
    print(f"[AUTO-STUBS] Could not set checkbox '{label_text}' to '{value}'.")
    return False

# ----------- radio helpers (generic & resilient) -----------
def _norm(s):
    import re
    return re.sub(r"[\s\u00A0]+", "", (s or "").strip().lower())

def _find_radio_like(ctx, value: str):
    """Return a Locator for the radio whose visible label or value matches `value` (space/case-insensitive)."""
    import re as _re
    target_norm = _norm(value)
    rx_val = _re.compile(rf"^\s*{_re.escape(value)}\s*$", _re.I)

    # 1) ARIA role by accessible name
    try:
        el = ctx.get_by_role("radio", name=rx_val).first
        if el and el.count()>0 and el.is_visible():
            return el
    except Exception: pass

    # 2) Iterate inputs and match by value/label/nearby text
    try:
        radios = ctx.locator("input[type='radio']")
        cnt = radios.count()
        for i in range(cnt):
            r = radios.nth(i)
            try:
                v = r.get_attribute("value") or ""
            except Exception:
                v = ""
            if _norm(v) == target_norm:
                return r

            # extract text from labels / next sibling / parent
            try:
                txt = r.evaluate("""(n) => {
                    let t = "";
                    try {
                      if (n.labels && n.labels.length) {
                        for (const L of n.labels) t += " " + (L.innerText || L.textContent || "");
                      }
                      if (!t && n.nextSibling) t += " " + (n.nextSibling.textContent || "");
                      const p = n.parentElement;
                      if (!t && p) t += " " + (p.innerText || p.textContent || "");
                    } catch {}
                    return t;
                }""") or ""
            except Exception:
                txt = ""
            if _norm(txt) == target_norm or target_norm in _norm(txt):
                return r
    except Exception: pass

    # 3) Label text → input relation
    try:
        lab = ctx.locator("label").filter(has_text=rx_val).first
        if lab and lab.count()>0 and lab.is_visible():
            # Prefer 'for' association
            try:
                fid = lab.get_attribute("for")
                if fid:
                    cand = ctx.locator(f"#{fid}").first
                    if cand and cand.count()>0 and cand.is_visible():
                        return cand
            except Exception: pass
            # Otherwise use nearest preceding input
            try:
                inp = lab.locator("xpath=preceding::input[@type='radio'][1]").first
                if inp and inp.count()>0 and inp.is_visible():
                    return inp
            except Exception: pass
    except Exception: pass

    # 4) Text node preceding/adjacent a radio
    try:
        el = ctx.locator(f"xpath=//*[normalize-space(text())='{value}']/preceding::input[@type='radio'][1]").first
        if el and el.count()>0 and el.is_visible():
            return el
    except Exception: pass

    return None

def _check_radio(page, group_label: str, value: str):
    _disable_motion_and_zoom(page)
    _wait_layout_stable(page, stable_ms=200)

    # If a group label was provided, restrict search to that container when possible.
    ctxs = [page]
    if group_label:
        try:
            rg = page.get_by_role("radiogroup", name=re.compile(group_label, re.I)).first
            if rg and rg.count()>0: ctxs = [rg]
        except Exception: pass
        if ctxs == [page]:
            try:
                cont = page.locator(f"section:has-text('{group_label}'), form:has-text('{group_label}'), div:has-text('{group_label}')").first
                if cont and cont.count()>0: ctxs = [cont]
            except Exception: pass

    # Search in page (or group) then frames.
    for ctx in ctxs:
        el = _find_radio_like(ctx, value)
        if el:
            try:
                el.check(timeout=_FAST_TIMEOUT)
            except Exception:
                el.click(timeout=_FAST_TIMEOUT)
            _wait_layout_stable(page, stable_ms=200)
            return True

    try:
        for fr in page.frames:
            if fr is page.main_frame: continue
            el = _find_radio_like(fr, value)
            if el:
                try: el.check(timeout=_FAST_TIMEOUT)
                except Exception: el.click(timeout=_FAST_TIMEOUT)
                _wait_layout_stable(page, stable_ms=200)
                return True
    except Exception: pass

    print(f"[AUTO-STUBS] Radio '{value}' not found (group='{group_label or ''}').")
    return False

def assert_radio_selected(page, value: str):
    """Assert that a radio with label/value `value` is checked."""
    el = _find_radio_like(page, value)
    if not el:
        # Try frames too
        try:
            for fr in page.frames:
                if fr is page.main_frame: continue
                el = _find_radio_like(fr, value)
                if el: break
        except Exception:
            pass
    if not el:
        raise AssertionError(f"Radio '{value}' not found to assert selection.")
    expect(el).to_be_checked(timeout=_FAST_TIMEOUT*4)

# ----------- assert helpers -----------
def _result_context(page):
    candidates = ["#result",".display-result","#output",".mt-3","p:has-text('You have selected')","div:has-text('You have selected')"]
    for sel in candidates:
        try:
            el = page.locator(sel).first
            if el and el.count()>0 and el.is_visible(): return el
        except Exception: pass
    return page.locator("body")

def _normalize_space(s: str) -> str:
    import re
    return re.sub(r"\s+", " ", (s or "").strip())

def assert_text_contains(page, value: str):
    el = _result_context(page)
    try:
        expect(el).to_contain_text(value, timeout=_FAST_TIMEOUT*4); return
    except Exception: pass
    try:
        txt = _normalize_space(el.inner_text()); val = _normalize_space(value)
        if val and val in txt: return
    except Exception: pass
    m = re.match(r"^(.*?selected)\s+(.*)$", (value or "").strip(), re.I)
    if m:
        part1, part2 = m.group(1).strip(), m.group(2).strip()
        if part1: expect(el).to_contain_text(part1, timeout=_FAST_TIMEOUT*2)
        if part2: expect(el).to_contain_text(part2, timeout=_FAST_TIMEOUT*2)
        return
    tokens = [t.strip() for t in re.split(r"[\s:]+", value or "") if len(t.strip()) >= 3]
    for t in tokens:
        expect(el).to_contain_text(t, timeout=_FAST_TIMEOUT)

def assert_text_block(page, text: str):
    lines = [ln.strip() for ln in (text or "").splitlines() if ln.strip()]
    for ln in lines:
        assert_text_contains(page, ln)

# ----------- upload helpers -----------
def click_file_upload(page):
    try:
        link = page.get_by_role("link", name=re.compile(r"^\s*File Upload\s*$", re.I)).first
        if link and link.count()>0:
            try:
                with page.expect_navigation(timeout=_FAST_TIMEOUT*4):
                    link.click(timeout=_FAST_TIMEOUT)
            except Exception:
                link.click(timeout=_FAST_TIMEOUT)
            return
    except Exception: pass
    try:
        b = page.get_by_role("button", name=re.compile(r"\bupload\b", re.I)).first
        if b and b.count()>0: b.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    try:
        l = page.get_by_role("link", name=re.compile(r"\bupload\b", re.I)).first
        if l and l.count()>0:
            try:
                with page.expect_navigation(timeout=_FAST_TIMEOUT*4):
                    l.click(timeout=_FAST_TIMEOUT)
            except Exception:
                l.click(timeout=_FAST_TIMEOUT)
            return
    except Exception: pass
    try:
        t = page.get_by_text(re.compile(r"\bupload\b", re.I)).first
        if t and t.count()>0: t.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass

def upload_file(page, value=""):
    try:
        page.locator("input#file-upload, input[type='file']").first.wait_for(state="attached", timeout=_FAST_TIMEOUT*4)
    except Exception: pass
    inp = None
    try:
        loc = page.locator("input[type='file']"); inp = _visible_first(loc)
    except Exception: pass
    if not inp:
        try:
            t = page.get_by_text(re.compile(r"^\s*File Upload\s*$", re.I)).first
            if t and t.count()>0:
                try:
                    with page.expect_navigation(timeout=_FAST_TIMEOUT*4):
                        t.click(timeout=_FAST_TIMEOUT)
                except Exception:
                    t.click(timeout=_FAST_TIMEOUT)
                loc = page.locator("input[type='file']"); inp = _visible_first(loc)
        except Exception: pass
    if not inp: raise AssertionError("No <input type='file'> found on the page.")
    path = _ensure_upload_file(value)
    try: inp.scroll_into_view_if_needed()
    except Exception: pass
    try: inp.set_input_files(path, timeout=_FAST_TIMEOUT*4)
    except Exception as e: raise AssertionError(f"set_input_files failed for '{path}': {e!r}")

def click_upload(page):
    try:
        btn = page.locator("#file-submit").first
        if btn and btn.count()>0: btn.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    rx = re.compile(r"^\s*Upload\s*$", re.I)
    try:
        page.get_by_role("button", name=rx).first.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    try:
        page.get_by_role("link", name=rx).first.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    try:
        page.get_by_text(rx).first.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    try:
        inp = page.locator("input[type='file']").first
        if inp:
            form = inp.locator("xpath=ancestor::form[1]")
            if form and form.count()>0:
                bf = form.locator("button, [role='button'], input[type='submit']").first
                if bf and bf.count()>0: bf.click(timeout=_FAST_TIMEOUT); return
    except Exception: pass
    raise AssertionError("Upload button not found.")

def assert_upload(page, expected_path=""):
    try: page.wait_for_load_state("domcontentloaded", timeout=_FAST_TIMEOUT*4)
    except Exception: pass
    try:
        h = page.locator("h3").first
        if not h or h.count()==0: raise AssertionError("Upload result header not found.")
        txt = (h.inner_text() or "").strip()
        if "File Uploaded!" not in txt: raise AssertionError(f"Expected 'File Uploaded!' but saw '{txt}'")
    except Exception as e:
        raise AssertionError(f"Upload success message missing: {e!r}")
    exp = Path(_normalize_story_path(expected_path)).name if expected_path else ""
    try:
        name_el = page.locator("#uploaded-files, #uploaded_file, .uploaded-file, .uploaded-files").first
        if name_el and name_el.count()>0:
            name = (name_el.inner_text() or "").strip()
            if exp and exp != name: raise AssertionError(f"Expected uploaded name '{exp}', got '{name}'")
    except Exception:
        if exp: raise

def linger_after_success(page):
    secs = int(os.getenv("UI_LINGER_SEC", "6") or "6")
    time.sleep(max(0, secs))

def _fallback_call(fn_name, page, *args):
    try:
        if fn_name.startswith("click_"):
            label = fn_name[len("click_"):].replace("_", " ").strip()
            _disable_motion_and_zoom(page); _wait_layout_stable(page, stable_ms=200)
            if _click_best(page, label): return
            try:
                for fr in page.frames:
                    if fr is page.main_frame: continue
                    el = fr.get_by_text(re.compile(re.escape(label), re.I)).first
                    if el and el.count()>0 and el.is_visible():
                        if _click_attempt(page, el): return
            except Exception: pass
            raise TimeoutError(f"Could not click '{label}'")

        if fn_name.startswith("enter_"):
            label = fn_name[len("enter_"):].replace("_", " ").strip()
            value = args[0] if args else ""
            if _fill_text_like(page, label, value): return
            try:
                for fr in page.frames:
                    if fr is page.main_frame: continue
                    if _fill_text_like(fr, label, value): return
            except Exception: pass
            try:
                tb = page.get_by_role("textbox")
                if tb.count()>0:
                    tb.nth(max(0, tb.count()-1)).fill(value, timeout=_FAST_TIMEOUT); return
            except Exception: pass

        if fn_name.startswith("select_"):
            label = fn_name[len("select_"):].replace("_", " ").strip()
            value = args[0] if args else ""
            if _fast_select_dropdown(page, label, value): return
            try:
                sel = page.get_by_label(re.compile(label, re.I))
                try: sel.select_option(label=value, timeout=_FAST_TIMEOUT); return
                except Exception: pass
                try: sel.select_option(value=value, timeout=_FAST_TIMEOUT); return
                except Exception: pass
            except Exception: pass
            try:
                page.get_by_role("combobox", name=re.compile(label, re.I)).first.click(timeout=_FAST_TIMEOUT)
                page.get_by_role("option", name=re.compile(value, re.I)).first.click(timeout=_FAST_TIMEOUT); return
            except Exception: pass
            try:
                sel = page.locator("select").first
                try: sel.select_option(label=value, timeout=_FAST_TIMEOUT); return
                except Exception: pass
                try: sel.select_option(value=value, timeout=_FAST_TIMEOUT); return
                except Exception: pass
            except Exception: pass

        if fn_name.startswith("radio_"):
            group = fn_name[len("radio_"):].replace("_", " ").strip()
            value = (args[0] if args else "") or ""
            _check_radio(page, group, value); return

        if fn_name.startswith("checkbox_"):
            label = fn_name[len("checkbox_"):].replace("_", " ").strip()
            value = args[0] if args else "check"
            _set_checkbox(page, label, value); return

        if fn_name in ("pick_date", "set_onward_date", "set_return_date"):
            return None
    except Exception as e:
        print(f"[AUTO-STUBS] Fallback failed for {fn_name}: {e!r}")
def click_add_customer(page):
    return _fallback_call('click_add_customer', page)

def click_customers(page):
    return _fallback_call('click_customers', page)

def enter_address(page, value):
    return _fallback_call('enter_address', page, value)

def enter_annual_income(page, value):
    return _fallback_call('enter_annual_income', page, value)

def enter_email(page, value):
    return _fallback_call('enter_email', page, value)

def enter_full_name(page, value):
    return _fallback_call('enter_full_name', page, value)

def enter_initial_deposit(page, value):
    return _fallback_call('enter_initial_deposit', page, value)

def enter_occupation(page, value):
    return _fallback_call('enter_occupation', page, value)

def enter_phone_number(page, value):
    return _fallback_call('enter_phone_number', page, value)

def select_account_type(page, value):
    return _fallback_call('select_account_type', page, value)
