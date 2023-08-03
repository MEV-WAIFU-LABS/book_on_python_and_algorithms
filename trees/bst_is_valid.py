#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl


def is_valid_bst_recursive(root):
  
          def is_valid(root, min_val=float(-inf), max_val=float(inf)):
            if root is None:
                return True
        
            return (min_val < root.val < max_val) and \
                        is_valid(root.left, min_val, root.val) and \
                        is_valid(root.right, root.val, max_val)
        
      return is_valid(root)


def is_valid_bst_iterative(root):
        
        queue = deque()
        queue.append((root, float(-inf), float(inf)))
        
        while queue:
            node, min_val, max_val = queue.popleft()
            if node:
                if min_val >= node.val or node.val >= max_val:
                    return False
                if node.left:
                    queue.append((node.left, min_val, node.val))
                if node.right:
                    queue.append((node.right, node.val, max_val))
        
        return True
    
    
def is_valid_bst_inorder(root):
        
        def inorder(node):
            if node is None:
                return True
            
            inorder(node.left)
            queue.append(node.val)
            inorder(node.right)
            
        queue = []
        inorder(root)
        for i in range(1, len(queue)):
            if queue[i] <= queue[i-1]:
                return False
            
        return True
  