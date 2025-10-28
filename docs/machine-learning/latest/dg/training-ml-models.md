We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Training ML Models

The process of training an ML model involves providing an ML
algorithm (that is, the _learning algorithm_)
with training data to learn from. The term _ML
model_ refers to the model artifact that is created by the
training process.

The training data must contain the correct answer, which is known as
a _target_ or _target
attribute_. The learning algorithm finds patterns in the
training data that map the input data attributes to the target (the
answer that you want to predict), and it outputs an ML model that
captures these patterns.

You can use the ML model to get predictions on new data for which you do not know the
target. For example, let's say that you want to train an ML model to predict if an email is spam
or not spam. You would provide Amazon ML with training data that contains emails for which you know
the target (that is, a label that tells whether an email is spam or not spam). Amazon ML would train
an ML model by using this data, resulting in a model that attempts to predict whether new email
will be spam or not spam.

For general information about ML models and ML algorithms, see [Machine Learning Concepts](machine-learning-concepts.md "machine-learning-concepts.md").

###### Topics

- [Types of ML Models](types-of-ml-models.md "types-of-ml-models.md")
- [Training Process](training-process.md "training-process.md")
- [Training Parameters](training-parameters.md "training-parameters.md")
- [Creating an ML Model](creating-ml-model-on-the-amazon-ml-console.md "creating-ml-model-on-the-amazon-ml-console.md")
