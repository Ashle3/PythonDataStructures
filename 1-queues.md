# Queues

Waiting in lines is apart of daily living. Whether it's lining up to go to recess, waiting in the checkout line at the grocery store, or waiting for your order number to be called at a restaurant, we have all had practice waiting for our turn behind other people. Lines have what's known as a First-In-First-Out (FIFO) structure, which means that the first person who enters the line is the first person to leave the line. 

This is almost exactly how a queue works in programming. Using the queue data structure, an object gets added to the end of the list, also known as the back. This process of entering the back of the list is known as an enqueue operation (To help remember this, enter and enqueue have the same prefix of "en"). The object leaves the queue when it reaches the front, or is the first item in the list. This process of leaving the front of the line is called a dequeue operation. It is important to note that no object can cut in line; all objects must enqueue at the back. 

[Image_of_Queue_Structure](queue_image.png)