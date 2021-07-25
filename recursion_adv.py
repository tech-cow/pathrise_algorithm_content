def groupSum(arr, target):
    '''
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target?
    This is a classic backtracking recursion problem.
     Once you understand the recursive backtracking strategy in this problem, you can use the same pattern for many problems to search a
    space of choices. Rather than looking at the whole array, our convention is to consider the part of the array starting at index start and
    continuing to the end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed
    -- the recursive calls progress down the array.


    groupSum([2, 4, 8], 10) → true
    groupSum([2, 4, 8], 14) → true
    groupSum([2, 4, 8], 9) → false


    groupSum(arr, target) returns boolean indication of sum of subsets from arr that adds to the target
    induction hypothesis: for any array of arr2, which len(arr2) < len(arr), groupSum(arr2, target) works as intended

    '''
    n = len(arr)
    if not arr: return False
    if n < 3: return sum(arr) == target

    reason why I find it to be difficult:
    * The problem that I solved before, each adjancent element within strings or arrays are nicely correlated, not the case for this problem
    * If we assume our indusction hypothesis, if our groupSum(arr2) already solved the problem, it's pretty much done already..
        So 1 instance I was thinking was:

            if n >= 3:
                return True + groupSum(arr[3:])

        Which doesn't make sense.



def splitOdd10(arr):
    # Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a multiple of 10,
    # and the sum of the other group is odd. Every int must be in one group or the other.
    # Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive
    # helper from splitOdd10(). (No loops needed.)
    #
    #
    # splitOdd10([5, 5, 5]) → true
    # splitOdd10([5, 5, 6]) → false
    # splitOdd10([5, 5, 6, 1]) → true

    splitOdd10(arr) returns the boolean indications of whether the arr can be splited into 2 groups where:
        group 1: sum of group 1 is a multiple of 10
        group 2: sum of the other group is odd

    Induction hypothesis:
        for any array of arr2, which len(arr2) < len(arr), splitOdd10(arr2) works as intended

    Q: what is the value of knowing splitOdd10(arr2) in this case?

        like I can't just say:

        if current index != 10:
            return False
        else:
            return True + splitOdd10(arr2)

        samething with the odd logic.

        Also how to determine do we pick the current element for group 1 or group 2? There is no clear rules around it
