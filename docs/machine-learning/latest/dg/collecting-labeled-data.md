We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Collecting Labeled Data

ML problems start with data—preferably, lots of data (examples or observations) for which you already
know the target answer. Data for which you already know the target answer is called _labeled data_. In
supervised ML, the algorithm teaches itself to learn from the labeled examples that we provide.

Each example/observation in your data must contain two elements:

- The target – The answer that you want to predict. You provide data that is labeled with the target
  (correct answer) to the ML algorithm to learn from. Then, you will use the trained ML model to
  predict this answer on data for which you do not know the target answer.
- Variables/features – These are attributes of the example that can be used to identify patterns to
  predict the target answer.
  For example, for the email classification problem, the target is a label that indicates whether an email is
  spam or not spam. Examples of variables are the sender of the email, the text in the body of the email, the
  text in the subject line, the time the email was sent, and the existence of previous correspondence between
  the sender and receiver.

Often, data is not readily available in a labeled form. Collecting and preparing the variables and the target
are often the most important steps in solving an ML problem. The example data should be representative of
the data that you will have when you are using the model to make a prediction. For example, if you want to
predict whether an email is spam or not, you must collect both positive (spam emails) and negative
(non-spam emails) for the machine learning algorithm to be able to find patterns that will distinguish
between the two types of email.

Once you have the labelled data, you might need to convert it to a format that is acceptable to your
algorithm or software. For example, to use Amazon ML you need to convert the data to
comma-separated (CSV) format with each example making up one row of the CSV file, each column
containing one input variable, and one column containing the target answer.
