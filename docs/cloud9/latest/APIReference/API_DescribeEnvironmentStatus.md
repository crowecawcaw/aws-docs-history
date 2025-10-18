# DescribeEnvironmentStatus

Gets status information for an AWS Cloud9 development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "environmentId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[environmentId](#API_DescribeEnvironmentStatus_RequestSyntax "#API_DescribeEnvironmentStatus_RequestSyntax")**


The ID of the environment to get status information about.


Type: String


Pattern: `^[a-zA-Z0-9]{8,32}$`



Required: Yes




## Response Syntax



```
{
   "message": "***string***",
   "status": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[message](#API_DescribeEnvironmentStatus_ResponseSyntax "#API_DescribeEnvironmentStatus_ResponseSyntax")**


Any informational message about the status of the environment.


Type: String




**[status](#API_DescribeEnvironmentStatus_ResponseSyntax "#API_DescribeEnvironmentStatus_ResponseSyntax")**


The status of the environment. Available values include:



* `connecting`: The environment is connecting.
* `creating`: The environment is being created.
* `deleting`: The environment is being deleted.
* `error`: The environment is in an error state.
* `ready`: The environment is ready.
* `stopped`: The environment is stopped.
* `stopping`: The environment is stopping.

Type: String


Valid Values: `error | creating | connecting | ready | stopping | stopped | deleting`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**BadRequestException** 


The target request is invalid.


HTTP Status Code: 400




**ConflictException** 


A conflict occurred.


HTTP Status Code: 400




**ForbiddenException** 


An access permissions issue occurred.


HTTP Status Code: 400




**InternalServerErrorException** 


An internal server error occurred.


HTTP Status Code: 500




**LimitExceededException** 


A service limit was exceeded.


HTTP Status Code: 400




**NotFoundException** 


The target resource cannot be found.


HTTP Status Code: 400




**TooManyRequestsException** 


Too many service requests were made over the given time period.


HTTP Status Code: 400




## Examples


### Example


The following example gets status information about the specified AWS Cloud9 development
 environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
X-Amz-Date: <Date>
X-Amz-Target: AWSCloud9WorkspaceManagementService.DescribeEnvironmentStatus
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature> 
Content-Length: <PayloadSizeBytes>
Content-Type: application/x-amz-json-1.1

{
  "environmentId": "8d9967e2f0624182b74e7690ad69ebEX"
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
  "message": "Environment is ready to use",
  "status": "ready"
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DescribeEnvironmentStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DescribeEnvironmentStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DescribeEnvironmentStatus")
