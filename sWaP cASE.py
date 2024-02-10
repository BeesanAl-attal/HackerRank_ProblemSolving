def swap_case(s):
    modified_string = ''
    for char in s:
        
        if char.isupper() :
            char = char.lower()
        else:
            char = char.upper()
        modified_string += char 
        
    return modified_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

    