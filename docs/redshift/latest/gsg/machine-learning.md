Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Training machine learning models with Amazon Redshift data

Using Amazon Redshift machine learning (Amazon Redshift ML), you can train a model by providing the data to Amazon Redshift. Then Amazon Redshift ML creates models that capture patterns in the input data. You can then use these models to generate predictions for new input data without incurring additional costs. By using Amazon Redshift ML, you can train machine learning models using SQL statements and invoke them in SQL queries for prediction. You can continue to improve the accuracy of the predictions by iteratively changing parameters and improving your training data.

Amazon Redshift ML makes it easier for SQL users to create, train, and deploy machine learning
models using familiar SQL commands. By using Amazon Redshift ML, you can use your data in Amazon Redshift
clusters to train models with Amazon SageMaker AI Autopilot and automatically get the best model.
You can then localize the models and make predictions from within an Amazon Redshift database.

For more information about Amazon Redshift ML, see [Getting started with Amazon Redshift
ML](../dg/getting-started-machine-learning.md "../dg/getting-started-machine-learning.md") in the _Amazon Redshift Database Developer Guide._
