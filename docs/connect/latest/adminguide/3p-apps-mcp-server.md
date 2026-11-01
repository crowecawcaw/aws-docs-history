

# Integrate an MCP server with Connect Customer
<a name="3p-apps-mcp-server"></a>

To use an MCP server with Connect Customer, you need an Amazon Bedrock AgentCore gateway. The gateway turns your APIs, Lambda functions, and services into MCP tools. AI agents can use these tools.

**Note**  
Each gateway supports one MCP server and one instance. The instance must use the gateway's Discovery URL. For information about setting up the gateway, see [Create a gateway in Bedrock AgentCore](#3p-apps-mcp-server-create-gateway).

## How to integrate an MCP server
<a name="3p-apps-mcp-server-how-to-integrate"></a>

1. On the **Add integration** page, enter the following details:

   1. **Integration information**
      + **Display name** – A name for the integration. This name appears on security profiles. You can change it later.
      + **Description** (optional) – A description of the integration.
      + **Integration type** – Select **MCP server**.
      + **Integration identifier** – A unique ID for the integration. Use letters, numbers, hyphens (-), and underscores (\_). You can't change it later.
**Note**  
The **Integration identifier** doesn't need to match the gateway ID. You can use any value. Add the same value to the gateway's **Allowed audiences** field.  
![The Add integration page showing the Integration information fields for an MCP server.](https://docs.aws.amazon.com/connect/latest/adminguide/images/integrations-3p-mcp-app.png)

   1. **Integration details**

      Select a Bedrock AgentCore gateway to use with Connect Customer. If you don't have a gateway, choose **create a new one**. For more information about the gateway settings that Connect Customer requires, see [Create a gateway in Bedrock AgentCore](#3p-apps-mcp-server-create-gateway).  
![The Integration details section showing gateway selection.](https://docs.aws.amazon.com/connect/latest/adminguide/images/integrations-3p-mcp-select-gateway.png)

   1. **Instance association** (optional)

      Select the instance that uses the gateway's Discovery URL. The default is **None**. You can skip this and add an instance later.  
![The Instance association section showing instance selection options.](https://docs.aws.amazon.com/connect/latest/adminguide/images/3p-apps-mcp-instance.png)

1. Choose **Add integration**.

1. After you add the integration, the **View integration** page opens. It shows a success notification and the **Integration details** section.  
![The View integration page in the Connect Customer console with a success notification and the Integration details section.](https://docs.aws.amazon.com/connect/latest/adminguide/images/3p-apps-mcp-success.png)

## Create a gateway in Bedrock AgentCore
<a name="3p-apps-mcp-server-create-gateway"></a>

When you create a gateway in Bedrock AgentCore for Connect Customer, use the following settings.

**Supported protocol versions**  
Connect Customer supports only 2025 Model Context Protocol (MCP) versions. The gateway's **Supported versions** must include one of the 2025 versions: `2025-03-26`, `2025-06-18`, or `2025-11-25`.  
When you create the gateway, expand **Additional configurations**. Then choose a 2025 version from the **Supported versions** list. You can't change the version later. If an existing gateway doesn't have a 2025 version, create a new one.

![The Define gateway details page in Bedrock AgentCore with a 2025 version selected in Supported versions.](https://docs.aws.amazon.com/connect/latest/adminguide/images/3p-apps-mcp-bedrock.png)


**Note**  
The Discovery URL must use this format: `[connect instance URL]/.well-known/openid-configuration`. For example: `https://my-instance.my.connect.aws/.well-known/openid-configuration`.

**Allowed audiences**  
On the **Configure Inbound Identity** page, choose **Use JSON Web Tokens (JWT)** and **Use existing Identity provider configurations**. Under **Allowed audiences**, enter your **Integration identifier** in the **Audiences** field.  
Connect Customer sends a JWT to the gateway. The token's `aud` (audience) claim has the **Integration identifier**. If the gateway's audiences don't include this value, the gateway rejects the token, and tool calls fail.  
**Allowed audiences** is the only field that Connect Customer needs. You can leave the **Allowed clients**, **Allowed scopes and advertised values**, and **Custom claims** fields empty.

![The Configure Inbound Identity page in Bedrock AgentCore with the Integration identifier entered in the Audiences field.](https://docs.aws.amazon.com/connect/latest/adminguide/images/3p-apps-mcp-bedrock-inbound-identity.png)
