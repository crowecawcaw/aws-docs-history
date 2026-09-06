

# Turn on Container Insights
<a name="cloudwatch-container-insights-working"></a>

Complete the following steps to turn on Container Insights for AWS Batch compute environments.

------
#### [ AWS Management Console ]

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch/home).

1. Choose **Environments**.

1. Choose the compute environment that you want.

1. On the **Container insights** tab, turn on **Container insights** for the compute environment.
**Tip**  
You can select a default interval to aggregate the metrics or create a custom interval.

------
#### [ AWS CLI ]

**Enable Container Insights when creating a compute environment**

Use the `--ecs-settings` parameter with `create-compute-environment` to enable Container Insights on a new compute environment.

```
$ aws batch create-compute-environment \
    --compute-environment-name {{my-compute-env}} \
    --type MANAGED \
    --state ENABLED \
    --ecs-settings containerInsights=ENHANCED \
    --compute-resources type=FARGATE,maxvCpus=256,subnets={{subnet-a123456b}},securityGroupIds={{sg-a12b3456}}
```

Valid values for `containerInsights` are `ENABLED`, `ENHANCED`, and `DISABLED`.

**Enable Container Insights on an existing compute environment**

Use `update-compute-environment` to enable or change Container Insights on an existing compute environment.

```
$ aws batch update-compute-environment \
    --compute-environment {{my-compute-env}} \
    --ecs-settings containerInsights=ENHANCED
```

**Verify the Container Insights setting**

Use `describe-compute-environments` to verify the current setting.

```
$ aws batch describe-compute-environments \
    --compute-environments {{my-compute-env}} \
    --query "computeEnvironments[0].ecsSettings"
```

The following shows the output when Container Insights is enabled.

```
{
    "containerInsights": "ENHANCED"
}
```

**Note**  
If Container Insights has never been set on the compute environment, the `ecsSettings` field is absent from the response.

------
#### [ API ]

Use the `ecsSettings` parameter in your [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) or [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) request.

**Create a compute environment with Container Insights**

Include `ecsSettings` in the request body:

```
{
    "computeEnvironmentName": "{{my-compute-env}}",
    "type": "MANAGED",
    "state": "ENABLED",
    "ecsSettings": {
        "containerInsights": "ENHANCED"
    },
    "computeResources": {
        "type": "FARGATE",
        "maxvCpus": 256,
        "subnets": ["{{subnet-a123456b}}"],
        "securityGroupIds": ["{{sg-a12b3456}}"]
    }
}
```

**Update Container Insights on an existing compute environment**

```
{
    "computeEnvironment": "{{my-compute-env}}",
    "ecsSettings": {
        "containerInsights": "ENHANCED"
    }
}
```

For more information, see [CreateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_CreateComputeEnvironment.html) and [UpdateComputeEnvironment](https://docs.aws.amazon.com/batch/latest/APIReference/API_UpdateComputeEnvironment.html) in the *AWS Batch API Reference*.

------

**Important**  
After you set a Container Insights value on a compute environment, you cannot revert to the default (unset) behavior, where the Container Insights setting is managed outside of AWS Batch. To change the Container Insights mode, you must call `UpdateComputeEnvironment` with the new value.  
This also means that if you set this property in a CloudFormation template, a stack rollback cannot revert the setting to its previous unset state.