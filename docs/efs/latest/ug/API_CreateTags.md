# CreateTags

###### Note

DEPRECATED - `CreateTags` is deprecated and not maintained. To create tags for EFS
resources, use the [TagResource](API_TagResource.md "API_TagResource.md") API action.

Creates or overwrites tags associated with a file system. Each tag is a key-value pair. If
a tag key specified in the request already exists on the file system, this operation
overwrites its value with the value provided in the request. If you add the `Name`
tag to your file system, Amazon EFS returns it in the response to the [DescribeFileSystems](API_DescribeFileSystems.md "API_DescribeFileSystems.md") operation.

This operation requires permission for the `elasticfilesystem:CreateTags`
action.

## Request Syntax

```
POST /2015-02-01/create-tags/`FileSystemId` HTTP/1.1
Content-type: application/json

{
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_CreateTags_RequestSyntax "#API_CreateTags_RequestSyntax")**

The ID of the file system whose tags you want to modify (String). This operation modifies
the tags only, not the file system.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Tags](#API_CreateTags_RequestSyntax "#API_CreateTags_RequestSyntax")**

An array of `Tag` objects to add. Each `Tag` object is a key-value
pair.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/cli2/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/boto3/elasticfilesystem-2015-02-01/CreateTags.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateTags.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreateTags.md")
