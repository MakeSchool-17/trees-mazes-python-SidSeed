import maze


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
   backtrack=[]
   random_cell = random.randint(1,m.total_cells-1)
   visited = [0] * m.total_cells
   visited[random_cell] = 1
   while(visited.count(1) < m.total_cells ):
       cells_neighbor=m.cell_neighbors(random_cell)
       if(len(cells_neighbor)>=1):
            random_neighbor=cells_neighbor[random.randint(0,len(cells_neighbor)-1)]
            m.connect_cells(random_cell,random_neighbor[0],random_neighbor[1])
            backtrack.append(random_cell)
            random_cell = random_neighbor[0]
            visited[random_cell]=1
       else:
        random_cell=backtrack.pop()
       m.refresh_maze_view()
   m.state='solve'

def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
