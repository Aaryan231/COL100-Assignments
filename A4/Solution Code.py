# MAKING A CALCULATOR


list1 = ["+", "-", "*", "/", "(", ")"]


# list1 is established


def calculate(a, b, x):
    if x == "+":
        return a + b
    elif x == "-":
        return a - b
    elif x == "*":
        return a * b
    elif x == "/":
        return a / b


def readNumber(s, i):
    # ASSERT: String s and index i are established
    q = ""
    # This If Loop is there to recognize negative numbers
    if s[i] == "-":
        q += str(s[i])
        i += 1
    for x in range(i, len(s)):
        # INV: All the s[a] from s[i] to s[x - 1] will not contain any elements from list1
        for a in list1:
            if s[x] == a:
                # ASSERT: String q will give us a substring consisting of just the number while x gives the index
                #         of the index of next element of string s after last element of substring q.
                return float(q), x
        q += str(s[x])


def evalParen(s, i):
    # ASSERT: String s and index i are established
    if s[readNumber(s, i + 1)[1]] == ")":
        return s[(i + 1):(readNumber(s, i + 1)[1])], readNumber(s, i + 1)[1] + 1
    result = calculate(readNumber(s, i + 1)[0], readNumber(s, readNumber(s, i + 1)[1] + 1)[0],
                       s[readNumber(s, i + 1)[1]])
    # ASSERT: result will give us the value of a single parenthesized expression while the 2nd term of the tuple will
    #         give us the index of next element of s remaining after calculating the parenthesis
    return result, (readNumber(s, readNumber(s, i + 1)[1] + 1)[1] + 1)


def evaluate(s):
    brackets = False
    # String s and boolean brackets is established
    for x in range(len(s)):
        # INV: For all s[a] in s[0],s[1]...s[x - 1] do not contain "(" or ")"
        if s[x] == "(" or s[x] == ")":
            brackets = True
            break
    if not brackets:
        # ASSERT: The string s will get modified to contain opening and closing parenthesis if it did not have them
        #         initially
        return evaluate("(" + s + ")")
    for i in range(len(s)):
        # INV: At any point, this loop always finds the innermost parenthesized expression and solves it using the
        #      evalParen function and recursively solves the new string
        if s[i] == "(":
            c = 1
            while c > 0:
                if s[i + c] != "(":
                    if s[i + c] == ")":
                        if i + c == len(s) - 1 and i == 0:
                            # ASSERT: evalParen(s, 0)[0] gives us the final result after all the recursive calculations
                            return evalParen(s, 0)[0]
                        else:
                            return evaluate(s[:i] + str(evalParen(s, i)[0]) + s[(i + c + 1):])
                    else:
                        c += 1
                else:
                    break


# A SEQUENCE OF UNIQUE SUMS


def exists(ls, a):
    # List ls and variable a is established
    left = 0
    right = len(ls) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check if a is present at mid
        if a == ls[mid]:
            return True
        elif ls[mid] < a:
            left = mid + 1
        # If a is greater, ignore left half
        else:
            right = mid - 1
        # If a is smaller, ignore right half
    # If we reach here, then a was not present in ls and we return False
    return False


def element(ls):
    # List ls is established
    c = 1
    # INITIALIZATION
    while c > 0:
        # INV: Any number from ls[-1] to ls[-1] + c - 1 is not our desired output and thus can't be a part of the final
        #      list
        count = 0
        for x in range(len(ls)):
            if exists(ls, ls[-1] + c - ls[x]) and 2 * ls[x] != ls[-1] + c:
                count += 1
            if count > 2:
                break
        if count == 2:
            # ASSERT: When we reach here, we have our desired element which is the next element of the list we form in
            #         sumSequence. This element is the smallest number greater than ls[-1] which can be uniquely
            #         represented as sum of 2 elements of the list
            return ls[-1] + c
        c += 1


def sumSequence(n):
    ls = [1, 2]
    # List ls is established
    if n == 1:
        return [1]
    else:
        for x in range(2, n):
            # INV: For every ls[a] in ls[0], ls[1]...ls[x], ls[a] is greater than all ls[a-k] where k is between 1 to a
            #      and ls[a] can be represented as the minimum sum of 2 elements uniquely of the old list
            ls.append(element(ls))
    # ASSERT: When we reach here, the list ls will contain our desired elements
    return ls


# SHORTEST SUBLIST WITH SUFFICIENT SUM


def add(ls):
    output = 0
    for i in ls:
        # INV: After k iterations, where 0 < k <= n, output = ls[0]+ls[1]+....ls[k-1]
        output = output + i
    # ASSERT: This function gives the sum of all the elements of a list
    return output


def min_value(ls):
    y = 0
    for i in range(len(ls)):
        # INV: for every i in 0 to len(ls)-1, ls[y] will be less than ls[i]
        if ls[i] < ls[y]:
            y = i
    # ASSERT: This function gives the value of the minimum element of a list
    return ls[y]


def minLength(ls, a):
    # Input list ls and constraint variable a are established
    output = []
    for i in range(len(ls)):
        # A valid sublist is one whose sum of elements is greater than constraint variable a
        # INV: After each time this loop is executed, the output contains length of lists of those valid sublists whose
        #      index of first element <= i
        for j in range(i + 1, len(ls) + 1):
            # INV: After each time this loop is executed, the output contains length of lists of those valid sublists
            #      whose index of last element <= j
            if add(ls[i:j]) > a:
                output.append(j - i)

    if len(output) == 0:
        # ASSERT: If we reach here, that means no sublist of the list exist where sum of elements exceeds a and hence
        #         we return -1
        return -1
    # ASSERT: We get the minimum length of the sublist such that sum of its elements exceeds a
    return min_value(output)


# MERGING A CONTACT LIST


def mergeAB(arr, b, l, m, r):
    i = l  # Initial	index	of	first	subarray
    j = m  # Initial	index	of	second	subarray
    k = l  # Initial	index	of	merged	subarray
    while i < m and j < r:
        if arr[i] <= arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1
    # Copy remaining elements of arr[i:m], if there are any
    while i < m:
        b[k] = arr[i]
        i += 1
        k += 1
    # Copy remaining elements of arr[j:r], if there are any
    while j < r:
        b[k] = arr[j]
        j += 1
        k += 1


def merge(A, B, n, l):
    # List A of size n consists of n/l sorted list of size l each (Last list may be shorter)
    # We merge them in pairs, writing the result in B (There may be 1 unpaired list if total number of lists is odd)
    right = 0
    if n % l == 0:
        count = n // l
    else:
        count = n // l + 1
    for i in range(count // 2):
        left = i * l * 2
        right = min(left + (2 * l), n)
        mergeAB(A, B, left, left + l, right)
    # Copy the last list if there is any (may happen if count is odd)
    for i in range(right, n):
        B[i] = A[i]


def mergeSort(A):
    n = len(A)
    l = 1
    B = [0 for x in range(n)]
    count = 0
    while l < n:
        if count == 0:
            merge(A, B, n, l)
            count = 1
        else:
            merge(B, A, n, l)
            count = 0
        l *= 2
    # If result is in B, we copy the result to A
    if count == 1:
        for i in range(n):
            A[i] = B[i]


def mergeContacts(ls):
    # Input list ls is established and sorted using mergeSort
    mergeSort(ls)
    i = 0
    output = []
    result = []
    # INITIALIZATION
    while i < len(ls) - 1:
        # INV: If the first element of the tuple ls[i] from the list of tuple ls, if ls[i] is equal to ls[i + 1], that
        #      means that the name of person is same, hence we need to appends both the e-mails into a single list for
        #      one name. If the names are not equal, that means the e mails belong to different people and hence we
        #      don't append those e-mails into a single list.
        if ls[i][0] == ls[i + 1][0]:
            result.append(ls[i][1])
        else:
            result.append(ls[i][1])
            output.append((ls[i][0], result))
            result = []
        i += 1
    # The if-else statement below is there to deal with the last element of the input list
    if ls[i][0] == ls[i - 1][0]:
        result.append(ls[i][1])
        output.append((ls[i][0], result))
    else:
        output.append((ls[i][0], ls[i][1]))
    # ASSERT: In the output, the mails of people with common name get appended into a single list which is then returned
    #         as a list of tuples in the end.
    return output

#             x-x-x-x-x-x-x-x-x-x-x-x-x-x-  END OF CODE  -x-x-x-x-x-x-x-x-x-x-x-x-x-x
