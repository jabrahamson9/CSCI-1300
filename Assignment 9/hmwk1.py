def ParityParty(d):
        lis=[]
        if d%2=0:
                lis.append(0)
                lis.append(d/2)
        else:
                lis.append(1)
                lis.append((d-1)/2)
        return lis


def main():
        ParityParty(4)

if __name__=="__main__":
        main()
