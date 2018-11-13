
def chack_id(lengh,str_id):
    if lengh>9:
         return 0

    for x in str_id:
        if ord(x) < 48 or  ord(x) >57:           
             return 0

    return 1
def fii_zero (lengh,str_id):
    num=9-lengh 
    zero_digit=num*"0"
    str_id=str_id+zero_digit
    return  str_id

def fun_index(lengh,str_id):

    arr_new=[0,0,0,0,0,0,0,0,0]
    for x in range(0,lengh):    
        if x % 2 != 0:
            arr_new[x]=((int)(str_id[x]))*2
        else:
            arr_new[x]=((int)(str_id[x]))  

    
    return arr_new
            
         

def fun_plus(lengh,a):
    sum1=0
    
    for x in range(0,lengh):
        if a[x] >9:
            digit_one=((int)(a[x]%10))
            digit_ten=((int)(a[x]/10))
            a[x]=digit_one+digit_ten
        sum1=sum1+a[x] 
    print(a)  
    print(sum1)
    
    if sum1%10==0:
        return 1
 
    else:
        return 0
    

 

        
str_id=(input("Please enter your ID number...\n"))
lengh=len(str_id)

while not chack_id(lengh,str_id):
    str_id=input("Your ID number is wrong enter again...\n")
    lengh=len(str_id)

if lengh < 9:
     str_id= fii_zero(lengh,str_id)

print(str_id)
print(fun_index(lengh,str_id))
if fun_plus(lengh,fun_index(lengh,str_id))==1 :
    print("the id Correct") 
else:
    print("the id not Correct")






  









