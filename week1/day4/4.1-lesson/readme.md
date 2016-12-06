# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Math Primer 2
Week 1 | Lesson 4.1

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe a matrix and an array
- Explain how to add and subtract arrays
- Explain the dot product


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- [intro to arrays] (https://www.khanacademy.org/computing/computer-programming/programming/arrays/p/intro-to-arrays#)


### LESSON GUIDE
| TIMING  | TYPE  | TOPIC  |
|:-:|---|---|
| 5 min  | [Introduction](#introduction)   | Matrices, arrays, the dot product  |
| 20 min  | [Demo / Guided Practice](#demo)  | Matrices and arrays  |
| 20 min  | [Demo / Guided Practice](#demo)  | Adding and subtracting arrays  |
| 20 min  | [Demo / Guided Practice](#demo)  | The dot product  |
| 20 min  | [Independent Practice](#ind-practice)  |  |
| 5 min  | [Conclusion](#conclusion)  |  |

---

<a name="Why use arrays?"></a>
## Introduction: Why Use arrays? (5 mins)

An array is a collection of related data items, called elements, associated
with a single variable name. Arrays can ease programming and offer improved performance.
When writing an application, you are usually faced with the problem of storing and
manipulating large collections of data. Arrays simplify the task of naming and
referencing the individual items in each collection.  Using arrays can boost the
performance of your application . Arrays let you manipulate an entire collection of data
items with a single statement.

- [arrays](https://docs.oracle.com/cd/A57673_01/DOC/api/doc/PC_22/ch10.htm)


<a name="Matrices and arrays"></a>
## Demo / Guided Practice / Demo: Matrices and arrays (20 mins)

An array is a data structure that allows you to group several numeric or string
variables under a single name. A vector is a one-dimensional array, a
table or a matrix is two-dimensional array, or an array may have several dimensions. An array may
contain either string or numeric values, but a given array may not contain both
types of values.

As mentioned above, a matrix is a specific type of array, that is 2D.

- [arrays and matrices](http://www.truebasic.com/node/1038)

Here's a great picture showing the difference between vectors, matrices, and arrays.

![vectors, matrices, arrays](./assets/images/vectorArrayMatrix.jpg)

Here is some information on [vectors, matrices, arrays](http://www.slideshare.net/mikeranderson/2013-1114-enter-thematrix).

Let's use the following [demo code](./code/w1-4.1-demo.ipynb) to get started.


First, use numpy to create an array.

in Jupyter notebook type:

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
```

You've just created your first two arrays! Since we know that matrices are simply
a 2D array, we'll just keep keep our focus on arrays for the moment. Since there may be some
confusion using matrices and arrays, some Python users find it easier just to stick with arrays.

You can read more about the confusion between the two and some problems that arise
[here](http://stackoverflow.com/questions/12024820/danger-of-mixing-numpy-matrix-and-array)

**Check** What is the difference between a vector, a matrix, and an array? Is a vector an array?
Is an array a vector? Is a matrix an array? Is an array a matrix? Can arrays have both numeric and string values?


<a name=" Adding and subtracting two arrays"></a>
## Demo / Guided Practice / Demo:  Adding and subtracting two arrays (20 mins)

Let's take a look at the two arrays we just created above.

```python
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
```

Let's add them together.
[6, 6, 6, 6, 6]


Now, let's let numpy do the work.
in Jupyter notebook type:

```python
np.add(a, b)
```
Thanks numpy, that was easy!


Let's try subtraction.
[-4, -2, 0, 2, 4]


Now, let's let numpy do the work.
in iPython notebook type:

```bash
np.subtract(a, b)
```
Thanks numpy, that was easy!


<a name=" The dot product"></a>
## Demo / Guided Practice / Demo:  The dot product (20 mins)

The dot product is one way to multiply arrays. The dot product is represented like [this]:

![](./assets/images/dot-product.png)

Let's take a look again at the two arrays we just created above:

```python
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
```

Using the formula for the dot product that we just learned, let's find the dot product for our
two arrays.

1 * 5 = 5
2 * 4 = 8
3 * 3 = 9
4 * 2 = 8
5 * 1 = 5
       --
       35

Now, let's let numpy do the work.
in iPython notebook type:

```python
np.dot(a, b)
```
Thanks numpy, that was easy!

[dot product](http://www.maplesoft.com/support/help/maple/view.aspx?path=SignalProcessing%2FDotProduct)
[dot product](http://tutorial.math.lamar.edu/Classes/CalcII/DotProduct.aspx)

<a name="ind-practice"></a>
## Independent Practice: Topic (20 minutes)
- Create 2 arrays. Add them together, subtract them, and find their dot product.
- Multiply each element in an array by a constant. Can you see if this is faster than using a loop? Do you have any ideas why?

## Reshaping and transposing
In linear algebra, the transpose of a matrix A is another matrix AT (also written A′, Atr, tA or At) created by any one of the following equivalent actions:

- reflect A over its main diagonal (which runs from top-left to bottom-right) to obtain AT
- write the rows of A as the columns of AT
- write the columns of A as the rows of AT

Reshaping is about retaining the same data, but altering the shape of the array in which each value is held. The best way to see this is to play around with it and see what outputs you get and there is a lab to do that. So that uses np.reshape Additionally you might want to play with the np.ravel, which returns a 1-d array for whatever array you input.


<a name="conclusion"></a>
## Conclusion (5 mins)
- What's the difference between a matrix and an array?
- Explain how to add to arrays together, subtract them, get the dot product to a partner.
