from collections import deque


class Problem(object):
    def __init__(self, init_state, goal_state):
        self.initial_state = init_state;
        self.goal_state = goal_state;
        self.state_space = {};
        self.state_space['Arad'] = {'R1': 'Zerind', 'R2': 'Sibiu', 'R3': 'Timisoara'};
        self.state_space['Zerind'] = {'R1': 'Oradea', 'R2': 'Arad'};
        self.state_space['Oradea'] = {'R1': 'Sibiu', 'R2': 'Zerind'};
        self.state_space['Timisoara'] = {'R1': 'Lugoj', 'R2': 'Arad'};
        self.state_space['Lugoj'] = {'R1': 'Timisoara', 'R2': 'Mehandia'};
        self.state_space['Drobeta'] = {'R1': 'Mehandia', 'R2': 'Craiova'};
        self.state_space['Craiova'] = {'R1': 'Drobeta', 'R2': 'Rimnicu Vilcea', 'R3': 'Pitesti'};
        self.state_space['Rimnicu Vilcea'] = {'R1': 'Sibiu', 'R2': 'Pitesti', 'R3': 'Craiova'};
        self.state_space['Sibiu'] = {'R1': 'Arad', 'R2': 'Fagaras', 'R3': 'Oradea', 'R4': 'Rimnicu Vilcea'};
        self.state_space['Fagaras'] = {'R1': 'Sibiu', 'R2': 'Bucharest'};
        self.state_space['Pitesti'] = {'R1': 'Rimnicu Vilcea', 'R2': 'Craiova', 'R3': 'Bucharest'};
        self.state_space['Bucharest'] = {'R1': 'Fagaras', 'R2': 'Pitesti', 'R3': 'Giurgiu', 'R4': 'Urziceni'};
        self.state_space['Giurgiu'] = {'R1': 'Bucharest'};
        self.state_space['Urziceni'] = {'R1': 'Bucharest', 'R2': 'Valsui', 'R3': 'Hirsova'};
        self.state_space['Hirsova'] = {'R1': 'Eforie', 'R2': 'Urziceni'};
        self.state_space['Eforie'] = {'R1': 'Hirsova'};
        self.state_space['Valsui'] = {'R1': 'Urziceni', 'R2': 'Iasi'};
        self.state_space['Iasi'] = {'R1': 'Valsui', 'R2': 'Neamt'};
        self.state_space['Neamt'] = {'R1': 'Iasi'};
        self.state_space['Mehandia'] = {'R1': 'Lugoj', 'R2': 'Drobeta'};

        self.step_cost = {};
        self.step_cost['Arad'] = {'R1': 75, 'R2': 140, 'R3': 118};
        self.step_cost['Zerind'] = {'R1': 71, 'R2': 75};
        self.step_cost['Oradea'] = {'R1': 152, 'R2': 71};
        self.step_cost['Timisoara'] = {'R1': 111, 'R2': 118};
        self.step_cost['Lugoj'] = {'R1': 111, 'R2': 70};
        self.step_cost['Drobeta'] = {'R1': 75, 'R2': 120};
        self.step_cost['Craiova'] = {'R1': 120, 'R2': 146, 'R3': 138};
        self.step_cost['Rimnicu Vilcea'] = {'R1': 80, 'R3': 97, 'R4': 146};
        self.step_cost['Sibiu'] = {'R1': 140, 'R2': 99, 'R3': 151, 'R4': 80};
        self.step_cost['Fagaras'] = {'R1': 99, 'R2': 211};
        self.step_cost['Pitesti'] = {'R1': 97, 'R2': 138, 'R3': 101};
        self.step_cost['Bucharest'] = {'R1': 211, 'R2': 101, 'R3': 90, 'R4': 85};
        self.step_cost['Giurgiu'] = {'R1': 90};
        self.step_cost['Urziceni'] = {'R1': 85, 'R2': 142, 'R3': 98};
        self.step_cost['Hirsova'] = {'R1': 86, 'R2': 98};
        self.step_cost['Eforie'] = {'R1': 86};
        self.step_cost['Valsui'] = {'R1': 142, 'R2': 92};
        self.step_cost['Iasi'] = {'R1': 92, 'R2': 87};
        self.step_cost['Neamt'] = {'R1': 87};
        self.step_cost['Mehandia'] = {'R1': 70, 'R2': 75};

    def Actions(self, state):
        lst = self.state_space[state].keys()
        return lst

    def Result(self, state, action):
        return self.state_space[state][action]

    def Goal_test(self, state):
        return state == self.goal_state

    def Path_cost(self, state, action):
        return self.step_cost[state][action]


# ______________________________________________________________________________
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return "<Node {} {}>".format(self.state, self.path_cost)

    def __lt__(self, node):
        return isinstance(node, Node) and self.state < node.state

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state


# -----------------------------------------------------------------------------
def child_node(problem, parent, action):
    next_state = problem.Result(parent.state, action)
    step_cost = problem.Path_cost(parent.state, action)
    next_node = Node(next_state, parent, action, parent.path_cost + int(step_cost))
    return next_node


def solution(node):
    path_back = []
    while node:
        path_back.append(node)
        node = node.parent
    for n in reversed(path_back):
        print(n)


# ______________________________________________________________________________
def DFS(problem):
    node = Node(problem.initial_state)
    if problem.Goal_test(node.state): return solution(node)
    frontier = deque()
    frontier.append(node)
    explored = []
    while True:
        if not frontier: return print('Failure')
        node = frontier.pop()
        explored.append(node.state)
        for action in problem.Actions(node.state):
            child = child_node(problem, node, action)
            if child.state not in explored and child not in frontier:
                if problem.Goal_test(child.state):  return solution(child)
                frontier.append(child)
            # End of if
        # End of for
    # End of while


# ____________________________________________________________________________
# Program main part
p = Problem('Arad', 'Bucharest')
DFS(p)
