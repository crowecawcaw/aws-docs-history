We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Learning Algorithm

The learning algorithm’s task is to learn the weights for the model. The weights describe the likelihood that the patterns that the model
is learning reflect actual relationships in the data. A learning algorithm consists of a loss
function and an optimization technique. The loss is the penalty that is incurred when the estimate of the
target provided by the ML model does not equal the target exactly. A loss function
quantifies this penalty as a single value. An optimization technique seeks to minimize the loss. In Amazon
Machine Learning, we use three loss functions, one for each of the three types of prediction problems.
The optimization technique used in Amazon ML is online Stochastic Gradient Descent
(SGD). SGD makes sequential passes over the training data, and during each pass, updates feature weights
one example at a time with the aim of approaching the optimal weights that minimize the loss.

Amazon ML uses the following learning algorithms:

- For binary classification, Amazon ML uses logistic regression (logistic loss function +
  SGD).
- For multiclass classification, Amazon ML uses multinomial logistic regression
  (multinomial logistic loss + SGD).
- For regression, Amazon ML uses linear regression (squared loss function + SGD).
