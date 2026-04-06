def sort_stack(stack: list[int]) -> list[int]:
    if not stack:
        return stack
    
    aux_stack = []
    
    while stack:
        temp = stack.pop()
        
        while aux_stack and aux_stack[-1] > temp:
            stack.append(aux_stack.pop())
        
        aux_stack.append(temp)
    
    while aux_stack:
        stack.append(aux_stack.pop())
    
    return stack


if __name__ == "__main__":
    stack = [5, 2, 7, 1, 9, 3]
  
    sort_stack(stack)
    print(stack)