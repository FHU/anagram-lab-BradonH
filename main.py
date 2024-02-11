#REMOVE PASS AND FIX THIS FUNCTION
def anagram(a,b):
    a = a.lower()
    b = b.lower()
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    list1 = []
    list2 = []
    for x in range(len(a)):
        list1.append(a[x])
    for y in range(len(b)):
        list2.append(b[y])
    if len(a) == len(b):
        for w in range(len(a)):
            if a[w] in b:
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
    anagram(word1, word2)