We are no longer updating the Amazon Machine Learning service or accepting
new users for it. This documentation is available for existing users, but we are
no longer updating it. For more information, see [What is Amazon Machine Learning](what-is-amazon-machine-learning.md "what-is-amazon-machine-learning.md").

# Feature Processing

After getting to know your data through data summaries and visualizations, you might want to transform
your variables further to make them more meaningful. This is known as _feature processing_. For example,
say you have a variable that captures the date and time at which an event occurred. This date and time will
never occur again and hence won’t be useful to predict your target. However, if this variable is transformed
into features that represent the hour of the day, the day of the week, and the month, these variables could be
useful to learn if the event tends to happen at a particular hour, weekday, or month. Such feature processing
to form more generalizable data points to learn from can provide significant improvements to the predictive
models.

Other examples of common feature processing:

- Replacing missing or invalid data with more meaningful values (e.g., if you know that a missing
  value for a product type variable actually means it is a book, you can then replace all missing values
  in the product type with the value for book). A common strategy used to impute missing values is to
  replace missing values with the mean or median value. It is important to understand your data before
  choosing a strategy for replacing missing values.
- Forming Cartesian products of one variable with another. For example, if you have two variables,
  such as population density (urban, suburban, rural) and state (Washington, Oregon, California), there
  might be useful information in the features formed by a Cartesian product of these two variables
  resulting in features (urban_Washington, suburban_Washington, rural_Washington, urban_Oregon,
  suburban_Oregon, rural_Oregon, urban_California, suburban_California, rural_California).
- Non-linear transformations such as binning numeric variables to categories. In many cases, the
  relationship between a numeric feature and the target is not linear (the feature value does not increase
  or decrease monotonically with the target). In such cases, it might be useful to bin the numeric
  feature into categorical features representing different ranges of the numeric feature. Each
  categorical feature (bin) can then be modeled as having its own linear relationship with the target.
  For example, say you know that the continuous numeric feature age is not linearly correlated with
  the likelihood to purchase a book. You can bin age into categorical features that might be able to
  capture the relationship with the target more accurately. The optimum number of bins for a numeric
  variable is dependent on characteristics of the variable and its relationship to the target, and this is
  best determined through experimentation. Amazon ML suggests the optimal bin
  number for a numeric feature based on data statistics in the suggested recipe. See the Developer
  Guide for details about the _suggested recipe_.
- Domain-specific features (e.g., you have length, breadth, and height as separate variables; you can
  create a new volume feature to be a product of these three variables).
- Variable-specific features. Some variable types such as text features, features that capture the
  structure of a web page, or the structure of a sentence have generic ways of processing that help
  extract structure and context. For example, forming _n-grams_ from text “the fox jumped over the fence” can be represented with _unigrams_: the, fox, jumped, over, fence or _bigrams_: the fox, fox
  jumped, jumped over, over the, the fence.
  Including more relevant features helps to improve prediction power. Clearly, it is not always possible to
  know the features with “signal” or predictive influence in advance. So it is good to include all features that
  can potentially be related to the target label and let the model training algorithm pick the features with the
  strongest correlations. In Amazon ML, feature processing can be specified in the recipe
  when creating a model. See the Developer Guide for a list of available feature processors.
