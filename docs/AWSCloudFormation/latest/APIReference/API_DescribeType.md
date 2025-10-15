# DescribeType

Returns detailed information about an extension from the CloudFormation registry in your
 current account and Region.

If you specify a `VersionId`, `DescribeType` returns information
 about that specific extension version. Otherwise, it returns information about the default
 extension version.

For more information, see [Edit configuration
 data for extensions in your account](../UserGuide/registry-set-configuration.md "../UserGuide/registry-set-configuration.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Arn** 


The Amazon Resource Name (ARN) of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`



Required: No




**PublicVersionNumber** 


The version number of a public third-party extension.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`



Required: No




**PublisherId** 


The publisher ID of the extension publisher.


Extensions provided by AWS are not assigned a publisher ID.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`



Required: No




**Type** 


The kind of extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension.


Conditional: You must specify either `TypeName` and `Type`, or
 `Arn`.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: No




**VersionId** 


The ID of a specific version of the extension. The version ID is the value at the end of
 the Amazon Resource Name (ARN) assigned to the extension version when it is registered.


If you specify a `VersionId`, `DescribeType` returns information
 about that specific extension version. Otherwise, it returns information about the default
 extension version.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`



Required: No




## Response Elements


The following elements are returned by the service.





**Arn** 


The Amazon Resource Name (ARN) of the extension.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`





**AutoUpdate** 


Whether CloudFormation automatically updates the extension in this account and Region when a
 new *minor* version is published by the extension publisher. Major versions
 released by the publisher must be manually updated. For more information, see [Automatically use new versions of extensions](../UserGuide/registry-public.md#registry-public-enable-auto "../UserGuide/registry-public.md#registry-public-enable-auto") in the
 *AWS CloudFormation User Guide*.


Type: Boolean




**ConfigurationSchema** 


A JSON string that represent the current configuration data for the extension in this
 account and Region.


To set the configuration data for an extension, use [SetTypeConfiguration](API_SetTypeConfiguration.md "API_SetTypeConfiguration.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 60000.


Pattern: `[\s\S]+`





**DefaultVersionId** 


The ID of the default version of the extension. The default version is used when the
 extension version isn't specified.


This applies only to private extensions you have registered in your account. For public
 extensions, both those provided by AWS and published by third parties, CloudFormation returns
 `null`. For more information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").


To set the default version of an extension, use [SetTypeDefaultVersion](API_SetTypeDefaultVersion.md "API_SetTypeDefaultVersion.md").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[A-Za-z0-9-]+`





**DeprecatedStatus** 


The deprecation status of the extension version.


Valid values include:



* `LIVE`: The extension is activated or registered and can be used in
 CloudFormation operations, dependent on its provisioning behavior and visibility scope.
* `DEPRECATED`: The extension has been deactivated or deregistered and can no
 longer be used in CloudFormation operations.

For public third-party extensions, CloudFormation returns `null`.


Type: String


Valid Values: `LIVE | DEPRECATED`





**Description** 


The description of the extension.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




**DocumentationUrl** 


The URL of a page providing detailed documentation for this extension.


Type: String


Length Constraints: Maximum length of 4096.




**ExecutionRoleArn** 


The Amazon Resource Name (ARN) of the IAM execution role used to register the extension.
 This applies only to private extensions you have registered in your account. For more
 information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").


If the registered extension calls any AWS APIs, you must create an *[IAM execution
 role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html")* that includes the necessary permissions to call those AWS APIs,
 and provision that execution role in your account. CloudFormation then assumes that execution role
 to provide your extension with the appropriate credentials.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `arn:.+:iam::[0-9]{12}:role/.+`





**IsActivated** 


Whether the extension is activated in the account and Region.


This only applies to public third-party extensions. For all other extensions, CloudFormation
 returns `null`.


Type: Boolean




**IsDefaultVersion** 


Whether the specified extension version is set as the default version.


This applies only to private extensions you have registered in your account, and
 extensions published by AWS. For public third-party extensions, whether they are activated
 in your account, CloudFormation returns `null`.


Type: Boolean




**LastUpdated** 


When the specified extension version was registered. This applies only to:



* Private extensions you have registered in your account. For more information, see
 [RegisterType](API_RegisterType.md "API_RegisterType.md").
* Public extensions you have activated in your account with auto-update specified. For
 more information, see [ActivateType](API_ActivateType.md "API_ActivateType.md").

Type: Timestamp




**LatestPublicVersion** 


The latest version of a public extension *that is available* for
 use.


This only applies if you specify a public extension, and you don't specify a version. For
 all other requests, CloudFormation returns `null`.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`





**LoggingConfig** 


Contains logging configuration information for private extensions. This applies only to
 private extensions you have registered in your account. For public extensions, both those
 provided by AWS and published by third parties, CloudFormation returns `null`. For
 more information, see [RegisterType](API_RegisterType.md "API_RegisterType.md").


Type: [LoggingConfig](API_LoggingConfig.md "API_LoggingConfig.md") object




**OriginalTypeArn** 


For public extensions that have been activated for this account and Region, the Amazon
 Resource Name (ARN) of the public extension.


Type: String


Length Constraints: Maximum length of 1024.


Pattern: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`





**OriginalTypeName** 


For public extensions that have been activated for this account and Region, the type name
 of the public extension.


If you specified a `TypeNameAlias` when enabling the extension in this account
 and Region, CloudFormation treats that alias as the extension's type name within the account and
 Region, not the type name of the public extension. For more information, see [Use aliases to refer to extensions](../UserGuide/registry-public.md#registry-public-enable-alias "../UserGuide/registry-public.md#registry-public-enable-alias") in the
 *AWS CloudFormation User Guide*.


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`





**ProvisioningType** 


For resource type extensions, the provisioning behavior of the resource type. CloudFormation
 determines the provisioning type during registration, based on the types of handlers in the
 schema handler package submitted.


Valid values include:



* `FULLY_MUTABLE`: The resource type includes an update handler to process
 updates to the type during stack update operations.
* `IMMUTABLE`: The resource type doesn't include an update handler, so the
 type can't be updated and must instead be replaced during stack update operations.
* `NON_PROVISIONABLE`: The resource type doesn't include all the following
 handlers, and therefore can't actually be provisioned.




	+ create
	+ read
	+ delete

Type: String


Valid Values: `NON_PROVISIONABLE | IMMUTABLE | FULLY_MUTABLE`





**PublicVersionNumber** 


The version number of a public third-party extension.


This applies only if you specify a public extension you have activated in your account, or
 specify a public extension without specifying a version. For all other extensions, CloudFormation
 returns `null`.


Type: String


Length Constraints: Minimum length of 5.


Pattern: `^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(.*)$`





**PublisherId** 


The publisher ID of the extension publisher.


This applies only to public third-party extensions. For private registered extensions, and
 extensions provided by AWS, CloudFormation returns `null`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 40.


Pattern: `[0-9a-zA-Z]{12,40}`





**RequiredActivatedTypes.member.N**


For extensions that are modules, the public third-party extensions that must be activated
 in your account in order for the module itself to be activated.


Type: Array of [RequiredActivatedType](API_RequiredActivatedType.md "API_RequiredActivatedType.md") objects




**Schema** 


The schema that defines the extension.


For more information, see [Resource type
 schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html") in the *AWS CloudFormation Command Line Interface (CLI) User Guide* and the [AWS CloudFormation
 Hooks User Guide](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html "https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html").


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16777216.




**SourceUrl** 


The URL of the source code for the extension.


Type: String


Length Constraints: Maximum length of 4096.




**TimeCreated** 


When the specified private extension version was registered or activated in your
 account.


Type: Timestamp




**Type** 


The kind of extension.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`





**TypeName** 


The name of the extension.


If the extension is a public third-party type you have activated with a type name alias,
 CloudFormation returns the type name alias. For more information, see [ActivateType](API_ActivateType.md "API_ActivateType.md").


Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`





**TypeTestsStatus** 


The contract test status of the registered extension version. To return the extension test
 status of a specific extension version, you must specify `VersionId`.


This applies only to registered private extension versions. CloudFormation doesn't return this
 information for public extensions, whether they are activated in your account.



* `PASSED`: The extension has passed all its contract tests.


An extension must have a test status of `PASSED` before it can be
 published. For more information, see [Publishing
 extensions to make them available for public use](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.
* `FAILED`: The extension has failed one or more contract tests.
* `IN_PROGRESS`: Contract tests are currently being performed on the
 extension.
* `NOT_TESTED`: Contract tests haven't been performed on the
 extension.

Type: String


Valid Values: `PASSED | FAILED | IN_PROGRESS | NOT_TESTED`





**TypeTestsStatusDescription** 


The description of the test status. To return the extension test status of a specific
 extension version, you must specify `VersionId`.


This applies only to registered private extension versions. CloudFormation doesn't return this
 information for public extensions, whether they are activated in your account.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `[\s\S]+`





**Visibility** 


The scope at which the extension is visible and usable in CloudFormation operations.


Valid values include:



* `PRIVATE`: The extension is only visible and usable within the account in
 which it is registered. CloudFormation marks any extensions you register as
 `PRIVATE`.
* `PUBLIC`: The extension is publicly visible and usable within any AWS
 account.

Type: String


Valid Values: `PUBLIC | PRIVATE`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




**TypeNotFound** 


The specified extension doesn't exist in the CloudFormation registry.


HTTP Status Code: 404




## Examples


### DescribeType


This example illustrates one usage of DescribeType.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DescribeType
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &VersionId=00000002
 &Type=RESOURCE
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191203T234428Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<DescribeTypeResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <DescribeTypeResult>
    <Schema>{
    [details omitted]
}
</Schema>
    <Visibility>PRIVATE</Visibility>
    <DeprecatedStatus>LIVE</DeprecatedStatus>
    <TypeName>My::Resource::Example</TypeName>
    <Description>Resource schema for My::Resource::Example</Description>
    <Type>RESOURCE</Type>
    <SourceUrl>https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-logs.git</SourceUrl>
    <LastUpdated>2019-12-03T23:29:33.321Z</LastUpdated>
    <ProvisioningType>FULLY_MUTABLE</ProvisioningType>
    <TimeCreated>2019-12-03T23:29:33.321Z</TimeCreated>
    <Arn>arn:aws:cloudformation:us-east-1:012345678910:type/resource/My-Resource-Example/00000002</Arn>
  </DescribeTypeResult>
  <ResponseMetadata>
    <RequestId>8d2dd588-b16f-4096-8516-ee941example</RequestId>
  </ResponseMetadata>
</DescribeTypeResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DescribeType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DescribeType")
