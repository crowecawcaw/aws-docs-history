We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Building a Machine Learning Application

Building ML applications is an iterative process that involves a sequence of steps. To build an ML
application, follow these general steps:

1. Frame the core ML problem(s) in terms of what is observed and what answer you want the model to
   predict.
2. Collect, clean, and prepare data to make it suitable for consumption by ML model training
   algorithms. Visualize and analyze the data to run sanity checks to validate the quality of the data and
   to understand the data.
3. Often, the raw data (input variables) and answer (target) are not represented in a way that can be
   used to train a highly predictive model. Therefore, you typically should attempt to construct more
   predictive input representations or features from the raw variables.
4. Feed the resulting features to the learning algorithm to build models and evaluate the quality of the
   models on data that was held out from model building.
5. Use the model to generate predictions of the target answer for new data instances.
