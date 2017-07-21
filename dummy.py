def fx(x):
    return 10-x*x
def testLocal():
    i=-4
    j=1
    step=0
    while j-i>1e-6:
        mid=(i+j)/2
        fmid=fx(mid)
        fnext=fx(mid+1e-6)
        if fnext>fmid:
            i=mid
        elif fnext<fmid:
            j=mid
        step+=1
    print(round(j))
    print(step)
if __name__ == '__main__':
    testLocal()
    #dummy
    #dummy2