from random import *
import datetime
import random
import csv
import os

class Test2:
    
    def __init__(self,input):
        self.input = input
        self.names = ["Nathasha","Logan","Ben","Jack","Nick","Hitman","Dale","Chester","Ghazi","Jerry","Oscar","Matt","Ryan","Lilly","Portia","Dania","Karabo","Mpumi","Ntokozo","Palesa"]
        self.surnames = ["Hadebe","Visser","Donker","Trump","Pele","Dube","Swazi","De Kock","Nel","Moodley","Grobblar","Benjami","Johnson","Peters","Jacob","Zulu","Mthembu","De Klerk","Stroud","Khan"]
        self.records = [["Id","Name","Surname","Initials","Age","DateofBirth"]]
        self.noRecords = 1

    def DataPopulating(self):
        while self.noRecords != self.input + 1:
            selectedName = random.choice(self.names)
            selectedSurname = random.choice(self.surnames)
            currentDate = datetime.datetime.now()
            randomDate = datetime.datetime(randint(1900, 2000), randint(1, 12), randint(1, 28)) 
            record = [selectedName,selectedSurname, selectedName[0] + selectedSurname[0], str(currentDate.year - randomDate.year) , randomDate.strftime("%d/%m/%Y")]
              
            
            if record in self.records:
                continue
            else:    
                self.records.append([str(self.noRecords)] + record)
                self.noRecords += 1   

        return self.records
    
    def WriteCSV(self, records):
        file = open(r'output.csv', 'w+', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerows(records)
        print("output.csv was created into folder: '{0}'".format(os.getcwd()))

if __name__ == "__main__":
    while True:
        try:
            inputSize = int(input("Please enter amount to be generated(whole number): "))
            person = Test2(inputSize)
            person.WriteCSV(person.DataPopulating())
            break
        except:
            print("Program has been terminated or invalid input Data type was entered...\n")

