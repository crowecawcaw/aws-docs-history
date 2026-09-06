

We are no longer updating the Amazon Machine Learning service or accepting new users for it. This documentation is available for existing users, but we are no longer updating it. For more information, see [ What is Amazon Machine Learning](https://docs.aws.amazon.com/machine-learning/latest/dg/what-is-amazon-machine-learning.html).

# Feature Transformations with Data Recipes
<a name="feature-transformations-with-data-recipes"></a>

 There are two ways to transform features before creating ML models with Amazon ML: you can transform your input data directly before showing it to Amazon ML, or you can use the built-in data transformations of Amazon ML. You can use Amazon ML recipes, which are pre-formatted instructions for common transformations. With recipes, you can do the following: 
+  Choose from a list of built-in common machine learning transformations, and apply these to individual variables or groups of variables 
+  Select which of the input variables and transformations are made available to the machine learning process 

 Using Amazon ML recipes offers several advantages. Amazon ML performs the data transformations for you, so you do not need to implement them yourself. In addition, they are fast because Amazon ML applies the transformations while reading input data, and provides results to the learning process without the intermediate step of saving results to disk. 