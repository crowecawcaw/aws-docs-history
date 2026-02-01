# CreateLocationFsxWindows

Creates a transfer _location_ for an Amazon FSx for Windows File Server file
system. AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync
[accesses
FSx for Windows File Server file systems](create-fsx-location.md#create-fsx-location-access "create-fsx-location.md#create-fsx-location-access").

## Request Syntax

```
{
   "Domain": "`string`",
   "FsxFilesystemArn": "`string`",
   "Password": "`string`",
   "SecurityGroupArns": [ "`string`" ],
   "Subdirectory": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "User": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Domain](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies the name of the Windows domain that the FSx for Windows File Server file system
belongs to.

If you have multiple Active Directory domains in your environment, configuring this
parameter makes sure that DataSync connects to the right file system.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`

Required: No

**[FsxFilesystemArn](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) for the FSx for Windows File Server file
system.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`

Required: Yes

**[Password](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies the password of the user with the permissions to mount and access the files,
folders, and file metadata in your FSx for Windows File Server file system.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^.{0,104}$`

Required: Yes

**[SecurityGroupArns](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies the ARNs of the Amazon EC2 security groups that provide access to your
file system's preferred subnet.

The security groups that you specify must be able to communicate with your file system's
security groups. For information about configuring security groups for file system access, see
the [_Amazon FSx for Windows File Server User Guide_](../../../fsx/latest/WindowsGuide/limit-access-security-groups.md "../../../fsx/latest/WindowsGuide/limit-access-security-groups.md").

###### Note

If you choose a security group that doesn't allow connections from within itself, do one
of the following:

- Configure the security group to allow it to communicate within itself.
- Choose a different security group that can communicate with the mount target's
  security group.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: Yes

**[Subdirectory](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies a mount path for your file system using forward slashes. This is where DataSync reads or writes data (depending on if this is a source or destination
location).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

Required: No

**[Tags](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS
resources. We recommend creating at least a name tag for your location.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

**[User](#API_CreateLocationFsxWindows_RequestSyntax "#API_CreateLocationFsxWindows_RequestSyntax")**

Specifies the user with the permissions to mount and access the files, folders, and file
metadata in your FSx for Windows File Server file system.

For information about choosing a user with the right level of access for your transfer,
see [required permissions](create-fsx-location.md#create-fsx-windows-location-permissions "create-fsx-location.md#create-fsx-windows-location-permissions") for FSx for Windows File Server locations.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

Required: Yes

## Response Syntax

```
{
   "LocationArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LocationArn](#API_CreateLocationFsxWindows_ResponseSyntax "#API_CreateLocationFsxWindows_ResponseSyntax")**

The ARN of the FSx for Windows File Server file system location you created.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxWindows.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxWindows.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxWindows.md")
