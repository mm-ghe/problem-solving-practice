EVENS_SUM = 0
n = 0
m = 1
while m < 4_000_000:
    NEXT = n + m
    n = m
    m = NEXT
    if NEXT % 2 == 0:
        EVENS_SUM += NEXT

print(EVENS_SUM)
