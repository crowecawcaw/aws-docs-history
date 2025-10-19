# DescribeEnvironmentMemberships

Gets information about environment members for an AWS Cloud9 development environment.

###### Important


 AWS Cloud9 is no longer available to new customers. Existing customers of 
 AWS Cloud9 can continue to use the service as normal. 
 [Learn more"](http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/ "http://aws.amazon.com/blogs/devops/how-to-migrate-from-aws-cloud9-to-aws-ide-toolkits-or-aws-cloudshell/")



## Request Syntax



```
{
   "environmentId": "`string`",
   "maxResults": `number`,
   "nextToken": "`string`",
   "permissions": [ "`string`" ],
   "userArn": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[environmentId](#API_DescribeEnvironmentMemberships_RequestSyntax "#API_DescribeEnvironmentMemberships_RequestSyntax")**


The ID of the environment to get environment member information about.


Type: String


Pattern: `^[a-zA-Z0-9]{8,32}$`



Required: No




**[maxResults](#API_DescribeEnvironmentMemberships_RequestSyntax "#API_DescribeEnvironmentMemberships_RequestSyntax")**


The maximum number of environment members to get information about.


Type: Integer


Valid Range: Minimum value of 0. Maximum value of 25.


Required: No




**[nextToken](#API_DescribeEnvironmentMemberships_RequestSyntax "#API_DescribeEnvironmentMemberships_RequestSyntax")**


During a previous call, if there are more than 25 items in the list, only the first 25
 items are returned, along with a unique string called a *next token*. To
 get the next batch of items in the list, call this operation again, adding the next token to
 the call. To get all of the items in the list, keep calling this operation with each
 subsequent next token that is returned, until no more next tokens are returned.


Type: String


Required: No




**[permissions](#API_DescribeEnvironmentMemberships_RequestSyntax "#API_DescribeEnvironmentMemberships_RequestSyntax")**


The type of environment member permissions to get information about. Available values
 include:



* `owner`: Owns the environment.
* `read-only`: Has read-only access to the environment.
* `read-write`: Has read-write access to the environment.

If no value is specified, information about all environment members are returned.


Type: Array of strings


Valid Values: `owner | read-write | read-only`



Required: No




**[userArn](#API_DescribeEnvironmentMemberships_RequestSyntax "#API_DescribeEnvironmentMemberships_RequestSyntax")**


The Amazon Resource Name (ARN) of an individual environment member to get information
 about. If no value is specified, information about all environment members are
 returned.


Type: String


Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):(iam|sts)::\d+:(root|(user\/[\w+=/:,.@-]{1,64}|federated-user\/[\w+=/:,.@-]{2,32}|assumed-role\/[\w+=:,.@-]{1,64}\/[\w+=,.@-]{1,64}))$`



Required: No




## Response Syntax



```
{
   "memberships": [ 
      { 
         "environmentId": "***string***",
         "lastAccess": ***number***,
         "permissions": "***string***",
         "userArn": "***string***",
         "userId": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[memberships](#API_DescribeEnvironmentMemberships_ResponseSyntax "#API_DescribeEnvironmentMemberships_ResponseSyntax")**


Information about the environment members for the environment.


Type: Array of [EnvironmentMember](API_EnvironmentMember.md "API_EnvironmentMember.md") objects




**[nextToken](#API_DescribeEnvironmentMemberships_ResponseSyntax "#API_DescribeEnvironmentMemberships_ResponseSyntax")**


If there are more than 25 items in the list, only the first 25 items are returned, along
 with a unique string called a *next token*. To get the next batch of items
 in the list, call this operation again, adding the next token to the call.


Type: String




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


### Get environment members for a development environment


The following example gets information about all of the environment members for the
 specified AWS Cloud9 development environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
User-Agent: <UserAgentString>
X-Amz-Date: <Date>
X-Amz-Target: AWSCloud9WorkspaceManagementService.DescribeEnvironmentMemberships
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature> 
Content-Length: <PayloadSizeBytes>

{
  "permissions": [
    "owner"
  ], 
  "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa"
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
  "memberships": [
    {
      "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa",
      "permissions": "owner",
      "userArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "userId": "ABCDEFGHIJKLMNOPQRSTU"
    }
  ]
}
```

### Get the owner of a development environment


The following example gets information about the owner of the specified AWS Cloud9
 development environment.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCloud9WorkspaceManagementService.DescribeEnvironmentMemberships
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature> 
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>

{
  "userArn": "arn:aws:iam::123456789012:user/MyDemoUser"
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
  "memberships": [
    {
      "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa",
      "lastAccess": 1.516403173E9,
      "permissions": "owner",
      "userArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "userId": "XXXXXXXXXXXXXXXXXX"
    },
    {
      "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa",
      "lastAccess": 1.516405159E9,
      "permissions": "owner",
      "userArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "userId": "ABCDEFGHIJKLMNOPQRSTUV"
    }
  ]
}
```

### Get Development Environment Memberships for a User


The following example gets AWS Cloud9 development environment membership information for
 the specified user.


#### Sample Request



```
POST / HTTP/1.1
Host: cloud9.<region>.amazonaws.com
Accept-Encoding: identity
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSCloud9WorkspaceManagementService.DescribeEnvironmentMemberships
X-Amz-Date: <Date>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature> 
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>

{
  "userArn": "arn:aws:iam::123456789012:user/MyDemoUser"
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
  "memberships": [
    {
      "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa",
      "lastAccess": 1.516403173E9,
      "permissions": "owner",
      "userArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "userId": "XXXXXXXXXXXXXXXXXX"
    },
    {
      "environmentId": "9999aaaa9999aaaa9999aaaa9999aaaa",
      "lastAccess": 1.516405159E9,
      "permissions": "owner",
      "userArn": "arn:aws:iam::123456789012:user/MyDemoUser",
      "userId": "ABCDEFGHIJKLMNOPQRSTUV"
    }
  ]
}
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/cli2/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForCpp/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForGoV2/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForKotlin/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/boto3/cloud9-2017-09-23/DescribeEnvironmentMemberships")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DescribeEnvironmentMemberships "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloud9-2017-09-23/DescribeEnvironmentMemberships")
