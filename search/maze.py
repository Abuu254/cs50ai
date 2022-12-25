import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__ (self):
        self.frontier = []

    # Add item to frontier
    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier.")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier.")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# the maze

class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            


    def solve(self):
        """Finds solution to maze"""
        # keep track of states explored
        self.num_explored = 0

        # Initialize frontier to starting position
        start = Node(state=self.start, parent=None, action=None)
        frontier = StackFrontier()
        frontier.add(start)

        #intialize an empty of explored set
        self.explored = set()
        # Loop until solution is found
        while True:

            # if nothing left in stack, no solution
            if frontier.empty():
                raise Exception("no solution.")

            # Choose a node from the frontier
            node = frontier.remove()
            self.num_explored +=1

            # check if it is the answer
            if node.state == self.goal:
                actions = []
                cells = []

                # back track to find path
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return
            # if not the path






