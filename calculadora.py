class matematica(object):
	
	titulo = 'calculadora'
	operaciones = ['division','multiplicacion','suma','resta']
	espacio = ('=' * 80)
	

	def __init__(self):
		print self.espacio + '\n\n' + self.titulo + '\n\n' + self.espacio
		self.opc()
	
	def opc(self):
		print 'por favor escoja una de las siguientes opciones'
		print 'puede elegir entre escribir el nombre o el numero'
		contador = 1
		for x in self.operaciones:
			print '%s(%d)' % (x,contador),
			contador = contador + 1
		opcion = raw_input('\n>> ')
		if opcion == '1' or opcion.lower() == 'division':
			self.division()
		elif opcion == '2' or opcion.lower() == 'multiplicacion':
			self.multiplicacion()
		elif opcion == '3' or opcion.lower() == 'suma':
			self.suma()
		elif opcion == '4' or opcion.lower() == 'resta':
			self.resta()
		else:
			print 'opcion invalida'
			self.opc()

	def division(self):
		self.numeros()
		try:
			self.num1 / self.num2
		except ZeroDivisionError:
			print 'no puedes dividir %d entre %d\n' %(self.num1,self.num2)
			self.division()
		else:
			res = self.num1 / self.num2
			print 'El resultado de la division de %d entre %d es igual a %d' % (self.num1,self.num2,res)

	def multiplicacion(self):
		self.numeros()
		res = self.num1 * self.num2
		print 'El resultado de la multiplicacion de %d * %d es igual a %d' % (self.num1,self.num2,res)

	def suma(self):
		self.numeros()
		res = self.num1 + self.num2
		print 'el resultado de la suma de %d + %d es igual a %d' % (self.num1,self.num2,res)

	def resta(self):
		self.numeros()
		res = self.num1 - self.num2
		print 'el resultado de la resta de %d - %d es igual a %d' % (self.num1,self.num2,res)	

	def numeros(self):
		print self.espacio
		print 'ingrese los numeros'
		try:
			self.num1 = int(raw_input('>> '))
			self.num2 = int(raw_input('>> '))
		except ValueError:
			print 'No es un valor valido.\nPor favor vuelva a intentelo de nuevo.\n'
			self.numeros()
		
		

operacion = matematica()
