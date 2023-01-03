# -*- coding: utf-8 -*
import random as rd

# 定义一个玩家的数据：从左到右分别是序列号，玩家名，角色名，当前血量，最大生命，攻击，防御，当前行动点，最大行动点，行动点回复，回复机制，手牌数，技能1，技能1CD，技能2，技能2CD，技能3，技能3CD，护盾值，状态
pldata1 = ['01', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata2 = ['02', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata3 = ['03', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata4 = ['04', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata5 = ['05', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata6 = ['06', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata7 = ['07', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata8 = ['08', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
pldata9 = ['09', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]  # 空置

# 储存一个玩家的手牌
crdata1 = ['01']
crdata2 = ['02']
crdata3 = ['03']
crdata4 = ['04']
crdata5 = ['05']
crdata6 = ['06']
crdata7 = ['07']
crdata8 = ['08']

# 定义boss数据：从左到右分别是角色名，当前血量，最大生命，攻击，防御，技能1，技能1CD，技能2，技能2CD，技能3，技能3CD，状态
bossdata = ['', 0, 0, 0, 0, '', 0, '', 0, '', 0]

# 定义角色数据：从左到右分别是角色名，当前血量，最大生命，攻击，防御，当前行动点，最大行动点，行动点回复，回复机制
chrdata1 = ['晴箬', 1250, 1250, 75, 45, 5, 5, 2, 1]
chrdata2 = ['妮卡欧', 1000, 1000, 95, 35, 5, 5, 2, 1]
chrdata3 = ['云云子', 1000, 1000, 105, 25, 5, 5, 3, 1]
chrdata4 = ['星尘', 1000, 1000, 80, 50, 6, 6, 2, 1]
chrdata5 = ['黯星', 900, 900, 125, 20, 6, 6, 2, 1]
chrdata6 = ['冰块', 1000, 1000, 95, 35, 5, 5, 2, 1]
chrdata7 = ['恪玥', 1000, 1000, 65, 65, 4, 4, 2, 1]
chrdata8 = ['飖', 1000, 1000, 95, 35, 5, 5, 2, 1]

# 定义队伍数据
teamdata1 = ['01']
teamdata2 = ['02']
teamdata3 = ['03']
teamdata4 = ['04']

# 抽卡相关数据
prop_card = open('propcard.txt', 'r', encoding='utf-8')
prop = prop_card.read().splitlines()
prop_card.close()
skill_card = open('skill.txt', 'r', encoding='utf-8')
skills = skill_card.read().splitlines()
skill_card.close()

gamesequence = []  # 玩家回合顺序，第n位的值代表以该值为序列号的玩家会是每轮第n个进行回合的人
plcount = 0  # 游戏未开始时当前玩家数
turn = 0  # 到了哪个玩家的回合
round = 0  # 到了第几轮
ongame = 0  # 0表示无进行游戏；1表示游戏未开始；2表示游戏开始
gametype = 0  # 0表示个人战；1表示团队战；2表示Boss战
teamcount = 2
atkplus = 0
dmgplus = 0
atkmulti = 1
dmgmulti = 1


def init():
    global pldata1, pldata2, pldata3, pldata4, pldata5, pldata6, pldata7, pldata8, crdata1, crdata2, crdata3, crdata4, \
        crdata5, crdata6, crdata7, crdata8, bossdata, gamesequence, plcount, turn, round, ongame, gametype, teamcount, \
        prop, skills, prop_card, skill_card, teamdata1, teamdata2, teamdata3, teamdata4, atkplus, atkmulti, dmgplus, \
        dmgmulti
    pldata1 = ['01', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata2 = ['02', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata3 = ['03', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata4 = ['04', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata5 = ['05', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata6 = ['06', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata7 = ['07', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]
    pldata8 = ['08', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, '', -1, '', -1, '', -1, 0]

    crdata1 = ['01']
    crdata2 = ['02']
    crdata3 = ['03']
    crdata4 = ['04']
    crdata5 = ['05']
    crdata6 = ['06']
    crdata7 = ['07']
    crdata8 = ['08']

    teamdata1 = ['01']
    teamdata2 = ['02']
    teamdata3 = ['03']
    teamdata4 = ['04']

    bossdata = ['', 0, 0, 0, 0, '', 0, '', 0, '', 0]

    prop_card = open('propcard.txt', 'r', encoding='utf-8')
    prop = prop_card.read().splitlines()
    prop_card.close()
    skill_card = open('skill.txt', 'r', encoding='utf-8')
    skills = skill_card.read().splitlines()
    skill_card.close()

    gamesequence = []
    plcount = 0
    turn = 0
    round = 0
    ongame = 0
    gametype = 0
    teamcount = 2
    atkplus = 0
    dmgplus = 0
    atkmulti = 1
    dmgmulti = 1


# 从8个pldata中搜索相关项并返回对应pldata
def listsearch(word):
    global pldata1, pldata2, pldata3, pldata4, pldata5, pldata6, pldata7, pldata8
    error = ['error', 'error', 'error']
    for i in range(0, len(pldata1)):
        if str(pldata1[i]) == word:
            return pldata1
    for i in range(0, len(pldata2)):
        if str(pldata2[i]) == word:
            return pldata2
    for i in range(0, len(pldata3)):
        if str(pldata3[i]) == word:
            return pldata3
    for i in range(0, len(pldata4)):
        if str(pldata4[i]) == word:
            return pldata4
    for i in range(0, len(pldata5)):
        if str(pldata5[i]) == word:
            return pldata5
    for i in range(0, len(pldata6)):
        if str(pldata6[i]) == word:
            return pldata6
    for i in range(0, len(pldata7)):
        if str(pldata7[i]) == word:
            return pldata7
    for i in range(0, len(pldata8)):
        if str(pldata8[i]) == word:
            return pldata8
    return error


# 从4个teamdata中搜索相关项并返回对应teamdata
def teamsearch(word):
    global teamdata1, teamdata2, teamdata3, teamdata4
    error = ['error', 'error', 'error']
    for i in range(0, len(teamdata1)):
        if str(teamdata1[i]) == word:
            return teamdata1
    for i in range(0, len(teamdata2)):
        if str(teamdata2[i]) == word:
            return teamdata2
    for i in range(0, len(teamdata3)):
        if str(teamdata3[i]) == word:
            return teamdata3
    for i in range(0, len(teamdata4)):
        if str(teamdata4[i]) == word:
            return teamdata4
    return error


def cardsearch(word):
    global crdata1, crdata2, crdata3, crdata4, crdata5, crdata6, crdata7, crdata8
    error = ['error', 'error', 'error']
    for i in range(0, len(crdata1)):
        if str(crdata1[i]) == word:
            return crdata1
    for i in range(0, len(crdata2)):
        if str(crdata2[i]) == word:
            return crdata2
    for i in range(0, len(crdata3)):
        if str(crdata3[i]) == word:
            return crdata3
    for i in range(0, len(crdata4)):
        if str(crdata4[i]) == word:
            return crdata4
    for i in range(0, len(crdata5)):
        if str(crdata5[i]) == word:
            return crdata5
    for i in range(0, len(crdata6)):
        if str(crdata6[i]) == word:
            return crdata6
    for i in range(0, len(crdata7)):
        if str(crdata7[i]) == word:
            return crdata7
    for i in range(0, len(crdata8)):
        if str(crdata8[i]) == word:
            return crdata8
    return error


def hascard(player, card):
    crdata = cardsearch(listsearch(player)[0])
    hascard = 0
    for i in range(0, len(crdata)):
        if card == crdata[i]:
            hascard = 1
    return hascard


# 发起游戏
def startgame(player, type):
    global ongame, gametype
    if ongame == 0:
        setplayer(player)
        gametype = type
        if gametype == 0:
            print(player + '发起了一场Strife & Strike 个人战！')
        if gametype == 1:
            print(player + '发起了一场Strife & Strike 团队战！')
        if gametype == 2:
            print(player + '发起了一场Strife & Strike Boss战！')
        ongame = 1
    else:
        print('error')


# 取消游戏
def cancelgame(player):
    global ongame
    if pldata1[1] == player:
        if ongame == 1:
            ongame = 0
            print(player + '取消了战斗！')
            init()  # 重置游戏
        elif ongame == 2:
            print('战斗已开始！')
        elif ongame == 0:
            print('当前无可用游戏！')
    else:
        print('你无法取消游戏，因为你不是发起人！')


# 设置队伍数目
def setteamnum(player, value):
    global teamcount
    if gametype == 1:
        if pldata1[1] == player:
            if 2 <= value <= 4:
                teamcount = value
            else:
                print('不支持该队伍人数')
        else:
            print('你无法更改队伍数目，因为你不是发起人！')
    else:
        print('当前游戏不是团队战！')


# 加入游戏
def joingame(player):
    global ongame
    if ongame == 1:
        if listsearch(player)[0] == 'error':
            setplayer(player)
            print(player + '加入了战斗！')
        else:
            print(player + '已经在游戏中了！')
    elif ongame == 2:
        print('游戏已开始！')
    elif ongame == 0:
        print('当前无可用游戏！')


# 开始游戏
def start(player):
    global ongame, gamesequence, teamcount, teamdata1, teamdata2, teamdata3, teamdata4, pldata1, round, turn
    if ongame == 1:
        if pldata1[1] == player:
            ready = 1
            for i in range(0, 8):
                num = '0' + str(i)
                if listsearch(num)[1] != '' and listsearch(num)[2] == '':
                    ready = 0
                # 若pldata1位非空（有玩家占用此数据）而2位为空（角色没选），则不开始游戏
            if ready == 1:
                ongame = 2
                if gametype == 0:
                    rd.shuffle(gamesequence)
                elif gametype == 1:
                    rd.shuffle(gamesequence)
                    j = 0
                    for i in range(0, plcount):
                        if j % teamcount == 0:
                            teamdata1.append(gamesequence[i])
                        elif j % teamcount == 1:
                            teamdata2.append(gamesequence[i])
                        elif j % teamcount == 2:
                            teamdata3.append(gamesequence[i])
                        elif j % teamcount == 3:
                            teamdata4.append(gamesequence[i])
                        j = j+1
                print('战斗开始！')
                for k in range(1, plcount+1):
                    num2 = '0' + str(k)
                    drawcard(num2, 4)
                drawcard('0' + str(gamesequence[0]), 2)
                round = 1
                turn = 1
            else:
                print('有玩家还未准备好！')
        else:
            print('你无法开始游戏，因为你不是发起人！')
    elif ongame == 2:
        print('游戏已开始！')
    elif ongame == 0:
        print('当前无可用游戏！')


# 将玩家加入游戏队伍
def setplayer(player):
    global plcount, gamesequence
    if listsearch(player)[0] == 'error':
        if plcount <= 7:
            for i in range(1, 9):
                if plcount == i - 1:
                    plstr = '0' + str(i)
                    listsearch(plstr)[1] = player
                    plcount += 1
                    gamesequence.append(i)
                    break
        else:
            print('error')
    else:
        print('error')


# 选择角色
def choosechara(player, chara):
    if listsearch(player)[0] != 'error':
        if listsearch(chara)[0] == 'error':
            a = 9
            print(player + '选择了' + chara + '!')
            if chara == '晴箬':
                global chrdata1
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata1[i]
            elif chara == '妮卡欧':
                global chrdata2
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata2[i]
            elif chara == '云云子':
                global chrdata3
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata3[i]
            elif chara == '星尘':
                global chrdata4
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata4[i]
            elif chara == '黯星':
                global chrdata5
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata5[i]
            elif chara == '冰块':
                global chrdata6
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata6[i]
            elif chara == '恪玥':
                global chrdata7
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata7[i]
            elif chara == '飖':
                global chrdata8
                for i in range(0, a):
                    listsearch(player)[i+2] = chrdata8[i]
            else:
                print('该角色不存在！')
        else:
            print('此角色已被选择！')

    else:
        print('玩家不在游戏中')


# 从牌堆中返回一张卡牌
def draw(times):
    global prop
    card = []
    for i in range(0, times):
        c = prop[rd.randint(0, len(prop) - 1)]
        card.append(c)
        prop.remove(c)
        if len(prop) == 0:
            print('牌堆里已经没有牌了!')
            break
    return card


def drawcard(player, times):
    card = draw(times)
    num = listsearch(player)[0]
    for m in range(0, len(card)):
        cardsearch(num).append(card[m])


# 删除卡牌
def delcard(player, card):
    crdata = cardsearch(listsearch(player)[0])
    for i in range(1, len(crdata)):
        if crdata[i] == card:
            crdata.pop(i)
            break


# 出牌
def playcard(source, target, card):
    global turn, gamesequence, atkplus, atkmulti, dmgplus, dmgmulti
    turnpl = gamesequence[turn-1]
    num = '0' + str(turnpl)
    atkplus = 0
    dmgplus = 0
    atkmulti = 1
    dmgmulti = 1
    dicesize = 4
    hadcard = 1
    element = 0  # 值为-1时，此伤害为真实伤害

    if listsearch(source)[0] == num and ongame == 2:
        if listsearch(source)[7] >= len(card) >= 1:
            for i2 in range(0, len(card)):
                if hascard(source, card[i2]) == 0:
                    hadcard = 0
            if hadcard == 1:
                for i in range(0, len(card)):
                    if card[i] == '末影水晶':
                        losthealth(source, (30 + 15 * dice(source, 4, 2)))
                        tglist = []
                        if gametype == 1:
                            for j in range(0, len(gamesequence)):
                                num2 = str(gamesequence[j])
                                if teamsearch(num2) != teamsearch(str(turnpl)):
                                    tglist.append('0' + num2)
                        elif gametype == 0:
                            for j in range(0, len(gamesequence)):
                                num2 = '0' + str(gamesequence[j])
                                if num2 != num:
                                    tglist.append(num2)
                        value = 40 + 15 * dice(source, 8, 1)
                        for k in range(0, len(tglist)):
                            tg1 = listsearch(tglist[k])[1]
                            damage(source, tg1, value, 0)
                    elif card[i] == '英雄传说':
                        gainhealth(source, 100)
                        atkplus = atkplus + 20
                    elif card[i] == '木剑':
                        listsearch(source)[5] = listsearch(source)[5] + 10
                    elif card[i] == '梦想的庇护':
                        gainhealth(source, 100)
                        listsearch(source).append(499)
                    elif card[i] == '盾牌':
                        listsearch(source)[6] = listsearch(source)[6] + 5
                        listsearch(source)[18] = listsearch(source)[18] + 100
                    elif card[i] == '登神的长阶':
                        losthealth(source, listsearch(source)[4] * 0.1)
                        tglist2 = []
                        mindice = 6
                        maxdice = 1
                        for j2 in range(0, len(gamesequence)):
                            num3 = '0' + str(gamesequence[j2])
                            dice1 = dice(listsearch(num3)[1], 6, 1)
                            if dice1 < mindice:
                                mindice = dice1
                                tglist2 = [num3]
                            elif dice1 == mindice:
                                tglist2.append(num3)
                            if dice1 > maxdice:
                                maxdice = dice1
                        value2 = maxdice * 50
                        for j4 in range(0, len(tglist2)):
                            tg1 = listsearch(tglist2[j4])[1]
                            damage(source, tg1, value2, 0)
                    elif card[i] == '六方棱':
                        dicesize = 6
                    elif card[i] == '八重镜':
                        dicesize = 8
                    elif card[i] == '十面璃':
                        dicesize = 10
                if haseffect(target, '庇护') == 1:
                    atkplus = atkplus - 10
                    deleffect(target, '庇护')
                dmg = (dice(source, dicesize, 1) * ((listsearch(source)[5] + atkplus) * atkmulti - listsearch(target)[6]) + dmgplus) * dmgmulti
                damage(source, target, dmg, element)
                listsearch(source)[7] = listsearch(source)[7] - len(card)
                for i3 in range(0, len(card)):
                    delcard(source, card[i3])
        elif len(card) == 0 and listsearch(source)[7] >= 1:
            if haseffect(target, '庇护') == 1:
                atkplus = atkplus - 10
                deleffect(target, '庇护')
            dmg = (dice(source, dicesize, 1) * ((listsearch(source)[5] + atkplus) * atkmulti - listsearch(target)[6]) + dmgplus) * dmgmulti
            damage(source, target, dmg, 0)
            listsearch(source)[7] = listsearch(source)[7] - 1
        else:
            print('你的行动点不足！')
    else:
        print('当前不是你的回合！')


# 弃牌
def discard(player, card):
    global turn, gamesequence
    num = '0' + str(gamesequence[turn])
    if listsearch(player)[11] > 8 and num == listsearch(player)[0]:  # 手牌数>8且为该玩家回合
        delcard(player, card)


# 丢骰子
def dice(player, size, times):
    value = 0
    for i in range(1, times+1):
        value = value + rd.randint(1, size)
    print(str(player) + '的' + str(times) + 'd' + str(size) + '投掷结果是： ' + str(value))
    return value


# 造成伤害
def damage(source, target, value, element):
    if haseffect(target, '咕了') == 0:
        if haseffect(target, '闪避') == 0:
            if listsearch(target)[18] >= value:  # 判定目标护盾是否存在并给予伤害
                listsearch(target)[18] = listsearch(target)[18] - value
            elif value > listsearch(target)[18] > 0:
                listsearch(target)[3] = listsearch(target)[3] - value + listsearch(target)[18]
                listsearch(target)[18] = 0
            else:
                listsearch(target)[3] = listsearch(target)[3] - value
            print(source + '对' + target + '造成了' + str(value) + '点伤害！')
        else:
            print(source + '凭借灵巧的身法闪避了一次攻击')
    else:
        print(source + '咕了这回合，所以并没有受到伤害')


def losthealth(target, value):
    listsearch(target)[3] = listsearch(target)[3] - value
    print(target + '失去了' + str(value) + '点生命！')


def gainhealth(target, value):
    if haseffect(target, '死灵') == 0:
        listsearch(target)[3] = listsearch(target)[3] + value
        for i in range(1, 9):  # 将玩家生命保持在最大值以下
            num = '0' + str(i)
            if listsearch(num)[3] > listsearch(num)[4]:
                listsearch(num)[3] = listsearch(num)[4]
        print(target + '回复了' + str(value) + '点生命！')
    else:
        print('治愈失败了……')


# 将玩家生命保持在最大值以下
'''def maxhealth():
    for i in range(1, 9):
        num = '0' + str(i)
        if listsearch(num)[3] > listsearch(num)[4]:
            listsearch(num)[3] = listsearch(num)[4]'''


def passturn():
    global turn, round, plcount, gamesequence, pldata9
    num = '0' + str(gamesequence[turn-1])
    if listsearch(num)[11] <= 8:
        turn = turn + 1
        if turn == plcount + 1:
            turn = 1
            round += 1
        effclr = []
        effclrpl = []
        for i in range(1, 9):
            num = '0' + str(i)
            if len(listsearch(num)) > len(pldata9):
                for j in range(len(pldata9), len(listsearch(num))):
                    listsearch(num)[j] = listsearch(num)[j] - 1  # 状态持续时间-1
                    if listsearch(num)[j] % 100 == 0:  # 清除持续时间为0的状态
                        effclr.append(geteffecttype(listsearch(num)[0], j + 1 - len(pldata9)))
                        effclrpl.append(listsearch(num)[0])
        if len(effclr) != 0:
            for k in range(0, len(effclr)):
                deleffect(effclrpl[k], effclr[k])
        turnpl = '0' + str(gamesequence[turn - 1])
        drawcard(turnpl, 2)
    else:
        print('手牌超过上限，需要弃牌！')


def playerpass(player):
    if listsearch(gamesequence[turn-1]) == player:
        passturn()
    else:
        print('当前不是你的回合！')


def geteffecttype(player, num):
    global pldata9
    type = 0
    effect = listsearch(player)[num - 1 + len(pldata9)]  # 偷懒.jpg
    if effect//100 == 1:
        type = '力量'
    elif effect//100 == 2:
        type = '力量II'
    elif effect//100 == 3:
        type = '再生'
    elif effect//100 == 4:
        type = '庇护'
    elif effect//100 == 5:
        type = '浴霸'
    elif effect//100 == 6:
        type = '熔岩之触'
    elif effect//100 == 7:
        type = '凛冰之拥'
    elif effect//100 == 8:
        type = '死灵'
    elif effect//100 == 9:
        type = '混乱'
    elif effect//100 == 10:
        type = '星牢'
    elif effect//100 == 11:
        type = '嘲讽'
    elif effect//100 == 12:
        type = '脆弱'
    elif effect//100 == 13:
        type = '氤氲'
    elif effect//100 == 14:
        type = '透支'
    elif effect//100 == 15:
        type = '镜像'
    elif effect//100 == 16:
        type = '梦境'
    elif effect//100 == 17:
        type = '咕了'
    elif effect//100 == 18:
        type = '冰封'
    elif effect//100 == 19:
        type = '余韵'
    elif effect//100 == 20:
        type = '闪避'
    elif effect//100 == 21:
        type = '自疗'
    elif effect//100 == 22:
        type = '灵曜'
    elif effect//100 == 23:
        type = '迟缓'
    elif effect//100 == 24:
        type = '迅捷'
    elif effect//100 == 25:
        type = '附身'
    elif effect//100 == 26:
        type = '落龙阵'
    return type


# 获取指定effect的持续时间 （若该值=99，则受击后消失；）
def geteffecttime(player, num):
    global pldata9, plcount
    effect = listsearch(player)[num - 1 + len(pldata9)]  # 偷懒.jpg
    num = (effect % 100)//plcount + 1
    return num


def haseffect(player, effect):
    global pldata9
    haseffect = 0
    if len(listsearch(player)) != len(pldata9):
        for i in range(1, len(listsearch(player)) - len(pldata9) + 1):
            if geteffecttype(player, i) == effect:
                haseffect = 1
    return haseffect


def deleffect(player, effect):
    if haseffect(player, effect) == 1:
        for i in range(1, len(listsearch(player)) - len(pldata9) + 1):
            if geteffecttype(player, i) == effect:
                listsearch(player).pop(i + len(pldata9) - 1)
                break


# debug区域
init()
joingame('Icecube')
startgame('Icecube', 1)
choosechara('Icecube', '飖')
choosechara('Icecube', '晴箬')
cancelgame('Sier')
joingame('Sier')
choosechara('Sier', '恪玥')
joingame('.')
choosechara('.', '飖')
setteamnum('Icecube', 2)
start('Icecube')
print(gamesequence)
print(pldata1)
print(pldata2)
print(pldata3)
