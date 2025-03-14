orig_hash = [
    'dd41ab0f74888ed22902452c552939b8',
    '7a3039bcc32517b141b834f010de12e4',
    '760d196beed8d1625b0808954ef29b05',
    '239d39e00c9cfba828fd02001a9a901e'
] # DO NOT CHANGE ORIGINAL HASH UNLESS DATABASE IS UPDATED
from tqdm.rich import tqdm # progress bar
import os

# BACKUP LOCATION

conv1 = '\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\tÿþ÷'
conv = [
        '\n3þCSQNF8Ldg\'20)T^{z§R6kbZ%Y:#]}<1,+~\tWec@nXqBGPl_r|DhvOo9Js;Hyt(A5.pi\\E`f>[M4-"w!? $mu&*7aKjIUV/ÿx=÷',
        '\n3lgþLP5AQnfJ/zRaH=§6Seq2E1,\tB8r({jid0kZo&:$-t*V|;vDU!9[Gb\'s}NO\\ph+^mcW_TF%Xu>Y"`#I~<C.y7?w 4M@x)ÿ]K÷',
        '\n31?rJþR-/`o5g~VYL,X§xmsBjHW0;NZ!&9\\]n4\'kdt|%^O[liA.*}fTMG8c$>:KUev ywIS_pQb2+")({\tq@hzPuC#=E76÷FDÿ<a',
        '\n3X"VU/qþ,%+i:$vlxG_§az\\<hEc|Wb)L&sJCjtDMp6;A-F40\t QH2yI8fgwn5R]k^*oZP(`T>dN÷[}SKm1#=eru@\'?O7.{!9Yÿ~B',
        '\n3*bHn)tþzF+mv8CQA5B:2ga[T\'"\tl;{f#Wdy]&-I0^7`X/V~exLOr§,(hc%÷Z=@<J9DkqwR_PNSEjM61!U.sp> \\iu}G4Y|o?ÿ$K',
        '\n3>zPy5,w=MTþ&uQ}<EnI]Z4d\\K§V8:2FgN0U9A"rSvami$+f÷eRJ{HY7j-C;/)?6Xq#pb*xDsBc .k\t_`\'L@1O~!t%^o(lhG|ÿ[W',
        '\n3u7$8iv*/2lY^þ§=0VIDf4k,pT(Z5#;Jz:]\'Xy.%+@ex\t[`6÷abM)SQ_9<om~c|RLtAq"-CEhHGN}&>gFOUr{j!1dKns?BPWÿw \\',
        '\n346|TrXmY:lsb^§þjQPo,ty ?@fH\t]V.K&8EF#h\\%daJze<*(÷1q"U;M_70\'NpCBg+!R`A[2nG>xcwSI-{~vk=}9LZO5D$)ÿiWu/',
        '\n3!AIocz>)-d+RU.§Lþ<e(4#&1%tw^Gn/Q\',[K i=Cb]\t}{D0?OT;÷NBl`ZJ7\\Eqya*:hVPuspMgW|25v"SX$FkHY~xm9r@fÿ68_j',
        '\n3PW-8KBYM~!DE5§CZþL0Fp7q(9JOv\'ydA"mV}&ts]k)HiRb?>;.r÷ gGz_%l|\\oQ[n@T:*cS#$U{x1jw+ef,Na`X4h\tu^</ÿI=62',
        '\n3Q!ZsXwfN6A,2devo§)ilþ8}GF|^mW*7\tqD[91EaJ5\\u$_@&gUOn.<÷c](=H%VB ;p-tPLMT\'"`~0h{#+y:b?jR>xkrISz/ÿC4KY',
        '\n3ji$Y(ANldB)K@9y+U§5^p/þsP#_-[:*qeE.\\7;n8<gJ,|XDSwGTZ?÷tc14kmb{~`x6\tRH"QaMrW0>}&v%!=FChIo\'fz ]LÿO2uV',
        '\n3y\\:&Q= JI{R/8`wkO§%,~*vþLl#1)>hTWPcfB5qC.6F<d}GZxn!_M+÷HS]tgE4|a$j7i0"9os\tpmue\'ANb[-^VY2rK?zU@ÿX(;D',
        '\n3${Qe7;YL]y|gz*Ju!w+§C<%=TqþS5N:lG/,-iEk\\p0IA ?_sW(^H9#4÷Rc@Pb~dfBxj\tn6XvU>Khr&D12"8ot}[FO\'Mma.ÿZ`V)',
        '\n3\t~c^$07DwXA?4{mn§]5BK\\\'b=þ`6H&ryYJ/v[kZ>!gG*WxI"%+,Q.}÷ sE)F|d#OpqTuSl9tR_8zhVfL@NCa;-oe1i<:Mjÿ(P2U',
        '\n3Ua21fz\'&+`$rR}#4B§eF<~P,Gyiþ lv^[H*xcA;bZ{gm:uO%W>XY?)_nq÷jKV/ts-J0h@w"\\.C\tDM8EI]oTSp9!k|d5QL6ÿ(7N=',
        '\n3K\\h0iu9GSn;mV}1^[2§r)FzQq\'Z<þ&a5vWH|pAx:t\to{#DwX`T*"O,gR÷ e8+l?dN4U@->Y!cL7b/~(._M]Jj$=BPkfIEsÿyC6%',
        '\n3D+0k)`;zOGMeg@d=cfR]§s"N#A?P4i\\/þrJlq&\'EW}:-|F87\tVC!Z.2Y%÷o, KSu1{<(^hIUavBp$~6Xwyxb*H>t[9n5mLÿjT_Q',
        '\n3dpx~;Uq&)bQ*gAVjv=/]-[D\\tyR§z?8BO_\'>Gþ{$LJ0|2n}XMaF<NY5l,.^#W÷"mEkwP+4:T\t(7Cf hru6%iH@SK9`!cesÿ1IZo',
        '\n3%@"WjT5N)]Rh2M6r.1f>#:[pYiE9HZ_wD|{A+7<B4þ§GyCblPUF*k}Q`08gcnoVt÷sO\'L,/!u-a~^\tdx&=KI$mJzq;Xv (e\\S?ÿ',
        '\n3BG)D<oQOIt-Y8zd,?;:\'|Tpe}VAU!i7 .w$W"SgEb§þq%*#X@R0xyr9`s+h45a÷Fkc^K\t~{26j1=Z>\\(m]N&Jn_lCLHPv/[uMfÿ',
        '\n3:.\'Xh f8a>kyvxM*K;s=I?[cqZ)/@<pW`2(01CA-9o§bþ}YiNj!\t%w^DF~r6J$,U÷+VzBT]Ren5G"#gOS{lQPt&m_udH\\47LE|ÿ',
        '\n3^)0/z#O7\'UNK|w1JoH&I`PxC2cy5$@q9E%-Y?LeRm§tWþl}F!ghQ[sX8G{(:M;6.÷4=_>A+vZÿ"SjT]u,naVfDip\tr\\<bB~dk* ',
        '\n3o4yh>UtVX+?}*(!7m#Iirq5D]J@L\\"Sj2Kfkb:/<z)M=§ B;þ.`{%RZ8n[lYF,waC÷~vAWHd$1ÿe|O-_Esg9Pup0\tN\'GcT&^xQ6'
]

def tmp_clear():
    print('\033[0mRemoving all encryption temp files...')
    os.system('sudo rm -fv /tmp/encryption*.tmp\nsudo rm -fv ~/encryption*.tmp\n# & del /f %temp%\\encryption*.tmp')
    print('Successful.\n')
print('\033[1mPlease check the hash below to keep your data safe.\033[0m\n\033[96m-------------------------------------------------------------------')

# epf = []
epf = open(str(__file__),'r').read()

"""
for i in open(str(__file__),'r').read():
    epf += [str(i).strip('\n')]
"""

edah, edbh, epfa, epfb = (
    __import__('hashlib').md5(str(conv1).encode()).hexdigest(),
    __import__('hashlib').md5(str(conv).encode()).hexdigest(),
    __import__('hashlib').md5(str(epf[0:92]).encode()).hexdigest(), # epfa and epfb calculated manually
    __import__('hashlib').md5(str(epf[175:len(epf)]).encode()).hexdigest()
)

status = '\033[92mPASSED' if orig_hash[0] == edah else '\033[91mFAILED'
print(f'\033[96mEncryption Database A Hash: {__import__('hashlib').md5(str(conv1).encode()).hexdigest()} {status}')
status = '\033[92mPASSED' if orig_hash[1] == edbh else '\033[91mFAILED'
print(f'\033[96mEncryption Database B Hash: {__import__('hashlib').md5(str(conv).encode()).hexdigest()} {status}')
status = '\033[92mPASSED' if orig_hash[2] == epfa else '\033[91mFAILED'
print(f'\033[96mEncryptor Part A Hash:      {epfa} {status}')
status = '\033[92mPASSED' if orig_hash[3] == epfb else '\033[91mFAILED'
print(f'\033[96mEncryptor Part B Hash:      {epfb} {status}')


print('\033[96m-------------------------------------------------------------------')
print(
    '\033[96mHash Status: \033[92mOK'  
    if orig_hash[0] == edah and orig_hash[1] == edbh and orig_hash[2] == epfa and orig_hash[3] == epfb else
    '\033[96mHash Status: \033[91mFAIL'
)
print('\033[96m-------------------------------------------------------------------\033[0m\n')

if orig_hash[0] != edah or orig_hash[1] != edbh:
    i = input('\033[93m[!!] Database does not match the factory hash.\nAs a result, you will get corrupted files.\n Continue? [y,n]: \033[0m')
    if i != 'y':
        print('Exiting.'); exit(2)

if orig_hash[2] != epfa or orig_hash[3] != epfb:
    i = input('\033[93m[!!] Encryptor does not match its factory hash.\nAs a result, your encrypted files may be unsafe.\n Continue? [y,n]: \033[0m')
    if i != 'y':
        print('Exiting.'); exit(3)

if not ( '-e' in __import__('sys').argv or '-d' in __import__('sys').argv or '-r' in __import__('sys').argv ):
    tmp_clear()
    i = input('e to encode, d to decode or r to run encoded program [e,d,r]: ')
else: i = list(str(__import__('sys').argv[1]))[1]
if i == 'e' or '-e' in __import__('sys').argv:
    if not '-e' in __import__('sys').argv:
        i = input('file: ')
        fi = open(file=i,mode='r',encoding='utf-8')
        o = input('output file (create new, *.amns recommended): ')
        fo = open(file=o,mode='w',encoding='utf-8')
    else:
        i = __import__('sys').argv[2]
        o = __import__('sys').argv[3]
        fi = open(file=i,mode='r',encoding='utf-8')
        fo = open(file=o,mode='w',encoding='utf-8')
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    fails = 0
    fbytes = 0
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}, {fails} corrupted blocks, {fbytes} corrupted bytes')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[list(conv[a])[i]] = conv1[i]
        preresult = ""
        isfail = False
        for b in range(len(str(last))):
            try:
                preresult += conv2[list(str(last))[b]]
                bar.update(1)
            except:
                fails += 1
                isfail = True
        last = preresult
        result = str(preresult)
        if isfail: fbytes += len(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}, total {fails} corrupted blocks, total {fbytes} corrupted bytes')
    fo.write(result)
    bar.close()
    print('compiled.')
    if fails != 0: print(f'\033[93m[!!] {fbytes} bytes in {fails} blocks has been found as corrupted!\033[0m')
elif i == 'd' or '-d' in __import__('sys').argv:
    if not '-d' in __import__('sys').argv:
        i = input('file: ')
        fi = open(file=i,mode='r',encoding='utf-8')
        o = input('output file (create new): ')
        fo = open(file=o,mode='w',encoding='utf-8')
    else:
        i = __import__('sys').argv[2]
        fi = open(file=i,mode='r',encoding='utf-8')
        o = __import__('sys').argv[3]
        fo = open(file=o,mode='w',encoding='utf-8')
    conv.reverse()
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    fails = 0
    fbytes = 0
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}, {fails} corrupted blocks, {fbytes} corrupted bytes')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[list(conv[a])[i]] = conv1[i]
        preresult = ""
        isfail = False
        for b in range(len(str(last))):
            try:
                preresult += conv2[list(str(last))[b]]
                bar.update(1)
            except:
                fails += 1
                isfail = True
        last = preresult
        result = str(preresult)
        if isfail: fbytes += len(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}, total {fails} corrupted blocks, total {fbytes} corrupted bytes')
    fo.write(result)
    bar.close()
    print('compiled.')
    if fails != 0: print(f'\033[93m[!!] {fbytes} bytes in {fails} blocks has been found as corrupted!\033[0m')
elif i == 'r' or '-r' in __import__('sys').argv:
    if not '-r' in __import__('sys').argv: i = input('file: ')
    else: i = __import__('sys').argv[2]
    fi = open(file=i,mode='r',encoding='utf-8')
    o = f"encryption{__import__('random').randint(114514,0x1919810)}.tmp"
    fo = open(file=o,mode='w',encoding='utf-8')
    conv.reverse()
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    fails = 0
    fbytes = 0
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}, {fails} corrupted blocks, {fbytes} corrupted bytes')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[list(conv[a])[i]] = conv1[i]
        preresult = ""
        isfail = False
        for b in range(len(str(last))):
            try:
                preresult += conv2[list(str(last))[b]]
                bar.update(1)
            except:
                fails += 1
                isfail = True
        last = preresult
        result = str(preresult)
        if isfail: fbytes += len(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}, total {fails} corrupted blocks, total {fbytes} corrupted bytes')
    fo.write(result)
    bar.close()
    print('compiled.')
    if fails != 0: print(f'\033[93m[!!] {fbytes} bytes in {fails} blocks has been found as corrupted!\033[0m')
    if not ( '-e' in __import__('sys').argv or '-d' in __import__('sys').argv or '-r' in __import__('sys').argv ):
        lang = None
        lang = input('enter compiler path or command (example: py, ipython3, java): ')
        if lang == None or lang == '': lang = 'python'
        para1 = input('enter parameter before filename. if no, type nothing and continue: ')
        para2 = input('enter parameter after filename. if no, type nothing and continue: ')
    else:
        try: lang = __import__('sys').argv[3]
        except: lang = 'python'
        try: para1 = __import__('sys').argv[4]
        except: para1 = '' 
        try: para2 = __import__('sys').argv[5]
        except: para2 = ''
        if para1 == 'none' or para1 == 'None': para1 = ''
        if para2 == 'none' or para2 == 'None': para2 = '' 
    # print(f'program launch command: {lang} {para1} {o} {para2}')
    fo.close()
    os.system(f'mv {o} /tmp/{o} \n# & move {o} %temp%\\{o}')
    os.system(f'{lang} {para1} /tmp/{o} {para2} # & start wt {lang} {para1} %temp%\\{o} {para2}')
    
# Ctrl+K+U to remove note 
# Ctrl+K+C to add note