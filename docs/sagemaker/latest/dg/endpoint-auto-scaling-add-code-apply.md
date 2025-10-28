# Apply a scaling policy

After you register your model and define a scaling policy, apply the scaling policy to
the registered model. This section shows how to apply a scaling policy using the the
AWS Command Line Interface (AWS CLI) or the Application Auto Scaling API.

###### Topics

- [Apply a target tracking
  scaling policy (AWS CLI)](#endpoint-auto-scaling-add-code-apply-cli "#endpoint-auto-scaling-add-code-apply-cli")
- [Apply a scaling policy
  (Application Auto Scaling API)](#endpoint-auto-scaling-add-code-apply-api "#endpoint-auto-scaling-add-code-apply-api")

## Apply a target tracking

scaling policy (AWS CLI)

To apply a scaling policy to your model, use the [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") AWS CLI command with the following parameters:

- `--policy-name`—The name of the scaling policy.
- `--policy-type`—Set this value to
  `TargetTrackingScaling`.
- `--resource-id`—The resource identifier for the variant.
  For this parameter, the resource type is `endpoint` and the
  unique identifier is the name of the variant. For example,
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `--service-namespace`—Set this value to
  `sagemaker`.
- `--scalable-dimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.
- `--target-tracking-scaling-policy-configuration`—The
  target-tracking scaling policy configuration to use for the model.

The following example applies a target tracking scaling policy named
`my-scaling-policy` to a variant
named `my-variant`, running on the
`my-endpoint` endpoint. For the
`--target-tracking-scaling-policy-configuration` option, specify
the `config.json` file that you created previously.

```
aws application-autoscaling put-scaling-policy \
  --policy-name `my-scaling-policy` \
  --policy-type TargetTrackingScaling \
  --resource-id endpoint/`my-endpoint`/variant/`my-variant` \
  --service-namespace sagemaker \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount \
  --target-tracking-scaling-policy-configuration file://config.json
```

## Apply a scaling policy

(Application Auto Scaling API)

To apply a scaling policy to a variant with the Application Auto Scaling API, use the [PutScalingPolicy](../../../autoscaling/application/APIReference/API_PutScalingPolicy.md "../../../autoscaling/application/APIReference/API_PutScalingPolicy.md") Application Auto Scaling API action with the following
parameters:

- `PolicyName`—The name of the scaling policy.
- `ServiceNamespace`—Set this value to
  `sagemaker`.
- `ResourceID`—The resource identifier for the variant.
  For this parameter, the resource type is `endpoint` and the
  unique identifier is the name of the variant. For example,
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `ScalableDimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.
- `PolicyType`—Set this value to
  `TargetTrackingScaling`.
- `TargetTrackingScalingPolicyConfiguration`—The
  target-tracking scaling policy configuration to use for the variant.

The following example applies a target tracking scaling policy named
`my-scaling-policy` to a variant
named `my-variant`, running on the
`my-endpoint` endpoint. The policy
configuration keeps the average invocations per instance at 70.

```
POST / HTTP/1.1
Host: application-autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AnyScaleFrontendService.
X-Amz-Date: 20230506T182145Z
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "PolicyName": "`my-scaling-policy`",
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/`my-endpoint`/variant/`my-variant`",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount",
    "PolicyType": "TargetTrackingScaling",
    "TargetTrackingScalingPolicyConfiguration": {
        "TargetValue": `70.0`,
        "PredefinedMetricSpecification":
        {
            "PredefinedMetricType": "SageMakerVariantInvocationsPerInstance"
        }
    }
}
```
