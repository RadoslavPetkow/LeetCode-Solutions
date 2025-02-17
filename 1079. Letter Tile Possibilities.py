from itertools import permutations

class Solution(object):
    def numTilePossibilities(self, tiles):
        unique_perms = set()

        for length in range(1, len(tiles) + 1):
            for perm in permutations(tiles, length):
                unique_perms.add("".join(perm))

        return len(unique_perms)
        
