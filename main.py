from itertools import takewhile


class Matrix:
    def __init__(self, rcs):
        self.matrix = rcs

    def output(self):
        for row in self.matrix:
            print(row)

    def reorder_pivots(self):
        self.matrix.sort(key=(lambda r: len(list(takewhile(lambda a: a == 0, r)))))

    def leading0s(self, row):
        return len(list(takewhile(lambda a: a == 0, row)))

    def rowsum(self, r1, r2, scale):
        ans_row = []
        for i in range(len(r1)):
            ans_row.append(r1[i] - (scale * r2[i]))
        return ans_row

    def gaussian(self):
        matrix.output()
        print("\n\n")
        nrows = len(self.matrix)
        for row_index in range(nrows):

            # Part 1 - Scaling the row of the matrix so the pivot is equal to 1.
            row_copy = self.matrix[row_index]
            pivot_index = self.leading0s(row_copy)
            pivot = row_copy[pivot_index]
            self.matrix[row_index] = list(map(lambda a: a/pivot, row_copy))
            row_copy = self.matrix[row_index]

            # Part 2 - Subtracting the specific row from every other row below it.
            for row_index_sub in range(row_index+1, nrows):
                scale = self.matrix[row_index_sub][pivot_index]
                print(scale)
                this_row_copy = self.matrix[row_index_sub]
                self.matrix[row_index_sub] = self.rowsum(this_row_copy, row_copy, scale)


# Basic stuff.
num_rows = int(input("Input number of rows:     "))
m = []

# Converts input to matrix form.
for i in range(num_rows):
    m.append([int(i) for i in input().split()])
    checker = (list(map((lambda a: len(a)), m)))
    if not (all(i == checker[0] for i in (list(map((lambda a: len(a)), m))))):
        raise Exception("Invalid matrix provided :(")


matrix = Matrix(m)

matrix.reorder_pivots()
matrix.gaussian()

matrix.output()