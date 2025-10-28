# DeleteTags

###### Note

DEPRECATED - `DeleteTags` is deprecated and not maintained. To remove tags from EFS
resources, use the [UntagResource](API_UntagResource.md "API_UntagResource.md") API action.

Deletes the specified tags from a file system. If the `DeleteTags` request
includes a tag key that doesn't exist, Amazon EFS ignores it and doesn't cause an
error. For more information about tags and related restrictions, see [Tag restrictions](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
_AWS Billing and Cost Management User Guide_.

This operation requires permissions for the `elasticfilesystem:DeleteTags`
action.

## Request Syntax

```
POST /2015-02-01/delete-tags/`FileSystemId` HTTP/1.1
Content-type: application/json

{
   "TagKeys": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_DeleteTags_RequestSyntax "#API_DeleteTags_RequestSyntax")**

The ID of the file system whose tags you want to delete (String).

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[TagKeys](#API_DeleteTags_RequestSyntax "#API_DeleteTags_RequestSyntax")**

A list of tag keys to delete.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^(?![aA]{1}[wW]{1}[sS]{1}:)([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`

Required: Yes

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteTags.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteTags.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteTags.md")
