Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# TagResource

Associates the specified tags to a resource with the specified `resourceArn`.
If existing tags on a resource are not specified in the request parameters, they are not
changed. When a resource is deleted, the tags associated with that resource are also
deleted.

###### Important

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "http://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

## Request Syntax

```
{
   "ResourceArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The Amazon Resource Name (ARN) that identifies the resource for which to list the tags.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):forecast:.*:.*:.+`

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The tags to add to the resource. A tag is an array of key-value pairs.

The following basic restrictions apply to tags:

- Maximum number of tags per resource - 50.
- For each resource, each tag key must be unique, and each tag key can have only one
  value.
- Maximum key length - 128 Unicode characters in UTF-8.
- Maximum value length - 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember that
  other services may have restrictions on allowed characters. Generally allowed characters
  are: letters, numbers, and spaces representable in UTF-8, and the following characters: +

* = . \_ : / @.

- Tag keys and values are case sensitive.
- Do not use `aws:`, `AWS:`, or any upper or lowercase combination
  of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag
  keys with this prefix. Values can have this prefix. If a tag value has `aws` as
  its prefix but the key does not, then Forecast considers it to be a user tag and will
  count against the limit of 50 tags. Tags with only the key prefix of `aws` do
  not count against your tags per resource limit.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

We can't process the request because it includes an invalid value or a value that exceeds
the valid range.

HTTP Status Code: 400

**LimitExceededException**

The limit on the number of resources per account has been exceeded.

HTTP Status Code: 400

**ResourceNotFoundException**

We can't find a resource with that Amazon Resource Name (ARN). Check the ARN and try
again.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/forecast-2018-06-26/TagResource.md "../../../goto/cli2/forecast-2018-06-26/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/forecast-2018-06-26/TagResource.md "../../../goto/DotNetSDKV3/forecast-2018-06-26/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/forecast-2018-06-26/TagResource.md "../../../goto/SdkForCpp/forecast-2018-06-26/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/forecast-2018-06-26/TagResource.md "../../../goto/SdkForGoV2/forecast-2018-06-26/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/forecast-2018-06-26/TagResource.md "../../../goto/SdkForJavaV2/forecast-2018-06-26/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/TagResource.md "../../../goto/SdkForJavaScriptV3/forecast-2018-06-26/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/forecast-2018-06-26/TagResource.md "../../../goto/SdkForKotlin/forecast-2018-06-26/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/forecast-2018-06-26/TagResource.md "../../../goto/SdkForPHPV3/forecast-2018-06-26/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/forecast-2018-06-26/TagResource.md "../../../goto/boto3/forecast-2018-06-26/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/forecast-2018-06-26/TagResource.md "../../../goto/SdkForRubyV3/forecast-2018-06-26/TagResource.md")
