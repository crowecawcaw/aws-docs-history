# Turn off Container Insights

To explicitly disable Container Insights on a compute environment, set the value to
`DISABLED`.

AWS Management Console

1. Open the [AWS Batch console](https://console.aws.amazon.com/batch/home "https://console.aws.amazon.com/batch/home").
2. Choose **Environments**.
3. Choose the compute environment that you want.
4. On the **Container insights** tab, choose
   **Disabled** for the compute environment.

AWS CLI
Use `update-compute-environment` to disable Container Insights on an
existing compute environment.

```
`$` `aws batch update-compute-environment \
 --compute-environment `my-compute-env` \
 --ecs-settings containerInsights=DISABLED`
```

API
Set `containerInsights` to `DISABLED` in your [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") request.

```
{
    "computeEnvironment": "`my-compute-env`",
    "ecsSettings": {
        "containerInsights": "DISABLED"
    }
}
```

For more information, see [UpdateComputeEnvironment](../APIReference/API_UpdateComputeEnvironment.md "../APIReference/API_UpdateComputeEnvironment.md") in the _AWS Batch API Reference_.

###### Important

After you set a Container Insights value on a compute environment, you cannot revert to
the default (unset) behavior, where the Container Insights setting is managed outside of
AWS Batch. To change the Container Insights
mode, you must call `UpdateComputeEnvironment` with the new value.

This also means that if you set this property in a CloudFormation template, a stack rollback
cannot revert the setting to its previous unset state.
