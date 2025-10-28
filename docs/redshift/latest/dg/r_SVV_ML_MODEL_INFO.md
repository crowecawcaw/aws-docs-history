Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ML_MODEL_INFO

State information about the current state of the machine learning
model.

SVV_ML_MODEL_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type | Description                                                                                                                                                                                                                     |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------- | ---------------------------- | -------------------------- |
| database_name  | char(128) | The database of the model.                                                                                                                                                                                                      |
| schema_name    | char(128) | The schema of the model.                                                                                                                                                                                                        |
| user_name      | char(128) | The owner of the model.                                                                                                                                                                                                         |
| model_name     | char(128) | The name of the model.                                                                                                                                                                                                          |
| life_cycle     | char(20)  | The lifecycle status of the model.                                                                                                                                                                                              |
| is_refreshable | integer   | The state of the model whether it is refreshable if original tables and columns in the training query still exist and the user still has the permissions to them. Possible values are: 1 (refreshable) and 0 (not refreshable). |
| model_state    | char(128) | The current state of the model.                                                                                                                                                                                                 | ## Sample query The following query displays the current state of machine learning models. ``` SELECT schema_name, model_name, model_state FROM svv_ml_model_info; schema_name | model_name | model_state -------------+------------------------------+-------------------------------------- public | customer_churn_auto_model | Train Model On SageMaker In Progress public | customer_churn_xgboost_model | Model is Ready (2 row) ``` |
