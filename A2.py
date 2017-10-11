from __future__ import division
import math
import numpy as np


#Defining general parameters of the algorithm
n=3;
Lambda=10;
c=math.sqrt(1/n)
cr=3/(n+3)
cu=math.sqrt((2-c)/c)
B=1/n
Bind=1/(4*n) 
Br=math.sqrt(1/(4*n))
X1=math.sqrt(2/math.pi)
XN=math.sqrt(n)*(1-1/(4*n)+1/(21*math.pow(n,2))) 
optimum=0# We have to replace with the real optimum of the function

#Evolution strategy (1,Lambda) ES with A2 reproduction scheme
def One_Lambda_ES_A2(fun, lbounds, ubounds, budget):
    #Initial population = Only one parent X ( mu=1 )
    X=[]
    for j in range(n):
        X.append(np.random.uniform(lbounds,ubounds))
     
    #We have to initialize theses structures
    
    #Structures of parent
    s=np.array([0 for ligne in xrange(n)])#weighted sum for adaptation step size(Size=N)
    r=np.array([0 for ligne in xrange(n)])# a vector of n variables : direction vector used to produce line mutation (Size=N)
    
    sr=0 #weighted sum for adaptation of step size sigma_r    (Size=1)
    sigma=np.array([1 for ligne in xrange(n)])#vector of n variables :all individual step sizes (Size=N)
    sigma_r=0 #step size for direction  (Size=1)
    f=fitness(fun,X)
    
    #Structures of children
    X_N=np.array([[0 for colonne in xrange(n)] for ligne in xrange(Lambda)] )
    f_N=np.array([0 for ligne in xrange(Lambda)]) # fitness of offspring
    s_N=np.array([[0 for colonne in xrange(n)] for ligne in xrange(Lambda)] )
    sr_N=np.array([0 for ligne in xrange(Lambda)] )
    sigma_N=np.array([[0 for colonne in xrange(n)] for ligne in xrange(Lambda)])
    r_N=np.array([[0 for colonne in xrange(n)] for ligne in xrange(Lambda)])
    sigma_r_N=np.array([0 for ligne in xrange(Lambda)] )
    f_N=np.array([0 for ligne in xrange(Lambda)] )
    iter=0;
    
    while(f>optimum and iter<=budget):#while not happy loop
        #Reproduction (A2)
        
        for k in range(Lambda):#foreach offspring
            zrk=np.random.normal(0,1,1); #choose a normal distributed random zr 
            zk=np.random.normal(0,1,n)#vector of n normal. dist. rand. variables for the k-th offspring
            #2. Adaptation of the individual step sizes
            s_N[k]=(1-c)*s+c*(cu*zk)#WHAT IS ZK???????????
            #foreach variable of the k-th offspring
            for i in range(n):
                #1. Mutation of the object variables
                X_N[k][i]=X[i]+sigma[i]*zk[i]+sigma_r*zrk*r[i]
                sigma_N[k][i]=sigma[i]*np.exp(B*(np.linalg.norm(s_N)-XN))*np.exp(Bind*(math.fabs(s_N[k][i])-X1))#VERIFY THE FORMULA        
                #Direction adaptation
                
            sr_N[k]=max((1-c)*sr+c*(cu*zrk),0)
            r_prime=(1-cr)*sigma_r*r+cr*(X_N[k]-X)
            r_N[k]=r_prime/np.linalg.norm(r_prime)#VERIFY THIS ONE
            sigma_r_N=max(sigma_r*np.exp(Br*(math.fabs(sr_N[k])-X1)),1/3*np.linalg.norm(sigma_N))
            #Evaluate the k-th offspring
            f_N[k]=fitness(fun,X_N[k])
        #Choose the best offspring
         #The Elder become the best offspring
        iter=iter+1; 
        indMin=np.where(f_N == f_N.min())
        X = X_N[indMin]
        f=min(f_N)
        s=s_N[indMin]
        r=r_N[indMin]
        sigma_r=sigma_r_N[indMin]# a vector of n variables : direction vector used to produce line mutation (Size=N)
        sr=sr_N[indMin]
        sigma[indMin]=sigma_N
    #when we go out from the main loop: testing if we have found the optimum or 
    #we failed to find it with the given budget   
         
    if(iter<=budget):
        return X,iter
    else:
        print("can't find the optimum with this budget")
        return X
            
 
def fitness(fun,solution):
    #We have to call the problem function to calculate the function value of the solution
    return np.sum([x ** 2 for x in solution])

x,iter = One_Lambda_ES_A2('sphere', -10,10, 10)
print x