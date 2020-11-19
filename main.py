from jednostki import jednostki
from dziesiatki import dziesiatki
from setki import setki
from tysie import tysie

num = abs(int(input("Wprowadź dowolną cyfrę od 0 do 9999: ")))

string = str(num)
dlugosc = len(string)
jedval = int(string[-1])

if num < 20:
	print(jednostki(num))

elif num % 10 == 0 and num < 100:
	print(dziesiatki(num))

elif dlugosc == 2:
	dzesval = int(string[0] + "0")
	print(f'{dziesiatki(dzesval)} {jednostki(jedval)}')

elif num % 100 == 0 and num < 1000:
	print(setki(num))

elif dlugosc == 3:
	setval = int(string[0] + "00")
	dzesval = int(string[1] + "0")
	print(f'{setki(setval)} {dziesiatki(dzesval)} {jednostki(jedval)}')

elif num % 1000 == 0 and num < 10_000:
	print(tysie(num))

elif dlugosc == 4:
	tysval = int(string[0] + "000")
	setval = int(string[1] + "00")
	dzesval = int(string[2] + "0")
	print(f'{tysie(tysval)} {setki(setval)} {dziesiatki(dzesval)} {jednostki(jedval)}')

else:
	print("Out of range")