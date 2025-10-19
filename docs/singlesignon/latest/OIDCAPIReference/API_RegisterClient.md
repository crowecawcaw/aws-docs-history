# RegisterClient

Registers a public client with IAM Identity Center. This allows clients to perform authorization using
 the authorization code grant with Proof Key for Code Exchange (PKCE) or the device
 code grant.


## Request Syntax



```
POST /client/register HTTP/1.1
Content-type: application/json

{
   "clientName": "`string`",
   "clientType": "`string`",
   "entitledApplicationArn": "`string`",
   "grantTypes": [ "`string`" ],
   "issuerUrl": "`string`",
   "redirectUris": [ "`string`" ],
   "scopes": [ "`string`" ]
}
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in JSON format.





**[clientName](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The friendly name of the client.


Type: String


Required: Yes




**[clientType](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The type of client. The service supports only `public` as a client type.
 Anything other than public will be rejected by the service.


Type: String


Required: Yes




**[entitledApplicationArn](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


This IAM Identity Center application ARN is used to define administrator-managed configuration for
 public client access to resources. At authorization, the scopes, grants, and redirect URI
 available to this client will be restricted by this application resource.


Type: String


Required: No




**[grantTypes](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The list of OAuth 2.0 grant types that are defined by the client. This list is used to
 restrict the token granting flows available to the client. Supports the following OAuth 2.0
 grant types: Authorization Code, Device Code, and Refresh Token. 


\* Authorization Code - `authorization_code`



\* Device Code - `urn:ietf:params:oauth:grant-type:device_code`



\* Refresh Token - `refresh_token`



Type: Array of strings


Required: No




**[issuerUrl](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The IAM Identity Center Issuer URL associated with an instance of IAM Identity Center. This value is needed for user
 access to resources through the client.


Type: String


Required: No




**[redirectUris](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The list of redirect URI that are defined by the client. At completion of authorization,
 this list is used to restrict what locations the user agent can be redirected back to.


Type: Array of strings


Required: No




**[scopes](#API_RegisterClient_RequestSyntax "#API_RegisterClient_RequestSyntax")**


The list of scopes that are defined by the client. Upon authorization, this list is used
 to restrict permissions when granting an access token.


Type: Array of strings


Required: No




## Response Syntax



```
HTTP/1.1 200
Content-type: application/json

{
   "authorizationEndpoint": "***string***",
   "clientId": "***string***",
   "clientIdIssuedAt": ***number***,
   "clientSecret": "***string***",
   "clientSecretExpiresAt": ***number***,
   "tokenEndpoint": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[authorizationEndpoint](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


An endpoint that the client can use to request authorization.


Type: String




**[clientId](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


The unique identifier string for each client. This client uses this identifier to get
 authenticated by the service in subsequent calls.


Type: String




**[clientIdIssuedAt](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


Indicates the time at which the `clientId` and `clientSecret` were
 issued.


Type: Long




**[clientSecret](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


A secret string generated for the client. The client will use this string to get
 authenticated by the service in subsequent calls.


Type: String




**[clientSecretExpiresAt](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


Indicates the time at which the `clientId` and `clientSecret` will
 become invalid.


Type: Long




**[tokenEndpoint](#API_RegisterClient_ResponseSyntax "#API_RegisterClient_ResponseSyntax")**


An endpoint that the client can use to create tokens.


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




**InvalidClientMetadataException** 


Indicates that the client information sent in the request during registration is
 invalid.





**error** 


Single error code. For this exception the value will be
 `invalid_client_metadata`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




**InvalidRedirectUriException** 


Indicates that one or more redirect URI in the request is not supported for this
 operation.





**error** 


Single error code. For this exception the value will be
 `invalid_redirect_uri`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




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




**InvalidScopeException** 


Indicates that the scope provided in the request is invalid.





**error** 


Single error code. For this exception the value will be `invalid_scope`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




**UnsupportedGrantTypeException** 


Indicates that the grant type in the request is not supported by the service.





**error** 


Single error code. For this exception the value will be
 `unsupported_grant_type`.




**error\_description** 


Human-readable text providing additional information, used to assist the client developer
 in understanding the error that occurred.




HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/cli2/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/DotNetSDKV3/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForCpp/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForGoV2/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForKotlin/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForPHPV3/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/boto3/sso-oidc-2019-06-10/RegisterClient")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-oidc-2019-06-10/RegisterClient "https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-oidc-2019-06-10/RegisterClient")
