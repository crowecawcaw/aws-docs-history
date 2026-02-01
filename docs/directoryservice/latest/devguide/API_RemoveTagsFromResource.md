# RemoveTagsFromResource

Removes tags from a directory.

## Request Syntax

```
{
   "ResourceId": "`string`",
   "TagKeys": [ "`string`" ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceId](#API_RemoveTagsFromResource_RequestSyntax "#API_RemoveTagsFromResource_RequestSyntax")**

Identifier (ID) of the directory from which to remove the tag.

Type: String

Pattern: `^[d]-[0-9a-f]{10}$`

Required: Yes

**[TagKeys](#API_RemoveTagsFromResource_RequestSyntax "#API_RemoveTagsFromResource_RequestSyntax")**

The tag key (name) of the tag to be removed.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of RemoveTagsFromResource.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 58
X-Amz-Target: DirectoryService_20150416.RemoveTagsFromResource
X-Amz-Date: 20161214T234556Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=707f9d53696de7adc446b3bd54404571011febc29e9b76c6aed793767639bf47

 {
   "ResourceId":"d-926example",
   "TagKeys": ["environment"]
 }
```

### Example Response

This example illustrates one usage of RemoveTagsFromResource.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 767374a0-c257-11e6-ad7a-a9557d30f017
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 23:45:58 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/cli2/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/DotNetSDKV4/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForCpp/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForGoV2/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForKotlin/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForPHPV3/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/boto3/ds-2015-04-16/RemoveTagsFromResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RemoveTagsFromResource.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RemoveTagsFromResource.md")
