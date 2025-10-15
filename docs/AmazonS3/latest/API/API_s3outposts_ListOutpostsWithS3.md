# ListOutpostsWithS3

Lists the Outposts with S3 on Outposts capacity for your AWS account.
 Includes S3 on Outposts that you have access to as the Outposts owner, or as a shared user
 from Resource Access Manager (RAM). 


## Request Syntax



```
GET /S3Outposts/ListOutpostsWithS3?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[MaxResults](#API_s3outposts_ListOutpostsWithS3_RequestSyntax "#API_s3outposts_ListOutpostsWithS3_RequestSyntax")**


The maximum number of Outposts to return. The limit is 100.


Valid Range: Minimum value of 0. Maximum value of 100.




**[NextToken](#API_s3outposts_ListOutpostsWithS3_RequestSyntax "#API_s3outposts_ListOutpostsWithS3_RequestSyntax")**


When you can get additional results from the `ListOutpostsWithS3` call, a
 `NextToken` parameter is returned in the output. You can then pass in a
 subsequent command to the `NextToken` parameter to continue listing
 additional Outposts.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[NextToken](#AmazonS3-s3outposts_ListOutpostsWithS3-response-NextToken "#AmazonS3-s3outposts_ListOutpostsWithS3-response-NextToken")": "***string***",
   "[Outposts](#AmazonS3-s3outposts_ListOutpostsWithS3-response-Outposts "#AmazonS3-s3outposts_ListOutpostsWithS3-response-Outposts")": [ 
      { 
         "[CapacityInBytes](API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-CapacityInBytes "API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-CapacityInBytes")": ***number***,
         "[OutpostArn](API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OutpostArn "API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OutpostArn")": "***string***",
         "[OutpostId](API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OutpostId "API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OutpostId")": "***string***",
         "[OwnerId](API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OwnerId "API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-OwnerId")": "***string***",
         "[S3OutpostArn](API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-S3OutpostArn "API_s3outposts_Outpost.md#AmazonS3-Type-s3outposts_Outpost-S3OutpostArn")": "***string***"
      }
   ]
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[NextToken](#API_s3outposts_ListOutpostsWithS3_ResponseSyntax "#API_s3outposts_ListOutpostsWithS3_ResponseSyntax")**


Returns a token that you can use to call `ListOutpostsWithS3` again and receive additional results, if there are any.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





**[Outposts](#API_s3outposts_ListOutpostsWithS3_ResponseSyntax "#API_s3outposts_ListOutpostsWithS3_ResponseSyntax")**


Returns the list of Outposts that have the following characteristics:



* outposts that have S3 provisioned
* outposts that are `Active` (not pending any provisioning nor decommissioned)
* outposts to which the the calling AWS account has access

Type: Array of [Outpost](API_s3outposts_Outpost.md "API_s3outposts_Outpost.md") objects




## Errors





**AccessDeniedException** 


Access was denied for this action.


HTTP Status Code: 403




**InternalServerException** 


There was an exception with the internal server.


HTTP Status Code: 500




**ThrottlingException** 


The request was denied due to request throttling.


HTTP Status Code: 429




**ValidationException** 


There was an exception validating this data.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/ListOutpostsWithS3")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/ListOutpostsWithS3 "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/ListOutpostsWithS3")
