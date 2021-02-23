#checks input of number
#for repeated numbers
#returns True if present
def is_rep():

        l1= input("enter 10 numbers:")
        l2= []
        l3=[]
        n=0
        for i in l1:
            l2.append(i)
        l2.sort()
        # loops through l1 to find repeated numbers
        #this uses a while loop to prevent index out range error
        #if a copy is found
        #the copy can be removed and the new array is output
        #or the array can be output with the original and copy
        #if no copy is found, the array is output
        #this has a linear time complexity of 0(n)
        # because we have to sort through the whole array to find the copy
        while n<len(l2):
            print(n,",,,")
            for i in range(len(l2)-1):
                print(l2[i], l2[i+1])
                if l2[i]==l2[i+1]:
                    l3.append(l2[i+1])

                n += i

        return (f"copy found in array: {l3}") if len(l3)>0 else "no copy found"









print(is_rep())


