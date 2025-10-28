# Clean up

After you have finished using autoscaling for your serverless endpoint with Provisioned Concurrency,
you should clean up the resources you created. This involves deleting the scaling policy and
deregistering the model from Application Auto Scaling. Cleaning up ensures that you don't incur
unnecessary costs for resources you're no longer using.

## Delete a scaling policy

You can delete a scaling policy with the AWS Management Console, the AWS CLI, or the Application Auto Scaling API. For
more information on deleting a scaling policy with the AWS Management Console, see [Delete a scaling policy](endpoint-auto-scaling-delete.md "endpoint-auto-scaling-delete.md") in
the [SageMaker AI autoscaling documentation](endpoint-auto-scaling.md "endpoint-auto-scaling.md").

### Delete a scaling policy (AWS CLI)

To apply a scaling policy to your model, use the `delete-scaling-policy`
AWS CLI; command with the following parameters:

- `--policy-name` – The name of the scaling policy.
- `--resource-id` – The resource identifier for the
  variant. For this parameter, the resource type is `endpoint` and
  the unique identifier is the name of the variant. For example
  `endpoint/MyEndpoint/variant/MyVariant`.
- `--service-namespace` – Set this value to
  `sagemaker`.
- `--scalable-dimension` – Set this value to
  `sagemaker:variant:DesiredProvisionedConcurrency`.

The following example deletes scaling policy named `MyScalingPolicy` from
a model named `MyVariant`.

```
aws application-autoscaling delete-scaling-policy \
    --policy-name MyScalingPolicy \
    --service-namespace sagemaker \
    --scalable-dimension sagemaker:variant:DesiredProvisionedConcurrency \
    --resource-id endpoint/MyEndpoint/variant/MyVariant

```

### Delete a scaling policy (Application Auto Scaling API)

To delete a scaling policy to your model, use the `DeleteScalingPolicy`
Application Auto Scaling API action with the following parameters:

- `PolicyName` – The name of the scaling policy.
- `ResourceId` – The resource identifier for the
  variant. For this parameter, the resource type is `endpoint` and
  the unique identifier is the name of the variant. For example
  `endpoint/MyEndpoint/variant/MyVariant`.
- `ServiceNamespace` – Set this value to
  `sagemaker`.
- `ScalableDimension` – Set this value to
  `sagemaker:variant:DesiredProvisionedConcurrency`.

The following example uses the Application Auto Scaling API to delete a scaling policy named
`MyScalingPolicy` from a model named `MyVariant`.

```
POST / HTTP/1.1
Host: autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AnyScaleFrontendService.DeleteScalingPolicy
X-Amz-Date: 20160506T182145Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "MyScalingPolicy",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/MyEndpoint/variant/MyVariant",
    "ScalableDimension": "sagemaker:variant:DesiredProvisionedConcurrency",
}

```

## Deregister a model

You can deregister a model with the AWS Management Console, the AWS CLI, or the Application Auto Scaling API.

### Deregister a model (AWS CLI)

To deregister a model from Application Auto Scaling, use the `deregister-scalable-target`
AWS CLI; command with the following parameters:

- `--resource-id` – The resource identifier for the
  variant. For this parameter, the resource type is `endpoint` and
  the unique identifier is the name of the variant. For example
  `endpoint/MyEndpoint/variant/MyVariant`.
- `--service-namespace` – Set this value to
  `sagemaker`.
- `--scalable-dimension` – Set this value to
  `sagemaker:variant:DesiredProvisionedConcurrency`.

The following example deregisters a model named `MyVariant` from Application Auto Scaling.

```
aws application-autoscaling deregister-scalable-target \
    --service-namespace sagemaker \
    --scalable-dimension sagemaker:variant:DesiredProvisionedConcurrency \
    --resource-id endpoint/MyEndpoint/variant/MyVariant

```

### Deregister a model (Application Auto Scaling API)

To deregister a model from Application Auto Scaling use the `DeregisterScalableTarget`
Application Auto Scaling API action with the following parameters:

- `ResourceId` – The resource identifier for the
  variant. For this parameter, the resource type is `endpoint` and
  the unique identifier is the name of the variant. For example
  `endpoint/MyEndpoint/variant/MyVariant`.
- `ServiceNamespace` – Set this value to
  `sagemaker`.
- `ScalableDimension` – Set this value to
  `sagemaker:variant:DesiredProvisionedConcurrency`.

The following example uses the Application Auto Scaling API to deregister a model named
`MyVariant` from Application Auto Scaling.

```
POST / HTTP/1.1
Host: autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AnyScaleFrontendService.DeregisterScalableTarget
X-Amz-Date: 20160506T182145Z
User-Agent: aws-cli/1.10.23 Python/2.7.11 Darwin/15.4.0 botocore/1.4.8
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/MyEndpoint/variant/MyVariant",
    "ScalableDimension": "sagemaker:variant:DesiredProvisionedConcurrency",
}

```

### Deregister a model (AWS Management Console)

To deregister a model (production variant) with the AWS Management Console:

1. Open the [Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the navigational panel, choose **Inference**.
3. Choose **Endpoints** to view a list of your endpoints.
4. Choose the serverless endpoint hosting the production variant. A page
   with the settings of the endpoint will appear, with the production variants
   listed under **Endpoint runtime settings** section.
5. Select the production variant that you want to deregister, and choose
   **Configure auto scaling**. The **Configure variant automatic scaling**
   dialog box appears.
6. Choose **Deregister auto scaling**.
