#!/usr/bin/env python3

print("RUN " * 10)

sopStr = "AB!C + !BC + !A !C"

def sop2terms(sop):
    sopList = sop.split('+')
    sopList = [s.replace(' ', '') for s in sopList]
    return sopList

Lmax = max([max(ord(c) for c in T) for T in sop2terms(sopStr)])

Vars = [chr(n) for n in range(65, Lmax+1)]

#------------------------------------------------------------
def v2bterms(instr, vars):
    """ parameters:
    string  "A!B!D" representing a product in a sum of products
    boolean expression.
    list ['A', 'B', 'C', 'D'] containing all variables in the sum
    of products expression.
    returns a string "10X0" with missing variables in string replaced
    with a "X".  """
    inlist = []
    c = 0
    while c < len(instr):
        if instr[c] == '!':
           inlist.append(instr[c] + instr[c+1])
           c += 2
        else:
            inlist.append(instr[c])
            c += 1
    #print("\n\n\tinstr: {}\n\n\tinlist: {}".format(instr, inlist))
    #print("\n\n\t vars: {}".format(vars))

    resb = ''
    for c in vars:
        if c not in inlist and ('!' + c) not in inlist:
            resb += 'X'
        elif c in inlist:
            resb += '1'
        else:
            resb += '0'
    #print("Result: {}".format(resb))
    return resb
#------------------------------------------------------------

#------------------------------------------------------------

def decImps(term):
    """Parameter: String containing characters 1, 0 and X.
    Return list of all values where X's are replaced with all
    possible combinations of 1s and 0s"""
    numX = term.count("X")
    decList = []
    for b in range(2**numX):
        bbits = ("{:0>{}}".format(bin(b)[2:], numX))
        imp = term
        for bit in bbits:
            imp = imp.replace("X", bit, 1)
        decList.append(int(imp, 2))
    return(decList)

#------------------------------------------------------------

def sop2imps(sop, vars):
    '''Parameters: sop: String containing a SOP (sum of products)
                   vars: list containing variables
    vars may include variables not in sop string
    Returns sorted list of all implicants covered by the sop'''
    soplist = ' _ '.join(sop.split('+')).replace(' ', '').split('_')
#    print(sop, "\n\n ", soplist, "\n\n") #Comment

    covers = []
    for T in soplist:
        covers.append(v2bterms(T, vars))
#    print("\n\t", covers, "\n") #Comment

    coverImps = []
    for term in covers:
        for I in decImps(term):
            if I not in coverImps:
                coverImps.append(I)
    coverImps.sort()
    return coverImps

#------------------------------------------------------------


#------------------------------------------------------------






print('\t', sopStr)
print(sop2terms(sopStr))


