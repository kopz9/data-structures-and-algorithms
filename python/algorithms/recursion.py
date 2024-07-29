# 100 000 000 print all divisible by 1 000 000 
# cannot use loops 


def i(n, num=0):
  if num <= n:
    if num % 1_000_000 == 0:
      print(num)
    i(n, num+1)
  
i(3)
    