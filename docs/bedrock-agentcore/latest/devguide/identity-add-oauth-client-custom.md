# Add OAuth client using custom

provider

Custom providers enable you to connect to any OAuth2-compatible resource server
beyond the built-in provider options. You can configure custom providers by having
the system retrieve configuration details automatically, or by providing the server
information manually.

###### To add an OAuth client using a custom provider

1. Open the [AgentCore Identity](https://console.aws.amazon.com/bedrock-agentcore/identity "https://console.aws.amazon.com/bedrock-agentcore/identity") console.
2. In the **Outbound Auth** section, choose
   **Add OAuth client / API key**, and then
   select **Add OAuth client**.
3. For **Name**, you can either use the
   auto-generated name or enter your own descriptive name to help you identify
   this OAuth client in your account. Use alphanumeric characters, hyphens, and
   underscores only, with a maximum length of 50 characters.
4. For **Provider**, choose **Custom provider**.
5. In the **Provider configurations** section,
   depending on your provider requirements, choose one of the following
   options:
   1. **Discovery URL** (recommended) –
      Choose this option to have AgentCore Identity automatically retrieve
      configuration details from your provider. You provide the discovery
      URL where your provider publishes its OpenID Connect configuration,
      and AgentCore Identity handles the endpoint discovery process. This is the
      recommended approach when available as it reduces manual
      configuration.
      1. For **Client ID**, enter the
         unique identifier you received when registering your
         application with the identity provider.
      2. For **Client secret**, enter
         the confidential key associated with your client ID that
         AgentCore Identity securely stores for authentication.
      3. For **Discovery URL**, enter
         the URL where your provider publishes its OpenID Connect
         configuration. Discovery URLs must end with
         `.well-known/openid-configuration`. For
         example,
         https://`example.com`/.well-known/openid-configuration.

   2. **Manual config** – Choose this
      option to specify server information directly when your provider
      doesn't support automatic discovery. You'll define each endpoint URL
      individually, giving you complete control over the configuration
      details.
      1. For **Client ID**, enter the
         unique identifier you received when registering your
         application with the identity provider.
      2. For **Client secret**, enter
         the confidential key associated with your client ID that
         AgentCore Identity securely stores for authentication.
      3. For **Issuer**, enter the
         base URL that identifies your authorization server. This
         value appears in the `iss` claim of issued tokens
         and helps verify token authenticity.
      4. For **Authorization
         endpoint**, enter the URL where users will be
         directed to grant permission to your application. This is
         the entry point for the OAuth authorization flow.
      5. For **Token endpoint**, enter
         the URL where your agent exchanges authorization codes for
         access tokens. This endpoint handles the credential exchange
         process.
      6. (Optional) In the **Response
         types** section, configure how your OAuth
         client receives authentication responses by choosing
         **Add response type** and
         selecting the token formats your provider should return.
         Common types include `code` for authorization
         code flow or `token` for implicit flow.

6. Choose **Add OAuth Client**.
   After completing either configuration, AgentCore Identity securely stores your OAuth
   settings and provides an ARN you can reference in your agent code, enabling token
   requests without embedding sensitive credentials in your application. You can find
   this ARN in the properties page of the OAuth client (Choose the client name in the
   **Outbound Auth** section).
