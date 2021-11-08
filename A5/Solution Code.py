# PLAY WITH GRID


def gridPlay(grid):
    # ASSERT: Input grid is established
    n = len(grid)
    m = len(grid[0])
    S = [[grid[y][x] for x in range(m)] for y in range(n)]
    # ASSERT: Grid S and variables n & m are established of same dimensions as the input grid with every element as 0
    for i in range(n-2, -1, -1):
        # INV.: All the elements of type S[k][m-1], where n-2 >= k > i, represent the minimum penalty to move from
        #       (k,m-1) to (n-1,m-1)
        S[i][m-1] += S[i+1][m-1]
    # ASSERT: All the elements in the last column of the matrix S denote the minimum penalty to move from that element
    #         to the last element
    for j in range(m-2, -1, -1):
        # INV.: All the elements of type S[n-1][l], where m-2 >=lk > j, represent the minimum penalty to move from
        #       (n-1,l) to (n-1,m-1)
        S[n-1][j] += S[n-1][j+1]
    # ASSERT: All the elements in the last row of the matrix S denote the minimum penalty to move from that element
    #         to the last element
    for i in range(n-2, -1, -1):
        # INV.: All the elements whose index are of type S[l][k], where m-1 >= k > j and n-1 >= l > i, represent the
        #       minimum penalty to move from (l,k) to (n-1,m-1)
        for j in range(m-2, -1, -1):
            # INV.: For some fixed i, all the elements whose index are of type S[i][k], where m-1 >= k > j, represent
            #       the minimum penalty to move from (i,k) to (n-1,m-1)
            S[i][j] += min(S[i+1][j], S[i+1][j+1], S[i][j+1])
        # ASSERT: All the elements in the (i-1)th row of the matrix S denote the minimum penalty to move from that
        #         element to the last element
    # ASSERT: S[0][0] will be the minimum cost of going from (0, 0) to the last element, i.e., (n-1,m-1)
    return S[0][0]


# STRING PROBLEM


vowels = ["a", "e", "i", "o", "u"]
# ASSERT: List of vowels is established


def stringProblem(A, B):
    # ASSERT: Input strings A and B are established
    m = len(A)
    n = len(B)
    l = [[0 for x in range(m+1)] for y in range(n+1)]
    # ASSERT: Matrix l and variables n & m are established of same dimensions as the input grid with every element as 0
    for i in range(n+1):
        # INV.: For 0 <= p < i and 0 <= q < j, l[p][q] denotes the minimum number of changes to change a string
        #       consisting of first (p-1) characters of A to first (q-1) characters of B
        for j in range(m+1):
            # INV.: For some fixed i and 0 <= q < j, l[i][q] denotes the minimum number of changes to change a string
            #       consisting of first (i-1) characters of A to first (q-1) characters of B
            if i == 0:
                l[i][j] = j
            elif j == 0:
                l[i][j] = i
            elif A[j-1] == B[i-1]:
                l[i][j] = l[i-1][j-1]
            else:
                consonantA = True
                consonantB = True
                for alpha in vowels:
                    # INV. : If we are still in this loop, that means that A[j-1] is not any of the vowels before alpha
                    if alpha == A[j-1]:
                        # ASSERT: A[j-1] is a vowel and is thus present in the list of vowels
                        consonantA = False
                        break
                for beta in vowels:
                    # INV. : If we are still in this loop, that means that B[i-1] is not any of the vowels before beta
                    if beta == B[i-1]:
                        # ASSERT: B[i-1] is a vowel and is thus present in the list of vowels
                        consonantB = False

                if not consonantA and consonantB:
                    l[i][j] = min(l[i-1][j] + 1, l[i-1][j-1] + 2, l[i][j-1] + 1)
                else:
                    l[i][j] = min(l[i - 1][j] + 1, l[i - 1][j - 1] + 1, l[i][j - 1] + 1)
        # ASSERT: The elements of (i-1)th row denote the minimum number of allowed changes to change A[:k], where
        #         0 <= k < m, to B[:i] where i is fixed
    # ASSERT: l[n][m] represent the minimum number of allowed changes to change a string A to another string B
    return l[n][m]


# CALENDER PROBLEM


def isLeapYear(n):
    if n % 4 != 0:
        return False
    elif n % 100 == 0 and n % 400 != 0:
        return False
    else:
        return True


def firstDay(n):
    output = 1
    x = 1753
    for a in range(x, n):
        if isLeapYear(a):
            output += 2
        else:
            output += 1

    result = output % 7
    if result == 0:
        return 7
    else:
        return result


months = ["-JANUARY-", " -FEBRUARY-", "   -MARCH-", " -APRIL-", "     -MAY-", "      -JUNE-", "  -JULY-", "   -AUGUST-", "  -SEPTEMBER-", "-OCTOBER-", " -NOVEMBER-", "  -DECEMBER-"]
number = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
odd_days = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
days = ["M", "T", "W", "T", "F", "S", "S"]
final_list = []


def printCalender(year):
    first_day = firstDay(year)
    s = ""
    for x in range(44):
        s += " "
    s += str(year)
    final_list.append(s)
    s = ""
    final_list.append(s)
    for a in range(4):
        for b in range(3*a, 3*(a+1)):
            for c in range(8):
                s += " "
            s += months[b]
            for d in range(15):
                s += " "
        final_list.append(s)
        s = ""
        for e in range(3):
            for day in days:
                s += day + "   "
            s += "      "
        final_list.append(s)
        s = ""
        x = 1
        y = 1
        z = 1
        for f in range(6):
            for g in range(3*a, 3*a + 3):
                if g == 3*a + 1:
                    for h in range(34 - len(s)):
                        s += " "
                elif g == 3*a + 2:
                    for i in range(68 - len(s)):
                        s += " "
                if f == 0:
                    if isLeapYear(year) and g > 1:
                        for j in range(4 * ((first_day + odd_days[g]) % 7)):
                            s += " "
                    else:
                        for k in range(4 * ((first_day + odd_days[g] - 1) % 7)):
                            s += " "
                if g == 3*a:
                    while len(s) != 28 and x <= number[g]:
                        s += str(x)
                        if x < 10:
                            s += "   "
                        else:
                            s += "  "
                        x += 1
                if g == 3*a + 1:
                    if a == 0 and isLeapYear(year):
                        while len(s) != 62 and y <= number[g] + 1:
                            s += str(y)
                            if y < 10:
                                s += "   "
                            else:
                                s += "  "
                            y += 1
                    else:
                        while len(s) != 62 and y <= number[g]:
                            s += str(y)
                            if y < 10:
                                s += "   "
                            else:
                                s += "  "
                            y += 1
                if g == 3*a + 2:
                    while len(s) != 96 and z <= number[g]:
                        s += str(z)
                        if z < 10:
                            s += "   "
                        else:
                            s += "  "
                        z += 1
            final_list.append(s)
            s = ""
            if f == 5:
                for q in range(2):
                    final_list.append(s)

    fl = open("Calender", "w")
    for line in final_list:
        fl.write(line + "\n")