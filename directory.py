class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.parent = parent

    def add_child(self, child):
        self.children[child.name] = child
