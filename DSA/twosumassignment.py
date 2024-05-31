import array

def twosum(inputarr,target):
    outputarr = [0,0]
    for i in range(len(inputarr)):
        for j in range(i+1,len(inputarr)):
            if inputarr[i] + inputarr[j] == target:
                outputarr = [i,j]
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

