# DeleteMountTarget

Deletes the specified mount target.

This operation forcibly breaks any mounts of the file system by using the mount target
that is being deleted, which might disrupt instances or applications using those mounts. To
avoid applications getting cut off abruptly, you might consider unmounting any mounts of the
mount target, if feasible. The operation also deletes the associated network interface.
Uncommitted writes might be lost, but breaking a mount target using this operation does not
corrupt the file system itself. The file system you created remains. You can mount an
EC2 instance in your VPC by using another mount target.

This operation requires permissions for the following action on the file
system:

- `elasticfilesystem:DeleteMountTarget`

###### Note

The `DeleteMountTarget` call returns while the mount target state is still
`deleting`. You can check the mount target deletion by calling the [DescribeMountTargets](API_DescribeMountTargets.md "API_DescribeMountTargets.md") operation, which returns a list of mount target
descriptions for the given file system.

The operation also requires permissions for the following Amazon EC2 action on the
mount target's network interface:

- `ec2:DeleteNetworkInterface`

## Request Syntax

```
DELETE /2015-02-01/mount-targets/`MountTargetId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MountTargetId](#API_DeleteMountTarget_RequestSyntax "#API_DeleteMountTarget_RequestSyntax")**

The ID of the mount target to delete (String).

Length Constraints: Minimum length of 13. Maximum length of 45.

Pattern: `^fsmt-[0-9a-f]{8,40}$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

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

**DependencyTimeout**

The service timed out trying to fulfill the request, and the client should try the
call again.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 504

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

### Remove a file system's mount target

The following example sends a DELETE request to delete a specific mount target.

#### Sample Request

```
DELETE /2015-02-01/mount-targets/fsmt-9a13661e HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140622T232908Z
Authorization: <...>
```

#### Sample Response

```
HTTP/1.1 204 No Content
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteMountTarget.md")
