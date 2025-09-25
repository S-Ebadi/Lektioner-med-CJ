#Variabler & Datatyper
#En variabel är ett namn som pekar på ett värde.
#Datatyper är t.ex. int (heltal), float (decimaltal), str (text), bool (True/False).

#Uppgifter:
#Skapa variablerna name (str), age (int), height (float).
name = "Said"
age = 41
height = 1.88

#Skriv ut variablerna med print().
print(name)
print(age)
print(height)

#Använd type() för att ta reda på datatyperna.
print(type(name))
print(type(age))        
print(type(height)) 

#Input & utskrift
#Med input() kan du läsa in från användaren. Print() skriver ut till konsolen.
#Uppgifter:
#Fråga användaren om deras favoritfärg och skriv ut ett svar.
color = input("Vad är din favoritfärg? ")
print(f"Din favoritfärg är {color}.")

#Fråga efter två tal och skriv ut summan.
tal1 = int(input("Skriv in det första talet: "))
tal2 = int(input("Skriv in det andra talet: "))
print("Summan blir:", tal1 + tal2)

#Testa att skriva ut med f-strängar, t.ex.:
name = input("Vad heter du? ")
age = int(input("Hur gammal är du? "))
print(f"Hej {name}, du är {age} år gammal.")

#Strängformattering
#Strängar kan kombineras och formateras.
#Uppgifter:
#Skapa en sträng som säger "Mitt namn är ... och jag är ... år" med variabler.
name = "Said"
age = 41
print(f"Mitt namn är {name} och jag är {age} år.")

#Låt användaren skriva in en mening och skriv ut den i versaler (upper()).
sentence = input("Skriv en mening: ")
print(sentence.upper())

#Ta reda på längden av en sträng med len().
print("Antal tecken i meningen:", len(sentence)) 

#Loopar & villkor
#Loopar gör att kod körs flera gånger. If-satser används för logik.
#Uppgifter:
#Skriv en loop som skriver talen 1 till 10.
for i in range(1, 11):
    print(i)

#Skriv en loop som räknar ner från 5 till 1 och sedan skriver "Klar!"
for i in range(5, 0, -1):
    print(i)
print("Klar!")

#Fråga användaren om ålder och skriv om de är myndiga eller inte.
age = int(input("Hur gammal är du? "))
if age >= 18:
    print("Du är myndig.")
else:
    print("Du är inte myndig.")

#Listor
#En lista kan lagra flera värden i en ordnad samling.
#Uppgifter:
#Skapa en lista med tre favoritfilmer.
filmer = ["Scarface", "Interstellar", "The Dark Knight"]

#Lägg till en film med append().
filmer.append("Rambo First Blood")

#Skriv ut hela listan med en for-loop.
for film in filmer:
    print(film)

#Skriv ut endast den första och sista filmen
print("Första filmen:", filmer[0])
print("Sista filmen:", filmer[-1])

#Dictionaries
#En dictionary lagrar data i nyckel–värde-par.
#Uppgifter:
#Skapa en dictionary för en användare med nycklarna 'namn', 'ålder', 'stad'.
user = {
    "name": "Said", 
    "age": 42,
    "city": "Stockholm"
}

#Skriv ut värdena med print().
print(user["name"])
print(user["age"])
print(user["city"])

#Lägg till en ny nyckel 'favoritfärg'.
user["Favorite color"] = "Blue"

#Loopa igenom dictionaryn och skriv ut alla nycklar och värden
for key, value in user.items():
    print(f"{key}: {value}")  

#Mini-projekt: Kombinera
#Bygg ett litet program som:
#Frågar användaren efter namn, ålder och favoritfärg
#Sparar informationen i en dictionary.
user = {}
user["name"] = input("What is your name? ")
user["age"] = int(input("How old are you? "))
user["favorite_color"] = input("What is your favorite color? ")

#Lägger till användarens favoritfilmer i en lista.
filmer = []
print("Skriv tre favoritfilmer:")
for i in range(3):
    film = input(f"Film {i+1}: ")
    filmer.append(film)
#Sparar listan i dictionaryn under nyckeln 'favorite_movies'.
user["favorite_movies"] = filmer

#Skriver ut en personlig hälsning och sammanfattning av informationen.
print("\n--- Sammanfattning ---")
print(f"Hej {user['name']}! Du är {user['age']} år gammal och din favoritfärg är {user['favorite_color']}.")
print("Dina favoritfilmer är:")
for film in user["favorite_movies"]:
    print(f"- {film}")

#Om användaren är under 18, skriv en extra rad: "Du är minderårig."
if user["age"] < 18:
    print("Du är minderårig.")