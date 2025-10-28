# DescribeLifecycleConfiguration

Returns the current `LifecycleConfiguration` object for the specified
EFS file system. Lifecycle management uses the `LifecycleConfiguration`
object to identify when to move files between storage classes. For a file system without a
`LifecycleConfiguration` object, the call returns an empty array in the
response.

This operation requires permissions for the
`elasticfilesystem:DescribeLifecycleConfiguration` operation.

## Request Syntax

```
GET /2015-02-01/file-systems/`FileSystemId`/lifecycle-configuration HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_DescribeLifecycleConfiguration_RequestSyntax "#API_DescribeLifecycleConfiguration_RequestSyntax")**

The ID of the file system whose `LifecycleConfiguration` object you want to
retrieve (String).

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "LifecyclePolicies": [
      {
         "TransitionToArchive": "***string***",
         "TransitionToIA": "***string***",
         "TransitionToPrimaryStorageClass": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LifecyclePolicies](#API_DescribeLifecycleConfiguration_ResponseSyntax "#API_DescribeLifecycleConfiguration_ResponseSyntax")**

An array of lifecycle management policies. EFS supports a maximum of one
policy per file system.

Type: Array of [LifecyclePolicy](API_LifecyclePolicy.md "API_LifecyclePolicy.md") objects

Array Members: Maximum number of 3 items.

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

### Retrieve the lifecycle configuration for a file system

The following request retrieves the `LifecycleConfiguration` object for the
specified file system.

#### Sample Request

```
GET /2015-02-01/file-systems/fs-01234567/lifecycle-configuration HTTP/1.1
Host: elasticfilesystem.us-west-2.amazonaws.com
x-amz-date: 20181120T221118Z
Authorization: <...>


```

#### Sample Response

```
HTTP/1.1 200 OK
        x-amzn-RequestId: 01234567-89ab-cdef-0123-456789abcdef
        Content-Type: application/json
        Content-Length: 86
{
  "LifecyclePolicies": [
    {
        "TransitionToArchive": "AFTER_270_DAYS"
    },
    {
        "TransitionToIA": "AFTER_14_DAYS"
    },
    {
        "TransitionToPrimaryStorageClass": "AFTER_1_ACCESS"
    }
  ]
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DescribeLifecycleConfiguration.md")
