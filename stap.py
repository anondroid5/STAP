#coding: utf-8
#STAP細胞が生成されるまでを検証するプログラム
#STAP細胞の生成確率1/26^4=1/1,235,663,104
#STAP細胞を作成できるプログラム

import random
import time #処理時間計測用モジュール
starttime = time.clock()#処理開始時刻
alphabet = [chr(i) for i in xrange(65, 91)]
stap = "STAP"
tmp = ""
count = 0
while tmp != stap:
    tmp=""
    count +=1
    for i in range(4):
        tmp += alphabet[random.randint(0, len(alphabet)-1)]

    print str(count)+u"回目のサンプリング結果:"+tmp+u"細胞"
    #print tmp+u"細胞!"
    if tmp == stap:
        print ""
        print str(count)+u"回目に陽性反応を確認しました!"
        print ""
        print tmp+u"細胞はあります☆"
        print ""
        time1 = time.clock() #処理終了時刻
        acttime = (time1 - starttime)
        if acttime < 60:
            print u"STAP細胞発見まで"+str(acttime) +u"秒掛かりました."
        elif acttime > 60 and acttime <3600:
            print u"STAP細胞発見まで"+str(acttime/60) +u"分掛かりました."
        else:
            print u"STAP細胞発見まで"+str(acttime/3600) +u"時間掛かりました."