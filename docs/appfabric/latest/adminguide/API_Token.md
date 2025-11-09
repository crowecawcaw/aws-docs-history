# Token

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Contains information that allows AppClients to exchange an authorization code for
an access token.

###### Topics

- [Request body](#API_Token_request "#API_Token_request")
- [Response elements](#API_Token_response "#API_Token_response")

## Request body

The request accepts the following data in JSON format.

| Parameter         | Description                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **code**          | The authorization code received from the authorization<br>endpoint.<br>Type: String<br>Length Constraints: Minimum length of 1. Maximum length of<br>2048.<br>Required: No |
| **grant_type**    | The grant type for the token. Must be either<br>`authorization_code` or<br>`refresh_token`.<br>Type: String<br>Required: Yes                                               |
| **app_client_id** | The ID of the AppClient.<br>Type: String<br>Pattern:<br>`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br>Required: Yes                                    |
| **redirect_uri**  | The redirect URI passed to the authorization<br>endpoint.<br>Type: String<br>Required: No                                                                                  |
| **refresh_token** | The refresh token received from the initial token<br>request.<br>Type: String<br>Length Constraints: Minimum length of 1. Maximum length of<br>4096.<br>Required: No       |

## Response elements

If the action is successful, the service sends back an HTTP 200
response.

The following data is returned in JSON format by the service.

| Parameter             | Description                                                                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **appfabric_user_id** | The ID of the user for the token. This is returned only<br>for requests that use the `authorization_code`<br>grant type.<br>Type: String  |
| **expires_in**        | The number of seconds until the token expires.<br>Type: Long                                                                              |
| **refresh_token**     | The refresh token to use for a subsequent request.<br>Type: String<br>Length Constraints: Minimum length of 1. Maximum length of<br>2048. |
| **token**             | The access token.<br>Type: String<br>Length Constraints: Minimum length of 1. Maximum length of<br>2048.                                  |
| **token_type**        | The token type.<br>Type: String                                                                                                           |
