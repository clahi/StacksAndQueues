class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create an empty stack."""
        self._data = []                 # nonpublic list instance
        
    def __len__(self):
        """Return the number of elements in the stack"""
        return len(self._data)
    
    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._data) == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)        # new item stored at the end of list
        
    def top(self):
        """Return the element at the top of the stack with out poping.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[-1]               # return last item in the list
    
    def pop(self):
        """Remove and return the element at the top of the stack
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data.pop()             # remove last item from list
    
    
    
# A simple application (Reversing a file) using stack.
def reverse_file(filename):
    """Overwrite given file with its contents line-by-line reversed."""
    
    S = ArrayStack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n'))       # we will re-insert newlines when writing
    original.close()
    
    # now we overwrite with contents in LIFO order
    output = open(filename, 'w')        # reopening file overwrites original
    while not S.is_empty():
        output.write(S.pop( ) + '\n')   # re-insert newline characters
        
    output.close()

# Matching Parenthesis
def is_matched(expr):
    """Return true if all delimeters are properly match; False otherwise."""
    lefty = '([{'           # opening delimeters
    righty = ')]}'          # respective closing delims
    S = ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)       # push left delimeter on stack
        elif c in righty:
            if S.is_empty():
                return False    # nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False    # mismatches
    return S.is_empty()         # were all symbols matched

print(is_matched('([)'))

# ------------Matching Tags in a Markup Language-------------
def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')           # find first '<' character
    while j != -1:
        k = raw.find('>', j+1)  # find next '>' character
        if k == -1:
            return False        # invalid tag
        tag = raw[j+1:k]        # strip tag
        if not tag.startswith('/'):     # thi is opening tag
            S.push(tag)
        else:
            if S.is_empty():
                return False    # nothing to match with
            if tag[1:] != S.pop():
                return False    # mismatched delimeter
        j = raw.find('<', k+1)  # find next '<' character (if any)
    return S.is_empty()         # were all opening tags matched?
            
        
    