# DescribeReplicationConfigurations

Retrieves the replication configuration for a specific file system. If a file system is
not specified, all of the replication configurations for the AWS account in an
AWS Region are retrieved.

## Request Syntax

```
GET /2015-02-01/file-systems/replication-configurations?FileSystemId=`FileSystemId`&MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_DescribeReplicationConfigurations_RequestSyntax "#API_DescribeReplicationConfigurations_RequestSyntax")**

You can retrieve the replication configuration for a specific file system by providing its
file system ID. For cross-account,cross-region replication, an account can only describe the replication
configuration for a file system in its own Region.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[MaxResults](#API_DescribeReplicationConfigurations_RequestSyntax "#API_DescribeReplicationConfigurations_RequestSyntax")**

(Optional) To limit the number of objects returned in a response, you can specify the
`MaxItems` parameter. The default value is 100.

Valid Range: Minimum value of 1.

**[NextToken](#API_DescribeReplicationConfigurations_RequestSyntax "#API_DescribeReplicationConfigurations_RequestSyntax")**

`NextToken` is present if the response is paginated. You can use
`NextToken` in a subsequent request to fetch the next page of
output.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Replications": [
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
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeReplicationConfigurations_ResponseSyntax "#API_DescribeReplicationConfigurations_ResponseSyntax")**

You can use the `NextToken` from the previous response in a subsequent
request to fetch the additional descriptions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[Replications](#API_DescribeReplicationConfigurations_ResponseSyntax "#API_DescribeReplicationConfigurations_ResponseSyntax")**

The collection of replication configurations that is returned.

Type: Array of [ReplicationConfigurationDescription](API_ReplicationConfigurationDescription.md "API_ReplicationConfigurationDescription.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeReplicationConfigurations.md")
