# TagResource

Creates a tag for an EFS resource. You can create tags for EFS file
systems and access points using this API operation.

This operation requires permissions for the `elasticfilesystem:TagResource` action.

## Request Syntax

```
POST /2015-02-01/resource-tags/`ResourceId` HTTP/1.1
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

**[ResourceId](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The ID specifying the EFS resource that you want to create a tag for.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

An array of `Tag` objects to add. Each `Tag` object is a key-value
pair.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: Yes

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

## Examples

### Create Tags on a File System

The following request creates three tags (`"key1"`, `"key2"`,
and `"key3"`) on the specified file system.

#### Sample Request

```
POST /2015-02-01/tag-resource/fs-01234567 HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20140620T221118Z
Authorization: <...>
Content-Type: application/json
Content-Length: 160

{
    "Tags": [
        {
            "Key": "key1",
            "Value": "value1"
        },
        {
            "Key": "key2",
            "Value": "value2"
        },
        {
            "Key": "key3",
            "Value": "value3"
        }
    ]
}

```

#### Sample Response

```
HTTP/1.1 204 no content
x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/cli2/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/boto3/elasticfilesystem-2015-02-01/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/TagResource.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/TagResource.md")
