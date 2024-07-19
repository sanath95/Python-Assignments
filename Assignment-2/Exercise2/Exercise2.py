def count_squares(coordinates):
    # time complexity = O(1)
    # space complexity = O(1)
    n = len(coordinates)
    all_squares = []

    # time complexity = O(n*(n+2)*(n+2)*(n+2)) = O(n^4)
    # space complexity = O(n*n) = O(n^2)
    for i in range(n):
        p1 = coordinates[i]

        for j in range(n):

            if i == j: continue
            p2 = coordinates[j]

            if (p1[0] == p2[0]):

                for k in range(n):

                    if i == k or j == k: continue
                    p3 = coordinates[k]

                    if ((p1[1] == p3[1]) and (abs(p1[1]-p2[1]) == abs(p1[0]-p3[0]))):

                        for l in range(n):

                            if i == l or j == l or k == l: continue
                            p4 = coordinates[l]

                            if ((p2[1] == p4[1]) and (p3[0] == p4[0])):
                                square = [p1, p2, p3, p4]
                                square.sort(key = lambda point: (point[0], point[1]))
                                all_squares.append(square)

    unique_squares = []
    # time complexity = O(n + 1) = O(n)
    # space complexity = O(n)
    for square in all_squares:
        if square not in unique_squares:
            unique_squares.append(square)

    return len(unique_squares)

if __name__ == '__main__':

    coordinates = [[0,0], [0,1], [1,1], [1,0], [2,1], [2,0], [3,1], [3,0]]
    print(count_squares(coordinates))

# overall time complexity = O(n^4)
# overall space complexity = O(n^2)