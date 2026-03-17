def w_recursive(i):
    if i == 1:
        return 0.3
    if i == 2:
        return -1.5
    return w_recursive(i-1) * w_recursive(i-2) * ((i-1)**2) / ((i+1)**3)

print("\nРасчёт w_i:")
for i in range(1, 6):
    print(f"w{i} =", w_recursive(i))