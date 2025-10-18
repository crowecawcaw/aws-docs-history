# ListTagsForResource

Gets a list of the tags associated with an AWS Cloud9 development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "ResourceARN": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ResourceARN](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**


The Amazon Resource Name (ARN) of the AWS Cloud9 development environment to get the tags
 for.


Type: String


Pattern: `arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):cloud9:([a-z]{2}-[a-z]+-\d{1}):[0-9]{12}:environment:[a-zA-Z0-9]{8,32}`



Required: Yes




## Response Syntax



```
{
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





**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**


The list of tags associated with the AWS Cloud9 development environment.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Minimum number of 0 items. Maximum number of 200 items.




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**BadRequestException** 


The target request is invalid.


HTTP Status Code: 400




**InternalServerErrorException** 


An internal server error occurred.


HTTP Status Code: 500




**NotFoundException** 


The target resource cannot be found.


HTTP Status Code: 400




## Examples


### Example


The following example shows now to get a list of the tags that are associated with an
 AWS Cloud9 development environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
X-Amz-Date: <Date>
User-Agent: <UserAgentString>
X-Amz-Target: AWSCloud9WorkspaceManagementService.ListTagsForResource
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
  "ResourceARN": "arn:aws:cloud9:eu-west-1:123456789012:environment:8d9967e2f0624182b74e7690ad69ebEX",
}
```

#### Sample Response



```
HTTP/1.1 200 OK
Date: <Date>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
x-amzn-RequestId: <RequestId>
Connection: Keep-alive

{
  "Tags": [
    {
      "Key": "key",
      "Value": "orange"
    }
  ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/ListTagsForResource")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/ListTagsForResource "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/ListTagsForResource")
