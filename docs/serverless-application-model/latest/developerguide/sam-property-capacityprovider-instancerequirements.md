

# InstanceRequirements
<a name="sam-property-capacityprovider-instancerequirements"></a>

Specifies the requirements for EC2 instances that will be launched by the capacity provider, including architectures and instance type constraints.

## Syntax
<a name="sam-property-capacityprovider-instancerequirements-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-capacityprovider-instancerequirements-syntax.yaml"></a>

```
[Architectures](#sam-capacityprovider-instancerequirements-architectures): {{List}}
[AllowedTypes](#sam-capacityprovider-instancerequirements-allowedtypes): {{List}}
[ExcludedTypes](#sam-capacityprovider-instancerequirements-excludedtypes): {{List}}
```

**Note**  
You can choose to specify either `AllowedTypes` or `ExcludedTypes` when defining instance requirements for your capacity provider, but not both.

## Properties
<a name="sam-property-capacityprovider-instancerequirements-properties"></a>

 `Architectures`   <a name="sam-capacityprovider-instancerequirements-architectures"></a>
The instruction set architectures for the capacity provider instances.  
*Valid values*: `x86_64` or `arm64`  
*Type*: List  
*Required*: No  
*Default*: `x86_64`  
*CloudFormation compatibility*: This property is passed directly to the `[Architectures](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-instancerequirements.html#cfn-lambda-capacityprovider-instancerequirements-architectures)` property of `[InstanceRequirements](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-instancerequirements)` of an `AWS::Lambda::CapacityProvider` resource. 

 `AllowedTypes`   <a name="sam-capacityprovider-instancerequirements-allowedtypes"></a>
A list of allowed EC2 instance types for the capacity provider instance.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AllowedInstanceTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-instancerequirements.html#cfn-lambda-capacityprovider-instancerequirements-allowedinstancetypes)` property of `[InstanceRequirements](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-instancerequirements)` of an `AWS::Lambda::CapacityProvider` resource. 

 `ExcludedTypes`   <a name="sam-capacityprovider-instancerequirements-excludedtypes"></a>
A list of EC2 instance types to exclude from the capacity provider.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ExcludedInstanceTypes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-capacityprovider-instancerequirements.html#cfn-lambda-capacityprovider-instancerequirements-excludedinstancetypes)` property of `[InstanceRequirements](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-capacityprovider.html#cfn-lambda-capacityprovider-instancerequirements)` of an `AWS::Lambda::CapacityProvider` resource. 

## Examples
<a name="sam-property-capacityprovider-instancerequirements-examples"></a>

### Instance requirements configuration
<a name="sam-property-capacityprovider-instancerequirements-examples-basic"></a>

The following example shows instance requirements with specific architecture and instance type constraints.

```
InstanceRequirements:
  Architectures:
    - x86_64
  ExcludedTypes:
    - t2.micro
```