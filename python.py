def add(a,b):
  answer = a + b
  print(f'{str(a)} + {str(b)} = {answer}' '\n')



def sub(a,b):
  answer = a - b
  print(f'{str(a)} - {str(b)} = {answer}' '\n') 


def mul(a,b):
  answer = a * b
  print(f'{str(a)} * {str(b)} = {answer}' '\n')

def div(a,b):
  answer = a/b
  print(f'{str(a)} / {str(b)} = {answer}' '\n')

while True:
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiply')
    print('D. Division')
    print('E. Exit')
    
    choice = input('Enter your choice:')
    choice = choice.lower()
    if choice == 'a':
      print('Addition')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      add(a,b)
    
    elif choice == 'b':
      print('Subtraction')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      sub(a,b)
    
    elif choice == 'c':
      print('Multiply')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      mul(a,b)
    
    elif choice == 'd':
      print('Division')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      div(a,b)
    
    elif choice == 'e':
      
      print('Program ended')
      quit()
      sub(a,b)
    
    elif choice == 'c':
      print('Multiply')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      mul(a,b)
    
    elif choice == 'd':
      print('Division')
      a = int(input('First number:'))
      b = int(input('Second number:'))
      div(a,b)
    
    elif choice == 'e':
      
      print('Program ended')
      quit()