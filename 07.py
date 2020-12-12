import re
from pathlib import Path
from typing import Dict, List, Set

import runner

pattern = re.compile(r'^(?P<color>[\w\s]+) bags contain ((?P<children>((\d+) ([\w\s]+)+ bag(s?)(, )?)+)|(?P<nothing>no other bags))\.$')
child_pattern = re.compile(r'(\d+) ([\w\s]+)+ bags?(?:, )?')

def parse_spec(spec: str) -> dict:
    m = pattern.match(spec)
    if m:
        data = m.groupdict()
        children = []
        if data['children']:
            m_children = child_pattern.findall(data['children'])
            for child in m_children:
                children.extend(int(child[0])*[child[1]])
        elif not data['nothing']:
            raise ValueError('If there are no children it should say: "... contain no other bags".')
        return data['color'], children
    else:
        raise ValueError(f'Failed to parse: {spec}')
    
    
class Node:
    def __init__(self, color: str):
        """
        new node
        """
        self.color: str = color
        self.children: List[Node] = []
        self.parents: Set[Node] = set()
        
    def add_child(self, child: 'Node'):
        self.children.append(child)
        
    def add_parent(self, parent: 'Node'):
        self.parents.add(parent)
        
    def __repr__(self):
        return f'{self.color}, children={len(self.children)}, parents={len(self.parents)}'


def add_node(graph: Dict[str, Node], color: str, specs: Dict[str, Set[str]]) -> Node:
    if color not in graph:
        node = Node(color)
        graph[color] = node
        for child in specs.get(color, {}):
            child_node = graph.get(child, add_node(graph, child, specs))
            node.add_child(child_node)
            child_node.add_parent(node)
    return graph[color]

    
def build_graph(specs: Dict[str, Set[str]]) -> Dict[str, Node]:
    graph: Dict[str, Node] = {}
    
    for color in specs.keys():
        add_node(graph, color, specs)
        
    return graph
        
            
def get_parents(node: Node):
    parents = [parent.color for parent in node.parents]
    for parent in node.parents:
        parent_list = get_parents(parent)
        parents.extend(parent_list)
    return parents


def get_children(node: Node):
    children = [child.color for child in node.children]
    for child in node.children:
        child_list = get_children(child)
        children.extend(child_list)
    return children


def part1(data):
    specs = dict(map(parse_spec, data.splitlines()))
    # {a: {b, c}, b: {d}, ...}
    graph = build_graph(specs)
    
    parents = get_parents(graph['shiny gold'])
    print(len(parents))
    return len(set(parents))


def part2(data):
    specs = dict(map(parse_spec, data.splitlines()))
    # {a: {b, c}, b: {d}, ...}
    graph = build_graph(specs)
    
    children = get_children(graph['shiny gold'])
    print(len(children))
    return len(children)


runner.run(day=int(Path(__file__).stem))
