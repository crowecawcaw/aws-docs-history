# Construct a SageMaker AI

XGBoost estimator with the Debugger XGBoost Report rule

The [CreateXgboostReport](debugger-built-in-rules.md#create-xgboost-report "debugger-built-in-rules.md#create-xgboost-report")
rule collects the following output tensors from your training job:

- `hyperparameters` – Saves at the first step.
- `metrics` – Saves loss and accuracy every 5
  steps.
- `feature_importance` – Saves every 5 steps.
- `predictions` – Saves every 5 steps.
- `labels` – Saves every 5 steps.
  The output tensors are saved at a default S3 bucket. For example,
  `s3://sagemaker-`<region>`-`<12digit_account_id>`/`<base-job-name>`/debug-output/`.

When you construct a SageMaker AI estimator for an XGBoost training job, specify the rule
as shown in the following example code.

Using the SageMaker AI generic estimator

```
import boto3
import sagemaker
from sagemaker.estimator import Estimator
from sagemaker import image_uris
from sagemaker.debugger import Rule, rule_configs

`rules`=[
    `Rule.sagemaker(rule_configs.create_xgboost_report())`
]

region = boto3.Session().region_name
xgboost_container=sagemaker.image_uris.retrieve("xgboost", region, "`1.2-1`")

estimator=Estimator(
    role=sagemaker.get_execution_role()
    image_uri=xgboost_container,
    base_job_name="`debugger-xgboost-report-demo`",
    instance_count=`1`,
    instance_type="`ml.m5.2xlarge`",

    # Add the Debugger XGBoost report rule
    rules=`rules`
)

estimator.fit(wait=False)
```
