# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Panel:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.breakers = self.set_breakers(size)

    def set_breakers(self, size):
        breakers = {}
        for i in range(1, size):
            breakers[str(i)] = 'space'
        return breakers


class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = {}

    def add_panel(self, panel):
        if panel in self.nodes:
            print("panel already in network")
        else:
            self.nodes.append(panel)

    def connect_panel(self, parent, child):
        if parent in self.edges:
            self.edges[parent].append(child)
        else:
            self.edges[parent] = [child]

    def print_nodes(self):
        print(self.nodes)

    def print_connections(self):
        print(self.edges)


if __name__ == '__main__':
    dist = Network('1')
    dist2 = Network('2')
    dist.add_panel('a')
    dist.add_panel('b')
    dist.add_panel('c')
    dist.connect_panel('a', 'b')
    dist.connect_panel('a', 'c')
    dist.connect_panel('b', 'c')
    dist.print_nodes()
    dist.print_connections()
    dist2.print_connections()
    dist2.print_nodes()

    panel = Panel('panel_a', 42)
