# ScalingConfig

Configures how the capacity provider scales EC2 instances based on demand, including maximum instance limits and scaling policies.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
MaxVCpuCount: `Integer`
AverageCPUUtilization: `Double`
```

## Properties

`MaxVCpuCount`

The maximum number of vCPUs that the capacity provider can provision across all compute
instances.

_Type_: Integer

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`MaxVCpuCount` property of
`CapacityProviderScalingConfig` of an `AWS::Lambda::CapacityProvider` resource.

`AverageCPUUtilization`

The target average CPU utilization percentage (0-100) for scaling decisions. When the average CPU utilization exceeds this threshold, the capacity provider will scale up Amazon EC2 instances. When specified, AWS SAM constructs
`CapacityProviderScalingConfig` of an
`AWS::Lambda::CapacityProvider` resource with the
`ScalingMode` set to `'Manual'` and
`ScalingPolicies` set to
`[{PredefinedMetricType: 'LambdaCapacityProviderAverageCPUUtilization', TargetValue: <this value>}]`.

_Type_: Double

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### Scaling configuration

The following example shows a scaling configuration with maximum VCpu count and average CPU utilization.

```
ScalingConfig:
  MaxVCpuCount: 10
  AverageCPUUtilization: 70.0
```
