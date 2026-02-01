AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ListMigrationTaskUpdates

This is a paginated API that returns all the migration-task states for the specified
`MigrationTaskName` and `ProgressUpdateStream`.

## Request Syntax

```
{
   "MaxResults": `number`,
   "MigrationTaskName": "`string`",
   "NextToken": "`string`",
   "ProgressUpdateStream": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListMigrationTaskUpdates_RequestSyntax "#API_ListMigrationTaskUpdates_RequestSyntax")**

The maximum number of results to include in the response. If more results exist than the
value that you specify here for `MaxResults`, the response will include a token
that you can use to retrieve the next set of results.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[MigrationTaskName](#API_ListMigrationTaskUpdates_RequestSyntax "#API_ListMigrationTaskUpdates_RequestSyntax")**

A unique identifier that references the migration task. _Do not include
sensitive data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[NextToken](#API_ListMigrationTaskUpdates_RequestSyntax "#API_ListMigrationTaskUpdates_RequestSyntax")**

If `NextToken` was returned by a previous call, there are more results
available. The value of `NextToken` is a unique pagination token for each page.
To retrieve the next page of results, specify the `NextToken` value that the
previous call returned. Keep all other arguments unchanged. Each pagination token expires
after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken
error.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

Required: No

**[ProgressUpdateStream](#API_ListMigrationTaskUpdates_RequestSyntax "#API_ListMigrationTaskUpdates_RequestSyntax")**

The name of the progress-update stream, which is used for access control as well as a
namespace for migration-task names that is implicitly linked to your AWS account. The
progress-update stream must uniquely identify the migration tool as it is used for all
updates made by the tool; however, it does not need to be unique for each AWS account
because it is scoped to the AWS account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

## Response Syntax

```
{
   "MigrationTaskUpdateList": [
      {
         "MigrationTaskState": {
            "ProgressPercent": ***number***,
            "Status": "***string***",
            "StatusDetail": "***string***"
         },
         "UpdateDateTime": ***number***,
         "UpdateType": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[MigrationTaskUpdateList](#API_ListMigrationTaskUpdates_ResponseSyntax "#API_ListMigrationTaskUpdates_ResponseSyntax")**

The list of migration-task updates.

Type: Array of [MigrationTaskUpdate](API_MigrationTaskUpdate.md "API_MigrationTaskUpdate.md") objects

**[NextToken](#API_ListMigrationTaskUpdates_ResponseSyntax "#API_ListMigrationTaskUpdates_ResponseSyntax")**

If the response includes a `NextToken` value, that means that there are more
results available. The value of `NextToken` is a unique pagination token for
each page. To retrieve the next page of results, call this API again and specify this
`NextToken` value in the request. Keep all other arguments unchanged. Each
pagination token expires after 24 hours. Using an expired pagination token will return an
HTTP 400 InvalidToken error.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListMigrationTaskUpdates.md")
