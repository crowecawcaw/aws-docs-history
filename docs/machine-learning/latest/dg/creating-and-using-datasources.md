

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Creating and Using Datasources
<a name="creating-and-using-datasources"></a>

You can use Amazon ML datasources to train an ML model, evaluate an ML model, and generate batch predictions using an ML model. Datasource objects contain metadata about your input data. When you create a datasource, Amazon ML reads your input data, computes descriptive statistics on its attributes, and stores the statistics, a schema, and other information as part of the datasource object. After you create a datasource, you can use the [Amazon ML data insights](https://docs.aws.amazon.com/machine-learning/latest/dg/creating_datasources.html#data-insights) to explore statistical properties of your input data, and you can use the datasource to [train an ML model](https://docs.aws.amazon.com/machine-learning/latest/dg/training_models.html). 

**Note**  
This section assumes that you are familiar with [Amazon Machine Learning concepts](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html).

**Topics**
+ [Understanding the Data Format for Amazon ML](understanding-the-data-format-for-amazon-ml.md)
+ [Creating a Data Schema for Amazon ML](creating-a-data-schema-for-amazon-ml.md)
+ [Splitting Your Data](splitting-types.md)
+ [Data Insights](data-insights.md)
+ [Using Amazon S3 with Amazon ML](using-amazon-s3-with-amazon-ml.md)
+ [Creating an Amazon ML Datasource from Data in Amazon Redshift](using-amazon-redshift-with-amazon-ml.md)
+ [Using Data from an Amazon RDS Database to Create an Amazon ML Datasource](using-amazon-rds-with-amazon-ml.md)