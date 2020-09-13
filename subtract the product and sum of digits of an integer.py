

n = 234

def subtractProductAndSum(n):
    n = str(n)
    sumNum = sum(int(x) for x in n)

    mulNum = eval(n.replace('', '*')[1:-1])

    return mulNum - sumNum









print(subtractProductAndSum(n))