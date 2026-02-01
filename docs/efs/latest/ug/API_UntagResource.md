# UntagResource

Removes tags from an EFS resource. You can remove tags from EFS file
systems and access points using this API operation.

This operation requires permissions for the `elasticfilesystem:UntagResource` action.

## Request Syntax

```
DELETE /2015-02-01/resource-tags/`ResourceId`?tagKeys=`TagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ResourceId](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

Specifies the EFS resource that you want to remove tags from.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`

Required: Yes

**[TagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The keys of the key-value tag pairs that you want to remove from the specified
EFS resource.

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/cli2/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/boto3/elasticfilesystem-2015-02-01/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UntagResource.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/UntagResource.md")
