# CreateEnvironmentMembership

Adds an environment member to an AWS Cloud9 development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "environmentId": "`string`",
   "permissions": "`string`",
   "userArn": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[environmentId](#API_CreateEnvironmentMembership_RequestSyntax "#API_CreateEnvironmentMembership_RequestSyntax")**


The ID of the environment that contains the environment member you want to add.


Type: String


Pattern: `^[a-zA-Z0-9]{8,32}$`



Required: Yes




**[permissions](#API_CreateEnvironmentMembership_RequestSyntax "#API_CreateEnvironmentMembership_RequestSyntax")**


The type of environment member permissions you want to associate with this environment
 member. Available values include:



* `read-only`: Has read-only access to the environment.
* `read-write`: Has read-write access to the environment.

Type: String


Valid Values: `read-write | read-only`



Required: Yes




**[userArn](#API_CreateEnvironmentMembership_RequestSyntax "#API_CreateEnvironmentMembership_RequestSyntax")**


The Amazon Resource Name (ARN) of the environment member you want to add.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`



Required: Yes




## Response Syntax



```
{
   "membership": { 
      "environmentId": "***string***",
      "lastAccess": ***number***,
      "permissions": "***string***",
      "userArn": "***string***",
      "userId": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[membership](#API_CreateEnvironmentMembership_ResponseSyntax "#API_CreateEnvironmentMembership_ResponseSyntax")**


Information about the environment member that was added.


Type: [EnvironmentMember](API_EnvironmentMember.md "API_EnvironmentMember.md") object




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


The following example adds the specified environment member to the specified AWS Cloud9
 development environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
X-Amz-Date: <Date>
User-Agent: <UserAgentString>
X-Amz-Target: AWSCloud9WorkspaceManagementService.CreateEnvironmentMembership
Content-Length: <PayloadSizeBytes>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>

{
  "environmentId": "8d9967e2f0624182b74e7690ad69ebEX", 
  "permissions": "read-write", 
  "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser"
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
  "membership": {
    "environmentId": "8d9967e2f0624182b74e7690ad69ebEX",
    "permissions": "read-write",
    "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser",
    "userId": "AIDAJ3BA6O2FMJWCWXHEX"
  }
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/CreateEnvironmentMembership")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/CreateEnvironmentMembership "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/CreateEnvironmentMembership")
