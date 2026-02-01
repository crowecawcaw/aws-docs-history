# DescribeMountTargets

Returns the descriptions of all the current mount targets, or a specific mount target,
for a file system. When requesting all of the current mount targets, the order of mount
targets returned in the response is unspecified.

This operation requires permissions for the
`elasticfilesystem:DescribeMountTargets` action, on either the file system ID
that you specify in `FileSystemId`, or on the file system of the mount target that
you specify in `MountTargetId`.

The corresponding CLI command is `describe-mount-targets`.

## Request Syntax

```
GET /2015-02-01/mount-targets?AccessPointId=`AccessPointId`&FileSystemId=`FileSystemId`&Marker=`Marker`&MaxItems=`MaxItems`&MountTargetId=`MountTargetId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[AccessPointId](#API_DescribeMountTargets_RequestSyntax "#API_DescribeMountTargets_RequestSyntax")**

(Optional) The ID of the access point whose mount targets that you want to list. It must be included in your request if a
`FileSystemId` or `MountTargetId` is not included in your request. Accepts either an access point ID or ARN as input.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`

**[FileSystemId](#API_DescribeMountTargets_RequestSyntax "#API_DescribeMountTargets_RequestSyntax")**

(Optional) ID of the file system whose mount targets you want to list (String). It must
be included in your request if an `AccessPointId` or `MountTargetId` is not included. Accepts either a file system ID or ARN as input.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[Marker](#API_DescribeMountTargets_RequestSyntax "#API_DescribeMountTargets_RequestSyntax")**

(Optional) Opaque pagination token returned from a previous
`DescribeMountTargets` operation (String). If present, it specifies to continue
the list from where the previous returning call left off.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[MaxItems](#API_DescribeMountTargets_RequestSyntax "#API_DescribeMountTargets_RequestSyntax")**

(Optional) Maximum number of mount targets to return in the response. Currently, this
number is automatically set to
10, and other values are ignored. The response is paginated at 100 per page if you have more than 100 mount targets.

Valid Range: Minimum value of 1.

**[MountTargetId](#API_DescribeMountTargets_RequestSyntax "#API_DescribeMountTargets_RequestSyntax")**

(Optional) ID of the mount target that you want to have described (String). It must be
included in your request if `FileSystemId` is not included. Accepts either a mount target ID or ARN as input.

Length Constraints: Minimum length of 13. Maximum length of 45.

Pattern: `^fsmt-[0-9a-f]{8,40}$`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Marker": "***string***",
   "MountTargets": [
      {
         "AvailabilityZoneId": "***string***",
         "AvailabilityZoneName": "***string***",
         "FileSystemId": "***string***",
         "IpAddress": "***string***",
         "Ipv6Address": "***string***",
         "LifeCycleState": "***string***",
         "MountTargetId": "***string***",
         "NetworkInterfaceId": "***string***",
         "OwnerId": "***string***",
         "SubnetId": "***string***",
         "VpcId": "***string***"
      }
   ],
   "NextMarker": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Marker](#API_DescribeMountTargets_ResponseSyntax "#API_DescribeMountTargets_ResponseSyntax")**

If the request included the `Marker`, the response returns that value in
this field.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[MountTargets](#API_DescribeMountTargets_ResponseSyntax "#API_DescribeMountTargets_ResponseSyntax")**

Returns the file system's mount targets as an array of
`MountTargetDescription` objects.

Type: Array of [MountTargetDescription](API_MountTargetDescription.md "API_MountTargetDescription.md") objects

**[NextMarker](#API_DescribeMountTargets_ResponseSyntax "#API_DescribeMountTargets_ResponseSyntax")**

If a value is present, there are more mount targets to return. In a subsequent request,
you can provide `Marker` in your request with this value to retrieve the next set
of mount targets.

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

**MountTargetNotFound**

Returned if there is no mount target with the specified ID found in the
caller's AWS account.

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

## Examples

### Retrieve descriptions of mount targets created for a file system

The following request retrieves descriptions of mount targets created for the
specified file system.

#### Sample Request

```
GET /2015-02-01/mount-targets?FileSystemId=fs-01234567 HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140622T191252Z
Authorization: <...>
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Type: application/json
Content-Length: 357

{
   "MountTargets":[
      {
         "OwnerId":"251839141158",
         "MountTargetId":"fsmt-01234567",
         "FileSystemId":"fs-01234567",
         "SubnetId":"subnet-01234567",
         "LifeCycleState":"added",
         "IpAddress":"10.0.2.42",
         "NetworkInterfaceId":"eni-1bcb7772"
      }
   ]
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeMountTargets.md")
