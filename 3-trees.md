# Trees

Trees are very similar to linked lists in that they both have nodes, and that each node has pointers. What makes them different however, is that trees can connect to multiple different nodes, while linked lists cannot. To help visualize this, think of the structure of a linked list as a chain; each link in the chain can only connect to the link directly in front of it. This singular linkage gives a chain its linear structure, essentially making it one dimensional. 

With this still in mind, let's think of the structure of a tree as, well, a branch on a tree. A tree branch isn't limited to a linear structure like a chain is. Instead, a tree branch can break off into multiple branches, those branches breaking off into their own branches, and so on and so forth. What we have now, is a structure that's more complex both visually and functionally. 

In this lesson, we will be reviewing 3 different types of data structure trees:
- Binary Tree
- Binary Search Tree (BST)
- Balanced Binary Search Tree

## Binary Tree

A __binary tree__ is a tree in which each node can link to no more than two other nodes. The first node in the tree, or the node that is at the very top, is known as the __root__ node. On the other end, nodes that do not connect to any other nodes, and are at the very bottom of the tree, are known as the __leaf__ nodes. If a node is connected to other nodes below it, it is referred to as a __parent__ node, while nodes that are directly connected to, and are below, a parent node, are referred to as a __child__ node. Parent and child nodes are structured similarly to how a parent and child would be displayed in a family tree, with the children branching off from the parent. 

![Binary Tree Structure](timages/binary_tree.png)

There is one more term to define, and that is __subtree__. When looking at a family tree, you might see a parent displayed with 2 kids. At least one of those 2 kids might have their own kids displayed in the tree as well. In this situation, the child that has their own kids is a subtree. A __subtree__ is essentially a child node, that is a parent to other nodes. As you can see in the image above, the nodes within the red box make up a subtree. 

It is also important to note that nodes can link to other nodes, either before or after them, similar to a linked list. The red and black arrows in the image above represent this.

## Binary Search Tree

A __binary search tree__ (also known as a BST) is the same as a binary tree, except for the fact that there are rules to be followed when entering a new node. When entering a new node into a binary search tree (BST), the value of the node being entered is compared to the value of the root node (**if there isn't a root node, then the new node will become the root node*). If the value of the new node is __less__ than the root node, it goes into the __left__ subtree. If the new node is __greater__ than the root node, it will be placed into the __right__ subtree. Then, depending on whether the new node has been sent to the left or the right subtree, the new node is compared to the root of that subtree, and the process starts all over again until an empty spot can be found. 

Take the following tree for example: 

![Binary Search Tree](timages/bst.png)

Let's say that we wanted to insert the node with a value of 2 into the binary search tree. We would first have to compare 2 to the root node, which is 5. Is 2 greater than or less than 5? Since 2 is less than 5, we would start searching in the left subtree.

At this point, the process starts all over again, and we compare 2 to 3. Is 2 less than or greater than 3? Since it is less than, we would again look into the left subtree.

Now we will be comparing 2 to 1. Is 2 less than or greater than 1? Since 2 is greater than 1, it will be going into the right sub tree this time. And, since there isn't a node in 1's right pointer, we will insert 2 there.

![2 placed in bst](timages/bst_2_placement.png)

This is the process we have to go through every time we insert a node into a binary search tree. 

## Balanced Binary Search Tree

The tree in the example above is what's known as a __balanced binary search tree__. What this means is that the difference in height between the left subtree and the right subtree is less than 2. We can find the height of a tree by counting from the lowest leaf, back up to the root. In the example above, we calculate the height of the left subtree by starting at 2, the lowest leaf, and count up to the root node 5. 

![Finding the height of the left subtree](timages/left_subtree_height.png)

As you can see, we have counted 4 nodes, meaning that the height of the left subtree is 4.

To find the height of the right subtree, we do the same by starting at 9, the lowest leaf in that subtree, and count back up to the root node.

![Finding the height of the right subtree](timages/right_subtree_height.png)

We have counted 3 nodes, so the height of the right subtree is 3.

Now, we calculate the height of the entire tree by subtracting 3, the height of the right subtree, from 4, the height of the left subtree, getting 1 as a result. Since the difference in height between the two subtrees is less than 2, we can conclude that this tree is a balanced binary search tree. 

But what if the tree is unbalanced? If we're not careful, this could happen easily. Going back to our example, if we were to add a node of 1.5 to the left of node 2, the tree would become unbalanced, since the height of the left subtree is 2 nodes greater than the height of the right subtree. 

![Unbalanced bst](timages/unbalanced_bst.png)

This can be fixed using the AVL algorithm which switches up the numbers. 

I will explain and show how a bst can become unbalanced. 

I will briefly explain how AVL can balance a tree.

## How to create an empty BST in python

Similar to how I walked through the LinkedList class in the previous tutorial, I will walk through how to create an empty bst, and how to create a new node.

## Insert into a BST

I will then go over how to insert a node into a bst, based on its value.

## I will also go over how to print out the items in a bst

For my example problem, I will enter items from a sorted list, into a bst

For the practice problem, the student will have to create their own function that inserts items from a sorted list into a bst.