class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)

    def reverse_string(string):
        result = ''
        for char in string:
            stack.append(char)
        for i in range(len(stack)): #
            result+= stack.pop()
        return result

    def is_balanced1(string):
        stack = deque()
        in_balenced = [] #
        brackets = {'(': ')', '[': ']', '{': '}'}
        for char in string:
            if char in brackets.keys() or char in brackets.values():
                stack.push(char)
        while len(stack) > 0:
            ending_brackets = stack.pop()
            for char1 in stack :
                key =[key for key, value in brackets.items() if value == ending_brackets]
                if key == []:
                    in_balenced.append(ending_brackets)
                    break
                if char1 == key[0]:
                    stack.remove(key[0])
                    break
            else :
                in_balenced.append(ending_brackets)
        if len(in_balenced) == 0:   
            return True
        else:
            return False
        
    def is_match(char1, char2):
        matching = {')': '(', ']': '[', '}': '{'}   
        return char2 == matching[char1]
        
    def is_balanced(string):
        stack = deque()
        for char in string:
            if char in ['(', '[', '{']:
                stack.append(char)
            elif char in [')', ']', '}']:
                if len(stack) == 0 :
                    return False
                    break
                else:
                    if not is_match(char,stack.pop()):
                        return False
        return  stack.size() ==0
                 
        
    
print(reverse_string("We will conquere COVID-19"))
print(  is_balanced("({a+b})"),   #  --> True
        is_balanced("))((a+b}{"), #  --> False
        is_balanced("((a+b))"),   # --> True
        is_balanced("))"), # --> False
        is_balanced("[a+b]*(x+2y)*{gg+kk}")) # --> True
