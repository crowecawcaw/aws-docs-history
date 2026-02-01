# DescribeMountTargetSecurityGroups

Returns the security groups currently in effect for a mount target. This operation
requires that the network interface of the mount target has been created and the lifecycle
state of the mount target is not `deleted`.

This operation requires permissions for the following actions:

- `elasticfilesystem:DescribeMountTargetSecurityGroups` action on the mount
  target's file system.
- `ec2:DescribeNetworkInterfaceAttribute` action on the mount target's
  network interface.

## Request Syntax

```
GET /2015-02-01/mount-targets/`MountTargetId`/security-groups HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MountTargetId](#API_DescribeMountTargetSecurityGroups_RequestSyntax "#API_DescribeMountTargetSecurityGroups_RequestSyntax")**

The ID of the mount target whose security groups you want to retrieve.

Length Constraints: Minimum length of 13. Maximum length of 45.

Pattern: `^fsmt-[0-9a-f]{8,40}$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "SecurityGroups": [ "***string***" ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[SecurityGroups](#API_DescribeMountTargetSecurityGroups_ResponseSyntax "#API_DescribeMountTargetSecurityGroups_ResponseSyntax")**

An array of security groups.

Type: Array of strings

Array Members: Maximum number of 100 items.

Length Constraints: Minimum length of 11. Maximum length of 43.

Pattern: `^sg-[0-9a-f]{8,40}`

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

**IncorrectMountTargetState**

Returned if the mount target is not in the correct state for the
operation.

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

### Retrieve security groups in effect for a file system

The following example retrieves the security groups that are in effect for the
network interface associated with a mount target.

#### Sample Request

```
GET /2015-02-01/mount-targets/fsmt-9a13661e/security-groups HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T223513Z
Authorization: <...>
```

#### Sample Response

```
HTTP/1.1 200 OK
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
Content-Length: 57

{
"SecurityGroups" : [
"sg-188d9f74"
]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeMountTargetSecurityGroups.md")
