AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# CreateProgressUpdateStream

Creates a progress update stream which is an AWS resource used for access control as
well as a namespace for migration task names that is implicitly linked to your AWS account.
It must uniquely identify the migration tool as it is used for all updates made by the
tool; however, it does not need to be unique for each AWS account because it is scoped to
the AWS account.

## Request Syntax

```
{
   "DryRun": `boolean`,
   "ProgressUpdateStreamName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DryRun](#API_CreateProgressUpdateStream_RequestSyntax "#API_CreateProgressUpdateStream_RequestSyntax")**

Optional boolean flag to indicate whether any effect should take place. Used to test if
the caller has permission to make the call.

Type: Boolean

Required: No

**[ProgressUpdateStreamName](#API_CreateProgressUpdateStream_RequestSyntax "#API_CreateProgressUpdateStream_RequestSyntax")**

The name of the ProgressUpdateStream. _Do not store personal data in this
field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

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

**HomeRegionNotSetException**

The home region is not set. Set the home region to continue.

HTTP Status Code: 400

**InternalServerError**

Exception raised when an internal, configuration, or dependency error is
encountered.

HTTP Status Code: 500

**InvalidInputException**

Exception raised when the provided input violates a policy constraint or is entered in
the wrong format or data type.

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

## Examples

### Create a progress update stream

The following example creates a progress update stream identified by the values
passed to the required parameter `ProgressUpdateStreamName` in the
request.

#### Sample Request

```

{
    "ProgressUpdateStreamName": "SMS",
    "DryRun": false
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/CreateProgressUpdateStream.md")
