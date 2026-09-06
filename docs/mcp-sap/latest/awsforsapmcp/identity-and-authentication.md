

# Identity and Authentication
<a name="identity-and-authentication"></a>

The AWS for SAP MCP Server uses two layers of authentication: inbound authentication controls access to the Model Context Protocol (MCP) Server, and outbound authentication controls access to SAP. For more information about the authentication patterns supported by Bedrock AgentCore Identity, see [Supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-auth-patterns.html).

## Inbound Authentication
<a name="inbound-authentication"></a>

Inbound authentication determines which clients are allowed to invoke the MCP server. The AgentCore runtime validates incoming JSON Web Tokens (JWT) before requests reach the server. Only requests with a valid token from a trusted identity provider are accepted.

The CloudFormation template supports two inbound authentication options:

1.  **Amazon Cognito** 

   When [Amazon Cognito](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-cognito.html) is selected as the inbound authentication provider, the CloudFormation template automatically creates and configures a Cognito user pool, client, resource server, and domain. MCP Clients authenticate by requesting a token from the Cognito token endpoint using client credentials. The Cognito user pool client ID, client secret, and token endpoint are available in the CloudFormation stack outputs after deployment.

1.  **External Identity Provider** 

   When an external identity provider such as [Microsoft Entra ID](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-idp-microsoft.html) is selected, the CloudFormation template configures the AgentCore runtime to validate tokens issued by that provider.

## Outbound Authentication
<a name="outbound-authentication"></a>

You can choose from the following authentication flows to connect to SAP systems. You select the authentication flow through the CloudFormation template.

### Choosing your outbound authentication setup
<a name="choosing-outbound-auth"></a>


| Scenario | Auth Flow | Protocol | Identity Provider | SAP Configuration | 
| --- | --- | --- | --- | --- | 
| Direct SAP credentials, no IdP | BASIC | Basic Auth | None | SAP System User | 
| SAP as Authorization Server with OAuth2 | M2M | OAuth2 | SAP | SAP OAuth2 Client | 
| External IdP with OIDC | M2M | OIDC | Entra ID | SAP OIDC trust | 
| SAP as Authorization Server with OAuth2 and SAML IdP redirect | User Federation | OAuth2 \+ SAML | Entra ID or other SAML IdP | SAP OAuth2 client \+ SAML trusted provider | 
| External IdP with OIDC | User Federation | OIDC | Entra ID | SAP OIDC trust | 
| External IdP with token exchange | On-Behalf-Of Token Exchange | OIDC | Entra ID | SAP OIDC trust | 

### Basic Authentication
<a name="auth-basic"></a>

The Basic authentication flow retrieves SAP username and password credentials from AWS Secrets Manager at runtime. This is the simplest flow, suitable for development, testing, and environments where direct SAP credentials are acceptable.

**Warning**  
Not recommended for production deployments.

 **How it works:** 

1. At startup, the server validates that the secret specified in the CloudFormation template exists in AWS Secrets Manager. If the secret is not found, the server fails to start.

1. On each SAP OData request, the server calls AWS Secrets Manager to retrieve the username and password from the secret.

 **Key characteristics:** 
+ Credentials are retrieved from AWS Secrets Manager per request.
+ No user interaction is required.
+ No dependency on Bedrock AgentCore Identity.

### Machine to Machine (2-Legged OAuth)
<a name="auth-m2m"></a>

The machine-to-machine (M2M) authentication flow uses Bedrock AgentCore Identity to exchange credentials for an SAP OData (Open Data Protocol) OAuth token without any user interaction. This flow is designed for automated and headless deployments. M2M uses either OAuth2 or OIDC depending on your choice of IdP.

 **How it works:** 

1. At startup, the server validates the OAuth provider specified by the CloudFormation template against Bedrock AgentCore Identity. If the provider does not exist, the server fails to start.

1. Bedrock AgentCore Identity performs the OAuth token exchange and returns an access token.

 **Key characteristics:** 
+ No user interaction required - fully automated token exchange.
+ Token is never persisted in MCP Server.
+ Requires a pre-configured OAuth provider in Bedrock AgentCore Identity.

### User Federation (3-Legged OAuth)
<a name="auth-user-federation"></a>

User Federation authentication flow uses Bedrock AgentCore Identity with a callback URL to perform interactive OAuth token exchange. This flow is designed for scenarios where user-specific access is required, and the user must authorize access via a browser. This flow uses either OAuth2, OIDC, or SAML2 depending on your choice of IdP.

 **How it works:** 

1. At startup, the server validates the OAuth provider against Bedrock AgentCore Identity. If the provider does not exist, the server fails to start.

1. Bedrock AgentCore Identity returns an authorization URL, which the server passes back to the MCP client for the user to open in a browser.

1. The user authorizes access in the browser, which redirects to the AgentCore callback URL.

1. AgentCore then redirects the user’s browser to the client application callback URL to signal the flow is complete.

1. After authorization completes, Bedrock AgentCore Identity issues an access token.

**Note**  
This flow uses two callback URLs: \* The AgentCore callback URL (auto-generated, must be registered with your IdP). \* The client application callback URL (configured via CloudFormation template).

### On-Behalf-Of Token Exchange
<a name="auth-obo-token-exchange"></a>

The On-Behalf-Of (OBO) Token Exchange authentication flow uses Bedrock AgentCore Identity to exchange a user’s inbound token for an outbound access token that preserves the user’s identity. This flow propagates the authenticated user’s identity from the MCP client all the way through to SAP, ensuring that data access is scoped to an individual user. The outbound token exchange happens entirely server-side.

 **How it works:** 

1. The MCP client sends a request with a JWT that identifies the authenticated user.

1. The AgentCore runtime validates the inbound JWT against the configured discovery URL and allowed audiences.

1. Bedrock AgentCore Identity performs the OBO token exchange with the configured identity provider using the outbound app’s client credentials.

1. The identity provider issues a new access token that carries the original user’s identity.

1. The MCP server forwards this token to SAP.

1. SAP validates the token and maps the user identity to a SAP user based on your SAP configuration.

 **Key characteristics:** 
+ User identity is preserved end-to-end.
+ No additional user interaction required after initial login.
+ The token exchange is fully server-side.
+ Requires an identity provider that supports the On-Behalf-Of token exchange grant type.