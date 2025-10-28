# DescribeBackupPolicy

Returns the backup policy for the specified EFS file system.

## Request Syntax

```
GET /2015-02-01/file-systems/`FileSystemId`/backup-policy HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_DescribeBackupPolicy_RequestSyntax "#API_DescribeBackupPolicy_RequestSyntax")**

Specifies which EFS file system for which to retrieve the
`BackupPolicy`.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BackupPolicy": {
      "Status": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BackupPolicy](#API_DescribeBackupPolicy_ResponseSyntax "#API_DescribeBackupPolicy_ResponseSyntax")**

Describes the file system's backup policy, indicating whether automatic backups are
turned on or off.

Type: [BackupPolicy](API_BackupPolicy.md "API_BackupPolicy.md") object

## Errors

**BadRequest**

Returned if the request is malformed or contains an error such as an invalid
parameter value or a missing required parameter.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**FileSystemNotFound**

Returned if the specified `FileSystemId` value doesn't exist in the
requester's AWS account.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

**InternalServerError**

Returned if an error occurred on the server side.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 500

**PolicyNotFound**

Returned if the specified IAM policy or resource policy cannot be located or accessed. Depending on the action being performed, the error may also be returned if the default file system policy
is in effect for the EFS file system or if no backup policy is specified.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

**ValidationException**

Returned if the AWS Backup service is not available in the AWS Region in which the request was made.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeBackupPolicy.md")
