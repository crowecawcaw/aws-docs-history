We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Retraining Models on New Data

For a model to predict accurately, the data that it is making predictions on must have a similar distribution
as the data on which the model was trained. Because data distributions can be expected to drift over time,
deploying a model is not a one-time exercise but rather a continuous process. It is a good practice to
continuously monitor the incoming data and retrain your model on newer data if you find that the data
distribution has deviated significantly from the original training data distribution. If monitoring data to
detect a change in the data distribution has a high overhead, then a simpler strategy is to train the model
periodically, for example, daily, weekly, or monthly. In order to retrain models in Amazon ML, you would need
to create a new model based on your new training data.
