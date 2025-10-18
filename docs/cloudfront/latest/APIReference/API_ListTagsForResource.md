# ListTagsForResource

List tags for a CloudFront resource. For more information, see [Tagging a distribution](../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md "../../../AmazonCloudFront/latest/DeveloperGuide/tagging.md") in the *Amazon CloudFront Developer Guide*.


## Request Syntax



```
GET /2020-05-31/tagging?Resource=`Resource` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Resource](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**


An ARN of a CloudFront resource.


Pattern: `arn:aws(-cn)?:cloudfront::[0-9]+:.*`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Tags>
   <Items>
      <Tag>
         <Key>***string***</Key>
         <Value>***string***</Value>
      </Tag>
   </Items>
</Tags>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**


Root level tag for the Tags parameters.


Required: Yes




**[Items](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**


A complex type that contains `Tag` elements.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidTagging** 


The tagging specified is not valid.


HTTP Status Code: 400




**NoSuchResource** 


A resource that was specified is not valid.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListTagsForResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListTagsForResource")
