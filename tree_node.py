class TreeNode:
    def __init__(self, data, designation=0):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self ,tree_level =-1, print_type = "both"): 
        '''
        **args:** print_type = [ "both" , "name" , "designation"]
        
        '''
        if tree_level <-1 :
            raise ValueError("'tree_level' must be positive or equal to -1 to print the whole tree")
        level = self.get_level()
        if level == tree_level: 
            return ""
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix , end="")
        if print_type == "designation":
            print(self.data[1])
        elif print_type == "name":
            print(self.data[0])
        elif print_type == "both":
            print(self.data[0] + self.data[1])
        if self.children:
            for child in self.children:
                child.print_tree(tree_level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def build_product_tree():
        root = TreeNode("Electronics")

        laptop = TreeNode("Laptop")
        laptop.add_child(TreeNode("Mac"))
        laptop.add_child(TreeNode("Surface"))
        laptop.add_child(TreeNode("Thinkpad"))

        cellphone = TreeNode("Cell Phone")
        cellphone.add_child(TreeNode("iPhone"))
        cellphone.add_child(TreeNode("Google Pixel"))
        cellphone.add_child(TreeNode("Vivo"))

        tv = TreeNode("TV")
        tv.add_child(TreeNode("Samsung"))
        tv.add_child(TreeNode("LG"))

        root.add_child(laptop)
        root.add_child(cellphone)
        root.add_child(tv)

        root.print_tree()
        
def build_management_tree():
    
    level_0 = TreeNode(("Nilupul","(CEO)"))
    
    level_1_0 = TreeNode(("Chinmay","(CTO)"))
    
    level_2_0 = TreeNode(("Vishwa", "(Infrastructure Head)"))
    level_2_0.add_child(TreeNode(("Dhaval","(Cloud Manager)")))
    level_2_0.add_child(TreeNode(("Abhijit","(App Manager)")))
    
    level_2_1 = TreeNode(("Aamir","(Application Head)"))
    
    level_1_0.add_child(level_2_0)
    level_1_0.add_child(level_2_1)
    
    
    level_1_1 = TreeNode(("Gels","(HR Head)"))
    level_1_1.add_child(TreeNode(("Peter","(Recruitment Manager)")))
    level_1_1.add_child(TreeNode(("Waqas","(Policy Manager)")))
    
    level_0.add_child(level_1_0)
    level_0.add_child(level_1_1)
    
    return level_0
    
        
if __name__ == "__main__":
# Test the function
    root_node = build_management_tree()
    root_node.print_tree(1) # prints only name hierarchy
    print("--------------------------------")
    root_node.print_tree(2) # prints only designation hierarchy
    print("--------------------------------")
    root_node.print_tree(-1) # prints both (name and designation) hierarchy