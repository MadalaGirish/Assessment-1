2#
def fibonacci(n):
    sequence =[0,1]
    for i in range(2,n+1):
        next_num =sequence[-1] +sequence[-2]
        sequence.append(next_num)
    return sequence
sequence = fibonacci(13)
print(sequence)







