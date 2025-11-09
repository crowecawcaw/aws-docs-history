# Perform exploratory data analysis (EDA)

Data Wrangler includes built-in analyses that help you generate visualizations and data
analyses in a few clicks. You can also create custom analyses using your own code.

You add an analysis to a dataframe by selecting a step in your data flow, and then
choosing **Add analysis**. To access an analysis you've created, select the
step that contains the analysis, and select the analysis.

Analyses are generated using a sample of up to 200,000 rows of your dataset, and you can configure the sample size.
For more information about changing the sample size of your data flow, see
[Edit the data flow sampling configuration](canvas-data-flow-edit-sampling.md "canvas-data-flow-edit-sampling.md").

###### Note

Analyses are optimized for data with 1000 or fewer columns. You
may experience some latency when generating analyses for data with additional columns.

You can add the following analysis to a dataframe:

- Data visualizations, including histograms and scatter plots.
- A quick summary of your dataset, including number of entries, minimum and maximum
  values (for numeric data), and most and least frequent categories (for categorical
  data).
- A quick model of the dataset, which can be used to generate an importance score
  for each feature.
- A target leakage report, which you can use to determine if one or more features
  are strongly correlated with your target feature.
- A custom visualization using your own code.
  Use the following sections to learn more about these options.

## Get insights on data and data quality

Use the **Data Quality and Insights Report** to perform an analysis of
the data that you've imported into Data Wrangler. We recommend that you create the report after you
import your dataset. You can use the report to help you clean and process your data. It
gives you information such as the number of missing values and the number of outliers. If
you have issues with your data, such as target leakage or imbalance, the insights report can
bring those issues to your attention.

Use the following procedure to create a Data Quality and Insights report. It assumes that you've already imported a dataset into your Data Wrangler flow.

###### To create a Data Quality and Insights report

1. Choose the ellipsis icon next to a node in your Data Wrangler flow.
2. Select **Get data insights**.
3. For **Analysis type**, select **Data Quality and Insights Report**.
4. For **Analysis name**, specify a name for the insights report.
5. For **Problem type**, specify **Regression** or **Classification**.
6. For **Target column**, specify the target column.
7. For **Data size**, specify one of the following:
   - **Sampled dataset** – Uses the interactive sample from your data flow,
     which can contain up to 200,000 rows of your dataset. For information about how to
     edit the size of your sample, see [Edit the data flow sampling configuration](canvas-data-flow-edit-sampling.md "canvas-data-flow-edit-sampling.md").
   - **Full dataset** – Uses the full dataset from your data source to create the report.

###### Note

Creating a Data Quality and Insights report on the full dataset uses an Amazon SageMaker processing job.
A SageMaker Processing job provisions the additional compute resources required to get insights for all of your data.
For more information about SageMaker Processing jobs, see [Data transformation
workloads with SageMaker Processing](processing-job.md "processing-job.md"). 8. Choose **Create**.

The following topics show the sections of the report:

###### Topics

- [Summary](#canvas-data-insights-summary "#canvas-data-insights-summary")
- [Target column](#canvas-data-insights-target-column "#canvas-data-insights-target-column")
- [Quick model](#canvas-data-insights-quick-model "#canvas-data-insights-quick-model")
- [Feature summary](#canvas-data-insights-feature-summary "#canvas-data-insights-feature-summary")
- [Samples](#canvas-data-insights-samples "#canvas-data-insights-samples")
- [Definitions](#canvas-data-insights-definitions "#canvas-data-insights-definitions")

You can either download the report or view it online. To download the report, choose the
download button at the top right corner of the screen.

### Summary

The insights report has a brief summary of the data that includes general information
such as missing values, invalid values, feature types, outlier counts, and more. It can
also include high severity warnings that point to probable issues with the data. We
recommend that you investigate the warnings.

### Target column

When you create the Data Quality and Insights Report, Data Wrangler gives you the option to
select a target column. A target column is a column that you're trying to predict. When
you choose a target column, Data Wrangler automatically creates a target column analysis. It also
ranks the features in the order of their predictive power. When you select a target
column, you must specify whether you’re trying to solve a regression or a classification
problem.

For classification, Data Wrangler shows a table and a histogram of the most common classes. A
class is a category. It also presents observations, or rows, with a missing or invalid
target value.

For regression, Data Wrangler shows a histogram of all the values in the target column. It also
presents observations, or rows, with a missing, invalid, or outlier target value.

### Quick model

The **Quick model** provides an estimate of the expected predicted
quality of a model that you train on your data.

Data Wrangler splits your data into training and validation folds. It uses 80% of the samples
for training and 20% of the values for validation. For classification, the sample is
stratified split. For a stratified split, each data partition has the same ratio of
labels. For classification problems, it's important to have the same ratio of labels
between the training and classification folds. Data Wrangler trains the XGBoost model with the
default hyperparameters. It applies early stopping on the validation data and performs
minimal feature preprocessing.

For classification models, Data Wrangler returns both a model summary and a confusion
matrix.

To learn more about the
information that the classification model summary returns, see [Definitions](#canvas-data-insights-definitions "#canvas-data-insights-definitions").

A confusion matrix gives you the following information:

- The number of times the predicted label matches the true label.
- The number of times the predicted label doesn't match the true label.

The true label represents an actual observation in your data. For example, if you're
using a model to detect fraudulent transactions, the true label represents a transaction
that is actually fraudulent or non-fraudulent. The predicted label represents the label
that your model assigns to the data.

You can use the confusion matrix to see how well the model predicts the presence or
the absence of a condition. If you're predicting fraudulent transactions, you can use
the confusion matrix to get a sense of both the sensitivity and the specificity of the
model. The sensitivity refers to the model's ability to detect fraudulent transactions.
The specificity refers to the model's ability to avoid detecting non-fraudulent
transactions as fraudulent.

### Feature summary

When you specify a target column, Data Wrangler orders the features by their prediction power.
Prediction power is measured on the data after it is split into 80% training and 20%
validation folds. Data Wrangler fits a model for each feature separately on the training fold. It
applies minimal feature preprocessing and measures prediction performance on the
validation data.

It normalizes the scores to the range [0,1]. Higher prediction scores indicate columns
that are more useful for predicting the target on their own. Lower scores point to
columns that aren’t predictive of the target column.

It’s uncommon for a column that isn’t predictive on its own to be predictive when it’s
used in tandem with other columns. You can confidently use the prediction scores to
determine whether a feature in your dataset is predictive.

A low score usually indicates the feature is redundant. A score of 1 implies perfect
predictive abilities, which often indicates target leakage. Target leakage usually
happens when the dataset contains a column that isn’t available at the prediction time.
For example, it could be a duplicate of the target column.

### Samples

Data Wrangler provides information about whether your samples are anomalous or if there are
duplicates in your dataset.

Data Wrangler detects anomalous samples using the _isolation forest
algorithm_. The isolation forest associates an anomaly score with each
sample (row) of the dataset. Low anomaly scores indicate anomalous samples. High scores
are associated with non-anomalous samples. Samples with a negative anomaly score are
usually considered anomalous and samples with positive anomaly score are considered
non-anomalous.

When you look at a sample that might be anomalous, we recommend that you pay attention
to unusual values. For example, you might have anomalous values that result from errors
in gathering and processing the data. The following is an example of the most anomalous
samples according to the Data Wrangler’s implementation of the isolation forest algorithm. We
recommend using domain knowledge and business logic when you examine the anomalous
samples.

Data Wrangler detects duplicate rows and calculates the ratio of duplicate rows in your data.
Some data sources could include valid duplicates. Other data sources could have
duplicates that point to problems in data collection. Duplicate samples that result from
faulty data collection could interfere with machine learning processes that rely on
splitting the data into independent training and validation folds.

The following are elements of the insights report that can be impacted by duplicated
samples:

- Quick model
- Prediction power estimation
- Automatic hyperparameter tuning

You can remove duplicate samples from the dataset using the **Drop
duplicates** transform under **Manage rows**. Data Wrangler shows
you the most frequently duplicated rows.

### Definitions

The following are definitions for the technical terms that are used in the data
insights report.

Feature types
The following are the definitions for each of the feature types:

- **Numeric** – Numeric values
  can be either floats or integers, such as age or income. The machine
  learning models assume that numeric values are ordered and a
  distance is defined over them. For example, 3 is closer to 4 than to
  10 and 3 < 4 < 10.
- **Categorical** – The column entries belong to a set of unique
  values, which is usually much smaller than the number of entries in
  the column. For example, a column of length 100 could contain the
  unique values `Dog`, `Cat`, and
  `Mouse`. The values could be numeric, text, or a
  combination of both. `Horse`, `House`,
  `8`, `Love`, and `3.1` would
  all be valid values and could be found in the same categorical
  column. The machine learning model does not assume order or distance
  on the values of categorical features, as opposed to numeric
  features, even when all the values are numbers.
- **Binary** – Binary features
  are a special categorical feature type in which the cardinality of
  the set of unique values is 2.
- **Text** – A text column
  contains many non-numeric unique values. In extreme cases, all the
  elements of the column are unique. In an extreme case, no two
  entries are the same.
- **Datetime** – A datetime
  column contains information about the date or time. It can have
  information about both the date and time.

Feature statistics
The following are definitions for each of the feature statistics:

- **Prediction power** –
  Prediction power measures how useful the column is in predicting the
  target.
- **Outliers** (in numeric columns)
  – Data Wrangler detects outliers using two statistics that are robust
  to outliers: median and robust standard deviation (RSTD). RSTD is
  derived by clipping the feature values to the range [5 percentile,
  95 percentile] and calculating the standard deviation of the clipped
  vector. All values larger than median + 5 \* RSTD or smaller than
  median - 5 \* RSTD are considered to be outliers.
- **Skew** (in numeric columns) –
  Skew measures the symmetry of the distribution and is defined as the
  third moment of the distribution divided by the third power of the
  standard deviation. The skewness of the normal distribution or any
  other symmetric distribution is zero. Positive values imply that the
  right tail of the distribution is longer than the left tail.
  Negative values imply that the left tail of the distribution is
  longer than the right tail. As a rule of thumb, a distribution is
  considered skewed when the absolute value of the skew is larger than

3.

- **Kurtosis** (in numeric columns)
  – Pearson's kurtosis measures the heaviness of the tail of the
  distribution. It's defined as the fourth moment of the distribution
  divided by the square of the second moment. The kurtosis of the
  normal distribution is 3. Kurtosis values lower than 3 imply that
  the distribution is concentrated around the mean and the tails are
  lighter than the tails of the normal distribution. Kurtosis values
  higher than 3 imply heavier tails or outliers.
- **Missing values** – Null-like
  objects, empty strings and strings composed of only white spaces are
  considered missing.
- **Valid values for numeric features or
  regression target** – All values that you can
  cast to finite floats are valid. Missing values are not
  valid.
- **Valid values for categorical, binary, or
  text features, or for classification target** –
  All values that are not missing are valid.
- **Datetime features** – All
  values that you can cast to a datetime object are valid. Missing
  values are not valid.
- **Invalid values** – Values
  that are either missing or you can't properly cast. For example, in
  a numeric column, you can't cast the string `"six"` or a
  null value.

Quick model metrics for regression
The following are the definitions for the quick model metrics:

- R2 or coefficient of determination) – R2 is the proportion
  of the variation in the target that is predicted by the model. R2 is
  in the range of [-infty, 1]. 1 is the score of the model that
  predicts the target perfectly and 0 is the score of the trivial
  model that always predicts the target mean.
- MSE or mean squared error – MSE is in the range [0, infty].
  0 is the score of the model that predicts the target
  perfectly.
- MAE or mean absolute error – MAE is in the range [0, infty]
  where 0 is the score of the model that predicts the target
  perfectly.
- RMSE or root mean square error – RMSE is in the range [0,
  infty] where 0 is the score of the model that predicts the target
  perfectly.
- Max error – The maximum absolute value of the error over the
  dataset. Max error is in the range [0, infty]. 0 is the score of the
  model that predicts the target perfectly.
- Median absolute error – Median absolute error is in the
  range [0, infty]. 0 is the score of the model that predicts the
  target perfectly.

Quick model metrics for classification
The following are the definitions for the quick model metrics:

- **Accuracy** – Accuracy is the
  ratio of samples that are predicted accurately. Accuracy is in the
  range [0, 1]. 0 is the score of the model that predicts all samples
  incorrectly and 1 is the score of the perfect model.
- **Balanced accuracy** –
  Balanced accuracy is the ratio of samples that are predicted
  accurately when the class weights are adjusted to balance the data.
  All classes are given the same importance, regardless of their
  frequency. Balanced accuracy is in the range [0, 1]. 0 is the score
  of the model that predicts all samples wrong. 1 is the score of the
  perfect model.
- **AUC (binary classification)**
  – This is the area under the receiver operating characteristic
  curve. AUC is in the range [0, 1] where a random model returns a
  score of 0.5 and the perfect model returns a score of 1.
- **AUC (OVR)** – For multiclass
  classification, this is the area under the receiver operating
  characteristic curve calculated separately for each label using one
  versus rest. Data Wrangler reports the average of the areas. AUC is in the
  range [0, 1] where a random model returns a score of 0.5 and the
  perfect model returns a score of 1.
- **Precision** – Precision is
  defined for a specific class. Precision is the fraction of true
  positives out of all the instances that the model classified as that
  class. Precision is in the range [0, 1]. 1 is the score of the model
  that has no false positives for the class. For binary
  classification, Data Wrangler reports the precision of the positive
  class.
- **Recall** – Recall is defined
  for a specific class. Recall is the fraction of the relevant class
  instances that are successfully retrieved. Recall is in the range
  [0, 1]. 1 is the score of the model that classifies all the
  instances of the class correctly. For binary classification, Data Wrangler
  reports the recall of the positive class.
- **F1** – F1 is defined for a
  specific class. It's the harmonic mean of the precision and recall.
  F1 is in the range [0, 1]. 1 is the score of the perfect model. For
  binary classification, Data Wrangler reports the F1 for classes with positive
  values.

Textual patterns
**Patterns** describe the textual format of a string using an easy to read format. The following are examples of textual patterns:

- "{digits:4-7}" describes a sequence of digits that have a length between 4 and 7.
- "{alnum:5}" describes an alpha-numeric string with a length of exactly 5.

Data Wrangler infers the patterns by looking at samples of non-empty strings from your data. It can describe many of the commonly used patterns. The **confidence** expressed as a percentage indicates how much of the data is estimated to match the pattern.
Using the textual pattern, you can see which rows in your data you need to correct or drop.

The following describes the patterns that Data Wrangler can recognize:

| Pattern      | Textual Format                         |
| ------------ | -------------------------------------- |
| {alnum}      | Alphanumeric strings                   |
| {any}        | Any string of word characters          |
| {digits}     | A sequence of digits                   |
| {lower}      | A lowercase word                       |
| {mixed}      | A mixed-case word                      |
| {name}       | A word beginning with a capital letter |
| {upper}      | An uppercase word                      |
| {whitespace} | Whitespace characters                  |

A word character is either an underscore or a character that might appear in a word in any language. For example, the strings `'Hello_word'` and `'écoute'` both consist of word characters. 'H' and 'é' are both examples of word characters.

## Bias report

SageMaker Canvas provides the bias report in Data Wrangler to help uncover potential biases in your data.
The bias report analyzes the relationship between the target column (label) and a column
that you believe might contain bias (facet variable). For example, if you are trying to
predict customer conversion, the facet variable may be the age of the customer. The bias
report can help you determine whether or not your data is biased toward a certain age
group.

To generate a bias report in Canvas, do the following:

1. In your data flow in Data Wrangler, choose the **More options** icon (
   ![Vertical ellipsis icon representing a menu or more options.](images/studio/canvas/more-options-icon.png)
   ) next to a node in the flow.
2. From the context menu, choose **Get data insights**.
3. The **Create analysis** side panel opens.
   For the **Analysis type** dropdown menu, select **Bias Report**.
4. In the **Analysis name** field, enter a name for the bias report.
5. For the **Select the column your model predicts (target)** dropdown menu,
   select your target column.
6. For **Is your predicted column a value or threshold?**, select
   **Value** if your target column has categorical values or
   **Threshold** if it has numerical values.
7. For **Predicted value** (or **Predicted threshold**, depending
   on your selection in the previous step), enter the target column value or values that correspond to a positive outcome.
   For example, if predicting customer conversion, your value might be `yes` to indicate that a customer was converted.
8. For the **Select the column to analyze for bias** dropdown menu, select the
   column that you believe might contain bias, also known as the facet
   variable.
9. For **Is your column a value or threshold?**, select
   **Value** if the facet variable has categorical values or
   **Threshold** if it has numerical values.
10. For **Column value(s) to analyze for bias** (or
    **Column threshold to analyze for bias**, depending on your selection in the previous step),
    enter the value or values that you want to analyze for potential bias. For example, if you're checking for
    bias against customers over a certain age, use the beginning of that age range as your threshold.
11. For **Choose bias metrics**, select the bias metrics you'd like to include
    in your bias report. Hover over the info icons for more information about each metric.
12. (Optional) When prompted with the option **Would you like to analyze additional
    metrics?**, select **Yes** to view and include more bias metrics.
13. When you're ready to create the bias report, choose **Add**.

Once generated, the report gives you an overview of the bias metrics you selected. You can view
the bias report at any time from the **Analyses** tab of your data flow.

## Histogram

Use histograms to see the counts of feature values for a specific feature. You can
inspect the relationships between features using the **Color by**
option.

You can use the **Facet by** feature to create histograms of one
column, for each value in another column.

## Scatter plot

Use the **Scatter Plot** feature to inspect the relationship between
features. To create a scatter plot, select a feature to plot on the **X
axis** and the **Y axis**. Both of these columns must be
numeric typed columns.

You can color scatter plots by an additional column.

Additionally, you can facet scatter plots by features.

## Table summary

Use the **Table Summary** analysis to quickly summarize your
data.

For columns with numerical data, including log and float data, a table summary reports
the number of entries (count), minimum (min), maximum (max), mean, and standard
deviation (stddev) for each column.

For columns with non-numerical data, including columns with string, Boolean, or
date/time data, a table summary reports the number of entries (count), least frequent
value (min), and most frequent value (max).

## Quick model

Use the **Quick Model** visualization to quickly evaluate your data
and produce importance scores for each feature. A [feature importance score](http://spark.apache.org/docs/2.1.0/api/python/pyspark.ml.html#pyspark.ml.classification.DecisionTreeClassificationModel.featureImportances "http://spark.apache.org/docs/2.1.0/api/python/pyspark.ml.html#pyspark.ml.classification.DecisionTreeClassificationModel.featureImportances") score indicates how useful a feature is at
predicting a target label. The feature importance score is between [0, 1] and a higher
number indicates that the feature is more important to the whole dataset. On the top of
the quick model chart, there is a model score. A classification problem shows an F1
score. A regression problem has a mean squared error (MSE) score.

When you create a quick model chart, you select a dataset you want evaluated, and a
target label against which you want feature importance to be compared. Data Wrangler does the
following:

- Infers the data types for the target label and each feature in the dataset
  selected.
- Determines the problem type. Based on the number of distinct values in the
  label column, Data Wrangler determines if this is a regression or classification problem
  type. Data Wrangler sets a categorical threshold to 100. If there are more than 100
  distinct values in the label column, Data Wrangler classifies it as a regression problem;
  otherwise, it is classified as a classification problem.
- Pre-processes features and label data for training. The algorithm used
  requires encoding features to vector type and encoding labels to double type.
- Trains a random forest algorithm with 70% of data. Spark’s [RandomForestRegressor](https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression "https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-regression") is used to train a model for regression
  problems. The [RandomForestClassifier](https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-classifier "https://spark.apache.org/docs/latest/ml-classification-regression.html#random-forest-classifier") is used to train a model for classification
  problems.
- Evaluates a random forest model with the remaining 30% of data. Data Wrangler evaluates
  classification models using an F1 score and evaluates regression models using an
  MSE score.
- Calculates feature importance for each feature using the Gini importance
  method.

## Target leakage

Target leakage occurs when there is data in a machine learning training dataset that
is strongly correlated with the target label, but is not available in real-world data.
For example, you may have a column in your dataset that serves as a proxy for the column
you want to predict with your model.

When you use the **Target Leakage** analysis, you specify the
following:

- **Target**: This is the feature about which you want your ML
  model to be able to make predictions.
- **Problem type**: This is the ML problem type on which you
  are working. Problem type can either be **classification** or
  **regression**.
- (Optional) **Max features**: This is the maximum number of
  features to present in the visualization, which shows features ranked by their
  risk of being target leakage.

For classification, the target leakage analysis uses the area under the receiver
operating characteristic, or AUC - ROC curve for each column, up to **Max
features**. For regression, it uses a coefficient of determination, or R2
metric.

The AUC - ROC curve provides a predictive metric, computed individually for each
column using cross-validation, on a sample of up to around 1000 rows. A score of 1
indicates perfect predictive abilities, which often indicates target leakage. A score of
0.5 or lower indicates that the information on the column could not provide, on its own,
any useful information towards predicting the target. Although it can happen that a
column is uninformative on its own but is useful in predicting the target when used in
tandem with other features, a low score could indicate the feature is redundant.

## Multicollinearity

Multicollinearity is a circumstance where two or more predictor variables are related
to each other. The predictor variables are the features in your dataset that you're
using to predict a target variable. When you have multicollinearity, the predictor
variables are not only predictive of the target variable, but also predictive of each
other.

You can use the **Variance Inflation Factor (VIF)**,
**Principal Component Analysis (PCA)**, or **Lasso feature
selection** as measures for the multicollinearity in your data. For more
information, see the following.

Variance Inflation Factor (VIF)
The Variance Inflation Factor (VIF) is a measure of collinearity among
variable pairs. Data Wrangler returns a VIF score as a measure of how closely the
variables are related to each other. A VIF score is a positive number that
is greater than or equal to 1.

A score of 1 means that the variable is uncorrelated with the other
variables. Scores greater than 1 indicate higher correlation.

Theoretically, you can have a VIF score with a value of infinity. Data Wrangler
clips high scores to 50. If you have a VIF score greater than 50, Data Wrangler sets
the score to 50.

You can use the following guidelines to interpret your VIF scores:

- A VIF score less than or equal to 5 indicates that the variables
  are moderately correlated with the other variables.
- A VIF score greater than or equal to 5 indicates that the
  variables are highly correlated with the other variables.

Principle Component Analysis (PCA)
Principal Component Analysis (PCA) measures the variance of the data along
different directions in the feature space. The feature space consists of all
the predictor variables that you use to predict the target variable in your
dataset.

For example, if you're trying to predict who survived on the _RMS
Titanic_ after it hit an iceberg, your feature space can
include the passengers' age, gender, and the fare that they paid.

From the feature space, PCA generates an ordered list of variances. These
variances are also known as singular values. The values in the list of
variances are greater than or equal to 0. We can use them to determine how
much multicollinearity there is in our data.

When the numbers are roughly uniform, the data has very few instances of
multicollinearity. When there is a lot of variability among the values, we
have many instances of multicollinearity. Before it performs PCA, Data Wrangler
normalizes each feature to have a mean of 0 and a standard deviation of

1.

###### Note

PCA in this circumstance can also be referred to as Singular Value
Decomposition (SVD).

Lasso feature selection
Lasso feature selection uses the L1 regularization technique to only
include the most predictive features in your dataset.

For both classification and regression, the regularization technique
generates a coefficient for each feature. The absolute value of the
coefficient provides an importance score for the feature. A higher
importance score indicates that it is more predictive of the target
variable. A common feature selection method is to use all the features that
have a non-zero lasso coefficient.

## Detect anomalies in time

series data

You can use the anomaly detection visualization to see outliers in your time series
data. To understand what determines an anomaly, you need to understand that we decompose
the time series into a predicted term and an error term. We treat the seasonality and
trend of the time series as the predicted term. We treat the residuals as the error
term.

For the error term, you specify a threshold as the number of standard of deviations
the residual can be away from the mean for it to be considered an anomaly. For example,
you can specify a threshold as being 3 standard deviations. Any residual greater than 3
standard deviations away from the mean is an anomaly.

You can use the following procedure to perform an **Anomaly
detection** analysis.

1. Open your Data Wrangler data flow.
2. In your data flow, under **Data types**, choose the
   **+**, and select **Add analysis**.
3. For **Analysis type**, choose **Time
   Series**.
4. For **Visualization**, choose **Anomaly
   detection**.
5. For **Anomaly threshold**, choose the threshold that a value is
   considered an anomaly.
6. Choose **Preview** to generate a preview of the analysis.
7. Choose **Add** to add the transform to the Data Wrangler data flow.

## Seasonal trend decomposition in

time series data

You can determine whether there's seasonality in your time series data by using the
Seasonal Trend Decomposition visualization. We use the STL (Seasonal Trend decomposition
using LOESS) method to perform the decomposition. We decompose the time series into its
seasonal, trend, and residual components. The trend reflects the long term progression
of the series. The seasonal component is a signal that recurs in a time period. After
removing the trend and the seasonal components from the time series, you have the
residual.

You can use the following procedure to perform a **Seasonal-Trend
decomposition** analysis.

1. Open your Data Wrangler data flow.
2. In your data flow, under **Data types**, choose the
   **+**, and select **Add analysis**.
3. For **Analysis type**, choose **Time
   Series**.
4. For **Visualization**, choose **Seasonal-Trend
   decomposition**.
5. For **Anomaly threshold**, choose the threshold that a value
   is considered an anomaly.
6. Choose **Preview** to generate a preview of the
   analysis.
7. Choose **Add** to add the transform to the Data Wrangler data
   flow.

## Create custom visualizations

You can add an analysis to your Data Wrangler flow to create a custom visualization. Your
dataset, with all the transformations you've applied, is available as a [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html"). Data Wrangler uses the `df` variable to store the
dataframe. You access the dataframe by calling the variable.

You must provide the output variable, `chart`, to store an [Altair](https://altair-viz.github.io/ "https://altair-viz.github.io/") output chart. For example, you
can use the following code block to create a custom histogram using the Titanic
dataset.

```
import altair as alt
df = df.iloc[:30]
df = df.rename(columns={"Age": "value"})
df = df.assign(count=df.groupby('value').value.transform('count'))
df = df[["value", "count"]]
base = alt.Chart(df)
bar = base.mark_bar().encode(x=alt.X('value', bin=True, axis=None), y=alt.Y('count'))
rule = base.mark_rule(color='red').encode(
    x='mean(value):Q',
    size=alt.value(5))
chart = bar + rule
```

###### To create a custom visualization:

1. Next to the node containing the transformation that you'd like to visualize,
   choose the **+**.
2. Choose **Add analysis**.
3. For **Analysis type**, choose **Custom
   Visualization**.
4. For **Analysis name**, specify a name.
5. Enter your code in the code box.
6. Choose **Preview** to preview your visualization.
7. Choose **Save** to add your visualization.

If you don’t know how to use the Altair visualization package in Python, you can use
custom code snippets to help you get started.

Data Wrangler has a searchable collection of visualization snippets. To use a visualization
snippet, choose **Search example snippets** and specify a query in the
search bar.

The following example uses the **Binned scatterplot** code snippet.
It plots a histogram for 2 dimensions.

The snippets have comments to help you understand the changes that you need to make to
the code. You usually need to specify the column names of your dataset in the
code.

```

import altair as alt

# Specify the number of top rows for plotting
rows_number = 1000
df = df.head(rows_number)
# You can also choose bottom rows or randomly sampled rows
# df = df.tail(rows_number)
# df = df.sample(rows_number)


chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        # Specify the column names for binning and number of bins for X and Y axis
        x=alt.X("col1:Q", bin=alt.Bin(maxbins=20)),
        y=alt.Y("col2:Q", bin=alt.Bin(maxbins=20)),
        size="count()",
    )
)

# :Q specifies that label column has quantitative type.
# For more details on Altair typing refer to
# https://altair-viz.github.io/user_guide/encoding.html#encoding-data-types

```
