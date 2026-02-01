AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# ListApplicationStates

Lists all the migration statuses for your applications. If you use the optional
`ApplicationIds` parameter, only the migration statuses for those
applications will be returned.

## Request Syntax

```
{
   "ApplicationIds": [ "`string`" ],
   "MaxResults": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ApplicationIds](#API_ListApplicationStates_RequestSyntax "#API_ListApplicationStates_RequestSyntax")**

The configurationIds from the Application Discovery Service that uniquely identifies
your applications.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 100 items.

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `^.{1,1600}$`

Required: No

**[MaxResults](#API_ListApplicationStates_RequestSyntax "#API_ListApplicationStates_RequestSyntax")**

Maximum number of results to be returned per page.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListApplicationStates_RequestSyntax "#API_ListApplicationStates_RequestSyntax")**

If a `NextToken` was returned by a previous call, there are more results
available. To retrieve the next page of results, make the call again using the returned
token in `NextToken`.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `^[a-zA-Z0-9\/\+\=]{0,2048}$`

Required: No

## Response Syntax

```
{
   "ApplicationStateList": [
      {
         "ApplicationId": "***string***",
         "ApplicationStatus": "***string***",
         "LastUpdatedTime": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ApplicationStateList](#API_ListApplicationStates_ResponseSyntax "#API_ListApplicationStates_ResponseSyntax")**

A list of Applications that exist in Application Discovery Service.

Type: Array of [ApplicationState](API_ApplicationState.md "API_ApplicationState.md") objects

Array Members: Minimum number of 0 items. Maximum number of 1000 items.

**[NextToken](#API_ListApplicationStates_ResponseSyntax "#API_ListApplicationStates_ResponseSyntax")**

If a `NextToken` was returned by a previous call, there are more results
available. To retrieve the next page of results, make the call again using the returned
token in `NextToken`.

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/ListApplicationStates.md")
