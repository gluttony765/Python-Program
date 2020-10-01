def dectobinary(n):                        #Made the code into a recursive function
        if n==1:
            return(str(1)) 
        else:
           return(str(n%2)+dectobinary(n//2))
# To run the code
s=dectobinary(293)
print(s)
#Output = 101001001
