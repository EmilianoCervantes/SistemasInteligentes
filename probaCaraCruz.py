import random as rd

cara = 0
cruz = 0

for moneda in range(0, 1000):
	if rd.random() < 0.5:
		cara += 1
	else:
		cruz += 1
		
cara = str(cara)
cruz = str(cruz)
print("Veces cara: "+cara+", veces cruz: "+cruz)
