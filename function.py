def is_leap(year):
    leap = False
    if (leap%4==0 & leap%100==0) | leap%400==0:
        leap=True
    else :
        leap=False
    
    return leap

year = int(input())
print(is_leap(year))