class GoalBasedAgent:
    def __init__(self, start_position, goal_position, grid_size):
        self.current_position = start_position
        self.goal_position = goal_position
        self.grid_size = grid_size
        self.path = [] 
    def perceive_environment(self):
       return self.current_position, self.goal_position

    def plan_action(self):
        queue = [(self.current_position, [])] 
        visited = {self.current_position}

        while queue:
            (r, c), current_path = queue.pop(0)

            if (r, c) == self.goal_position:
                self.path = current_path
                return

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]: 
                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < self.grid_size[0] and \
                   0 <= new_c < self.grid_size[1] and \
                   (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append(((new_r, new_c), current_path + [(new_r, new_c)]))
        
        print("No path found to the goal.")
        self.path = [] 
    def execute_action(self):
        if self.path:
            next_step = self.path.pop(0)
            print(f"Moving from {self.current_position} to {next_step}")
            self.current_position = next_step
            return True
        else:
            print("No more steps in the plan or goal reached.")
            return False

    def is_goal_reached(self):
        return self.current_position == self.goal_position

if __name__ == "__main__":
    grid_size = (5, 5)
    start = (0, 0)
    goal = (4, 4)

    agent = GoalBasedAgent(start, goal, grid_size)

    print(f"Agent starting at {agent.current_position}, aiming for {agent.goal_position}")

    agent.plan_action()

    while not agent.is_goal_reached():
        if not agent.execute_action():
            break 
    if agent.is_goal_reached():
        print(f"Goal reached at {agent.current_position}!")
    else:
        print("Agent failed to reach the goal.")