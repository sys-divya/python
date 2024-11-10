import heapq

class Node:
    def __init__(self, state, parent=None, action=None, g_cost=0, h_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_cost = g_cost
        self.h_cost = h_cost

    def __lt__(self, other):
        return (self.gc + self.hc) < (other.gc + other.hc)  # Compare nodes based on f = g + h

class hu:
    @staticmethod
    def m_d(st, gs):
        return abs(st[0] - gs[0]) + abs(st[1] - gs[1])

class succ:
    @staticmethod
    def get_action(st):
        x, y = st
        return [("go right", (x+1, y), 1), ("go down", (x, y+1), 1)]

    @staticmethod
    def get_result(st, at):
        return at[1]

    @staticmethod
    def get_step_count(st, at):
        return at[2]

def get_solution(node):
    p = []
    while node:
        p.append((node.at, node.st))
        node = node.pn
    return list(reversed(p))

def a_star(i_n, gs, heu, su):
    s = node(i_n, None, None, 0, heu(i_n, gs))
    o_l = [s]
    c_s = set()
    while o_l:
        c_n = heapq.heappop(o_l)
        if c_n.st == gs:
            return get_solution(c_n)
        c_s.add(c_n.st)
        for at in su.get_action(c_n.st):
            ss = su.get_result(c_n.st, at)
            sc = su.get_step_count(c_n.st, at)
            if ss in c_s:
                continue
            s_gc = c_n.gc + sc
            s_n = None
            for n in o_l:
                if n.st == ss:
                    s_n = n
                    break
            if not s_n or s_gc < s_n.gc:
                s_n = node(ss, c_n, at[0], s_gc, hu.m_d(ss, gs))
                heapq.heappush(o_l, s_n)
    return None

i = (0, 0)
v = (4, 4)
s = a_star(i, v, hu.m_d, succ)
