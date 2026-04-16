def smallest(n:float, m:float) -> float:
    if n < m:
        return n #For which calls below is this statement evaluated? neither
    else:
        return m

first = smallest (3,2) #What is the value of first? 2
second = smallest (2,2)  #What is the value of second? 2
# Is this a reasonable result?   # Why or why not? Yes because the function is n < m which is true cause 2 isn't less than 2
print()