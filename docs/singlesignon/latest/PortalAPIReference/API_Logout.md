# Logout

Removes the locally stored SSO tokens from the client-side cache and sends an API call to
 the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center sign in
 session.

###### Note

If a user uses IAM Identity Center to access the AWS CLI, the user’s IAM Identity Center sign in session is
 used to obtain an IAM session, as specified in the corresponding IAM Identity Center permission set.
 More specifically, IAM Identity Center assumes an IAM role in the target account on behalf of the user,
 and the corresponding temporary AWS credentials are returned to the client.

After user logout, any existing IAM role sessions that were created by using IAM Identity Center
 permission sets continue based on the duration configured in the permission set.
 For more information, see [User
 authentications](../userguide/authconcept.md "../userguide/authconcept.md") in the *IAM Identity Center User
 Guide*.


## Request Syntax



```
POST /logout HTTP/1.1
x-amz-sso_bearer_token: `accessToken`

```

## URI Request Parameters


The request uses the following URI parameters.





**[accessToken](#API_Logout_RequestSyntax "#API_Logout_RequestSyntax")**


The token issued by the `CreateToken` API call. For more information, see
 [CreateToken](../OIDCAPIReference/API_CreateToken.md "../OIDCAPIReference/API_CreateToken.md") in the *IAM Identity Center OIDC API Reference Guide*.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidRequestException** 


Indicates that a problem occurred with the input to the request. For example, a required
 parameter might be missing or out of range.


HTTP Status Code: 400




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/cli2/sso-2019-06-10/Logout")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-2019-06-10/Logout")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForCpp/sso-2019-06-10/Logout")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForGoV2/sso-2019-06-10/Logout")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-2019-06-10/Logout")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-2019-06-10/Logout")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForKotlin/sso-2019-06-10/Logout")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-2019-06-10/Logout")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/boto3/sso-2019-06-10/Logout")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/Logout "https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-2019-06-10/Logout")
