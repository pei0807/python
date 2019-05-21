# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def main():
    list = [2,7,11,15,20,40,60]
    list1=[0]
    target = 100


    index1=findIndex(list1,target)
    print('index found to be %i and %i' %(index1,index1+1))

def findIndex(list, target):
    if len(list) >1:
        for ind in range(0,len(list)-1,1):
            total = list[ind]+list[ind+1]
            if total == target:
                return ind
    else:
        print('length of list less than 2')
        exit()



main()