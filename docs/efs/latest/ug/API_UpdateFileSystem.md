# UpdateFileSystem

Updates the throughput mode or the amount of provisioned throughput of an existing file
system.

## Request Syntax

```
PUT /2015-02-01/file-systems/`FileSystemId` HTTP/1.1
Content-type: application/json

{
   "ProvisionedThroughputInMibps": `number`,
   "ThroughputMode": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_UpdateFileSystem_RequestSyntax "#API_UpdateFileSystem_RequestSyntax")**

The ID of the file system that you want to update.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[ProvisionedThroughputInMibps](#API_UpdateFileSystem_RequestSyntax "#API_UpdateFileSystem_RequestSyntax")**

(Optional) The throughput, measured in mebibytes per second (MiBps), that you want to
provision for a file system that you're creating. Required if `ThroughputMode`
is set to `provisioned`. Valid values are 1-3414 MiBps, with the upper limit
depending on Region. To increase this limit, contact Support. For more information,
see [Amazon EFS
quotas that you can increase](limits.md#soft-limits "limits.md#soft-limits") in the _Amazon EFS User
Guide_.

Type: Double

Valid Range: Minimum value of 1.0.

Required: No

**[ThroughputMode](#API_UpdateFileSystem_RequestSyntax "#API_UpdateFileSystem_RequestSyntax")**

(Optional) Updates the file system's throughput mode. If you're not
updating your throughput mode, you don't need to provide this value in your
request. If you are changing the `ThroughputMode` to `provisioned`,
you must also set a value for `ProvisionedThroughputInMibps`.

Type: String

Valid Values: `bursting | provisioned | elastic`

Required: No

## Response Syntax

```
HTTP/1.1 202
Content-type: application/json

{
   "AvailabilityZoneId": "***string***",
   "AvailabilityZoneName": "***string***",
   "CreationTime": ***number***,
   "CreationToken": "***string***",
   "Encrypted": ***boolean***,
   "FileSystemArn": "***string***",
   "FileSystemId": "***string***",
   "FileSystemProtection": {
      "ReplicationOverwriteProtection": "***string***"
   },
   "KmsKeyId": "***string***",
   "LifeCycleState": "***string***",
   "Name": "***string***",
   "NumberOfMountTargets": ***number***,
   "OwnerId": "***string***",
   "PerformanceMode": "***string***",
   "ProvisionedThroughputInMibps": ***number***,
   "SizeInBytes": {
      "Timestamp": ***number***,
      "Value": ***number***,
      "ValueInArchive": ***number***,
      "ValueInIA": ***number***,
      "ValueInStandard": ***number***
   },
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ],
   "ThroughputMode": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

**[AvailabilityZoneId](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The unique and consistent identifier of the Availability Zone in which the file system is
located, and is valid only for One Zone file systems. For example,
`use1-az1` is an Availability Zone ID for the us-east-1 AWS Region, and
it has the same location in every AWS account.

Type: String

**[AvailabilityZoneName](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

Describes the AWS Availability Zone in which the file system is located, and is
valid only for One Zone file systems. For more information, see [Using EFS storage
classes](storage-classes.md "storage-classes.md") in the _Amazon EFS User Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

**[CreationTime](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The time that the file system was created, in seconds (since
1970-01-01T00:00:00Z).

Type: Timestamp

**[CreationToken](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The opaque string specified in the request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

**[Encrypted](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

A Boolean value that, if true, indicates that the file system is encrypted.

Type: Boolean

**[FileSystemArn](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The Amazon Resource Name (ARN) for the EFS file system, in the
format
`arn:aws:elasticfilesystem:*region*:*account-id*:file-system/*file-system-id*`.
Example with sample data:
`arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-01234567`

Type: String

**[FileSystemId](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The ID of the file system, assigned by Amazon EFS.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[FileSystemProtection](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

Describes the protection on the file system.

Type: [FileSystemProtectionDescription](API_FileSystemProtectionDescription.md "API_FileSystemProtectionDescription.md") object

**[KmsKeyId](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The ID of an AWS KMS key used to protect the encrypted file system.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`

**[LifeCycleState](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The lifecycle phase of the file system.

Type: String

Valid Values: `creating | available | updating | deleting | deleted | error`

**[Name](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

You can add tags to a file system, including a `Name` tag. For more
information, see [CreateFileSystem](API_CreateFileSystem.md "API_CreateFileSystem.md"). If the file system has a `Name` tag, Amazon EFS returns
the value in this field.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

**[NumberOfMountTargets](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The current number of mount targets that the file system has. For more information, see [CreateMountTarget](API_CreateMountTarget.md "API_CreateMountTarget.md").

Type: Integer

Valid Range: Minimum value of 0.

**[OwnerId](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The AWS account that created the file system.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

**[PerformanceMode](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The performance mode of the file system.

Type: String

Valid Values: `generalPurpose | maxIO`

**[ProvisionedThroughputInMibps](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The amount of provisioned throughput, measured in MiBps, for the file system. Valid for
file systems using `ThroughputMode` set to `provisioned`.

Type: Double

Valid Range: Minimum value of 1.0.

**[SizeInBytes](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The latest known metered size (in bytes) of data stored in the file system, in its
`Value` field, and the time at which that size was determined in its
`Timestamp` field. The `Timestamp` value is the integer number of
seconds since 1970-01-01T00:00:00Z. The `SizeInBytes` value doesn't represent
the size of a consistent snapshot of the file system, but it is eventually consistent when
there are no writes to the file system. That is, `SizeInBytes` represents actual
size only if the file system is not modified for a period longer than a couple of hours.
Otherwise, the value is not the exact size that the file system was at any point in time.

Type: [FileSystemSize](API_FileSystemSize.md "API_FileSystemSize.md") object

**[Tags](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

The tags associated with the file system, presented as an array of `Tag`
objects.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

**[ThroughputMode](#API_UpdateFileSystem_ResponseSyntax "#API_UpdateFileSystem_ResponseSyntax")**

Displays the file system's throughput mode. For more information, see
[Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes")
in the _Amazon EFS User Guide_.

Type: String

Valid Values: `bursting | provisioned | elastic`

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/cli2/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/boto3/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UpdateFileSystem.md")
