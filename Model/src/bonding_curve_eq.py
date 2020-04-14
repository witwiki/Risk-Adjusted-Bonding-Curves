import numpy as np

default_kappa = 2 ## Can we have default set kappa? Curvature and reserve ratio change as bonding curve is adjusted for risk
default_exit_tax = .02

#value function for a given state (R,S)
def invariant_V0(R,S,kappa=default_kappa):    
    return (S**kappa)/R

########### REVISIT (replace alpha -> omega?) ##############
#value function for a given state (C, alpha)
def invariant_I0(C, alpha, kappa=default_kappa):
    return (C*alpha*kappa)/(kappa-1)

#given a value function (parameterized by kappa)
#and an invariant coeficient V0
#return Supply S as a function of reserve R
def reserve(S, V0, kappa=default_kappa):
    return (S**kappa)/V0

#given a value function (parameterized by kappa)
#and an invariant coeficient V0
#return Supply S as a function of reserve R
def supply(R, V0, kappa=default_kappa):
    return (V0*R)**(1/kappa)

#given a value function (parameterized by kappa)
#and an invariant coeficient V0
#return a spot price P as a function of reserve R
def spot_price(R, V0, kappa=default_kappa):
    return kappa*R**((kappa-1)/kappa)/V0**(1/kappa)

########### REVISIT ##############
#given a value function (parameterized by kappa)
#and an invariant coeficient I0
#return a spot alpha as a function of reserve R
def spot_alpha(C, I0, kappa=default_kappa):
    return (I0*(kappa-1))/(C*kappa)

#for a given state (R,S)
#given a value function (parameterized by kappa)
#and an invariant coeficient V0
#deposit deltaR to Mint deltaS
#with realized price deltaR/deltaS
def mint(deltaR, R,S, V0, kappa=default_kappa):
    deltaS = (V0*(R+deltaR))**(1/kappa)-S
    if deltaS == 0:
        realized_price = spot_price(R+deltaR, V0, kappa)
    else:
        realized_price = deltaR/deltaS
    return deltaS, realized_price

#for a given state (R,S)
#given a value function (parameterized by kappa)
#and an invariant coefficient V0
#burn deltaS to Withdraw deltaR
#with realized price deltaR/deltaS
def withdraw(deltaS, R,S, V0, kappa=default_kappa):
    deltaR = R-((S-deltaS)**kappa)/V0
    if deltaS == 0:
        realized_price = spot_price(R+deltaR, V0, kappa)
    else:
        realized_price = deltaR/deltaS
    return deltaR, realized_price

########### REVISIT ##############
#given a value function 
#and an invariant coefficient I0
#bond deltaS_1 to obtain deltaQ_1
#with realized alpha ????
def attest_pos

def withdraw_with_tax(deltaS, R,S, V0, exit_tax = default_exit_tax, kappa=default_kappa):
    deltaR = R-((S-deltaS)**kappa)/V0
    #print(deltaR)
    quantity_taxed = exit_tax*deltaR
    quantity_recieved = (1-exit_tax)*deltaR
    
    realized_price = quantity_recieved/deltaS
    
    return quantity_recieved, quantity_taxed, realized_price