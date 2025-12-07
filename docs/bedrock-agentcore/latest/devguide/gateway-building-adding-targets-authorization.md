# Specify the authorization type and credentials to access the gateway target

You provide the credential provider configuration as a member of the array that the `credentialProviderConfigurations` field in the [CreateGatewayTarget](../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateGatewayTarget.md") request body maps to. The configuration that you provide depends on the outbound authorization that you set up. For reference information about the API structure for the credential provider configuration, see [CredentialProviderConfiguration](../../../bedrock-agentcore-control/latest/APIReference/API_CredentialProviderConfiguration.md "../../../bedrock-agentcore-control/latest/APIReference/API_CredentialProviderConfiguration.md"). For more information on outbound authorization, see [Set up outbound authorization for your gateway](gateway-outbound-auth.md "gateway-outbound-auth.md").

To learn more about a credential provider configuration, select a topic:

###### Topics

- [AgentCore Gateway service role (IAM) authorization](#gateway-building-adding-targets-authorization-service-role "#gateway-building-adding-targets-authorization-service-role")
- [OAuth authorization](#gateway-building-adding-targets-authorization-oauth "#gateway-building-adding-targets-authorization-oauth")
- [API key authorization](#gateway-building-adding-targets-authorization-api-key "#gateway-building-adding-targets-authorization-api-key")

## AgentCore Gateway service role (IAM) authorization

If you're using IAM authorization through an AgentCore Gateway service role for your target, you can just specify the `credentialProviderType` as `GATEWAY_IAM_ROLE"` and omit the `credentialProvider` field, as in the following example:

```
{
    "credentialProviderType": "GATEWAY_IAM_ROLE"
}
```

## OAuth authorization

If you're using OAuth authorization, you specify the `credentialProviderType` as `OAUTH`. In the object that the `credentialProvider` field maps to, map an `oauthCredentialProvider` field name to an [OAuthCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md") object and provide the values based on your outbound authorization setup.

The structure of the [OAuthCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md") differs depending on the type of authentication pattern that you set up. To learn more about different authentication patterns, see [Supported authentication patterns](common-use-cases.md "common-use-cases.md").

- If you set up machine-to-machine authentication, also known as a client credentials grant or 2-legged OAuth (2LO), follow the structure in the **Client credentials** tab.
- If you set up user-delegated access, also known as an authorization code grant or 3-legged OAuth (3LO), follow the structure in the **Authorization code** tab.

Select one of the following methods:

Client credentials
Specify the `grantType` as `CLIENT_CREDENTIALS`, as in the following example:

```
{
    "credentialProviderType": "OAUTH",
    "credentialProvider": {
        "oauthCredentialProvider": {
            "providerArn": "`string`",
            "grantType": "CLIENT_CREDENTIALS",
            "scopes": [
                "`string`",
                ...
            ],
            "customParameters": {
                "`string`": "`string`"
            }
        }
    }
}
```

Authorization code
Specify the `grantType` as `AUTHORIZATION_CODE` and include, in the `defaultReturnUrl` field, the URL to which to redirect the end user's browser after obtaining the authorization code, as in the following example:

```
{
    "credentialProviderType": "OAUTH",
    "credentialProvider": {
        "oauthCredentialProvider": {
            "providerArn": "`string`",
            "grantType": "AUTHORIZATION_CODE",
            "defaultReturnUrl": "`string`",
            "scopes": [
                "`string`",
                ...
            ],
            "customParameters": {
                "`string`": "`string`"
            }
        }
    }
}
```

To learn more about 3LO authentication, see [OAuth 2.0 authorization URL session binding](oauth2-authorization-url-session-binding.md "oauth2-authorization-url-session-binding.md").

## API key authorization

If you set up API key authorization, you specify the `credentialProviderType` as `API_KEY`. In the object that the `credentialProvider` field maps to, map an `oauthCredentialProvider` field name to an [OAuthCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_OAuthCredentialProvider.md") object and provide the values based on your outbound authorization setup. The following JSON shows the structure:

```
{
    "credentialProviderType": "API_KEY",
    "credentialProvider": {
        "apiKeyCredentialProvider": {
            "providerArn": "`string`",
            "credentialLocation": "HEADER" | "QUERY PARAMETER",
            "credentialParameterName": "`string`",
            "credentialPrefix": "`string`"
        }
    }
}
```
