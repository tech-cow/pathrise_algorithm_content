def countHi2(s):
    '''
    Given a string, compute recursively the number of times lowercase "hi" appears in the string,
    however do not count "hi" that have an 'x' immedately before them.
    countHi2("ahixhi") → 1
    countHi2("ahibhi") → 2
    countHi2("xhixhi") → 0

    rules:
    countHi2(s) returns the number of occurences of "hi" in str s, except when 'x' appears in front of "hi"
    induction hypothesis: for any given s2 which len(s2) < len(s), countHi2(s2) works as intended

      nil rules:

    '''

    n = len(s)
    if n <= 3:
        if s == 'xhi': return 0
        if 'hi' in s: return 1
        return 0

    if 'hi' in s[:3]:
        if s[:3] == "xhi": return 0 + countHi2(s[3:])
        if s[0] == 'h': return 1 + countHi2(s[2:])
        return 1 + countHi2(s[3:])
    return 0 + countHi2(s[1:])

# nil's solution
    n = len(s)
    if n < 2:
        return 0
    if n == 3:
        if 'hi' in s and s != 'xhi':
            return 1
        return 0
    if s[0] == 'h' and s[1] == 'i':
        return 1 + countHi2(s[2:])
    elif s[:3] == "xhi":
        return countHi2(s[3:])
    return countHi2(s[1:])

    #you can do this with both strings and arrays

    '''
    s2 = s
    s2 = s[:]
    s2[0] = 1

    s2 = s       reference
    s2 = s[:] <- make a copy
    '''

    """
    Time Complexity: O(N^2)
    Space Complexity: O(N^2)
    Always: Time complexity >= (non-input) Space complexity
    """




## Start typing heredef groupSum(arr, target):
    '''
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target?
    This is a classic backtracking recursion problem.
     Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a
    space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at index start and
    continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed
    -- the recursive calls progress down the array.


    groupSum([1, 2, 8], 10) → true
    groupSum([2, 4, 8], 14) → true
    groupSum([2, 4, 8], 9) → false

    Yu's steps:
    1. groupSum(arr, target) returns boolean indication of sum of subsets from 'arr' that adds to the 'target'
    2.a) induction hypothesis: for any array of arr2 and integer of 'target2', which len(arr2) < len(arr) and 'target2' == 'target' , groupSum(arr2, target2) works as intended
    2.b) induction hypothesis: for any array of arr2 and integer of 'target2', which len(arr2) < len(arr), groupSum(arr2, target2) works as intended

    2.b) is more "general" aka "powerful" aka "versatile" aka "can be used in more cases"
    Takeaway: don't add unnecessary constraints to your induction hypothesis.

    Nil's steps:
    1. groupSum(arr, target) returns whether there exists a subset in 'arr' with sum equal to 'target'
    2. induction hypothesis:  for any array 'arr2' and integer 'target2' with len(arr2) < len(arr), groupSum(arr2, target2) works as intended
    3.


    **Reason why I find it to be difficult:**
- [ ]  The problem that I solved before, each adjancent element within strings or arrays are nicely correlated, not the case for this problem
- [ ]  If we assume our indusction hypothesis, if our `groupSum(arr2)` already solved the problem, it's pretty much done already..
    - [ ]  So 1 instance I was thinking was:

                `if n >= 3:
                    return True + groupSum(arr[3:])`
            Which doesn't make sense.


    '''
    # n = len(arr)
    # if not arr: return False
    # if n < 3: return sum(arr) == target

# Nil's solution
def groupSum(arr, target):
    # induction hypothesis: for any array 'arr2' and integer 'target2' with len(arr2) < len(arr), groupSum(arr2, target2) works as intended

    #base case
    n = len(arr)
    if n == 0:
        return target == 0

    #general case
    return groupSum(arr[1:], target-arr[0]) or groupSum(arr[1:], target) #include x or not include x


    """
    [1,2,8], target=9
    [2,1,8], target=9
    """

def groupSum(arr, target):
    n = len(arr)

    # base case
    if n < 2:
        return arr[0] == target
    if n == 2:
        return sum(arr) == target

    # induction hypothesis:  for any array 'arr2' and integer 'target2' with len(arr2) < len(arr), groupSum(arr2, target2) works as intended
    return groupSum(arr[1:], target - arr[0]) or
    #                                   ^
    #                             add arr[0] to the subset that adds up to target

    """
    There exists a subset of [1,2,8] which adds up to 9 if there is a subset of [2,8] which adds up to 9-1.

    """

    [1     |    ,2,8]   target = 9

    1 and 8 -> 9
    I am not consider 1



    [2,1,8]

    [2 |   1,8]






    """
    You don't need a general case for each base case.
    The two are unrelated. You can have 1 genreal case and 3 base cases or 3 general cases and 1 base case

    Avoid redundant calls
    """










Given the head of a singly linked list, reverse the list, and return the reversed list.



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """


    """
    Yu's version:
        reverseList(head) takes ListNode object 'head', it returns a reversed version of the linked list, where the new 'head' points to the tail of the linked list
        induction hypothesis:
            assume the size of the linkedlist is n, and the linkedlist is indexing from 0 to n
            for any ListNode head1 that is not at index 0, reverseList(head1) works as intended

    """

    """
    Nil's version:
    reverseList(head) reverses the linked list starting at 'head' in-place and returns the new head.
    Induction hypothesis: for any node 'v' such that len(v) < len(head), reverseList(v) works as intended,
    where len(node) means the number of nodes in the linked list starting at 'node'.
    """

    # base case
    if head == None:
        return None
    if head.next == None:
        return head
    # general case (head is not None)

    #observation: the second node (head.next) becomes the new tail after the recursive call
    secondNode = head.next  # save pointer to the 2
    lastNode = reverseList(head.next) # takes 2 -> 3 -> 4 -> 5 -> NULL and returns 5 -> 4 -> 3 -> 2 -> NULL
    secondNode.next = head # plug the 1 at the end
    return lastNode # return the 5

    #takeaway: induction still works when the function has side-effects (not only when it returns something)


    """

    1 -> 2 -> 3 -> 4 -> 5 -> NULL
    ^
    head

    reverseList(head.next) takes
    2 -> 3 -> 4 -> 5 -> NULL
    and returns (by induction hypothesis)
    5 -> 4 -> 3 -> 2 -> NULL
    ^
    new head

    what I really want is

    5 -> 4 -> 3 -> 2 -> 1 -> NULL
    ^
    new head

    """



    """
    takeaway: the induction hypothesis lives in the universe of math, not in the universe of code.
    You don't need to compute the length of the list in order to mention it in the induction hypothesis.

    """
