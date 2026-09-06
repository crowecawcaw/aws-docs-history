

# ScalingConfig
<a name="sam-property-capacityprovider-scalingconfig"></a>

Configures how the capacity provider scales EC2 instances based on demand, including maximum instance limits and scaling policies.

## Syntax
<a name="sam-property-capacityprovider-scalingconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-capacityprovider-scalingconfig-syntax.yaml"></a>

```
[MaxVCpuCount](#sam-capacityprovider-scalingconfig-maxvcpucount): {{Integer}}
[AverageCPUUtilization](#sam-capacityprovider-scalingconfig-averagecpuutilization): {{Double}}
```

## Properties
<a name="sam-property-capacityprovider-scalingconfig-properties"></a>

 `MaxVCpuCount`   <a name="sam-capacityprovider-scalingconfig-maxvcpucount"></a>
The maximum number of vCPUs that the capacity provider can provision across all compute instances.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MaxVCpuCount](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderscalingconfig.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig-maxvcpucount)` property of `[CapacityProviderScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig)` of an `AWS::Lambda::CapacityProvider` resource. 

 `AverageCPUUtilization`   <a name="sam-capacityprovider-scalingconfig-averagecpuutilization"></a>
The target average CPU utilization percentage (0-100) for scaling decisions. When the average CPU utilization exceeds this threshold, the capacity provider will scale up Amazon EC2 instances. When specified, AWS SAM constructs `[CapacityProviderScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig)` of an `AWS::Lambda::CapacityProvider` resource with the `[ScalingMode](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderscalingconfig.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingmode)` set to `'Manual'` and `[ScalingPolicies](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-capacityproviderscalingconfig.html#cfn-lambda-capacityprovider-capacityproviderscalingconfig-scalingpolicies)` set to `[{PredefinedMetricType: 'LambdaCapacityProviderAverageCPUUtilization', TargetValue: <this value>}]`.   
*Type*: Double  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent. 

## Examples
<a name="sam-property-capacityprovider-scalingconfig-examples"></a>

### Scaling configuration
<a name="sam-property-capacityprovider-scalingconfig-examples-basic"></a>

The following example shows a scaling configuration with maximum VCpu count and average CPU utilization.

```
ScalingConfig:
  MaxVCpuCount: 10
  AverageCPUUtilization: 70.0
```