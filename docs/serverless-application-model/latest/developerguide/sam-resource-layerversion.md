# AWS::Serverless::LayerVersion

Creates a Lambda LayerVersion that contains library or runtime code needed by a Lambda Function.

The AWS::Serverless::LayerVersion resource also supports the `Metadata` resource attribute, so you can instruct AWS SAM to build layers included in your application. For more information about building layers, see [Building Lambda layers in AWS SAM](building-layers.md "building-layers.md").

**Important Note**: Since the release of the [UpdateReplacePolicy](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md") resource attribute in AWS CloudFormation, [AWS::Lambda::LayerVersion](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.md") (recommended) offers the same benefits as AWS::Serverless::LayerVersion.

When a Serverless LayerVersion is transformed, SAM also transforms the logical id of the resource so that old LayerVersions are not automatically deleted by CloudFormation when the resource is updated.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources. For more information,
see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
Type: AWS::Serverless::LayerVersion
Properties:
  CompatibleArchitectures: `List`
  CompatibleRuntimes: `List`
  ContentUri: `String | LayerContent`
  Description: `String`
  LayerName: `String`
  LicenseInfo: `String`
  PublishLambdaVersion: `Boolean`
  RetentionPolicy: `String`

```

## Properties

`CompatibleArchitectures`

Specifies the supported instruction set architectures for the layer version.

For more information about this property, see [Lambda instruction set architectures](../../../lambda/latest/dg/foundation-arch.md "../../../lambda/latest/dg/foundation-arch.md") in the _AWS Lambda Developer Guide_.

_Valid values_: `x86_64`, `arm64`

_Type_: List

_Required_: No

_Default_: `x86_64`

_AWS CloudFormation compatibility_: This property is passed directly to the `CompatibleArchitectures` property of an `AWS::Lambda::LayerVersion` resource.

`CompatibleRuntimes`

List of runtimes compatible with this LayerVersion.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `CompatibleRuntimes` property of an `AWS::Lambda::LayerVersion` resource.

`ContentUri`

Amazon S3 Uri, path to local folder, or LayerContent object of the layer code.

If an Amazon S3 Uri or LayerContent object is provided, The Amazon S3 object referenced must be a valid ZIP archive that contains the contents of an [Lambda layer](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md").

If a path to a local folder is provided, for the content to be transformed properly the template must go through the workflow that includes [sam build](sam-cli-command-reference-sam-build.md "sam-cli-command-reference-sam-build.md") followed by either [sam deploy](sam-cli-command-reference-sam-deploy.md "sam-cli-command-reference-sam-deploy.md") or [sam package](sam-cli-command-reference-sam-package.md "sam-cli-command-reference-sam-package.md"). By default, relative paths are resolved with respect to the AWS SAM template's location.

_Type_: String | [LayerContent](sam-property-layerversion-layercontent.md "sam-property-layerversion-layercontent.md")

_Required_: Yes

_AWS CloudFormation compatibility_: This property is similar to the `Content` property of an `AWS::Lambda::LayerVersion` resource. The nested Amazon S3 properties are named differently.

`Description`

Description of this layer.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `Description` property of an `AWS::Lambda::LayerVersion` resource.

`LayerName`

The name or Amazon Resource Name (ARN) of the layer.

_Type_: String

_Required_: No

_Default_: Resource logical id

_AWS CloudFormation compatibility_: This property is similar to the `LayerName` property of an `AWS::Lambda::LayerVersion` resource. If you don't specify a name, the logical id of the resource will be used as the name.

`LicenseInfo`

Information about the license for this LayerVersion.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the `LicenseInfo` property of an `AWS::Lambda::LayerVersion` resource.

`PublishLambdaVersion`

An opt-in property that creates a new Lambda version whenever there is a change in the referenced `LayerVersion` resource. When enabled with `AutoPublishAlias` and `AutoPublishAliasAllProperties` in the connected Lambda function,
there will be a new Lambda version created for every change made to the `LayerVersion` resource.

_Type_: Boolean

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

`RetentionPolicy`

This property specifies whether old versions of your `LayerVersion` are retained or deleted when you delete a resource.
If you need to retain old versions of your `LayerVersion` when updating or replacing a resource, you must have the `UpdateReplacePolicy` attribute enabled.
For information on doing this, refer to [`UpdateReplacePolicy` attribute](../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md "../../../AWSCloudFormation/latest/UserGuide/aws-attribute-updatereplacepolicy.md")
in the _AWS CloudFormation User Guide_.

_Valid values_: `Retain` or `Delete`

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an AWS CloudFormation equivalent.

_Additional notes_: When you specify `Retain`, AWS SAM adds a [Resource attributes supported by AWS SAM](sam-specification-resource-attributes.md "sam-specification-resource-attributes.md") of `DeletionPolicy: Retain` to the transformed `AWS::Lambda::LayerVersion` resource.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the resource ARN of the underlying Lambda LayerVersion.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

## Examples

### LayerVersionExample

Example of a LayerVersion

#### YAML

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
