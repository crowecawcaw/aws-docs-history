# DescribeLocationFsxWindows

Provides details about how an AWS DataSync transfer location for an Amazon FSx for Windows File Server file system is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationFsxWindows_RequestSyntax "#API_DescribeLocationFsxWindows_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the FSx for Windows File Server location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "Domain": "***string***",
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "SecurityGroupArns": [ "***string***" ],
   "User": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The time that the FSx for Windows File Server location was created.

Type: Timestamp

**[Domain](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The name of the Microsoft Active Directory domain that the FSx for Windows File Server file
system belongs to.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`

**[LocationArn](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The ARN of the FSx for Windows File Server location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The uniform resource identifier (URI) of the FSx for Windows File Server location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[SecurityGroupArns](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The ARNs of the Amazon EC2 security groups that provide access to your file
system's preferred subnet.

For information about configuring security groups for file system access, see the [_Amazon FSx for Windows File Server User Guide_](../../../fsx/latest/WindowsGuide/limit-access-security-groups.md "../../../fsx/latest/WindowsGuide/limit-access-security-groups.md").

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

**[User](#API_DescribeLocationFsxWindows_ResponseSyntax "#API_DescribeLocationFsxWindows_ResponseSyntax")**

The user with the permissions to mount and access the FSx for Windows File Server file
system.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxWindows.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxWindows.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxWindows.md")
