# Queues

Waiting in lines is apart of daily living. Whether it's lining up to go to recess, waiting in the checkout line at the grocery store, or waiting for your order number to be called at a restaurant, we have all had practice waiting for our turn behind other people. Lines have what's known as a First-In-First-Out (FIFO) structure, which means that the first person who enters the line is the first person to leave the line. 

This is almost exactly how a queue works in programming. Using the queue data structure, an object gets added to the end of the list, also known as the back. This process of entering the back of the list is known as an enqueue operation (To help remember this, enter and enqueue have the same prefix of "en"). The object leaves the queue when it reaches the front, or is the first item in the list. This process of leaving the front of the line is called a dequeue operation. It is important to note that no object can cut in line; all objects must enqueue at the back. 

[Image_of_Queue_Structure](queue_image.png)

## Real World Uses

One thing that the queue data structure is used for are web server requests. Let's say that multiple people click on the link to a YouTube video at the same time. These clicks are what are called requests. Each person's request gets put in to a queue, and is in there until the web server can "help the next customer" so to speak, or in our case, process the request and return the YouTube video to the user.

Online shopping is another great example of when queues are used. When a popular new clothing item is released online to the public, many people will want to buy it, so much so that it could be sold out within minutes. To help manage the number of people visiting the website, visitors are placed in a virtual waiting room until there is enough space to let them in. This is a more visual example of how queues are used in software. It's a first-come-first-serve situation, and the people at the front of the queue are more likely to purchase the item than the people who joined later, at the back. 

## Queues in Python

In python, we use a list to create a queue. The process of creating an empty queue is the same as creating an empty list:

```python
#define an empty queue
my_queue = []

```

To add an item to the queue, we use the .append() function:

```python
#append objects to the list
my_queue.append("Mary")
my_queue.append("Ted")
my_queue.append("Roger")

print(my_queue)
```

If you run the code above, it should return:

```python
['Mary', 'Ted', 'Roger']
```

As you see, each new name is enqueued to the back of the queue in the order they were added. The process of enqueueing items to the back of the queue is O(1) performance, since the .append() function doesn't require a lot of memory.  

Dequeueing an item is a little more complex. Due to the rules of the queueing structure, you can only remove items at the front of the queue. The .pop() method alone would not be helpful in this case, since it removes the last item in the queue. To make the .pop() method work, we need to specify the index of the item we would like to remove, which in our case, would be 0.

```python
my_queue.pop(0)
```
This can also be written using the delete function:

```python
del my_queue[0]
```
Whichever way you write it is up to you, but they both do the same thing. If you were to run either of these lines of code, it would return:

```python
['Ted', 'Roger']
```

The process of dequeueing an item has a performance of O(n). This is because you need to first isolate the item you'd like to remove (O(1)), and then delete it (O(1)). Since both of these processes are O(1) performance, putting them together would make 2(O(n)), which translates to O(n).