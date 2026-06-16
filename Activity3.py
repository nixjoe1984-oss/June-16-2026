import array as arr
a=arr.array("i",[1, 3, 5, 3, 7, 9, 3])
print("Original array: "+str(a))
print("Number of occurences of thhe number 3 in the array: "+str(a.count(3)))
a.reverse()
print("Reversed array is:")
print(str(a))