# Submission link: https://codeforces.com/contest/1525/submission/258173540
def main():
    n, m = MII()
    dist = [LII() for _ in range(n)]

    mod = 998244353
    cnt = [0] * n

    inv = 1
    for i in range(1, n + 1):
        inv *= i
        inv %= mod
    inv = pow(inv, -1, mod)

    ans = 0
    for i in range(m):
        for j in range(n):
            if dist[j][i] >= 2:
                cnt[dist[j][i] - 2] += 1
        
        cur = 1
        cur_cnt = 0
        for j in range(n - 1, -1, -1):
            cur_cnt += cnt[j]
            cur *= cur_cnt
            cur %= mod
            cur_cnt -= 1
        
        for j in range(n):
            cnt[j] = 0
        
        ans = (ans + 1 - cur * inv) % mod

    print(ans)