Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW MODEL

Shows useful information about a machine learning model, including its status, the
parameters used to create it and the prediction function with its input argument types. You
can use the information from the SHOW MODEL to recreate the model. If base tables have
changed, running CREATE MODEL with the same SQL statement results in a different model. The
information returned by the SHOW MODEL is different for the model owner and a user with the
EXECUTE privilege. SHOW MODEL shows different outputs when a model is trained from Amazon Redshift
or when the model is a BYOM model.

## Syntax

```
SHOW MODEL ( ALL | `model_name` )
```

## Parameters

ALL

Returns all the models that the user can use and their schemas.

_model_name_

The name of the model. The model name in a schema must be unique.

## Usage notes

The SHOW MODEL command returns the following:

- The model name.
- The schema where the model was created.
- The owner of the model.
- The model creation time.
- The status of the model, such as READY, TRAINING, or FAILED.
- The reason message for a failed model.
- The validation error if model has finished training.
- The estimated cost needed to derive the model for a non-BYOM approach. Only the
  owner of the model can view this information.
- A list of user-specified parameters and their values, specifically the
  following:
  - The specified TARGET column.
  - The model type, AUTO or XGBoost.
  - The problem type, such as REGRESSION, BINARY_CLASSIFICATION,
    MULTICLASS_CLASSIFICATION. This parameter is specific to AUTO.
  - The name of the Amazon SageMaker AI training job or the Amazon SageMaker AI Autopilot job that
    created the model. You can use this job name to find more information about
    the model on Amazon SageMaker AI.
  - The objective, such as MSE, F1, Accuracy. This parameter is specific to
    AUTO.
  - The name of the created function.
  - The type of inference, local or remote.
  - The prediction function input arguments.
  - The prediction function input argument types for models that aren't bring
    your own model (BYOM).
  - The return type of the prediction function. This parameter is specific to
    BYOM.
  - The name of the Amazon SageMaker AI endpoint for a BYOM model with remote
    inference.
  - The IAM role. Only the owner of the model can see this.
  - The S3 bucket used. Only the owner of the model can see this.
  - The AWS KMS key, if one was provided. Only the owner of the model can see
    this.
  - The maximum time that the model can run.

- If the model type is not AUTO, then Amazon Redshift also shows the list of
  hyperparameters provided and their values.

You can also view some of the information provided by SHOW MODEL in other catalog
tables, such as pg_proc. Amazon Redshift returns information about the prediction function that
is registered in pg_proc catalog table. This information includes the input argument
names and their types for the prediction function. Amazon Redshift returns the same information
in the SHOW MODEL command.

```
SELECT * FROM pg_proc WHERE proname ILIKE '%<function_name>%';
```

## Examples

The following example shows the show model output.

```
SHOW MODEL ALL;

Schema Name |  Model Name
------------+---------------
 public     | customer_churn
```

The owner of the customer_churn can see the following output. A user with only the
EXECUTE privilege can't see the IAM role, the Amazon S3 bucket, and the estimated cost
of the mode.

```
SHOW MODEL customer_churn;

       Key                 |           Value
---------------------------+-----------------------------------
 Model Name                | customer_churn
 Schema Name               | public
 Owner                     | 'owner'
 Creation Time             | Sat, 15.01.2000 14:45:20
 Model State               | READY
 validation:F1             | 0.855
 Estimated Cost            | 5.7
                           |
 TRAINING DATA:            |
 Table                     | customer_data
 Target Column             | CHURN
                           |
 PARAMETERS:               |
 Model Type                | auto
 Problem Type              | binary_classification
 Objective                 | f1
 Function Name             | predict_churn
 Function Parameters       | age zip average_daily_spend average_daily_cases
 Function Parameter Types  | int int float float
 IAM Role                  | 'iam_role'
 KMS Key                   | 'kms_key'
 Max Runtime               | 36000
```
