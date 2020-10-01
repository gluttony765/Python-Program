def decToBinary(n): 
      
    # array to store 
    # binary number 
    binaryNum = [0] * n; 
  
    # counter for binary array 
    i = 0; 
    while (n > 0):  
  
        # storing remainder  
        binaryNum[i] = n % 2; 
        n = int(n / 2); 
        i += 1;  
  
    # printing binary array 
    for j in range(i - 1, -1, -1): 
        print(binaryNum[j], end = ""); 
