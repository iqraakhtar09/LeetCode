class Solution:
    
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while(num > 1):
            if num%2 == 0:  
                counter += 1
            else:
                counter +=2
            num = num//2
        if num == 1:
            counter += 1
        return counter
        
            
        