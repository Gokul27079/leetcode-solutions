class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        empty = []
        for num in nums:
            if num != 0:
                empty.append(num)

        for num in nums:
            if num == 0:
                empty.append(num)
                
        nums[:] = empty


                    
                   

                 
 
    

            
            
        
  
