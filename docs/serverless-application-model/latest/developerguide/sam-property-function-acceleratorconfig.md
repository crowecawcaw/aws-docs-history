

# AcceleratorConfig

`AcceleratorConfig` is a property of `AWS::Serverless::Function` that configures accelerator resources, such as GPUs, for an AWS Lambda (Lambda) function that runs on Lambda Managed Instances. You specify the amount of accelerator memory that Lambda allocates to each execution environment of the function.

To use `AcceleratorConfig`, the function must also specify [CapacityProviderConfig](sam-resource-function.md#sam-function-capacityproviderconfig). Lambda supports accelerator configuration only for functions that use the `Image` package type and the `x86_64` architecture.

## Syntax
<a name="sam-property-function-acceleratorconfig-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-acceleratorconfig-syntax.yaml"></a>

```yaml
[AcceleratorMemorySize](#sam-function-acceleratorconfig-acceleratormemorysize): {{Integer}}
```

## Properties
<a name="sam-property-function-acceleratorconfig-properties"></a>

`AcceleratorConfig` has the following property.

 `AcceleratorMemorySize`   <a name="sam-function-acceleratorconfig-acceleratormemorysize"></a>
The amount of accelerator memory, in GiB, that Lambda allocates to each execution environment.  
*Valid values*: `3`, `6`, `12`, `16`, `24`, or `48`  
*Type*: Integer  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the [AcceleratorMemorySize](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-function-acceleratorconfig.html#cfn-lambda-function-acceleratorconfig-acceleratormemorysize) property of the `AWS::Lambda::Function` `AcceleratorConfig` data type.

## Examples
<a name="sam-property-function-acceleratorconfig--examples"></a>

### GPU function on a capacity provider
<a name="sam-property-function-acceleratorconfig--examples--gpufunction"></a>

The following example defines a container image function that requests 24 GiB of accelerator memory and runs on a capacity provider.

#### YAML
<a name="sam-property-function-acceleratorconfig--examples--gpufunction--yaml"></a>

```yaml
Resources:
  MyGpuFunction:
    Type: AWS::Serverless::Function
    Properties:
      PackageType: Image
      ImageUri: {{111122223333.dkr.ecr.us-east-1.amazonaws.com/my-gpu-image:latest}}
      Architectures:
        - x86_64
      MemorySize: 2048
      CapacityProviderConfig:
        Arn: !GetAtt {{MyCapacityProvider}}.Arn
      AcceleratorConfig:
        AcceleratorMemorySize: 24
```