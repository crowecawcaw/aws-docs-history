AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# DescribeApplicationState

Gets the migration status of an application.

## Request Syntax

```
{
   "ApplicationId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationId](#API_DescribeApplicationState_RequestSyntax "#API_DescribeApplicationState_RequestSyntax")**

The configurationId in Application Discovery Service that uniquely identifies the
grouped application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `^.{1,1600}$`

Required: Yes

## Response Syntax

```
{
   "ApplicationStatus": "***string***",
   "LastUpdatedTime": ***number***
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ApplicationStatus](#API_DescribeApplicationState_ResponseSyntax "#API_DescribeApplicationState_ResponseSyntax")**

Status of the application - Not Started, In-Progress, Complete.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED`

**[LastUpdatedTime](#API_DescribeApplicationState_ResponseSyntax "#API_DescribeApplicationState_ResponseSyntax")**

The timestamp when the application status was last updated.

Type: Timestamp

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

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

**PolicyErrorException**

Exception raised when there are problems accessing Application Discovery Service
(Application Discovery Service); most likely due to a misconfigured policy or the
`migrationhub-discovery` role is missing or not configured correctly.

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

## Examples

### Describe a migration task by listing all associated attributes

The following example lists all of the attributes associated with the values
passed to the required parameters of `MigrationTaskName` and
`ProgressUpdateStream`.

#### Sample Request

```

{
    "ApplicationId": "d-application-0039038d504694533"
}
```

#### Sample Response

```

{
    "ApplicationStatus": "IN_PROGRESS",
    "LastUpdatedTime": 1493405005.639
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/DescribeApplicationState.md")
