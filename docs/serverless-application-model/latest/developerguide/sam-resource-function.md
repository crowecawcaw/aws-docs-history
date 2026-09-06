

# AWS::Serverless::Function
<a name="sam-resource-function"></a>

Creates an AWS Lambda function, an AWS Identity and Access Management (IAM) execution role, and event source mappings that trigger the function.

The [AWS::Serverless::Function](#sam-resource-function) resource also supports the `Metadata` resource attribute, so you can instruct AWS SAM to build custom runtimes that your application requires. For more information about building custom runtimes, see [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md).

**Note**  
When you deploy to AWS CloudFormation, AWS SAM transforms your AWS SAM resources into CloudFormation resources. For more information, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).

## Syntax
<a name="sam-resource-function-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-resource-function-syntax.yaml"></a>

```
Type: AWS::Serverless::Function
Properties:
  [Architectures](#sam-function-architectures): {{List}}
  [AssumeRolePolicyDocument](#sam-function-assumerolepolicydocument): {{JSON}}
  [AutoPublishAlias](#sam-function-autopublishalias): {{String}}
  AutoPublishAliasAllProperties: {{Boolean}}
  [AutoPublishCodeSha256](#sam-function-autopublishcodesha256): {{String}}
  [CapacityProviderConfig](#sam-function-capacityproviderconfig): {{CapacityProviderConfig}}
  [CodeSigningConfigArn](#sam-function-codesigningconfigarn): {{String}}
  [CodeUri](#sam-function-codeuri): {{String | FunctionCode}}
  [DeadLetterQueue](#sam-function-deadletterqueue): {{Map | DeadLetterQueue}}
  [DeploymentPreference](#sam-function-deploymentpreference): {{DeploymentPreference}}
  [Description](#sam-function-description): {{String}}
  [DurableConfig](#sam-function-durableconfig): {{DurableConfig}}
  [Environment](#sam-function-environment): {{[Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html)}}
  [EphemeralStorage](#sam-function-ephemeralstorage): {{[EphemeralStorage](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage)}}
  [EventInvokeConfig](#sam-function-eventinvokeconfig): {{EventInvokeConfiguration}}
  [Events](#sam-function-events): {{EventSource}}
  [FileSystemConfigs](#sam-function-filesystemconfigs): {{List}}
  [FunctionName](#sam-function-functionname): {{String}}
  [FunctionScalingConfig](#sam-function-functionscalingconfig): {{FunctionScalingConfig}}
  [FunctionUrlConfig](#sam-function-functionurlconfig): {{FunctionUrlConfig}}
  [Handler](#sam-function-handler): {{String}}
  [ImageConfig](#sam-function-imageconfig): {{[ImageConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig)}}
  [ImageUri](#sam-function-imageuri): {{String}}
  [InlineCode](#sam-function-inlinecode): {{String}}
  [KmsKeyArn](#sam-function-kmskeyarn): {{String}}
  [Layers](#sam-function-layers): {{List}}
  LoggingConfig: {{[LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-loggingconfig.html)}}
  [MemorySize](#sam-function-memorysize): {{Integer}}
  [PackageType](#sam-function-packagetype): {{String}}
  [PermissionsBoundary](#sam-function-permissionsboundary): {{String}}
  [Policies](#sam-function-policies): {{String | List | Map}}
  [PublishToLatestPublished](#sam-function-publishtolatestpublished): {{Boolean}}
  PropagateTags: {{Boolean}}
  [ProvisionedConcurrencyConfig](#sam-function-provisionedconcurrencyconfig): {{[ProvisionedConcurrencyConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig)}}
  RecursiveLoop: {{String}}
  [ReservedConcurrentExecutions](#sam-function-reservedconcurrentexecutions): {{Integer}}
  [Role](#sam-function-role): {{String}}
  [RolePath](#sam-function-rolepath): {{String}}
  [Runtime](#sam-function-runtime): {{String}}
  RuntimeManagementConfig: {{[RuntimeManagementConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html)}}
  SnapStart: {{[SnapStart](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html)}}
  [SourceKMSKeyArn](#sam-function-sourcekmskeyarn): {{String}}
  [Tags](#sam-function-tags): {{Map}}
  [TenancyConfig](#sam-function-tenancyconfig): {{TenancyConfig}}
  [Timeout](#sam-function-timeout): {{Integer}}
  [Tracing](#sam-function-tracing): {{String}}
  [VersionDescription](#sam-function-versiondescription): {{String}}
  [VersionDeletionPolicy](#sam-function-versiondeletionpolicy): {{String}}
  [VpcConfig](#sam-function-vpcconfig): {{[VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html)}}
```

## Properties
<a name="sam-resource-function-properties"></a>

 `Architectures`   <a name="sam-function-architectures"></a>
The instruction set architecture for the function.  
For more information about this property, see [Lambda instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html) in the *AWS Lambda Developer Guide*.  
*Valid values*: One of `x86_64` or `arm64`  
*Type*: List  
*Required*: No  
*Default*: `x86_64`  
*CloudFormation compatibility*: This property is passed directly to the `[Architectures](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-architectures)` property of an `AWS::Lambda::Function` resource.

 `AssumeRolePolicyDocument`   <a name="sam-function-assumerolepolicydocument"></a>
Adds an AssumeRolePolicyDocument for the default created `Role` for this function. If this property isn't specified, AWS SAM adds a default assume role for this function.  
*Type*: JSON  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[AssumeRolePolicyDocument](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-assumerolepolicydocument)` property of an `AWS::IAM::Role` resource. AWS SAM adds this property to the generated IAM role for this function. If a role's Amazon Resource Name (ARN) is provided for this function, this property does nothing.

 `AutoPublishAlias`   <a name="sam-function-autopublishalias"></a>
The name of the Lambda alias. For more information about Lambda aliases, see [Lambda function aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) in the *AWS Lambda Developer Guide*. For examples that use this property, see [Deploying serverless applications gradually with AWS SAM](automating-updates-to-serverless-apps.md).  
AWS SAM generates [AWS::Lambda::Version](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html) and [AWS::Lambda::Alias](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html) resources when this property is set. For information about this scenario, see [AutoPublishAlias property is specified](sam-specification-generated-resources-function.md#sam-specification-generated-resources-function-autopublishalias). For general information about generated CloudFormation resources, see [Generated CloudFormation resources for AWS SAM](sam-specification-generated-resources.md).  
**Version publishing and intrinsic functions**  
AWS SAM determines whether to publish a new version by comparing property values in the template between deployments. For values supplied through intrinsic functions, AWS SAM compares the unresolved reference, not the resolved value. One example is an environment variable set to `!Ref` of a template parameter.  
If a deployment changes only the value of a stack parameter, the template itself is unchanged. In this case, AWS SAM does not publish a new version or update the alias. AWS SAM applies the change to the function's `$LATEST` version only. For workarounds, see example using [AWS::LanguageExtensions](#sam-function-autopublishaliasallproperties).
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AutoPublishAliasAllProperties`   <a name="sam-function-autopublishaliasallproperties"></a>
Specifies when a new [`AWS::Lambda::Version`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html) is created. When `true`, a new Lambda version is created when any property in the Lambda function is modified. When `false`, a new Lambda version is created only when any of the following properties are modified:  
+ `Environment`, `MemorySize`, or `SnapStart`.
+ Any change that results in an update to the `Code` property, such as `CodeDict`, `ImageUri`, or `InlineCode`.
**Parameter changes and version publishing**  
AWS SAM publishes a new version only when a property's value changes in the template. If a property value comes from an intrinsic function, AWS SAM sees the unresolved reference. One example is an environment variable defined as `!Ref` of a template parameter. Deployments that change only the parameter's value do not publish a new version, even with `AutoPublishAliasAllProperties: true`. AWS SAM applies the change to `$LATEST` only.
Use one of the following workarounds to force AWS SAM to publish a new version when only a parameter value changes:  
+ **Standard AWS SAM and CloudFormation deployments**: add the [AWS::LanguageExtensions transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-languageextensions.html) before `AWS::Serverless-2016-10-31` in your template's `Transform` section. CloudFormation resolves references to their actual values before AWS SAM computes the version hash. A change to the parameter's value then publishes a new version and updates the alias:

  ```
  Transform:
    - AWS::LanguageExtensions
    - AWS::Serverless-2016-10-31
  ```
+ **AWS Serverless Application Repository applications**: the AWS Serverless Application Repository supports only the `AWS::Serverless-2016-10-31` transform and rejects templates that declare `AWS::LanguageExtensions`. For applications that you publish through the AWS Serverless Application Repository, supply the value directly as a literal in the template instead of referencing a parameter. This makes the change visible when AWS SAM computes the version hash.
This property requires `AutoPublishAlias` to be defined.  
If `AutoPublishCodeSha256` is also specified, its behavior takes precedence over `AutoPublishAliasAllProperties: true`.  
*Type*: Boolean  
*Required*: No  
*Default value*: `false`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `AutoPublishCodeSha256`   <a name="sam-function-autopublishcodesha256"></a>
When used, this string works with the `CodeUri` value to determine if a new Lambda version needs to be published. This property is often used to resolve the following deployment issue: A deployment package is stored in an Amazon S3 location and is replaced by a new deployment package with updated Lambda function code but the `CodeUri` property remains unchanged (as opposed to the new deployment package being uploaded to a new Amazon S3 location and the `CodeUri` being changed to the new location).  
This problem is marked by an AWS SAM template having the following characteristics:  
+ The `DeploymentPreference` object is configured for gradual deployments (as described in [Deploying serverless applications gradually with AWS SAM](automating-updates-to-serverless-apps.md))
+ The `AutoPublishAlias` property is set and doesn't change between deployments
+ The `CodeUri` property is set and doesn't change between deployments.
In this scenario, updating `AutoPublishCodeSha256` results in a new Lambda version being created successfully. However, new function code deployed to Amazon S3 will not be recognized. To recognize new function code, consider using versioning in your Amazon S3 bucket. Specify the `Version` property for your Lambda function and configure your bucket to always use the latest deployment package.  
In this scenario, to trigger the gradual deployment successfully, you must provide a unique value for `AutoPublishCodeSha256`.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `CapacityProviderConfig`   <a name="sam-function-capacityproviderconfig"></a>
Configures the capacity provider to which published versions of the function will be attached. This enables the function to run on customer-owned EC2 instances managed by Lambda Managed Instances.  
*Type*: [CapacityProviderConfig](sam-property-function-capacityproviderconfig.md)  
*Required*: No  
*CloudFormation compatibility*: SAM flattens the property passed to the `[CapacityProviderConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-capacityproviderconfig)` property of an `AWS::Lambda::Function` resource and reconstructs the nested structure.

 `CodeSigningConfigArn`   <a name="sam-function-codesigningconfigarn"></a>
The ARN of the [AWS::Lambda::CodeSigningConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-codesigningconfig.html) resource, used to enable code signing for this function. For more information about code signing, see [Set up code signing for your AWS SAM application](authoring-codesigning.md).  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[CodeSigningConfigArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-codesigningconfigarn)` property of an `AWS::Lambda::Function` resource.

 `CodeUri`   <a name="sam-function-codeuri"></a>
The code for the function. Accepted values include:  
+ The function's Amazon S3 URI. For example, `s3://bucket-123456789/sam-app/1234567890abcdefg`.
+ The local path to the function. For example, `hello_world/`.
+ A [FunctionCode](sam-property-function-functioncode.md) object.
If you provide a function's Amazon S3 URI or [FunctionCode](sam-property-function-functioncode.md) object, you must reference a valid [Lambda deployment package](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html).  
If you provide a local file path, use the AWS SAM CLI to upload the local file at deployment. To learn more, see [How AWS SAM uploads local files at deployment](deploy-upload-local-files.md).  
If you use intrinsic functions in `CodeUri` property, AWS SAM will not be able to correctly parse the values. Consider using [AWS::LanguageExtensions transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-languageextensions.html) instead.
*Type*: [ String \| [FunctionCode](sam-property-function-functioncode.md) ]  
*Required*: Conditional. When `PackageType` is set to `Zip`, one of `CodeUri` or `InlineCode` is required.  
*CloudFormation compatibility*: This property is similar to the `[ Code](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-code)` property of an `AWS::Lambda::Function` resource. The nested Amazon S3 properties are named differently.

 `DeadLetterQueue`   <a name="sam-function-deadletterqueue"></a>
Configures an Amazon Simple Notification Service (Amazon SNS) topic or Amazon Simple Queue Service (Amazon SQS) queue where Lambda sends events that it can't process. For more information about dead-letter queue functionality, see [Dead-letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async-retain-records.html#invocation-dlq) in the *AWS Lambda Developer Guide*.  
If your Lambda function's event source is an Amazon SQS queue, configure a dead-letter queue for the source queue, not for the Lambda function. The dead-letter queue that you configure for a function is used for the function's [asynchronous invocation queue](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html), not for event source queues.
*Type*: Map \| [DeadLetterQueue](sam-property-function-deadletterqueue.md)  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[DeadLetterConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-deadletterconfig.html)` property of an `AWS::Lambda::Function` resource. In CloudFormation the type is derived from the `TargetArn`, whereas in AWS SAM you must pass the type along with the `TargetArn`.

 `DeploymentPreference`   <a name="sam-function-deploymentpreference"></a>
The settings to enable gradual Lambda deployments.  
If a `DeploymentPreference` object is specified, AWS SAM creates an [AWS::CodeDeploy::Application](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html) called `ServerlessDeploymentApplication` (one per stack), an [AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html) called `{{<function-logical-id>}}DeploymentGroup`, and an [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) called `CodeDeployServiceRole`.  
*Type*: [DeploymentPreference](sam-property-function-deploymentpreference.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.  
*See also*: For more information about this property, see [Deploying serverless applications gradually with AWS SAM](automating-updates-to-serverless-apps.md).

 `Description`   <a name="sam-function-description"></a>
A description of the function.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-description)` property of an `AWS::Lambda::Function` resource.

 `DurableConfig`   <a name="sam-function-durableconfig"></a>
Configuration for durable functions. Enables stateful execution with automatic checkpointing and replay capabilities.  
*Type*: [DurableConfig](sam-property-function-durableconfig.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Environment`   <a name="sam-function-environment"></a>
The configuration for the runtime environment.  
*Type*: [Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Environment](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-environment.html)` property of an `AWS::Lambda::Function` resource.

 `EphemeralStorage`   <a name="sam-function-ephemeralstorage"></a>
An object that specifies the disk space, in MB, available to your Lambda function in `/tmp`.  
For more information about this property, see [Lambda execution environment](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html) in the *AWS Lambda Developer Guide*.  
*Type*: [EphemeralStorage](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[EphemeralStorage](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-ephemeralstorage)` property of an `AWS::Lambda::Function` resource.

 `EventInvokeConfig`   <a name="sam-function-eventinvokeconfig"></a>
The object that describes event invoke configuration on a Lambda function.  
*Type*: [EventInvokeConfiguration](sam-property-function-eventinvokeconfiguration.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Events`   <a name="sam-function-events"></a>
Specifies the events that trigger this function. Events consist of a type and a set of properties that depend on the type.  
*Type*: [EventSource](sam-property-function-eventsource.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `FileSystemConfigs`   <a name="sam-function-filesystemconfigs"></a>
List of [FileSystemConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-filesystemconfig.html) objects that specify the connection settings for an Amazon Elastic File System (Amazon EFS) file system or an Amazon S3 Files file system. You can attach either an Amazon EFS access point or an S3 Files access point, but not both.  
Each `FileSystemConfig` object contains an `Arn` (the access point ARN) and a `LocalMountPath` (the path where the file system is mounted in the function). For Amazon EFS, the ARN is an Amazon EFS access point ARN. For S3 Files, the ARN is an `AWS::S3Files::AccessPoint` ARN.  
If your template contains an [AWS::EFS::MountTarget](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-efs-mounttarget.html) resource, you must also specify a `DependsOn` resource attribute to ensure that the mount target is created or updated before the function. Similarly, if your template contains an `AWS::S3Files::MountTarget` resource, you must specify a `DependsOn` attribute for the S3 Files mount target.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FileSystemConfigs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-filesystemconfigs)` property of an `AWS::Lambda::Function` resource.

 `FunctionName`   <a name="sam-function-functionname"></a>
A name for the function. If you don't specify a name, a unique name is generated for you.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionName](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionname)` property of an `AWS::Lambda::Function` resource.

 `FunctionScalingConfig`   <a name="sam-function-functionscalingconfig"></a>
Configures the scaling behavior for Lambda functions running on capacity providers. Defines the minimum and maximum number of execution environments.  
*Type*: [FunctionScalingConfig](sam-property-function-functionscalingconfig.md)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[FunctionScalingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-functionscalingconfig)` property of an `AWS::Lambda::Function` resource.

 `FunctionUrlConfig`   <a name="sam-function-functionurlconfig"></a>
The object that describes a function URL. A function URL is an HTTPS endpoint that you can use to invoke your function.  
For more information, see [Function URLs](https://docs.aws.amazon.com/lambda/latest/dg/lambda-urls.html) in the *AWS Lambda Developer Guide*.  
*Type*: [FunctionUrlConfig](sam-property-function-functionurlconfig.md)  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `Handler`   <a name="sam-function-handler"></a>
The function within your code that is called to begin execution. This property is only required if the `PackageType` property is set to `Zip`.  
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is passed directly to the `[Handler](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-handler)` property of an `AWS::Lambda::Function` resource.

 `ImageConfig`   <a name="sam-function-imageconfig"></a>
The object used to configure Lambda container image settings. For more information, see [Using container images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html) in the *AWS Lambda Developer Guide*.  
*Type*: [ImageConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ImageConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-imageconfig)` property of an `AWS::Lambda::Function` resource.

 `ImageUri`   <a name="sam-function-imageuri"></a>
The URI of the Amazon Elastic Container Registry (Amazon ECR) repository for the Lambda function's container image. This property only applies if the `PackageType` property is set to `Image`, otherwise it is ignored. For more information, see [Using container images with Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-images.html) in the *AWS Lambda Developer Guide*.  
If the `PackageType` property is set to `Image`, then either `ImageUri` is required, or you must build your application with necessary `Metadata` entries in the AWS SAM template file. For more information, see [Default build with AWS SAM](serverless-sam-cli-using-build.md).
Building your application with necessary `Metadata` entries takes precedence over `ImageUri`, so if you specify both then `ImageUri` is ignored.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ImageUri](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-imageuri)` property of the `AWS::Lambda::Function` `Code` data type.

 `InlineCode`   <a name="sam-function-inlinecode"></a>
The Lambda function code that is written directly in the template. This property only applies if the `PackageType` property is set to `Zip`, otherwise it is ignored.  
If the `PackageType` property is set to `Zip` (default), then one of `CodeUri` or `InlineCode` is required.
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is passed directly to the `[ZipFile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-code.html#cfn-lambda-function-code-zipfile)` property of the `AWS::Lambda::Function` `Code` data type.

 `KmsKeyArn`   <a name="sam-function-kmskeyarn"></a>
The ARN of an AWS Key Management Service (AWS KMS) key that Lambda uses to encrypt and decrypt your function's environment variables.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[KmsKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-kmskeyarn)` property of an `AWS::Lambda::Function` resource.

 `Layers`   <a name="sam-function-layers"></a>
The list of `LayerVersion` ARNs that this function should use. The order specified here is the order in which they will be imported when running the Lambda function. The version is either a full ARN including the version or a reference to a LayerVersion resource. For example, a reference to a `LayerVersion` will be `!Ref MyLayer` while a full ARN including the version will be `arn:aws:lambda:{{region}}:{{account-id}}:layer:{{layer-name}}:{{version}}`.  
*Type*: List  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Layers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-layers)` property of an `AWS::Lambda::Function` resource.

 `LoggingConfig`   <a name="sam-function-loggingconfig"></a>
The function's Amazon CloudWatch Logs configuration settings.  
*Type*: [LoggingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-loggingconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the [`LoggingConfig`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-loggingconfig) property of an `AWS::Lambda::Function` resource.

 `MemorySize`   <a name="sam-function-memorysize"></a>
The size of the memory in MB allocated per invocation of the function.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[MemorySize](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-memorysize)` property of an `AWS::Lambda::Function` resource.

 `PackageType`   <a name="sam-function-packagetype"></a>
The deployment package type of the Lambda function. For more information, see [Lambda deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-package.html) in the *AWS Lambda Developer Guide*.  
**Notes**:  
1. If this property is set to `Zip` (default), then either `CodeUri` or `InlineCode` applies, and `ImageUri` is ignored.  
2. If this property is set to `Image`, then only `ImageUri` applies, and both `CodeUri` and `InlineCode` are ignored. The Amazon ECR repository required to store the function's container image can be auto created by the AWS SAM CLI. For more information, see [sam deploy](sam-cli-command-reference-sam-deploy.md).  
*Valid values*: `Zip` or `Image`  
*Type*: String  
*Required*: No  
*Default*: `Zip`  
*CloudFormation compatibility*: This property is passed directly to the `[PackageType](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-packagetype)` property of an `AWS::Lambda::Function` resource.

 `PermissionsBoundary`   <a name="sam-function-permissionsboundary"></a>
The ARN of a permissions boundary to use for this function's execution role. This property works only if the role is generated for you.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[PermissionsBoundary](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-permissionsboundary)` property of an `AWS::IAM::Role` resource.

 `Policies`   <a name="sam-function-policies"></a>
Permission policies for this function. Policies will be appended to the function's default AWS Identity and Access Management (IAM) execution role.  
This property accepts a single value or list of values. Allowed values include:  
+ [AWS SAM policy templates](serverless-policy-templates.md).
+ The ARN of an [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [ customer managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies).
+ The name of an AWS managed policy from the following [ list](https://github.com/aws/serverless-application-model/blob/develop/samtranslator/internal/data/aws_managed_policies.json).
+ An [ inline IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#inline-policies) formatted in YAML as a map.
If you set the `Role` property, this property is ignored.
*Type*: String \| List \| Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Policies](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-policies)` property of an `AWS::IAM::Role` resource.

 `PublishToLatestPublished`   <a name="sam-function-publishtolatestpublished"></a>
Specifies whether to publish the latest function version when the function is updated.  
*Type*: Boolean  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[PublishToLatestPublished](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-publishtolatestpublished)` property of an `AWS::Lambda::Function` resource.

`PropagateTags`  <a name="sam-function-propagatetags"></a>
Indicate whether or not to pass tags from the `Tags` property to your [AWS::Serverless::Function](sam-specification-generated-resources-function.md) generated resources. Specify `True` to propagate tags in your generated resources.  
*Type*: Boolean  
*Required*: No  
*Default*: `False`  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

 `ProvisionedConcurrencyConfig`   <a name="sam-function-provisionedconcurrencyconfig"></a>
The provisioned concurrency configuration of a function's alias.  
`ProvisionedConcurrencyConfig` can be specified only if the `AutoPublishAlias` is set. Otherwise, an error results.
*Type*: [ProvisionedConcurrencyConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ProvisionedConcurrencyConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html#cfn-lambda-alias-provisionedconcurrencyconfig)` property of an `AWS::Lambda::Alias` resource.

 `RecursiveLoop`   <a name="sam-function-recursiveloop"></a>
The status of your function's recursive loop detection configuration.  
When this value is set to `Allow` and Lambda detects your function being invoked as part of a recursive loop, it doesn't take any action.  
When this value is set to `Terminate` and Lambda detects your function being invoked as part of a recursive loop, it stops your function being invoked and notifies you.   
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[RecursiveLoop](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-recursiveloop)` property of the `AWS::Lambda::Function` resource.

 `ReservedConcurrentExecutions`   <a name="sam-function-reservedconcurrentexecutions"></a>
The maximum number of concurrent executions that you want to reserve for the function.  
For more information about this property, see [Lambda Function Scaling](https://docs.aws.amazon.com/lambda/latest/dg/scaling.html) in the *AWS Lambda Developer Guide*.  
*Type*: Integer  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ReservedConcurrentExecutions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-reservedconcurrentexecutions)` property of an `AWS::Lambda::Function` resource.

 `Role`   <a name="sam-function-role"></a>
The ARN of an IAM role to use as this function's execution role.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-role)` property of an `AWS::Lambda::Function` resource. This is required in CloudFormation but not in AWS SAM. If a role isn't specified, one is created for you with a logical ID of `{{<function-logical-id>}}Role`.

 `RolePath`   <a name="sam-function-rolepath"></a>
The path to the function's IAM execution role.  
Use this property when the role is generated for you. Do not use when the role is specified with the `Role` property.  
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is passed directly to the `[Path](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html#cfn-iam-role-path)` property of an `AWS::IAM::Role` resource.

 `Runtime`   <a name="sam-function-runtime"></a>
The identifier of the function's [runtime](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). This property is only required if the `PackageType` property is set to `Zip`.  
If you specify the `provided` identifier for this property, you can use the `Metadata` resource attribute to instruct AWS SAM to build the custom runtime that this function requires. For more information about building custom runtimes, see [Building Lambda functions with custom runtimes in AWS SAM](building-custom-runtimes.md).
*Type*: String  
*Required*: Conditional  
*CloudFormation compatibility*: This property is passed directly to the `[Runtime](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-runtime)` property of an `AWS::Lambda::Function` resource.

 `RuntimeManagementConfig`   <a name="sam-function-runtimemanagementconfig"></a>
Configure runtime management options for your Lambda functions such as runtime environment updates, rollback behavior, and selecting a specific runtime version. To learn more, see [Lambda runtime updates](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html) in the *AWS Lambda Developer Guide*.  
*Type*: [RuntimeManagementConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[ RuntimeManagementConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-runtimemanagementconfig.html)` property of an `AWS::Lambda::Function` resource.

 `SnapStart`   <a name="sam-function-snapstart"></a>
Create a snapshot of any new Lambda function version. A snapshot is a cached state of your initialized function, including all of its dependencies. The function is initialized just once and the cached state is reused for all future invocations, improving application performance by reducing the number of times your function must be initialized. To learn more, see [Improving startup performance with Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) in the *AWS Lambda Developer Guide*.  
*Type*: [SnapStart](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SnapStart](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-snapstart.html)` property of an `AWS::Lambda::Function` resource.

 `SourceKMSKeyArn`   <a name="sam-function-sourcekmskeyarn"></a>
Represents a KMS key ARN that is used to encrypt the customer's ZIP function code.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[SourceKMSKeyArn](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-sourcekmskeyarn)` property of an `AWS::Lambda::Function` `Code` data type.

 `Tags`   <a name="sam-function-tags"></a>
A map (string to string) that specifies the tags added to this function. For details about valid keys and values for tags, see [Tag Key and Value Requirements](https://docs.aws.amazon.com/lambda/latest/dg/configuration-tags.html#configuration-tags-restrictions) in the *AWS Lambda Developer Guide*.  
When the stack is created, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this Lambda function, and to the default roles that are generated for this function.  
*Type*: Map  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[Tags](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tags)` property of an `AWS::Lambda::Function` resource. The `Tags` property in AWS SAM consists of key-value pairs (whereas in CloudFormation this property consists of a list of `Tag` objects). Also, AWS SAM automatically adds a `lambda:createdBy:SAM` tag to this Lambda function, and to the default roles that are generated for this function.

 `TenancyConfig`   <a name="sam-function-tenancyconfig"></a>
Configuration for Lambda tenant isolation mode. Ensures execution environments are never shared between different tenant IDs, providing compute-level isolation for multi-tenant applications.  
*Type*: [TenancyConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-tenancyconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[TenancyConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tenancyconfig)` property of an `AWS::Lambda::Function` resource.

 `Timeout`   <a name="sam-function-timeout"></a>
The maximum time in seconds that the function can run before it is stopped.  
*Type*: Integer  
*Required*: No  
*Default*: 3  
*CloudFormation compatibility*: This property is passed directly to the `[Timeout](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-timeout)` property of an `AWS::Lambda::Function` resource.

 `Tracing`   <a name="sam-function-tracing"></a>
The string that specifies the function's X-Ray tracing mode.  
+ `Active` – Activates X-Ray tracing for the function.
+ `Disabled` – Deactivates X-Ray for the function.
+ `PassThrough` – Activates X-Ray tracing for the function. Sampling decision is delegated to the downstream services.
If specified as `Active` or `PassThrough` and the `Role` property is not set, AWS SAM adds the `arn:aws:iam::aws:policy/AWSXrayWriteOnlyAccess` policy to the Lambda execution role that it creates for you.  
For more information about X-Ray, see [Using AWS Lambda with AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html) in the *AWS Lambda Developer Guide*.  
*Valid values*: [`Active`\|`Disabled`\|`PassThrough`]  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is similar to the `[TracingConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html#cfn-lambda-function-tracingconfig)` property of an `AWS::Lambda::Function` resource.

 `VersionDescription`   <a name="sam-function-versiondescription"></a>
Specifies the `Description` field that is added on the new Lambda version resource.  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[Description](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html#cfn-lambda-version-description)` property of an `AWS::Lambda::Version` resource.

 `VersionDeletionPolicy`   <a name="sam-function-versiondeletionpolicy"></a>
Specifies the deletion policy for the Lambda version resource that is created when `AutoPublishAlias` is set. This controls whether the version resource is retained or deleted when the stack is deleted.  
*Valid values*: `Delete`, `Retain`, or `Snapshot`  
*Type*: String  
*Required*: No  
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent. It sets the `DeletionPolicy` attribute on the generated `AWS::Lambda::Version` resource.

 `VpcConfig`   <a name="sam-function-vpcconfig"></a>
The configuration that enables this function to access private resources within your virtual private cloud (VPC).  
*Type*: [VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html)  
*Required*: No  
*CloudFormation compatibility*: This property is passed directly to the `[VpcConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-lambda-function-vpcconfig.html)` property of an `AWS::Lambda::Function` resource.

## Return Values
<a name="sam-resource-function-return-values"></a>

### Ref
<a name="sam-resource-function-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, it returns the resource name of the underlying Lambda function.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html) in the *AWS CloudFormation User Guide*. 

### Fn::GetAtt
<a name="sam-resource-function-return-values-fn--getatt"></a>

`Fn::GetAtt` returns a value for a specified attribute of this type. The following are the available attributes and sample return values. 

For more information about using `Fn::GetAtt`, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) in the *AWS CloudFormation User Guide*. 

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the underlying Lambda function.

## Examples
<a name="sam-resource-function-examples"></a>

### Simple function
<a name="sam-resource-function-examples-simple-function"></a>

The following is a basic example of an [AWS::Serverless::Function](#sam-resource-function) resource of package type `Zip` (default) and function code in an Amazon S3 bucket.

#### YAML
<a name="sam-resource-function-examples-simple-function--yaml"></a>

```
Type: AWS::Serverless::Function
Properties:
  Handler: index.handler
  Runtime: python3.9
  CodeUri: s3://{{bucket-name}}/{{key-name}}
```

### Function properties example
<a name="sam-resource-function-examples-function-properties-example"></a>

The following is an example of an [AWS::Serverless::Function](#sam-resource-function) of package type `Zip` (default) that uses `InlineCode`, `Layers`, `Tracing`, `Policies`, `Amazon EFS` file system, and an `Api` event source.

#### YAML
<a name="sam-resource-function-examples-function-properties-example--yaml"></a>

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
          Resource: 'arn:aws:s3:::{{sam-s3-demo-bucket}}/*'
  Events:
    ApiEvent:
      Type: Api
      Properties:
        Path: /path
        Method: get
```

### ImageConfig example
<a name="sam-resource-function-examples-imageconfig-example"></a>

The following is an example of an `ImageConfig` for a Lambda function of package type `Image`.

#### YAML
<a name="sam-resource-function-examples-imageconfig-example--yaml"></a>

```
HelloWorldFunction:
  Type: AWS::Serverless::Function
  Properties:
    PackageType: Image
    ImageUri: {{account-id}}.dkr.ecr.{{region}}.amazonaws.com/{{ecr-repo-name}}:{{image-name}}
    ImageConfig:
      Command:
        - "{{app.lambda_handler}}"
      EntryPoint:
        - "{{entrypoint1}}"
      WorkingDirectory: "{{workDir}}"
```

### RuntimeManagementConfig examples
<a name="sam-resource-function-examples-runtimemanagementconfig-examples"></a>

A Lambda function configured to update its runtime environment according to current behavior:

```
TestFunction
  Type: AWS::Serverless::Function
  Properties:
    ...
    Runtime: python3.9
    RuntimeManagementConfig:
      UpdateRuntimeOn: Auto
```

A Lambda function configured to update its runtime environment when the function is updated:

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

### SnapStart examples
<a name="sam-resource-function-examples-snapstart-examples"></a>

Example of a Lambda function with SnapStart turned on for future versions:

```
TestFunc
  Type: AWS::Serverless::Function
  Properties:
    ...
    SnapStart:
      ApplyOn: PublishedVersions
```

### TenancyConfig examples
<a name="sam-resource-function-examples-tenancyconfig-examples"></a>

Example of a Lambda function with tenant isolation mode turned on:

```
TestFunction
  Type: AWS::Serverless::Function
  Properties:
    ...
    TenancyConfig:
      TenantIsolationMode: PER_TENANT
```

### S3 Files file system example
<a name="sam-resource-function-examples-s3files-example"></a>

The following example creates a Lambda function that mounts an Amazon S3 Files file system. The template creates an S3 bucket, an S3 Files file system backed by that bucket, a mount target in a VPC subnet, and an access point. The function mounts the access point at `/mnt/s3files` and can read and write files that sync to the S3 bucket.

**Note**  
You can attach either an Amazon EFS file system or an S3 Files file system to a Lambda function, but not both at the same time.

#### YAML
<a name="sam-resource-function-examples-s3files-example--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: Lambda function with S3 Files file system

Resources:
  # VPC and networking
  MyVpc:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsSupport: true
      EnableDnsHostnames: true

  MySubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVpc
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select [0, !GetAZs '']

  MySecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Security group for Lambda and S3 Files
      VpcId: !Ref MyVpc
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 2049
          ToPort: 2049
          CidrIp: 10.0.0.0/16

  # S3 bucket for file storage
  MyS3Bucket:
    Type: AWS::S3::Bucket

  # IAM role for S3 Files to access the bucket
  S3FilesRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: elasticfilesystem.amazonaws.com
            Action: sts:AssumeRole
      Policies:
        - PolicyName: S3FilesBucketAccess
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: Allow
                Action:
                  - s3:GetObject
                  - s3:PutObject
                  - s3:DeleteObject
                  - s3:ListBucket
                Resource:
                  - !GetAtt MyS3Bucket.Arn
                  - !Sub '${MyS3Bucket.Arn}/*'

  # S3 Files resources
  MyS3FilesFileSystem:
    Type: AWS::S3Files::FileSystem
    Properties:
      Bucket: !GetAtt MyS3Bucket.Arn
      RoleArn: !GetAtt S3FilesRole.Arn

  MyS3FilesMountTarget:
    Type: AWS::S3Files::MountTarget
    Properties:
      FileSystemId: !Ref MyS3FilesFileSystem
      SubnetId: !Ref MySubnet
      SecurityGroups:
        - !Ref MySecurityGroup

  MyS3FilesAccessPoint:
    Type: AWS::S3Files::AccessPoint
    Properties:
      FileSystemId: !Ref MyS3FilesFileSystem
      PosixUser:
        Uid: '1000'
        Gid: '1000'
      RootDirectory:
        Path: /lambda
        CreationInfo:
          OwnerUid: '1000'
          OwnerGid: '1000'
          Permissions: '750'

  # Lambda function with S3 Files mount
  MyFunction:
    Type: AWS::Serverless::Function
    DependsOn: MyS3FilesMountTarget
    Properties:
      Handler: index.handler
      Runtime: python3.12
      Timeout: 120
      VpcConfig:
        SecurityGroupIds:
          - !Ref MySecurityGroup
        SubnetIds:
          - !Ref MySubnet
      FileSystemConfigs:
        - Arn: !GetAtt MyS3FilesAccessPoint.AccessPointArn
          LocalMountPath: /mnt/s3files
      Policies:
        - Version: '2012-10-17'
          Statement:
            - Effect: Allow
              Action:
                - s3files:ClientMount
                - s3files:ClientWrite
              Resource: !GetAtt MyS3FilesAccessPoint.AccessPointArn
      InlineCode: |
        import os

        def handler(event, context):
            # Write a file to the S3 Files mount
            with open('/mnt/s3files/hello.txt', 'w') as f:
                f.write('Hello from Lambda!')

            # List files at the mount path
            files = os.listdir('/mnt/s3files')
            return {'files': files}
```