# DeleteLocation

Deletes a transfer location resource from AWS DataSync.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DeleteLocation_RequestSyntax "#API_DeleteLocation_RequestSyntax")**

The Amazon Resource Name (ARN) of the location to delete.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DeleteLocation.md "../../../goto/cli2/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DeleteLocation.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForCpp/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DeleteLocation.md "../../../goto/boto3/datasync-2018-11-09/DeleteLocation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DeleteLocation.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DeleteLocation.md")
