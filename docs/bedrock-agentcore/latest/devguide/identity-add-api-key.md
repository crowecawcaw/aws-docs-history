# Add API key

API keys provide key-based authentication for services that require direct key
access with secure storage capabilities. An API key is a unique identifier used to
authenticate and authorize access to a resource, enabling your agent to access
external services without embedding sensitive credentials directly in your
application code.

###### To add an API key

1. Open the [AgentCore Identity](https://console.aws.amazon.com/bedrock-agentcore/identity "https://console.aws.amazon.com/bedrock-agentcore/identity") console.
2. In the **Outbound Auth** section, choose
   **Add OAuth client / API key**, then choose
   **Add API key**.
3. For **Name**, you can either use the
   auto-generated name or enter your own descriptive name to help you identify
   this API key in your account. Use alphanumeric characters, hyphens, and
   underscores only, with a maximum length of 50 characters.
4. For **API key**, enter the key value provided
   by your external service. AgentCore Identity securely stores this value and makes it
   available to your agent at runtime.
5. Choose **Add**.
   After creating the API key, AgentCore Identity provides an ARN that you can reference in
   your agent code to access the stored key without exposing sensitive information in
   your application. You can find this ARN in the properties page of the API key
   (Choose the API key name in the **Outbound Auth** section).
