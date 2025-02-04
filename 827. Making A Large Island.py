from collections import deque


class Solution:
    def largestIsland(self, grid):
        n = len(grid)

        if n == 0:
            return 0

        def bfs_label_island(start_row, start_col, island_id):
            queue = deque([(start_row, start_col)])
            grid[start_row][start_col] = island_id
            area = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        queue.append((nr, nc))
                        area += 1
            return area

        area_map = {}
        island_id = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area_map[island_id] = bfs_label_island(r, c, island_id)
                    island_id += 1

        if not area_map:
            return 1

        max_island_size = max(area_map.values())

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    distinct_islands = set()
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] != 0:
                            distinct_islands.add(grid[nr][nc])

                    new_area = 1
                    for island_id_neighbor in distinct_islands:
                        new_area += area_map[island_id_neighbor]

                    max_island_size = max(max_island_size, new_area)

        return max_island_size

