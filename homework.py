
# Register machine

# list of (supported) denominations
d_global = [100, 50, 25, 10, 5, 1]

# C calculates the difference of a & b (the change in cents)
def C(a,b):
    return b-a

def Q(change, denom):
    q = [0,0,0,0,0,0] # empty denom list
    i = 0 # i is tracking e
    for e in denom: # i is tracking e, e is moving though denom
        while change >= e: # e is the value 
            change = change - e
            q[i] = q[i] + 1 # you are inc to put this denom, i is a moving target, i is moving with e 
        i = i + 1
    return q

def P(a,b):
    return Q(C(a,b), d_global)

print("your change is: ", P(2000, 4300))
