# -*- coding: utf-8 -*-
"""
SER501 Assignment 5 scaffolding code
created by: Sarthak Tiwari
"""
from collections import deque
import sys
# =============================================================================


class Tree(object):
    """docstring for Tree"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def level_order_traversal(self):
        path = []
        if not self:
            return path
        traversed = 0
        q = deque([self, ])
        while q:
            path.append([])
            for i in range(len(q)):
                curr = q.popleft()
                path[traversed].append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            traversed += 1
        return path
# =============================================================================


class Graph(object):
    """docstring for Graph"""

    def __init__(self, vertices, edges):
        super(Graph, self).__init__()
        n = len(vertices)
        self.matrix = [[0 for x in range(n)] for y in range(n)]
        self.vertices = vertices
        self.edges = edges
        for edge in edges:
            x = vertices.index(edge[0])
            y = vertices.index(edge[1])
            self.matrix[x][y] = edge[2]

    def display(self):
        print(self.vertices)
        for i, v in enumerate(self.vertices):
            print(v, self.matrix[i])

    def DFS_helper(self, src, visited):
        self.visited[self.vertices.index(src)] = True
        for i in range(len(self.vertices)):
            if self.matrix[self.vertices.index(src)][i]:
                if self.visited[i] == False:
                    self.DFS_helper(self.vertices[i], self.visited)

    def DFS(self, src):
        self.visited = [False] * (len(self.vertices))
        self.DFS_helper(src, self.visited)

    def valid_path(self, source, target, intermediate):
        self.visited = []
        self.DFS(source)
        k = False
        if self.visited[self.vertices.index(intermediate)] == True:
            k = True
        self.DFS(intermediate)
        k2 = False
        if self.visited[self.vertices.index(target)] == True:
            k2 = True
        if k and k2:
            return True
        else:
            return False

# Graph Question End Here
# =============================================================================

def number_of_ways(n):
    stairs = [0 for x in range(n+1)]
    stairs[0] = 0
    stairs[1] = 1
    if n >= 2:
        stairs[2] = 2
    if n >= 3:
        stairs[3] = 4
    if(n > 3):
        for i in range(4, n+1):
            stairs[i] = stairs[i-1] + stairs[i-2] + stairs[i-3]
    return stairs[n]

# =============================================================================

def smallest_set_of_units(points):
    # TODO: Problem 4
    points.sort()
    end = points[0] + 1
    count = 1
    for i in range(len(points)):
        if(points[i] > end):
            end = points[i] + 1
            count += 1
    return count

# =============================================================================

def lcs(submission1, submission2):
    # TODO: Problem 5
    sub1 = len(submission1)
    sub2 = len(submission2)
    LCS = [[0] * (sub2 + 1) for i in range(sub1 + 1)]
    for i in range(1, sub1 + 1):
        for j in range(1, sub2 + 1):
            if submission1[i - 1] == submission2[j - 1]:
                LCS[i][j] = LCS[i - 1][j - 1] + 1
            else:
                LCS[i][j] = max(LCS[i - 1][j], LCS[i][j - 1])
    return LCS[sub1][sub2]

# =============================================================================

def test():
    # Thoroughly test your program and produce useful output.
    # Problem 1
    treeRoot = Tree(3)

    node9 = Tree(9)
    node20 = Tree(20)
    node15 = Tree(15)
    node7 = Tree(7)

    treeRoot.left = node9
    treeRoot.right = node20
    node20.left = node15
    node20.right = node7

    assert(treeRoot.level_order_traversal() == [[3], [9, 20], [15, 7]])

    # Problem 2
    graph = Graph(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                  [('q', 's', 1),
                   ('s', 'v', 1),
                   ('v', 'w', 1),
                   ('w', 's', 1),
                   ('q', 'w', 1),
                   ('q', 't', 1),
                   ('t', 'x', 1),
                   ('x', 'z', 1),
                   ('z', 'x', 1),
                   ('t', 'y', 1),
                   ('y', 'q', 1),
                   ('r', 'y', 1),
                   ('r', 'u', 1),
                   ('u', 'y', 1)])
    assert(graph.valid_path('q', 'z', 't') == True)

    # Problem 3
    assert(number_of_ways(3) == 4)

    # Problem 4
    assert(smallest_set_of_units([0.8, 4.3, 1.7, 5.4]) == 3)

    # Problem 5
    submission1 = [1, 2, 3, 4, 5]
    submission2 = [1, 3, 5]

    assert(lcs(submission1, submission2) == 3)

    print('All test cases passed !')


if __name__ == '__main__':
    test()
