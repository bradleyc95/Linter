# Bradley Cox, 10/12/2022
# Linter 

# define a stack
class Stack:
    def __init__(self):
        self.items = []
    
    # checks to see if stack is empty, returns bool
    def isEmpty(self):
        return self.size == 0

    # push an item to the top of the stack
    def push(self, item):
        self.items.append(item)

    # pop an item from the top of the stack
    def pop(self):
        self.items.pop

    # return the item at the top of the stack
    def peek(self):
        if self.size() != 0:
            return self.items[-1]
        else:
            return None

    # return the size of the stack
    def size(self):
        return len(self.items)

def Lint(text):

    s = Stack()
    
    for char in text:
        # if char is an opening brace, push character to stack
        if isOpeningBrace(char) == True:
            s.push(char)

        # if char is closing bracket...
        elif isClosingBrace(char) == True:
            # and stack is not empty, save opening brace and pop
            if s.isEmpty() == False:
                poppedOpeningBrace = s.peek()
                s.pop()

            # if stack is empty, same poppedOpeningBrace as none    
            else:
                poppedOpeningBrace = None

            # if no poppedOpeningBrace, return error below
            if poppedOpeningBrace == None:
                return char + " does not have an opening brace."
            
            # if braces do not match, return error below
            if isNotAMatch(poppedOpeningBrace, char) == True:
                return char + " has a mismatched opening brace."

    # if stack is not empty after going through every char, return error below    
    if s.isEmpty() == False:
        return s.peek() + " does not have a closing brace."
    
            

# function to check if char is an opening brace
def isOpeningBrace(char):
    if char in ['(', '[', '{']:
        return True
    else:
        return False

# function to check if char is a closing brace
def isClosingBrace(char):
    if char in [')', ']', '}']:
        return True
    else:
        return False

# function to check if opening and closing braces match
def isNotAMatch(opening, closing):
    if opening == '(' and closing == ')':
        return False
    elif opening == '[' and closing == ']':
        return False
    elif opening == '{' and closing == '}':
        return False
    else:
        return True


t1 = "( lol"
t2 = "lol )"
t3 = "[ lol )"
t4 = "[( lol )"

print(Lint(t1))
print(Lint(t2))
print(Lint(t3))
print(Lint(t4))