We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Creating and Using Datasources

You can use Amazon ML
datasources to train an ML model, evaluate an ML model, and generate batch predictions using an
ML model. Datasource objects contain metadata about your input data. When you create a
datasource, Amazon ML reads your input data, computes descriptive statistics on its attributes, and
stores the statistics, a schema, and other information as part of the datasource object. After
you create a datasource, you can use the [Amazon ML data insights](creating_datasources.md#data-insights "creating_datasources.md#data-insights") to
explore statistical properties of your input data, and you can use the
datasource to [train an ML model](training_models.md "training_models.md").

###### Note

This section assumes that you are familiar with [Amazon Machine Learning concepts](amazon-machine-learning-key-concepts.md "amazon-machine-learning-key-concepts.md").

###### Topics

- [Understanding the Data Format for
  Amazon ML](understanding-the-data-format-for-amazon-ml.md "understanding-the-data-format-for-amazon-ml.md")
- [Creating a Data Schema for Amazon ML](creating-a-data-schema-for-amazon-ml.md "creating-a-data-schema-for-amazon-ml.md")
- [Splitting Your Data](splitting-types.md "splitting-types.md")
- [Data Insights](data-insights.md "data-insights.md")
- [Using Amazon S3 with Amazon ML](using-amazon-s3-with-amazon-ml.md "using-amazon-s3-with-amazon-ml.md")
- [Creating an Amazon ML Datasource from Data in
  Amazon Redshift](using-amazon-redshift-with-amazon-ml.md "using-amazon-redshift-with-amazon-ml.md")
- [Using Data from an Amazon RDS Database to Create an
  Amazon ML Datasource](using-amazon-rds-with-amazon-ml.md "using-amazon-rds-with-amazon-ml.md")
