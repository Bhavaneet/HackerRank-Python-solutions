set_a = set(map(int, input().split()))
condition = True
for _ in range(int(input())):
    set_x = set(map(int, input().split()))
    if not set_a > set_x:
        condition = False
        break
           
print(condition)