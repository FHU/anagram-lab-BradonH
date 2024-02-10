#REMOVE PASS AND FIX THIS FUNCTION
def anagram(a,b):
    a.replace(' ', '')
    b.replace(' ', '')
    list1 = []
    list2 = []
    for x in range(len(a)):
        list1.append(a[x])
    for y in range(len(b)):
        list2.append(b[y])
    if len(a) == len(b):
        for w in range(len(a)):
            if a[w] in b == True:
                print('yep')
                return True
            else:
                return False
    else:
        return False
                

if __name__ == '__main__':
    #REMOVE PASS YOUR CODE GOES HERE
    word1 = input()
    word2 = input()
    word1.replace(' ', '')
    word2.replace(' ', '')
    list1 = []
    list2 = []
    for x in range(len(word1)):
        list1.append(word1[x])
    for y in range(len(word2)):
        list2.append(word2[y])
    anagram(list1, list2)