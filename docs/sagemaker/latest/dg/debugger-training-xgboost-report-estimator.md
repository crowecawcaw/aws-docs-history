# Construct a SageMaker AI XGBoost ModelTrainer with the Debugger XGBoost Report rule

###### Note

Amazon SageMaker Debugger is no longer open to new customers.
Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
Debugger, but we do not plan to introduce new features. For more information, see [Debugger availability change](debugger-availability-change.md "debugger-availability-change.md").

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

When you construct a SageMaker AI ModelTrainer for an XGBoost training job, specify the rule
as shown in the following example code.

```
import boto3
import sagemaker
from sagemaker.train import ModelTrainer
from sagemaker import image_uris
from sagemaker.debugger import Rule, rule_configs

`rules`=[
    `Rule.sagemaker(rule_configs.create_xgboost_report())`
]

region = boto3.Session().region_name
xgboost_container=sagemaker.image_uris.retrieve("xgboost", region, "`1.2-1`")

model_trainer=ModelTrainer(
    role=sagemaker.get_execution_role()
    image_uri=xgboost_container,
    base_job_name="`debugger-xgboost-report-demo`",
    instance_count=`1`,
    instance_type="`ml.m5.2xlarge`",

    # Add the Debugger XGBoost report rule
    rules=`rules`
)

model_trainer.train()
```
