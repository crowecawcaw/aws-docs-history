

# Authentication methods

AWS Quick supports multiple authentication methods for connectors. The available methods depend on the specific connector. During setup, you choose your authentication method from the **OAuth Configuration** options or from the connector-specific authentication settings.

AWS Quick invokes connectors from your AWS Quick account, so the web, mobile, and desktop applications don't call the third-party service directly. AWS Quick stores each connector's OAuth tokens in a token vault in your AWS Quick account and uses the refresh token to renew the access token. With three-legged OAuth (3LO), you sign in to the third-party service, so AWS Quick doesn't receive your password. Some connectors authenticate differently, as the following sections describe.

## Default OAuth app
<a name="quick-managed-auth"></a>

Default authentication lets you connect by choosing the connector and authenticating, with nothing to configure. Behind the scenes, default authentication uses one of three mechanisms: a managed OAuth application that AWS hosts on your behalf, Dynamic Client Registration (DCR), or Client ID Metadata Documents (CIMD). These mechanisms streamline authentication for the MCP servers that a connector relies on. From your perspective, you choose the connector, authenticate, and start using it.

Default authentication includes the following key features:
+ No additional credentials or configuration required.
+ User-specific authentication through provider sign-in.
+ Secure credential storage managed by AWS Quick.
+ Automatic token refresh.
+ 90-day refresh token lifecycle.

To set up default authentication, complete the following steps:

1. Choose **Default OAuth app** as your OAuth configuration.

1. Complete the service provider sign-in flow.

1. Grant the requested permissions.

1. Confirm the connection.

**Note**  
Not all connectors support Default OAuth app. Check the connector-specific documentation for available authentication methods.

## Custom OAuth app
<a name="quick-custom-user-auth"></a>

Custom OAuth app authentication is for organizations that require specific control over the OAuth application configuration. Like Default OAuth app, this method uses a three-legged OAuth (3LO) flow where users sign in directly with the service provider. The difference is that you provide your own OAuth credentials instead of using the AWS Quick managed application.

Custom OAuth app authentication requires the following information:
+ Client ID
+ Client Secret
+ Domain URL
+ Authorization URL
+ Token URL
+ Redirect URL

To set up a custom OAuth app, complete the following steps:

1. Create an OAuth application in your service provider's developer console.

1. Choose **Custom OAuth app** as your OAuth configuration.

1. Enter the credentials from your OAuth application.

1. Complete the sign-in flow and validate the connection.

## Service-to-Service OAuth
<a name="quick-actions-service-to-service-auth"></a>

Service-to-Service OAuth uses client credentials for server-to-server authentication without user interaction. This method is suitable for automated workflows and shared connectors where tools run under a service account.

For select remotely hosted MCP servers, AWS Quick also supports OAuth with Dynamic Client Registration (DCR), which registers the client with the server automatically. For more information, see [MCP servers](integrations-connectors.md#connectors-mcp-servers).

Service-to-Service OAuth requires the following information:
+ Client ID
+ Client Secret
+ Domain URL
+ Token URL
+ Service-specific parameters (varies by connector)

## API key authentication
<a name="quick-actions-api-key-auth"></a>

Some connectors support API key authentication for service-level access. This method uses a single token for authentication and is common for connectors that don't support OAuth.

API key authentication requires the following information:
+ Valid API key from the service provider
+ Base URL or domain
+ Service-specific parameters (such as email or account ID)

## Basic authentication
<a name="quick-actions-basic-auth"></a>

Basic authentication uses a standard user name and password. It is suitable for services that don't support OAuth or API keys.

Basic authentication includes the following key features:
+ Uses standard HTTP Basic Authentication headers.
+ Credentials are base64 encoded and require a secure HTTPS connection.
+ We recommend that you don't use Basic authentication for public-facing services.

## None
<a name="quick-actions-no-auth"></a>

Some connectors support None authentication, which needs no credentials or tokens. This method is limited to public, read-only operations, such as public data feeds. When a connector supports None authentication, its own connector documentation calls that out.

None authentication includes the following key features:
+ No credentials or tokens are needed.
+ Used for public APIs and services.
+ We recommend that you don't use this method for sensitive operations.