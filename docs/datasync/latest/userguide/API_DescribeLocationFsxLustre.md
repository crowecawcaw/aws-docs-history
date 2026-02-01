# DescribeLocationFsxLustre

Provides details about how an AWS DataSync transfer location for an Amazon FSx for Lustre file system is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationFsxLustre_RequestSyntax "#API_DescribeLocationFsxLustre_RequestSyntax")**

The Amazon Resource Name (ARN) of the FSx for Lustre location to describe.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "SecurityGroupArns": [ "***string***" ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeLocationFsxLustre_ResponseSyntax "#API_DescribeLocationFsxLustre_ResponseSyntax")**

The time that the FSx for Lustre location was created.

Type: Timestamp

**[LocationArn](#API_DescribeLocationFsxLustre_ResponseSyntax "#API_DescribeLocationFsxLustre_ResponseSyntax")**

The Amazon Resource Name (ARN) of the FSx for Lustre location that was
described.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationFsxLustre_ResponseSyntax "#API_DescribeLocationFsxLustre_ResponseSyntax")**

The URI of the FSx for Lustre location that was described.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[SecurityGroupArns](#API_DescribeLocationFsxLustre_ResponseSyntax "#API_DescribeLocationFsxLustre_ResponseSyntax")**

The Amazon Resource Names (ARNs) of the security groups that are configured for the
FSx for Lustre file system.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxLustre.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxLustre.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxLustre.md")
