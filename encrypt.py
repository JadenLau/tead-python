orig_hash = [
    '12bdfe19810f5ac3f04a71106f48b679',
    'aeffd2b49bcb94fd5669b94d5475c20a',
    'b063f11d615447a5e496b1f78f4cbde7',
    '9e6a00d61d6bac79e88d2f792bf96c05'
] # DO NOT CHANGE ORIGINAL HASH UNLESS DATABASE IS UPDATED
from tqdm.rich import tqdm # progress bar
import os
import sys

# AMNS Compiler
conv_loader = 4

if conv_loader == 1: 
    conv = ['\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\tÿþ÷']
    conv1 = '\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\tÿþ÷'

if conv_loader == 2:
    conv = ['\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ;:,.!? "']
    conv1 = '\ntuvwxyzabcdefghijklmnopqrsTUVWXYZABCDEFGHIJKLMNOPQRS;:,.!? "'

if conv_loader == 3:
    conv = [
        '\nji$Y(ANldB)K@9y+U§5^p/þsP#_-[:*qeE.\\7;n8<gJ,|XDSwGT3Z?÷tc14kmb{~`x6\tRH"QaMrW0>}&v%!=FChIo\'fz ]LÿO2uV',
        '\ny\\:&Q= JI{R/8`wkO§%,~*vþLl#1)>hTWPc3fB5qC.6F<d}GZxn!_M+÷HS]tgE4|a$j7i0"9os\tpmue\'ANb[-^VY2rK?zU@ÿX(;D',
        '\n${Qe7;YL]y|gz*Ju!w+§C<%=TqþS5N:lG/,-iEk\\p0IA ?_sW(^H9#4÷Rc@Pb~dfBx3j\tn6XvU>Khr&D12"8ot}[FO\'Mma.ÿZ`V)',
        '\n\t~c^$07DwXA?4{mn§]5BK\\\'b=þ`6H&ryYJ/v[kZ>!gG*WxI"%+,Q.}÷@sE)F|d#OpqTuSl9tR_8zhVfL NCa;-oe1i<:Mjÿ(P23U'
    ]
    conv1 = '\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\tÿþ÷'

if conv_loader == 4:
    conv = ['\nabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 `~!@#$%^&*()-=_+[{]}\\|;:\'",./<>?§\tÿþ÷']
    conv1 = 'tlM,)of2þy{~LU0z6sA%\'&e<]HE"`BdY/14u@CFh8TmD!÷rP:|37}$.i# (>kJO\tp§Vw?n[vcRb5SNW+^*\nÿajXGZ;K\\g_qIQ9=-x'

# old: 0 (dead)
# new: 1
# custom: 2+

if conv_loader == 0:
    conv = [
        '\n3þCSQNF8Ldg\'20)T^{z§R6kbZ%ąæãàáåâā,+~\tWec@näǎăGPl_r|DhvOo9Js;Hyt(A5.pi\\E`f>[M4-"w!? $mu&*7aKjIUV/ÿx=÷',
        '\n3lgþLP5AQnfJ/zRaH=§6Seq2E1,\tB8r({jid0kZo&:$-t*V|€;vDU!9[Gb\'s}NO\\ph+^mcW_TF%Xu>Y"`#I~<C.y7?w 4M@x)ÿ]K÷',
        '\n31?rJþR-/`o5g~VYL,X§xmsBjHW0;NZ!&9\\]n4\'kdt|%^O[liA.*}fTMG8c$€>:KUev ywIS_pQb2+")({\tq@hzPuC#=E76÷FDÿ<a',
        '\n3X"VU/qþ,%+i:$vlxG_§az\\<hEc|Wb)L&sJCjtDMp6;A-F40\t QH2yI8fgwn5R]k^*oZP(`T>d€N÷[}SKm1#=eru@\'?O7.{!9Yÿ~B',
        '\n3*bHn)tþzF+mv8CQA5B:2ga[T\'"\tl;{f#Wdy]&-I0^7`X/V~exLOr§,(hc%€÷Z=@<J9DkqwR_PNSEjM61!U.sp> \\iu}G4Y|o?ÿ$K',
        '\n3>zPy5,w=MTþ&uQ}<EnI]Z4d\\K§V8:2FgN0U9A"rSvami$+f÷eRJ{HY7j-C;/)?6Xq#pb*x€DsBc .k\t_`\'L@1O~!t%^o(lhG|ÿ[W',
        '\n3u7$8iv*/2lY^þ§=0VIDf4k,pT(Z5#;Jz:]\'Xy.%+@ex\t[`6÷abM)SQ_9<¥£°ëķâLtAq"-CEhHG€N}&>gFOUr{j!1dKns?BPWÿw \\',
        '\n346|TrXmY:lsb^§þjQPo,ty ?@fH\t]V.K&8EF#h\\%daJze<*(÷1q"U;M_70\'NpCBg+!R`A[2nG>xcw€SI-{~vk=}9LZO5D$)ÿiWu/',
        '\n3!AIocz>)-d+Rźż§Lþ<e(4#&1%tw^Gn/Q\',[K i=Cb]\t}{D0?OT;÷NBl`ZJ7\\Eqya*:hVPuspMgW|2€5v"SX$FkHY~xm9r@fÿ68_j',
        '\n3PW-8KBYM~!DE5§CZþL0Fp7q(9JOv\'ydA"mV}&ts]k)HiRb?>;.r÷ gGz_%l|\\oQ[n@T:*cS#$U{x1jw+€ef,Na`X4h\tu^</ÿI=62',
        '\n3Q!ZsXwfN6A,2devo§)ilþ8}GF|^mW*7\tqD[91EaJ5\\u$_@&gUOn.<÷c](=H%VB ;p-tPLMT\'"`~0h{#+€y:b?jR>xkrISz/ÿC4KY',
        '\n3ji$Y(ANldB)K@9y+U§5^p/þsP#_-[:*qeE.\\7;n8<gJ,|XDSwGTZ?÷tc14kmb{~`x6\tRH"QaMrW0>}&v%€!=FChIo\'fz ]LÿO2uV',
        '\n3y\\:&Q= JI{R/8`wkO§%,~*vþLl#1)>hTWPcfB5qC.6F<d}GZxn!_M+÷HS]tgE4|a$j7i0"9os\tpmue\'€ANb[-^VY2rK?zU@ÿX(;D',
        '\n3${Qe7;YL]y|gz*Ju!w+§C<%=TqþS5N:lG/,-iEk\\p0IA ?_sW(^H9#4÷Rc@Pb~dfBxj\tn6XvU>Khr&D1€2"8ot}[FO\'Mma.ÿZ`V)',
        '\n3\t~c^$07DwXėěêèéëęē5BK\\\'b=þ`6H&ryYJ/v[kZ>!gG*WxI"%+,Q.}÷ sE)F|d#OpqTuSl9tR_8zhVfL€@NCa;-oe1i<:Mjÿ(P2U',
        '\n3Ua21fz\'&+`$rR}#4B§eF<~P,Gyiþ lv^[H*xcA;bZ{gm:uO%W>XY?)_nq÷jKV/ts-J0h@w"\\.C\tDM8EI]€oTSp9!k|d5QL6ÿ(7N=',
        '\n3K\\h0iu9GSn;mV}1^[2§r)FzQq\'Z<þ&a5vWH|pAx:t\to{#DwX`T*"O,gR÷ e8+l?dN4U@->Y!cL7b/~(€._M]Jj$=BPkfIEsÿyC6%',
        '\n3D+0k)`;zOGMeg@d=cfR]§s"N#A?P4i\\/þrJlq&\'EW}:-|F87\tVC!Z.2Y%÷o, KSu1{<(^hIUavBp$~6€Xwyxb*H>t[9n5mLÿjT_Q',
        '\n3dpx~;Uq&)bQ*gAVjv=/]-[D\\tyR§z?8BO_\'>Gþ{$LJ0|2n}XMaF<NY5l,.^#W÷"mEkwP+4:T\t(7Cf hr€u6%iH@SK9`!cesÿ1IZo',
        '\n3%@"WjT5N)]Rh2M6r.1f>#:[pYiE9HZ_wD|{A+7<B4þ§GyCblPUF*k}Q`08g€cnoVt÷sO\'L,/!u-a~^\tdx&=KI$mJzq;Xv (e\\S?ÿ',
        '\n3BG)D<oQOIt-Y8zd,?;:\'|Tpe}VAU!i7 .w$W"SgEb§þq%*#X@R0xyr9`s+h4€5a÷Fkc^K\t~{26j1=Z>\\(m]N&Jn_lCLHPv/[uMfÿ',
        '\n3:.\'Xh f8a>kyvxM*K;s=I?[cqZ)/@<pW`2(01CA-9o§bþ}YiNj!\t%w^DF~€r6J$,U÷+VzBT]Ren5G"#gOS{lQPt&m_udH\\47LE|ÿ',
        '\n3^)0/z#O7\'UNK|w1JoH&I`PxC2cy5$@q9E%-Y?LeRm§tWþl}F!ghQ[sX8G{(:€M;6.÷4=_>A+vZÿ"SjT]u,naVfDip\tr\\<bB~dk* ',
        '\n3o4yh>UtVX+?}*(!7m#Iirq5D]J@L\\"Sj2Kfkb:/<z)M=§ B;þ.`{%RZ8n[l€YF,waC÷~vAWHd$1ÿe|O-_Esg9Pup0\tN\'GcT&^xQ6'
    ]


# conv = [
#     'c wbAK|x:4I]-),<%=\~"^>*1`\', '7S,Kd[f]}=O\'<8PNv*$&(:RIW/)X%`A@3rt\\Y6pu!w0; ME#m+4Gj1iJq|eT§xþoUgFh{_-cQ29kbValH5nz?ÿ>CLsy\tD.^~\n÷"BZ', '%7÷-}LKIvxa>3($~O[{*=f1G&dgrH@\n?qpÿ|Y^AQFeJE<UlN"9+TsCV\tkS8 oZWy\\D0!6þ`,\'§_;2MiBwjnbmz)/4]ucXP#:Rt5.h', 'vW\'awdc\\m-FEsLbY/r2A|KG=ZC@6UHJ]f}X[RTQ"?Sq8,#n5;4ODBþ(9lo&INtV\n`P:eg<_i>3^k.{1!ÿj0\t%yzh x÷+*u7p$M)§~', 'R2\n{\\$Z:"V^ÿ4\t÷,m\'O80U]Tj1F(_?nc5[d!DA>z.6HG)q fwN|La9EeC/§tBXr7QhPSþl+Ib=iu}-~xp%*#g@yWk3s;JKMo&Y`<v', 'hY3_|21Opt0#sQ~eb§+oKCn.g\n\t@";?54&(`6j v>{þfz$%P9GXH÷^ÿq,U*)=LwkDBR\\[}/xTd:yacm<E8u]WJI!F\'lVrMS7AZ-iN', '{T&$Zc,\ts Fq:zV\'?YEu5<Of\n#GDx~kUn`=mCþwQd>3R9^SHW[Keth+"jLl6÷§X(\\iMo]aNB_/0-.1J}rg*2Ivb47%;)!@PA|8ÿyp', 'i\tJ,Ubptu/H\nF9!+h7{?4leM^V_2dw&(GT§O\\@1$KÿL\'~fC6BESþ>÷R:<=vI[kD-`|oz)q.;*}j PyZYQN8gxaW503Ac#Xn%m"]sr', '5TWaK8Ct÷3\n_</H(pmwUJAZ2lVb "^j§9cON,o&PL.ig0\'G4x*)I7\t#:|qnÿvf]$Xz@y+}M=`k1þQRSe;%hF>{d?s!\\-Y6rD~Eu[B', 'M;X`PhQG\nd*/TL}ZI(41"÷k9z!7mNx\'So%|De@§<#[:\tru8g3c_q6iÿ.v=+pwRlH^- FKþAnfs\\&BY,VC2ab?0OEJW~)$]>j5y{tU', '{@N1;:7=O§Ji.EkXx Ad$m>fqB÷oW6D^bt&u,\'93FwK~g]ÿhsze`\nC+8Rcy4YprLT<Uj)-v_PlGV0(n!Z\\5þM?}|%/\t#"HSQ[a*2I', 'DEBefOpYjUaTW9(}1C8L3&Q`Z#d_G,kx5 q|A*X>hI%ÿN\'<þ\\÷§{o!"P.-MSz;+:7\n]/\tcFJlygRn?)b04ms[$vi=rVtK2u^H@~6w', 'Z\nH\'Xþ8lK#!>%2 qUi\tR3MgFNjT:÷]V`r?~;,5t*mcLCSW-JD(<v@+x$s}n[w7{eIbOzkAoQ^/f1|\\d6a§p_)E&h9B=0.u4yÿP"YG', 'XZ$q|<y80t{HuY}Pa[w:DN2m@,JR)*f5Ubÿ3~1kQT6þ.hpxl-\tKM 4§?ns^;÷S\nW=7zj#(v&\\gi/_d9EC>%]eArO!`IFGB"ocL\'+V', 'z0÷yZpxC1@+QWR!9$XL;6j?7Tu,<HYti[v \n~o{I\\GOSaB&m*U`/3h_NbEAfk4\t2s\'q%nwÿg"d)-lMc8D§Jr}F]PV|^=e(>#5:Kþ.', '9fp$%47qþ:3\t\\?tN>=PK<X§!U\nkhRJGW~\'jSw/-DOeudA÷H2s0l}`EMrTxic5[bYyz&.]^F@;,)ÿa1v" +g(|L{I#oV6B*C_mZ8nQ', 'h.÷u>3E~iw9vY#?$gXG[\'þA8LzmBQd§0_JT<RZ;q|CpN^HSnoO\t:6M`\n-f1%2sx5*"j=b!F{Pÿ&7@a()V}c+\\U/IKk ]Dtey,4rlW', ',joH$\nECsN|@VFK7I4^\'c?p.Uÿ~=!n÷f)QdmxXJW*2w`:\\\tDzS%T§];0AhP[_Mvt+qBGe1Z&i}6Y/l8ku ra>gLþ"5R3#y-O(9<{b', ' F{^3PjTbZ6y9>@5J+kei*~\'?D-p"CSG.$2Kha}fH\\dz,]8U:mrWl7|oqR&EM\tOQcÿV!Y§s%[þn1#B_NtAX/v)uI<4=w÷`g0;x\n(L', '}?+/M-3&*\'mzN^[I@bs0uW7B%hpQP5i]>T!#þF~rnOÿ{=,4yU1÷(V"XqS<g`_;Dt2 .8owAkL:H\nCc6Yd\\Z\txEfR|KlGa§$vJ9)ej', 'V§4NS@_%j"Ty`\':~Zs2^A\tzv*ÿbrh8E<Qw!a9knCM6eg]7p;Hm|loK)qD=IO\\P,[#-X÷Y0}&/?+RG>$\nfþ13LUc(.dt{W JBi5Fxu', 'P*kh^_w/D[b%~`t#SGW4|AÿHiR\tJ2"MzrXE3j&5f8a:@>Bþ1dyeKF$+(TN]!§Q=,÷c{m\\ug;\'7Ox6-nIvV\n?<sp0Y9}qLU. )ClZo', 'Et:\\þ/"y{IkF^&§!SX@jbQ\tU$RKD|\'w[pBGoÿ*Y÷M<`u%dC}W-( Osi57+>\nl;xmc~a0zr,N3f)ZH2Tq?V]nA=PJhLv1#6eg.84_9', '§ >dPlBG%YHC2oDx9Fs0krb3yuO+){NXc6g.jpRÿh,wE;eWMUL5]#8$Q7"4q}v\\KJ÷\'at:&~@/!-Z<`*|I1in(ST[^z=m?fAþV\t\n_', '/iDB}Lt^þ52hz4<y\'K#:&E*`l!\n=dCw |_[-@XJfIHc~VW÷ok%79v)a8,0§1eYgGm3\\xQqNZ">\tU;sTÿnuRO(AM]jSF{?6+rbpP$.', 'R{þC"tLM%÷lQ+&§ÿYHO}<TP\t|U9fG2anZ\nd:yp5$3o@1)]u~XBzI;[?EK-> `w*#6NS=jJe48m^srb.i,q\\xWDvFk0g_V7\'/h!A(c', ',p§kYaSl!O];goB-hÿ}iQVx"4vc=&TG28$j6yt/1ZF%*|HDX#NM5E?r\\7Aef^\'d_LI>u{Pzmw÷þ 9WJ`snR~q[<bU03)+C(\t.K\n@:', '#gscIRAD8o1;mr?M{fH+UZ}/ÿXG)h=><j:Bbxv§F[_lW-\t6e5z`%TO*4þSyNt n&qL"aP^k|uQ,0p(9J7]~$d@iE2K\\CV\'!.÷\nY3w', '=Dht÷{T(^y)\'rcG"UJ:M75Y9W,;n\\`fZ?$+~xE>q*}|FKA<þBg1.@zÿjk[dw_b3aiN0ICVs#X-\n2H]e/8&!LP\t§ SoQm46%pRvluO', 'ZHztAhWvOl,iaPUÿ}T>9)*$2r\tY0+-_3Jxfe?MEBQm@:{"Rq#§CK/D[1<8nGd(k.5X7~s|=u%\'b]4;o ÷N!I^þVL`\\ySFc&6\njgpw', 'tSR|"\\4XF&}0rn>!?DcabQ[8*÷{Z<$]iIp1þG/`\'9)7,\tsl^z§fkCWVv#u\n OBq56jP@_=e(YÿN+EgKMA:~m23yHh-T.odx;wJ%UL', 'VsaC5bqg>^TQ!\ndþr46w,Lln13NP§fz"K\'];kÿDphA| e}o?ciR+U-*÷HJ)_WI{Z@9X:$m=\t[%8\\2yxEtOB~Y7<M#SGF.0/(`v&ju', 'f/jiSþ(p^6`&9x51lCaÿvn|T_z§8Ht@BGURW=u#N;egq>PM.EAcJyhd~Z\t)[]s{÷+%4Yr7b\\\'*0L"OX3mw ?:IK2Vk}o-,\nFQ$D!<', 'qÿbJW\t.=?Z-Dwl,~/!\\GovHNRa8L"E+[u4A)xm;i*k|]z(Kh3g2CIFn_ScB&:UQe^\'t0T57`6$VdPOYrM1÷y@9þs§X\n}>#p{ f%j<', ';yI/\nhA?s.}K{4FcYpÿO@:k81%_PN)QL#5U6mjg|&VqxC\'!D§>r<2wnS"Wil+XRZ a\t,^zEMHbf7]Gþ\\oT$(t[=9du0e÷vJ*B-~3`', '7#z\'fCÿK|lM+p nG5&_h2RQaLt.B9Z"`V${HEgrAD\\÷^§/y3w*?1uJ(kqej-N0~S\t8[x;P%)IiTs6oFþ:}\nOU]WX=m!cd<@v>Yb4,', 'iOy=|9r<`DpnA,WMg!KIþb*@v$Hlt\t>§{05X:q]#sx)fde_/FVC~^Y};cÿP8J÷\'aR"L[-Eh21G6T3uB.Z%N7w\\+(&z\n 4mkSjUQ?o', 'Ilj!&$8w\nBXP[_`,Q}5mG4xi-O\'bÿMh<@:þ9/Eg3]?ZDvC*H#zcya;0(J%K+)u.\\Y|N^A=os\tp>t21RLSnqfrUWdVF{e"÷7§kT~6 ', 'X$1Q[6*PGf\\pY(43@g&>j=Kl)?mNaLW§0-}+eOMR;!wiy]Tuzr\t`vB<ctA,noVCEdH7÷D\nZ8I59|2^"S#q/hFþ%s{:b_~\'.ÿx UJk', 'yYJbþkKc%F\\~0"M84e§&(3!Pz.#O)\'÷/+H=, _$vopxAd<`D:Ba1|l5EhXW;}@-TI]CQ\ntNquwV*ÿs[mGrLn^gfU{>9?S26j7ZR\ti', 'G`m=98IY-?4Z&#>Tn!3/V0J5§(.Ca"yB2,:jQub|XDÿf6EUcO~LK÷*\\iro_wHk<xgt;s17lFþ\n\'pdWR}M{%h N+\t$v]q[AS^)P@ez', '2gnV6QK3#\n<l%aH;t>.Yh0|bL@jprmþdAM!O5kcZNI)[Ef}CF+8^9DPx(`/s\'_u?U1"w TB]§-\tRo÷,4*WyS:v~qz7i=$ÿ\\GeJ{&X', 'a#DY/u+þEV)ptdTN3h\' =lkXq>M.@]ILiz&y;1e!-7:P?fF69O<U[Gÿ\\,`\nZx÷B_*~JHr8bwvACR(}S|5o{Q4K^mjW2§\t"0ns%g$c', 'gPrM÷H =KOm|@2`136fI#%ncEo(4u{XU}sRW5Z:<SBlCtz-NþG_9&/"].*\tÿqw;\n\'p!?Fa0T>d+jL8)VvJe~A[Q$i\\^§xD7ykbYh,', '÷\n#+k|VCf9[cjuOP.KBql\\ThUiY\t/z-;62@\'m "HIreMD5d&F*)G$waJSpy`7QvL§1A=3,<!oRþ?0nN(~X%^tEsbZÿ}_xW]:48{g>', 'n:2gTzav/,{3\nt.P-|\\)FwS_?~o"+1EXþbm6^`k\tDx]#[7(*fMqHAsG=V!UW8}KRu%§0÷Oe 4ihY$9J<Qry@>Z;CNB\'jI5&lLdÿcp', 'I=*s§68r1\nq_D,mVe\'^hFYK:nc[÷(?JA)uv/>94Wl@x|\tO\\#RaHC& {2wp"<i$XMg~U+PT-57.tL3}ZkbSBdG%!ojE0y;]zÿNQfþ`', '!;(T9þ%s*E=wF8,v2xhkXu|M^0G#:3K7S<V5\n6pRt4i`cZWq"P.$Y{ÿrLfna[§lJ&+)b1C÷zmd-\\\tN}OAUjQg@H?IoB\'_]~ye/ D>', '§HaDk\te1{M4WJZpx<U#wFd@RV=\'NStv-nAz6)QT5}[c>!j8%bOþ~]CBmI07|\ngEqoiÿ\\rYPf;"L $/3l(:÷h&+,XG^?9uK_sy`.2*', 'q2\\Xy=N%KW_QP^9Fþj{sC*M-,m]dJ1b§6I\n)[U5:+Af.~|h\t4?ÿ"w$pL!/0T÷Y}3tSBauc lre<\'ZOovDV&GH(7x@>;k`n8Eig#zR', '[J%;pW!+vebw1gE÷$=fAH:P/]\nu(V§4a5G<@qr}39ÿ,Cx2X>8Y-sij7z0R|"*~#k)`^B6dhtoDM&TK.Qc?y_mSO\\þ\'IN{Z\t FLnlU', '3w1zG#?OVc-ta_b2Hq+dNC§pD6}"u\'|j*vÿ58g;,x70B$[]J Qy`sþ<@%&:\t\n9rA~hL4)FWKT>/=klioIZR!÷efSUP^EM(n\\Y{mX.', 'GHr=§a0&v]m\\Xpd[{ex.B?h;bVY_÷kEft8|TuoW<$z#ÿC>OD*K}\'-6w:/l2qc!7Ai`)LQþZ@^(P S1"+FUn\n94IyNJ\t53R,Mj%g~s', 'GTixh]~PRd!þ\ty§5;pLl3S$g./bEK2#X){j_en@4fk÷8stY9NVD,ocQO-:6|F17BMrC+W(Aq"[Z\nm?H*a^%U<v>w=&Jz u0}ÿ`I\'\\', '\nl am9ADhkþKYIiX@j$|÷.>~U!o,^c/ZVOr8_w";5pE)}6[0HsL§ÿWe#\tRf&y3bnJM\'g4\\T]NB{=Q*`+<PSz27vCGqu?t(Fd:%1-x', '0w%C>n}SVfgÿ|rhl6DQqEO-4,mF)d÷.329@:JTA\'t;?"z]!pWivo5byZþIH{M7c/`eNaR +s&k\t#(B$YG=LU\n\\K~_^*<j18Xx§P[u', '§yYsx~}A$r1=dg/eP^X6cRK;&*G4N0SlQ7!_jM>[5w\ta?Vv8tn,iH+:JO2<qZWÿ\'Eo TD`|kb#(]%B-\nmIz){U@hf÷uC."p9L\\Fþ3', '@^1=iq>r\'$[m\nTPz,:|.&0_RMw/§\\L6*]XKZo`Fal8j-<I\tOCxEþU4HdA5+vc{2g?JeufN3pQG~h Y÷}#DB7ÿWnsyV;%!()9"bktS', '(/6s§!5.þ`qp%J>XL\t{_k#,\\@ae\'3PE9y\ncO$UTÿ1m"f*Bz;n M^S})ZGr|HD=?g&<CVbwYN]87~K[F:WohQR+÷0vAxtIldu2i4-j', '9?C:VL;>=0gZA.B@U"÷s §-3Iawi/ol(Qm_kjT,$zx2~dÿnS8]K!1r%f6`PXHy*&RMuONp|4#cEF5[J\'{D^7\t)hvWqþ}\\Y\n+<etbG', 'eH/ÿYA(8\n2L÷kRajZp&9EPW0#"~<v_$f]\'þrt5BoiODQ,lTM* zV%3mq\\}@>S[=gh1:C§I6dF;4Gws?.K`^ucJNU7n\tybx-{)X+|!', 'vrQxD8KCn/ok=L7Y1\'F÷MG!^s45N$jE `tZ2)*|X[gl3bz.%?0aSuc]Ifd@hH>W;e+6#&<q:JTþU}(P-O9V\n{_y§"mAwRi\tB,ÿ~\\p', 'pz$?u[SW>(2f<n÷+F3erx8"YvdK!ZqPU0`cD7~;Iw9 -)\nlB&]E6to5|A.^þ,{b_kR/agO*N}h\'TGÿ1%Xj@=LmJ#:HC\\sQM4y§V\ti', '|^YOuM-do~CN.VIjB{F&L7Eb#UDe\nP5K?q$>;%*]/Q3<÷\\a\'TRpÿ§129ZsGW!A_+cf@0v6rx}=g\tyi8m"`zthnw)S(,:J4[HXþkl ', 'K\'S\n9qJsþÿ?uL,/)7#\\~n k!:t$QDW6xbO.§Mp\ta|UFHog`dIT÷2zc&=%ywVveB0;Ghf(<5>EXY}]*Ci"-P[ljm_4^Z1{8r@A3+NR', 'aA.{=~l]v§ÿYP\nCH\t!IVE%G`pb^Bh,T|f-þy;W Qqm(ouDtjx647FROkJKwn>9@)SUs#L/÷0*5\'id&1c3<r28MeX\\Ng}+[_Z$?z":', ']þER{Kfj&\\G"\nXvP~l,qÿ4+(6FWwIm@÷[.MVBcnx`A*b;8T!1uz}\tU5)piY2 J/k:C%hLe?Sod9QNDr>\'s7tg|^Z-0y#aH$<3_§=O', '+0\n-rU\\bY)m\tTz:&9n]L=5gc(<w§6s?B Fq!#;E8_2÷lx,p4aHZAS{GKeO@|P1QR"CI[uiNÿ.k~fW*37/þ`hXMDd^o>tyvj}\'VJ%$', 'QsKmþ7Fg\t~8N":rVWA bk§PB;D^31vo4-p\nMw<?cEC_T6`itÿj/Ln(O@[>%hIl,)H$+0Y#U9÷*xq!\\G&y\'=XZa|.uzf{5}SdJ]e2R', ',b\\/vT^(@j$2tk&EB§us7}[XUO*_ai3!÷>S.þPDVp)m\tFCgrcR"Jy45K]-ÿ Yd|f6A{GH9%~lQhZN\n+wo<W\'eqx`L80zn#I1M?;=:', 'v.:)?D|A~huSPþ<Vm=y!ÿ\tFpx_#INaw\nW`1JU0X/"dL5T*;[%>^GHCt]b{c§o\\EZq&jR2+÷gsr7} 3BK(4iO-8$nzY\'6eQl@Mf9,k', 'Ywu]gþXAJD7\'[HQ0Ga|UM8PCl+/;fj\tqc}omÿxkW"ven#2hI!>L\n-1&R4÷sZ\\r{O.tK@Tp(5Sd`)yF :?Ni6=E^%$~B,zV<_b§9*3', '$ÿr%D?Rx&w{^:\'e9)3\\lgVGaJ8þ*K6fBXLnb,]TO[Ut-!NmjW+;~/Cz>"#vp`H_ .u(=qcEs0ZP|÷A\nF}IoSi<Y§Qy1h\t7d54M2k@', '^7}lKi&\'Opÿn~ze\n=j_I"v38 Jþ%.WsN1M+*VSZuc$Qh/aAr-!L)w[6YXy9;PBGb<`@dm5,H:>CgtT4q2\\F(x?ok{E#|0§fDU\t]÷R', 'h[\n_2Vz\t0§FIGe<lY fa\\qX$4O÷on&9u#jJ6~@r-+}!wv>"75d%kHL1WREsZgU;(,AC=^c{Qy)Pÿm.K:*bTBtx3|/N`Mi]þS8\'p?D', ' 6#;I$J|2z?T+~rtþd_&MU§\'LY"=-18\tlQ>k`wC@ybA)e\\H]nqX\n0W.uipNj*/}OPgm59(xB{oRc%v^ÿ<G!4hE3[7F:D÷f,sVZaSK', 'PM0$m^>t_÷R{-1QK#clba5%pw4eBGky?.v:<ExsJ=[3\\/U")T7no(qiY!fF+g9\t8j&Xh*AID ]2;uSzZLO}`,@þ~r6CV|H\'Nÿ\nWd§', 'a@ÿ#Nop,*={R1ixd÷Mbz<]c6+Y%&\t8?/klfLmTGIU$AyE2þs^!nvCOQ}B7t_`u )FwJW\'SKq-5Zg\\(>\n9X|.je4P:h~rH["30§DV;', 't5c\ta71$p[3hYIq.j2"XzxQuvK=%G÷+>U*T|WLFE-Ses}Cl?§_]ÿ`#Jiw^~)nr!þA&H bo{@MyBV\\d8gR<Zf\n6:D4Nk(O9mP,;0\'/', 'E(fSQgÿ\nl3!~WþG^YjoA%mT}Hn]2)47-D$h1F._dew\'÷*\t+@&0t\\bBvpcJ9:;sC `6=L,R§8{ZU|<#X"qNkzKx>5OI/?r[iuPVaMy', 'E_bdh>§Kvn*QD7$mRBJxC3q(igs\\ek9uMT~pr[l.Nÿ;fF"%Vþo5A\nO,w1X:aWSI46HZ@U\t+c]Py{=j! ÷Y^&\'}zt)?L2-/`#0<|G8', 'Zmw> &MV§-Q]!We?[,Ea|TPþ7/Y:\n1`o4sUnOqg\'(RD{=zB2K5y<GC}i8÷ÿvbp^%+h0\tAt$;3.~9)NJ6fjdL\\FlHI@uxX*"#rcSk_', '|Pj48O_ QnY<q5+(rþS=§{~`k"cb@X!A1o/÷ey&Dsv\tI-p3)2tLRz9[#;WmlNx^VH,Tw}.g$0:hCfdMGa7ÿB%>\\Zu*\nJ]U?\'FK6iE', 'pR%ÿD5\tgf&+~iNBc1§÷0Em2HMKb -Q\\FJnOr$I8[SXWC\'aU`{;#>})u\n/xYG7P*lLþeVT]@(.3,o?Z=zw!sh6yjk4|9d^_"<vtq:A', 'QrmOk.o~A\t(1S$]l2|6^vf`=?),#aZ:&w>c_-ÿ[K÷PWxLR"d\'/M7Y5I}JpCzFXbtns;!ghU8u j<þ%*y9+B\\G0eDi{4VH@3§qNTE\n', '/]c\n_P(?9NiK:Vp=YþW- ;62hEquM&\'.w1+lk\t0÷yOf3j[g\\XZGHz}{Ta~C<dn%@>8!,Ltv4I^|RDQ$ÿJ)b`#e*F5o"§xA7mBSUrs', '{<bwndPM,Ag8t&@Gs pqJ-ol/c%!ÿDUFvek;:\\1a÷6[hX?m5~.^_§QxfL#7K\'C|RY\n*yE)"9zV(]Z4S0uOW+H}N$=rþI2`BT3>ij\t', '6w:\\=J3k" azIf§grRT+þmY]Hv7$|nU÷E1W,{FKt>iN.OÿleDx!oBjh<%Pyu-)b~2^*}4#/09pVM8(5@SAqXQ[`\tZs&GC;c_\'?\ndL', 'hP&BO_8e§iykg{b?$x(adÿ~^2T1VL }Zþ*=wAf3|]Kvnp)\\I!jz9"u5M+÷-Rq6#\nC0m:Frt/c`,S<.%lW@QEN[oXJH74Gs;D\'\tUY>', ',cd|s&R_zx\nÿ53jiS!Y8e+-*{a9^AX}Wp/÷o?Mu@=`Bmþ#Fr<(~ZK)L:NE4.Vbk2"0twTGQOf;g$\t%P>71JlhyqDU]6v \\[H§\'ICn', 'BZtAGp]CVL@ey^W+9|}Hþ{.s-J÷4 a%&q)Ig(uKY28$<O~oQS[\tkm>i_X*:§F"=T\\\nU;Nv,!rRxD?#cz\'jE5/ÿ0Mwhf3ldP716`bn', '4v.÷A\\b>DF<-G;zkrÿV3Kl{%x*$R _\nBN5d)pu1"qOh~H/2L@!nw&§f[Qm=a\',T\tXj?`96]o:ZCSisþ+ygc#}7PI(Yt^WJ0e8EMU|', 'B RFhP7XeL1\'j/ZI8O;?CH&bG@yÿ~m^.s\\T{%UMV"\t_r=-!Q2c4i÷K)zW<wg+dqxAkol\n:3E$S#(nJv[t6pu`f]§Y5*},a>|þD90N', '*FkKGrT3Ud_HowZta{QxB+DR§pil;L~cgþ-S!\t.$z=\\j@E#nN<"Amu5&Ie/0[J|fhb2÷`O>)sP7 9C6^Y4}]?MX%V(\'y18,:Wvq\nÿ', 'PF+|p1\\k4\n3!=:Se%}#w$NzR?;fy)c.8@ 9hjdZr6AC÷`M{WD0l\'qsHOa]vm&Vg§7B*QþbX5Yt_Ex~(Iui"[JTG-,2LÿU/>oK\t^<n', 'ÿcz2@:4j\\þ+[Q!-\n %t58^ieBL9J;3uW&{,p*r$0\'A_>y<Xo§m]RO/1DgG.|Zw÷xNnd?~sbV`"EfPI7=MHvSq}#CK(ThaY6U\t)Flk', 'Wi!H4/&6=5Lþl1J#;dRwME[rvx7pja?@(.zDfQK3\\G\tF qtZe,YVT*\n~|{Shms)X2N^I÷}nuA9C8cUÿ<$yb`§%+B-\':]0P>kg_"oO', 'P`07zkTOr"oYF-&tluG_p*?dgLRhK3H<.9nQ\n\tyS=x§D/a]\\;(\'v1j2@XqV,b+#4NiJ^[:~|c!wU>%Z65þEBfm$IA)8{ }ÿse÷WCM', 'cqmUz]61Ir`+(A|=7{Zb:5JPYL#W_\nR§xk;þj^E*Xstai>nl3%GCdOwM\'0 ~/}$\tf?V8Nyÿ2D!S4TBQHKu9,<@p)-[F÷ehog\\v&."', ' ^\'÷ICqy8-YMQrzg(_mP{ÿ:L§S!B;bw$f2%4i0*F,DENU7#[a5Z@3H<"xtGAR=`c).k~s\\jþX}u&V]KO\


def tmp_clear():
    print('\033[0mRemoving all encryption temp files...')
    os.system('sudo rm -fv /tmp/encryption*.tmp\nsudo rm -fv ~/encryption*.tmp\n# & del /f %temp%\\encryption*.tmp')
    print('Successful.')
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


if not ( '-c' in sys.argv or '-e' in sys.argv or '-d' in sys.argv or '-r' in sys.argv or '--keygen' in sys.argv or '-k' in sys.argv ):
    # tmp_clear()
    i = input('[e]ncode, [d]ecode, [r]un encoded, [c] crack and [k]ey generation [e,d,r,k]: ')
else: i = list(str(sys.argv[1]))[1]
if i == 'e' or '-e' in sys.argv:
    if not '-e' in sys.argv:
        i = input('file: ')
        fi = open(file=i,mode='r',encoding='utf-8')
        o = input('output file (create new, *.amns recommended): ')
        fo = open(file=o,mode='w',encoding='utf-8')
    else:
        i = sys.argv[2]
        o = sys.argv[3]
        fi = open(file=i,mode='r',encoding='utf-8')
        fo = open(file=o,mode='w',encoding='utf-8')
    try: fi = fi.read()
    except: pass
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    for a in range(len(conv)): # conv[23] maximum
        bar.set_description(f'{a} of {len(conv)}')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            try: conv2[conv1[i]] = list(conv[a])[i]
            except: conv2[conv1[i]] = list(conv[a])[__import__('random').randint(0,len(list(conv[a])))-1]
        preresult = ""
        for b in range(len(str(last))): # convert original to encrypted
            try:
                preresult += conv2[list(str(last))[b]]
                bar.update(1)
            except: pass
        last = preresult
        result = str(preresult)
        print(f'data length written: {len(preresult)}')
    fo.write(result)
    bar.close()
    print('done.')
elif i == 'd' or '-d' in sys.argv:
    if not '-d' in sys.argv:
        i = input('file: ')
        fi = open(file=i,mode='r',encoding='utf-8')
        o = input('output file (create new): ')
        fo = open(file=o,mode='w',encoding='utf-8')
    else:
        i = sys.argv[2]
        fi = open(file=i,mode='r',encoding='utf-8')
        o = sys.argv[3]
        fo = open(file=o,mode='w',encoding='utf-8')
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
            try:
                preresult += conv2[list(str(last))[b]]
                bar.update(1)
            except: pass
        last = preresult
        result = str(preresult)
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}')
    fo.write(result)
    bar.close()
    print('done.')
elif i == 'r' or '-r' in sys.argv:
    if not '-r' in sys.argv: i = input('file: ')
    else: i = sys.argv[2]
    fi = open(file=i,mode='r',encoding='utf-8')
    o = f"encryption{__import__('random').randint(114514,0x1919810)}.tmp"
    fo = open(file=o,mode='w',encoding='utf-8')
    conv.reverse()
    try: fi = fi.read()
    except: pass
    last, result = str(fi),str(fi)
    conv2 = {}
    bar = tqdm(total=len(conv)*len(str((last))))
    fails = 0
    fbytes = 0
    for a in range(len(conv)): # conv[23] maximum
        def bsd(): bar.set_description(f'{a}/{len(conv)}, C_BLK={fails} C_BYTE={fbytes}')
        conv2.clear()
        conv2 = {}
        for i in range(len(conv1)): # conv1[i] -> conv[a][i] create converter
            try: conv2[list(conv[a])[i]] = conv1[i]
            except: fbytes += 1
        preresult = ""
        isfail = False
        for b in range(len(str(last))):
            try:
                preresult += conv2[list(str(last))[b]]
            except:
                fbytes += 1
                isfail = True
            bar.update(1)
            bsd()
        last = preresult
        result = str(preresult)
        if isfail: fails += 1
        print(f'{a} of {len(conv)} completed, data length {len(preresult)}, total {fails} corrupted blocks, total {fbytes} corrupted bytes')
    fo.write(result)
    bar.close()
    print('compiled.')
    if fbytes != 0: print(f'\033[93m[!!] {fbytes} bytes in {fails} blocks has been found as corrupted!\033[0m')
    if not ( '-e' in sys.argv or '-d' in sys.argv or '-r' in sys.argv ):
        lang = None
        lang = input('enter compiler path or command (example: py, ipython3, java): ')
        if lang == None or lang == '': lang = 'python'
        para1 = input('enter parameter before filename. if no, type nothing and continue: ')
        para2 = input('enter parameter after filename. if no, type nothing and continue: ')
    else:
        try: lang = sys.argv[3]
        except: lang = 'python'
        try: para1 = sys.argv[4]
        except: para1 = '' 
        try: para2 = sys.argv[5]
        except: para2 = ''
        if para1 == 'none' or para1 == 'None': para1 = ''
        if para2 == 'none' or para2 == 'None': para2 = '' 
    # print(f'program launch command: {lang} {para1} {o} {para2}')
    fo.close()
    os.system(f'mv {o} /tmp/{o} \n# & move {o} %temp%\\{o}')
    os.system(f'{lang} {para1} /tmp/{o} {para2} # & start wt {lang} {para1} %temp%\\{o} {para2}')
elif i == 'k' or '--keygen' in sys.argv or '-k' in sys.argv:
    keysource_d = conv1
    keylength = input(f'key length (default {len(keysource_d)}): ')
    if keylength == '' or keylength is None: keylength = 24
    try: keylength = sys.argv[2]
    except: pass
    keylength = int(keylength)
    keysource = input(f'the default key source is: {ascii(keysource_d)}\nenter new key source, or type nothing to use the default one: ')
    if keysource == '' or keysource is None: keysource = conv1
    try: keysource = sys.argv[3]
    except: pass
    conv_new = []
    for i in range(keylength):
        result = ''
        while True:
            rand = __import__('random').randint(0,len(keysource)-1)
            if not keysource[rand] in list(result): result += keysource[rand]
            if len(result) >= len(keysource): break
        conv_new += [result]
    print(f'key generated: \n{str(conv_new)}')
    p = f"encryption-conv1-{__import__('random').randint(114514,0x1919810)}.tmp"
    open(p,mode='w').write(str(conv_new))
    print(f'\033[33m[!!] Please note that if you are not using default key source, please write down the key source:\n\t\033[35{ascii(keysource)}\033[33m')
    o = f"encryption-conv-{__import__('random').randint(114514,0x1919810)}.tmp"
    open(o,mode='w').write(keysource)
    print(f'\033[33m     or read the key data (conv) written into file \033[1m"{o}"\033[0m\033[33m.\nDo not forget the generated key location: "\033[1m{p}\033[0m\033[33m"\033[0m')
elif i == 'c' or '-c' in sys.argv or '--crack' in sys.argv: # crack manually yourself!
    if True: # if not argument mode, "True" is the override
        i = sys.argv[2] if '-c' in sys.argv or '--crack' == sys.argv else input('enter encoded filename: ')
        fi = open(file=i,mode='r',encoding='utf-8')
        fi = fi.read()
        data = fi
        factory_data = fi
        replace_e = []
        replace_d = []
        cracked_char = []
        while True:
            # decoding game, maybe
            os.system('clear')
            print(f'=== Begin file ===\n{data}\n=== End file ===\n')
            c = input('[r]Replace, [q]Quit, [w]Save, [a]Auto, [.]Config\n   \\--> ')
            # Incompleted: q,w,a
            if len(c) != 0:
                if list(c)[0] == '.':
                    if c == '.load' or c == '.import':
                        print('\n(Config Load/Import) Save file:')
                        i = input('   \\--> ')
                        fi = open(file=i,mode='r',encoding='utf-8')
                        fi = eval(fi.read())
                        if fi[0] == 'r': # [R]Result, [F]Everything
                            print(f'Save time in UNIX Timestamp: {fi[1]}\n=== Begin Data Preview (File {i}) ===\n{fi[2]}\n=== End Data Preview (File {i})')
                            sure = input('[!] Read-only: This file was saved in result-only mode. Editing isn\'t supported.\nImport data to this session? [y,n]: ')
                            if sure != 'y': print('Abort.')
                            else:
                                begin = __import__('time').time()
                                print('Loading data...')
                                data = fi[2]
                                print(f'Completed in {round((__import__('time').time()-begin)*1000)}ms')
                                __import__('time').sleep(1)
                        if fi[0] == 'f':
                            os.system('clear # & cls')
                            input(f'Save time in UNIX Timestamp: {fi[1]}\n=== Begin Data Preview (File {i}) ===\n{fi[2]}\n=== End Data Preview (File {i}) ===\nPage 1 of 3 (Manual Decoded Data)\n\npress [return] to continue...')
                            os.system('clear # & cls')
                            input(f'Save time in UNIX Timestamp: {fi[1]}\n=== Begin Data Preview (File {i}) ===\n{fi[3]}\n=== End Data Preview (File {i}) ===\nPage 2 of 3 (Factory / Encoded Data)\n\npress [return] to continue...')
                            os.system('clear # & cls')
                            input(f'Save time in UNIX Timestamp: {fi[1]}\n=== Begin Data Preview (File {i}) ===\ne: {fi[4]}\nd: {fi[5]}\ncracked: {fi[6]}\n=== End Data Preview (File {i})\nPage 3 of 3 (Other Variables)\n\n')
                            sure = input('[v] This file was saved in full-export mode. Import data to this session?\n   \\--[y,n]-> ')
                            if sure != 'y': print('Abort.')
                            else:
                                begin = __import__('time').time()
                                print('Loading data...')
                                data = fi[2]
                                print('Loading factory_data...')
                                factory_data = fi[3]
                                print('Loading replace_e...')
                                replace_e = fi[4]
                                print('Loading replace_d...')
                                replace_d = fi[5]
                                print('Loading cracked_char...')
                                cracked_char = fi[6]
                                print(f'Completed in {round((__import__('time').time()-begin)*1000)}ms')
                                __import__('time').sleep(1)

                elif c == 'r' or list(c)[0] == 'r':
                    re = input('(Replace) character before: ') if not len(c)==3 else list(c)[1] 
                    contains = 0
                    bar = tqdm(total=len(data))
                    for i in list(factory_data):
                        if i == re: contains += 1
                        bar.update(1)
                        bar.set_description(f'Found {contains} same character "{re}"')
                    bar.close()
                    print(f'{contains} same character has been found.')
                    rd = input('(Replace) replace with: ') if not len(c)==3 else list(c)[2]
                    print('Replace "{re}" to "{rd}".\n')
                    preview = list(factory_data)
                    bar = tqdm(total=2*len(data))
                    bar.set_description('Generating preview')
                    for i in range(len(factory_data)):
                        if factory_data[i] == re: preview[i] = f'\033[93m{rd}\033[0m' 
                        else: preview[i] = f'\033[91m{preview[i]}\033[0m'
                        bar.update(1)
                    for o in range(len(replace_e)):
                        for i in range(len(factory_data)):
                            if factory_data[i] == replace_e[o]: preview[i] = f'\033[92m{replace_d[o]}\033[0m' 
                    preview2 = ""
                    for i in preview:
                        preview2 += str(i)
                        bar.update(1)
                    bar.close()
                    preview = preview2
                    print('Preview generated.\n')
                    print(f'=== Begin data (preview) ===\n{preview}\n=== End data (preview) ===\n\n')
                    rs = input('(Replace) Are you sure to replace all of them? [y/n]: ')
                    if rs == 'y':
                        data = preview
                        cracked_char += [rd]
                        replace_e += [re]
                        replace_d += [rd]
                        print('Done.')
                    else: print('Abort.')
                elif c == 'a': # Auto (a)
                    print(f'(pysymbol1) the : symbol')
                    sel = input('(ID), [!=ID]Exit: ')
                    if sel == 'pysymbol1':
                        print('Detecting.')
                        preview = list(data)
                        passed = []
                        bar = tqdm(total=len(preview))
                        for i in range(len(preview)):
                            if preview[i] == '\n': preview[i-1]
                elif c == 'w':
                    print(f'(save) attempting to save changes.')
                    mode = input('[r]ResultOnly, [f]Full (Everything,Recommended), [any*]Abort (BackToHome)  [r,f,*]: ')
                    if mode == 'r':
                        print('selected: [r] Export result only\nYou will not be able to edit again if you use R mode.')
                        sure = input('Are you really sure? [y/n]: ')
                        if sure != 'y': mode = 'abort'
                    elif mode == 'f':
                        print('selected: [f] Export everyting (yes, everything!)\nExport All changes, debug informations and other things.')
                        sure = input('Are you sure? [y/n]: ')
                        if sure != 'y': mode = 'abort'
                    else: mode = 'abort'
                    if mode == 'r':
                        o = input('output file (automatic create or replace): ')
                        fo = open(file=o,mode='w',encoding='utf-8')
                        clock = __import__('time').time()
                        fo.write(str(['r',clock,data]))
                        input('Saved! Press [return] to continue.')
                    elif mode == 'f':
                        o = input('output file( automatic create or replace): ')
                        fo = open(file=o,mode='w',encoding='utf-8')
                        clock = __import__('time').time()
                        fo.write(str(['f',clock,data,factory_data,replace_e,replace_d,cracked_char]))
                        input('Saved! Press [return] to continue.')
                    else: print('Abort.')
                elif c == 'q':
                    vc = __import__('random').randint(100000,999999)
                    sure = input(f'\nAre you sure to exit? Remember to save your changes...\nType "{vc}" to exit, or press [return] to abort.\n   \\--> ')
                    if str(sure) == str(vc): exit()
                    else:
                        print('Abort.'); __import__('time').sleep(1)

# Ctrl+K+U to remove note 
# Ctrl+K+C to add note