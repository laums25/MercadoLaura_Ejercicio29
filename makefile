Ejercicio29.png  : Ejercicio29.dat Ejercicio29.py
	python Ejercicio29.py

Ejercicio29.dat  : Ejer.x
	./Ejer.x 

Ejer.x : MercadoLaura_Ejercicio29.cpp
	c++ MercadoLaura_Ejercicio29.cpp -o Ejer.x
	
clean:
	rm Ejer.x Ejercicio29.dat Ejercicio29.png
