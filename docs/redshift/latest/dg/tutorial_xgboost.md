Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Tutorial: Building XGBoost models

In this tutorial, you create a model with data from Amazon S3 and run prediction
queries with the model using Amazon Redshift ML. The XGBoost algorithm is an optimized
implementation of the gradient boosted trees algorithm. XGBoost handles more data
types, relationships, and distributions than other gradient boosted trees algorithms.
You can use XGBoost for regression, binary classification, multi-class
classification, and ranking problems. For more information about the XGBoost
algorithm, see [XGBoost
algorithm](../../../sagemaker/latest/dg/xgboost.md "../../../sagemaker/latest/dg/xgboost.md") in the Amazon SageMaker AI Developer Guide.

The Amazon Redshift ML `CREATE MODEL` operation with the `AUTO OFF`
option currently supports XGBoost as the `MODEL_TYPE`. You can provide
relevant information such as the objective and hyperparameters as part of the
`CREATE MODEL` command, based on your use case.

In this tutorial, you use the [banknote
authentication dataset](https://archive.ics.uci.edu/ml/datasets/banknote+authentication "https://archive.ics.uci.edu/ml/datasets/banknote+authentication"), which is a binary classification problem to
predict whether a given banknote is genuine or forged.

## Use case examples

You can solve other binary classification problems using Amazon Redshift ML, such as predicting whether
a patient is healthy or has a disease. You could also predict whether an email is spam or not spam.

**Tasks**

- Prerequisites
- Step 1: Load the data from Amazon S3 to Amazon Redshift
- Step 2: Create the machine learning model
- Step 3: Perform predictions with the model

## Prerequisites

To complete this tutorial, you must complete the
[Administrative setup](admin-setup.md "admin-setup.md") for Amazon Redshift ML.

## Step 1: Load the data from Amazon S3 to Amazon Redshift

Use the [Amazon Redshift query editor v2](../mgmt/query-editor-v2-using.md "../mgmt/query-editor-v2-using.md") to run the following queries.

The following query creates two tables, loads the data from Amazon S3, and splits
the data into a training set and a testing set. You will use the training set to
train your model and create the prediction function. Then, you will test the
prediction function on the testing set.

```
--create training set table
CREATE TABLE banknoteauthentication_train(
    variance FLOAT,
    skewness FLOAT,
    curtosis FLOAT,
    entropy FLOAT,
    class INT
);

--Load into training table
COPY banknoteauthentication_train
FROM
    's3://redshiftbucket-ml-sagemaker/banknote_authentication/train_data/' IAM_ROLE default REGION 'us-west-2' IGNOREHEADER 1 CSV;

--create testing set table
CREATE TABLE banknoteauthentication_test(
    variance FLOAT,
    skewness FLOAT,
    curtosis FLOAT,
    entropy FLOAT,
    class INT
);

--Load data into testing table
COPY banknoteauthentication_test
FROM
    's3://redshiftbucket-ml-sagemaker/banknote_authentication/test_data/'
    IAM_ROLE default
    REGION 'us-west-2'
    IGNOREHEADER 1
    CSV;
```

## Step 2: Create the machine learning model

The following query creates the XGBoost model in Amazon Redshift ML from the training set
you created in the previous step. Replace `amzn-s3-demo-bucket` with
your own `S3_BUCKET`, which will store your input datasets and other
Redshift ML artifacts.

```
CREATE MODEL model_banknoteauthentication_xgboost_binary
FROM
    banknoteauthentication_train
    TARGET class
    FUNCTION func_model_banknoteauthentication_xgboost_binary
    IAM_ROLE default
    AUTO OFF
    MODEL_TYPE xgboost
    OBJECTIVE 'binary:logistic'
    PREPROCESSORS 'none'
    HYPERPARAMETERS DEFAULT
EXCEPT(NUM_ROUND '100')
SETTINGS(S3_BUCKET 'amzn-s3-demo-bucket');
```

### Show the status of model training (optional)

You can use the SHOW MODEL command to know when your model is ready.

Use the following query to monitor the progress of the model
training.

```
SHOW MODEL model_banknoteauthentication_xgboost_binary;
```

If the model is `READY`, the SHOW MODEL operation also provides
the `train:error` metric, as shown in the following example of the
output. The `train:error` metric is a measure of accuracy of your
model that measures to six decimal places. A value of 0 is most accurate and a
value of 1 is least accurate.

```
+--------------------------+--------------------------------------------------+
|        Model Name        |   model_banknoteauthentication_xgboost_binary    |
+--------------------------+--------------------------------------------------+
| Schema Name              | public                                           |
| Owner                    | awsuser                                          |
| Creation Time            | Tue, 21.06.2022 19:07:35                         |
| Model State              | READY                                            |
| train:error              |                                         0.000000 |
| Estimated Cost           |                                         0.006197 |
|                          |                                                  |
| TRAINING DATA:           |                                                  |
| Query                    | SELECT *                                         |
|                          | FROM "BANKNOTEAUTHENTICATION_TRAIN"              |
| Target Column            | CLASS                                            |
|                          |                                                  |
| PARAMETERS:              |                                                  |
| Model Type               | xgboost                                          |
| Training Job Name        | redshiftml-20220621190735686935-xgboost          |
| Function Name            | func_model_banknoteauthentication_xgboost_binary |
| Function Parameters      | variance skewness curtosis entropy               |
| Function Parameter Types | float8 float8 float8 float8                      |
| IAM Role                 | default-aws-iam-role                             |
| S3 Bucket                | amzn-s3-demo-bucket                              |
| Max Runtime              |                                             5400 |
|                          |                                                  |
| HYPERPARAMETERS:         |                                                  |
| num_round                |                                              100 |
| objective                | binary:logistic                                  |
+--------------------------+--------------------------------------------------+

```

## Step 3: Perform predictions with the model

### Check the accuracy of the model

The following prediction query uses the prediction function created in the
previous step to check the accuracy of your model. Run this query on the
testing set to make sure the model does not correspond too closely to the
training set. This close correspondence is also known as overfitting, and
overfitting could cause the model to make unreliable predictions.

```
WITH predict_data AS (
    SELECT
        class AS label,
        func_model_banknoteauthentication_xgboost_binary (variance, skewness, curtosis, entropy) AS predicted,
        CASE
            WHEN label IS NULL THEN 0
            ELSE label
        END AS actual,
        CASE
            WHEN actual = predicted THEN 1 :: INT
            ELSE 0 :: INT
        END AS correct
    FROM
        banknoteauthentication_test
),
aggr_data AS (
    SELECT
        SUM(correct) AS num_correct,
        COUNT(*) AS total
    FROM
        predict_data
)
SELECT
    (num_correct :: FLOAT / total :: FLOAT) AS accuracy
FROM
    aggr_data;
```

### Predict the amount of original and counterfeit banknotes

The following prediction query returns the predicted amount of original and
counterfeit banknotes in the testing set.

```
WITH predict_data AS (
    SELECT
        func_model_banknoteauthentication_xgboost_binary(variance, skewness, curtosis, entropy) AS predicted
    FROM
        banknoteauthentication_test
)
SELECT
    CASE
        WHEN predicted = '0' THEN 'Original banknote'
        WHEN predicted = '1' THEN 'Counterfeit banknote'
        ELSE 'NA'
    END AS banknote_authentication,
    COUNT(1) AS count
FROM
    predict_data
GROUP BY
    1;
```

### Find the average observation for an original and a counterfeit

banknote

The following prediction query returns the average value of each feature for
banknotes that are predicted to be original and counterfeit in the testing
set.

```
WITH predict_data AS (
    SELECT
        func_model_banknoteauthentication_xgboost_binary(variance, skewness, curtosis, entropy) AS predicted,
          variance,
          skewness,
          curtosis,
          entropy
    FROM
        banknoteauthentication_test
)
SELECT
    CASE
        WHEN predicted = '0' THEN 'Original banknote'
        WHEN predicted = '1' THEN 'Counterfeit banknote'
        ELSE 'NA'
    END AS banknote_authentication,
    TRUNC(AVG(variance), 2) AS avg_variance,
    TRUNC(AVG(skewness), 2) AS avg_skewness,
    TRUNC(AVG(curtosis), 2) AS avg_curtosis,
    TRUNC(AVG(entropy), 2) AS avg_entropy
FROM
    predict_data
GROUP BY
    1
ORDER BY
    2;
```

## Related topics

For more information about Amazon Redshift ML, see the following documentation:

- [Costs for using Amazon Redshift ML](cost.md "cost.md")
- [CREATE MODEL operation](r_CREATE_MODEL.md "r_CREATE_MODEL.md")
- [EXPLAIN_MODEL function](r_explain_model_function.md "r_explain_model_function.md")

For more information about machine learning, see the following documentation:

- [Machine learning overview](machine_learning_overview.md "machine_learning_overview.md")
- [Machine learning for novices and experts](novice_expert.md "novice_expert.md")
- [What Is Fairness and Model Explainability for Machine Learning
  Predictions?](../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md "../../../sagemaker/latest/dg/clarify-fairness-and-explainability.md")
