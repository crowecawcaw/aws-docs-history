# Register a model

Before you add a scaling policy to your model, you first must register your model for
auto scaling and define the scaling limits for the model.

The following procedures cover how to register a model (production variant) for auto
scaling using the AWS Command Line Interface (AWS CLI) or Application Auto Scaling API.

###### Topics

- [Register a model (AWS CLI)](#endpoint-auto-scaling-add-cli "#endpoint-auto-scaling-add-cli")
- [Register a model (Application Auto Scaling
  API)](#endpoint-auto-scaling-add-api "#endpoint-auto-scaling-add-api")

## Register a model (AWS CLI)

To register your production variant, use the [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command with the following parameters:

- `--service-namespace`—Set this value to
  `sagemaker`.
- `--resource-id`—The resource identifier for the model
  (specifically, the production variant). For this parameter, the resource
  type is `endpoint` and the unique identifier is the name of the
  production variant. For example,
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `--scalable-dimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.
- `--min-capacity`—The minimum number of instances. This
  value must be set to at least 1 and must be equal to or less than the value
  specified for `max-capacity`.
- `--max-capacity`—The maximum number of instances. This
  value must be set to at least 1 and must be equal to or greater than the
  value specified for `min-capacity`.

###### Example

The following example shows how to register a variant named
`my-variant`, running on the
`my-endpoint` endpoint, that can
be dynamically scaled to have one to eight instances.

```
aws application-autoscaling register-scalable-target \
  --service-namespace sagemaker \
  --resource-id endpoint/`my-endpoint`/variant/`my-variant` \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount \
  --min-capacity `1` \
  --max-capacity `8`
```

## Register a model (Application Auto Scaling

API)

To register your model with Application Auto Scaling, use the [RegisterScalableTarget](../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md "../../../autoscaling/application/APIReference/API_RegisterScalableTarget.md") Application Auto Scaling API action with the following
parameters:

- `ServiceNamespace`—Set this value to
  `sagemaker`.
- `ResourceID`—The resource identifier for the production
  variant. For this parameter, the resource type is `endpoint` and
  the unique identifier is the name of the variant. For example
  `endpoint/`my-endpoint`/variant/`my-variant``.
- `ScalableDimension`—Set this value to
  `sagemaker:variant:DesiredInstanceCount`.
- `MinCapacity`—The minimum number of instances. This
  value must be set to at least 1 and must be equal to or less than the value
  specified for `MaxCapacity`.
- `MaxCapacity`—The maximum number of instances. This
  value must be set to at least 1 and must be equal to or greater than the
  value specified for `MinCapacity`.

###### Example

The following example shows how to register a variant named
`my-variant`, running on the
`my-endpoint` endpoint, that can
be dynamically scaled to use one to eight instances.

```
POST / HTTP/1.1
Host: application-autoscaling.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AnyScaleFrontendService.RegisterScalableTarget
X-Amz-Date: 20230506T182145Z
User-Agent: aws-cli/2.0.0 Python/3.7.5 Windows/10 botocore/2.0.0dev4
Content-Type: application/x-amz-json-1.1
Authorization: AUTHPARAMS

{
    "ServiceNamespace": "sagemaker",
    "ResourceId": "endpoint/`my-endpoint`/variant/`my-variant`",
    "ScalableDimension": "sagemaker:variant:DesiredInstanceCount",
    "MinCapacity": `1`,
    "MaxCapacity": `8`
}
```
