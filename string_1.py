# check weather it is palindrome

def palindrome(check):
    start = 0
    end = len(check)-1
    while start <= end:
        print(start,end)
        if check[start] != check[end]:
            return 'Not Palindrome'
        start += 1
        end -= 1
    return 'Palindrome'

d = 'doiido'
print(palindrome(d))


# check duplicates in a string
def duplicate_finder(check):
    start = 0
    end = 0
    ans = []
    while start < len(check)-1:
        start += 1
        while end < start:
            if check[start] == check[end]:
                ans.append(check[start])
            end += 1
        end = 0
    return ans

val = [1,2,3,4,5,5,4,3,6,7,32,6,8]
print(duplicate_finder(val))
