class Panel:
    def __init__(self, name, size, ll_volt=208, ln_volt=120, load_va=0):
        self.name = name
        self.size = size
        self.ll_volt = ll_volt
        self.ln_volt = ln_volt
        self.breakers = self.set_breakers(size)
        self.connections = []
        self.load_va = load_va

    def set_breakers(self, size):
        breakers = {}
        for i in range(1, size):
            breakers[str(i)] = 'space'
        return breakers

    def set_voltages(self, ll_volt, ln_volt):
        self.ll_volt = ll_volt
        self.ln_volt = ln_volt

    def print_panel(self):
        print('name: ' + self.name)
        print('line-line voltage: ' + str(self.ll_volt) + ' volts')
        print('line-neutral voltage: ' + str(self.ln_volt) + ' volts')
        print('connected load: ' + str(self.load_va) + ' watts')
        print('connections: ' + str(self.connections))

    def append_connection(self, con_name):
        self.connections.append(con_name)


class Transformer:
    def __init__(self, name, input_con, output_con, input_v, output_v, load_va):
        self.name = name
        self.input_con = input_con
        self.output_con = output_con
        self.input_v = input_v
        self.output_v = output_v
        self.load_va = load_va

    def print_info(self):
        print('name: ' + self.name)
        print('input: ' + self.input_con + ' output: ' + self.output_con)
        print('line_voltage: ' + str(self.input_v) + ' load_voltage: ' + str(self.output_v))
        print('demand load: ' + str(self.load_va) + ' watts')


class Network:
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        if node in self.nodes:
            print("panel already in network")
        else:
            self.nodes.append(node)

    def connect_nodes(self, parent, child):
        if parent in self.edges:
            self.edges[parent].append(child)
        else:
            self.edges[parent] = [child]

    def print_nodes(self):
        print(self.nodes)

    def print_connections(self):
        print(self.edges)
