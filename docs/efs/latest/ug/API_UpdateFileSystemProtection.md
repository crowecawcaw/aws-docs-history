# UpdateFileSystemProtection

Updates protection on the file system.

This operation requires permissions for the
`elasticfilesystem:UpdateFileSystemProtection` action.

## Request Syntax

```
PUT /2015-02-01/file-systems/`FileSystemId`/protection HTTP/1.1
Content-type: application/json

{
   "ReplicationOverwriteProtection": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_UpdateFileSystemProtection_RequestSyntax "#API_UpdateFileSystemProtection_RequestSyntax")**

The ID of the file system to update.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[ReplicationOverwriteProtection](#API_UpdateFileSystemProtection_RequestSyntax "#API_UpdateFileSystemProtection_RequestSyntax")**

The status of the file system's replication overwrite protection.

- `ENABLED` – The file system cannot be used as the destination file
  system in a replication configuration. The file system is writeable. Replication overwrite
  protection is `ENABLED` by default.
- `DISABLED` – The file system can be used as the destination file
  system in a replication configuration. The file system is read-only and can only be
  modified by EFS replication.
- `REPLICATING` – The file system is being used as the destination file
  system in a replication configuration. The file system is read-only and is only modified
  only by EFS replication.

If the replication configuration is deleted, the file system's replication overwrite
protection is re-enabled and the file system becomes writeable.

Type: String

Valid Values: `ENABLED | DISABLED | REPLICATING`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ReplicationOverwriteProtection": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ReplicationOverwriteProtection](#API_UpdateFileSystemProtection_ResponseSyntax "#API_UpdateFileSystemProtection_ResponseSyntax")**

The status of the file system's replication overwrite protection.

- `ENABLED` – The file system cannot be used as the destination file
  system in a replication configuration. The file system is writeable. Replication overwrite
  protection is `ENABLED` by default.
- `DISABLED` – The file system can be used as the destination file
  system in a replication configuration. The file system is read-only and can only be
  modified by EFS replication.
- `REPLICATING` – The file system is being used as the destination
  file system in a replication configuration. The file system is read-only and is modified
  only by EFS replication.

If the replication configuration is deleted, the file system's replication overwrite
protection is re-enabled, the file system becomes writeable.

Type: String

Valid Values: `ENABLED | DISABLED | REPLICATING`

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

**IncorrectFileSystemLifeCycleState**

Returned if the file system's lifecycle state is not "available".

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**InsufficientThroughputCapacity**

Returned if there's not enough capacity to provision additional throughput. This value
might be returned when you try to create a file system in provisioned throughput mode,
when you attempt to increase the provisioned throughput of an existing file system, or
when you attempt to change an existing file system from Bursting Throughput to
Provisioned Throughput mode. Try again later.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 503

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

**ReplicationAlreadyExists**

Returned if the file system is already included in a replication configuration.>

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**ThroughputLimitExceeded**

Returned if the throughput mode or amount of provisioned throughput can't be changed
because the throughput limit of 1024 MiB/s has been reached.

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

**TooManyRequests**

Returned if you don’t wait at least 24 hours before either changing the throughput mode, or
decreasing the Provisioned Throughput value.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 429

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/cli2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/boto3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UpdateFileSystemProtection.md")
