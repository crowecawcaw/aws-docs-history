# UpdateLocationFsxLustre

Modifies the following configuration parameters of the Amazon FSx for Lustre
transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with FSx for Lustre](create-lustre-location.md "create-lustre-location.md").

## Request Syntax

```
{
   "LocationArn": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_UpdateLocationFsxLustre_RequestSyntax "#API_UpdateLocationFsxLustre_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the FSx for Lustre transfer location
that you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Subdirectory](#API_UpdateLocationFsxLustre_RequestSyntax "#API_UpdateLocationFsxLustre_RequestSyntax")**

Specifies a mount path for your FSx for Lustre file system. The path can include
subdirectories.

When the location is used as a source, DataSync reads data from the mount path.
When the location is used as a destination, DataSync writes data to the mount path.
If you don't include this parameter, DataSync uses the file system's root directory
(`/`).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

Required: No

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxLustre.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxLustre.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxLustre.md")
