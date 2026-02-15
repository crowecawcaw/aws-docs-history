# Use ML with Athena syntax

The `USING EXTERNAL FUNCTION` clause specifies an ML with Athena function or
multiple functions that can be referenced by a subsequent `SELECT` statement
in the query. You define the function name, variable names, and data types for the
variables and return values.

## Synopsis

The following syntax shows a `USING EXTERNAL FUNCTION` clause that
specifies an ML with Athena function.

```
USING EXTERNAL FUNCTION `ml_function_name` (`variable1` `data_type`[, `variable2` `data_type`][,...])
RETURNS `data_type`
SAGEMAKER '`sagemaker_endpoint`'
SELECT `ml_function_name`()
```

## Parameters

**USING EXTERNAL FUNCTION `ml_function_name`
(`variable1`
`data_type`[, `variable2`
`data_type`][,...])**

`ml_function_name` defines the function name,
which can be used in subsequent query clauses. Each
`variable data_type` specifies a named
variable and its corresponding data type that the SageMaker AI model accepts as
input. The data type specified must be a supported Athena data
type.

**RETURNS `data_type`**

`data_type` specifies the SQL data type that
`ml_function_name` returns to the query as
output from the SageMaker AI model.

**SAGEMAKER '`sagemaker_endpoint`'**

`sagemaker_endpoint` specifies the endpoint
of the SageMaker AI model.

**SELECT [...]
`ml_function_name`(`expression`)
[...]**

The SELECT query that passes values to function variables and the SageMaker AI
model to return a result. `ml_function_name`
specifies the function defined earlier in the query, followed by an
`expression` that is evaluated to pass
values. Values that are passed and returned must match the corresponding
data types specified for the function in the `USING EXTERNAL
 FUNCTION` clause.

## Example

The following example demonstrates a query using ML with Athena.

###### Example

```
USING EXTERNAL FUNCTION predict_customer_registration(age INTEGER)
    RETURNS DOUBLE
    SAGEMAKER 'xgboost-2019-09-20-04-49-29-303'
SELECT predict_customer_registration(age) AS probability_of_enrolling, customer_id
     FROM "sampledb"."ml_test_dataset"
     WHERE predict_customer_registration(age) < 0.5;
```
