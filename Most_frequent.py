import operator
W= input('Please enter a string ')
d=dict() 
def most_frequent(string):
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
print (most_frequent(W))
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
