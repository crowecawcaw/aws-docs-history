

# Flow block in Connect Customer: External Tool
<a name="external-tool"></a>

This topic defines the flow block for invoking a tool from an external application directly from a flow.

**Note**  
The **External Tool** block is only available in [Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/enable-nextgeneration-amazonconnect.html) instances, and only in certain Regions. For the list of Regions, see [External Tool](regions.md#externaltool_region).

## Description
<a name="external-tool-description"></a>
+ Use this block to invoke a tool from an external application integrated with your Connect Customer instance through an Amazon Bedrock AgentCore gateway. Your flow can send data to and read data from third-party applications, resolving customer issues with fewer steps instead of relying on custom Lambda functions.
+ Run a tool synchronously (the flow pauses until the tool returns) or asynchronously (the flow continues). For an asynchronous invocation, add a second **External Tool** block set to **Load tool result** to retrieve the result.
+ Results are stored in the `$.ExternalTool` namespace.

## Supported channels
<a name="external-tool-channels"></a>

The following table lists how this block routes a contact who is using the specified channel.


| Channel | Supported? | 
| --- | --- | 
| Voice | Yes | 
| Chat | Yes | 
| Task | Yes | 
| Email | Yes | 

## Flow types
<a name="external-tool-types"></a>

You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types):
+ All flows

## Prerequisites and dependencies
<a name="external-tool-prerequisites"></a>

Before you can use this block, you must [integrate an external application with your Connect Customer instance as an MCP server](https://docs.aws.amazon.com/connect/latest/adminguide/3p-apps-mcp-server.html#3p-apps-mcp-server-how-to-integrate). To set up the integration:

1. Navigate to the Connect Customer console within your AWS console.

1. In the Connect Customer console, add a new integration and select **MCP server** as the integration type.

1. Select a Bedrock AgentCore gateway to connect with your instance. If no gateway exists, [create one in Bedrock AgentCore](https://docs.aws.amazon.com/connect/latest/adminguide/3p-apps-mcp-server.html#3p-apps-mcp-server-how-to-integrate) first.

1. In the gateway's inbound identity configuration, add the gateway ID to the **Allowed audiences** field. This is required because if the gateway ID is missing, tool invocations will fail.

1. Associate your Connect Customer instance with the integration by selecting the instance that is configured with the gateway's Discovery URL.

After the integration is complete, the application appears in the **External Tool** block and can be selected by name.

## Properties
<a name="external-tool-properties"></a>

The block supports the following actions. Select an action using **Select an action**. The default is **Invoke tool**.

### Invoke tool
<a name="external-tool-invoke-tool"></a>

The following images show the Invoke tool action configuration in the External Tool block properties.

![The External Tool block showing the Invoke tool action with the Application name and Tool name fields.](http://docs.aws.amazon.com/connect/latest/adminguide/images/external-tool-invoke.png)


![The External Tool block showing the Execution mode and Timeout settings for the Invoke tool action.](http://docs.aws.amazon.com/connect/latest/adminguide/images/external-tool-invoke-2.png)

+ **Application name** (required): The external application to call. You can set this manually or dynamically. Only applications associated with your instance appear.
+ **Tool name** (required): The tool to invoke within the application. You can set this manually or dynamically; the manual list updates by application. Input fields are generated from the tool schema, and tool inputs can be provided manually, dynamically, or as raw JSON.
+ **Execution mode**:
  + **Synchronous**: The contact is routed to the next block only after the External Tool invocation completes.
  + **Asynchronous**: The contact is routed to the next block without waiting for the External Tool invocation to complete. You can configure a [Wait](wait.md) block to wait for an External Tool that is invoked in asynchronous execution mode.
+ **Timeout**: How long to wait before the External Tool invocation times out. The maximum is 8 seconds for **Synchronous** mode and 60 seconds for **Asynchronous** mode.
  + If an External Tool invocation is throttled, or a general service failure (500 error) occurs, the request is retried.
  + When an External Tool invocation returns an error, Connect Customer retries up to three times, up to the specified timeout. At that point, the contact is routed down the **Error** branch.
+ Branches: **Success** and **Error**.

### Load tool result
<a name="external-tool-load-tool-result"></a>

The following image shows the Load tool result action configuration in the External Tool block properties.

![The External Tool block configured for the Load tool result action.](http://docs.aws.amazon.com/connect/latest/adminguide/images/external-tool-load.png)

+ **External tool invocation ID**: The invocation ID of the External Tool that was run in **Asynchronous** mode. `$.ExternalTool.InvocationId` contains the invocation ID of the most recent asynchronously run External Tool.
+ For the **Load tool result** action, set **Namespace** = `ExternalTool` and **Key** = **Invocation ID**.
+ Branches: **Success**, **In progress**, and **Error**.

## Namespace
<a name="external-tool-namespace"></a>

The **External Tool** block writes results to the following namespace paths:
+ `$.ExternalTool.InvocationId` – the current invocation ID.
+ `$.ExternalTool.ResultData` – the tool result (up to 32 KB).

Each new invocation overwrites the previous `$.ExternalTool` result. To keep a result, copy it to a contact attribute (`$.Attributes.*`) or flow attribute (`$.FlowAttribute.*`) before invoking another tool.

## Configuration tips
<a name="external-tool-tips"></a>
+ **Application name** and **Tool name** can be set dynamically as well as manually.
+ Synchronous results are capped at 32 KB. Larger responses take the **Error** branch.

## Example
<a name="external-tool-example"></a>

When a customer contacts a financial institution about a recent transaction, a flow can use the **External Tool** block to retrieve previous case history or recent transactions from an integrated third-party application. The flow can then use the returned data in `$.ExternalTool.ResultData` to determine the next step, such as routing the contact to a specialist or continuing on a standard support path.

## Configured
<a name="external-tool-configured"></a>

After you configure the block, it shows the **Success** and **Error** branches. For a **Load tool result** action, it also shows the **In progress** branch.

![The External Tool block configured with Success and Error branches after being added to a flow.](http://docs.aws.amazon.com/connect/latest/adminguide/images/external-tool-configured.png)
