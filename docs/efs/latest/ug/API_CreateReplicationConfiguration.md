# CreateReplicationConfiguration

Creates a replication conﬁguration to either a new or existing EFS file system.
For more information, see [Amazon EFS replication](efs-replication.md "efs-replication.md") in the _Amazon EFS User
Guide_. The replication configuration specifies the following:

- **Source file system** – The EFS file
  system that you want to replicate.
- **Destination file system** – The destination file
  system to which the source file system is replicated. There can only be one destination
  file system in a replication configuration.

###### Note

A file system can be part of only one replication configuration.

The destination parameters for the replication configuration depend on
whether you are replicating to a new file system or to an existing file system, and if you
are replicating across AWS accounts. See [DestinationToCreate](API_DestinationToCreate.md "API_DestinationToCreate.md") for more information.
This operation requires permissions for the `elasticfilesystem:CreateReplicationConfiguration`
action. Additionally, other permissions are required depending on how you are replicating file systems.
For more information, see [Required permissions for replication](efs-replication.md#efs-replication-permissions "efs-replication.md#efs-replication-permissions")
in the _Amazon EFS User
Guide_.

## Request Syntax

```
POST /2015-02-01/file-systems/`SourceFileSystemId`/replication-configuration HTTP/1.1
Content-type: application/json

{
   "Destinations": [
      {
         "AvailabilityZoneName": "`string`",
         "FileSystemId": "`string`",
         "KmsKeyId": "`string`",
         "Region": "`string`",
         "RoleArn": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[SourceFileSystemId](#API_CreateReplicationConfiguration_RequestSyntax "#API_CreateReplicationConfiguration_RequestSyntax")**

Specifies the Amazon EFS file system that you want to replicate. This file system cannot already be
a source or destination file system in another replication configuration.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Destinations](#API_CreateReplicationConfiguration_RequestSyntax "#API_CreateReplicationConfiguration_RequestSyntax")**

An array of destination configuration objects. Only one destination configuration object is supported.

Type: Array of [DestinationToCreate](API_DestinationToCreate.md "API_DestinationToCreate.md") objects

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreationTime": ***number***,
   "Destinations": [
      {
         "FileSystemId": "***string***",
         "LastReplicatedTimestamp": ***number***,
         "OwnerId": "***string***",
         "Region": "***string***",
         "RoleArn": "***string***",
         "Status": "***string***",
         "StatusMessage": "***string***"
      }
   ],
   "OriginalSourceFileSystemArn": "***string***",
   "SourceFileSystemArn": "***string***",
   "SourceFileSystemId": "***string***",
   "SourceFileSystemOwnerId": "***string***",
   "SourceFileSystemRegion": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

Describes when the replication configuration was created.

Type: Timestamp

**[Destinations](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

An array of destination objects. Only one destination object is supported.

Type: Array of [Destination](API_Destination.md "API_Destination.md") objects

**[OriginalSourceFileSystemArn](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the original source EFS file
system in the replication configuration.

Type: String

**[SourceFileSystemArn](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the current source file system in the
replication configuration.

Type: String

**[SourceFileSystemId](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

The ID of the source Amazon EFS file system that is being replicated.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[SourceFileSystemOwnerId](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

ID of the AWS account in which the source file system resides.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

**[SourceFileSystemRegion](#API_CreateReplicationConfiguration_ResponseSyntax "#API_CreateReplicationConfiguration_ResponseSyntax")**

The AWS Region in which the source EFS file system is
located.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`

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

**ConflictException**

Returned if the source file system in a replication is encrypted but the destination file system is unencrypted.

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

**FileSystemLimitExceeded**

Returned if the AWS account has already created the maximum number of file systems
allowed per account.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 403

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

**ReplicationNotFound**

Returned if the specified file system does not have a replication
configuration.

**ErrorCode**

ReplicationNotFound

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

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

**UnsupportedAvailabilityZone**

Returned if the requested Amazon EFS functionality is not available in the specified Availability Zone.

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/cli2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/boto3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateReplicationConfiguration.md")
