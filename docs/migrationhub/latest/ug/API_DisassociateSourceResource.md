AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# DisassociateSourceResource

Removes the association between a source resource and a migration task.

## Request Syntax

```
{
   "DryRun": `boolean`,
   "MigrationTaskName": "`string`",
   "ProgressUpdateStream": "`string`",
   "SourceResourceName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DryRun](#API_DisassociateSourceResource_RequestSyntax "#API_DisassociateSourceResource_RequestSyntax")**

This is an optional parameter that you can use to test whether the call will succeed.
Set this parameter to `true` to verify that you have the permissions that are
required to make the call, and that you have specified the other parameters in the call
correctly.

Type: Boolean

Required: No

**[MigrationTaskName](#API_DisassociateSourceResource_RequestSyntax "#API_DisassociateSourceResource_RequestSyntax")**

A unique identifier that references the migration task. _Do not include
sensitive data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[ProgressUpdateStream](#API_DisassociateSourceResource_RequestSyntax "#API_DisassociateSourceResource_RequestSyntax")**

The name of the progress-update stream, which is used for access control as well as a
namespace for migration-task names that is implicitly linked to your AWS account. The
progress-update stream must uniquely identify the migration tool as it is used for all
updates made by the tool; however, it does not need to be unique for each AWS account
because it is scoped to the AWS account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

**[SourceResourceName](#API_DisassociateSourceResource_RequestSyntax "#API_DisassociateSourceResource_RequestSyntax")**

The name that was specified for the source resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 400

**DryRunOperation**

Exception raised to indicate a successfully authorized action when the
`DryRun` flag is set to "true".

HTTP Status Code: 400

**InternalServerError**

Exception raised when an internal, configuration, or dependency error is
encountered.

HTTP Status Code: 500

**InvalidInputException**

Exception raised when the provided input violates a policy constraint or is entered in
the wrong format or data type.

HTTP Status Code: 400

**ResourceNotFoundException**

Exception raised when the request references a resource (Application Discovery Service
configuration, update stream, migration task, etc.) that does not exist in Application
Discovery Service (Application Discovery Service) or in Migration Hub's repository.

HTTP Status Code: 400

**ServiceUnavailableException**

Exception raised when there is an internal, configuration, or dependency error
encountered.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

**Message**

A message that provides information about the exception.

**RetryAfterSeconds**

The number of seconds the caller should wait before retrying.

HTTP Status Code: 400

**UnauthorizedOperation**

Exception raised to indicate a request was not authorized when the `DryRun`
flag is set to "true".

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DisassociateSourceResource.md")
