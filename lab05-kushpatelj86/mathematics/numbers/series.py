def sum(list=[1,2,3,5,6]):
    sum = 0
    for i in list:
        sum += i
    return sum



def average(list=[1,2,3,5,6]):
    sum = 0
    for i in list:
        sum += i
    if len(list) == 0:
        return 0
    else:
        average = sum / len(list)
        return average
    
