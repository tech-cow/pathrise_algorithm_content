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
    return 5 + bunny_ear(n - 2)

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

    # yu:
    if n < 10:
        return 1 if n == 7 else 0
    return count7(n // 10) + count7(n % 10)

    # nil:
    if n == 0:
        return 0
    return count7(n // 10) + 1 if n % 10 == 7 else 0

# Yu:


def countX(s):
    '''
    Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.

    countX("x | xhixx") → 4
    countX("xhixhix") → 3
    countX("hi") → 0

    countX(s): return the number of lowercase 'x' cahrs in the given string s
    induction hypothesis: for k < len(s) , countX(ss with lenght of k)
    return the number of lowercase 'x' cahrs in the given string ss
    '''

    n = len(s)

    if n == 0:
        return 0
    if n == 1:
        return 1 if s == 'x' else 0
    return countX(s[1:]) + countX(s[:1])

# Nil:


def countX(s):
    '''
    countX(s) returns the number of 'x' in s
    induction hypothesis: for any string s2 such that len(s2) < len(s), countX(s2) works as intended
    '''
    if len(s) == 0:
        return 0
    return countX(s[1:]) + 1 if s[0] == 'x' else 0


def change_pi(s):
    # Given a string, compute recursively(no loops) a new string where all appearances of "pi" have been replaced by "3.14".
    # changePi("xpix") → "x3.14x"
    # changePi("pipi") → "3.143.14"
    # changePi("pip") → "3.14p"
    '''
    change_pi(s) replaces all of the "pi" in s to "3.14" , when length == len(s)
    induction hypothesis: for any string s2 such that len(s2) < len(s), change_pi(s2) works as intended
    '''
    n = len(s)
    # edge + base:
    if n == 0: return ""
    if n == 1: return s

    if s[0] == 'p' and s[1] == 'i':
        return "3.14" + change_pi(s[2:])
    return s[:1] + change_pi(s[1:])

def array11(nums):
    # Given an array of ints, compute recursively the number of times that the value 11 appears in the array.
    # array11([1, 2, 11]) → 1
    # array11([11, 11]) → 2
    # array11([1, 2, 3, 4]) → 0

    # index will always be valid from 0 -> n - 1
    '''
    array11(nums, index) return the frequency of appearence for value 11 in array "nums" from size 0 to len(nums)
    induction hypothesis: for any array nums2 that len(nums2) < len(nums), array11(s2) works as intended
    '''
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1 if nums[0] == 11 else 0
    return array11(nums[:1]) + array11(nums[1:])



def pairStar(s):
    '''
    Given a string, compute recursively a new string where identical chars that are adjacent in the original string are separated
    from each other by a "*".
    pairStar("hello") → "hel*lo"
    pairStar("xxyy") → "x*xy*y"
    pairStar("aaaa") → "a*a*a*a"


    pairStar(s) returns a modified s1 from s, which that it inserts an '*' to separate adjacent repeated alphabetic character
    induction hypothesis: for any string of s2, where len(s2) < len(s1), pairStar(s2) works as intended
    '''

    # Edge
    if len(s) < 2: return s

    # Base
    if s[0] == s[1]:
        return s[0] + '*' + pairStar(s[1:])
    return s[:1] + pairStar(s[1:])

    print(pairStar("hello"), pairStar("xxyy"), pairStar("aaaa"))



def countAbc(s):
    # Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
    #
    # countABC(s): return the total number of "abc" and "aba" substrings from given s
    # induction hypothesis: for any given s2 that len(s2) < len(s), countABC(s2) works as intended

    if len(s) < 3: return 0
    if s[:3] == "abc" or s[:3] == "aba":
        return 1 + countAbc(s[3:])
    return 0 + countAbc(s[1:])



def stringClean(s):
    # Given a string, return recursively a "cleaned" string where
    # adjacent chars that are the same have been reduced to a single char.
    # So "yyzzza" yields "yza".
    #
    # stringClean(s): return cleaned string where no adjacent chars are repeated
    # induction hypothesis: for any s2 which len(s2) < len(s), stringClean(s2) works as intended
    # print(stringClean("yyzzza"))
    # print(stringClean("abbbcdd"))
    # print(stringClean("Hello"))
    # → "yza" → "abcd" → "Helo"

    if len(s) < 2: return s
    if s[0] == s[1]:
        return stringClean(s[1:])
    return s[0] + stringClean(s[1:])



def countHi2(s):
    '''
    Given a string, compute recursively the number of times lowercase "hi" appears in the string,
    however do not count "hi" that have an 'x' immedately before them.
    countHi2("ahixhi") → 1
    countHi2("ahibhi") → 2
    countHi2("xhixhi") → 0

    rules:
    countHi2(s) return the number of occurences of "hi" in str s, except when 'x' appears in front
    induction hypothesis: for any given s2 which len(s2) < len(s), countHi2(s2) works as intended
    '''

    n = len(s)
    if n < 3:
        if s == 'xhi': return 0
        if 'hi' in s: return 1
        return 0

    if 'hi' in s[:3]:
        if s[:3] == "xhi": return 0 + countHi2(s[3:])
        if s[0] == 'h': return 1 + countHi2(s[2:])
        return 1 + countHi2(s[3:])
    return 0 + countHi2(s[1:])



def parenBit(s):
    # Given a string that contains a single pair of parenthesis, compute recursively a new string made of
    # only of the parenthesis and their contents
    # so "xyz(abc)123" yields "(abc)".

    # parenBit("xyz(abc)123") → "(abc)"
    # parenBit("x(hello)") → "(hello)"
    # parenBit("(xy)1") → "(xy)"

    # parenBit(s) returns a parenthesis of 0 to n character
    # induction hypothesis: for any s2 which |s2| < |s| , parenBit(s2) works as intended

    if len(s) < 2: return None
    if s[0] == '(' and s[-1] == ')':
        return s
    if s[0] != '(':
        return parenBit(s[1:])
    if s[-1] != ')':
        return parenBit(s[:-1])



def nestParen(s):
    # Given a string, return true if it is a nesting of zero or more pairs of
    # parenthesis, like "(())" or "((()))".
    # Suggestion: check the first and last chars, and then recur on what's inside
    # them.

    # nestParen("(())") → true
    # nestParen("((()))") → true
    # nestParen("(((x))") → false
    # nestParen("(((x)))") → true

    if len(s) == 0: return True
    if len(s) == 1:
        if s[0] not in "()":
            return True

    if s[0] == '(' and s[-1] == ')':
        return True and nestParen(s[1:-1])
    return False


def strCopies_diff(s, substr, target):
    # Given a string and a non-empty substring **sub**, compute recursively if at least n copies of sub appear in the string somewhere,
    # possibly with overlapping. N will be non-negative.
    #
    # ```python
    # strCopies("catcowcat", "cat", 2) → true
    # strCopies("catcowcat", "cow", 2) → false
    # strCopies("catcowcat", "cow", 1) → true
    # ```

    # strCopies(s, substr, target) returns booleans indication of whether *s* contains *target* number of *substr*
    # Indunction hypothesis: for any s2, that strCopies(s2, substr, target) works as intended when we assume len(s2) < len(s1)

    # what is the base case exactly?
    # when target == 0 if we keep deducting it?
    #
    #
    # if target == 0:
    #     return True
    #
    # n = len(s):
    # if n < 3:
    #     if s == substr:
    #         target -= 1
    #
    #
    # if s[0] != substr[0]:
    #     return
    pass

def strCopies(s, substr, target):
    # Given a string and a non-empty substring **sub**, compute recursively if at least n copies of sub appear in the string somewhere,
    # possibly with overlapping. N will be non-negative.
    #
    # ```python
    # strCopies("catcowcat", "cat", 2) → true
    # strCopies("catcowcat", "cow", 2) → false
    # strCopies("catcowcat", "cow", 1) → true
    # ```

    # rec_helper(s, substr) returns the number of appearence of substr in s
    # induction hypothesis: for any s2 that |s2| < |s|, rec_helper(s2) works as intended
    def rec_helper(s):
        n = len(s)
        if n == 1 or n == 2: return 0
        if s[:len(substr)] == substr:
            return 1 + rec_helper(s[1:])
        return 0 + rec_helper(s[1:])
    return rec_helper(s) >= target
print(strCopies("cccccccc", "c", 5))
