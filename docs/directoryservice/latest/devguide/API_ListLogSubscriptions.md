# ListLogSubscriptions

Lists the active log subscriptions for the AWS account.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ListLogSubscriptions_RequestSyntax "#API_ListLogSubscriptions_RequestSyntax")**

If a _DirectoryID_ is provided, lists only the log subscription
associated with that directory. If no _DirectoryId_ is provided, lists all
log subscriptions associated with your AWS account. If there are no log subscriptions for
the AWS account or the directory, an empty list will be returned.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**[Limit](#API_ListLogSubscriptions_RequestSyntax "#API_ListLogSubscriptions_RequestSyntax")**

The maximum number of items returned.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[NextToken](#API_ListLogSubscriptions_RequestSyntax "#API_ListLogSubscriptions_RequestSyntax")**

The token for the next set of items to return.

Type: String

Required: No

## Response Syntax

```
{
   "LogSubscriptions": [
      {
         "DirectoryId": "***string***",
         "LogGroupName": "***string***",
         "SubscriptionCreatedDateTime": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LogSubscriptions](#API_ListLogSubscriptions_ResponseSyntax "#API_ListLogSubscriptions_ResponseSyntax")**

A list of active [LogSubscription](API_LogSubscription.md "API_LogSubscription.md") objects for calling the
AWS account.

Type: Array of [LogSubscription](API_LogSubscription.md "API_LogSubscription.md") objects

**[NextToken](#API_ListLogSubscriptions_ResponseSyntax "#API_ListLogSubscriptions_ResponseSyntax")**

The token for the next set of items to return.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidNextTokenException**

The `NextToken` value is not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/cli2/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/DotNetSDKV3/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForCpp/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForGoV2/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForKotlin/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/boto3/ds-2015-04-16/ListLogSubscriptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ListLogSubscriptions.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ListLogSubscriptions.md")
