AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ListMigrationTasks

Lists all, or filtered by resource name, migration tasks associated with the user
account making this call. This API has the following traits:

- Can show a summary list of the most recent migration tasks.
- Can show a summary list of migration tasks associated with a given discovered
  resource.
- Lists migration tasks in a paginated interface.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "ResourceName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[MaxResults](#API_ListMigrationTasks_RequestSyntax "#API_ListMigrationTasks_RequestSyntax")**

Value to specify how many results are returned per page.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListMigrationTasks_RequestSyntax "#API_ListMigrationTasks_RequestSyntax")**

If a `NextToken` was returned by a previous call, there are more results
available. To retrieve the next page of results, make the call again using the returned
token in `NextToken`.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

Required: No

**[ResourceName](#API_ListMigrationTasks_RequestSyntax "#API_ListMigrationTasks_RequestSyntax")**

Filter migration tasks by discovered resource name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `^.{1,1600}$`

Required: No

## Response Syntax

```
{
   "MigrationTaskSummaryList": [
      {
         "MigrationTaskName": "***string***",
         "ProgressPercent": ***number***,
         "ProgressUpdateStream": "***string***",
         "Status": "***string***",
         "StatusDetail": "***string***",
         "UpdateDateTime": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[MigrationTaskSummaryList](#API_ListMigrationTasks_ResponseSyntax "#API_ListMigrationTasks_ResponseSyntax")**

Lists the migration task's summary which includes: `MigrationTaskName`,
`ProgressPercent`, `ProgressUpdateStream`, `Status`,
and the `UpdateDateTime` for each task.

Type: Array of [MigrationTaskSummary](API_MigrationTaskSummary.md "API_MigrationTaskSummary.md") objects

**[NextToken](#API_ListMigrationTasks_ResponseSyntax "#API_ListMigrationTasks_ResponseSyntax")**

If there are more migration tasks than the max result, return the next token to be
passed to the next call as a bookmark of where to start from.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

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

### List a summary of all the migration tasks

The following example lists a summary of the migration tasks associated with the
values passed to the optional parameters of `ResourceName` and
`MaxResults`.

#### Sample Request

```

{
   "MaxResults": 1,
   "ResourceName": "d-server-0025db43a885966c8"
}
```

#### Sample Response

```

{
    "MigrationTaskSummaryList": [
        {
            "Status": "COMPLETED",
            "ProgressUpdateStream": "SMS",
            "StatusDetail": "Replication finished",
            "UpdateDateTime": 1487858882.0,
            "MigrationTaskName": "sms-12de3cf1a"
        }
    ]
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/DotNetSDKV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListMigrationTasks.md")
