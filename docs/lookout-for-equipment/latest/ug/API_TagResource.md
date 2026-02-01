On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# TagResource

Associates a given tag to a resource in your account. A tag is a key-value pair which
can be added to an Amazon Lookout for Equipment resource as metadata. Tags can be used for organizing your
resources as well as helping you to search and filter by tag. Multiple tags can be added to
a resource, either when you create it, or later. Up to 50 tags can be associated with each
resource.

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

The Amazon Resource Name (ARN) of the specific resource to which the tag should be
associated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The tag or tags to be associated with a specific resource. Both the tag key and value
are specified.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

The request could not be completed because you do not have access to the resource.

HTTP Status Code: 400

**InternalServerException**

Processing of the request has failed because of an unknown error, exception or failure.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource requested could not be found. Verify the resource ID and retry your
request.

HTTP Status Code: 400

**ServiceQuotaExceededException**

Resource limitations have been exceeded.

HTTP Status Code: 400

**ThrottlingException**

The request was denied due to request throttling.

HTTP Status Code: 400

**ValidationException**

The input fails to satisfy constraints specified by Amazon Lookout for Equipment or a related AWS
service that's being utilized.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lookoutequipment-2020-12-15/TagResource.md "../../../goto/cli2/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/TagResource.md "../../../goto/DotNetSDKV4/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForGoV2/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForJavaScriptV3/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForKotlin/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForPHPV3/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/lookoutequipment-2020-12-15/TagResource.md "../../../goto/boto3/lookoutequipment-2020-12-15/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/TagResource.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/TagResource.md")
