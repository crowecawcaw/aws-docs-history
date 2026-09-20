

# Instance preference lists for processing jobs
<a name="processing-job-instance-preferences"></a>

A processing job can accept an ordered list of up to 5 instance types instead of one. SageMaker AI launches the job on the first type in the list that has capacity, so the job starts sooner when your preferred type is constrained. It then runs, is monitored, and is billed exactly as if you had requested that type directly.

Instance preferences are available through the `CreateProcessingJob` API, the AWS SDKs, the AWS CLI, the SageMaker Python SDK, and the SageMaker AI console.

## How it works
<a name="processing-job-instance-preferences-how"></a>

Provide `InstancePreferences` in `ProcessingClusterConfig` instead of `InstanceType`, and set the instance count in one of two ways:
+ **Uniform** – one `InstanceCount` in `ProcessingClusterConfig`, used with whichever type is selected.
+ **Per preference** – an `InstanceCount` on every entry, for types with different accelerator counts. For example, `ml.g5.12xlarge` has four GPUs and `ml.g5.16xlarge` has one, so you can give the second a higher count.

A request that sets counts in both places, in neither, or on only some entries is rejected.

## Service quotas
<a name="processing-job-instance-preferences-quotas"></a>

SageMaker AI checks your service quota for every type in the list, not just the one it selects. Each type's quota must cover the instance count you request for it. If any type falls short, the request is rejected, even when the types ahead of it would have succeeded.

Request quota increases for every type in the list before you submit the job, in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas).

## Considerations
<a name="processing-job-instance-preferences-considerations"></a>
+ `InstancePreferences` can't be combined with `InstanceType`.
+ Each instance type can appear only once.
+ If you use a built-in algorithm, every listed type must be one it supports; otherwise the request is rejected.
+ SageMaker AI selects by capacity only. It doesn't compare GPU architecture, accelerator memory, or driver versions, so make sure your container works with every type in the list. A job that launches on an incompatible type can fail.
+ Processing jobs use On-Demand capacity only. To use a training plan, see [Instance preference lists for training jobs](train-instance-preferences.md).
+ `VolumeSizeInGB` and `VolumeKmsKeyId` apply to whichever type is selected.

## Examples
<a name="processing-job-instance-preferences-examples"></a>

The examples show the [ProcessingClusterConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingClusterConfig.html) part of a [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html) request.

Three types with a uniform count. The job launches on `ml.g6.4xlarge`, or on the next type in the list that has capacity:

```
"ProcessingResources": {
  "ClusterConfig": {
    "InstanceCount": 2,
    "VolumeSizeInGB": 100,
    "InstancePreferences": [
      { "InstanceType": "ml.g6.4xlarge" },
      { "InstanceType": "ml.g5.4xlarge" },
      { "InstanceType": "ml.g5.2xlarge" }
    ]
  }
}
```

A count on each entry:

```
"ProcessingResources": {
  "ClusterConfig": {
    "VolumeSizeInGB": 100,
    "InstancePreferences": [
      { "InstanceType": "ml.m5.12xlarge", "InstanceCount": 2 },
      { "InstanceType": "ml.m5.4xlarge", "InstanceCount": 6 }
    ]
  }
}
```

## Find the selected instance type
<a name="processing-job-instance-preferences-selected"></a>

`DescribeProcessingJob` returns the list you submitted plus the read-only `SelectedInstanceType` and `SelectedInstanceCount`. These two fields appear only after a type is selected, which can be shortly after the job is created. The top-level `InstanceType` isn't returned for these jobs:

```
"ProcessingResources": {
  "ClusterConfig": {
    "VolumeSizeInGB": 100,
    "InstancePreferences": [
      { "InstanceType": "ml.m5.12xlarge", "InstanceCount": 2 },
      { "InstanceType": "ml.m5.4xlarge", "InstanceCount": 6 }
    ],
    "SelectedInstanceType": "ml.m5.4xlarge",
    "SelectedInstanceCount": 6
  }
}
```

## Use instance preferences with the SageMaker Python SDK
<a name="processing-job-instance-preferences-pysdk"></a>

**Note**  
Instance preferences require version 3.22.0 or later of the SageMaker Python SDK. For more information about this release, see [Release v3.22.0](https://github.com/aws/sagemaker-python-sdk/releases/tag/v3.22.0) on the GitHub website.

Pass `instance_preferences` to `Processor` or `ScriptProcessor` as a list of dictionaries in the API's field names. Set `instance_count` on the processor for a uniform count, or in each dictionary instead.

```
from sagemaker.core.processing import Processor

processor = Processor(
    role="<execution-role-arn>",
    image_uri="<processing-image-uri>",
    volume_size_in_gb=100,
    instance_preferences=[
        {"InstanceType": "ml.m5.12xlarge", "InstanceCount": 2},
        {"InstanceType": "ml.m5.4xlarge", "InstanceCount": 6},
    ],
)
processor.run()
```

## Use instance preferences with Spark
<a name="processing-job-instance-preferences-spark"></a>

`PySparkProcessor` and `SparkJarProcessor` accept the same `instance_preferences` parameter. The Spark container image is resolved for the first type in the list, so keep all listed types in the same processor family (all CPU or all GPU). For more information about running Spark jobs, see [Run a Processing Job with Apache Spark](use-spark-processing-container.md).

```
from sagemaker.core.spark.processing import PySparkProcessor

spark_processor = PySparkProcessor(
    base_job_name="spark-preprocess",
    framework_version="3.5",
    role="<execution-role-arn>",
    instance_count=4,
    instance_preferences=[
        {"InstanceType": "ml.m5.4xlarge"},
        {"InstanceType": "ml.m5.2xlarge"},
    ],
)
spark_processor.run(
    submit_app="./preprocess.py",
    arguments=["--input", "s3://amzn-s3-demo-bucket/input"],
)
```

For more information, see the [SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/ml_ops/index.html#processing-jobs) on the Read the Docs website and the [SageMaker Python SDK example notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/ml-ops-examples/v3-processing-instance-preferences.ipynb) on the GitHub website.

## Use instance preferences in the SageMaker AI console
<a name="processing-job-instance-preferences-console"></a>

1. On the **Create processing job** page, under **Instance types**, choose the **Instance type** you prefer most. Then enter its **Instance count**.

1. Choose **Add another instance type**. The form becomes a list, with your first choice as **Priority** 1 and a new row below it. Fill in the new row, and repeat for up to 5 types.

1. To reorder, change a row's **Priority**; the row swaps places with the one that held that number. Choose **Remove** to drop a row.

After launch, the job details page shows an **Instance type preferences** table with the chosen type marked **Selected**.

## Related resources
<a name="processing-job-instance-preferences-related"></a>
+ [ProcessingClusterConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingClusterConfig.html) and [ProcessingInstancePreference](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProcessingInstancePreference.html) in the API reference
+ [Instance preference lists for training jobs](train-instance-preferences.md)
+ [SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/ml_ops/index.html#processing-jobs) on the Read the Docs website
+ [SageMaker Python SDK example notebook](https://github.com/aws/sagemaker-python-sdk/blob/master/v3-examples/ml-ops-examples/v3-processing-instance-preferences.ipynb) on the GitHub website