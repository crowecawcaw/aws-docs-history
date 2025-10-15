# CreateEndpoint

Creates an endpoint and associates it with the specified Outpost.

###### Note

It can take up to 5 minutes for this action to finish.

Related actions include:


* [DeleteEndpoint](API_s3outposts_DeleteEndpoint.md "API_s3outposts_DeleteEndpoint.md")
* [ListEndpoints](API_s3outposts_ListEndpoints.md "API_s3outposts_ListEndpoints.md")

## Request Syntax



```
POST /S3Outposts/CreateEndpoint HTTP/1.1
Content-type: application/json

{
   "[AccessType](#AmazonS3-s3outposts_CreateEndpoint-request-AccessType "#AmazonS3-s3outposts_CreateEndpoint-request-AccessType")": "`string`",
   "[CustomerOwnedIpv4Pool](#AmazonS3-s3outposts_CreateEndpoint-request-CustomerOwnedIpv4Pool "#AmazonS3-s3outposts_CreateEndpoint-request-CustomerOwnedIpv4Pool")": "`string`",
   "[OutpostId](#AmazonS3-s3outposts_CreateEndpoint-request-OutpostId "#AmazonS3-s3outposts_CreateEndpoint-request-OutpostId")": "`string`",
   "[SecurityGroupId](#AmazonS3-s3outposts_CreateEndpoint-request-SecurityGroupId "#AmazonS3-s3outposts_CreateEndpoint-request-SecurityGroupId")": "`string`",
   "[SubnetId](#AmazonS3-s3outposts_CreateEndpoint-request-SubnetId "#AmazonS3-s3outposts_CreateEndpoint-request-SubnetId")": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[AccessType](#API_s3outposts_CreateEndpoint_RequestSyntax "#API_s3outposts_CreateEndpoint_RequestSyntax")**


The type of access for the network connectivity for the Amazon S3 on Outposts endpoint. To use
 the AWS VPC, choose `Private`. To use the endpoint with an on-premises
 network, choose `CustomerOwnedIp`. If you choose
 `CustomerOwnedIp`, you must also provide the customer-owned IP address
 pool (CoIP pool).


###### Note


`Private` is the default access type value.


Type: String


Valid Values: `Private | CustomerOwnedIp`



Required: No




**[CustomerOwnedIpv4Pool](#API_s3outposts_CreateEndpoint_RequestSyntax "#API_s3outposts_CreateEndpoint_RequestSyntax")**


The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses
 are allocated from this pool for the endpoint.


Type: String


Pattern: `^ipv4pool-coip-([0-9a-f]{17})$`



Required: No




**[OutpostId](#API_s3outposts_CreateEndpoint_RequestSyntax "#API_s3outposts_CreateEndpoint_RequestSyntax")**


The ID of the AWS Outposts. 


Type: String


Pattern: `^(op-[a-f0-9]{17}|\d{12}|ec2)$`



Required: Yes




**[SecurityGroupId](#API_s3outposts_CreateEndpoint_RequestSyntax "#API_s3outposts_CreateEndpoint_RequestSyntax")**


The ID of the security group to use with the endpoint.


Type: String


Pattern: `^sg-([0-9a-f]{8}|[0-9a-f]{17})$`



Required: Yes




**[SubnetId](#API_s3outposts_CreateEndpoint_RequestSyntax "#API_s3outposts_CreateEndpoint_RequestSyntax")**


The ID of the subnet in the selected VPC. The endpoint subnet must belong to the Outpost
 that has Amazon S3 on Outposts provisioned.


Type: String


Pattern: `^subnet-([0-9a-f]{8}|[0-9a-f]{17})$`



Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "[EndpointArn](#AmazonS3-s3outposts_CreateEndpoint-response-EndpointArn "#AmazonS3-s3outposts_CreateEndpoint-response-EndpointArn")": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[EndpointArn](#API_s3outposts_CreateEndpoint_ResponseSyntax "#API_s3outposts_CreateEndpoint_ResponseSyntax")**


The Amazon Resource Name (ARN) of the endpoint.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$`





## Errors





**AccessDeniedException** 


Access was denied for this action.


HTTP Status Code: 403




**ConflictException** 


There was a conflict with this action, and it could not be completed.


HTTP Status Code: 409




**InternalServerException** 


There was an exception with the internal server.


HTTP Status Code: 500




**OutpostOfflineException** 


The service link connection to your Outposts home Region is down. Check your connection and try again.


HTTP Status Code: 400




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/cli2/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForGoV2/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForKotlin/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/boto3/s3outposts-2017-07-25/CreateEndpoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/CreateEndpoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3outposts-2017-07-25/CreateEndpoint")
