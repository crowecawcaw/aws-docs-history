

# Token
<a name="API_Token"></a>


|  | 
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. | 

Contains information that allows AppClients to exchange an authorization code for an access token.

**Topics**
+ [Request body](#API_Token_request)
+ [Response elements](#API_Token_response)

## Request body
<a name="API_Token_request"></a>

The request accepts the following data in JSON format.


| Parameter | Description | 
| --- | --- | 
| **code** | The authorization code received from the authorization endpoint.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 2048.<br />Required: No | 
| **grant\_type** | The grant type for the token. Must be either `authorization_code` or `refresh_token`.<br />Type: String<br />Required: Yes | 
| **app\_client\_id** | The ID of the AppClient.<br />Type: String<br />Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br />Required: Yes | 
| **redirect\_uri** | The redirect URI passed to the authorization endpoint.<br />Type: String<br />Required: No | 
| **refresh\_token** | The refresh token received from the initial token request.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 4096.<br />Required: No | 

## Response elements
<a name="API_Token_response"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.


| Parameter | Description | 
| --- | --- | 
| **appfabric\_user\_id** | The ID of the user for the token. This is returned only for requests that use the `authorization_code` grant type.<br />Type: String | 
| **expires\_in** | The number of seconds until the token expires.<br />Type: Long | 
| **refresh\_token** | The refresh token to use for a subsequent request.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 2048. | 
| **token** | The access token.<br />Type: String<br />Length Constraints: Minimum length of 1. Maximum length of 2048. | 
| **token\_type** | The token type.<br />Type: String | 