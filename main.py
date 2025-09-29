import requests
import time
import os
import threading
import json
from colorama import init, Fore, Style
from datetime import datetime
import re

# Initialize Colorama
init(autoreset=True)
stop_flag = False
invalid_tokens = set()
runtime_start = datetime.now()  # Runtime Start Time
session_file = "session.json"   # Session file for auto-resume

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, delay=0.002, color=Fore.WHITE):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def display_colored_banner():
    parts = [
        (Fore.CYAN, "<<════════════════════════════════((🌐🎯♻️ NONSTOP RUNNING ♻️🎯🌐))═══════════════════════════════════════>>")
    ]
    for color, text in parts:
        print(color + text, end='')
    print("\n")

def display_animated_logo():
    clear_screen()
    logo_lines = [
    ("   .S_SSSs           .S_sSSs            sSSs_sSSs           .S     S.          sSSs         .S_sSSs    ", Fore.YELLOW),
    ("   .SS~SSSSS         .SS~YS%%b          d%%SP~YS%%b         .SS    SS.        d%%SP         .SS~YS%%b   ", Fore.YELLOW),
    ("   S%S   SSSS        S%S   `S%b        d%S'     `S%b        S%S    S&S        d%S'          S%S   `S%b  ", Fore.GREEN),
    ("   S%S    S%S        S%S    S%S        S%S       S%S        S%S    d*S        S%S           S%S    S%S  ", Fore.GREEN),
    ("   S%S SSSS%P        S%S    d*S        S&S       S&S        S&S   .S*S        S&S           S%S    S&S  ", Fore.CYAN),
    ("   S&S  SSSY         S&S   .S*S        S&S       S&S        S&S_sdSSS         S&S_Ss        S&S    S&S  ", Fore.YELLOW),
    ("   S&S    S&S        S&S_sdSSS         S&S       S&S        S&S~YSSY%b        S&S~SP        S&S    S&S  ", Fore.YELLOW),
    ("   S&S    S&S        S&S~YSY%b         S&S       S&S        S&S    `S%        S&S           S&S    S&S  ", Fore.YELLOW),
    ("   S*S    S&S        S*S   `S%b        S*b       d*S        S*S     S%        S*b           S*S    S*S  ", Fore.GREEN),
    ("   S*S    S*S        S*S    S%S        S*S.     .S*S        S*S     S&        S*S.          S*S    S*S  ", Fore.GREEN),
    ("   S*S SSSSP         S*S    S&S         SSSbs_sdSSS         S*S     S&         SSSbs        S*S    S*S  ", Fore.YELLOW),
    ("   S*S  SSY          S*S    SSS          YSSP~YSSY          S*S     SS          YSSP        S*S    SSS  ", Fore.YELLOW),
        ("  ╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.GREEN),
        ("  ║          NAME                BROKEN NADEEM           GOD ABBUS                 RAKHNA             ║", Fore.CYAN),
        ("  ║          STATUS              RUNNING                 KARNEE PE                 SAB GOD            ║", Fore.GREEN),
        ("  ║          FORM                BIHAR PATNA             APPEARED                  ABBUS BANA         ║", Fore.CYAN),
        ("  ║          BRAND               MULTI CONVO             HATA DIYA                 HAI BILKUL         ║", Fore.GREEN),
        ("  ║          GITHUB              BROKEN NADEEM           JAAEGA YE                 KOI BHI HO         ║", Fore.CYAN),
        ("  ║          WHATSAP             +917209101285           BAAT YWAD                 GOD ABBUS NO       ║", Fore.GREEN),
        ("  ╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.GREEN),
        ("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN),
        ("         │                         【•】 YOUR COUNTRY  ➤ INDIA                            │", Fore.CYAN),
        ("         │                         【•】 YOUR REGION   ➤ GUJRAT                           │", Fore.CYAN),
        ("         │                         【•】 YOUR CITY     ➤ AHMEDABAD                        │", Fore.CYAN),
        ("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN),
    ]
    for line, color in logo_lines:
        typing_effect(line, 0.005, color)
    typing_effect("                       <<━━━━━━━━━━━━━━━⚓ 𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠 ⚓━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)
    time.sleep(1)

def animated_input(prompt_text):
    print(Fore.CYAN + "<<═════════════════════════════════((♻️👑🌐 ONWER BROKEN NADEEM 🌐👑♻️))═════════════════════════════════>>")
    typing_effect(prompt_text, 0.03, Fore.LIGHTYELLOW_EX)
    return input(Fore.GREEN + "➜ ")

def fetch_password_from_pastebin(pastebin_url):
    try:
        response = requests.get(pastebin_url, timeout=10)
        response.raise_for_status()
        return response.text.strip()
    except:
        exit(1)

def fetch_profile_name(access_token):
    if access_token in invalid_tokens:
        return "Invalid Token"
    try:
        response = requests.get("https://graph.facebook.com/me", params={"access_token": access_token}, timeout=10)
        if response.status_code != 200:
            data = response.json()
            if "error" in data and "OAuth" in data["error"].get("type", ""):
                invalid_tokens.add(access_token)
                return "Invalid Token"
            return "Permission Error"
        return response.json().get("name", "Unknown")
    except:
        invalid_tokens.add(access_token)
        return "Invalid Token"

def fetch_target_name(target_id, access_token):
    try:
        response = requests.get(f"https://graph.facebook.com/{target_id}", params={"access_token": access_token}, timeout=10)
        response.raise_for_status()
        return response.json().get("name", "GROUP UID")   # Always "GROUP UID"
    except:
        return "GROUP UID"

def stop_listener():
    global stop_flag
    while True:
        cmd = input()
        if cmd.strip().lower() == "stop":
            print(Fore.RED + "\n[!] STOP COMMAND RECEIVED. EXITING...\n")
            stop_flag = True
            break

def format_runtime(seconds):
    years = seconds // (365*24*3600)
    seconds %= (365*24*3600)
    months = seconds // (30*24*3600)
    seconds %= (30*24*3600)
    days = seconds // (24*3600)
    seconds %= (24*3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return years, months, days, hours, minutes, seconds

def runtime_display(seconds):
    y, m, d, h, mi, s = format_runtime(seconds)
    parts = []
    if y > 0:
        parts.append(f"{y} YEARS")
        parts.append(f"{m} MONTHS")
        parts.append(f"{d} DAYS")
        parts.append(f"{h} HOURS")
        parts.append(f"{mi} MINUTES")
    elif m > 0:
        parts.append(f"{m} MONTHS")
        parts.append(f"{d} DAYS")
        parts.append(f"{h} HOURS")
        parts.append(f"{mi} MINUTES")
    elif d > 0:
        parts.append(f"{d} DAYS")
        parts.append(f"{h} HOURS")
        parts.append(f"{mi} MINUTES")
    elif h > 0:
        parts.append(f"{h} HOURS")
        parts.append(f"{mi} MINUTES")
    elif mi > 0:
        parts.append(f"{mi} MINUTES")
        parts.append(f"{s} SECONDS")
    else:
        parts.append(f"{s} SECONDS")
    return " ".join(parts)

# ✅ Time formatter
def format_datetime(dt):
    day = dt.day
    month = dt.strftime("%B").upper()
    year = dt.year
    time_str = dt.strftime("%I:%M:%S %p")  # Correct spacing
    return f"{day} {month} {year}  {time_str}"

def save_session(tokens, target_id, haters_name, messages_file, speed, mode):
    session_data = {
        "tokens": tokens,
        "target_id": target_id,
        "haters_name": haters_name,
        "messages_file": messages_file,
        "speed": speed,
        "mode": mode
    }
    with open(session_file, "w") as f:
        json.dump(session_data, f)

def load_session():
    if os.path.exists(session_file):
        with open(session_file, "r") as f:
            return json.load(f)
    return None

def extract_token_from_cookies(cookies_str):
    """Try to extract EAAD/EAAB/EAA style token or common access_token from a cookies string."""
    if not cookies_str:
        return None
    # common long Facebook tokens often start with EAAB/EAAD/EAA
    m = re.search(r'(EAAD\w+|EAAB\w+|EAA\w+)', cookies_str)
    if m:
        return m.group(1)
    m = re.search(r'(?:(?:access_token|token)=)([^; \n]+)', cookies_str, re.IGNORECASE)
    if m:
        return m.group(1)
    return None

def send_messages(tokens, target_id, messages, haters_name, speed, single_mode=False):
    global stop_flag
    token_profiles = {token: fetch_profile_name(token) for token in tokens}
    target_profile_name = fetch_target_name(target_id, tokens[0])
    headers = {"User-Agent": "Mozilla/5.0"}
    start_time = time.time()
    max_runtime = 730 * 24 * 60 * 60
    while not stop_flag:
        if time.time() - start_time > max_runtime:
            print(Fore.RED + "\n[!] FUTURE SYSTEM LIMIT REACHED (2 YEARS NONSTOP COMPLETE). EXITING...\n")
            break
    ... (truncated for brevity)
