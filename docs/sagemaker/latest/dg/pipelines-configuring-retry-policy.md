# Configuring a retry policy

While SageMaker Pipelines provide a robust and automated way to orchestrate machine learning workflows, you might encounter failures when you run them.
To handle such scenarios gracefully and improve the reliability of your pipelines, you can configure retry policies that define how and when to automatically retry specific steps after encountering an exception.
The retry policy allows you to specify the types of exceptions to retry, the maximum number of retry attempts, the interval between retries, and the backoff rate for increasing the retry intervals. The following section provides examples of how to configure a retry policy for a training step in your pipeline, both in JSON and using the SageMaker Python SDK.

The following is an example of a training step with a retry policy.

```
{
    "Steps": [
        {
            "Name": "`MyTrainingStep`",
            "Type": "Training",
            "RetryPolicies": [
                {
                    "ExceptionType": [
                        "`SageMaker.JOB_INTERNAL_ERROR`",
                        "`SageMaker.CAPACITY_ERROR`"
                    ],
                    "IntervalSeconds": `1`,
                    "BackoffRate": `2`,
                    "MaxAttempts": `5`
                }
            ]
        }
    ]
}
```

The following is an example of how to build a `TrainingStep` in SDK for Python (Boto3) with
a retry policy.

```
from sagemaker.workflow.retry import (
    StepRetryPolicy,
    StepExceptionTypeEnum,
    SageMakerJobExceptionTypeEnum,
    SageMakerJobStepRetryPolicy
)

step_train = TrainingStep(
    name="`MyTrainingStep`",
    xxx,
    retry_policies=[
        // override the default
        StepRetryPolicy(
            exception_types=[
                `StepExceptionTypeEnum.SERVICE_FAULT`,
                `StepExceptionTypeEnum.THROTTLING`
            ],
            expire_after_mins=`5`,
            interval_seconds=`10`,
            backoff_rate=`2.0`
        ),
        // retry when resource limit quota gets exceeded
        SageMakerJobStepRetryPolicy(
            exception_types=[`SageMakerJobExceptionTypeEnum.RESOURCE_LIMIT`],
            expire_after_mins=`120`,
            interval_seconds=`60`,
            backoff_rate=`2.0`
        ),
        // retry when job failed due to transient error or EC2 ICE.
        SageMakerJobStepRetryPolicy(
            failure_reason_types=[
                `SageMakerJobExceptionTypeEnum.INTERNAL_ERROR`,
                `SageMakerJobExceptionTypeEnum.CAPACITY_ERROR`,
            ],
            max_attempts=`10`,
            interval_seconds=`30`,
            backoff_rate=`2.0`
        )
    ]
)
```

For more information on configuring retry behavior for certain step types, see
_[Amazon SageMaker Pipelines - Retry Policy](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#retry-policy "https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_model_building_pipeline.html#retry-policy")_ in the Amazon SageMaker Python SDK
documentation.
