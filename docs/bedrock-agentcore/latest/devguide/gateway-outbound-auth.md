# Set up outbound authorization for your gateway

Outbound authorization lets Amazon Bedrock AgentCore gateways securely access gateway targets on behalf
of users that were authenticated and authorized during inbound authorization.

AgentCore Gateway supports the following types of outbound authorization:

- **No authorization (not recommended)** – Some target types provide you the option to bypass outbound authorization. This less secure option is not recommended.
- **IAM-based outbound authorization** – Use the [gateway service role](gateway-prerequisites-permissions.md#gateway-service-role-permissions "gateway-prerequisites-permissions.md#gateway-service-role-permissions") to authenticate access to the gateway target with [AWS Signature Version 4 (Sig V4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md").
- **2-legged OAuth (OAuth 2LO)** – An open authorization framework that allows a client application to access resources on the application's behalf, rather than on behalf of the user. For more information, see [OAuth 2.0](https://oauth.net/2/ "https://oauth.net/2/"). You can use OAuth 2LO with a [built-in identity provider](identity-idps.md "identity-idps.md") or with a custom one.
- **API key** – Use the AgentCore service to generate an API key to authenticate access to the gateway target.
  The type of outbound authorization that you can set up is dependent on the gateway target type to which you authorize access:

| Target type     | No authorization | Gateway service role | OAuth client | API key |
| --------------- | ---------------- | -------------------- | ------------ | ------- |
| Lambda function | No               | Yes                  | No           | No      |
| MCP server      | Yes              | No                   | Yes          | No      |
| OpenAPI schema  | No               | No                   | Yes          | Yes     |
| Smithy schema   | No               | Yes                  | No           | No      |

###### Note

If you use an integration provider template as a target, review the supported authorization types for different templates at [Built-in templates from integration providers as targets](gateway-target-integrations.md "gateway-target-integrations.md").

Before adding a target to your gateway, you must set up authorization for it through one of the supported methods.

###### Note

You can skip this prerequisite if you plan to use the AWS Management Console or AgentCore starter toolkit to create your gateway. If you use either of these tools, you can let AgentCore automatically create a service role for you with the necessary permissions to access the target. Each time you add a target, the necessary permissions will be automatically attached to your service role.

Select a topic to learn how to set up that type of authorization:

###### Topics

- [Set up IAM-based outbound authorization with a gateway service role](#gateway-outbound-auth-iam "#gateway-outbound-auth-iam")
- [Set up outbound authorization with an OAuth client](#gateway-outbound-auth-oauth "#gateway-outbound-auth-oauth")
- [Set up outbound authorization with an API key](#gateway-outbound-auth-api-key "#gateway-outbound-auth-api-key")

## Set up IAM-based outbound authorization with a gateway service role

IAM-based outbound authorization lets you use the gateway service role's IAM credentials to authorize with [AWS Signature Version 4 (Sig V4)](../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md "../../../AmazonS3/latest/API/sig-v4-authenticating-requests.md"). This option lets the Amazon Bedrock AgentCore service to authenticate to gateway targets on your gateway callers' behalf.

If you use this option, make sure that the gateway service role has `bedrock-agentcore:InvokeGateway` permissions. The service role's credentials will be used for authentication during gateway invocation.

## Set up outbound authorization with an OAuth client

To set up outbound authorization with an OAuth client, you use the AgentCore Identity service and specify client credentials that you receive from creating a client in either a built-in identity provider (see [Provider setup and configuration](identity-idps.md "identity-idps.md") or a custom identity provider.

###### To set up outbound authorization with an OAuth client

1. Register your client application with a supported third-party provider.
2. You'll receive a client ID, client secret, and possibly other values that you'll reference when you set up the outbound authorization.
3. Follow one of the steps below, depending on your requirements:
   - To configure outbound authorization in the console using a built-in identity provider, follow the steps at [Add OAuth client using included
     provider](identity-add-oauth-client-included.md "identity-add-oauth-client-included.md").
   - To configure outbound authorization in the console using a custom identity provider, follow the steps at [Add OAuth client using custom
     provider](identity-add-oauth-client-custom.md "identity-add-oauth-client-custom.md").
   - To configure outbound authorization using the API, send a [CreateOauth2CredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_CreateOauth2CredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateOauth2CredentialProvider.md") with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp"). For examples, see [Examples for setting OAuth client authorization](#gateway-outbound-auth-oauth-examples "#gateway-outbound-auth-oauth-examples").

   ###### Note

   The shape of the JSON object that the `oauth2ProviderConfigInput` field maps to depends on the provider that you use and must be congruent with the `credentialProviderVendor` value that you specify. To see examples of different configurations for different credential providers, see the outbound authorization examples in your credential provider of choice at [Provider setup and configuration](identity-idps.md "identity-idps.md").

4. Take note of the generated credential ARN (`credentialProviderArn` in the API) and the AWS Secrets Manager secret ARN (`secretArn` in the API). You'll use these values when you create your gateway target.
5. (If you're using a custom gateway service role) Attach the following identity-based policy to your gateway service role:

```
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "GetWorkloadAccessToken",
        "Effect": "Allow",
        "Action": [
            "bedrock-agentcore:GetWorkloadAccessToken",
        ],
        "Resource": [
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default",
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default/workload-identity/`GatewayName`-*"
        ]
      },
      {
        "Sid": "GetResourceOauth2Token",
        "Effect": "Allow",
        "Action": [
            "bedrock-agentcore:GetResourceOauth2Token",
        ],
        "Resource": [
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:token-vault/`TokenVaultId`/oauth2credentialprovider/`CredentialName`"
        ]
      },
      {
        "Sid": "GetSecretValue",
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue",
        ],
        "Resource": [
            "arn:aws:secretsmanager:`us-east-1`:`123456789012`:secret:`SecretId`"
        ]
      }
    ]
}
```

Replace the values of the following fields:

    * In the `GetWorkloadAccessToken` statement, replace the `GatewayName` in the `Resource` list with the name of your gateway.
    * In the `GetResourceOauth2Token` statement, replace the value in the `Resource` list with the ARN of the credential that you just generated.
    * In the `GetSecretValue` statement, replace the value in the `Resource` list with the ARN of the AWS secret returned in the response when you generated the credential.

### Examples for setting OAuth client authorization

The following examples show you how to set authorization through an OAuth client for your gateway target:

CLI

```
aws bedrock-agentcore-control create-oauth2-credential-provider \
  --name oauth-credential-provider \
  --credential-provider-vendor CustomOAuth2 \
  --oauth2-provider-config-input '{
    "customOAuth2ProviderConfig": {
      "oauthDiscovery": {
        "discoveryUrl": "<DiscoveryUrl>"
      },
      "clientId": "<ClientId>",
      "clientSecret": "<ClientSecret>"
    }
  }'
```

Boto3

```
import boto3

client = boto3.client("bedrock-agentcore-control")

client.create_oauth2_credential_provider(
  name="oauth-credential-provider",
  credentialProviderVendor="CustomOAuth2",
  oauth2ProviderConfigInput={
    "oauthDiscovery": {
      "discoveryUrl": "<DiscoveryUrl>"
    },
    "clientId": "<ClientId>",
    "clientSecret": "<ClientSecret>"
  }
)
```

## Set up outbound authorization with an API key

To set up outbound authorization with an API key, you use the AgentCore Identity service and specify an API key that you receive from a supported identity provider.

###### To set up outbound authorization with an OAuth client

1. Register your client application with a supported third-party provider.
2. Set up an API key for the provider's service. Take note of the following values, which you'll specify when you add the gateway target:
   - **Credential location** – Whether the API key should be placed in the header or as a query parameter.
   - **Credential prefix** – The prefix for the credential (ex. Bearer).

3. Follow one of the steps below, depending on your requirements:
   - To create an API key in the AgentCore console, follow the steps at [Add API key](identity-add-api-key.md "identity-add-api-key.md") and specify the value of the API key.
   - To create an API key using the AgentCore API, send a [CreateApiKeyCredentialProvider](../../../bedrock-agentcore-control/latest/APIReference/API_CreateApiKeyCredentialProvider.md "../../../bedrock-agentcore-control/latest/APIReference/API_CreateApiKeyCredentialProvider.md") request with one of the [AgentCore control plane endpoints](../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp "../../../general/latest/gr/bedrock_agentcore.md#bedrock_agentcore_cp") and specify the value of the API key in the `apiKey` field. For examples, see [Examples for setting an API key](#gateway-outbound-auth-api-key-examples "#gateway-outbound-auth-api-key-examples").

4. Take note of the following values, which you'll specify when you add the gateway target:
   - **Credential provider ARN** – An Amazon Resource Name (ARN) generated for the credential provider.
   - **Name** – The name you gave to the API key.
   - **Secret ARN** – An AWS Secrets Manager secret ARN generated for the API key.

5. (If you're using a custom gateway service role) Attach the following identity-based policy to your gateway service role:

```
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "GetWorkloadAccessToken",
        "Effect": "Allow",
        "Action": [
            "bedrock-agentcore:GetWorkloadAccessToken",
        ],
        "Resource": [
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default",
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:workload-identity-directory/default/workload-identity/`GatewayName`-*"
        ]
      },
      {
        "Sid": "GetResourceApiKey",
        "Effect": "Allow",
        "Action": [
            "bedrock-agentcore:GetResourceApiKey",
        ],
        "Resource": [
            "arn:aws:bedrock-agentcore:`us-east-1`:`123456789012`:token-vault/`TokenVaultId`/apikeycredentialprovider/`Name`"
        ]
      },
      {
        "Sid": "GetSecretValue",
        "Effect": "Allow",
        "Action": [
            "secretsmanager:GetSecretValue",
        ],
        "Resource": [
            "arn:aws:secretsmanager:us-east-1:123456789012:secret:`SecretId`"
        ]
      }
    ]
}
```

Replace the values of the following fields:

    * In the `GetWorkloadAccessToken` statement, replace the `GatewayName` in the `Resource` list with the name of your gateway.
    * In the `GetResourceApiKey` statement, replace the value in the `Resource` list with the ARN of the credential that you just generated.
    * In the `GetSecretValue` statement, replace the value in the `Resource` list with the ARN of the AWS secret returned in the response when you generated the credential.

### Examples for setting an API key

The following examples show you how to set an API key for your gateway target:

CLI

```
aws bedrock-agentcore-control create-api-key-credential-provider \
  --name api-key-credential-provider \
  --api-key <API_KEY_VALUE>
```

Boto3

```
import boto3

client = boto3.client("bedrock-agentcore-control")

client.create_api_key_credential_provider(
  name="api-key-credential-provider",
  apiKey="<API_KEY_VALUE>"
)
```
