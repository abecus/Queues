pyqueues
=================================

A library for Priority-Queues containing Indexed-Priority-Queue and Simple Priority-Queue.

--Installation:

clone the this reporitory using,
`https://github.com/abecus/Queue.git`

or, install using pip,
`pip install pyqueues`

Works with Python 3.x and PyPy.

## Overview
Both, the Indexed priority queue and the queue has been implemented as a min binary heap to use it as a max heap or to uea it with custome key pass the values as a tuple in the heaps eg. (key, value). The time complexities are,

- peek highest priority element: O(1) 

- pop highest priority element: O(log n) 

- push new element: O(log n) 

additionally for Indexed Priority Queue,

- lookup of any item by key: O(1)

- remove element by key: O(log n) 

- update element by key: O(log n) 

## Usage

	from pyqueues.indexedPriorityQueue import IndexedPriorityQueue
	from pyqueues.heap import heapify, heapPop, heapPush

- to heapify a list (does not changes the original list, but heapifies internally),

	arr = [10, 20, 15, 12, 40, 25, 18, 40]
	pq = IndexedPriorityQueue(arr)
	pq.heapify()
    
- to push items into the priority queue,	

    	pq.push(2)
    	pq.push(-1)
    	
- to update a item using key (we an saperatly keep track of the key of the values using a dict by mapping values to the arrSize arrtibute of the priority queue)
    	
    	pq.update(pq.arrSize-1, 100)    # updates -1 to 100
    	pq.update(pq.arrSize-2, -1)     # updates 2 to -1

"similarly use pq.decreaseKey() and pq.increaseKey() methods (works in half of, the time required for update method), when we know that we are increseing or decresing the values while updating."

- to remove a values from priority queue,

	pq.remove(pq.arrSize-1)    # removes 100

- to pop highest priority element,

	pq.pop()        # pops -1

License 
-------
MIT License

Copyright (c) 2020 abecus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
