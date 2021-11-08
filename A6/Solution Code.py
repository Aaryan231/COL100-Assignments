# QUIZ SYSTEM DESIGN


class Quiz:
    # This is the constructor for the Quiz class
    def __init__(self, title, correctAnswers):
        # These are the attributes of the constructor
        self.title = title
        self._answers = correctAnswers

    def copyAnswers(self):
        return self._answers.copy()


class Course:
    # This is the constructor for the Course class
    def __init__(self, courseCode, quiz):
        # These are the attributes of the constructor
        self.courseCode = courseCode
        self._quiz = quiz

    def copyQuiz(self):
        return self._quiz.copy()


class Student:
    # This is the constructor for the Student class
    def __init__(self, entryNo, courses):
        # These are the attributes of the constructor
        self.entryNo = entryNo
        self._courses = courses
        self.marks = []

    def attempt(self, courseCode, quizTitle, attemptedAnswers):
        for course in self._courses:
            if courseCode == course.courseCode:
                for quiz in course.copyQuiz():
                    if quizTitle == quiz.title:
                        if len(self.marks) == 0:
                            for i in range(len(attemptedAnswers)):
                                if attemptedAnswers[i] == quiz.copyAnswers()[i]:
                                    attemptedAnswers[i] = 1
                                else:
                                    attemptedAnswers[i] = 0
                            self.marks.append((course.courseCode, quiz.title, sum(attemptedAnswers)))
                        else:
                            for a in range(len(self.marks)):
                                if self.marks[a][0] == courseCode and self.marks[a][1] == quizTitle:
                                    break
                                elif a == len(self.marks) - 1:
                                    for i in range(len(attemptedAnswers)):
                                        if attemptedAnswers[i] == quiz.copyAnswers()[i]:
                                            attemptedAnswers[i] = 1
                                        else:
                                            attemptedAnswers[i] = 0
                                    self.marks.append((course.courseCode, quiz.title, sum(attemptedAnswers)))
    # ASSERT: The attempt function leads to a quiz being attempted by a student and their input answers are stored

    def getUnattemptedQuizzes(self):
        output = []
        for course in self._courses:
            for quiz in course.copyQuiz():
                for a in range(len(self.marks)):
                    if self.marks[a][0] == course.courseCode and self.marks[a][1] == quiz.title:
                        break
                    elif a == len(self.marks) - 1:
                        output.append((course.courseCode, quiz.title))
                        break
        # ASSERT: We get the list of unattempted quizzes as the final output
        return output

    def getAverageScore(self, courseCode):
        x = 0
        y = 0
        for i in range(len(self.marks)):
            if self.marks[i][0] == courseCode:
                x += self.marks[i][2]
                y += 1
        # ASSERT: We get the average score in a particular course for a student as the final output
        if y == 0:
            return 0
        else:
            return x / y


# MATRICES


class Matrix:
    # This is the constructor for the Matrix class
    def __init__(self, matrix):
        # These are the attributes of the constructor
        self.matrix = matrix
        self.row = len(self.matrix)
        self.column = len(self.matrix[0])

    def __str__(self):
        s = ""
        for i in range(self.row):
            for j in range(self.column):
                m = self.matrix[0][j]
                for x in range(self.row):
                    if len(str(m)) < len(str(self.matrix[x][j])):
                        m = self.matrix[x][j]
                for a in range(len(str(m)) - len(str(self.matrix[i][j]))):
                    s += " "
                s += str(self.matrix[i][j]) + "  "
            s += "\n"
        # ASSERT: s returns the matrix in the nicely formatted way
        return s

    def __add__(self, r):
        # ASSERT: Matrices are compatible to be added
        assert self.row == r.row and self.column == r.column
        output = [[0 for x in range(self.column)] for y in range(self.row)]
        # List of lists output is established
        for i in range(self.row):
            for j in range(self.column):
                output[i][j] = self.matrix[i][j] + r.matrix[i][j]
        # ASSERT: Final output is A+B and belongs to the matrix class
        return Matrix(output)

    def __sub__(self, r):
        # ASSERT: Matrices are compatible to be subtracted
        assert self.row == r.row and self.column == r.column
        output = [[0 for x in range(self.column)] for y in range(self.row)]
        # List of lists output is established
        for i in range(self.row):
            for j in range(self.column):
                output[i][j] = self.matrix[i][j] - r.matrix[i][j]
        # ASSERT: Final output is A-B and belongs to the matrix class
        return Matrix(output)

    def __mul__(self, r):
        if isinstance(r, int) or isinstance(r, float):
            output = [[self.matrix[y][x] for x in range(len(self.matrix[0]))] for y in range(len(self.matrix))]
            # List of lists output is established
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    output[i][j] *= r

        else:
            # ASSERT: Matrix multiplication is compatible
            assert self.column == r.row
            output = [[0 for x in range(self.column)] for y in range(len(self.matrix))]
            # List of lists output is established
            i = len(self.matrix)
            j = self.column
            for x in range(i):
                for y in range(j):
                    a = 0
                    for k in range(self.row):
                        a += self.matrix[x][k] * r.matrix[k][y]
                    output[x][y] = a
        # ASSERT: Final output is the required result belonging to the matrix class
        return Matrix(output)

    def toSparse(self):
        output = []
        # List output is established
        for i in range(self.row):
            result = []
            # List result is established
            for j in range(self.column):
                if self.matrix[i][j] != 0:
                    result += [(j, self.matrix[i][j])]

            output += [result]
        # ASSERT: Final output is the required result belonging to the SparseMatrix class
        return SparseMatrix(output, self.row, self.column)


class SparseMatrix:
    # This is the constructor of the class
    def __init__(self, sparse_matrix, nrows, ncols):
        # These are the attributes of the constructor
        self.sparse_matrix = sparse_matrix
        self.nrows = nrows
        self.ncols = ncols

    def __str__(self):
        output = [[0 for x in range(self.ncols)] for y in range(self.nrows)]
        # List of lists output is established
        for i in range(self.nrows):
            if len(self.sparse_matrix[i]) != 0:
                for j in range(len(self.sparse_matrix[i])):
                    output[i][self.sparse_matrix[i][j][0]] = self.sparse_matrix[i][j][1]

        s = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                m = output[0][j]
                for x in range(self.nrows):
                    if len(str(m)) < len(str(output[x][j])):
                        m = output[x][j]
                for a in range(len(str(m)) - len(str(output[i][j]))):
                    s += " "
                s += str(output[i][j]) + "  "
            s += "\n"
        # ASSERT: String s returns the matrix in a nicely formatted way
        return s

    def __add__(self, r):
        # ASSERT: Matrix addition is compatible
        assert self.nrows == r.nrows and self.ncols == r.ncols
        output = []
        # List output is established
        for i in range(self.nrows):
            if len(r.sparse_matrix[i]) == 0:
                output += [self.sparse_matrix[i]]
            elif len(self.sparse_matrix[i]) == 0:
                output += [r.sparse_matrix[i]]
            else:
                result = []
                for j in range(self.ncols):
                    c = 0
                    for x in range(len(self.sparse_matrix[i])):
                        if self.sparse_matrix[i][x][0] == j:
                            c += self.sparse_matrix[i][x][1]
                            break
                    for y in range(len(r.sparse_matrix[i])):
                        if r.sparse_matrix[i][y][0] == j:
                            c += r.sparse_matrix[i][y][1]
                            break
                    if c != 0:
                        result += [(j, c)]
                output += [result]
        # ASSERT: Final output is addition of 2 matrices belonging to SparseMatrix class
        return SparseMatrix(output, self.nrows, self.ncols)

    def __sub__(self, r):
        # ASSERT: Matrix subtraction is compatible
        assert self.nrows == r.nrows and self.ncols == r.ncols
        output = []
        # List output is established
        for i in range(self.nrows):
            if len(r.sparse_matrix[i]) == 0:
                output += [self.sparse_matrix[i]]
            elif len(self.sparse_matrix[i]) == 0:
                output += [r.sparse_matrix[i]]
            else:
                result = []
                for j in range(self.ncols):
                    c = 0
                    for x in range(len(self.sparse_matrix[i])):
                        if self.sparse_matrix[i][x][0] == j:
                            c += self.sparse_matrix[i][x][1]
                            break
                    for y in range(len(r.sparse_matrix[i])):
                        if r.sparse_matrix[i][y][0] == j:
                            c -= r.sparse_matrix[i][y][1]
                            break
                    if c != 0:
                        result += [(j, c)]
                output += [result]
        # ASSERT: Final output is subtraction of 2 matrices belonging to SparseMatrix class
        return SparseMatrix(output, self.nrows, self.ncols)

    def __mul__(self, r):
        if isinstance(r, int) or isinstance(r, float):
            output = []
            # List output is established
            if r == 0:
                # If r = 0, then our final output should be a list of empty lists belonging to SparseMatrix class
                for i in range(len(self.sparse_matrix)):
                    output += [[]]
            else:
                for i in range(len(self.sparse_matrix)):
                    result = []
                    for j in range(len(self.sparse_matrix[i])):
                        result += [(self.sparse_matrix[i][j][0], r * self.sparse_matrix[i][j][1])]
                    output += [result]
            # ASSERT: Final output is the required result belonging to the SparseMatrix class
            return SparseMatrix(output, self.nrows, self.ncols)
        else:
            # ASSERT: Matrix multiplication is compatible
            assert self.ncols == r.nrows
            output = []
            # List output is established
            for i in range(self.nrows):
                if len(self.sparse_matrix[i]) == 0:
                    output += [[]]
                else:
                    result = []
                    for j in range(r.ncols):
                        ans = []
                        for k in range(r.nrows):
                            c = 1
                            for x in range(len(self.sparse_matrix[i])):
                                if self.sparse_matrix[i][x][0] == k:
                                    c *= self.sparse_matrix[i][x][1]
                                    break
                                elif x == len(self.sparse_matrix[i]) - 1:
                                    c = 0
                            if len(r.sparse_matrix[k]) == 0:
                                c = 0
                            else:
                                for a in range(len(r.sparse_matrix[k])):
                                    if r.sparse_matrix[k][a][0] == j:
                                        c *= r.sparse_matrix[k][a][1]
                                        break
                                    elif a == len(r.sparse_matrix[k]) - 1:
                                        c = 0
                            ans.append(c)
                        l = sum(ans)
                        result += [(j, l)]
                    output += [result]
            # ASSERT: Final output is the required result belonging to the SparseMatrix class
            return SparseMatrix(output, self.nrows, r.ncols)

    def toDense(self):
        output = [[0 for x in range(self.ncols)] for y in range(self.nrows)]
        # List of lists output is established
        for i in range(self.nrows):
            if len(self.sparse_matrix[i]) != 0:
                for j in range(len(self.sparse_matrix[i])):
                    output[i][self.sparse_matrix[i][j][0]] = self.sparse_matrix[i][j][1]
        # ASSERT: Final output gives a new matrix belonging to the Matrix class
        return Matrix(output)


# MAZE TRAVERSAL


def isPossible(maze, x, y):
    if x > len(maze) - 1 or y > len(maze[0]) - 1 or x < 0 or y < 0:
        return False
    elif maze[x][y] == "_" or maze[x][y] == "E" or maze[x][y] == "S":
        return True
    else:
        return False


def traverseMaze(mazeFile):
    f = open(mazeFile)
    a = []
    line = f.readlines()
    # line represents a list of strings
    for i in line:
        # a contains a list of lists where every sublist contains each string is split about " " without the last
        # element up until the ith string
        L = i.split(" ")
        b = L.pop()
        L.append(b[0])
        a.append(L)
    # a contains a matrix of maze with characters 'X','S','E','_'
    f.close()
    output = []
    # List output is established
    i = 0
    j = 0
    c = 1
    for i in range(len(a)):
        # INV.: a[l][k] is not equal to "S" for 0 <= l < i and 0 <= k < j
        for j in range(len(a[0])):
            # INV.: For some fixed i, a[i][k] is not equal to "S" for 0 <= k < j
            if a[i][j] == "S":
                break
        if a[i][j] == "S":
            break
    # ASSERT: a[i][j] gives the starting position "S"
    while c > 0:
        # The above while loop is there just because we need to run a loop and thus there is no changes on c. So, we
        # keep running in this loop until we return our output
        u = isPossible(a, i - 1, j)
        r = isPossible(a, i, j + 1)
        d = isPossible(a, i + 1, j)
        l = isPossible(a, i, j - 1)
        if a[i][j] == "E":
            # ASSERT: a[i][j] is the ending point of our maze, so we stop here and return the output
            return output
        # Now we give the preference order of the direction we want to move in in the order U > R > D > L as long as we
        # are not backtracking our path.
        elif a[i][j] == "S":
            # ASSERT: a[i][j] is the starting point of the maze
            if u:
                output.append("U")
                i -= 1
            elif r:
                output.append("R")
                j += 1
            elif d:
                output.append("D")
                i += 1
            elif l:
                output.append("L")
                j -= 1
            a[i][j] = "X"
        else:
            if not u and not r and not d and not l:
                # ASSERT: If we reach here, that means we have taken a path which doesn't lead to the ending point.
                #         So, we start backtracking our path until we reach the crossroad where we made the decision
                #         according to our preference order and change all the elements on the path we went to to "X"
                q = output.pop()
                a[i][j] = "X"
                if q == "U":
                    i += 1
                elif q == "R":
                    j -= 1
                elif q == "D":
                    i -= 1
                elif q == "L":
                    j += 1
                a[i][j] = "_"
            # Now, we move through the maze according to our preference order making sure that we never backtrack our
            # path until absolutely necessary
            elif u and output[-1] != "D":
                a[i][j] = "X"
                output.append("U")
                i -= 1
            elif r and output[-1] != "L":
                a[i][j] = "X"
                output.append("R")
                j += 1
            elif d and output[-1] != "U":
                a[i][j] = "X"
                output.append("D")
                i += 1
            elif l and output[-1] != "R":
                a[i][j] = "X"
                output.append("L")
                j -= 1

#                      -x-x-x-x-x-x-x-x-x-x-x-x- END OF CODE -x-x-x-x-x-x-x-x-x-x-x-x-
