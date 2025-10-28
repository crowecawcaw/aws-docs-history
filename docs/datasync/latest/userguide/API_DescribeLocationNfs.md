# DescribeLocationNfs

Provides details about how an AWS DataSync transfer location for a Network
File System (NFS) file server is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationNfs_RequestSyntax "#API_DescribeLocationNfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the NFS location that you want information
about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "MountOptions": {
      "Version": "***string***"
   },
   "OnPremConfig": {
      "AgentArns": [ "***string***" ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeLocationNfs_ResponseSyntax "#API_DescribeLocationNfs_ResponseSyntax")**

The time when the NFS location was created.

Type: Timestamp

**[LocationArn](#API_DescribeLocationNfs_ResponseSyntax "#API_DescribeLocationNfs_ResponseSyntax")**

The ARN of the NFS location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationNfs_ResponseSyntax "#API_DescribeLocationNfs_ResponseSyntax")**

The URI of the NFS location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[MountOptions](#API_DescribeLocationNfs_ResponseSyntax "#API_DescribeLocationNfs_ResponseSyntax")**

The mount options that DataSync uses to mount your NFS file server.

Type: [NfsMountOptions](API_NfsMountOptions.md "API_NfsMountOptions.md") object

**[OnPremConfig](#API_DescribeLocationNfs_ResponseSyntax "#API_DescribeLocationNfs_ResponseSyntax")**

The AWS DataSync agents that can connect to your Network File System (NFS)
file server.

Type: [OnPremConfig](API_OnPremConfig.md "API_OnPremConfig.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Example

The following example returns information about the NFS location specified in the
sample request.

#### Sample Request

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa"
}
```

### Example

This example illustrates one usage of DescribeLocationNfs.

#### Sample Response

```
{
   "CreationTime": 1532660733.39,
   "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa",
   "LocationUri": "hostname.amazon.com",
   "OnPremConfig": {
      "AgentArns": [ "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs" ]
   }
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationNfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationNfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationNfs.md")
