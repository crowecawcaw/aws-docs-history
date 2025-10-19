# RegisterType

Registers an extension with the CloudFormation service. Registering an extension makes it
 available for use in CloudFormation templates in your AWS account, and includes:


* Validating the extension schema.
* Determining which handlers, if any, have been specified for the extension.
* Making the extension available for use in your account.
For more information about how to develop extensions and ready them for registration, see
 [Creating resource types using the CloudFormation CLI](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html") in the
 *AWS CloudFormation Command Line Interface (CLI) User Guide*.

You can have a maximum of 50 resource extension versions registered at a time. This
 maximum is per account and per Region. Use [DeregisterType](API_DeregisterType.md "API_DeregisterType.md")
 to deregister specific extension versions if necessary.

Once you have initiated a registration request using RegisterType, you
 can use [DescribeTypeRegistration](API_DescribeTypeRegistration.md "API_DescribeTypeRegistration.md") to monitor the progress of the registration
 request.

Once you have registered a private extension in your account and Region, use [SetTypeConfiguration](API_SetTypeConfiguration.md "API_SetTypeConfiguration.md") to specify configuration properties for the extension. For
 more information, see [Edit configuration
 data for extensions in your account](../UserGuide/registry-set-configuration.md "../UserGuide/registry-set-configuration.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**ClientRequestToken** 


A unique identifier that acts as an idempotency key for this registration request.
 Specifying a client request token prevents CloudFormation from generating more than one version of
 an extension from the same registration request, even if the request is submitted multiple
 times.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**ExecutionRoleArn** 


The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking
 the extension.


For CloudFormation to assume the specified execution role, the role must contain a trust
 relationship with the CloudFormation service principal
 (`resources.cloudformation.amazonaws.com`). For more information about adding
 trust relationships, see [Modifying a role trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy "https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy") in the *AWS Identity and Access Management User
 Guide*.


If your extension calls AWS APIs in any of its handlers, you must create an
 *[IAM
 execution role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html")* that includes the necessary permissions to call those
 AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke
 the resource type handler, CloudFormation assumes this execution role to create a temporary
 session token, which it then passes to the resource type handler, thereby supplying your
 resource type with the appropriate credentials.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 256.


Pattern: `arn:.+:iam::[0-9]{12}:role/.+`



Required: No




**LoggingConfig** 


Specifies logging configuration information for an extension.


Type: [LoggingConfig](API_LoggingConfig.md "API_LoggingConfig.md") object


Required: No




**SchemaHandlerPackage** 


A URL to the S3 bucket that contains the extension project package that contains the
 necessary files for the extension you want to register.


For information about generating a schema handler package for the extension you want to
 register, see [submit](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html "https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html") in
 the *AWS CloudFormation Command Line Interface (CLI) User Guide*.


###### Note

The user registering the extension must be able to access the package in the S3 bucket.
 That's, the user needs to have [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html "https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html") permissions for the schema
 handler package. For more information, see [Actions, Resources, and Condition Keys for
 Amazon S3](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html") in the *AWS Identity and Access Management User Guide*.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 4096.


Required: Yes




**Type** 


The kind of extension.


Type: String


Valid Values: `RESOURCE | MODULE | HOOK`



Required: No




**TypeName** 


The name of the extension being registered.


We suggest that extension names adhere to the following patterns:



* For resource types, `company_or_organization::service::type`.
* For modules, `company_or_organization::service::type::MODULE`.
* For Hooks, `MyCompany::Testing::MyTestHook`.

###### Note

The following organization namespaces are reserved and can't be used in your extension
 names:


* `Alexa`
* `AMZN`
* `Amazon`
* `AWS`
* `Custom`
* `Dev`

Type: String


Length Constraints: Minimum length of 10. Maximum length of 204.


Pattern: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`



Required: Yes




## Response Elements


The following element is returned by the service.





**RegistrationToken** 


The identifier for this registration request.


Use this registration token when calling [DescribeTypeRegistration](API_DescribeTypeRegistration.md "API_DescribeTypeRegistration.md"), which
 returns information about the status and IDs of the extension registration.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CFNRegistry** 


An error occurred during a CloudFormation registry operation.





**Message** 


A message with details about the error that occurred.




HTTP Status Code: 400




## Examples


### RegisterType


This example illustrates one usage of RegisterType.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=RegisterType
 &Version=2010-05-15
 &TypeName=My::Resource::Example
 &SchemaHandlerPackage=[s3 url]
 &Type=RESOURCE
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20171211T230005Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```
<RegisterTypeResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <RegisterTypeResult>
    <RegistrationToken>f5525280-104e-4d35-bef5-8f1f1example</RegistrationToken>
  </RegisterTypeResult>
  <ResponseMetadata>
    <RequestId>4d121847-1d2b-4ebe-8ca5-499405example</RequestId>
  </ResponseMetadata>
</RegisterTypeResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/RegisterType")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RegisterType "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/RegisterType")
