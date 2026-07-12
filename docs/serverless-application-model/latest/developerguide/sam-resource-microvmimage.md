# AWS::Serverless::MicrovmImage

Creates a AWS Lambda MicroVM image from a code artifact stored in Amazon S3. A MicroVM image is a
Firecracker snapshot built from a Dockerfile and application code, enabling sub-second
startup for MicroVM instances.

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation
resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::MicrovmImage
Properties:
  AdditionalOsCapabilities: `List`
  BaseImageArn: `String`
  BaseImageVersion: `String`
  BuildRoleArn: `String`
  CodeUri: `String`
  CpuConfigurations: `List`
  Description: `String`
  EgressNetworkConnectors: `List`
  EnvironmentVariables: `Map`
  Hooks: `Hooks`
  Logging: `Logging`
  Name: `String`
  PropagateTags: `Boolean`
  Resources: `List`
  Tags: `Map`

```

## Properties

`AdditionalOsCapabilities`

Additional OS capabilities to grant to the MicroVM runtime environment. If you don't specify a value, the service grants no additional OS capabilities.

_Valid values_: `ALL`

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`AdditionalOsCapabilities` property of an
`AWS::Lambda::MicrovmImage` resource.

`BaseImageArn`

The ARN of the base MicroVM image to build from.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`BaseImageArn` property of an
`AWS::Lambda::MicrovmImage` resource.

`BaseImageVersion`

The version of the base MicroVM image to use.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`BaseImageVersion` property of an
`AWS::Lambda::MicrovmImage` resource.

`BuildRoleArn`

The ARN of the IAM role that the MicroVM build service assumes to download your
code artifact from Amazon S3 and write build logs.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`BuildRoleArn` property of an
`AWS::Lambda::MicrovmImage` resource. This is required in CloudFormation
but not in AWS SAM. If you don't specify a role, AWS SAM creates one with a
logical ID of ``<resource-logical-id>`BuildRole`.
If your code artifact is encrypted with a customer managed key in AWS KMS, you must provide
your own role with the appropriate `kms:Decrypt` permission.

`CodeUri`

The Amazon S3 URI of the zip artifact containing the Dockerfile and application code.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is transformed to the
`CodeArtifact` property of an
`AWS::Lambda::MicrovmImage` resource. AWS SAM wraps the URI into the
`CodeArtifact.Uri` structure.

`CpuConfigurations`

A list of [CpuConfiguration](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-cpuconfiguration.md") objects that specify the supported CPU architectures
for the MicroVM. If you don't specify a value, the service uses the default CPU architecture.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`CpuConfigurations` property of an
`AWS::Lambda::MicrovmImage` resource.

`Description`

A description of the MicroVM image.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Description` property of an
`AWS::Lambda::MicrovmImage` resource.

`EgressNetworkConnectors`

The list of egress network connector ARNs available to the MicroVM at runtime.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`EgressNetworkConnectors` property of an
`AWS::Lambda::MicrovmImage` resource.

`EnvironmentVariables`

Environment variables set in the MicroVM runtime environment.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`EnvironmentVariables` property of an
`AWS::Lambda::MicrovmImage` resource. In AWS SAM, specify as a map
(for example, `KEY: value`). AWS SAM converts to the CloudFormation array format
`[{Key: KEY, Value: value}]`.

`Hooks`

Lifecycle hook configuration for MicroVMs and MicroVM images.

_Type_: [Hooks](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Hooks` property of an
`AWS::Lambda::MicrovmImage` resource.

`Logging`

Configuration for MicroVM logging output. Specify exactly one: `CloudWatch` to enable CloudWatch logging, or `Disabled` to turn off logging.

_Type_: [Logging](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-logging.md")

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Logging` property of an
`AWS::Lambda::MicrovmImage` resource.

`Name`

The name of the MicroVM image.

_Type_: String

_Required_: Yes

_CloudFormation compatibility_: This property is passed directly to the
`Name` property of an
`AWS::Lambda::MicrovmImage` resource.

`PropagateTags`

Specifies whether to pass tags from the `Tags` property to generated
resources, such as the auto-generated build role.

_Type_: Boolean

_Required_: No

_Default_: `False`

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

`Resources`

A list of [Resources](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.md "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-resources.md") objects that specify the resource requirements for the MicroVM.

_Type_: List

_Required_: No

_CloudFormation compatibility_: This property is passed directly to the
`Resources` property of an
`AWS::Lambda::MicrovmImage` resource.

`Tags`

A map of key-value pairs that specifies the tags added to this MicroVM image.

_Type_: Map

_Required_: No

_CloudFormation compatibility_: This property is similar to the
`Tags` property of an
`AWS::Lambda::MicrovmImage` resource. The `Tags` property
in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a
list of `Tag` objects). Also, AWS SAM automatically adds
a `lambda:createdBy:SAM` tag to this MicroVM image, and to the default roles
that are generated for it.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic
function, it returns the ARN of the MicroVM image.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The
following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`CreatedAt`

The timestamp when the MicroVM image version was created.

`ImageArn`

The ARN of the MicroVM image.

`LatestActiveImageVersion`

The latest active version of the MicroVM image.

`LatestFailedImageVersion`

The latest failed version of the MicroVM image, if any.

`State`

The current state of the MicroVM image.

`UpdatedAt`

The timestamp when the MicroVM image version was last updated.

## Examples

### Minimal MicroVM image

The following example creates a MicroVM image with only the required properties.
AWS SAM automatically generates a build role.

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
