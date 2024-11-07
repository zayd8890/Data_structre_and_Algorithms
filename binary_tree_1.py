from typing import Any


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    def calculate_sum(self):
        if type(self.data) is int: 
            elements = 0
            if self.left:
                elements += self.left.calculate_sum()

            elements= self.data

            if self.right:
                elements += self.right.calculate_sum()

            return elements
        else:
            raise TypeError("data type must be int")
        

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        if self.right:
            elements += self.right.in_order_traversal()
        elements.append(self.data)

        return elements
    
    def pre_order_traversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements
        

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("------------------------------------------------------------------------------------------------")
    print("pre_order traversal gives this sorted list:",numbers_tree.pre_order_traversal())    
    print("------------------------------------------------------------------------------------------------")
    print("post_order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("------------------------------------------------------------------------------------------------")
    print("mininum:",numbers_tree.find_min())
    print("------------------------------------------------------------------------------------------------")
    print("maximum:",numbers_tree.find_max())
    print("------------------------------------------------------------------------------------------------")
    print("the sum of all the numbers are:",numbers_tree.calculate_sum())
    print("------------------------------------------------------------------------------------------------")
    '''1. find_min(): finds minimum element in entire binary tree
2. find_max(): finds maximum element in entire binary tree
3. calculate_sum(): calcualtes sum of all elements
4. post_order_traversal(): performs post order traversal of a binary tree
5. pre_order_traversal(): perofrms pre order traversal of a binary tree
'''