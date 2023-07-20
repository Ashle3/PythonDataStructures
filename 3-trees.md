# Trees

Trees are very similar to linked lists in that they both have nodes, and that each node has pointers. What makes them different however, is that trees can connect to multiple different nodes, while linked lists cannot. To help visualize this, think of the structure of a linked list as a chain; each link in the chain can only connect to the link directly in front of it. This singular linkage gives a chain its linear structure, essentially making it one dimensional. With this still in mind, let's think of the structure of a tree as, well, a branch on a tree. A tree branch isn't limited to a linear structure like a chain is. Instead, a tree branch can break off into multiple branches, those branches breaking off into their own branches, and so on and so forth. What we have now, is a structure that's more complex both visually and functionally. 

In this lesson, we will be reviewing 3 different types of trees:
- Binary Tree
- Binary Search Tree (BST)
- Balanced Binary Search Tree

## Binary Tree

A __binary tree__ is a tree in which each node can link to no more than two other nodes. The first node in the tree, or the node that is at the very top, is known as the __root__ node. On the other end, nodes that do not connect to any other nodes, and are at the very bottom of the tree, are known as the __leaf__ nodes. If a node is connected to other nodes below it, it is referred to as a __parent__ node, while nodes that are directly connected to, and are below, a parent node, are referred to as a __child__ node. Parent and child nodes are structured similarly to how a parent and child would be displayed in a family tree, with the children branching off from the parent. 

![Binary Tree Structure](timages/binary_tree.png)

There is one more term to define, and that is __subtree__. When looking at a family tree, you might see a parent displayed with 2 kids. At least one of those 2 kids might have their own kids displayed in the tree as well. In this situation, the child that has their own kids is a subtree. A __subtree__ is essentially a child node, that is a parent to other nodes. As you can see in the image above, the nodes within the red box make up a subtree. 

It is also important to note that nodes can link to other nodes, either before or after them, similar to a linked list. 

## Binary Search Tree

Define what a Binary Search Tree is (state how there are rules to inserting into a binary search tree; lower goes on the left, higher goes on the right).

Will also have a diagram displaying this.

## Balanced vs Unbalanced Binary Search Tree

I will explain and show how a bst can become unbalanced. 

I will briefly explain how AVL can balance a tree.

## How to create an empty BST in python

Similar to how I walked through the LinkedList class in the previous tutorial, I will walk through how to create an empty bst, and how to create a new node.

## Insert into a BST

I will then go over how to insert a node into a bst, based on its value.

## I will also go over how to print out the items in a bst

For my example problem, I will enter items from a sorted list, into a bst

For the practice problem, the student will have to create their own function that inserts items from a sorted list into a bst.