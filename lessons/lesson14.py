new_number=0
vacabruary= {"I":1, "V": 5, "X":10, "L": 50,"C":100, "D": 500, "M":1000}
number=input('Enter number: ')

class Transform():
    def __init__(self, number):
        self.number=number
    
    def transformer(self, number):
        for i in number:
            if(i=vacabruary[:]):
                global new_number.append(vacabruary[:i])

print(new_number)


   