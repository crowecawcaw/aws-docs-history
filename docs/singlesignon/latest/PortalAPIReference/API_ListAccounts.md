# ListAccounts

Lists all AWS accounts assigned to the user. These AWS accounts are assigned by the
 administrator of the account. For more information, see [Assign User Access](../userguide/useraccess.md#assignusers "../userguide/useraccess.md#assignusers") in the *IAM Identity Center User Guide*. This operation
 returns a paginated response.


## Request Syntax



```
GET /assignment/accounts?max_result=`maxResults`&next_token=`nextToken` HTTP/1.1
x-amz-sso_bearer_token: `accessToken`

```

## URI Request Parameters


The request uses the following URI parameters.





**[accessToken](#API_ListAccounts_RequestSyntax "#API_ListAccounts_RequestSyntax")**


The token issued by the `CreateToken` API call. For more information, see
 [CreateToken](../OIDCAPIReference/API_CreateToken.md "../OIDCAPIReference/API_CreateToken.md") in the *IAM Identity Center OIDC API Reference Guide*.


Required: Yes




**[maxResults](#API_ListAccounts_RequestSyntax "#API_ListAccounts_RequestSyntax")**


This is the number of items clients can request per page.


Valid Range: Minimum value of 1. Maximum value of 100.




**[nextToken](#API_ListAccounts_RequestSyntax "#API_ListAccounts_RequestSyntax")**


(Optional) When requesting subsequent pages, this is the page token from the previous
 response output.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "accountList": [ 
      { 
         "accountId": "***string***",
         "accountName": "***string***",
         "emailAddress": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[accountList](#API_ListAccounts_ResponseSyntax "#API_ListAccounts_ResponseSyntax")**


A paginated response with the list of account information and the next token if more
 results are available.


Type: Array of [AccountInfo](API_AccountInfo.md "API_AccountInfo.md") objects




**[nextToken](#API_ListAccounts_ResponseSyntax "#API_ListAccounts_ResponseSyntax")**


The page token client that is used to retrieve the list of accounts.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidRequestException** 


Indicates that a problem occurred with the input to the request. For example, a required
 parameter might be missing or out of range.


HTTP Status Code: 400




**ResourceNotFoundException** 


The specified resource doesn't exist.


HTTP Status Code: 404




**TooManyRequestsException** 


Indicates that the request is being made too frequently and is more than what the server
 can handle.


HTTP Status Code: 429




**UnauthorizedException** 


Indicates that the request is not authorized. This can happen due to an invalid access
 token in the request.


HTTP Status Code: 401




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/ListAccounts")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-2019-06-10/ListAccounts")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/ListAccounts")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/ListAccounts")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/ListAccounts")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/ListAccounts")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/ListAccounts")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/ListAccounts")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/ListAccounts")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/ListAccounts "https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/ListAccounts")
