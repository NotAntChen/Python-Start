def twosum(inputarr,target):
    #initialize output array with zeroes for now
    outputarr = [0,0]
    #for n elements in the input array
    for i in range(len(inputarr)):
        #sum the i-th element with another element inside of the array
        for j in range(i+1,len(inputarr)):
            #if sum of the two elements matches the target, return an output array that has the indices of the two numbers
            if inputarr[i] + inputarr[j] == target:
                outputarr[0] = i
                outputarr[1] = j
                return outputarr

input = [2,7,11,15]
target = 9
print(twosum(input,target))
input2 = [3,2,4]
target2 = 6
print(twosum(input2,target2))
input3 = [3,3]
target3 = 6
print(twosum(input3,target3))

