# ListTagsForResource

Lists all tags for a top-level EFS resource. You must provide the ID of the
resource that you want to retrieve the tags for.

This operation requires permissions for the `elasticfilesystem:DescribeAccessPoints` action.

## Request Syntax

```
GET /2015-02-01/resource-tags/`ResourceId`?MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

(Optional) Specifies the maximum number of tag objects to return in the response. The default value is 100.

Valid Range: Minimum value of 1.

**[NextToken](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

(Optional) You can use `NextToken` in a subsequent request to fetch the next page of access point descriptions if the response payload was paginated.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[ResourceId](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

Specifies the EFS resource you want to retrieve tags for. You can retrieve tags
for EFS file systems and access points using this API endpoint.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:(access-point/fsap|file-system/fs)-[0-9a-f]{8,40}|fs(ap)?-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

`NextToken` is present if the response payload is paginated. You can use `NextToken` in a subsequent request to fetch the next page of access point descriptions.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `.+`

**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

An array of the tags for the specified EFS resource.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/cli2/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/DotNetSDKV3/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/boto3/elasticfilesystem-2015-02-01/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ListTagsForResource.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ListTagsForResource.md")
