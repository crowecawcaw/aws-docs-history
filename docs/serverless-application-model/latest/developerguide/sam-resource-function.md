# AWS::Serverless::Function

Creates an AWS Lambda function, an AWS Identity and Access Management (IAM) execution role, and event source
mappings that trigger the function.

The AWS::Serverless::Function resource
also supports the `Metadata` resource attribute, so you can instruct AWS SAM to build
custom runtimes that your application requires. For more information about building custom
runtimes, see [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md "building-custom-runtimes.md").

###### Note

When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into AWS CloudFormation resources.
For more information, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following
syntax.

### YAML

```
Type: AWS::Serverless::Function
Properties:
  Architectures: `List`
  AssumeRolePolicyDocument: `JSON`
  AutoPublishAlias: `String`
  AutoPublishAliasAllProperties: `Boolean`
  AutoPublishCodeSha256: `String`
  CodeSigningConfigArn: `String`
  CodeUri: `String | FunctionCode`
  DeadLetterQueue: `Map | DeadLetterQueue`
  DeploymentPreference: `DeploymentPreference`
  Description: `String`
  Environment: `Environment`
  EphemeralStorage: `EphemeralStorage`
  EventInvokeConfig: `EventInvokeConfiguration`
  Events: `EventSource`
  FileSystemConfigs: `List`
  FunctionName: `String`
  FunctionUrlConfig: `FunctionUrlConfig`
  Handler: `String`
  ImageConfig: `ImageConfig`
  ImageUri: `String`
  InlineCode: `String`
  KmsKeyArn: `String`
  Layers: `List`
  LoggingConfig: `LoggingConfig`
  MemorySize: `Integer`
  PackageType: `String`
  PermissionsBoundary: `String`
  Policies: `String | List | Map`
  PropagateTags: `Boolean`
  ProvisionedConcurrencyConfig: `ProvisionedConcurrencyConfig`
  RecursiveLoop: `String`
  ReservedConcurrentExecutions: `Integer`
  Role: `String`
  RolePath: `String`
  Runtime: `String`
  RuntimeManagementConfig: `RuntimeManagementConfig`
  SnapStart: `SnapStart`
  SourceKMSKeyArn: `String`
  Tags: `Map`
  Timeout: `Integer`
  Tracing: `String`
  VersionDescription: `String`
  VpcConfig: `VpcConfig`

```

## Properties

`Architectures`

The instruction set architecture for the function.

For more information about this property, see [Lambda instruction set architectures](../../../lambda/latest/dg/foundation-arch.md "../../../lambda/latest/dg/foundation-arch.md") in
the _AWS Lambda Developer Guide_.

_Valid values_: One of `x86_64` or
`arm64`

_Type_: List

_Required_: No

_Default_: `x86_64`

_AWS CloudFormation compatibility_: This property is passed directly to the
`Architectures` property of an `AWS::Lambda::Function`
resource.

`AssumeRolePolicyDocument`

Adds an AssumeRolePolicyDocument for the default created `Role` for this
function. If this property isn't specified, AWS SAM adds a default assume role for this
function.

_Type_: JSON

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`AssumeRolePolicyDocument` property of an `AWS::IAM::Role`
resource. AWS SAM adds this property to the generated IAM role for this function. If a
role's Amazon Resource Name (ARN) is provided for this function, this property does
nothing.

`AutoPublishAlias`

The name of the Lambda alias. For more information about Lambda aliases, see [Lambda function aliases](../../../lambda/latest/dg/configuration-aliases.md "../../../lambda/latest/dg/configuration-aliases.md") in the
_AWS Lambda Developer Guide_. For examples that use this
property, see [Deploying serverless applications
gradually with AWS SAM](automating-updates-to-serverless-apps.md "automating-updates-to-serverless-apps.md").

AWS SAM generates [AWS::Lambda::Version](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.md") and [AWS::Lambda::Alias](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md") resources when this property is set. For
information about this scenario, see [AutoPublishAlias property is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-autopublishalias "sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-autopublishalias"). For
general information about generated AWS CloudFormation resources, see [Generated AWS CloudFormation resources for AWS SAM](sam-specification-generated-resources.md "sam-specification-generated-resources.md").

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`AutoPublishAliasAllProperties`

Specifies when a new [`AWS::Lambda::Version`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.md") is created. When `true`, a new
Lambda version is created when any property in the Lambda function is modified. When
`false`, a new Lambda version is created only when any of the following
properties are modified:

- `Environment`, `MemorySize`, or
  `SnapStart`.
- Any change that results in an update to the `Code` property, such as
  `CodeDict`, `ImageUri`, or `InlineCode`.

This property requires `AutoPublishAlias` to be defined.

If `AutoPublishCodeSha256` is also specified, its behavior takes precedence
over `AutoPublishAliasAllProperties: true`.

_Type_: Boolean

_Required_: No

_Default value_: `false`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`AutoPublishCodeSha256`

When used, this string works with the `CodeUri` value to determine if a new Lambda version needs to be published.
This property is often used to resolve the following deployment issue: A deployment package is stored in an Amazon S3 location
and is replaced by a new deployment package with updated Lambda function code but the `CodeUri` property remains unchanged
(as opposed to the new deployment package being uploaded to a new Amazon S3 location and the `CodeUri`
being changed to the new location).

This problem is marked by an AWS SAM template having the following characteristics:

- The `DeploymentPreference` object is configured for gradual deployments (as described in [Deploying serverless applications
  gradually with AWS SAM](automating-updates-to-serverless-apps.md "automating-updates-to-serverless-apps.md"))
- The `AutoPublishAlias` property is set and doesn't change between deployments
- The `CodeUri` property is set and doesn't change between deployments.

In this scenario, updating `AutoPublishCodeSha256` results in a new Lambda version being created successfully.
However, new function code deployed to Amazon S3 will not be recognized. To recognize new function code, consider using versioning in your Amazon S3 bucket.
Specify the `Version` property for your Lambda function and configure your bucket to always use the latest deployment package.

In this scenario, to trigger the gradual deployment successfully, you must provide a unique value for `AutoPublishCodeSha256`.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`CodeSigningConfigArn`

The ARN of the [AWS::Lambda::CodeSigningConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.md") resource, used to enable code
signing for this function. For more information about code signing, see [Set up code signing for your AWS SAM application](authoring-codesigning.md "authoring-codesigning.md").

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`CodeSigningConfigArn` property of an
`AWS::Lambda::Function` resource.

`CodeUri`

The code for the function. Accepted values include:

- The function's Amazon S3 URI. For example, `s3://bucket-123456789/sam-app/1234567890abcdefg`.
- The local path to the function. For example, `hello_world/`.
- A [FunctionCode](sam-property-function-functioncode.md "sam-property-function-functioncode.md") object.

###### Note

If you provide a function's Amazon S3 URI or [FunctionCode](sam-property-function-functioncode.md "sam-property-function-functioncode.md") object,
you must reference a valid [Lambda deployment package](../../../lambda/latest/dg/gettingstarted-package.md "../../../lambda/latest/dg/gettingstarted-package.md").

If you provide a local file path, use the AWS SAM CLI to upload the local file at deployment. To learn more, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md "deploy-upload-local-files.md").

If you use intrinsic functions in `CodeUri` property, AWS SAM will not be able to correctly parse the values. Consider using
[AWS::LanguageExtensions transform](../../../AWSCloudFormation/latest/UserGuide/transform-aws-languageextensions.md "../../../AWSCloudFormation/latest/UserGuide/transform-aws-languageextensions.md") instead.

_Type_: [ String | [FunctionCode](sam-property-function-functioncode.md "sam-property-function-functioncode.md") ]

_Required_: Conditional. When `PackageType` is set to `Zip`, one of `CodeUri` or `InlineCode` is
required.

_AWS CloudFormation compatibility_: This property is similar to the `Code` property of an `AWS::Lambda::Function` resource. The nested Amazon S3 properties are named differently.

`DeadLetterQueue`

Configures an Amazon Simple Notification Service (Amazon SNS) topic or Amazon Simple Queue Service (Amazon SQS) queue where Lambda sends
events that it can't process. For more information about dead-letter queue
functionality, see [Dead-letter queues](../../../lambda/latest/dg/invocation-async-retain-records.md#invocation-dlq "../../../lambda/latest/dg/invocation-async-retain-records.md#invocation-dlq") in the _AWS Lambda Developer Guide_.

###### Note

If your Lambda function's event source is an Amazon SQS queue, configure a dead-letter
queue for the source queue, not for the Lambda function. The dead-letter queue that you
configure for a function is used for the function's [asynchronous invocation queue](../../../lambda/latest/dg/invocation-async.md "../../../lambda/latest/dg/invocation-async.md"), not
for event source queues.

_Type_: Map | [DeadLetterQueue](sam-property-function-deadletterqueue.md "sam-property-function-deadletterqueue.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`DeadLetterConfig` property of an `AWS::Lambda::Function`
resource. In AWS CloudFormation the type is derived from the `TargetArn`, whereas in AWS SAM
you must pass the type along with the `TargetArn`.

`DeploymentPreference`

The settings to enable gradual Lambda deployments.

If a `DeploymentPreference` object is specified, AWS SAM creates an [AWS::CodeDeploy::Application](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.md") called
`ServerlessDeploymentApplication` (one per stack), an [AWS::CodeDeploy::DeploymentGroup](../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.md") called
``<function-logical-id>`DeploymentGroup`,
 and an [AWS::IAM::Role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.md") called
 `CodeDeployServiceRole`.

_Type_: [DeploymentPreference](sam-property-function-deploymentpreference.md "sam-property-function-deploymentpreference.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

_See also_: For more information about this property, see [Deploying serverless applications
gradually with AWS SAM](automating-updates-to-serverless-apps.md "automating-updates-to-serverless-apps.md").

`Description`

A description of the function.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::Lambda::Function`
resource.

`Environment`

The configuration for the runtime environment.

_Type_: [Environment](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Environment` property of an `AWS::Lambda::Function`
resource.

`EphemeralStorage`

An object that specifies the disk space, in MB, available to your Lambda function in
`/tmp`.

For more information about this property, see [Lambda execution environment](../../../lambda/latest/dg/runtimes-context.md "../../../lambda/latest/dg/runtimes-context.md") in the
_AWS Lambda Developer Guide_.

_Type_: [EphemeralStorage](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-ephemeralstorage "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-ephemeralstorage")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`EphemeralStorage` property of an `AWS::Lambda::Function`
resource.

`EventInvokeConfig`

The object that describes event invoke configuration on a Lambda function.

_Type_: [EventInvokeConfiguration](sam-property-function-eventinvokeconfiguration.md "sam-property-function-eventinvokeconfiguration.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Events`

Specifies the events that trigger this function. Events consist of a type and a set
of properties that depend on the type.

_Type_: [EventSource](sam-property-function-eventsource.md "sam-property-function-eventsource.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`FileSystemConfigs`

List of [FileSystemConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.md") objects that specify the connection settings for an
Amazon Elastic File System (Amazon EFS) file system.

If your template contains an [AWS::EFS::MountTarget](../../../AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.md") resource, you must also specify a
`DependsOn` resource attribute to ensure that the mount target is created
or updated before the function.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FileSystemConfigs` property of an `AWS::Lambda::Function`
resource.

`FunctionName`

A name for the function. If you don't specify a name, a unique name is generated for
you.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`FunctionName` property of an `AWS::Lambda::Function`
resource.

`FunctionUrlConfig`

The object that describes a function URL. A function URL is an HTTPS endpoint that
you can use to invoke your function.

For more information, see [Function
URLs](../../../lambda/latest/dg/lambda-urls.md "../../../lambda/latest/dg/lambda-urls.md") in the _AWS Lambda Developer Guide_.

_Type_: [FunctionUrlConfig](sam-property-function-functionurlconfig.md "sam-property-function-functionurlconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`Handler`

The function within your code that is called to begin execution. This property is
only required if the `PackageType` property is set to
`Zip`.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`Handler` property of an `AWS::Lambda::Function`
resource.

`ImageConfig`

The object used to configure Lambda container image settings. For more information,
see [Using container images with
Lambda](../../../lambda/latest/dg/lambda-images.md "../../../lambda/latest/dg/lambda-images.md") in the _AWS Lambda Developer Guide_.

_Type_: [ImageConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-imageconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-imageconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ImageConfig` property of an `AWS::Lambda::Function`
resource.

`ImageUri`

The URI of the Amazon Elastic Container Registry (Amazon ECR) repository for the Lambda function's container
image. This property only applies if the `PackageType` property is set to
`Image`, otherwise it is ignored. For more information, see [Using container images with Lambda](../../../lambda/latest/dg/lambda-images.md "../../../lambda/latest/dg/lambda-images.md") in the
_AWS Lambda Developer Guide_.

###### Note

If the `PackageType` property is set to `Image`, then either
`ImageUri` is required, or you must build your application with necessary
`Metadata` entries in the AWS SAM template file. For more information, see
[Default build with AWS SAM](serverless-sam-cli-using-build.md "serverless-sam-cli-using-build.md").

Building your application with necessary `Metadata` entries takes
precedence over `ImageUri`, so if you specify both then `ImageUri`
is ignored.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ImageUri` property of the `AWS::Lambda::Function`
`Code` data type.

`InlineCode`

The Lambda function code that is written directly in the template. This property only
applies if the `PackageType` property is set to `Zip`, otherwise
it is ignored.

###### Note

If the `PackageType` property is set to `Zip` (default),
then one of `CodeUri` or `InlineCode` is required.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`ZipFile` property of the `AWS::Lambda::Function`
`Code` data type.

`KmsKeyArn`

The ARN of an AWS Key Management Service (AWS KMS) key that Lambda uses to encrypt and decrypt your
function's environment variables.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`KmsKeyArn` property of an `AWS::Lambda::Function`
resource.

`Layers`

The list of `LayerVersion` ARNs that this function should use. The order
specified here is the order in which they will be imported when running the Lambda
function. The version is either a full ARN including the version or a reference to a LayerVersion resource. For example, a reference to a `LayerVersion` will be `!Ref MyLayer`
while a full ARN including the version will be
`arn:aws:lambda:`region`:`account-id`:layer:`layer-name`:`version``.

_Type_: List

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Layers` property of an `AWS::Lambda::Function`
resource.

`LoggingConfig`

The function's Amazon CloudWatch Logs configuration settings.

_Type_: [LoggingConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-loggingconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-loggingconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
[`LoggingConfig`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-loggingconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.md#cfn-lambda-function-loggingconfig") property of an `AWS::Lambda::Function` resource.

`MemorySize`

The size of the memory in MB allocated per invocation of the function.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`MemorySize` property of an `AWS::Lambda::Function`
resource.

`PackageType`

The deployment package type of the Lambda function. For more information, see [Lambda deployment packages](../../../lambda/latest/dg/gettingstarted-package.md "../../../lambda/latest/dg/gettingstarted-package.md") in
the _AWS Lambda Developer Guide_.

**Notes**:

1. If this property is set to `Zip` (default), then either
   `CodeUri` or `InlineCode` applies, and `ImageUri` is
   ignored.

2. If this property is set to `Image`, then only `ImageUri`
   applies, and both `CodeUri` and `InlineCode` are ignored. The
   Amazon ECR repository required to store the function's container image can be auto created by
   the AWS SAM CLI. For more information, see [sam deploy](sam-cli-command-reference-sam-deploy.md "sam-cli-command-reference-sam-deploy.md").

_Valid values_: `Zip` or
`Image`

_Type_: String

_Required_: No

_Default_: `Zip`

_AWS CloudFormation compatibility_: This property is passed directly to the
`PackageType` property of an `AWS::Lambda::Function`
resource.

`PermissionsBoundary`

The ARN of a permissions boundary to use for this function's execution role. This
property works only if the role is generated for you.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`PermissionsBoundary` property of an `AWS::IAM::Role`
resource.

`Policies`

Permission policies for this function. Policies will be appended to the function's
default AWS Identity and Access Management (IAM) execution role.

This property accepts a single value or list of values. Allowed values
include:

- [AWS SAM policy templates](serverless-policy-templates.md "serverless-policy-templates.md").
- The ARN of an [AWS managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies").
- The name of an AWS managed policy from the following [list](https://github.com/aws/serverless-application-model/blob/develop/samtranslator/internal/data/aws_managed_policies.json "https://github.com/aws/serverless-application-model/blob/develop/samtranslator/internal/data/aws_managed_policies.json").
- An [inline IAM policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") formatted in YAML as a map.

###### Note

If you set the `Role` property, this property is ignored.

_Type_: String | List | Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Policies` property of an `AWS::IAM::Role` resource.

`PropagateTags`

Indicate whether or not to pass tags from the `Tags` property to your
[AWS::Serverless::Function](sam-specification-generated-resources-function.md "sam-specification-generated-resources-function.md") generated
resources. Specify `True` to propagate tags in your generated
resources.

_Type_: Boolean

_Required_: No

_Default_: `False`

_AWS CloudFormation compatibility_: This property is unique to AWS SAM and
doesn't have an AWS CloudFormation equivalent.

`ProvisionedConcurrencyConfig`

The provisioned concurrency configuration of a function's alias.

###### Note

`ProvisionedConcurrencyConfig` can be specified only if the
`AutoPublishAlias` is set. Otherwise, an error results.

_Type_: [ProvisionedConcurrencyConfig](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md#cfn-lambda-alias-provisionedconcurrencyconfig "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.md#cfn-lambda-alias-provisionedconcurrencyconfig")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ProvisionedConcurrencyConfig` property of an
`AWS::Lambda::Alias` resource.

`RecursiveLoop`

The status of your function's recursive loop detection configuration.

When this value is set to `Allow` and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.

When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RecursiveLoop`
property of the `AWS::Lambda::Function` resource.

`ReservedConcurrentExecutions`

The maximum number of concurrent executions that you want to reserve for the
function.

For more information about this property, see [Lambda Function Scaling](../../../lambda/latest/dg/scaling.md "../../../lambda/latest/dg/scaling.md") in the _AWS Lambda Developer Guide_.

_Type_: Integer

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`ReservedConcurrentExecutions` property of an
`AWS::Lambda::Function` resource.

`Role`

The ARN of an IAM role to use as this function's execution role.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Role` property of an `AWS::Lambda::Function` resource.
This is required in AWS CloudFormation but not in AWS SAM. If a role isn't specified, one is created
for you with a logical ID of
``<function-logical-id>`Role`.

`RolePath`

The path to the function's IAM execution role.

Use this property when the role is generated for you. Do not use when the role is
specified with the `Role` property.

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`Path` property of an `AWS::IAM::Role` resource.

`Runtime`

The identifier of the function's [runtime](../../../lambda/latest/dg/lambda-runtimes.md "../../../lambda/latest/dg/lambda-runtimes.md"). This property is only required if the `PackageType`
property is set to `Zip`.

###### Note

If you specify the `provided` identifier for this property, you can use
the `Metadata` resource attribute to instruct AWS SAM to build the custom
runtime that this function requires. For more information about building custom
runtimes, see [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md "building-custom-runtimes.md").

_Type_: String

_Required_: Conditional

_AWS CloudFormation compatibility_: This property is passed directly to the
`Runtime` property of an `AWS::Lambda::Function`
resource.

`RuntimeManagementConfig`

Configure runtime management options for your Lambda functions such as runtime
environment updates, rollback behavior, and selecting a specific runtime version. To
learn more, see [Lambda runtime updates](../../../lambda/latest/dg/runtimes-update.md "../../../lambda/latest/dg/runtimes-update.md") in the _AWS Lambda Developer Guide_.

_Type_: [RuntimeManagementConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`RuntimeManagementConfig` property of an
`AWS::Lambda::Function` resource.

`SnapStart`

Create a snapshot of any new Lambda function version. A snapshot is a cached state of
your initialized function, including all of its dependencies. The function is
initialized just once and the cached state is reused for all future invocations,
improving application performance by reducing the number of times your function must be
initialized. To learn more, see [Improving startup performance with Lambda
SnapStart](../../../lambda/latest/dg/snapstart.md "../../../lambda/latest/dg/snapstart.md") in the _AWS Lambda Developer Guide_.

_Type_: [SnapStart](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`SnapStart` property of an `AWS::Lambda::Function`
resource.

`SourceKmsKeyArn`

Represents a KMS key ARN that is used to encrypt the customer's ZIP function code.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`SourceKmsKeyArn` property of an `AWS::Lambda::Function` `Code` data type.

`Tags`

A map (string to string) that specifies the tags added to this function. For details
about valid keys and values for tags, see [Tag Key and
Value Requirements](../../../lambda/latest/dg/configuration-tags.md#configuration-tags-restrictions "../../../lambda/latest/dg/configuration-tags.md#configuration-tags-restrictions") in the _AWS Lambda Developer Guide_.

When the stack is created, AWS SAM automatically adds a
`lambda:createdBy:SAM` tag to this Lambda function, and to the default roles
that are generated for this function.

_Type_: Map

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the
`Tags` property of an `AWS::Lambda::Function` resource. The
`Tags` property in AWS SAM consists of key-value pairs (whereas in AWS CloudFormation this
property consists of a list of `Tag` objects). Also, AWS SAM automatically adds
a `lambda:createdBy:SAM` tag to this Lambda function, and to the default roles
that are generated for this function.

`Timeout`

The maximum time in seconds that the function can run before it is stopped.

_Type_: Integer

_Required_: No

_Default_: 3

_AWS CloudFormation compatibility_: This property is passed directly to the
`Timeout` property of an `AWS::Lambda::Function`
resource.

`Tracing`

The string that specifies the function's X-Ray tracing mode.

- `Active` – Activates X-Ray tracing for the function.
- `Disabled` – Deactivates X-Ray for the function.
- `PassThrough` – Activates X-Ray tracing for the function. Sampling decision is delegated
  to the downstream services.

If specified as `Active` or `PassThrough` and the `Role` property is not set,
AWS SAM adds the `arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess` policy to the Lambda execution role that
it creates for you.

For more information about X-Ray, see [Using AWS Lambda with
AWS X-Ray](../../../lambda/latest/dg/lambda-x-ray.md "../../../lambda/latest/dg/lambda-x-ray.md") in the _AWS Lambda Developer Guide_.

_Valid values_: [`Active`|`Disabled`|`PassThrough`]

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is similar to the `TracingConfig` property of an `AWS::Lambda::Function` resource.

`VersionDescription`

Specifies the `Description` field that is added on the new Lambda version
resource.

_Type_: String

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`Description` property of an `AWS::Lambda::Version`
resource.

`VpcConfig`

The configuration that enables this function to access private resources within your
virtual private cloud (VPC).

_Type_: [VpcConfig](../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.md")

_Required_: No

_AWS CloudFormation compatibility_: This property is passed directly to the
`VpcConfig` property of an `AWS::Lambda::Function`
resource.

## Return Values

### Ref

When the logical ID of this resource is provided to the `Ref` intrinsic
function, it returns the resource name of the underlying Lambda function.

For more information about using the `Ref` function, see [`Ref`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.md") in the _AWS CloudFormation User Guide_.

### Fn::GetAtt

`Fn::GetAtt` returns a value for a specified attribute of this type. The
following are the available attributes and sample return values.

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md "../../../AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.md") in the _AWS CloudFormation User Guide_.

`Arn`

The ARN of the underlying Lambda function.

## Examples

### Simple function

The following is a basic example of an [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md") resource of package type `Zip`
(default) and function code in an Amazon S3 bucket.

#### YAML

```
Type: AWS::Serverless::Function
Properties:
  Handler: index.handler
  Runtime: python3.9
  CodeUri: s3://`bucket-name`/`key-name`

```

### Function

properties example

The following is an example of an [AWS::Serverless::Function](sam-resource-function.md "sam-resource-function.md") of package type `Zip` (default) that
uses `InlineCode`, `Layers`, `Tracing`,
`Policies`, `Amazon EFS`, and an `Api` event source.

#### YAML

```
Type: AWS::Serverless::Function
DependsOn: MyMountTarget        # This is needed if an AWS::EFS::MountTarget resource is declared for EFS
Properties:
  Handler: index.handler
  Runtime: python3.9
  InlineCode: |
    def handler(event, context):
      print("Hello, world!")
  ReservedConcurrentExecutions: 30
  Layers:
    - Ref: MyLayer
  Tracing: Active
  Timeout: 120
  FileSystemConfigs:
    - Arn: !Ref MyEfsFileSystem
      LocalMountPath: /mnt/EFS
  Policies:
    - AWSLambdaExecute
    - Version: '2012-10-17		 	 	 '
      Statement:
        - Effect: Allow
          Action:
            - s3:GetObject
            - s3:GetObjectACL
          Resource: 'arn:aws:s3:::`sam-s3-demo-bucket`/*'
  Events:
    ApiEvent:
      Type: Api
      Properties:
        Path: /path
        Method: get

```

### ImageConfig

example

The following is an example of an `ImageConfig` for a Lambda function of
package type `Image`.

#### YAML

```
HelloWorldFunction:
  Type: AWS::Serverless::Function
  Properties:
    PackageType: Image
    ImageUri: `account-id`.dkr.ecr.`region`.amazonaws.com/`ecr-repo-name`:`image-name`
    ImageConfig:
      Command:
        - "`app.lambda_handler`"
      EntryPoint:
        - "`entrypoint1`"
      WorkingDirectory: "`workDir`"

```

###

RuntimeManagementConfig examples

A Lambda function configured to update its runtime environment according to current
behavior:

```
TestFunction
  Type: AWS::Serverless::Function
  Properties:
    ...
    Runtime: python3.9
    RuntimeManagementConfig:
      UpdateRuntimeOn: Auto
```

A Lambda function configured to update its runtime environment when the function is
updated:

```
TestFunction
  Type: AWS::Serverless::Function
  Properties:
    ...
    Runtime: python3.9
    RuntimeManagementConfig:
      UpdateRuntimeOn: FunctionUpdate
```

A Lambda function configured to update its runtime environment manually:

```
TestFunction
  Type: AWS::Serverless::Function
  Properties:
    ...
    Runtime: python3.9
    RuntimeManagementConfig:
      RuntimeVersionArn: arn:aws:lambda:us-east-1::runtime:4c459dd0104ee29ec65dcad056c0b3ddbe20d6db76b265ade7eda9a066859b1e
      UpdateRuntimeOn: Manual
```

### SnapStart

examples

Example of a Lambda function with SnapStart turned on for future versions:

```
TestFunc
  Type: AWS::Serverless::Function
  Properties:
    ...
    SnapStart:
      ApplyOn: PublishedVersions
```
