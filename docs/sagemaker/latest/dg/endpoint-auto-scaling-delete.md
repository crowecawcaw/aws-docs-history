

# Delete a scaling policy
<a name="endpoint-auto-scaling-delete"></a>

If you no longer need a scaling policy, you can delete it at any time.

**Topics**
+ [Delete all scaling policies and deregister the model (console)](#endpoint-auto-scaling-delete-console)
+ [Delete a scaling policy (AWS CLI or Application Auto Scaling API)](#endpoint-auto-scaling-delete-code)

## Delete all scaling policies and deregister the model (console)
<a name="endpoint-auto-scaling-delete-console"></a>

**To delete all scaling policies and deregister the variant as a scalable target**

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. On the navigation pane, choose **Endpoints**.

1. Choose your endpoint, and then for **Endpoint runtime settings**, choose the variant.

1. Choose **Configure auto scaling**.

1. Choose **Deregister auto scaling**.

## Delete a scaling policy (AWS CLI or Application Auto Scaling API)
<a name="endpoint-auto-scaling-delete-code"></a>

You can use the AWS CLI or the Application Auto Scaling API to delete a scaling policy from a variant.

### Delete a scaling policy (AWS CLI)
<a name="endpoint-auto-scaling-delete-code-cli"></a>

To delete a scaling policy from a variant, use the [delete-scaling-policy](https://docs.aws.amazon.com/cli/latest/reference/application-autoscaling/delete-scaling-policy.html) command with the following parameters:
+ `--policy-name`—The name of the scaling policy.
+ `--resource-id`—The resource identifier for the variant. For this parameter, the resource type is `endpoint` and the unique identifier is the name of the variant. For example, `endpoint/{{my-endpoint}}/variant/{{my-variant}}`.
+ `--service-namespace`—Set this value to `sagemaker`.
+ `--scalable-dimension`—Set this value to `sagemaker:variant:DesiredInstanceCount`.

**Example**  
The following example deletes a target tracking scaling policy named `{{my-scaling-policy}}` from a variant named `{{my-variant}}`, running on the `{{my-endpoint}}` endpoint.  

```
aws application-autoscaling delete-scaling-policy \
  --policy-name {{my-scaling-policy}} \
  --resource-id endpoint/{{my-endpoint}}/variant/{{my-variant}} \
  --service-namespace sagemaker \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount
```

### Delete a scaling policy (Application Auto Scaling API)
<a name="endpoint-auto-scaling-delete-code-api"></a>

To delete a scaling policy from your variant, use the [DeleteScalingPolicy](https://docs.aws.amazon.com/autoscaling/application/APIReference/API_DeleteScalingPolicy.html) Application Auto Scaling API action with the following parameters:
+ `PolicyName`—The name of the scaling policy.
+ `ServiceNamespace`—Set this value to `sagemaker`.
+ `ResourceID`—The resource identifier for the variant. For this parameter, the resource type is `endpoint` and the unique identifier is the name of the variant. For example, `endpoint/{{my-endpoint}}/variant/{{my-variant}}`.
+ `ScalableDimension`—Set this value to `sagemaker:variant:DesiredInstanceCount`.

**Example**  
The following example deletes a target tracking scaling policy named `{{my-scaling-policy}}` from a variant named `{{my-variant}}`, running on the `{{my-endpoint}}` endpoint.  

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
    "PolicyName": "{{my-scaling-policy}}",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/{{my-endpoint}}/variant/{{my-variant}}",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount"
}
```