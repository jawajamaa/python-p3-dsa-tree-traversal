class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = list()
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      if node["id"] == id:
        return node
      else:
        result.append(node["id"])
      nodes_to_visit = nodes_to_visit + node["children"]

  # def get_element_by_id(self, id, node):
  #   result = list()
  #   nodes_to_visit = [node]

  #   while len(nodes_to_visit) > 0:
  #     node = nodes_to_visit.pop[0]
  #     if node["id"] == id:
  #       return node
  #     else:
  #       result.append(node["text_content"])
  #     nodes_to_visit = nodes_to_visit + node["children"]
