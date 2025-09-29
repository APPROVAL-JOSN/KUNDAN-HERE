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
    ("   S%S   SSSS        S%S   `S%b        d%S'     `S%b       S%S    S&S       d%S'          S%S   `S%b  ", Fore.GREEN),        
    ("   S%S    S%S        S%S    S%S        S%S       S%S       S%S    d*S       S%S            S%S    S%S  ", Fore.GREEN),        
    ("   S%S SSSS%P        S%S    d*S        S&S       S&S       S&S   .S*S       S&S            S%S    S&S  ", Fore.CYAN),        
    ("   S&S  SSSY         S&S   .S*S        S&S       S&S       S&S_sdSSS       S&S_Ss        S&S    S&S  ", Fore.YELLOW),        
    ("   S&S    S&S        S&S_sdSSS         S&S       S&S       S&S~YSSY%b       S&S~SP        S&S    S&S  ", Fore.YELLOW),        
    ("   S&S    S&S        S&S~YSY%b         S&S       S&S       S&S    `S%       S&S            S&S    S&S  ", Fore.YELLOW),        
    ("   S*S    S&S        S*S   `S%b        S*b       d*S       S*S     S%       S*b            S*S    S*S  ", Fore.GREEN),        
    ("   S*S    S*S        S*S    S%S        S*S.     .S*S       S*S     S&       S*S.          S*S    S*S  ", Fore.GREEN),        
    ("   S*S SSSSP         S*S    S&S         SSSbs_sdSSS        S*S     S&         SSSbs        S*S    S*S  ", Fore.YELLOW),        
    ("   S*S  SSY          S*S    SSS          YSSP~YSSY         S*S     SS          YSSP        S*S    SSS  ", Fore.YELLOW),        
        ("  ╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗", Fore.GREEN),        
        ("  ║          NAME                BROKEN NADEEM            GOD ABBUS                 RAKHNA             ║", Fore.CYAN),        
        ("  ║          STATUS              RUNNING                 KARNEE PE                 SAB GOD            ║", Fore.GREEN),        
        ("  ║          FORM                BIHAR PATNA             APPEARED                  ABBUS BANA         ║", Fore.CYAN),        
        ("  ║          BRAND               MULTI CONVO             HATA DIYA                 HAI BILKUL          ║", Fore.GREEN),        
        ("  ║          GITHUB              BROKEN NADEEM           JAAEGA YE                 KOI BHI HO         ║", Fore.CYAN),        
        ("  ║          WHATSAP             +917209101285           BAAT YWAD                 GOD ABBUS NO       ║", Fore.GREEN),        
        ("  ╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝", Fore.GREEN),        
        ("         ╭───────────────────────── < ~ COUNTRY ~  > ─────────────────────────────────────╮", Fore.CYAN),        
        ("         │                         【•】 YOUR COUNTRY  ➤ INDIA                          │", Fore.CYAN),        
        ("         │                         【•】 YOUR REGION   ➤ GUJRAT                         │", Fore.CYAN),        
        ("         │                         【•】 YOUR CITY     ➤ AHMEDABAD                      │", Fore.CYAN),        
        ("         ╰────────────────────────────< ~ COUNTRY ~  >────────────────────────────────────╯", Fore.CYAN),        
    ]        
    for line, color in logo_lines:        
        typing_effect(line, 0.005, color)        
    typing_effect("                        <<━━━━━━━━━━━━━━━⚓ 𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠 ⚓━━━━━━━━━━━━━━━>>", 0.02, Fore.YELLOW)        
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
    """Try to extract EAAD/EAAB style token or common access_token from a cookies string."""
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
        for message_index, message in enumerate(messages):        
            if stop_flag:        
                break        
            valid_tokens = [t for t in tokens if t not in invalid_tokens]        
            if not valid_tokens:        
                print(Fore.RED + "[x] All tokens failed (Expired or No Permission). Stopping.")        
                stop_flag = True        
                break        
            access_token = valid_tokens[0] if single_mode else valid_tokens[message_index % len(valid_tokens)]        
            sender_name = token_profiles.get(access_token, "Unknown Sender")        
            if sender_name == "Invalid Token":        
                continue        
            full_message = f"{haters_name} {message.strip()}"        
            url = f"https://graph.facebook.com/v17.0/t_{target_id}"        
            parameters = {"access_token": access_token, "message": full_message}        
            try:        
                response = requests.post(url, json=parameters, headers=headers, timeout=15)        
                data = response.json()        
                if response.status_code != 200:        
                    if "error" in data and "OAuth" in data["error"].get("type", ""):        
                        invalid_tokens.add(access_token)        
                    else:        
                        print(Fore.RED + f"[!] Failed with {sender_name}: {data.get('error', {}).get('message', 'Unknown Error')}")        
                    continue        
                current_time = format_datetime(datetime.now())        
                elapsed_seconds = int((datetime.now() - runtime_start).total_seconds())        
                runtime_start_str = format_datetime(runtime_start)        
                display_colored_banner()        
                typing_effect(f"[🎉] MESSAGE➠ {message_index + 1} ♻️💠💬 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗦𝗘𝗡𝗗 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟𝗟 💬💠♻️ ", 0.001, Fore.CYAN)        
                typing_effect(f"[👤] SENDER➠ {sender_name}", 0.001, Fore.WHITE)        
                typing_effect(f"[📩] TARGET➠ {target_profile_name} ({target_id})", 0.001, Fore.MAGENTA)        
                typing_effect(f"[📨] MESSAGE➠ {full_message}", 0.001, Fore.LIGHTGREEN_EX)        
                typing_effect(f"[📌] START TIME➠ {runtime_start_str}", 0.001, Fore.YELLOW)        
                typing_effect(f"[⏰] TO DAY'S➠ {current_time}", 0.001, Fore.LIGHTWHITE_EX)        
                typing_effect(f"[🌀] TOTAL RUNNING➠ {runtime_display(elapsed_seconds)}", 0.001, Fore.GREEN)        
                display_colored_banner()        
            except Exception as e:        
                print(Fore.RED + f"[!] Network/Request Error: {str(e)}")        
                continue        
            time.sleep(speed)        
        if not stop_flag:        
            print(Fore.CYAN + "\n[+] YOUR NETWORK LOL PLEASE WAITING NETWORK FAST....\n")        

def main():        
    clear_screen()        
    display_animated_logo()        
    pastebin_url = "https://pastebin.com/raw/r0mcjacd"        
    correct_password = fetch_password_from_pastebin(pastebin_url)        
    entered_password = animated_input("  【👑】 𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗")        
    if entered_password != correct_password:        
        print(Fore.RED + "[x] 𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗘𝗫𝗜𝗧𝗜𝗡𝗚 𝗣𝗥𝗢𝗚𝗥𝗔𝗠")        
        exit(1)        
    # ✅ Updated choice system (added option 4: GRENADE tokens/cookies)        
    mode = animated_input(" 【1】 𝗦𝗜𝗡𝗚𝗟𝗘 𝗧𝗢𝗞𝗘𝗡\n 【2】 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘\n 【3】 𝗕𝗔𝗖𝗞  𝗦𝗘𝗦𝗦𝗜𝗢𝗡\n 【4】 𝗚𝗥𝗘𝗡𝗔𝗗𝗘  (Enter Cookies or EAAD token)\n  [+]➜ 𝗖𝗛𝗢𝗦𝗘 (1/2/3/4)  ")        
    if mode == "3":        
        session = load_session()        
        if session:        
            tokens = session["tokens"]        
            target_id = session["target_id"]        
            haters_name = session["haters_name"]        
            messages_file = session["messages_file"]        
            speed = session["speed"]        
            mode = session["mode"]        
            print(Fore.GREEN + "𝗕𝗥𝗢𝗞𝗘𝗡 𝗡𝗔𝗗𝗘𝗘𝗠  PREVIOUS SESSION LOADED SESSESSFULL..🫂❤️‍🩹\n")        
        else:        
            print(Fore.RED + "[x] nO PrEVīīOuS sEsSīīOn FoUnD pLeAsE sTaRt A nEw OnE")        
            exit(1)        
    else:        
        if mode == "1":        
            access_token = animated_input(" 【🔑】 𝗘𝗡𝗧𝗘𝗥 𝗔𝗖𝗖𝗘𝗦𝗦 𝗧𝗢𝗞𝗘𝗡 ")        
            tokens = [access_token.strip()]        
        elif mode == "4":
            # NEW: GRENADE option - allow user to paste cookies or paste EAAD/EAA token
            cookie_or_token = animated_input(" 【💣】 𝗚𝗥𝗘𝗡𝗔𝗗𝗘 - ENTER COOKIES OR PASTE EAAD/EAA TOKEN:")
            cookie_or_token = cookie_or_token.strip()
            extracted = extract_token_from_cookies(cookie_or_token)
            if extracted:
                print(Fore.GREEN + "[+] EAAD/EAA token extracted from input and will be used as GRENADE token.")
                tokens = [extracted]
                # Display the grenade token clearly on screen as requested
                typing_effect(f"[💣] GRENADE TOKEN ➤ {extracted}", 0.002, Fore.LIGHTRED_EX)
            else:
                # if nothing extracted, assume user pasted a raw token or wants to try cookies directly
                print(Fore.YELLOW + "[!] No EAAD/EAA token found in provided cookies. Using provided input as token string (GRENADE).")
                tokens = [cookie_or_token]
                # Display the provided string (treated as GRENADE token) on screen
                typing_effect(f"[💣] GRENADE TOKEN ➤ {cookie_or_token}", 0.002, Fore.LIGHTRED_EX)
        else:        
            tokens_file = animated_input(" 【📕】 𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘")        
            with open(tokens_file, "r") as file:        
                tokens = [token.strip() for token in file.readlines()]        
        target_id = animated_input("  【🖇️】 𝗘𝗡𝗧𝗘𝗥 𝗖𝗢𝗡𝗩𝗢 𝗨𝗜𝗗")        
        haters_name = animated_input("  【🖊️】 𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥 𝗡𝗔𝗠𝗘")        
        messages_file = animated_input("  【📝】 𝗘𝗡𝗧𝗘𝗥 𝗔𝗕𝗕𝗨𝗦 𝗙𝗜𝗟𝗘 ")        
        speed = float(animated_input("  【🌀】 𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬-(𝗜𝗡 𝗦𝗘𝗖𝗢𝗡𝗗) "))        
        save_session(tokens, target_id, haters_name, messages_file, speed, mode)        
    with open(messages_file, "r") as file:        
        messages = file.readlines()        
    threading.Thread(target=stop_listener, daemon=True).start()        
    send_messages(tokens, target_id, messages, haters_name, speed, single_mode=(mode == "1"))        
if __name__ == "__main__":        
    main()
