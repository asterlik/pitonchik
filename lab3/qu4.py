def w_iterative(n):
    if n == 1:
        return 0.3
    if n == 2:
        return -1.5
    
    w_prev2 = 0.3   # w1
    w_prev1 = -1.5  # w2
    
    for i in range(3, n + 1):
        w_current = w_prev1 * w_prev2 * ((i-1)**2) / ((i+1)**3)
        w_prev2, w_prev1 = w_prev1, w_current
    
    return w_prev1

print("\nРасчёт w_i:")
for i in range(1, 6):
    print(f"w{i} =", w_iterative(i))