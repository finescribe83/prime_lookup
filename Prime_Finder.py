
def factorial_function(num):
    num_count = int(num)
    factor_list=[]

    while num_count>0:
        ind = num % num_count
        if ind==0:
            factor_list.append(num_count)

        num_count-=1

    return(factor_list)


prime_list=[]

prime_list_count= int(input('No. of primes to lookup: '))

nm_series=1

while prime_list_count>len(prime_list):

    if len(factorial_function(nm_series))<3:
        prime_list.append(nm_series)
    
        print(len(prime_list),' primes added on list') 

    nm_series+=1


print(prime_list)
        
    






    
