def fx(x):
    return 10-x*x
def testLocal():
    l=-4
    h=1
    step=0
    while h-l>1e-6:
        mid=(h+l)/2
        fmid=fx(mid)
        fnext=fx(mid+1e-6)
        if fnext>fmid:
            l=mid
        elif fnext<fmid:
            h=mid
        step+=1
    print(int(h))
    print(step)
if __name__ == '__main__':
    testLocal()
    #dummy
    #dummy2