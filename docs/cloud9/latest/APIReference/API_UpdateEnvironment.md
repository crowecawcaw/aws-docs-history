# UpdateEnvironment

Changes the settings of an existing AWS Cloud9 development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "description": "`string`",
   "environmentId": "`string`",
   "managedCredentialsAction": "`string`",
   "name": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[description](#API_UpdateEnvironment_RequestSyntax "#API_UpdateEnvironment_RequestSyntax")**


Any new or replacement description for the environment.


Type: String


Length Constraints: Maximum length of 200.


Required: No




**[environmentId](#API_UpdateEnvironment_RequestSyntax "#API_UpdateEnvironment_RequestSyntax")**


The ID of the environment to change settings.


Type: String


Pattern: `^[a-zA-Z0-9]{8,32}$`



Required: Yes




**[managedCredentialsAction](#API_UpdateEnvironment_RequestSyntax "#API_UpdateEnvironment_RequestSyntax")**


Allows the environment owner to turn on or turn off the AWS managed temporary
 credentials for an AWS Cloud9 environment by using one of the following values:



* `ENABLE`
* `DISABLE`

###### Note

Only the environment owner can change the status of managed temporary credentials. An `AccessDeniedException` is thrown if an attempt to turn on or turn off managed temporary credentials is made by an account that's not the environment
 owner.


Type: String


Valid Values: `ENABLE | DISABLE`



Required: No




**[name](#API_UpdateEnvironment_RequestSyntax "#API_UpdateEnvironment_RequestSyntax")**


A replacement name for the environment.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 60.


Required: No




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


The following example changes information about the specified AWS Cloud9 development
 environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
User-Agent: <UserAgentString>
X-Amz-Target: AWSCloud9WorkspaceManagementService.UpdateEnvironment
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
Content-Type: application/x-amz-json-1.1

{
  "name": "my-changed-demo-environment", 
  "description": "This is my changed demonstration environment.", 
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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/UpdateEnvironment")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/UpdateEnvironment "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/UpdateEnvironment")
