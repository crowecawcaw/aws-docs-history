# AcceptSharedDirectory

Accepts a directory sharing request that was sent from the directory owner account.

## Request Syntax

```
{
   "SharedDirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[SharedDirectoryId](#API_AcceptSharedDirectory_RequestSyntax "#API_AcceptSharedDirectory_RequestSyntax")**

Identifier of the shared directory in the directory consumer account. This identifier is
different for each directory owner account.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "SharedDirectory": {
      "CreatedDateTime": ***number***,
      "LastUpdatedDateTime": ***number***,
      "OwnerAccountId": "***string***",
      "OwnerDirectoryId": "***string***",
      "SharedAccountId": "***string***",
      "SharedDirectoryId": "***string***",
      "ShareMethod": "***string***",
      "ShareNotes": "***string***",
      "ShareStatus": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SharedDirectory](#API_AcceptSharedDirectory_ResponseSyntax "#API_AcceptSharedDirectory_ResponseSyntax")**

The shared directory in the directory consumer account.

Type: [SharedDirectory](API_SharedDirectory.md "API_SharedDirectory.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryAlreadySharedException**

The specified directory has already been shared with this AWS account.

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

**InvalidParameterException**

One or more parameters are not valid.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/cli2/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/DotNetSDKV4/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/boto3/ds-2015-04-16/AcceptSharedDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AcceptSharedDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AcceptSharedDirectory.md")
