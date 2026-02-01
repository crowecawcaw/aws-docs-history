# DeleteLogSubscription

Deletes the specified log subscription.

## Request Syntax

```
{
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DeleteLogSubscription_RequestSyntax "#API_DeleteLogSubscription_RequestSyntax")**

Identifier of the directory whose log subscription you want to delete.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/cli2/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForCpp/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/boto3/ds-2015-04-16/DeleteLogSubscription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteLogSubscription.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteLogSubscription.md")
