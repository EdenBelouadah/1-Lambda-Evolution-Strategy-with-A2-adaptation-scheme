import math
import numpy as np


n=3;
Lambda=10;
mu=1; #=size population???
c=math.sqrt(1/n)
cr=3/(n+3)
cu=math.sqrt((2-c)/c)
B=1/n
Bind=1/(4*n)
Br=math.sqrt(1/(4*n))
X1=math.sqrt(2/math.pi)
XN=math.sqrt(n)*(1-1/(4*n)+1/(21*math.pow(n,2)))
#####################################################################
#Defining the population: Pop=[X;fits;s;z;r]
X=[] #values of the solution x1,...,xn more exactly (x1,sigma_i,z,r1),(x,sigma_i,z,r1)
s=[] #weighted sum for adaptation of step size
sr=[] #weighted sum for adaptation of step size
z=[] # ~N(0,1)
r=[]
fits=[]#fitnesses of the solutions
#####################################################################

#Evolution strategy (1,Lambda) ES with A2 reproduction scheme
def ES_A2(fun, lbounds, ubounds, budget):
    #Initial population = Only one parent
    for j in range(n):
        P.append(np.random.uniform(lbounds,ubounds))
    s=0
    f_P=fitness(fun,P)    
    sigma=[]#vector of n variables :all individual step sizes
    r=[]# a vector of n variables : direction vector used to produce line mutation
    sigma_r=0 #step size for direction 
    while(f_P>optimum and iter<=budget):#while not happy loop
        #Reproduction (A2)
        for k in range(Lambda):#foreach offspring
            zrk=np.random.normal(0,1,1); #choose a normal distributed random zr 
            X_Nk=[] #initialize the k-th offspring
            s_Nk=[] #initialize the weighted sum for adaptation of step size of the k-th offspring
            zk=np.random.normal(0,1,n)#vector of n normal. dist. rand. variables for the k-th offspring 
            #X_Ek=X[C_k]# Extract the Xs of the chosen parent from the population  
            #s_Ek=s[C_k]#Extract the weighted sum for adaptation of step size of chosen parent 
            for i in range(n):
                #1. Mutation of the object variables
                X_Nk[i][0]=P[i]+sigma[i]*zk[i]+sigma_r*zrk*r[i]
                #2. Adaptation of the individual step sizes
                s_Nk[i]=(1-c)*s+c*(cu*z[k])
                X_Nk[i][1]=X_Ek[i][1]*np.exp()*np.exp()        
                #Direction adaptation
                sr[k]=max((1-c)*sr[C_k]+c*(cu*zrk),0)
                r=(1-cr)*X_Ek[]*+cr*(-)
                
    #when we go out from the main loop: testing if we have found the optimum or 
    #we failed to find it with the given budget        
    if(iter<=budget):
        return X[best_solution]
    else:
        print("can't find the optimum with this budget")
        return null
            
 
def fitness(fun,solution):
    #We have to call the problem function to calculate the function value of the solution
    return 0
