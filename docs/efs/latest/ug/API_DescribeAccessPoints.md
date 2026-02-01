# DescribeAccessPoints

Returns the description of a specific Amazon EFS access point if the
`AccessPointId` is provided. If you provide an EFS
`FileSystemId`, it returns descriptions of all access points for that file
system. You can provide either an `AccessPointId` or a `FileSystemId` in
the request, but not both.

This operation requires permissions for the `elasticfilesystem:DescribeAccessPoints` action.

## Request Syntax

```
GET /2015-02-01/access-points?AccessPointId=`AccessPointId`&FileSystemId=`FileSystemId`&MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[AccessPointId](#API_DescribeAccessPoints_RequestSyntax "#API_DescribeAccessPoints_RequestSyntax")**

(Optional) Specifies an EFS access point to describe in the response; mutually
exclusive with `FileSystemId`.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`

**[FileSystemId](#API_DescribeAccessPoints_RequestSyntax "#API_DescribeAccessPoints_RequestSyntax")**

(Optional) If you provide a `FileSystemId`, EFS returns all access
points for that file system; mutually exclusive with `AccessPointId`.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[MaxResults](#API_DescribeAccessPoints_RequestSyntax "#API_DescribeAccessPoints_RequestSyntax")**

(Optional) When retrieving all access points for a file system,
you can optionally specify the `MaxItems` parameter to limit the number of objects returned in a response.
The default value is 100.

Valid Range: Minimum value of 1.

**[NextToken](#API_DescribeAccessPoints_RequestSyntax "#API_DescribeAccessPoints_RequestSyntax")**

`NextToken` is present if the response is paginated. You can use
`NextMarker` in the subsequent request to fetch the next page of access point descriptions.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AccessPoints": [
      {
         "AccessPointArn": "***string***",
         "AccessPointId": "***string***",
         "ClientToken": "***string***",
         "FileSystemId": "***string***",
         "LifeCycleState": "***string***",
         "Name": "***string***",
         "OwnerId": "***string***",
         "PosixUser": {
            "Gid": ***number***,
            "SecondaryGids": [ ***number*** ],
            "Uid": ***number***
         },
         "RootDirectory": {
            "CreationInfo": {
               "OwnerGid": ***number***,
               "OwnerUid": ***number***,
               "Permissions": "***string***"
            },
            "Path": "***string***"
         },
         "Tags": [
            {
               "Key": "***string***",
               "Value": "***string***"
            }
         ]
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccessPoints](#API_DescribeAccessPoints_ResponseSyntax "#API_DescribeAccessPoints_ResponseSyntax")**

An array of access point descriptions.

Type: Array of [AccessPointDescription](API_AccessPointDescription.md "API_AccessPointDescription.md") objects

**[NextToken](#API_DescribeAccessPoints_ResponseSyntax "#API_DescribeAccessPoints_ResponseSyntax")**

Present if there are more access points than returned in the response.
You can use the NextMarker in the subsequent request to fetch the additional descriptions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

## Errors

**AccessPointNotFound**

Returned if the specified `AccessPointId` value doesn't exist in the
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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeAccessPoints.md")
