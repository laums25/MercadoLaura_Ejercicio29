Ej29.png : Ej29.dat Ejercicio29.py
	python Ejercicio29.py

Ej29.dat : Ejer.x
	./Ejer.x

Ejer29.png : Ejer29.dat Ejercicio29.py
	python Ejercicio29.py

Ejer29.dat : Ejer.x
	./Ejer.x


Ejercicio29.png  : Ejercicio29.dat Ejercicio29.py
	python Ejercicio29.py

Ejercicio29.dat  : Ejer.x
	./Ejer.x 

Ejer.x : MercadoLaura_Ejercicio29.cpp
	c++ MercadoLaura_Ejercicio29.cpp -o Ejer.x
	
clean:
	rm Ejer.x Ejercicio29.dat Ejercicio29.png
