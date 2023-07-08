# Linked Lists

Most data structures in python are stored, using what's known as contiguous memory. That means that items in the data structure are stored right next to each other in memory. This makes finding the next item in the data structure is easy, since the next item is guaranteed to be in the memory slot right next to the item you are currently on.

![Regular List Example](regular_list.png)


Linked lists are not structured this way. Items in the list might be stored at different parts of the memory, and are thus, more difficult to find. This is where the 'links' in linked lists come into play. At the end of each item in a linked list, also known as a node, there is a link, or a pointer, giving directions to where the next node is in the memory. 

![Linked List Example](linked_list.png)

## Real World Application

Let's use a real world example to better understand linked lists. We can compare data structures with contiguous memory, (arrays, maps, lists), to a mailman delivering mail to houses on a street. It is easy for the mailman to find the next house because it is right next door to the house they just delivered mail to. 

![Mailman Example](mailman_example.png)

The structure of a linked list is similar to how a pizza delivery driver would deliver pizzas. When delivering pizzas, it is very unlikely that everyone on the same street ordered a pizza. In most cases, pizza delivery drivers have to drive across town to deliver their next pizza. In this example, the node, or the current item in the linked list, is represented by the houses that receive pizza from the delivery driver. The pointer, or the link to the next node in the list, is represented by the directions to the next house on the delivery route; the directions tell the driver exactly where the next house is in the city. 

![Pizza Delivery Example](pizza_example.png)

