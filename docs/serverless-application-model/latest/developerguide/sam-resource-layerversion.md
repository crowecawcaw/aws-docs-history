

# AWS::Serverless::LayerVersion
<a name="sam-resource-layerversion"></a>

Creates a Lambda LayerVersion that contains library or runtime code needed by a Lambda Function.

The [AWS::Serverless::LayerVersion](#sam-resource-layerversion) resource also supports the `Metadata` resource attribute, so you can instruct AWS SAM to build layers included in your application. For more information about building layers, see [Building Lambda layers in AWS SAM](building-layers.md).

**Important Note**: Since the release of the [UpdateReplacePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) resource attribute in CloudFormation, [AWS::Lambda::LayerVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html) (recommended) offers the same benefits as [AWS::Serverless::LayerVersion](#sam-resource-layerversion).

When a Serverless LayerVersion is transformed, SAM also transforms the logical id of the resource so that old LayerVersions are not automatically deleted by CloudFormation when the resource is updated.

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).

## Syntax
<a name="sam-resource-layerversion-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-layerversion-syntax.yaml"></a>

```
Type: AWS::Serverless::LayerVersion
Properties:
  [CompatibleArchitectures](#sam-layerversion-compatiblearchitectures): {{List}}
  [CompatibleRuntimes](#sam-layerversion-compatibleruntimes): {{List}}
  [ContentUri](#sam-layerversion-contenturi): {{String | LayerContent}}
  [Description](#sam-layerversion-description): {{String}}
  [LayerName](#sam-layerversion-layername): {{String}}
  [LicenseInfo](#sam-layerversion-licenseinfo): {{String}}
  [PublishLambdaVersion](#sam-layerversion-PublishLambdaVersion): {{Boolean}}
  [RetentionPolicy](#sam-layerversion-retentionpolicy): {{String}}
```

## Properties
<a name="sam-resource-layerversion-properties"></a>

 `CompatibleArchitectures`   <a name="sam-layerversion-compatiblearchitectures"></a>
Specifies the supported instruction set architectures for the layer version.  
For more information about this property, see [Lambda instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) in the *AWS Lambda Developer Guide*.  
*Valid values*: `x86_64`, `arm64`  
*Type*: List  
*Required*: No  
*Default*: `x86_64`  
*CloudFormation compatibility*: This property is passed directly to the `[CompatibleArchitectures](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatiblearchitectures)` property of an `AWS::Lambda::LayerVersion` resource.

 `CompatibleRuntimes`   <a name="sam-layerversion-compatibleruntimes"></a>
List of runtimes compatible with this LayerVersion.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CompatibleRuntimes](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-compatibleruntimes)` property of an `AWS::Lambda::LayerVersion` resource.

 `ContentUri`   <a name="sam-layerversion-contenturi"></a>
Amazon S3 Uri, path to local folder, or LayerContent object of the layer code.  
If an Amazon S3 Uri or LayerContent object is provided, The Amazon S3 object referenced must be a valid ZIP archive that contains the contents of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).  
If a path to a local folder is provided, for the content to be transformed properly the template must go through the workflow that includes [sam build](sam-cli-command-reference-sam-build.md) followed by either [sam deploy](sam-cli-command-reference-sam-deploy.md) or [sam package](sam-cli-command-reference-sam-package.md). By default, relative paths are resolved with respect to the AWS SAM template's location.  
*Type*: String \| [LayerContent](sam-property-layerversion-layercontent.md)  
*Required*: Yes  
*CloudFormation compatibility*: This property is similar to the `[Content](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-content)` property of an `AWS::Lambda::LayerVersion` resource. The nested Amazon S3 properties are named differently.

 `Description`   <a name="sam-layerversion-description"></a>
Description of this layer.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-description)` property of an `AWS::Lambda::LayerVersion` resource.

 `LayerName`   <a name="sam-layerversion-layername"></a>
The name or Amazon Resource Name (ARN) of the layer.  
*Type*: String  
*Required*: No  
*Default*: Resource logical id  
*CloudFormation compatibility*: This property is similar to the `[LayerName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-layername)` property of an `AWS::Lambda::LayerVersion` resource. If you don't specify a name, the logical id of the resource will be used as the name.

 `LicenseInfo`   <a name="sam-layerversion-licenseinfo"></a>
Information about the license for this LayerVersion.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[LicenseInfo](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html#cfn-lambda-layerversion-licenseinfo)` property of an `AWS::Lambda::LayerVersion` resource.

 `PublishLambdaVersion`   <a name="sam-layerversion-PublishLambdaVersion"></a>
An opt-in property that creates a new Lambda version whenever there is a change in the referenced `LayerVersion` resource. When enabled with `AutoPublishAlias` and `AutoPublishAliasAllProperties` in the connected Lambda function, there will be a new Lambda version created for every change made to the `LayerVersion` resource.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `RetentionPolicy`   <a name="sam-layerversion-retentionpolicy"></a>
This property specifies whether old versions of your `LayerVersion` are retained or deleted when you delete a resource. If you need to retain old versions of your `LayerVersion` when updating or replacing a resource, you must have the `UpdateReplacePolicy` attribute enabled. For information on doing this, refer to [`UpdateReplacePolicy` attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.html) in the *AWS CloudFormation User Guide*.  
*Valid values*: `Retain` or `Delete`  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.  
*Additional notes*: When you specify `Retain`, AWS SAM adds a [Resource attributes supported by AWS SAM](sam-specification-resource-attributes.md) of `DeletionPolicy: Retain` to the transformed `AWS::Lambda::LayerVersion` resource.

## Return Values
<a name="sam-resource-layerversion-return-values"></a>

### Ref
<a name="sam-resource-layerversion-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the resource ARN of the underlying Lambda LayerVersion.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*. 

## Examples
<a name="sam-resource-layerversion--examples"></a>

### LayerVersionExample
<a name="sam-resource-layerversion--examples--layerversionexample"></a>

Example of a LayerVersion

#### YAML
<a name="sam-resource-layerversion--examples--layerversionexample--yaml"></a>

```
Properties:
  LayerName: MyLayer
  Description: Layer description
  ContentUri: 's3://sam-s3-demo-bucket/my-layer.zip'
  CompatibleRuntimes:
    - nodejs10.x
    - nodejs12.x
  LicenseInfo: 'Available under the MIT-0 license.'
  RetentionPolicy: Retain
```