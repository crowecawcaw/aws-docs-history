# Update API key

You can update an existing API key to replace the key value when your external
service provider rotates credentials. Updating the API key ensures your agents
continue to have access to the external service with the current authentication
information.

###### To update an API key

1. Open the [AgentCore Identity](https://console.aws.amazon.com/bedrock-agentcore/identity "https://console.aws.amazon.com/bedrock-agentcore/identity") console.
2. In the **Outbound Auth** section, select the
   API key you want to update.
3. Choose **Edit**.
4. In the **Update API key** dialog, in
   **API key**, enter the updated key value
   provided by your external service. AgentCore Identity securely stores this new value
   and makes it available to your agent at runtime.
5. Choose **Update**.
   The updated API key configuration takes effect immediately. Your agents will use
   the new API key for all subsequent requests to the external service.
