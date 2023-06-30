# A recursive Python3 function to check
# if two linked lists are identical
# or not
def areIdentical(a,b):
    #If both lists are empty
    if (a==None and b==None):
        return True
    # If both lists are not empty,
    # then data of current nodes must
    # match, and same should be recursively
    # true for rest of the nodes.
    if (a != None and b != None):
        return ((a.data == b.data) and
                areIdentical(a.next , b.next))
    return False

if __name__ == '__main__':
    a=[1,2,3,4]
    b=[1,2,3,4]
    if (a==b):
        print("Identical ")
    else:
        print("Not identical ")


