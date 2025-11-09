# XGBoost Version 0.72

###### Important

The XGBoost 0.72 is deprecated by Amazon SageMaker AI. You can still use this old version of
XGBoost (as a built-in algorithm) by pulling its image URI as shown in the following
code sample. For XGBoost, the image URI ending with `:1` is for the old
version.

SageMaker Python SDK v1

```
import boto3
from sagemaker.amazon.amazon_estimator import get_image_uri

xgb_image_uri = get_image_uri(boto3.Session().region_name, "xgboost", repo_version="1")
```

SageMaker Python SDK v2

```
import boto3
from sagemaker import image_uris

xgb_image_uri = image_uris.retrieve("xgboost", boto3.Session().region_name, "1")
```

If you want to use newer versions, you have to explicitly specify the image URI
tags (see [Supported versions](xgboost.md#xgboost-supported-versions "xgboost.md#xgboost-supported-versions")).

This previous release of the Amazon SageMaker AI XGBoost algorithm is based on the 0.72 release.
[XGBoost](https://github.com/dmlc/xgboost "https://github.com/dmlc/xgboost") (eXtreme Gradient
Boosting) is a popular and efficient open-source implementation of the gradient boosted
trees algorithm. Gradient boosting is a supervised learning algorithm that attempts to
accurately predict a target variable by combining the estimates of a set of simpler,
weaker models. XGBoost has done remarkably well in machine learning competitions because
it robustly handles a variety of data types, relationships, and distributions, and
because of the large number of hyperparameters that can be tweaked and tuned for
improved fits. This flexibility makes XGBoost a solid choice for problems in regression,
classification (binary and multiclass), and ranking.

Customers should consider using the new release of [XGBoost algorithm with Amazon SageMaker AI](xgboost.md "xgboost.md"). They can use it as a SageMaker AI built-in algorithm or as a
framework to run scripts in their local environments as they would typically, for
example, do with a Tensorflow deep learning framework. The new implementation has a
smaller memory footprint, better logging, improved hyperparameter validation, and an
expanded set of metrics. The earlier implementation of XGBoost remains available to
customers if they need to postpone migrating to the new version. But this previous
implementation will remain tied to the 0.72 release of XGBoost.

## Input/Output Interface for the XGBoost

Release 0.72

Gradient boosting operates on tabular data, with the rows representing
observations, one column representing the target variable or label, and the
remaining columns representing features.

The SageMaker AI implementation of XGBoost supports CSV and libsvm formats for training
and inference:

- For Training ContentType, valid inputs are
  _text/libsvm_ (default) or
  _text/csv_.
- For Inference ContentType, valid inputs are
  _text/libsvm_ or (the default)
  _text/csv_.

###### Note

For CSV training, the algorithm assumes that the target variable is in the
first column and that the CSV does not have a header record. For CSV inference,
the algorithm assumes that CSV input does not have the label column.

For libsvm training, the algorithm assumes that the label is in the first
column. Subsequent columns contain the zero-based index value pairs for
features. So each row has the format: <label>
<index0>:<value0> <index1>:<value1> ... Inference
requests for libsvm may or may not have labels in the libsvm format.

This differs from other SageMaker AI algorithms, which use the protobuf training input
format to maintain greater consistency with standard XGBoost data formats.

For CSV training input mode, the total memory available to the algorithm (Instance
Count \* the memory available in the `InstanceType`) must be able to hold
the training dataset. For libsvm training input mode, it's not required, but we
recommend it.

SageMaker AI XGBoost uses the Python pickle module to serialize/deserialize the model,
which can be used for saving/loading the model.

###### To use a model trained with SageMaker AI XGBoost in open source XGBoost

- Use the following Python code:

```
import pickle as pkl
import tarfile
import xgboost

t = tarfile.open('model.tar.gz', 'r:gz')
t.extractall()

model = pkl.load(open(`model_file_path`, 'rb'))

# prediction with test data
pred = model.predict(`dtest`)
```

###### To differentiate the importance of labelled data points use Instance Weight

Supports

- SageMaker AI XGBoost allows customers to differentiate the importance of labelled
  data points by assigning each instance a weight value. For
  _text/libsvm_ input, customers can assign weight
  values to data instances by attaching them after the labels. For example,
  `label:weight idx_0:val_0 idx_1:val_1...`. For
  _text/csv_ input, customers need to turn on the
  `csv_weights` flag in the parameters and attach weight values
  in the column after labels. For example:
  `label,weight,val_0,val_1,...`).

## EC2 Instance Recommendation for the XGBoost

Release 0.72

SageMaker AI XGBoost currently only trains using CPUs. It is a memory-bound (as opposed to
compute-bound) algorithm. So, a general-purpose compute instance (for example, M4)
is a better choice than a compute-optimized instance (for example, C4). Further, we
recommend that you have enough total memory in selected instances to hold the
training data. Although it supports the use of disk space to handle data that does
not fit into main memory (the out-of-core feature available with the libsvm input
mode), writing cache files onto disk slows the algorithm processing time.

## XGBoost Release 0.72 Sample

Notebooks

For a sample notebook that shows how to use the latest version of SageMaker AI XGBoost as
a built-in algorithm to train and host a regression model, see [Regression with Amazon SageMaker AI XGBoost algorithm](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_abalone.html "https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_amazon_algorithms/xgboost_abalone/xgboost_abalone.html"). To use the 0.72 version of
XGBoost, you need to change the version in the sample code to 0.72. For instructions
how to create and access Jupyter notebook instances that you can use to run the
example in SageMaker AI, see [Amazon SageMaker notebook instances](nbi.md "nbi.md"). Once you have
created a notebook instance and opened it, select the **SageMaker AI
Examples** tab to see a list of all the SageMaker AI samples. The topic
modeling example notebooks using the XGBoost algorithms are located in the **Introduction to Amazon algorithms** section. To open a
notebook, click on its **Use** tab and select **Create copy**.

## XGBoost Release 0.72

Hyperparameters

The following table contains the hyperparameters for the XGBoost algorithm. These
are parameters that are set by users to facilitate the estimation of model
parameters from data. The required hyperparameters that must be set are listed
first, in alphabetical order. The optional hyperparameters that can be set are
listed next, also in alphabetical order. The SageMaker AI XGBoost algorithm is an
implementation of the open-source XGBoost package. Currently SageMaker AI supports version
0.72. For more detail about hyperparameter configuration for this version of
XGBoost, see [XGBoost
Parameters](https://xgboost.readthedocs.io/en/release_0.72/parameter.html "https://xgboost.readthedocs.io/en/release_0.72/parameter.html").

| Parameter Name           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `num_class`              | The number of classes.<br>\*_Required_<br>• if<br>`objective` is set to<br>*multi:softmax<br>• or<br>*multi:softprob\*.<br>Valid values: integer                                                                                                                                                                                                                                                                                                                                                                             |
| `num_round`              | The number of rounds to run the training.<br>**Required**<br>Valid values: integer                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `alpha`                  | L1 regularization term on weights. Increasing this value<br>makes models more conservative.<br>**Optional**<br>Valid values: float<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                       |
| `base_score`             | The initial prediction score of all<br>instances,<br>global bias.<br>**Optional**<br>Valid values: float<br>Default value: 0.5                                                                                                                                                                                                                                                                                                                                                                                               |
| `booster`                | Which booster to use. The `gbtree` and<br>`dart` values use a tree-based model, while<br>`gblinear` uses a linear function.<br>**Optional**<br>Valid values: String. One of `gbtree`,<br>`gblinear`, or `dart`.<br>Default value: `gbtree`                                                                                                                                                                                                                                                                                   |
| `colsample_bylevel`      | Subsample ratio of columns for each split, in each<br>level.<br>**Optional**<br>Valid values: Float. Range: [0,1].<br>Default value: 1                                                                                                                                                                                                                                                                                                                                                                                       |
| `colsample_bytree`       | Subsample ratio of columns when constructing each<br>tree.<br>**Optional**<br>Valid values: Float. Range: [0,1].<br>Default value: 1                                                                                                                                                                                                                                                                                                                                                                                         |
| `csv_weights`            | When this flag is enabled, XGBoost differentiates the<br>importance of instances for csv input by taking the second<br>column (the column after labels) in training data as the<br>instance weights.<br>**Optional**<br>Valid values: 0 or 1<br>Default value: 0                                                                                                                                                                                                                                                             |
| `early_stopping_rounds`  | The model trains until the validation score stops<br>improving. Validation error needs to decrease at least every<br>`early_stopping_rounds` to continue training.<br>SageMaker AI hosting uses the best model for inference.<br>**Optional**<br>Valid values: integer<br>Default value: -                                                                                                                                                                                                                                   |
| `eta`                    | Step size shrinkage used in updates to prevent overfitting.<br>After each boosting step, you can directly get the weights of<br>new features. The `eta` parameter actually shrinks<br>the feature weights to make the boosting process more<br>conservative.<br>**Optional**<br>Valid values: Float. Range: [0,1].<br>Default value: 0.3                                                                                                                                                                                     |
| `eval_metric`            | Evaluation metrics for validation data. A default metric is<br>assigned according to the objective:<br>• `rmse`: for regression<br>• `error`: for classification<br>• `map`: for ranking<br>For a list of valid inputs, see [XGBoost Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters "https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters").<br>**Optional**<br>Valid values: string<br>Default value: Default according to objective. |
| `gamma`                  | Minimum loss reduction required to make a further partition<br>on a leaf node of the tree. The larger, the more conservative<br>the algorithm is.<br>**Optional**<br>Valid values: Float. Range: [0,∞).<br>Default value: 0                                                                                                                                                                                                                                                                                                  |
| `grow_policy`            | Controls the way that new nodes are added to the tree.<br>Currently supported only if `tree_method` is set to<br>`hist`.<br>**Optional**<br>Valid values: String. Either `depthwise` or<br>`lossguide`.<br>Default value: `depthwise`                                                                                                                                                                                                                                                                                        |
| `lambda`                 | L2 regularization term on weights. Increasing this value<br>makes models more conservative.<br>**Optional**<br>Valid values: float<br>Default value: 1                                                                                                                                                                                                                                                                                                                                                                       |
| `lambda_bias`            | L2 regularization term on bias.<br>**Optional**<br>Valid values: Float. Range: [0.0, 1.0].<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                                                               |
| `max_bin`                | Maximum number of discrete bins to bucket continuous<br>features. Used only if `tree_method` is set to<br>`hist`.<br>**Optional**<br>Valid values: integer<br>Default value: 256                                                                                                                                                                                                                                                                                                                                             |
| `max_delta_step`         | Maximum delta step allowed for each tree's weight<br>estimation. When a positive integer is used, it helps make the<br>update more conservative. The preferred option is to use it in<br>logistic regression. Set it to 1-10 to help control the update.<br>**Optional**<br>Valid values: Integer. Range: [0,∞).<br>Default value: 0                                                                                                                                                                                         |
| `max_depth`              | Maximum depth of a tree. Increasing this value makes the<br>model more complex and likely to be overfit. 0 indicates no<br>limit. A limit is required when<br>`grow_policy`=`depth-wise`.<br>**Optional**<br>Valid values: Integer. Range: [0,∞)<br>Default value: 6                                                                                                                                                                                                                                                         |
| `max_leaves`             | Maximum number of nodes to be added. Relevant only if<br>`grow_policy` is set to<br>`lossguide`.<br>**Optional**<br>Valid values: integer<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                |
| `min_child_weight`       | Minimum sum of instance weight (hessian) needed in a child.<br>If the tree partition step results in a leaf node with the sum<br>of instance weight less than `min_child_weight`, the<br>building process gives up further partitioning. In linear<br>regression models, this simply corresponds to a minimum number<br>of instances needed in each node. The larger the algorithm, the<br>more conservative it is.<br>**Optional**<br>Valid values: Float. Range: [0,∞).<br>Default value: 1                                |
| `normalize_type`         | Type of normalization algorithm.<br>**Optional**<br>Valid values: Either *tree<br>• or<br>*forest*.<br>Default value: *tree\*                                                                                                                                                                                                                                                                                                                                                                                                |
| `nthread`                | Number of parallel threads used to run<br>_xgboost_.<br>**Optional**<br>Valid values: integer<br>Default value: Maximum number of threads.                                                                                                                                                                                                                                                                                                                                                                                   |
| `objective`              | Specifies the learning task and the corresponding learning<br>objective. Examples: `reg:logistic`,<br>`reg:softmax`, `multi:squarederror`.<br>For a full list of valid inputs, refer to [XGBoost Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters "https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters").<br>**Optional**<br>Valid values: string<br>Default value: `reg:squarederror`                                                  |
| `one_drop`               | When this flag is enabled, at least one tree is always<br>dropped during the dropout.<br>**Optional**<br>Valid values: 0 or 1<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                            |
| `process_type`           | The type of boosting process to run.<br>**Optional**<br>Valid values: String. Either `default` or<br>`update`.<br>Default value: `default`                                                                                                                                                                                                                                                                                                                                                                                   |
| `rate_drop`              | The dropout rate that specifies the fraction of previous<br>trees to drop during the dropout.<br>**Optional**<br>Valid values: Float. Range: [0.0, 1.0].<br>Default value: 0.0                                                                                                                                                                                                                                                                                                                                               |
| `refresh_leaf`           | This is a parameter of the 'refresh' updater plug-in. When<br>set to `true` (1), tree leaves and tree node stats<br>are updated. When set to `false`(0), only tree node<br>stats are updated.<br>**Optional**<br>Valid values:<br>0/1<br>Default value: 1                                                                                                                                                                                                                                                                    |
| `sample_type`            | Type of sampling algorithm.<br>**Optional**<br>Valid values: Either `uniform` or<br>`weighted`.<br>Default value: `uniform`                                                                                                                                                                                                                                                                                                                                                                                                  |
| `scale_pos_weight`       | Controls the balance of positive and negative weights. It's<br>useful for unbalanced classes. A typical value to consider:<br>`sum(negative cases)` / `sum(positive<br>cases)`.<br>**Optional**<br>Valid values: float<br>Default value: 1                                                                                                                                                                                                                                                                                   |
| `seed`                   | Random number seed.<br>**Optional**<br>Valid values: integer<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `silent`                 | 0 means print running messages, 1 means silent mode.<br>Valid values: 0 or 1<br>**Optional**<br>Default value: 0                                                                                                                                                                                                                                                                                                                                                                                                             |
| `sketch_eps`             | Used only for approximate greedy algorithm. This translates<br>into O(1 / `sketch_eps`) number of bins. Compared to<br>directly select number of bins, this comes with theoretical<br>guarantee with sketch accuracy.<br>**Optional**<br>Valid values: Float, Range: [0, 1].<br>Default value: 0.03                                                                                                                                                                                                                          |
| `skip_drop`              | Probability of skipping the dropout procedure during a<br>boosting iteration.<br>**Optional**<br>Valid values: Float. Range: [0.0, 1.0].<br>Default value: 0.0                                                                                                                                                                                                                                                                                                                                                               |
| `subsample`              | Subsample ratio of the training instance. Setting it to 0.5<br>means that XGBoost randomly collects half of the data instances<br>to grow trees. This prevents overfitting.<br>**Optional**<br>Valid values: Float. Range: [0,1].<br>Default value: 1                                                                                                                                                                                                                                                                        |
| `tree_method`            | The tree construction algorithm used in XGBoost.<br>**Optional**<br>Valid values: One of `auto`, `exact`,<br>`approx`, or `hist`.<br>Default value: `auto`                                                                                                                                                                                                                                                                                                                                                                   |
| `tweedie_variance_power` | Parameter that controls the variance of the Tweedie<br>distribution.<br>**Optional**<br>Valid values: Float. Range: (1, 2).<br>Default value: 1.5                                                                                                                                                                                                                                                                                                                                                                            |
| `updater`                | A comma-separated string that defines the sequence of tree<br>updaters to run. This provides a modular way to construct and to<br>modify the trees.<br>For a full list of valid inputs, please refer to [XGBoost Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst "https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst").<br>**Optional**<br>Valid values: comma-separated string.<br>Default value: `grow_colmaker`, prune                                                               |

## Tune an XGBoost Release 0.72 Model

_Automatic model tuning_, also known as
hyperparameter tuning, finds the best version of a model by running many jobs that
test a range of hyperparameters on your training and validation datasets. You choose
three types of hyperparameters:

- a learning `objective` function to optimize during model
  training
- an `eval_metric` to use to evaluate model performance during
  validation
- a set of hyperparameters and a range of values for each to use when tuning
  the model automatically

You choose the evaluation metric from set of evaluation metrics that the algorithm
computes. Automatic model tuning searches the hyperparameters chosen to find the
combination of values that result in the model that optimizes the evaluation metric.

For more information about model tuning, see [Automatic model tuning with SageMaker AI](automatic-model-tuning.md "automatic-model-tuning.md").

### Metrics Computed by the XGBoost Release

0.72 Algorithm

The XGBoost algorithm based on version 0.72 computes the following nine
metrics to use for model validation. When tuning the model, choose one of these
metrics to evaluate the model. For full list of valid `eval_metric`
values, refer to [XGBoost Learning Task Parameters](https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters "https://github.com/dmlc/xgboost/blob/master/doc/parameter.rst#learning-task-parameters")

| Metric Name           | Description                                                                         | Optimization Direction |
| --------------------- | ----------------------------------------------------------------------------------- | ---------------------- |
| `validation:auc`      | Area under the curve.                                                               | Maximize               |
| `validation:error`    | Binary classification error rate, calculated as #(wrong<br>cases)/#(all cases).     | Minimize               |
| `validation:logloss`  | Negative log-likelihood.                                                            | Minimize               |
| `validation:mae`      | Mean absolute error.                                                                | Minimize               |
| `validation:map`      | Mean average precision.                                                             | Maximize               |
| `validation:merror`   | Multiclass classification error rate, calculated as<br>#(wrong cases)/#(all cases). | Minimize               |
| `validation:mlogloss` | Negative log-likelihood for multiclass<br>classification.                           | Minimize               |
| `validation:ndcg`     | Normalized Discounted Cumulative Gain.                                              | Maximize               |
| `validation:rmse`     | Root mean square error.                                                             | Minimize               |

### Tunable XGBoost Release

0.72 Hyperparameters

Tune the XGBoost model with the following hyperparameters. The hyperparameters
that have the greatest effect on optimizing the XGBoost evaluation metrics are:
`alpha`, `min_child_weight`, `subsample`,
`eta`, and `num_round`.

| Parameter Name      | Parameter Type            | Recommended Ranges           |
| ------------------- | ------------------------- | ---------------------------- |
| `alpha`             | ContinuousParameterRanges | MinValue: 0, MaxValue: 1000  |
| `colsample_bylevel` | ContinuousParameterRanges | MinValue: 0.1, MaxValue: 1   |
| `colsample_bytree`  | ContinuousParameterRanges | MinValue: 0.5, MaxValue: 1   |
| `eta`               | ContinuousParameterRanges | MinValue: 0.1, MaxValue: 0.5 |
| `gamma`             | ContinuousParameterRanges | MinValue: 0, MaxValue: 5     |
| `lambda`            | ContinuousParameterRanges | MinValue: 0, MaxValue: 1000  |
| `max_delta_step`    | IntegerParameterRanges    | [0, 10]                      |
| `max_depth`         | IntegerParameterRanges    | [0, 10]                      |
| `min_child_weight`  | ContinuousParameterRanges | MinValue: 0, MaxValue: 120   |
| `num_round`         | IntegerParameterRanges    | [1, 4000]                    |
| `subsample`         | ContinuousParameterRanges | MinValue: 0.5, MaxValue: 1   |
