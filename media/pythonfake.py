class Car:
	carCount=0

	def __init__(self,color,model):
		self.color =color
		self.model =model
		Car.carCount +=1

	def displayCount(self):
		print("Total Employee %d" % Car.carCount)

	def displayCar(self):
		print ("Color : ",self.color, "Model: ",self.model) 


car1=Car("red","BMW")
car1.displayCount()
car1=Car("red","BMW")
car1.displayCount()
car1=Car("red","BMW")
car1.displayCount()
car1=Car("red","BMW")
car1.displayCount()
		

