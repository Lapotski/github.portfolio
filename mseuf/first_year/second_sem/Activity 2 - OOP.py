# ACTIVITY 2: OOP
# Kyla Dessirei L. Dequito (M001)

class Employee:
    
    #class constructor and attributes initializer
    def __init__(self):
        self._name = ""
        self._gender = ""
        self._bd = ""
        self._position = ""
        self._rate = 0
        self._daysWork = 0
        
    #encapsulated properties
    @property
    def getName(self):
        return self._name

    @getName.setter
    def setName(self, name):
        self._name = name

    @property
    def getGender(self):
        return self._gender

    @getGender.setter
    def setGender(self, gender):
        self._gender = gender
    
    @property
    def getBd(self):
        return self._bd

    @getBd.setter
    def setBd(self, bd):
        self._bd = bd
        
    @property
    def getPosition(self):
        return self._position
    
    @getPosition.setter
    def setPosition(self, position):
        self._position = position

    @property
    def getRate(self):
        return self._rate
    
    @getRate.setter
    def setRate(self, rate):
        self._rate = rate
        
    @property
    def getDaysWork(self):
        return self._daysWork
    
    @getDaysWork.setter
    def setDaysWork(self, days_work):
        self._daysWork = days_work
        

    #salary computation methods
    def getGross(self):
        gross = self._daysWork * self._rate
        return gross
    
    
    def getSSS(self):
        gross = self.getGross()
        if gross < 10000:
            return 500
        elif gross < 20000:
            return 1000
        else:
            return 1500
        
    def getTax(self):
        gross = self.getGross()
        if gross < 10000:
            return 0
        elif gross < 20000:
            return gross * 0.10
        elif gross < 30000:
            return gross * 0.20
        else:
            return gross * 0.25
        
    def getSalary(self):
        net = self.getGross() - self.getSSS() - self.getTax()
        return net
    
    def get_eDetails(self):
        eDetails = f'\nName: {self._name} \nGender: {self._gender} \nBirth Date: {self._bd} \nPosition: {self._position}'
        return eDetails
    
    def get_sDetails(self):
        sDetails = f'\nGross Salary: ₱{self.getGross():,.2f} \nSSS: ₱{self.getSSS():,.2f} \nTax: ₱{self.getTax():,.2f} \nNet Salary: ₱{self.getSalary():,.2f}'
        return sDetails
    
        
def main():
    name = input("Enter Employee Name: ")
    gender = input("Enter Gender (M/F): ")
    bd = input("Enter Birth Date: ")
    position = input("Enter Position: ")
    rate = float(input("Enter Rate per day: "))
    days_work = float(input("Enter Days Worked: "))

    e1= Employee()
    e1.setName = name
    e1.setGender = gender
    e1.setBd = bd
    e1.setPosition = position
    e1.setRate = rate
    e1.setDaysWork = days_work
    
    
    print("------------------------------------------------")
    print(f'\nEmployee Details: \n{e1.get_eDetails()}\n')
    print("------------------------------------------------")
    print(f'\nSalary Details: \n{e1.get_sDetails()}\n')
    print("------------------------------------------------")
    
if __name__ == "__main__":
    main()
