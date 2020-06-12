class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            #Try to put it on the left
            if self.left == None:
                self.left = BSTNode(value)
            else:
            #If there's already a node there, start over evaluating that node
                self.left.insert(value)
        else:
            #Try to put it on the right
            if self.right == None:
                self.right = BSTNode(value)
            else:
            #If there's already a node there, start over evaluating that node
                self.right.insert(value)

      
        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else: 
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
            
        
