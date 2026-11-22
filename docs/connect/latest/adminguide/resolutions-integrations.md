

# Connect business applications

 Work plan Steps call your business applications through flow modules. A Step's **InvokeFlowModule** configuration names the module to run. The module uses the **External tool** flow block to call a third-party API, such as a CRM or an order management system, through an Amazon Bedrock AgentCore gateway. It returns the result to the Work plan as contact attributes. 

 Extracting information from customer messages doesn't need a flow module. Resolutions uses the prebuilt agentic data extraction capability in Connect Customer and configures it for you in each version's information extraction flow. For more information, see [How Resolutions works](resolutions-how-it-works.md). 

## Call a business application with the External tool block
<a name="resolutions-integrations-call-a-business-application-with-the-external-tool-block"></a>

 The External tool block calls an API that you register as an external integration application on your instance. The block has two actions, **Invoke external tool** and **Load external tool result**. If the tool returns within a few seconds, you need only the invoke action. For long-running tools, invoke the tool and then load the result, because the call is asynchronous. 

The following procedure registers an API and confirms that a flow can call it.

### Step 1: Create a credential provider
<a name="resolutions-integrations-step-1-create-a-credential-provider"></a>

 In the Amazon Bedrock AgentCore console, open **Identity** and create a credential provider for the API. 
+  Choose **OAuth2** for APIs that use client credentials. 
+  Choose **API key** for APIs that use a token or a header. 

### Step 2: Create the gateway
<a name="resolutions-integrations-step-2-create-the-gateway"></a>

1.  In the AgentCore console, choose **Gateways**, and then choose **Create**. 

1. For protocol, choose **MCP**.

1. For inbound authorization, choose **Custom JWT**.

1.  For **Discovery URL**, enter your Connect Customer instance's OpenID Connect endpoint. 

   ```
   https://{{your-instance-url}}/.well-known/openid-configuration
   ```

1.  For **Allowed audiences**, enter a placeholder value. You replace it in the next step. 

1.  Expand **Additional configurations**. For **Supported versions**, choose a 2025 MCP version, such as 2025-03-26, 2025-06-18, or 2025-11-25. Connect Customer supports only 2025 versions, and you can't change the version after you create the gateway. 

1.  Create the gateway and wait for its status to change to **Ready**. 

 For the gateway settings that Connect Customer requires, see [Integrate an MCP server with Connect Customer](3p-apps-mcp-server.md). 

 For more information, see [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html). 

### Step 3: Set the allowed audience to the gateway ID
<a name="resolutions-integrations-step-3-set-the-allowed-audience-to-the-gateway-id"></a>

1.  Copy the **Gateway ID** from the gateway's details page. 

1.  Edit **Inbound Auth** and replace the placeholder audience with the gateway ID. 

1. Leave **Allowed clients** empty.

 Connect Customer sends the gateway a token whose audience claim is the integration's identifier. In step 5 you use the gateway ID as that identifier, so the allowed audience must be the gateway ID. If the two values don't match, the gateway rejects every call from Connect Customer. The ID doesn't exist until you create the gateway, which is why this is a separate step. 

### Step 4: Add a target
<a name="resolutions-integrations-step-4-add-a-target"></a>

1.  On the gateway, open **Targets** and choose **Add**. 

1.  For the target type, choose OpenAPI, and provide the API's OpenAPI schema. You can paste the schema inline or point to it in an Amazon S3 bucket. 

    Each `operationId` in the schema becomes a callable tool, so give each operation a clear name. The External tool block sends each tool input as a string. Declare `"type": "string"` for each parameter that receives a value from the flow, including numeric IDs. If a parameter is declared as an integer, the gateway rejects the call and the block takes the error branch. 

1. Select the credential provider from step 1.

1.  Wait for the target's status to change to **Ready**. 

 One gateway can hold several targets. To add another API later, repeat this step only. The gateway and the integration stay as they are. 

### Step 5: Add the gateway as an MCP server integration
<a name="resolutions-integrations-step-5-add-the-gateway-as-an-mcp-server-integration"></a>

 Register the gateway with Connect Customer as an MCP server integration, and associate the integration with your instance. Each gateway supports one integration and one instance. 

**To add the integration in the console**

1.  In the Connect Customer console, open the **Add integration** page. 

1.  Under **Integration information**, enter the following. 
   +  **Display name**. A name for the integration. It appears on security profiles, and you can change it later. 
   +  **Integration type**. Choose **MCP server**. 
   +  **Integration identifier**. Enter your gateway ID. You can't change the identifier later. 

1.  Under **Integration details**, choose the AgentCore gateway from step 2. 

1.  Under **Instance association**, choose your instance. It must be the instance whose Discovery URL you entered in step 2. 

1.  Choose **Add integration**. The **View integration** page opens and shows a success notification. 

 For more information, see [Integrate an MCP server with Connect Customer](3p-apps-mcp-server.md). 

**Note**  
 The published guide lets you use any value for the integration identifier, as long as the gateway's allowed audience has the same value. Use the gateway ID for both. The External tool block in step 6 refers to the integration by the gateway ID. 

**To add the integration with the AWS CLI**

 Install the latest version of the AWS CLI before you run these commands. Earlier versions don't support the `--application-type` parameter. 

1.  Create an application of type `MCP_SERVER` whose namespace is your gateway ID, and whose access URL is the gateway's MCP endpoint URL from the gateway's details page. 

   ```
   aws appintegrations create-application \
     --name "{{display-name}}" \
     --namespace "{{gateway-id}}" \
     --application-type MCP_SERVER \
     --application-source-config '{"ExternalUrlConfig":{"AccessUrl":"{{gateway-mcp-url}}"}}' \
     --region {{your-region}}
   ```

   Note the `Arn` in the response.

1. Associate the application with your instance.

   ```
   aws connect create-integration-association \
     --instance-id {{instance-id}} \
     --integration-type APPLICATION \
     --integration-arn {{application-arn}} \
     --region {{your-region}}
   ```

**Important**  
 You can't change the application's namespace or access URL after you create it. To use a different gateway, create a new integration and associate it with your instance. 

### Step 6: Confirm the tool binding
<a name="resolutions-integrations-step-6-confirm-the-tool-binding"></a>

Open the External tool block in your flow and check both values.


| Field | Value | 
| --- | --- | 
| ApplicationName | Your gateway ID | 
| ToolName |  gateway\_{{gatewayId}}\_\_{{targetName}}\_\_\_{{operationId}}  | 

**Important**  
 View the block, and then close it without saving. Saving in the flow designer can rewrite the tool name. 

### Step 7: Test the integration
<a name="resolutions-integrations-step-7-test-the-integration"></a>

 Start a test contact against a flow that contains the block. A successful run follows the success branch, and the flow log entry for the block shows the tool's response in `ExternalResults`. 

 The flow log doesn't say why the block took the error branch. To find out where the call failed, do the following. 

1.  In the CloudWatch console, open the `AWS/Bedrock-AgentCore` metrics for your gateway, and check the metrics for the `tools/call` method. 
   +  If `tools/call` has no invocations, the call didn't reach the gateway. Check the `ApplicationName` and `ToolName` values from step 6, and the allowed audience from step 3. 
   +  If `UserErrors` increased, the gateway rejected the request. Check that the tool inputs match the parameter types in your OpenAPI schema. For more information, see step 4. 

1.  If the gateway shows no errors, call the third-party API directly with the same credential. An expired trial account or a stopped database is a common cause. 

## Build a flow module that calls an external tool
<a name="resolutions-integrations-build-a-flow-module-that-calls-an-external-tool"></a>

 A flow module is a reusable flow. It declares typed inputs, runs a sequence of blocks, and returns typed outputs. When you wrap an External tool call in a module, every Work plan can call the same integration by name. You choose the module in a Step's **InvokeFlowModule** configuration. 

 This example builds a module that takes a Salesforce case ID and returns selected Salesforce case fields through a `getSalesforceCase` tool on your gateway. For general information about modules, see [Flow modules for reusable functions](contact-flow-modules.md). 

### Prerequisites
<a name="resolutions-integrations-prerequisites"></a>
+  An AgentCore gateway with a **Ready** target that exposes the tool. 
+  An `MCP_SERVER` application that's associated with your instance and whose namespace matches the gateway ID. 
+  The full tool name, in the form `gateway_{{gatewayId}}__{{targetName}}___{{operationId}}`. 

### Step 1: Declare inputs and outputs
<a name="resolutions-integrations-step-1-declare-inputs-and-outputs"></a>

 A module's contract lives in a `Settings` object inside the flow content, not in a separate field. 
+  **InputParameters.** Add one entry for each input. In this example, add a required `caseId` of type String. 
+  **OutputParameters.** Add one entry for each returned field, such as `CaseNumber`, `Status`, `Priority`, `ContactEmail`, and `SLAViolation__c`. Custom Salesforce fields keep their `__c` suffix. 

 These declarations make the module's inputs and outputs visible in the flow designer. At run time, the values move through contact attributes, so use the same names here as the attribute keys you set and read. 

### Step 2: Invoke the tool
<a name="resolutions-integrations-step-2-invoke-the-tool"></a>

 Add an External tool block as the module's start action, and configure it as follows. 


| Setting | Value | 
| --- | --- | 
| ApplicationName | The gateway ID, not the application's display name | 
| ToolName |  gateway\_{{gatewayId}}\_\_SalesforceCases\_\_\_getSalesforceCase  | 
| InvocationType |  SYNCHRONOUS, so the module waits for the result  | 
| Input | "caseId": "$.Attributes.caseId" | 

**Important**  
 Read the input from `$.Attributes.caseId`, not `$.Parameters.caseId`. The `Parameters` reference resolves to an empty value at run time. The tool receives no case ID and returns an empty result. The call itself succeeds, so neither the flow nor Resolutions has an error to report. 

 Route the block's error branch to a separate end action, so that a failed call never writes partial outputs. 

### Step 3: Capture the response
<a name="resolutions-integrations-step-3-capture-the-response"></a>

 In a **Set contact attributes** block, map each field from the tool's response. 

```
CaseNumber      = $.ExternalTool.ResultData.CaseNumber
Status          = $.ExternalTool.ResultData.Status
Priority        = $.ExternalTool.ResultData.Priority
ContactEmail    = $.ExternalTool.ResultData.ContactEmail
SLAViolation__c = $.ExternalTool.ResultData.SLAViolation__c
```

**Warning**  
 Don't use `$.External.{{field}}`, which is the AWS Lambda namespace, or `$.ExternalResults.{{field}}`, which is the key in flow logs. Both resolve to empty strings. The block completes successfully and writes blank values, so neither the flow nor Resolutions has an error to report. If your attributes come back empty, check this path first. 

### Step 4: End the module
<a name="resolutions-integrations-step-4-end-the-module"></a>

 End the module with an **End flow module execution** block. Leave its parameters empty. The block doesn't accept a `Result`, `ResultData`, `Outputs`, or end-behavior property. The module returns its values through the contact attributes from step 3. 

### Step 5: Call the module
<a name="resolutions-integrations-step-5-call-the-module"></a>

 In a Step's **InvokeFlowModule** configuration, choose the module. If you call the module from your own flow, use an **Invoke module** block. The block takes only the module ID, with no inline parameters. Before the block, set the input as a contact attribute, for example with a **Set contact attributes** block that sets `caseId`. After the module returns, read the outputs as `$.Attributes.CaseNumber`, `$.Attributes.Status`, and so on. 

### Step 6: Test the module
<a name="resolutions-integrations-step-6-test-the-module"></a>

 Enable [flow logs](contact-flow-logs.md) and start a test contact with the input attribute set. A successful run shows these entries in order. 

1.  `InvokeExternalTool` with a populated `ExternalResults` object 

1. `SetAttributes` entries with the real values

1. `ReturnFromFlowModule`

 If the `SetAttributes` values are empty, check the input path from step 2 and the response path from step 3. Those are the two places where blank values come from. 