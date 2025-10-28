We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Analyzing Your Data

Before feeding your labeled data to an ML algorithm, it is a good practice to inspect your data to identify
issues and gain insights about the data you are using. The predictive power of your model will only be as
good as the data you feed it.

When analyzing your data, you should keep the following considerations in mind:

- Variable and target data summaries – It is useful to understand the values that your variables take and
  which values are dominant in your data. You could run these summaries by a subject matter expert
  for the problem that you want to solve. Ask yourself or the subject matter expert: Does the data
  match your expectations? Does it look like you have a data collection problem? Is one class in your
  target more frequent than the other classes? Are there more missing values or invalid data than you
  expect?
- Variable-target correlations – Knowing the correlation between each variable and the target class is
  helpful because a high correlation implies that there is a relationship between the variable and the
  target class. In general, you want to include variables with high correlation because they are the ones
  with higher predictive power (signal), and leave out variables with low correlation because they are
  likely irrelevant.
  In Amazon ML, you can analyze your data by creating a data source and by reviewing the
  resulting data report.
