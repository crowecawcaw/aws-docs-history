We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Evaluating Model Accuracy

The goal of the ML model is to learn patterns that generalize well for unseen data instead of just
memorizing the data that it was shown during training. Once you have a model, it is important to check if
your model is performing well on unseen examples that you have not used for training the model. To do
this, you use the model to predict the answer on the evaluation dataset (held out data) and then compare the
predicted target to the actual answer (ground truth).

A number of metrics are used in ML to measure the predictive accuracy of a model. The choice of accuracy
metric depends on the ML task. It is important to review these metrics to decide if your model is
performing well.
