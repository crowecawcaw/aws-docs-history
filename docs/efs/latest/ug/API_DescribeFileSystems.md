# DescribeFileSystems

Returns the description of a specific Amazon EFS file system if either the file system
`CreationToken` or the `FileSystemId` is provided. Otherwise, it
returns descriptions of all file systems owned by the caller's AWS account in the
AWS Region of the endpoint that you're calling.

When retrieving all file system descriptions, you can optionally specify the
`MaxItems` parameter to limit the number of descriptions in a response.
This number is automatically set to 100. If more file system descriptions remain,
Amazon EFS returns a `NextMarker`, an opaque token, in the response. In this case,
you should send a subsequent request with the `Marker` request parameter set to the
value of `NextMarker`.

To retrieve a list of your file system descriptions, this operation is used in an
iterative process, where `DescribeFileSystems` is called first without the
`Marker` and then the operation continues to call it with the `Marker`
parameter set to the value of the `NextMarker` from the previous response until the
response has no `NextMarker`.

The order of file systems returned in the response of one
`DescribeFileSystems` call and the order of file systems returned across the
responses of a multi-call iteration is unspecified.

This operation requires permissions for the
`elasticfilesystem:DescribeFileSystems` action.

## Request Syntax

```
GET /2015-02-01/file-systems?CreationToken=`CreationToken`&FileSystemId=`FileSystemId`&Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[CreationToken](#API_DescribeFileSystems_RequestSyntax "#API_DescribeFileSystems_RequestSyntax")**

(Optional) Restricts the list to the file system with this creation token (String). You
specify a creation token when you create an Amazon EFS file system.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

**[FileSystemId](#API_DescribeFileSystems_RequestSyntax "#API_DescribeFileSystems_RequestSyntax")**

(Optional) ID of the file system whose description you want to retrieve
(String).

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[Marker](#API_DescribeFileSystems_RequestSyntax "#API_DescribeFileSystems_RequestSyntax")**

(Optional) Opaque pagination token returned from a previous
`DescribeFileSystems` operation (String). If present, specifies to continue the
list from where the returning call had left off.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[MaxItems](#API_DescribeFileSystems_RequestSyntax "#API_DescribeFileSystems_RequestSyntax")**

(Optional) Specifies the maximum number of file systems to return in the response
(integer). This number is automatically set to 100. The response is paginated at 100 per page if you have more than 100 file systems.

Valid Range: Minimum value of 1.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "FileSystems": [
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
   ],
   "Marker": "***string***",
   "NextMarker": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[FileSystems](#API_DescribeFileSystems_ResponseSyntax "#API_DescribeFileSystems_ResponseSyntax")**

An array of file system descriptions.

Type: Array of [FileSystemDescription](API_FileSystemDescription.md "API_FileSystemDescription.md") objects

**[Marker](#API_DescribeFileSystems_ResponseSyntax "#API_DescribeFileSystems_ResponseSyntax")**

Present if provided by caller in the request (String).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[NextMarker](#API_DescribeFileSystems_ResponseSyntax "#API_DescribeFileSystems_ResponseSyntax")**

Present if there are more file systems than returned in the response (String). You can
use the `NextMarker` in the subsequent request to fetch the descriptions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

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

## Examples

### Retrieve a list of 10 file systems

The following example sends a GET request to the `file-systems`
endpoint (`elasticfilesystem.us-west-2.amazonaws.com/2015-02-01/file-systems`).
The request specifies a `MaxItems` query parameter to limit the number of file
system descriptions to 10.

#### Sample Request

```
GET /2015-02-01/file-systems?MaxItems=10 HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140622T191208Z
Authorization: <...>
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 499
{
   "FileSystems":[
      {
         "OwnerId":"251839141158",
         "CreationToken":"MyFileSystem1",
         "FileSystemId":"fs-01234567",
         "PerformanceMode" : "generalPurpose",
         "CreationTime":"1403301078",
         "LifeCycleState":"created",
         "Name":"my first file system",
         "NumberOfMountTargets":1,
         "SizeInBytes":{
            "Timestamp": 1403301078,
            "Value": 29313618372,
            "ValueInArchive": 201156,
            "ValueInIA": 675432,
            "ValueInStandard": 29312741784
         }
      }
   ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeFileSystems.md")
