"""
Python program to check for balanced paranthesis and brackets ()[]{}
Made by Sneharsh Belsare (Github: neutr0nStar)
"""

class Stack:
    '''
    Stack class: stack data structure implementation in python
    '''
    def __init__(self):
        self._top = -1
        self._stack = []
    
    def push(self, x):
        self._top += 1
        self._stack.append(x)

    def pop(self):
        self._top -= 1;
        self._stack.pop()

    def peek(self):
        return self._stack[self._top]
    
    def isEmpty(self):
        if( self._top == -1):
            return True
        return False

    def __repr__(self):
        return self._stack


# Function to check balanced parenthesis
def checkBalancedParenthesis(inp: str) -> bool:
    s = Stack()
    for c in inp:
        if c == '(':
            s.push('(')
        elif c == '[':
            s.push('[')
        elif c == '{':
            s.push('{')
        elif c == ')':
            if s.isEmpty() or s.peek() != '(':
                return False
            else:
                s.pop()
        elif c == ']':
            if s.isEmpty() or s.peek() != '[':
                return False
            else:
                s.pop()
        elif c == '}':
            if s.isEmpty() or s.peek() != '{':
                return False
            else:
                s.pop()

    if(s.isEmpty()):
        return True
    else:
        return False


# Main
if __name__ == "__main__":
    inp = input("Enter the string to check balance for: ")
    res = checkBalancedParenthesis(inp)
    if res:
        print("Entered string is balanced")
    else:
        print("Entered string is not balanced")
