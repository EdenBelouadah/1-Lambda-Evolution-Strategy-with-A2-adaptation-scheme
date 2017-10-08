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

#Evolution strategy (1,Lambda) ES with A2 reproduction scheme
def One_Lambda_ES_A2(fun, lbounds, ubounds, budget):
    #Initial population = Only one parent X ( mu=1 )
    for j in range(n):
        X.append(np.random.uniform(lbounds,ubounds))
    s=0#weighted sum for adaptation step size
    sr=0 #weighted sum for adaptation of step size sigma_r    
    sigma=[]#vector of n variables :all individual step sizes
    r=[]# a vector of n variables : direction vector used to produce line mutation
    sigma_r=0 #step size for direction 
    f=fitness(fun,X)
    while(f>optimum and iter<=budget):#while not happy loop
        #Reproduction (A2)
        for k in range(Lambda):#foreach offspring
            zrk=np.random.normal(0,1,1); #choose a normal distributed random zr 
            zk=np.random.normal(0,1,n)#vector of n normal. dist. rand. variables for the k-th offspring
            X_Nk=[] #initialize the k-th offspring
            s_Nk[k]=0 #initialize the weighted sum for adaptation of step size of the k-th offspring
            sr_Nk[k]=0
            sigma_Nk=[]#individual step size for k-th offspring
            r_Nk=[]
            sigma_r_Nk=0
            #foreach variable of the k-th offspring
            for i in range(n):
                #1. Mutation of the object variables
                X_Nk[i][0]=P[i]+sigma[i]*zk[i]+sigma_r*zrk*r[i]
                #2. Adaptation of the individual step sizes
                s_Nk[k]=(1-c)*s+c*(cu*z[k])#WHAT IS ZK???????????
                sigma_Nk[i]=sigma[i][1]*np.exp(B*(np.linalg.norm(s_Nk)-Xn))*np.exp(Bind*(math.fabs(s_Nk[i])-X1))#VERIFY THE FORMULA        
                #Direction adaptation
                sr[k]=max((1-c)*sr+c*(cu*zrk),0)
                r_prime=(1-cr)*sigma_r*r+cr*(X_Nk-P)
                r_Nk=r_prime/np.linalg.norm(r_prime)#VERIFY THIS ONE
                sigma_r_Nk=max(sigma_r*np.exp(Br*(math.fabs(sr_Nk)-X1)),1/3*np.linalg.norm(sigma_Nk))
                
            #Evaluate the k-th offspring
            f_Nk=fitness(fun,X_Nk)
            #Choose the best offspring
            
            #The Elder become the best offspring
            P=X_Nk
                
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
