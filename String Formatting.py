# one of the most important methods for strings is slicing 
# which we used in our code 

def print_formatted(number):
  # space padding --> having a space trailing before 
  #the 'number' (in that context) in another words aligning, 'justifying'
  padding_width = len(bin(number)[2:])

  for i in range(1, (number + 1)):
    decimal = str(i)
    octal = oct(i)[2:] # string slicing from index 2 till the end 
    hexa = hex(i)[2:].upper()
    binary = bin(i)[2:]
    print(decimal.rjust(padding_width), octal.rjust(padding_width), hexa.rjust(padding_width), binary.rjust(padding_width))
   



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)