

# Instance preference lists for training jobs
<a name="train-instance-preferences"></a>

A training job can accept an ordered list of up to 5 instance types instead of one. SageMaker AI launches the job on the first type in the list that has capacity, so the job starts sooner when your preferred type is constrained. It then runs, is monitored, and is billed exactly as if you had requested that type directly.

Instance preferences are available through the `CreateTrainingJob` API, the AWS SDKs, the AWS CLI, the SageMaker Python SDK, and the SageMaker AI console.

## How it works
<a name="train-instance-preferences-how"></a>

Provide `InstancePreferences` in `ResourceConfig` instead of `InstanceType`, and set the instance count in one of two ways:
+ **Uniform** – one `InstanceCount` in `ResourceConfig`, used with whichever type is selected.
+ **Per preference** – an `InstanceCount` on every entry, for types with different accelerator counts. For example, `ml.g5.12xlarge` has four GPUs and `ml.g5.16xlarge` has one, so you can give the second a higher count.

A request that sets counts in both places, in neither, or on only some entries is rejected.

## Service quotas
<a name="train-instance-preferences-quotas"></a>

SageMaker AI checks your service quota for every type in the list, not just the one it selects. Each type's quota must cover the instance count you request for it. If any type falls short, the request is rejected, even when the types ahead of it would have succeeded.

Request quota increases for every type in the list before you submit the job. For more information, see [Step 2: Check and request service quotas](train-get-capacity.md#train-get-capacity-quotas).

## Waiting for capacity
<a name="train-instance-preferences-waiting"></a>

If no type in the list has capacity, the job waits and retries as capacity is released. `MaxPendingTimeInSeconds` sets how long it keeps retrying, as described in [On-Demand Instances](train-get-capacity.md#train-get-capacity-ondemand). With a list:
+ The limit covers the total time spent across the whole list, not each type separately.
+ Some `Pending` time on a training-plan-backed type doesn't count toward the limit. For more information, see [MaxPendingTimeInSeconds](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html#sagemaker-Type-StoppingCondition-MaxPendingTimeInSeconds).

**Note**  
The job waits only if the list includes at least one accelerated computing instance type, such as `ml.p`, `ml.g`, or `ml.trn`. A CPU-only list is evaluated once: the job starts if one of the types has capacity, and otherwise fails with a capacity error without being re-evaluated.

## Considerations
<a name="train-instance-preferences-considerations"></a>
+ `InstancePreferences` can't be combined with `InstanceType`, `InstanceGroups`, `InstancePlacementConfig`, or `EnableManagedSpotTraining`.
+ Each instance type can appear only once.
+ If you use a built-in algorithm, every listed type must be one it supports; otherwise the request is rejected.
+ SageMaker AI selects by capacity only. It doesn't compare GPU architecture, accelerator memory, Elastic Fabric Adapter (EFA) support, or driver versions, so make sure your container works with every type in the list. A job that launches on an incompatible type can fail.
+ `VolumeSizeInGB`, `VolumeKmsKeyId`, and `KeepAlivePeriodInSeconds` apply to whichever type is selected.

## Use instance preferences with training plans
<a name="train-instance-preferences-plans"></a>

Add `TrainingPlanArns` to an entry to fill it from a training plan. The entry's instance type must match the plan's. Entries without a plan use On-Demand capacity. Put the plan-backed entry first so that your reserved capacity is tried before the other types. For more information about plans, see [Reserve Flexible Training Plans for ML workloads](reserve-capacity-with-training-plans.md).

If the plan has no capacity when the job is evaluated, SageMaker AI moves on to the next entry rather than waiting for the reservation, so the job can start on On-Demand capacity right away.

Alternatively, set the job-level `TrainingPlanArn`. It applies to the entry whose instance type matches the plan and is rejected if none does. You can't set both the job-level and per-entry fields.

## Examples
<a name="train-instance-preferences-examples"></a>

The examples show the [ResourceConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html) and [StoppingCondition](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html) parts of a [CreateTrainingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingJob.html) request.

Two types with a uniform count. The job launches on `ml.g6.48xlarge`, or on `ml.g5.48xlarge` if that has no capacity:

```
"ResourceConfig": {
  "InstanceCount": 2,
  "VolumeSizeInGB": 500,
  "InstancePreferences": [
    { "InstanceType": "ml.g6.48xlarge" },
    { "InstanceType": "ml.g5.48xlarge" }
  ]
}
```

A count on each entry:

```
"ResourceConfig": {
  "VolumeSizeInGB": 500,
  "InstancePreferences": [
    { "InstanceType": "ml.g6.48xlarge", "InstanceCount": 2 },
    { "InstanceType": "ml.g5.48xlarge", "InstanceCount": 4 }
  ]
}
```

A 30-minute limit on waiting for capacity:

```
"StoppingCondition": {
  "MaxRuntimeInSeconds": 86400,
  "MaxPendingTimeInSeconds": 1800
}
```

A training plan on the first entry and On-Demand capacity on the second:

```
"ResourceConfig": {
  "InstanceCount": 4,
  "VolumeSizeInGB": 500,
  "InstancePreferences": [
    {
      "InstanceType": "ml.p5.48xlarge",
      "TrainingPlanArns": ["arn:aws:sagemaker:us-west-2:111122223333:training-plan/p5-plan"]
    },
    { "InstanceType": "ml.p4d.24xlarge" }
  ]
}
```

The same job using the job-level plan field:

```
"ResourceConfig": {
  "InstanceCount": 4,
  "VolumeSizeInGB": 500,
  "TrainingPlanArn": "arn:aws:sagemaker:us-west-2:111122223333:training-plan/p5-plan",
  "InstancePreferences": [
    { "InstanceType": "ml.p5.48xlarge" },
    { "InstanceType": "ml.p4d.24xlarge" }
  ]
}
```

## Find the selected instance type
<a name="train-instance-preferences-selected"></a>

`DescribeTrainingJob` returns the list you submitted plus the read-only `SelectedInstanceType` and `SelectedInstanceCount`. These two fields appear only after a type is selected, so they are absent while the job waits for capacity. The top-level `InstanceType` isn't returned for these jobs:

```
"ResourceConfig": {
  "VolumeSizeInGB": 500,
  "InstancePreferences": [
    { "InstanceType": "ml.g6.48xlarge", "InstanceCount": 2 },
    { "InstanceType": "ml.g5.48xlarge", "InstanceCount": 4 }
  ],
  "SelectedInstanceType": "ml.g5.48xlarge",
  "SelectedInstanceCount": 4
}
```

## Use instance preferences with the SageMaker Python SDK
<a name="train-instance-preferences-pysdk"></a>

**Note**  
Instance preferences require version 3.22.0 or later of the SageMaker Python SDK. For more information about this release, see [Release v3.22.0](https://github.com/aws/sagemaker-python-sdk/releases/tag/v3.22.0) on the GitHub website.

Pass `instance_preferences` in the `Compute` configuration of `ModelTrainer`. Set `instance_count` on `Compute` for a uniform count, or on each `InstancePreference` instead. Add `training_plan_arns` to an entry to fill it from a training plan.

```
from sagemaker.core.shapes import InstancePreference
from sagemaker.core.training.configs import Compute
from sagemaker.train.model_trainer import ModelTrainer

compute = Compute(
    volume_size_in_gb=500,
    instance_preferences=[
        InstancePreference(
            instance_type="ml.p5.48xlarge",
            instance_count=4,
            training_plan_arns=["arn:aws:sagemaker:us-west-2:111122223333:training-plan/p5-plan"],
        ),
        InstancePreference(instance_type="ml.p4d.24xlarge", instance_count=8),
    ],
)

trainer = ModelTrainer(
    training_image="<training-image-uri>",
    compute=compute,
)
trainer.train()
```

For more information, see the [SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/training/index.html#instance-preferences) on the Read the Docs website and the [SageMaker Python SDK example notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/training-examples/instance-preferences-example.ipynb) on the GitHub website.

## Use instance preferences in the SageMaker AI console
<a name="train-instance-preferences-console"></a>

1. On the **Create training job** page, under **Instance types**, choose the **Instance type** you prefer most. Then choose its **Instance capacity** (**On-Demand Instances** or a training plan) and enter its **Instance count**.

1. Choose **Add another instance type**. The form becomes a list, with your first choice as **Priority** 1 and a new row below it. Fill in the new row, and repeat for up to 5 types.

1. To reorder, change a row's **Priority**; the row swaps places with the one that held that number. Choose **Remove** to drop a row.

After launch, the job details page shows an **Instance type preferences** table with the chosen type marked **Selected**. Until a type is chosen, the instance type shows **Pending selection**.

## Related resources
<a name="train-instance-preferences-related"></a>
+ [ResourceConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceConfig.html) and [InstancePreference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstancePreference.html) in the API reference
+ [Instance preference lists for processing jobs](processing-job-instance-preferences.md)
+ [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/) for the instance types available in each Region
+ [SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/training/index.html#instance-preferences) on the Read the Docs website
+ [SageMaker Python SDK example notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/training-examples/instance-preferences-example.ipynb) on the GitHub website