'''
Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively (without loops).
factorial(1) → 1
factorial(2) → 2
factorial(3) → 6
'''
def factorial(n):
    '''
    idea:
        base case: when n == 1: return 1
        we assume that factorial(n - 1) will return factorial of n - 1
        if we start at n, then I will get my factorial by n * factorial(n - 1)
    '''
    if n == 1:
        return 1

    return n * factorial(n - 1)



'''
We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..)
we'll say have 3 ears, because they each have a raised foot.
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
'''

def bunny_ear(n):
    '''
    idea:
        base case:
            when n == 0: return 0
            when n == 1: return 2
        we assume that bunny_ear(n) returns the number of ears in a bunny line with n bunnies
    '''
    # bunny_ear(n-1) + bunny_ear(n-2)
    # the number of ears in a bunny line with n-1 bunnies plus the number of ears in a bunny line with n-2 bunnies
    # is this the number of ears in a bunny line with n bunnies?

    if n == 0:
        return 0
    if n == 1:
        return 2
    return 5 + bunny_ear(n-2)

    # if n % 2 == 1:
    #     return 2 + bunny_ear(n - 1)
    # else:
    #     return 3 + bunny_ear(n - 1)

    # last_bunny = 2 if n % 2 == 1 else 3
    # return last_bunny + bunny_ear(n - 1)



'''
Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

count7(717) → 2
count7(7) → 1
count7(123) → 0
'''

def count7(n):
    '''
    yu: count7(n) return the count of the occurrences of 7 as a digit when the given number is n
    nil: count7(n) returns the number of digits in n that are equal to 7

    induction hypothesis: for any k < n, count7(k) works as intended

    '''

    '''
    717 no correlation 716
    717 might has correlation wiht 7 | 1 | 7

    yu: if size is the length of the number
        I have iterator i to loop over the number(assuming we str(number))
        count7(i) + count7(rest of the digits)


    count7(n // 10) + count7(n % 10)


    Debug case n = 717
    n // 10 = 71
    n % 10 = 7
    count7(n // 10) = count7(71) = the number of digits in 71 that are equal to 7 = 1
    count7(n % 10) = count7(7) = the number of digits in 7 that are equal to 7 = 1
    count7(n // 10) + count7(n % 10) = 2


    Debug case n = 7777
    n // 10 = 777
    n % 10 = 7
    count7(n // 10) = count7(777) = the number of digits in 777 that are equal to 7 = 3
    count7(n % 10) = count7(7) = the number of digits in 7 that are equal to 7 = 1
    count7(n // 10) + count7(n % 10) = 4


    Debug case n = 5
    n // 10 = 0
    n % 10 = 5
    count7(n // 10) = count7(0) = the number of digits in 0 that are equal to 7 = 0
    count7(n % 10) = count7(5) != the number of digits in 5 that are equal to 7 = 0
    count7(n // 10) + count7(n % 10) = 4
    '''

    #yu:
    if n < 10:
        return 1 if n == 7 else 0
    return count7(n // 10) + count7(n % 10)

    #nil:
    if n == 0:
        return 0
    return count7(n // 10) + 1 if n%10 == 7 else 0


# Yu:
def countX(s):
    '''
    Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

    countX("x | xhixx") → 4
    countX("xhixhix") → 3
    countX("hi") → 0

    countX(s): return the number of lowercase 'x' cahrs in the given string s
    induction hypothesis: for k < len(s) , countX(ss with lenght of k) return the number of lowercase 'x' cahrs in the given string ss
    '''

    n = len(s)

    if n == 0: return 0
    if n == 1: return 1 if s == 'x' else 0
    return countX(s[1:]) + countX(s[:1])

#Nil:
def countX(s):
    '''
    countX(s) returns the number of 'x' in s
    induction hypothesis: for any string s2 such that len(s2) < len(s), countX(s2) works as intended
    '''
    if len(s) == 0:
        return 0
    return countX(s[1:]) + 1 if s[0] == 'x' else 0
