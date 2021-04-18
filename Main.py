import sys, requests, datetime, pyautogui, time, getpass, os
from termcolor import colored
from colorama import init
from datetime import datetime, date

FileName = 'Vacation.txt'
Holy = []
init()
print(colored('Reading vacation file...', 'white'))

Developer = True
try:
    with open(FileName) as File:
        for i in File.readlines():
            Holy.append(i.replace('\n', ''))
except FileNotFoundError:
    print('Vacation file not found')

g = requests.get("https://api.hypixel.net/guild?key=cd34d7bf-2d6f-45f8-90be-73ff7f2f1c94&name=EpicRush")
g = g.json()
Mass = []
rank1 = 25000
rank2 = 70000
rank3 = 150000

adminlist = ["Guild Master", "Helper", "Admin"]
Ranked = ['Member', 'Active', 'Old']

if Developer:
    Hellomotherfaka = f"u - updating information \ntop - Best players\np - Promote list\ni - inactive players (below {rank1})\nuf - update vacation list\nlog - create log file\na - turn on auto promote"
else:
    Hellomotherfaka = f"u - updating information \ntop - Best players\np - Promote list\ni - inactive players (below {rank1})\nuf - update vacation list\nlog - create log file)"


def gettime(ts):
    ts = ts / 1000
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d')


def getrank(N):
    try:
        N = int(N.replace(",", ""))
    except Exception:
        pass
    if N <= rank1:
        return "kicked"
    elif rank1 < N <= rank2:
        return "Member"
    elif rank2 < N <= rank3:
        return "Active"
    elif N > rank3:
        return "Old"


def getcollor(N):
    try:
        N = int(N.replace(",", ""))
    except Exception:
        pass
    if N <= rank1:
        return 'red'
    elif rank1 < N <= rank2:
        return 'yellow'
    elif rank2 < N <= rank3:
        return 'green'
    elif N > rank3:
        return 'cyan'


def Autospam():
    print(colored('Auto promote start in 5 seconds!', 'red'))
    time.sleep(5)
    print(colored('Auto promote start!!!!', 'red'))
    for i in Mass:
        if i[2] != getrank(i[1]):
            if i[2] != "Guild Master" and i[2] != "Helper" and i[2] != "Admin" and (i[0] not in Holy):
                a = gettime(i[3]).split('-')
                aa = date(int(a[0]), int(a[1]), int(a[2]))
                bb = date.today()
                JoinDate = str((bb - aa).days)
                if getrank(i[1]) == "kicked" and int(JoinDate) >= 10:
                    pyautogui.hotkey("t")
                    time.sleep(0.2)
                    pyautogui.write(f"/g kick {i[0]} Inactive")
                    time.sleep(0.5)
                    pyautogui.hotkey("enter")
                    time.sleep(0.3)
                else:
                    if getrank(i[1]) != 'kicked':
                        pyautogui.hotkey("t")
                        time.sleep(0.2)
                        pyautogui.write(f"/g setrank {i[0]} {getrank(i[1])}")
                        time.sleep(0.5)
                        pyautogui.hotkey("enter")
                        time.sleep(0.3)


def findme(N):
    FindPlayersList = []
    for i in Mass:
        if N.lower() in i[0].lower():
            L = ''
            for key, value in i[4].items():
                L += "{0}: {1}  ".format(key, value)
            a = gettime(i[3]).split('-')
            aa = date(int(a[0]), int(a[1]), int(a[2]))
            bb = date.today()
            JoinDate = str((bb - aa).days)
            FindPlayersList.append(
                f"{i[0]} has {'{:,}'.format(i[1])} GXP and have {i[2]} rank (join {JoinDate} days ago)")
            FindPlayersList.append(L)
    if FindPlayersList == []:
        return ['No Found']
    else:
        return FindPlayersList


def ComList():
    Out = ''
    for i in Mass:
        if i[2] in adminlist:
            pass
        elif i[0] in Holy:
            print(colored(f"{i[0].ljust(25, ' ')}{i[2]} -----> {getrank(i[1])}   ({'{:,}'.format(i[1])}GXP) (VACATION)",
                          'white'))
        elif getrank(i[1]) == 'kicked':
            a = gettime(i[3]).split('-')
            aa = date(int(a[0]), int(a[1]), int(a[2]))
            bb = date.today()
            JoinDate = str((bb - aa).days)
            if int(JoinDate) >= 10:
                print(colored(f"{i[0].ljust(25, ' ')}{i[2]} -----> {getrank(i[1])}   ({'{:,}'.format(i[1])}GXP)",
                              'red'))
            else:
                print(colored(
                    f"{i[0].ljust(25, ' ')}{i[2]} -----> {getrank(i[1])}   ({'{:,}'.format(i[1])}GXP)({JoinDate} days in guild)",
                    'white'))

        else:
            try:
                if Ranked.index(getrank(i[1])) > Ranked.index(i[2]):
                    print(
                        colored(f"{i[0].ljust(25, ' ')}{i[2]} -----> {getrank(i[1])}   ({'{:,}'.format(i[1])}GXP)",
                                'green'))
                elif Ranked.index(getrank(i[1])) == Ranked.index(i[2]):
                    pass
                else:
                    print(
                        colored(f"{i[0].ljust(25, ' ')}{i[2]} -----> {getrank(i[1])}   ({'{:,}'.format(i[1])}GXP)",
                                'yellow'))
            except ValueError:
                pass


def Inactive():
    Mass.sort(key=lambda i: i[1])
    for i in Mass:
        if i[1] <= rank1 and i[2] not in adminlist:
            if i[0] in Holy:
                N = i[0].ljust(17, ' ')
                print(colored(f"{N}     ({'{:,}'.format(i[1])}GXP)", 'green'), colored('VACATION'))
            else:
                a = gettime(i[3]).split('-')
                aa = date(int(a[0]), int(a[1]), int(a[2]))
                bb = date.today()
                JoinDate = str((bb - aa).days)
                N = i[0].ljust(17, ' ')
                print(colored(f"{N}     ({'{:,}'.format(i[1])}GXP) (join {JoinDate} days ago)", 'red'))


def TopforGXP():
    Mass.sort(key=lambda i: i[1], reverse=True)
    Counter = 0
    for i in Mass:
        Counter += 1
        N = i[0].ljust(17, ' ')
        a = gettime(i[3]).split('-')
        aa = date(int(a[0]), int(a[1]), int(a[2]))
        bb = date.today()
        JoinDate = str((bb - aa).days)
        print(colored(f"№{str(Counter).rjust(3, '0')} {N}got {'{:,}'.format(i[1])} GXP  (join {JoinDate} days ago)",
                      getcollor(i[1])))


def update():
    global Mass
    Mass = []
    N = len(g['guild']['members'])
    for i in range(len(g['guild']['members'])):
        uuid = g['guild']['members'][i]['uuid']
        x = requests.get("https://playerdb.co/api/player/minecraft/" + uuid)
        x = x.json()
        name = x['data']['player']['username']
        expHistory = g['guild']['members'][i]['expHistory']
        time = g['guild']['members'][i]['joined']
        rank = g['guild']['members'][i]['rank']
        expHistory = sum(expHistory.values())
        expHistory = "{:,}".format(sum(g['guild']['members'][i]['expHistory'].values()))
        Mass.append([name, int(expHistory.replace(',', '')), rank, time, g['guild']['members'][i]['expHistory']])
        print(f'[LOG] Complite {i + 1}/{N}')
    print(f'[LOG] Update complite successfully')


def FileUpdate():
    global Holy
    Holy = []
    print(colored('Reading setup file...', 'white'))
    try:
        with open(FileName) as File:
            for i in File.readlines():
                Holy.append(i.replace('\n', ''))
    except FileNotFoundError:
        print('Vacation file not found')


def log():
    Mass.sort(key=lambda i: i[1], reverse=True)
    Counter = 0
    with open(f'LogFile {datetime.now().date()}.txt', 'w') as f:
        for i in Mass:
            Counter += 1
            N = i[0].ljust(17, ' ')
            a = gettime(i[3]).split('-')
            aa = date(int(a[0]), int(a[1]), int(a[2]))
            bb = date.today()
            JoinDate = str((bb - aa).days)
            L = ''
            for key, value in i[4].items():
                L += "{0}: {1}  ".format(key, value)
            L += '\n'
            f.write(
                f"№{str(Counter).rjust(3, '0')} {N}got {'{:,}'.format(i[1])} GXP, have {i[2]} rank, join {JoinDate} days ago\n")
            f.write(L)
            f.write('\n')


print('\n')
print(colored('Use next commands to use program:', 'green'))
while True:
    print(colored(Hellomotherfaka, 'cyan'))
    print(colored('--------------------------------------------', 'red'))
    Command = input()
    if Command.lower() == 'u':
        update()
    elif Command.lower() == 'top':
        TopforGXP()
    elif Command.lower() == 'i':
        Inactive()
    elif Command.lower() == 'p':
        ComList()
    elif Command.lower() == 'a':
        if Developer:
            Autospam()
    elif Command.lower() == 'uf':
        FileUpdate()
    elif Command.lower() == 'l' or Command.lower() == 'log':
        log()
    else:
        try:
            for i in findme(Command):
                print(colored(i, 'white'))
        except Exception as err:
            print(err)
    print(colored('--------------------------------------------', 'red'))
