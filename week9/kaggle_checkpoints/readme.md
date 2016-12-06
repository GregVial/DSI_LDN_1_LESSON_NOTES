---
title: Kaggle Checkpoints
type: evaluation guideline
duration: N/A
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Kaggle Checkpoints


Use this guide to determine the milestones you should be hitting with your group. This will ensure that you do not fall behind, and are prepared for presentations at the end of the week.

### Day 2

At this point, your group should have the following:

1. Starter code to load your data into a Pandas DataFrame. This code should be submitted to the Kaggle Leaderboard as practice.
1. First attempts at using piplines to organize and clean the data.
1. In your own words, a problem statement which you will be modeling against. This can be similar to the project description on Kaggle. Be sure to discuss this with your instructor to make sure you are on the right path.
> Instructor's Note: The problem statement is just to ensure that the students understand the project, data, and goals.

### Day 3

At this point, your group should have the following:

1. Cleaned data, and code submitted on the Kaggle Leaderboard.
1. A clearly articulated decision on the first models you will be auditioning. **NOTE**: It is best to stick with models that have been covered in class so far. If you decide to use a more advanced model, please discuss with your instructor, though it is not advised to go this route.
1. Code that auditions, evaluates, and begins to tune your models. **HINT**: Always define a metric for evaluation before auditioning a model. This will help with tuning.
1. A clear log of your observations, decisions, and visualizations. This should be updated over the next few days to help tell the story behind the project lifecycle. This can be in the form of a text file, markdown file, or ipynb notebook.

### Day 4 (early)

At this point, your group should have the following:

1. First completed models fully evaluated. At this point you should have your first results from the Kaggle Leaderboard.
1. Code that runs transformations on your data, along with visualizations of the results. **HINT**: What technique have we covered that will allow us to emphasize variation and display strong patterns in our data?
1. Models built on top of the transformed data, along with observations regarding any improvements
1. Clearly documented log of observations and results up to this point.

> Instructor's Note: The students should be using PCA to transform their data. If anyone has not arrived at this observation, this would be your chance to nudge them along.

### Day 4 (late)

At this point, your group should have the following:

1. Use of clustering algorithms to classify the data. When deciding on a clustering algorithm, consider the features and how they will be used. Document your decisions.
1. Models fit using the cluster labels as features.
1. Visualizations that clearly display the results of clustering and the subsequent modeling done on the clustered labels.
1. Clearly documented log of observations and results up to this point.

> Instructor's Note: The students will likely want to use K-Means clustering, or hierarchical clustering at this point. DBSCAN is another option to fit this data.


### Day 5

At this point, your group should have the following:

1. Updates to all previous code and models, including updated pipelines to fit your approach. Remember, clean code is an absolute must have!
1. Visualizations of all results in Tableau, Matplotlib, or Seaborn.
1. Clearly documented observations of all approaches and results.
1. A client facing presentation ready to be presented to the class. This should include explanations of how you've optimized your models, a suggested plan of action for the CDC, and an analysis of the costs of that plan.

---

## Evaluation Metrics

The Kaggle competition will be evaluated on the following points:

1. **AUC Scoring**: A clear winning group will be determined based on the AUC Scoring performed by the Kaggle Leaderboard. This is not to say that the winning group's work was the best submission. Remember, just hitting a benchmark is not enough to determind success, the following points are just as important.

2. **Clearly documented observations**: Students should have some log, whether it is a markdown file, text file, or ipynb notebook, describing the observations and decisions they made along the way. This should be submitted to your instructor prior to your final presentation.

3. **Code**: All of your models, pipelines, cleaning techniques, and transformations should be properly coded and documented. Syntax is important, as Data Scientists are often tasked with building products that will be collaborated upon or maintained by other engineers. It is also important that no mistakes were made while pipelining data. If any data points were corrupted, the results are useless.

4. **Presentation**: Your presentation is expected to be client facing. Describe your data and approach as if your client is in front of you. This includes explaining the decisions made, the means by which you evaluated your decisions, and visualizations to support the story you are telling. This is a storytelling exercise, so be sure to set up, explain, and summarize the project lifecycle clearly. 
