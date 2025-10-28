# TagResource

Adds one or more tags to a signaling channel. A _tag_ is a
key-value pair (the value is optional) that you can define and assign to AWS resources.
If you specify a tag that already exists, the tag value is replaced with the value that
you specify in the request. For more information, see [Using Cost Allocation
Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing and Cost Management and Cost Management User
Guide_.

## Request Syntax

```
POST /TagResource HTTP/1.1
Content-type: application/json

{
   "ResourceARN": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ResourceARN](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The Amazon Resource Name (ARN) of the signaling channel to which you want to add
tags.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Pattern: `arn:[a-z\d-]+:kinesisvideo:[a-z0-9-]+:[0-9]+:[a-z]+/[a-zA-Z0-9_.-]+/[0-9]+`

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

A list of tags to associate with the specified signaling channel. Each tag is a
key-value pair.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 1 item. Maximum number of 50 items.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have required permissions to perform this operation.

HTTP Status Code: 401

**ClientLimitExceededException**

Kinesis Video Streams has throttled the request because you have exceeded the limit of
allowed client calls. Try making the call later.

HTTP Status Code: 400

**InvalidArgumentException**

The value for this input parameter is invalid.

HTTP Status Code: 400

**ResourceNotFoundException**

Amazon Kinesis Video Streams can't find the stream that you specified.

HTTP Status Code: 404

**TagsPerResourceExceededLimitException**

You have exceeded the limit of tags that you can associate with the resource.
A Kinesis video stream can support up to 50 tags.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kinesisvideo-2017-09-30/TagResource.md "../../../goto/cli2/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/TagResource.md "../../../goto/DotNetSDKV3/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForGoV2/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForJavaScriptV3/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForKotlin/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForPHPV3/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/kinesisvideo-2017-09-30/TagResource.md "../../../goto/boto3/kinesisvideo-2017-09-30/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/TagResource.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/TagResource.md")
