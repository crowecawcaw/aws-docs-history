

# Create or update a Studio app with a training plan using the SageMaker API or AWS CLI
<a name="use-training-plan-for-studio-app-creation-using-api-cli-sdk"></a>

To use SageMaker training plans for your SageMaker Studio app, specify the ARN of the training plan in the [`TrainingPlanArn`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceSpec.html#sagemaker-Type-ResourceSpec-TrainingPlanArn) parameter of the [`ResourceSpec`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceSpec.html) when calling the [`CreateApp`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateApp.html) API operation.

The following example shows how to create a JupyterLab or Code Editor app with a training plan using the AWS CLI. Replace the `--app-type` value with `JupyterLab` or `CodeEditor` as needed. The `InstanceType` must match the instance type of your training plan:

```
aws sagemaker create-app \
  --domain-id {{d-xxxxxxxxxxxx}} \
  --space-name {{my-space}} \
  --app-type {{JupyterLab}} \
  --app-name {{default}} \
  --resource-spec '{
    "InstanceType": "{{instance-type}}",
    "TrainingPlanArn": "{{arn:aws:sagemaker:us-east-1:123456789012:training-plan/my-training-plan}}"
  }'
```

After you create the app, you can verify the training plan association by calling the `DescribeApp` API. The response includes the `TrainingPlanArn` in the `ResourceSpec` if the app was created with a training plan.

```
aws sagemaker describe-app \
  --domain-id {{d-xxxxxxxxxxxx}} \
  --space-name {{my-space}} \
  --app-type {{JupyterLab}} \
  --app-name {{default}}
```

To update the training plan for an existing app, delete the current app and create a new one with the updated training plan ARN using the `create-app` command shown above:

```
aws sagemaker delete-app \
  --domain-id {{d-xxxxxxxxxxxx}} \
  --space-name {{my-space}} \
  --app-type {{JupyterLab}} \
  --app-name {{default}}
```