
from priority_queue import PriorityQueue
from helpers import get_path,offsets,read_maze,is_legal_pos

def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star(maze,start,goal):
    pq = PriorityQueue()
    pq.put(start,0)
    predecessors = {start:0}
    g_values = {start:0}
    
    while not pq.is_empty():
        current_cell = pq.get()

        if current_cell == goal:
            return get_path(predecessors, start, goal)
        
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0]+row_offset, current_cell[1]+col_offset)
            if is_legal_pos(maze,neighbour) and neighbour not in g_values:
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal,neighbour)
                pq.put(neighbour,f_value)
                predecessors[neighbour] = current_cell
    return none

if __name__ == "__main__":
    start_pos = (0,0)
    goal_pos = (2,2)
    maze = [[0] * 3 for row in range(3)]
    
    # maze = read_maze("mazes/mini_maze_bfs.txt")
    result = a_star(maze,start_pos,goal_pos)
    print(result)
    # assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # maze[1][2] = '*'  can used to exclude cell -> path will be different