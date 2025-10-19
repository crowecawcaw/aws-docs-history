# DeleteEnvironmentMembership

Deletes an environment member from a development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "environmentId": "`string`",
   "userArn": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[environmentId](#API_DeleteEnvironmentMembership_RequestSyntax "#API_DeleteEnvironmentMembership_RequestSyntax")**


The ID of the environment to delete the environment member from.


Type: String


Pattern: `^[a-zA-Z0-9]{8,32}$`



Required: Yes




**[userArn](#API_DeleteEnvironmentMembership_RequestSyntax "#API_DeleteEnvironmentMembership_RequestSyntax")**


The Amazon Resource Name (ARN) of the environment member to delete from the
 environment.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`



Required: Yes




## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


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


The following example deletes the specified environment member from the specified
 AWS Cloud9 development environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AWSCloud9WorkspaceManagementService.DeleteEnvironmentMembership
User-Agent: <UserAgentString>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Type: application/x-amz-json-1.1
X-Amz-Date: <Date>
Content-Length: <PayloadSizeBytes>

{
  "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser", 
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

{}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DeleteEnvironmentMembership")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DeleteEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DeleteEnvironmentMembership")
