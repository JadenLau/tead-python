from tqdm.rich import tqdm # progress bar

conv1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\n\tÿþ'
conv = [
        '3þCSQNF8Ldg\'20)T^{z§R6kbZ%Y:#]}<1,+~\tWec@nX\nqBGPl_r|DhvOo9Js;Hyt(A5.pi\\E`f>[M4-"w!? $mu&*7aKjIUV/ÿx=',
        '3lgþLP5AQnfJ/zRaH=§6Seq2E1,\tB8r({jid\n0kZo&:$-t*V|;vDU!9[Gb\'s}NO\\ph+^mcW_TF%Xu>Y"`#I~<C.y7?w 4M@x)ÿ]K',
        '31?rJþR-/`o5g~VYL,X§xmsBjHW0;NZ!&9\\]n4\'kdt|%^O[liA.*}fTMG8c$>:KUev ywIS_pQb2+")({\n\tq@hzPuC#=E76FDÿ<a',
        '3X"VU/qþ,%+i:\n$vlxG_§az\\<hEc|Wb)L&sJCjtDMp6;A-F40\t QH2yI8fgwn5R]k^*oZP(`T>dN[}SKm1#=eru@\'?O7.{!9Yÿ~B',
        '3\n*bHn)tþzF+mv8CQA5B:2ga[T\'"\tl;{f#Wdy]&-I0^7`X/V~exLOr§,(hc%Z=@<J9DkqwR_PNSEjM61!U.sp> \\iu}G4Y|o?ÿ$K',
        '3>zPy5,w=MTþ&uQ}<EnI]Z4d\\K§V8:2FgN0U\n9A"rSvami$+feRJ{HY7j-C;/)?6Xq#pb*xDsBc .k\t_`\'L@1O~!t%^o(lhG|ÿ[W',
        '3u7$8iv*/2lY^þ§=0VIDf4k,pT(Z5#;Jz:]\'Xy.%+@ex\n\t[`6abM)SQ_9<om~c|RLtAq"-CEhHGN}&>gFOUr{j!1dKns?BPWÿw \\',
        '346|TrXmY:lsb^§þjQP\no,ty ?@fH\t]V.K&8EF#h\\%daJze<*(1q"U;M_70\'NpCBg+!R`A[2nG>xcwSI-{~vk=}9LZO5D$)ÿiWu/',
        '3!AIocz>)-d+RU.§Lþ<e(4#&1%tw^Gn/Q\',[K i=Cb]\t}{D0?OT;NBl`ZJ7\\Eqya*:hVPuspMgW|25v"SX$FkHY~\nxm9r@fÿ68_j',
        '3P\nW-8KBYM~!DE5§CZþL0Fp7q(9JOv\'ydA"mV}&ts]k)HiRb?>;.r gGz_%l|\\oQ[n@T:*cS#$U{x1jw+ef,Na`X4h\tu^</ÿI=62',
        '3Q!ZsXwfN6A,2devo§)ilþ8}GF|^mW*7\tqD[91EaJ5\\u$_@&gUOn.<c](=H%VB ;p-tPLMT\'"`\n~0h{#+y:b?jR>xkrISz/ÿC4KY',
        '3ji$Y(ANldB)K@9y+U§5^p/þsP#_-[:*qeE.\\7;n8<gJ,|\nXDSwGTZ?tc14kmb{~`x6\tRH"QaMrW0>}&v%!=FChIo\'fz ]LÿO2uV',
        '3y\\:&Q= JI{R/8`wkO§%,~*vþLl#1)>hTWPcfB5qC.6F<d}GZxn\n!_M+HS]tgE4|a$j7i0"9os\tpmue\'ANb[-^VY2rK?zU@ÿX(;D',
        '3${Qe7;YL]y|gz*Ju!w+§C<%=TqþS5N:lG\n/,-iEk\\p0IA ?_sW(^H9#4Rc@Pb~dfBxj\tn6XvU>Khr&D12"8ot}[FO\'Mma.ÿZ`V)',
        '3\t~c^$07DwXA?4{mn§]5BK\\\'b=þ`6H&ryYJ/v[kZ>!gG*WxI"%+,Q.\n} sE)F|d#OpqTuSl9tR_8zhVfL@NCa;-oe1i<:Mjÿ(P2U',
        '3Ua21fz\'&+`$rR}#4B§eF<~P,\nGyiþ lv^[H*xcA;bZ{gm:uO%W>XY?)_nqjKV/ts-J0h@w"\\.C\tDM8EI]oTSp9!k|d5QL6ÿ(7N=',
        '3K\\h0iu9GSn;mV}1^[2§r)\nFzQq\'Z<þ&a5vWH|pAx:t\to{#DwX`T*"O,gR e8+l?dN4U@->Y!cL7b/~(._M]Jj$=BPkfIEsÿyC6%',
        '3D+0k)`;zOGMeg@d=cfR]§s"N#A?P\n4i\\/þrJlq&\'EW}:-|F87\tVC!Z.2Y%o, KSu1{<(^hIUavBp$~6Xwyxb*H>t[9n5mLÿjT_Q',
        '3dpx~;Uq&)bQ*gAVjv=/]-[D\\tyR§z?8BO_\'>Gþ{$LJ0|2n}XMaF<NY5l,.^#W"mEkwP+4:T\t(7Cf hru6%\niH@SK9`!cesÿ1IZo',
        '3%@"WjT5N)]Rh2M6r.1f>#:[pYiE9HZ_wD|{A+7<B4þ§GyCblPUF*k}Q`08gcnoVtsO\'L,/!u-a~^\tdx&=KI$mJzq;Xv (\ne\\S?ÿ',
        '3BG)D<oQOIt-Y8zd,?;:\'|Tpe}VAU!i7 .w$W"SgEb§þq%*#X@R0xyr9`s\n+h45aFkc^K\t~{26j1=Z>\\(m]N&Jn_lCLHPv/[uMfÿ',
        '3:.\'Xh f8a>kyvxM*K;s=I?[cqZ)/@<pW`2(01CA-9o§bþ}YiNj!\t%w^DF~r6J$,U+VzBT]Ren5G\n"#gOS{lQPt&m_udH\\47LE|ÿ',
        '3^)0/z#O7\'UNK|w1JoH&I`PxC2\ncy5$@q9E%-Y?LeRm§tWþl}F!ghQ[sX8G{(:M;6.4=_>A+vZÿ"SjT]u,naVfDip\tr\\<bB~dk* ',
        '3o4yh>UtVX+?}*(!7m#Iirq5D]J@L\\"Sj2Kfkb:/<z)M=§ B;þ.`{%RZ8n[lY\nF,waC~vAWHd$1ÿe|O-_Esg9Pup0\tN\'GcT&^xQ6'
    ]
print('\033[1mPlease check the hash below to keep your data safe.\033[0m\n\033[96m-------------------------------------------------------------------')
orig_hash = [
    'b0a598ec31acaf239cf4de399ec2f520',
    '7863017f7872d3a4fa8b3f3f79baec4a',
    'e59b46d8ba7fa31b9f2cd3d48d72495b'
]
edah, edbh, eph = (
    __import__('hashlib').md5(str(conv1).encode()).hexdigest(),
    __import__('hashlib').md5(str(conv).encode()).hexdigest(),
    __import__('hashlib').md5(str(open(__file__,'r')).encode()).hexdigest()
)

status = '\033[92mPASSED' if orig_hash[0] == edah else '\033[91mFAILED'
print(f'\033[96mEncryption Database A Hash: {__import__('hashlib').md5(str(conv1).encode()).hexdigest()} {status}')
status = '\033[92mPASSED' if orig_hash[1] == edbh else '\033[91mFAILED'
print(f'\033[96mEncryption Database B Hash: {__import__('hashlib').md5(str(conv).encode()).hexdigest()} {status}')
status = '\033[92mPASSED' if orig_hash[2] == eph else '\033[91mFAILED'
print(f'\033[96mEncryption Program Hash:    {__import__('hashlib').md5(str(open(__file__,'r')).encode()).hexdigest()} {status}')
print('\033[96m-------------------------------------------------------------------')
print(
    '\033[96mHash Status: \033[92mOK' 
    if orig_hash[0] == edah and orig_hash[1] == edbh and orig_hash[2] == eph else
    '\033[96mHash Status: \033[91mFAIL'
)
print('\033[96m-------------------------------------------------------------------\033[0m\n')

i = input('e to encode, d to decode or r to run encoded program [e,d,r]: ')
if i == 'e':
    i = input('file: ')
    fi = open(file=i,mode='r',encoding='utf-8')
    o = input('output file (create new): ')
    fo = open(file=o,mode='w',encoding='utf-8')
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[conv1[i]] = list(conv[a])[i]
        preresult = ""
        for b in range(len(str(last))): # convert original to encrypted
            preresult += conv2[list(str(last))[b]]
            bar.update(1)
        last = preresult
        result = str(preresult)
        print(f'data length written: {len(preresult)}')
    fo.write(result)
    bar.close()
    print('done.')
elif i == 'd':
    i = input('file: ')
    fi = open(file=i,mode='r')
    o = input('output file (create new): ')
    fo = open(file=o,mode='w')
    conv.reverse()
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[list(conv[a])[i]] = conv1[i]
        preresult = ""
        for b in range(len(str(last))):
            preresult += conv2[list(str(last))[b]]
            bar.update(1)
        last = preresult
        result = str(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}')
    fo.write(result)
    bar.close()
    print('done.')
elif i == 'r':
    i = input('file: ')
    fi = open(file=i,mode='r')
    o = f"encryption{__import__('random').randint(114514,0x1919810)}.tmp"
    fo = open(file=o,mode='w')
    conv.reverse()
    fi = fi.read()
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            conv2[list(conv[a])[i]] = conv1[i]
        preresult = ""
        for b in range(len(str(last))):
            preresult += conv2[list(str(last))[b]]
            bar.update(1)
        last = preresult
        result = str(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}')
    fo.write(result)
    bar.close()
    print('compiled.')
    lang = input('enter compiler path or command (example: py, ipython3, java): ')
    para = input('enter start parameter. if no, type nothing and continue: ')
    print(f'program launch command: {lang} {para} <compiled_output>')
    __import__('os').system(f'{lang} {para} {result}')

# Ctrl+K+U to remove note
# Ctrl+K+C to add note