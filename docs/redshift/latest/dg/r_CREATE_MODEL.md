Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE MODEL

###### Topics

- [Prerequisites](#r_create_model_prereqs "#r_create_model_prereqs")
- [Required privileges](#r_simple_create_model-privileges "#r_simple_create_model-privileges")
- [Cost control](#r_create_model_cost "#r_create_model_cost")
- [Full CREATE MODEL](#r_full_create_model "#r_full_create_model")
- [Parameters](#r_create_model_parameters "#r_create_model_parameters")
- [Usage notes](r_create_model_usage_notes.md "r_create_model_usage_notes.md")
- [Use cases](r_create_model_use_cases.md "r_create_model_use_cases.md")

## Prerequisites

Before you use the CREATE MODEL statement, complete the prerequisites in [Cluster setup for using Amazon Redshift ML](getting-started-machine-learning.md#cluster-setup "getting-started-machine-learning.md#cluster-setup"). The following is a
high-level summary of the prerequisites.

- Create an Amazon Redshift cluster with the AWS Management Console or the AWS
  Command Line Interface (AWS CLI).
- Attach the AWS Identity and Access Management (IAM) policy while creating the
  cluster.
- To allow Amazon Redshift and SageMaker AI to assume the role to interact with other services,
  add the appropriate trust policy to the IAM role.

For details for the IAM role, trust policy, and other prerequisites, see [Cluster setup for using Amazon Redshift ML](getting-started-machine-learning.md#cluster-setup "getting-started-machine-learning.md#cluster-setup").

Following, you can find different use cases for the CREATE MODEL statement.

- [Simple CREATE MODEL](r_create_model_use_cases.md#r_simple_create_model "r_create_model_use_cases.md#r_simple_create_model")
- [CREATE MODEL with user
  guidance](r_create_model_use_cases.md#r_user_guidance_create_model "r_create_model_use_cases.md#r_user_guidance_create_model")
- [CREATE XGBoost models with AUTO OFF](r_create_model_use_cases.md#r_auto_off_create_model "r_create_model_use_cases.md#r_auto_off_create_model")
- [Bring your own model (BYOM) - local
  inference](r_create_model_use_cases.md#r_byom_create_model "r_create_model_use_cases.md#r_byom_create_model")
- [Bring your own model (BYOM) - remote
  inference](r_create_model_use_cases.md#r_byom_create_model_remote "r_create_model_use_cases.md#r_byom_create_model_remote")
- [CREATE MODEL with K-MEANS](r_create_model_use_cases.md#r_k-means_create_model "r_create_model_use_cases.md#r_k-means_create_model")
- [Full CREATE MODEL](#r_full_create_model "#r_full_create_model")

## Required privileges

Following are required privileges for CREATE MODEL:

- Superuser
- Users with the CREATE MODEL privilege
- Roles with the GRANT CREATE MODEL privilege

## Cost control

Amazon Redshift ML uses existing cluster resources to create prediction models, so you
don’t have to pay additional costs. However, you might have additional costs if you need
to resize your cluster or want to train your models. Amazon Redshift ML uses Amazon SageMaker AI to train
models, which does have an additional associated cost. There are ways to control
additional costs, such as limiting the maximum amount of time training can take or by
limiting the number of training examples used to train your model. For more information,
see [Costs for using
Amazon Redshift ML](cost.md "cost.md").

## Full CREATE MODEL

The following summarizes the basic options of the full CREATE MODEL syntax.

### Full CREATE MODEL syntax

The following is the full syntax of the CREATE MODEL statement.

###### Important

When creating a model using the CREATE MODEL statement, follow the order of the
keywords in the syntax following.

```
CREATE MODEL model_name
FROM { table_name | ( select_statement )  | 'job_name' }
[ TARGET column_name ]
FUNCTION function_name [ ( data_type [, ...] ) ]
[ RETURNS data_type ]
  -- supported only for BYOM
[ SAGEMAKER 'endpoint_name'[:'model_name']]
  -- supported only for BYOM remote inference
IAM_ROLE { default | 'arn:aws:iam::<account-id>:role/<role-name>' }
[ AUTO ON / OFF ]
  -- default is AUTO ON
[ MODEL_TYPE { XGBOOST | MLP | LINEAR_LEARNER | KMEANS | FORECAST } ]
  -- not required for non AUTO OFF case, default is the list of all supported types
  -- required for AUTO OFF
[ PROBLEM_TYPE ( REGRESSION | BINARY_CLASSIFICATION | MULTICLASS_CLASSIFICATION ) ]
  -- not supported when AUTO OFF
[ OBJECTIVE ( 'MSE' | 'Accuracy' | 'F1' | 'F1_Macro' | 'AUC' |
             'reg:squarederror' | 'reg:squaredlogerror'| 'reg:logistic'|
             'reg:pseudohubererror' | 'reg:tweedie' | 'binary:logistic' | 'binary:hinge',
             'multi:softmax' | 'RMSE' | 'WAPE' | 'MAPE' | 'MASE' | 'AverageWeightedQuantileLoss' ) ]
  -- for AUTO ON: first 5 are valid
  -- for AUTO OFF: 6-13 are valid
  -- for FORECAST: 14-18 are valid
[ PREPROCESSORS 'string' ]
  -- required for AUTO OFF, when it has to be 'none'
  -- optional for AUTO ON
[ HYPERPARAMETERS { DEFAULT | DEFAULT EXCEPT ( Key 'value' (,...) ) } ]
  -- support XGBoost hyperparameters, except OBJECTIVE
  -- required and only allowed for AUTO OFF
  -- default NUM_ROUND is 100
  -- NUM_CLASS is required if objective is multi:softmax (only possible for AUTO OFF)
 [ SETTINGS (
   S3_BUCKET 'amzn-s3-demo-bucket',  |
    -- required
  TAGS 'string', |
    -- optional
  KMS_KEY_ID 'kms_string', |
    -- optional
  S3_GARBAGE_COLLECT on / off, |
    -- optional, defualt is on.
  MAX_CELLS integer, |
    -- optional, default is 1,000,000
  MAX_RUNTIME integer (, ...) |
    -- optional, default is 5400 (1.5 hours)
  HORIZON integer, |
    -- required if creating a forecast model
  FREQUENCY integer, |
    -- required if creating a forecast model
  PERCENTILES string, |
    -- optional if creating a forecast model
  MAX_BATCH_ROWS integer -- optional for BYOM remote inference
    ) ]
```

## Parameters

model_name

The name of the model. The model name in a schema must be unique.

FROM { _table_name_ | ( _select_query_ )
| _'job_name'_}

The table_name or the query that specifies the training data. They can
either be an existing table in the system, or an Amazon Redshift-compatible SELECT
query enclosed with parentheses, that is (). There must be at least two columns
in the query result.

TARGET _column_name_

The name of the column that becomes the prediction target. The column must
exist in the FROM clause.

FUNCTION _function_name_ ( _data_type_ [,
...] )

The name of the function to be created and the data types of the input
arguments. You can provide the schema name of a schema in your database instead
of a function name.

RETURNS _data_type_

The data type to be returned from the model's function. The returned
`SUPER` data type is applicable only to BYOM with remote
inference.

SAGEMAKER
'_endpoint_name_'[:'*model\_name*']

The name of the Amazon SageMaker AI endpoint. If the endpoint name points to a
multimodel endpoint, add the name of the model to use. The endpoint must be
hosted in the same AWS Region as the Amazon Redshift cluster.

IAM_ROLE { default | 'arn:aws:iam::<account-id>:role/<role-name>'
}

Use the default keyword to have Amazon Redshift use the IAM
role that is set as default and associated with the cluster when the CREATE
MODEL command runs. Alternatively, you can specify an ARN of an IAM role to
use that role.

[ AUTO ON / OFF ]

Turns on or off CREATE MODEL automatic discovery of preprocessor,
algorithm, and hyper-parameters selection. Specifying on when creating a
Forecast model indicates to use an AutoPredictor, where Amazon Forecast applies the
optimal combinations of algorithms to each time series in your dataset.

_MODEL_TYPE { XGBOOST | MLP | LINEAR_LEARNER | KMEANS | FORECAST
}_

(Optional) Specifies the model type. You can specify if you want to train a
model of a specific model type, such as XGBoost, multilayer perceptron (MLP),
KMEANS, or Linear Learner, which are all algorithms that Amazon SageMaker AI Autopilot
supports. If you don't specify the parameter, then all supported model
types are searched during training for the best model. You can also create a
forecast model in Redshift ML to create accurate time-series forecasts.

_PROBLEM_TYPE ( REGRESSION | BINARY_CLASSIFICATION |
MULTICLASS_CLASSIFICATION )_

(Optional) Specifies the problem type. If you know the problem type, you can
restrict Amazon Redshift to only search of the best model of that specific model type.
If you don't specify this parameter, a problem type is discovered during
the training, based on your data.

OBJECTIVE ( 'MSE' | 'Accuracy' | 'F1' | 'F1Macro' | 'AUC' | 'reg:squarederror'
| 'reg:squaredlogerror' | 'reg:logistic' | 'reg:pseudohubererror' | 'reg:tweedie'
| 'binary:logistic' | 'binary:hinge' | 'multi:softmax' | 'RMSE' | 'WAPE' | 'MAPE'
| 'MASE' | 'AverageWeightedQuantileLoss' )

(Optional) Specifies the name of the objective metric used to measure the
predictive quality of a machine learning system. This metric is optimized
during training to provide the best estimate for model parameter values from
data. If you don't specify a metric explicitly, the default behavior is to
automatically use MSE: for regression, F1: for binary classification, Accuracy:
for multiclass classification. For more information about objectives, see
[AutoMLJobObjective](../../../sagemaker/latest/APIReference/API_AutoMLJobObjective.md "../../../sagemaker/latest/APIReference/API_AutoMLJobObjective.md") in the _Amazon SageMaker AI API Reference_ and
[Learning task parameters](https://xgboost.readthedocs.io/en/latest/parameter.html#learning-task-parameters "https://xgboost.readthedocs.io/en/latest/parameter.html#learning-task-parameters")in the XGBOOST documentation. The values
RMSE, WAPE, MAPE, MASE, and AverageWeightedQuantileLoss are only applicable to
Forecast models. For more information, see the [CreateAutoPredictor](../../../forecast/latest/dg/API_CreateAutoPredictor.md#forecast-CreateAutoPredictor-request-OptimizationMetric "../../../forecast/latest/dg/API_CreateAutoPredictor.md#forecast-CreateAutoPredictor-request-OptimizationMetric") API operation.

_PREPROCESSORS 'string'_

(Optional) Specifies certain combinations of preprocessors to certain sets
of columns. The format is a list of columnSets, and the appropriate transforms
to be applied to each set of columns. Amazon Redshift applies all the transformers in
a specific transformers list to all columns in the corresponding ColumnSet. For
example, to apply OneHotEncoder with Imputer to columns t1 and t2, use the
sample command following.

```
CREATE MODEL customer_churn
FROM customer_data
TARGET 'Churn'
FUNCTION predict_churn
IAM_ROLE { default | 'arn:aws:iam::<account-id>:role/<role-name>' }
PROBLEM_TYPE BINARY_CLASSIFICATION
OBJECTIVE 'F1'
PREPROCESSORS '[
...
  {"ColumnSet": [
      "t1",
      "t2"
    ],
    "Transformers": [
      "OneHotEncoder",
      "Imputer"
    ]
  },
  {"ColumnSet": [
      "t3"
    ],
    "Transformers": [
      "OneHotEncoder"
    ]
  },
  {"ColumnSet": [
      "temp"
    ],
    "Transformers": [
      "Imputer",
      "NumericPassthrough"
    ]
  }
]'
SETTINGS (
  S3_BUCKET 'amzn-s3-demo-bucket'
)
```

HYPERPARAMETERS { DEFAULT | DEFAULT EXCEPT ( key ‘value’ (,..) ) }

Specifies whether the default XGBoost parameters are used or overridden by
user-specified values. The values must be enclosed with single quotes.
Following are examples of parameters for XGBoost and their defaults.

| Parameter name   | Parameter value | Default value                           | Notes                        |
| ---------------- | --------------- | --------------------------------------- | ---------------------------- |
| num_class        | Integer         | Required for Multiclass classification. | N/A                          |
| num_round        | Integer         | 100                                     | N/A                          |
| tree_method      | String          | Auto                                    | N/A                          |
| max_depth        | Integer         | 6                                       | [0 , 10]                     |
| min_child_weight | Float           | 1                                       | MinValue: 0, MaxValue: 120   |
| subsample        | Float           | 1                                       | MinValue: 0.5, MaxValue: 1   |
| gamma            | Float           | 0                                       | MinValue: 0, MaxValue: 5     |
| alpha            | Float           | 0                                       | MinValue: 0, MaxValue: 1000  |
| eta              | Float           | 0.3                                     | MinValue: 0.1, MaxValue: 0.5 |
| colsample_byleve | Float           | 1                                       | MinValue: 0.1, MaxValue: 1   |
| colsample_bynode | Float           | 1                                       | MinValue: 0.1, MaxValue: 1   |
| colsample_bytree | Float           | 1                                       | MinValue: 0.5, MaxValue: 1   |
| lambda           | Float           | 1                                       | MinValue: 0, MaxValue: 1000  |
| max_delta_step   | Integer         | 0                                       | [0, 10]                      |

SETTINGS ( S3_BUCKET _'amzn-s3-demo-bucket'_, | TAGS
'string', | KMS_KEY_ID _'kms_string'_ , | S3_GARBAGE_COLLECT on
/ off, | MAX_CELLS integer , | MAX_RUNTIME (,...) , | HORIZON integer, | FREQUENCY
forecast_frequency, | PERCENTILES array of strings )

S3_BUCKET clause specifies the Amazon S3 location that is used to store
intermediate results.

(Optional) The TAGS parameter is a comma-separated list of key-value pairs
that you can use to tag resources created in Amazon SageMaker AI; and Amazon Forecast. Tags help
you organize resources and allocate costs. Values in the pair are optional, so
you can create tags by using the format `key=value` or just by
creating a key. For more information about tags in Amazon Redshift, see [Tagging overview](../mgmt/amazon-redshift-tagging.md "../mgmt/amazon-redshift-tagging.md").

(Optional) KMS_KEY_ID specifies if Amazon Redshift uses server-side encryption with
an AWS KMS key to protect data at rest. Data in transit is protected with Secure
Sockets Layer (SSL).

(Optional) S3_GARBAGE_COLLECT { ON | OFF } specifies whether Amazon Redshift
performs garbage collection on the resulting datasets used to train models and
the models. If set to OFF, the resulting datasets used to train models and the
models remains in Amazon S3 and can be used for other purposes. If set to ON,
Amazon Redshift deletes the artifacts in Amazon S3 after the training completes. The
default is ON.

(Optional) MAX_CELLS specifies the number of cells in the training data.
This value is the product of the number of records (in the training query or
table) times the number of columns. The default is 1,000,000.

(Optional) MAX_RUNTIME specifies the maximum amount of time to train.
Training jobs often complete sooner depending on dataset size. This specifies
the maximum amount of time the training should take. The default is 5,400 (90
minutes).

HORIZON specifies the maximum number of predictions the forecast model can
return. Once the model is trained, you can't change this integer. This
parameter is required if training a forecast model.

FREQUENCY specifies how granular in time units you want the forecasts to be.
Available options are `Y | M | W | D | H | 30min | 15min | 10min | 5min |
 1min`. This parameter is required if training a forecast model.

(Optional) PERCENTILES is a comma-delimited string that specifies the
forecast types used to train a predictor. Forecast types can be quantiles from
0.01 to 0.99, in increments of 0.01 or higher. You can also specify the mean
forecast with mean. You can specify a maximum of five forecast types.

MAX_BATCH_ROWS _integer_

(Optional) The maximum number of rows that Amazon Redshift sends in a single batch
request for a single SageMaker AI invocation. It is supported only for BYOM with remote
inference. This parameter's minimum value is 1. The maximum value is
`INT_MAX`, or 2,147,483,647. This parameter is required only when
both input and returned data types are _SUPER_. The default
value is `INT_MAX`, or 2,147,483,647.
