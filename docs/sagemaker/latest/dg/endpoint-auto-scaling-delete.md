# Delete a scaling policy

If you no longer need a scaling policy, you can delete it at any time.

###### Topics

- [Delete all scaling policies
  and deregister the model (console)](#endpoint-auto-scaling-delete-console "#endpoint-auto-scaling-delete-console")
- [Delete a scaling policy (AWS CLI
  or Application Auto Scaling API)](#endpoint-auto-scaling-delete-code "#endpoint-auto-scaling-delete-code")

## Delete all scaling policies

and deregister the model (console)

###### To delete all scaling policies and deregister the variant as a scalable

target

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the navigation pane, choose **Endpoints**.
3. Choose your endpoint, and then for **Endpoint runtime
   settings**, choose the variant.
4. Choose **Configure auto scaling**.
5. Choose **Deregister auto scaling**.

## Delete a scaling policy (AWS CLI

or Application Auto Scaling API)

You
can use the AWS CLI or the Application Auto Scaling API to delete a scaling policy from a
variant.

### Delete a scaling policy

(AWS CLI)

To delete a scaling policy from a variant, use the [delete-scaling-policy](../../../cli/latest/reference/application-autoscaling/delete-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/delete-scaling-policy.md") command with the following parameters:

- `--policy-name`—The name of the scaling
  policy.
- `--resource-id`—The resource identifier for the
  variant. For this parameter, the resource type is `endpoint`
  and the unique identifier is the name of the variant. For example,
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `--service-namespace`—Set this value to
  `sagemaker`.
- `--scalable-dimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.

###### Example

The following example deletes a target tracking scaling policy named
`my-scaling-policy` from a
variant named `my-variant`, running on
the `my-endpoint` endpoint.

```
aws application-autoscaling delete-scaling-policy \
  --policy-name `my-scaling-policy` \
  --resource-id endpoint/`my-endpoint`/variant/`my-variant` \
  --service-namespace sagemaker \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount
```

### Delete a scaling policy

(Application Auto Scaling API)

To delete a scaling policy from your variant, use the [DeleteScalingPolicy](../../../autoscaling/application/APIReference/API_DeleteScalingPolicy.md "../../../autoscaling/application/APIReference/API_DeleteScalingPolicy.md") Application Auto Scaling API action with the following
parameters:

- `PolicyName`—The name of the scaling policy.
- `ServiceNamespace`—Set this value to
  `sagemaker`.
- `ResourceID`—The resource identifier for the
  variant. For this parameter, the resource type is `endpoint`
  and the unique identifier is the name of the variant. For example,
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `ScalableDimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.

###### Example

The following example deletes a target tracking scaling policy named
`my-scaling-policy` from a
variant named `my-variant`, running on
the `my-endpoint` endpoint.

```
POST / HTTP/1.1
Host: application-autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AnyScaleFrontendService.DeleteScalingPolicy
X-Amz-Date: 20230506T182145Z
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "`my-scaling-policy`",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/`my-endpoint`/variant/`my-variant`",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount"
}
```
