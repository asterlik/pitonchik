import itertools

lett = 'АНДРЕЙ'
cnt = 0
for code in itertools.product(lett, repeat=6):
    s = ''.join(code)
    if s.count('Й') > 1:
        continue
    if s[0] == 'Й' or s[-1] == 'Й':
        continue
    if 'ЕЙ' in s or 'ЙЕ' in s:
        continue
    cnt += 1
print(cnt)