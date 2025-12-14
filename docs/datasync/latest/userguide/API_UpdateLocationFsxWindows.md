# UpdateLocationFsxWindows

Modifies the following configuration parameters of the Amazon FSx for Windows File Server
transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with FSx for Windows File Server](create-fsx-location.md "create-fsx-location.md").

## Request Syntax

```
{
   "Domain": "`string`",
   "LocationArn": "`string`",
   "Password": "`string`",
   "Subdirectory": "`string`",
   "User": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Domain](#API_UpdateLocationFsxWindows_RequestSyntax "#API_UpdateLocationFsxWindows_RequestSyntax")**

Specifies the name of the Windows domain that your FSx for Windows File Server file system
belongs to.

If you have multiple Active Directory domains in your environment, configuring this
parameter makes sure that DataSync connects to the right file system.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^([A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252})?$`

Required: No

**[LocationArn](#API_UpdateLocationFsxWindows_RequestSyntax "#API_UpdateLocationFsxWindows_RequestSyntax")**

Specifies the ARN of the FSx for Windows File Server transfer location that you're
updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Password](#API_UpdateLocationFsxWindows_RequestSyntax "#API_UpdateLocationFsxWindows_RequestSyntax")**

Specifies the password of the user with the permissions to mount and access the files,
folders, and file metadata in your FSx for Windows File Server file system.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^.{0,104}$`

Required: No

**[Subdirectory](#API_UpdateLocationFsxWindows_RequestSyntax "#API_UpdateLocationFsxWindows_RequestSyntax")**

Specifies a mount path for your file system using forward slashes. DataSync uses
this subdirectory to read or write data (depending on whether the file system is a source or
destination location).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

Required: No

**[User](#API_UpdateLocationFsxWindows_RequestSyntax "#API_UpdateLocationFsxWindows_RequestSyntax")**

Specifies the user with the permissions to mount and access the files, folders, and file
metadata in your FSx for Windows File Server file system.

For information about choosing a user with the right level of access for your transfer,
see [required permissions](create-fsx-location.md#create-fsx-windows-location-permissions "create-fsx-location.md#create-fsx-windows-location-permissions") for FSx for Windows File Server locations.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxWindows.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxWindows.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxWindows.md")
