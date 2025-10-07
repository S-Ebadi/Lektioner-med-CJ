# Miniövning 4
# Skapa en klass Alarm som:
# har ett attribut type
# räknar antal larm som skapats (Klassvariabel)
# Skriver ut sin typ via __str__ 

class Alarm:
    count = 0

    def __init__(self, type):
        self.type = type
        Alarm.count += 1

    def __str__(self):
        return f"Alarm type: {self.type}, total alarms: {Alarm.count}"
    
a1 = Alarm("CPU")
a2 = Alarm("Memory")
a3 = Alarm("Disk")

print(a1)
print(a2)
print(a3)

print(f"Total alarms created: {Alarm.count}")
