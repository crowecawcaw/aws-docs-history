# UnshareDirectory

Stops the directory sharing between the directory owner and consumer accounts.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "UnshareTarget": {
      "Id": "`string`",
      "Type": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_UnshareDirectory_RequestSyntax "#API_UnshareDirectory_RequestSyntax")**

The identifier of the AWS Managed Microsoft AD directory that you want to stop sharing.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[UnshareTarget](#API_UnshareDirectory_RequestSyntax "#API_UnshareDirectory_RequestSyntax")**

Identifier for the directory consumer account with whom the directory has to be
unshared.

Type: [UnshareTarget](API_UnshareTarget.md "API_UnshareTarget.md") object

Required: Yes

## Response Syntax

```
{
   "SharedDirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SharedDirectoryId](#API_UnshareDirectory_ResponseSyntax "#API_UnshareDirectory_ResponseSyntax")**

Identifier of the directory stored in the directory consumer account that is to be
unshared from the specified directory (`DirectoryId`).

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryNotSharedException**

The specified directory has not been shared with this AWS account.

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

**InvalidTargetException**

The specified shared target is not valid.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UnshareDirectory.md "../../../goto/cli2/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UnshareDirectory.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UnshareDirectory.md "../../../goto/boto3/ds-2015-04-16/UnshareDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UnshareDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UnshareDirectory.md")
