# Create or update a Studio app with a training plan using the SageMaker API or AWS CLI

To use SageMaker training plans for your SageMaker Studio app, specify the ARN of the training plan in
the [`TrainingPlanArn`](../APIReference/API_ResourceSpec.md#sagemaker-Type-ResourceSpec-TrainingPlanArn "../APIReference/API_ResourceSpec.md#sagemaker-Type-ResourceSpec-TrainingPlanArn") parameter of the [`ResourceSpec`](../APIReference/API_ResourceSpec.md "../APIReference/API_ResourceSpec.md") when calling the [`CreateApp`](../APIReference/API_CreateApp.md "../APIReference/API_CreateApp.md") API operation.

The following example shows how to create a JupyterLab or Code Editor app with a training
plan using the AWS CLI. Replace the `--app-type` value with
`JupyterLab` or `CodeEditor` as needed. The
`InstanceType` must match the instance type of your training plan:

```
aws sagemaker create-app \
  --domain-id `d-xxxxxxxxxxxx` \
  --space-name `my-space` \
  --app-type `JupyterLab` \
  --app-name `default` \
  --resource-spec '{
    "InstanceType": "`instance-type`",
    "TrainingPlanArn": "`arn:aws:sagemaker:us-east-1:123456789012:training-plan/my-training-plan`"
  }'
```

After you create the app, you can verify the training plan association by calling the
`DescribeApp` API. The response includes the `TrainingPlanArn` in the
`ResourceSpec` if the app was created with a training plan.

```
aws sagemaker describe-app \
  --domain-id `d-xxxxxxxxxxxx` \
  --space-name `my-space` \
  --app-type `JupyterLab` \
  --app-name `default`
```

To update the training plan for an existing app, delete the current app and create a new
one with the updated training plan ARN using the `create-app` command shown
above:

```
aws sagemaker delete-app \
  --domain-id `d-xxxxxxxxxxxx` \
  --space-name `my-space` \
  --app-type `JupyterLab` \
  --app-name `default`
```
