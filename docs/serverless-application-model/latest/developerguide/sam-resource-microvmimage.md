

# AWS::Serverless::MicrovmImage
<a name="sam-resource-microvmimage"></a>

 Creates a AWS Lambda MicroVM image from a code artifact stored in Amazon S3. A MicroVM image is a Firecracker snapshot built from a Dockerfile and application code, enabling sub-second startup for MicroVM instances. 

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md). 

## Syntax
<a name="sam-resource-microvmimage-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-microvmimage-syntax.yaml"></a>

```
Type: AWS::Serverless::MicrovmImage
Properties:
  [AdditionalOsCapabilities](#sam-microvmimage-additionaloscapabilities): {{List}}
  [BaseImageArn](#sam-microvmimage-baseimagearn): {{String}}
  [BaseImageVersion](#sam-microvmimage-baseimageversion): {{String}}
  [BuildRoleArn](#sam-microvmimage-buildrolearn): {{String}}
  [CodeUri](#sam-microvmimage-codeuri): {{String}}
  [CpuConfigurations](#sam-microvmimage-cpuconfigurations): {{List}}
  [Description](#sam-microvmimage-description): {{String}}
  [EgressNetworkConnectors](#sam-microvmimage-egressnetworkconnectors): {{List}}
  [EnvironmentVariables](#sam-microvmimage-environmentvariables): {{Map}}
  [Hooks](#sam-microvmimage-hooks): {{[Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html)}}
  [Logging](#sam-microvmimage-logging): {{[Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html)}}
  [Name](#sam-microvmimage-name): {{String}}
  [PropagateTags](#sam-microvmimage-propagatetags): {{Boolean}}
  [Resources](#sam-microvmimage-resources): {{List}}
  [Tags](#sam-microvmimage-tags): {{Map}}
```

## Properties
<a name="sam-resource-microvmimage-properties"></a>

 `AdditionalOsCapabilities`   <a name="sam-microvmimage-additionaloscapabilities"></a>
Additional OS capabilities to grant to the MicroVM runtime environment. If you don't specify a value, the service grants no additional OS capabilities.  
*Valid values*: `ALL`  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[AdditionalOsCapabilities](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-additionaloscapabilities)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `BaseImageArn`   <a name="sam-microvmimage-baseimagearn"></a>
The ARN of the base MicroVM image to build from.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[BaseImageArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-baseimagearn)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `BaseImageVersion`   <a name="sam-microvmimage-baseimageversion"></a>
The version of the base MicroVM image to use.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[BaseImageVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-baseimageversion)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `BuildRoleArn`   <a name="sam-microvmimage-buildrolearn"></a>
The ARN of the IAM role that the MicroVM build service assumes to download your code artifact from Amazon S3 and write build logs.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[BuildRoleArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-buildrolearn)` property of an `AWS::Lambda::MicrovmImage` resource. This is required in CloudFormation but not in AWS SAM. If you don't specify a role, AWS SAM creates one with a logical ID of `{{<resource-logical-id>}}BuildRole`. If your code artifact is encrypted with a customer managed key in AWS KMS, you must provide your own role with the appropriate `kms:Decrypt` permission. 

 `CodeUri`   <a name="sam-microvmimage-codeuri"></a>
The Amazon S3 URI of the zip artifact containing the Dockerfile and application code.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is transformed to the `[CodeArtifact](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-codeartifact)` property of an `AWS::Lambda::MicrovmImage` resource. AWS SAM wraps the URI into the `CodeArtifact.Uri` structure. 

 `CpuConfigurations`   <a name="sam-microvmimage-cpuconfigurations"></a>
A list of [CpuConfiguration](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.html) objects that specify the supported CPU architectures for the MicroVM. If you don't specify a value, the service uses the default CPU architecture.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CpuConfigurations](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-cpuconfigurations)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `Description`   <a name="sam-microvmimage-description"></a>
A description of the MicroVM image.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-description)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `EgressNetworkConnectors`   <a name="sam-microvmimage-egressnetworkconnectors"></a>
The list of egress network connector ARNs available to the MicroVM at runtime.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[EgressNetworkConnectors](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-egressnetworkconnectors)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `EnvironmentVariables`   <a name="sam-microvmimage-environmentvariables"></a>
Environment variables set in the MicroVM runtime environment.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[EnvironmentVariables](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-environmentvariables)` property of an `AWS::Lambda::MicrovmImage` resource. In AWS SAM, specify as a map (for example, `KEY: value`). AWS SAM converts to the CloudFormation array format `[{Key: KEY, Value: value}]`. 

 `Hooks`   <a name="sam-microvmimage-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.  
*Type*: [Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Hooks](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-hooks)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `Logging`   <a name="sam-microvmimage-logging"></a>
Configuration for MicroVM logging output. Specify exactly one: `CloudWatch` to enable CloudWatch logging, or `Disabled` to turn off logging.  
*Type*: [Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Logging](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-logging)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `Name`   <a name="sam-microvmimage-name"></a>
The name of the MicroVM image.  
*Type*: String  
*Required*: Yes  
*CloudFormation compatibility*: This property is passed directly to the `[Name](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-name)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `PropagateTags`   <a name="sam-microvmimage-propagatetags"></a>
Specifies whether to pass tags from the `Tags` property to generated resources, such as the auto-generated build role.  
*Type*: Boolean  
*Required*: No  
*Default*: `False`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Resources`   <a name="sam-microvmimage-resources"></a>
A list of [Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.html) objects that specify the resource requirements for the MicroVM.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-resources)` property of an `AWS::Lambda::MicrovmImage` resource. 

 `Tags`   <a name="sam-microvmimage-tags"></a>
A map of key-value pairs that specifies the tags added to this MicroVM image.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html#cfn-lambda-microvmimage-tags)` property of an `AWS::Lambda::MicrovmImage` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of `Tag` objects). Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this MicroVM image, and to the default roles that are generated for it. 

## Return Values
<a name="sam-resource-microvmimage-return-values"></a>

### Ref
<a name="sam-resource-microvmimage-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the ARN of the MicroVM image.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*.

### Fn::GetAtt
<a name="sam-resource-microvmimage-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) in the *AWS CloudFormation User Guide*.

`CreatedAt`  <a name="sam-microvmimage-getatt-createdat"></a>
The timestamp when the MicroVM image version was created.

`ImageArn`  <a name="sam-microvmimage-getatt-imagearn"></a>
The ARN of the MicroVM image.

`LatestActiveImageVersion`  <a name="sam-microvmimage-getatt-latestactiveimageversion"></a>
The latest active version of the MicroVM image.

`LatestFailedImageVersion`  <a name="sam-microvmimage-getatt-latestfailedimageversion"></a>
The latest failed version of the MicroVM image, if any.

`State`  <a name="sam-microvmimage-getatt-state"></a>
The current state of the MicroVM image.

`UpdatedAt`  <a name="sam-microvmimage-getatt-updatedat"></a>
The timestamp when the MicroVM image version was last updated.

## Examples
<a name="sam-resource-microvmimage-examples"></a>

### Minimal MicroVM image
<a name="sam-resource-microvmimage-example-minimal"></a>

The following example creates a MicroVM image with only the required properties. AWS SAM automatically generates a build role.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyMicroVM:
    Type: AWS::Serverless::MicrovmImage
    Properties:
      Name: my-app
      CodeUri: s3://my-bucket/app.zip
      BaseImageArn: arn:aws:lambda:us-east-2:aws:microvm-image:al2023-1
      BaseImageVersion: "0"
```

### Full MicroVM image configuration
<a name="sam-resource-microvmimage-example-full"></a>

The following example creates a MicroVM image with all available properties configured.

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  MyMicroVM:
    Type: AWS::Serverless::MicrovmImage
    Properties:
      Name: my-app
      CodeUri: s3://my-bucket/app.zip
      BaseImageArn: arn:aws:lambda:us-east-2:aws:microvm-image:al2023-1
      BaseImageVersion: "0"
      Description: "Production MicroVM application"
      CpuConfigurations:
        - Architecture: ARM_64
      Resources:
        - MinimumMemoryInMiB: 1024
      AdditionalOsCapabilities:
        - ALL
      EgressNetworkConnectors:
        - arn:aws:lambda:us-east-2:aws:network-connector:aws-network-connector:INTERNET_EGRESS
      Hooks:
        Port: 9000
        MicrovmHooks:
          Run: ENABLED
          RunTimeoutInSeconds: 30
          Suspend: ENABLED
          Resume: ENABLED
        MicrovmImageHooks:
          Ready: ENABLED
          ReadyTimeoutInSeconds: 60
      EnvironmentVariables:
        LOG_LEVEL: info
        APP_ENV: production
      Logging:
        CloudWatch:
          LogGroup: /aws/lambda-microvms/my-app
      Tags:
        Environment: Production
        Team: Platform
```