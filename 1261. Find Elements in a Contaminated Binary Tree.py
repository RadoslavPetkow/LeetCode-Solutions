class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements(object):

    def __init__(self, root):
        """
        :type root: Optional[TreeNode]
        """
        self.recovered_values = set()  
        self.recover_tree(root, 0) 

    def recover_tree(self, node, val):
        """ Recovers the tree using DFS """
        if not node:
            return
        
        node.val = val 
        self.recovered_values.add(val)  

        self.recover_tree(node.left, 2 * val + 1)
        self.recover_tree(node.right, 2 * val + 2)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.recovered_values  
