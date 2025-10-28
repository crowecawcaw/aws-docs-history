# DeleteFileSystem

Deletes a file system, permanently severing access to its contents. Upon return, the
file system no longer exists and you can't access any contents of the deleted file
system.

You need to manually delete mount targets attached to a file system before you can delete
an EFS file system. This step is performed for you when you use the AWS console
to delete a file system.

###### Note

You cannot delete a file system that is part of an EFS replication configuration.
You need to delete the replication configuration first.

You can't delete a file system that is in use. That is, if the file system has
any mount targets, you must first delete them. For more information, see [DescribeMountTargets](API_DescribeMountTargets.md "API_DescribeMountTargets.md") and [DeleteMountTarget](API_DeleteMountTarget.md "API_DeleteMountTarget.md").

###### Note

The `DeleteFileSystem` call returns while the file system state is still
`deleting`. You can check the file system deletion status by calling the [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md") operation, which returns a list of file systems in your
account. If you pass file system ID or creation token for the deleted file system, the [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md") returns a `404 FileSystemNotFound`
error.

This operation requires permissions for the
`elasticfilesystem:DeleteFileSystem` action.

## Request Syntax

```
DELETE /2015-02-01/file-systems/`FileSystemId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_DeleteFileSystem_RequestSyntax "#API_DeleteFileSystem_RequestSyntax")**

The ID of the file system you want to delete.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

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

**FileSystemInUse**

Returned if a file system has mount targets.

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

### Delete a file system

The following example sends a DELETE request to the `file-systems` endpoint
(`elasticfilesystem.us-west-2.amazonaws.com/2015-02-01/file-systems/fs-01234567`)
to delete a file system whose ID is `fs-01234567`.

#### Sample Request

```
DELETE /2015-02-01/file-systems/fs-01234567 HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140622T233021Z
Authorization: <...>
```

#### Sample Response

```
HTTP/1.1 204 No Content
x-amzn-RequestId: a2d125b3-7ebd-4d6a-ab3d-5548630bff33
Content-Length: 0
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteFileSystem.md")
