n, q = map(int, raw_input().split())
last_ans = 0
s = []

for _ in range(n):
    s.append([])

for i in range(q):
    query_no,x,y = map(int,raw_input().split())
    seq_no = (x^last_ans)%n

    if query_no == 1:
        s[seq_no].append(y)
    elif query_no == 2:
        last_ans = s[seq_no][y%len(s[seq_no])]
        print last_ans
