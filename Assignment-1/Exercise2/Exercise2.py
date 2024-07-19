def stack_disks(disks):

    # time complexity = O(n log n)
    # space complexity = O(n)
    disks.sort(key = lambda disk: disk[2], reverse=True)

    # time complexity = O(n)
    # space complexity = O(n)
    max_heights = [disk[2] for disk in disks]
    next_best = [None for _ in disks]

    # time complexity = O(n) for outer loop and O(n) for inner loop = O(n^2)
    # space complexity = O(n)
    for i in range(1, len(disks)):
        this_disk = disks[i]
        for j in range(0, i):
            prev_disk = disks[j]
            if prev_disk[0] > this_disk[0] and prev_disk[1] > this_disk[1] and prev_disk[2] > this_disk[2]:
                if max_heights[i] <= max_heights[j] + this_disk[2]:
                    max_heights[i] = max_heights[j] + this_disk[2]
                    next_best[i] = j

    max_height = max(max_heights)

    # time complexity = O(n + 1) = O(n)
    # space complexity = O(n)
    all_max_height_indexes = [i for i in range(len(max_heights)) if max_heights[i] == max_height]

    stacked_disks = []

    # time complexity = O(n^2) where n in number of elements in 'disks' list
    # space complexity = O(n)
    for maxh_idx in all_max_height_indexes:
        combo = []
        while maxh_idx is not None:
            combo = combo + [disks[maxh_idx]]
            maxh_idx = next_best[maxh_idx]
        stacked_disks = stacked_disks + combo

    return stacked_disks

if __name__ == "__main__":

    disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5],]
    stacked_disks = stack_disks(disks)
    print(stacked_disks)

# overall time complexity = O(n^2)
# overall space complexity = O(n)