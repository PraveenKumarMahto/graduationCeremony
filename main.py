

def generate_tree(s,n):
    if s[-4:] == "0000":
        return 0, 0
    if n==0:
        if s[-1:] =="0":
            return  1, 1
        return 1, 0      
    t1, a1 = generate_tree(s + "1",(n-1))
    t2, a2 = generate_tree(s + "0",(n-1))
    return  t1+t2, a1+a2

N = 10
total_days, absent_days = generate_tree("", N)
print("1. The number of ways to attend classes over "+ str(N)+" days. : " +str(total_days))
print("2. The probability that you will miss your graduation ceremony. : " +str(absent_days) + "/" + str(total_days))











 






