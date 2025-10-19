# StartDeviceAuthorization

Initiates device authorization by requesting a pair of verification codes from the
 authorization service.


## Request Syntax



```
POST /device_authorization HTTP/1.1
Content-type: application/json

{
   "clientId": "`string`",
   "clientSecret": "`string`",
   "startUrl": "`string`"
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[clientId](#API_StartDeviceAuthorization_RequestSyntax "#API_StartDeviceAuthorization_RequestSyntax")**


The unique identifier string for the client that is registered with IAM Identity Center. This value
 should come from the persisted result of the [RegisterClient](API_RegisterClient.md "API_RegisterClient.md") API
 operation.


Type: String


Required: Yes




**[clientSecret](#API_StartDeviceAuthorization_RequestSyntax "#API_StartDeviceAuthorization_RequestSyntax")**


A secret string that is generated for the client. This value should come from the
 persisted result of the [RegisterClient](API_RegisterClient.md "API_RegisterClient.md") API operation.


Type: String


Required: Yes




**[startUrl](#API_StartDeviceAuthorization_RequestSyntax "#API_StartDeviceAuthorization_RequestSyntax")**


The URL for the AWS access portal. For more information, see [Using
 the AWS access portal](../userguide/using-the-portal.md "../userguide/using-the-portal.md") in the *IAM Identity Center User Guide*.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "deviceCode": "***string***",
   "expiresIn": ***number***,
   "interval": ***number***,
   "userCode": "***string***",
   "verificationUri": "***string***",
   "verificationUriComplete": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[deviceCode](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


The short-lived code that is used by the device when polling for a session token.


Type: String




**[expiresIn](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


Indicates the number of seconds in which the verification code will become invalid.


Type: Integer




**[interval](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


Indicates the number of seconds the client must wait between attempts when polling for a
 session.


Type: Integer




**[userCode](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


A one-time user verification code. This is needed to authorize an in-use device.


Type: String




**[verificationUri](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


The URI of the verification page that takes the `userCode` to authorize the
 device.


Type: String




**[verificationUriComplete](#API_StartDeviceAuthorization_ResponseSyntax "#API_StartDeviceAuthorization_ResponseSyntax")**


An alternate URL that the client can use to automatically launch a browser. This process
 skips the manual step in which the user visits the verification page and enters their
 code.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InternalServerException** 


Indicates that an error from the service occurred while trying to process a
 request.





**error** 


Single error code. For this exception the value will be `server_error`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 500




**InvalidClientException** 


Indicates that the `clientId` or `clientSecret` in the request is
 invalid. For example, this can occur when a client sends an incorrect `clientId` or
 an expired `clientSecret`.





**error** 


Single error code. For this exception the value will be
 `invalid_client`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 401




**InvalidRequestException** 


Indicates that something is wrong with the input to the request. For example, a required
 parameter might be missing or out of range.





**error** 


Single error code. For this exception the value will be
 `invalid_request`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




**SlowDownException** 


Indicates that the client is making the request too frequently and is more than the
 service can handle. 





**error** 


Single error code. For this exception the value will be `slow_down`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




**UnauthorizedClientException** 


Indicates that the client is not currently authorized to make the request. This can happen
 when a `clientId` is not issued for a public client.





**error** 


Single error code. For this exception the value will be
 `unauthorized_client`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/cli2/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForCpp/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForGoV2/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForKotlin/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/boto3/sso-oidc-2019-06-10/StartDeviceAuthorization")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-oidc-2019-06-10/StartDeviceAuthorization "https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-oidc-2019-06-10/StartDeviceAuthorization")
