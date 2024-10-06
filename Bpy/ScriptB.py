def carga_datos():
    list = []
    for x in range(5):
     num = int(input("Ingrese un numero:"))
     list.append(num)
    return list
    
def generate_list(list):
   positive=[]
   negative=[]
   for number in list:
      if number >=0:
         positive.append(number)
      elif number <= 0:
         negative.append(number)
   print(f"numeros positivos: {positive} \n numeros negativos:{negative}")
   return[positive, negative]

numerot=carga_datos()
generate_list(numerot)