

# Using environment variables in Amazon MWAA Serverless workflows
<a name="workflows-environment-variables"></a>

Environment variables pass key-value settings to every task in a workflow. You set them with the optional [Environment parameter](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html#mwaaserverless-CreateWorkflow-request-Environment) of `CreateWorkflow` or the [Environment parameter](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_UpdateWorkflow.html#mwaaserverless-UpdateWorkflow-request-Environment) of `UpdateWorkflow`. Your tasks receive them in their process environment.

Use environment variables for non-secret settings that your tasks read at runtime, such as a stage name, a feature flag, or a public endpoint.

**Important**  
`GetWorkflow` returns the variables that you set in the `Environment` block in plain text. Don't store passwords, tokens, or other secrets in environment variables. Store them in a secrets backend instead. For more information, see [Managing connections and variables](connections.md).

**Topics**
+ [Setting and reading environment variables](#workflows-environment-variables-set)
+ [Limits and reserved keys](#workflows-environment-variables-limits)
+ [Troubleshooting environment variables](#workflows-environment-variables-troubleshooting)

## Setting and reading environment variables
<a name="workflows-environment-variables-set"></a>

You set environment variables only when you create or update a workflow. You can't set or override them when you start a workflow run with `StartWorkflowRun`. A change that you make with `update-workflow` applies to the next run.

A workflow can have up to 50 environment variables. For all limits, see [Limits and reserved keys](#workflows-environment-variables-limits).

The following AWS CLI command creates a workflow with two environment variables. In the command, replace {{my-workflow}} with your workflow name, and replace {{dags/my\_dag.yaml}} with the Amazon S3 object key of your workflow definition. Replace the role ARN with your execution role ARN, and replace {{us-east-1}} with your Region. Replace the variable names and values with your own.

```
aws mwaa-serverless create-workflow \
    --name {{my-workflow}} \
    --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --environment '{"Variables": {"APP_STAGE": "prod", "FEATURE_X_ENABLED": "true"}}' \
    --region {{us-east-1}}
```

To change the variables of an existing workflow, run `update-workflow` with the complete set of variables that you want. Replace the workflow ARN, the object key, the role ARN, and the Region with your own values:

```
aws mwaa-serverless update-workflow \
    --workflow-arn {{arn:aws:airflow-serverless:us-east-1:111122223333:workflow/my-workflow-a1b2c3d4e5}} \
    --definition-s3-location '{"Bucket": "amzn-s3-demo-bucket", "ObjectKey": "{{dags/my_dag.yaml}}"}' \
    --role-arn {{arn:aws:iam::111122223333:role/MyMWAAServerlessRole}} \
    --environment '{"Variables": {"APP_STAGE": "prod", "FEATURE_X_ENABLED": "false"}}' \
    --region {{us-east-1}}
```

Every task in the workflow can read the environment variables when it runs.

## Limits and reserved keys
<a name="workflows-environment-variables-limits"></a>

The following limits apply to the `Variables` map:
+ Each workflow can have up to 50 variables.
+ Each key can be up to 128 characters. A key must start with a letter and can contain only letters, numbers, and underscores.
+ Each value can be up to 255 characters.

Amazon MWAA Serverless reserves the following keys and rejects requests that set them, except for the secrets backend keys that are described after this list:
+ Keys that start with `AWS_`
+ Keys that start with `AIRFLOW__` (two underscores)
+ `PATH`
+ `PYTHONPATH`
+ `HOME`
+ `AIRFLOW_HOME`
+ `TMPDIR`
+ `PYTHONUNBUFFERED`
+ `LC_CTYPE`

You can set the following two reserved keys to configure the secrets backend. For more information, see [Configuring a secrets backend](connections.md#connections-backend-override).
+ `AIRFLOW__WORKERS__SECRETS_BACKEND`
+ `AIRFLOW__WORKERS__SECRETS_BACKEND_KWARGS`

For the complete list of constraints, see the `Environment` parameter in the [Amazon MWAA Serverless API Reference](https://docs.aws.amazon.com/mwaa-serverless/latest/APIReference/API_CreateWorkflow.html#mwaaserverless-CreateWorkflow-request-Environment).

## Troubleshooting environment variables
<a name="workflows-environment-variables-troubleshooting"></a>

The following table lists common problems with environment variables, along with their causes and fixes.


| Error or symptom | Cause | Fix | 
| --- | --- | --- | 
| ValidationException on create-workflow or update-workflow | A key is reserved or breaks the naming rules, or the map exceeds a limit. | Rename or remove the key, and check the counts and lengths in [Limits and reserved keys](#workflows-environment-variables-limits). | 
| A run doesn't see a new or changed value | Amazon MWAA Serverless captures environment variables when you create or update a workflow. You can't pass them to start-workflow-run. | Run update-workflow with the new value, then start a new run. | 
| KeyError from os.environ, or a task reads an empty value | The key isn't set, or its case doesn't match. Keys are case sensitive. | Check the Environment block that get-workflow returns, and match the key exactly. | 