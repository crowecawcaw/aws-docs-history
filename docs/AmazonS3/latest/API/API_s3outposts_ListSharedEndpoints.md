# ListSharedEndpoints

Lists all endpoints associated with an Outpost that has been shared by AWS Resource Access Manager (RAM).

Related actions include:


* [CreateEndpoint](API_s3outposts_CreateEndpoint.md "API_s3outposts_CreateEndpoint.md")
* [DeleteEndpoint](API_s3outposts_DeleteEndpoint.md "API_s3outposts_DeleteEndpoint.md")

## Request Syntax



```
GET /S3Outposts/ListSharedEndpoints?maxResults=`MaxResults`&nextToken=`NextToken`&outpostId=`OutpostId` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[MaxResults](#API_s3outposts_ListSharedEndpoints_RequestSyntax "#API_s3outposts_ListSharedEndpoints_RequestSyntax")**


The maximum number of endpoints that will be returned in the response.


Valid Range: Minimum value of 0. Maximum value of 100.




**[NextToken](#API_s3outposts_ListSharedEndpoints_RequestSyntax "#API_s3outposts_ListSharedEndpoints_RequestSyntax")**


If a previous response from this operation included a `NextToken` value, you
 can provide that value here to retrieve the next page of results.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





**[OutpostId](#API_s3outposts_ListSharedEndpoints_RequestSyntax "#API_s3outposts_ListSharedEndpoints_RequestSyntax")**


The ID of the AWS Outpost.


Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[Endpoints](#AmazonS3-s3outposts_ListSharedEndpoints-response-Endpoints "#AmazonS3-s3outposts_ListSharedEndpoints-response-Endpoints")": [ 
      { 
         "[AccessType](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-AccessType "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-AccessType")": "***string***",
         "[CidrBlock](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CidrBlock "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CidrBlock")": "***string***",
         "[CreationTime](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CreationTime "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CreationTime")": ***number***,
         "[CustomerOwnedIpv4Pool](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CustomerOwnedIpv4Pool "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-CustomerOwnedIpv4Pool")": "***string***",
         "[EndpointArn](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-EndpointArn "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-EndpointArn")": "***string***",
         "[FailedReason](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-FailedReason "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-FailedReason")": { 
            "[ErrorCode](API_s3outposts_FailedReason.md#AmazonS3-Type-s3outposts_FailedReason-ErrorCode "API_s3outposts_FailedReason.md#AmazonS3-Type-s3outposts_FailedReason-ErrorCode")": "***string***",
            "[Message](API_s3outposts_FailedReason.md#AmazonS3-Type-s3outposts_FailedReason-Message "API_s3outposts_FailedReason.md#AmazonS3-Type-s3outposts_FailedReason-Message")": "***string***"
         },
         "[NetworkInterfaces](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-NetworkInterfaces "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-NetworkInterfaces")": [ 
            { 
               "[NetworkInterfaceId](API_s3outposts_NetworkInterface.md#AmazonS3-Type-s3outposts_NetworkInterface-NetworkInterfaceId "API_s3outposts_NetworkInterface.md#AmazonS3-Type-s3outposts_NetworkInterface-NetworkInterfaceId")": "***string***"
            }
         ],
         "[OutpostsId](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-OutpostsId "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-OutpostsId")": "***string***",
         "[SecurityGroupId](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-SecurityGroupId "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-SecurityGroupId")": "***string***",
         "[Status](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-Status "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-Status")": "***string***",
         "[SubnetId](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-SubnetId "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-SubnetId")": "***string***",
         "[VpcId](API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-VpcId "API_s3outposts_Endpoint.md#AmazonS3-Type-s3outposts_Endpoint-VpcId")": "***string***"
      }
   ],
   "[NextToken](#AmazonS3-s3outposts_ListSharedEndpoints-response-NextToken "#AmazonS3-s3outposts_ListSharedEndpoints-response-NextToken")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Endpoints](#API_s3outposts_ListSharedEndpoints_ResponseSyntax "#API_s3outposts_ListSharedEndpoints_ResponseSyntax")**


The list of endpoints associated with the specified Outpost that have been shared by AWS Resource Access Manager (RAM).


Type: Array of [Endpoint](API_s3outposts_Endpoint.md "API_s3outposts_Endpoint.md") objects




**[NextToken](#API_s3outposts_ListSharedEndpoints_ResponseSyntax "#API_s3outposts_ListSharedEndpoints_ResponseSyntax")**


If the number of endpoints associated with the specified Outpost exceeds `MaxResults`, 
 you can include this value in subsequent calls to this operation to retrieve more results.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `^[A-Za-z0-9\+\:\/\=\?\#-_]+$`





## Errors





**AccessDeniedException** 


Access was denied for this action.


HTTP Status Code: 403




**InternalServerException** 


There was an exception with the internal server.


HTTP Status Code: 500




**ResourceNotFoundException** 


The requested resource was not found.


HTTP Status Code: 404




**ThrottlingException** 


The request was denied due to request throttling.


HTTP Status Code: 429




**ValidationException** 


There was an exception validating this data.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/ListSharedEndpoints")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/ListSharedEndpoints "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/ListSharedEndpoints")
