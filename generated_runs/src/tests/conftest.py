import os, sys, platform, subprocess
from pathlib import Path
import pytest
from playwright.sync_api import sync_playwright

_THIS = Path(__file__).resolve()
_SRC_ROOT = _THIS.parents[1]  # generated_runs/src
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

def _b(v, default=False):
    if v is None: return default
    return str(v).strip().lower() in ("1","true","yes","y","on")

def _ensure_browsers():
    try:
        subprocess.run([sys.executable, "-m", "playwright", "--version"],
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False, text=True)
    except Exception:
        pass
    args = [sys.executable, "-m", "playwright", "install", "chromium"]
    if platform.system() == "Linux": args.append("--with-deps")
    subprocess.run(args, check=False)

def _launch_browser(pw):
    headless_env = os.getenv("HEADLESS")
    if headless_env is not None:
        headless = _b(headless_env, default=True)
    else:
        headless = False  # headed by default so you see the UI
    slow_mo = int(os.getenv("UI_RUNNER_SLOWMO", "0") or "0")
    args = []
    try:
        is_root = hasattr(os, "geteuid") and os.geteuid() == 0
    except Exception:
        is_root = False
    if _b(os.getenv("PLAYWRIGHT_NO_SANDBOX"), default=is_root and platform.system()=="Linux"):
        args.extend(["--no-sandbox","--disable-setuid-sandbox"])

    try:
        browser = pw.chromium.launch(headless=headless, slow_mo=slow_mo, args=args)
        return browser
    except Exception:
        _ensure_browsers()
        browser = pw.chromium.launch(headless=headless, slow_mo=slow_mo, args=args)
        return browser

@pytest.fixture(scope="session")
def _pw():
    _ensure_browsers()
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(_pw):
    browser = _launch_browser(_pw)
    try:
        yield browser
    finally:
        try: browser.close()
        except Exception: pass

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 900},
        device_scale_factor=1.0,
        is_mobile=False,
        has_touch=False,
        reduced_motion="reduce",
        color_scheme="light",
        accept_downloads=True
    )
    pg = context.new_page()
    pg.set_default_timeout(int(os.getenv("UI_RUNNER_TIMEOUT","20000") or "20000"))
    pg.set_default_navigation_timeout(int(os.getenv("UI_RUNNER_NAV_TIMEOUT","30000") or "30000"))
    try:
        yield pg
    finally:
        try: context.close()
        except Exception: pass
