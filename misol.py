class Numbers:
    def __init__(self,number):
        self.number=number
        return number

    
    
    def is_even(self):

        return True if self.number%2==0 else False
    def is_odd(self):
        return True if self.number%2==1 else False
    def is_prime(self):
        for i in self.number:
            if i%1==0 and i%i==0:
                return True
            else:
                return False
    def get_lenght(self):
        return len(list(self.number))
    
    def get_sum(self):
        return sum(int(self.number))

    def get_product(self):
        for i in self.number:
            m=[]
            if i.isdigit():
                m.append(i)
        return m
    def get_reverse(self):
        self.number.reverse()
        return self.number
    
    def get_digits(self):
        for i in self.number:
            m=0
            if i.isdigit():
                m+=1
        return m

    def get_max(self):
        return max(int(self.number))

    def get_min(self):
        return min(int(self.number))

    def get_average(self):
        return sum(int(self.number))/len(self.number)

    def get_median(self):
        if len(self.number)%2==1:
            return self.number[len(self.number)//2]
        if len(self.number)%2==0:
            return [len(self.number)//2],[(len(self.number)//2)-1]
    def get_range(self):
        for i in self.number:
            
            m=i.range(21)
                
        return m
    
