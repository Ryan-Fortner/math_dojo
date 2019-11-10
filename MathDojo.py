
class Math_Dojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num + sum(nums) 
        return self
    
    def subtract(self, num, *nums):
        self.result -= (num + sum(nums))
        return self
    
if __name__ == "__main__":
    md = Math_Dojo()
    x = md.add(2).add(2,5,1).subtract(3,2).result
    print(x)