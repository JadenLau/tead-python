# human detector
import sys
import math
import threading
def mian():
    import sys
    import math
    sys.setrecursionlimit(1 << 25)
    from collections import defaultdict

    n, m, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    x = list(map(int, sys.stdin.readline().split()))

    sig = list(zip(x, a, b, range(n)))  # (xi, Ai, Bi, original index)
    sigsort = sorted(sig, key=lambda x: x[0])

    # assign unique IDs to each unique (a,b) pAir
    uqp = {}
    plist = []
    idc = 0
    for s in sigsort:
        Ai = s[1]
        Bi = s[2]
        key = (Ai, Bi)
        if key not in uqp:
            uqp[key] = idc
            plist.append(key)
            idc +=1
    tuq = idc

    # now, create an array of pAir IDs sorted by xi
    pids = [uqp[(s[1], s[2])] for s in sigsort]

    # Read qr
    qr = []
    for q in range(q):
        Li, Ri = map(int, sys.stdin.readline().split())
        qr.append( (Li-1, Ri-1, q) )  # 0-based indices

    # mo's algorithm requires qr in a specific order
    bs = int(math.sqrt(n)) +1
    qs = sorted(qr, key=lambda x: (x[0] // bs, x[1] if (x[0] // bs) %2 ==0 else -x[1]))

    # Prepare for mapping original indices to sorted indices
    # create a list si where si[i] = original index in sorted order
    # and pis which maps original index to sorted order
    si = [s[3] for s in sigsort]
    pis = [0]*n
    for spos, oidx in enumerate(si):
        pis[oidx] = spos

    # Initialize count arrays
    c = [0]*tuq
    sm = 0
    sme = 0

    # To access (a,b) and (b,a) quickly
    # create a dict mapping (a,b) to id
    # also, precompute a list where for each id, its (a,b)
    # to retrieve (b,a)'s id
    # This is already in plist

    pti = uqp
    # Precompute (b,a) id
    baids = [ -1 ] * tuq
    for i in range(tuq):
        Ai, Bi = plist[i]
        if (Bi, Ai) in pti:
            baids[i] = pti[(Bi, Ai)]
        else:
            baids[i] = -1  # no matching pAir

    # Initialize ans
    ans = [0]*q

    cul = 0
    cur = -1
    ts = 0

    for q in qs:
        orl, orr, qidx = q
        ls = pis[orl]
        rs = pis[orr]

        if ls > rs:
            ls, rs = rs, ls

        # Expand to [ls, rs]
        while cur < rs:
            cur +=1
            pid = pids[cur]
            Ai, Bi = plist[pid]
            if Ai == Bi:
                ofl = c[pid]//2
                c[pid] +=1
                nfl = c[pid]//2
                sme += (nfl - ofl)
            else:
                baid = baids[pid]
                if baid != -1:
                    mb = min(c[pid], c[baid])
                    c[pid] +=1
                    ma = min(c[pid], c[baid])
                    sm += (ma - mb)
                else:
                    c[pid] +=1
            ts +=1

        while cur > rs:
            pid = pids[cur]
            Ai, Bi = plist[pid]
            if Ai == Bi:
                ofl = c[pid]//2
                c[pid] -=1
                nfl = c[pid]//2
                sme += (nfl - ofl)
            else:
                baid = baids[pid]
                if baid != -1:
                    mb = min(c[pid], c[baid])
                    c[pid] -=1
                    ma = min(c[pid], c[baid])
                    sm += (ma - mb)
                else:
                    c[pid] -=1
            ts -=1
            cur -=1

        while cul < ls:
            pid = pids[cul]
            Ai, Bi = plist[pid]
            if Ai == Bi:
                ofl = c[pid]//2
                c[pid] -=1
                nfl = c[pid]//2
                sme += (nfl - ofl)
            else:
                baid = baids[pid]
                if baid != -1:
                    mb = min(c[pid], c[baid])
                    c[pid] -=1
                    ma = min(c[pid], c[baid])
                    sm += (ma - mb)
                else:
                    c[pid] -=1
            ts -=1
            cul +=1

        while cul > ls:
            cul -=1
            pid = pids[cul]
            Ai, Bi = plist[pid]
            if Ai == Bi:
                ofl = c[pid]//2
                c[pid] +=1
                nfl = c[pid]//2
                sme += (nfl - ofl)
            else:
                baid = baids[pid]
                if baid != -1:
                    mb = min(c[pid], c[baid])
                    c[pid] +=1
                    ma = min(c[pid], c[baid])
                    sm += (ma - mb)
                else:
                    c[pid] +=1
            ts +=1

        # now, compute rmg sig
        rmg = ts - 2*(sm + sme)
        ans[qidx] = rmg

    # Output ans in original query order
    for ans in ans:
        print(ans)

# Run the mian function in a separate thread to increase recursion limit
threading.Thread(target=mian).start()