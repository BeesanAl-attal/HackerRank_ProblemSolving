# create your tools 
def find_percentage(query_name):
    for name1 in student_marks.keys():
        if name1 == query_name:
            mark_percentage = float(sum(student_marks[name1])) / float(len(student_marks[name1])) 
            formatted_number = f"{mark_percentage:.2f}" # formate the value to output value like this 56.00
            print(formatted_number)   
            
        else:
          continue
        

#execution 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
#use your tools 
find_percentage(query_name)
# the issue that faced me is trying to output the value like 56.00 not 56.0 
# and to solve that issue i  formatedd the calculated percentage  as stated in the above code 