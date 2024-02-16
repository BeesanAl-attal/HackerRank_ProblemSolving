# one of the most fun problems in hacker rank a bit hard but for me when it comes to drawing graphs 
# my first step is studying the graph to find the pattern i need to work one, then i divide the graph to parts and start writing my code 
# then the rest is try and fail till you get it right 

def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet = alphabet[:size] # because the size specifies the letters that you will use 
    # the below two line of code are used to iterate through the pattern of the rangoli in the correct order
    indices = list(range(size))
    indices = indices[:-1] + indices[::-1] 
    for i in indices:
        start_index = i + 1
        original = alphabet[-start_index:]
        reverse = original[::-1]
        row = reverse + original[1:]
        row = "-".join(row)
        width = size * 4 - 3
        row = row.center(width, "-")
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)