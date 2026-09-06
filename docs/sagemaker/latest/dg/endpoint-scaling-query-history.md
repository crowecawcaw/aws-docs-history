

# Check the status of a scaling activity by describing scaling activities
<a name="endpoint-scaling-query-history"></a>

You can check the status of a scaling activity for your auto scaled endpoint by describing scaling activities. Application Auto Scaling provides descriptive information about the scaling activities in the specified namespace from the previous six weeks. For more information, see [Scaling activities for Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/application-auto-scaling-scaling-activities.html) in the *Application Auto Scaling User Guide*.

To check the status of a scaling activity, use the [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) command. You can't check the status of a scaling activity using the console.

**Topics**
+ [Describe scaling activities (AWS CLI)](#endpoint-how-to)
+ [Identify blocked scaling activities from instance quotas (AWS CLI)](#endpoint-identify-blocked-autoscaling)

## Describe scaling activities (AWS CLI)
<a name="endpoint-how-to"></a>

To describe scaling activities for all SageMaker AI resources that registered with Application Auto Scaling, use the [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) command, specifying `sagemaker` for the `--service-namespace` option.

```
aws application-autoscaling describe-scaling-activities \
  --service-namespace sagemaker
```

To describe scaling activities for a specific resource, include the `--resource-id` option. 

```
aws application-autoscaling describe-scaling-activities \
  --service-namespace sagemaker \
  --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}}
```

The following example shows the output produced when you run this command.

```
{
    "ActivityId": "activity-id",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/my-endpoint/variant/my-variant",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount",
    "Description": "string",
    "Cause": "string",
    "StartTime": timestamp,
    "EndTime": timestamp,
    "StatusCode": "string",
    "StatusMessage": "string"
}
```

## Identify blocked scaling activities from instance quotas (AWS CLI)
<a name="endpoint-identify-blocked-autoscaling"></a>

When you scale out (add more instances), you might reach your account-level instance quota. You can use the [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) command to check whether you have reached your instance quota. When you exceed your quota, auto scaling is blocked. 

To check if you have reached your instance quota, use the [describe-scaling-activities](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/describe-scaling-activities.html) command and specify the resource ID for the `--resource-id` option. 

```
aws application-autoscaling describe-scaling-activities \
    --service-namespace sagemaker \
    --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}}
```

Within the return syntax, check the [StatusCode](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingActivity.html#autoscaling-Type-ScalingActivity-StatusCode) and [StatusMessage](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_ScalingActivity.html#autoscaling-Type-ScalingActivity-StatusMessage) keys and their associated values. `StatusCode` returns `Failed`. Within `StatusMessage` there is a message indicating that the account-level service quota was reached. The following is an example of what that message might look like: 

```
{
    "ActivityId": "activity-id",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/my-endpoint/variant/my-variant",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount",
    "Description": "string",
    "Cause": "minimum capacity was set to 110",
    "StartTime": timestamp,
    "EndTime": timestamp,
    "StatusCode": "Failed",
    "StatusMessage": "Failed to set desired instance count to 110. Reason: The 
    account-level service limit 'ml.xx.xxxxxx for endpoint usage' is 1000 
    Instances, with current utilization of 997 Instances and a request delta 
    of 20 Instances. Please contact AWS support to request an increase for this 
    limit. (Service: AmazonSageMaker; Status Code: 400; 
    Error Code: ResourceLimitExceeded; Request ID: request-id)."
}
```