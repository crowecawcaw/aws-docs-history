# Update a service environment in AWS Batch

You can update a service environment to modify its capacity limits, change its operational state, or update resource tags. Service environment updates allow you to adjust capacity as your SageMaker Training workload requirements change or modify operational settings without recreating the environment. Before updating a service environment, understand which parameters can be modified and the impact of changes on running jobs.

You can change the Capacity limits, State, or Tags of a service environment.

Update a service environment (AWS Console)Use the AWS Batch console to update a service environment through the web interface.

**To update a service environment**

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. In the navigation pane, choose **Environments**.
3. Choose the **Service environment** tab.
4. Choose the service environment to update.
5. Choose **Actions**, then choose either:
   - **State** - Choose **Enable** or **Disable** to change the state.
   - **Capacity limit** - Modify the
     **Max number of instances**

6. Choose **Save changes** to apply the changes.

The service environment updates immediately. Check the environment details to confirm the changes were applied successfully. If you disabled the service environment, associated job queues will stop processing new service job submissions until you re-enable it.

Update a service environment (AWS CLI)
Use the `update-service-environment` command to modify a service environment with the AWS CLI.

**To update service environment capacity limits**

1. Update the capacity limit for a service environment:

```
aws batch update-service-environment \
    --service-environment my-sagemaker-service-env \
    --capacity-limits capacityUnit=NUM_INSTANCES,maxCapacity=20
```

2. Verify the update was applied successfully:

```
aws batch describe-service-environments \
    --service-environments my-sagemaker-service-env
```

**To update service environment state**

1. Disable a service environment to stop processing new jobs:

```
aws batch update-service-environment \
    --service-environment my-sagemaker-service-env \
    --state DISABLED
```

2. Re-enable a service environment to resume processing:

```
aws batch update-service-environment \
    --service-environment my-sagemaker-service-env \
    --state ENABLED
```

Service environment updates take effect immediately. Monitor the service environment state to ensure updates complete successfully before submitting new jobs.
