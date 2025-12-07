# Set up inbound authorization for your gateway

Before you create your gateway, you must set up inbound authorization. Inbound authorization validates users who attempt to access targets through your AgentCore gateway. AgentCore supports the following types of inbound authorization:

- **JSON Web Token (JWT)** – A secure and compact token used for authorization. After creating the JWT, you specify it as the authorization configuration when you create the gateway. You can create a JWT with any of the identity providers at [Provider setup and configuration](identity-idps.md "identity-idps.md").
- **IAM identity** – Authorizes through the credentials of the AWS IAM identity trying to access the gateway.
- **No Authorization** – The gateway will not perform any inbound authorization. This makes your gateway accessible to all users to be invoked.

###### Important

Do not use No Authorization gateways for testing or development purposes. No Authorization gateways should only be used for production gateways that you intend to make public after you have implemented all the security best practices listed later on in this page.

###### Note

If use the AWS Management Console or AgentCore starter toolkit to create your gateway, you can create a default inbound authorization configuration using Amazon Cognito during gateway creation. If you plan to use the default authorization configuration, you can skip this prerequisite.

If you don't plan to use the default authorization configuration using Amazon Cognito, select the topic that corresponds to the type of authorization that you plan to use to learn how to set it up:

###### Topics

- [IAM-based inbound authorization](#gateway-inbound-auth-iam "#gateway-inbound-auth-iam")
- [JSON Web Token (JWT)-based inbound authorization](#gateway-inbound-auth-jwt "#gateway-inbound-auth-jwt")
- [No Authorization](#gateway-inbound-auth-none "#gateway-inbound-auth-none")

## IAM-based inbound authorization

IAM-based inbound authorization lets you use the gateway caller's IAM credentials for authorization. You can use this option if you want to create an IAM identity through which users that call your gateway can be authenticated.

###### To set up IAM-based inbound authorization

1. Create or use an existing IAM identity for your gateway callers.
2. Create an identity-based IAM policy that contains the following permissions:
   - `bedrock-agentcore:InvokeGateway` – After you create the gateway, you should modify this policy such that the `Resource` field is scoped to the gateway that you create as a security best practice.

3. Attach the policy to the gateway caller identity.

###### Example policy

The following example shows a policy you could attach to an identity to allow it to invoke a gateway with the ID `my-gateway-12345`

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowGatewayInvocation",
      "Effect": "Allow",
      "Action": [
        "bedrock-agentcore:InvokeGateway"
      ],
      "Resource": [
        "arn:aws:bedrock-agentcore:us-east-1:123456789012:gateway/`my-gateway-12345`"
      ]
    }
  ]
}
```

###### Resources

- For more information about AWS Identity and Access Management, see [Identity and access management for Amazon Bedrock AgentCore](security-iam.md "security-iam.md").
- For more information about Amazon Bedrock AgentCore actions, resources, and condition keys that you can specify in IAM policies, see [Actions, resources, and condition keys for Amazon Bedrock AgentCore](../../../service-authorization/latest/reference/list_amazonbedrockagentcore.md "../../../service-authorization/latest/reference/list_amazonbedrockagentcore.md").

## JSON Web Token (JWT)-based inbound authorization

A JSON Web Token (JWT) is a secure and compact token used for authorization. You can create a JWT with a supported identity provider. After you create a JWT, you can retrieve it and specify it as the authorization configuration when you create the gateway.

###### Important

Using inbound authorization based on JWT tokens will result in logging of some claims
of the JWT token in CloudTrail. The entry includes the [Subject](http://openid.net/specs/openid-connect-core-1_0.html#Claims "http://openid.net/specs/openid-connect-core-1_0.html#Claims") of the provided web identity token. We recommend that you avoid
using any personally identifiable information (PII) in this field. For example,
you could instead use a GUID or a pairwise identifier, as [suggested in the OIDC specification](http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes "http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes").

You can use the AgentCore starter toolkit to set up a default JWT, or create one manually with a supported identity provider. To learn more about different methods for setting up a JWT, select from the following topics:

###### Topics

- [Set up a default JWT](#gateway-inbound-auth-jwt-default "#gateway-inbound-auth-jwt-default")
- [Set up a JWT manually](#gateway-inbound-auth-jwt-manual "#gateway-inbound-auth-jwt-manual")

### Set up a default JWT

The AgentCore starter toolkit lets you easily create a default authorization configuration using Amazon Cognito that you can then use when creating a gateway. To create this default JWT, run the following code example:

```
# Initialize gateway client from starter toolkit
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient
client = GatewayClient()

# Retrieve JWT from the create response and store as the authorization configuration. When you create the gateway, specify it in the authorizer_config field
cognito_result = client.create_oauth_authorizer_with_cognito("my-gateway")
authorizer_configuration = cognito_result["authorizer_config"]
```

The `cognito_result` contains authentication and authorization information:

- You'll use the authorizer configuration when you create the gateway.
- For inbound authorization when invoking your gateway, you'll need to obtain an access token by using your client ID, client secret, and the token endpoint. For more information on how to obtain your access token, see the **Example** at [Use an AgentCore gateway](gateway-using.md "gateway-using.md") or [The token issuer endpoint](../../../cognito/latest/developerguide/token-endpoint.md "../../../cognito/latest/developerguide/token-endpoint.md") in the Amazon Cognito Developer Guide.

### Set up a JWT manually

Amazon Bedrock AgentCore supports JWTs from all identity providers. You can see some examples at [Provider setup and configuration](identity-idps.md "identity-idps.md").

In the process of creating the JWT, take note of the following values, which you'll fill out in the [CustomJWTAuthorizerConfiguration](../../../bedrock-agentcore-control/latest/APIReference/API_CustomJWTAuthorizerConfiguration.md "../../../bedrock-agentcore-control/latest/APIReference/API_CustomJWTAuthorizerConfiguration.md") when you create a gateway, if they're applicable to your use case:

- **Discovery URL** – The URL from which login credentials and the token endpoint can be retrieved.
- **Client ID** – The public identifier of a client application that requests a token, validated against the `client_id` claim.
- **Client secret** – The private key that authenticates access for the client application to retrieve a token.
- **Allowed audience** – The identifier that validates the intended recipients or consumers of a token via the `aud` claim.
- **Allowed scopes** – The scopes that define the limitations of an application's access to a user's account. For more information, see [OAuth Scopes](https://oauth.net/2/scope/ "https://oauth.net/2/scope/").
- **Other required claim values** – Depending on the authorizer you use, you might need to specify required custom claim fields and rules to match the claim field value to for authentication.

You'll need these values to do the following:

- Create the gateway by specifying values in the [authorizer configuration](../../../bedrock-agentcore-control/latest/APIReference/API_AuthorizerConfiguration.md "../../../bedrock-agentcore-control/latest/APIReference/API_AuthorizerConfiguration.md").
- Obtain authorization credentials to invoke the gateway. To learn how to obtain your credentials, look up your identity provider's documentation. For example, if you used Amazon Cognito, see [The token issuer endpoint](../../../cognito/latest/developerguide/token-endpoint.md "../../../cognito/latest/developerguide/token-endpoint.md") in the Amazon Cognito Developer Guide.

## No Authorization

You can create a gateway that is configured with no authorization by using `authorizerType=NONE`. The gateway will not perform any authorization on the incoming gateway request and the request can be unauthenticated.

###### Important

Do not use No Authorization gateways for testing or development purposes. No Authorization gateways should only be used for production gateways that you intend to make public after you have implemented all the security best practices listed below.

###### Security Best Practices

1. Use the `bedrock-agentcore:GatewayAuthorizerType` condition key to selectively allow/deny access within your organization for creating gateways with `authorizerType=NONE`
2. Do not use No Authorization gateways out of convenience for testing. They should be used for gateways you intend to make public but have implemented your own custom throttling rules and checks to ensure your public gateway can handle unauthenticated users
3. Do not use No Authorization gateways with targets that may respond with sensitive information. Although targets are configured with their own authorization configurations, it is best to add another security layer on the gateway.
