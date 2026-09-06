

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ML\_MODEL\_INFO
<a name="r_SVV_ML_MODEL_INFO"></a>

State information about the current state of the machine learning model.

SVV\_ML\_MODEL\_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_SVV_ML_MODEL_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database\_name | char(128)  | The database of the model. | 
| schema\_name | char(128)  | The schema of the model. | 
| user\_name | char(128)  | The owner of the model.  | 
| model\_name | char(128) | The name of the model.  | 
| life\_cycle | char(20) | The lifecycle status of the model. | 
| is\_refreshable | integer | The state of the model whether it is refreshable if original tables and columns in the training query still exist and the user still has the permissions to them. Possible values are: 1 (refreshable) and 0 (not refreshable). | 
| model\_state  | char(128) | The current state of the model. | 

## Sample query
<a name="r_SVV_ML_MODEL_INFO-sample-query"></a>

The following query displays the current state of machine learning models.

```
SELECT schema_name, model_name, model_state 
FROM svv_ml_model_info;

 schema_name |        model_name            |             model_state
-------------+------------------------------+--------------------------------------
 public      | customer_churn_auto_model    | Train Model On SageMaker In Progress
 public      | customer_churn_xgboost_model | Model is Ready
(2 row)
```