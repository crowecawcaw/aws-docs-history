Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# DROP MODEL

Removes a model from the database. Only the model owner or a superuser can drop a model.

DROP MODEL also deletes all the associated prediction function that is derived from this
model, all Amazon Redshift artifacts related to the model, and all Amazon S3 data related to the model.
While the model is still being trained in Amazon SageMaker AI, DROP MODEL will cancel those
operations.

This command isn't reversible. The DROP MODEL command commits immediately.

## Required permissions

Following are required permissions for DROP MODEL:

- Superuser
- Users with the DROP MODEL permission
- Model owner
- Schema owner

## Syntax

```
DROP MODEL [ IF EXISTS ] *model\_name*
```

## Parameters

_IF EXISTS_

A clause that indicates that if the specified schema already exists, the
command should make no changes and return a message that the schema
exists.

_model\_name_

The name of the model. The model name in a schema must be unique.

## Examples

The following example drops the model demo\_ml.customer\_churn.

```
DROP MODEL demo_ml.customer_churn

```
