def range_sum(l, r, origin):
    l -= origin
    r -= origin
    
    if l <= 0 and r <= 0:
        l, r = -r, -l
    elif not (l >= 0 and r >= 0):
        return range_sum(0, abs(l), 0) + range_sum(0, abs(r), 0)
    
    return (r*(r+1)//2) - (l*(l-1)//2)


r, g, b = map(int, input().split())

ans = 10000000000000

for i in range(450*2+1):
    l = i - 450
    calc = 0

    #R
    if -100 + (r-1)//2 >= l:
        calc += range_sum(l-r, l-1, -100)
    else:
        calc += range_sum(-(r//2),(r-1)//2, 0)
    
    #G
    calc += range_sum(l, l+g-1, 0)

    #B
    if l+g - 1 >= 100 - (b-1)//2:
        calc += range_sum(l+g, l+g+b-1, 100)
    else:
        calc += range_sum(-(b//2),(b-1)//2, 0)

    ans = min(ans, calc)

print(ans)
