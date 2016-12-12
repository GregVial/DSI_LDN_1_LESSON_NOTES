---
title: MRJob lab
type: lab
duration: "1:25"
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) MRJob Lab

### Virtual Machine Required
Note: This lab requiress additional prep in order to run successfully:

1. [Download and install Virtual Machine](../VM-installation.md).
    - Note: This is a big file. Please reserve time to download and troubleshoot installation.

## Introduction
In the past lab we've used a Virtual Machine to run Map Reduce jobs on native hadoop. As you may have understood, it's quite cumbersome and complicated.

Luckily we don't have to do that, because our friends at Yelp developed a great open source python library that wraps around hadoop streaming called [MRJob](https://github.com/Yelp/mrjob).

This is already installed in your VM, but you can also install it locally if you prefer, using:

`pip install mrjob`.

## Exercise

This lab will teach you to use [MRJob](https://github.com/Yelp/mrjob), a very powerful python library for map reduce.

> Except for Exercise 1, all the other exercises can also be run on the laptop in local mode, if some of them have trouble connecting or using the VM. All they need is `pip install mrjob`.

#### Requirements
- Exercise 1: running map reduce locally and on hadoop cluster
- Exercise 2: add a combiner
- Exercise 3: multi step jobs
- Exercise 4: Setup and teardown of tasks
- Exercise 5: Counters

**Bonus:**

- Putting it all together: find top 15 most frequent words for all books
- Use NLTK to recognize a book from the most frequent words


#### Starter code

[Starter Code](./assets/code/starter-code/starter-code.ipynb)

> [Solution Code](./assets/code/solution-code/solution-code.ipynb)


Additional Resources

- [MRJob Documentation](https://pythonhosted.org/mrjob/)
- [MRJob Examples](https://github.com/Yelp/mrjob/tree/master/mrjob/examples)
