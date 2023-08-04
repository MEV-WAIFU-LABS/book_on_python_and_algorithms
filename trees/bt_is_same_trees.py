#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: bt3gl

def is_same_trees(p, q):

        if not p and not q:
            return True
        
        if (not p and q) or (not q and p):
            return False
        
        if p.val != q.val:
            return False
        
        return self.is_same_trees(p.right, q.right) and self.is_same_trees(p.left, q.left)