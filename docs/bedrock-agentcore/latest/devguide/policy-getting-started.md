

# Getting started with Policy in AgentCore
<a name="policy-getting-started"></a>

In this tutorial, you’ll learn how to set up Policy in AgentCore and integrate it with a Amazon Bedrock AgentCore Gateway using the AgentCore CLI. You’ll create a refund processing tool with Cedar policies that enforce business rules for refund amounts.

**Topics**
+ [Prerequisites](#policy-getting-started-prerequisites)
+ [Step 1: Setup and install](#policy-getting-started-setup)
+ [Step 2: Add a gateway with a policy engine](#policy-getting-started-create-script)
+ [Step 3: Deploy](#policy-getting-started-run-setup)
+ [Step 4: Test the policy](#policy-getting-started-test)
+ [What you’ve built](#policy-getting-started-results)
+ [Troubleshooting](#policy-getting-started-troubleshooting)
+ [Clean up](#policy-getting-started-cleanup)

## Prerequisites
<a name="policy-getting-started-prerequisites"></a>

Before starting, make sure you have the following:
+  ** AWS Account** with credentials configured. To configure credentials, you can install and use the AWS Command Line Interface by following the steps at [Getting started with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
+  **Node.js 20\+** installed
+  **IAM permissions** for creating roles, Lambda functions, policy engines, and using Amazon Bedrock AgentCore
+  **A Lambda function** that processes refund requests. You can use an existing function or create one for this tutorial. Note the function ARN for use in Step 2.

The AgentCore CLI checks the CDK bootstrap stack during deployment. If bootstrap is required, interactive deployment asks for confirmation. Use `agentcore deploy --yes` to authorize it automatically.

## Step 1: Setup and install
<a name="policy-getting-started-setup"></a>

Install the AgentCore CLI:

```
npm install -g @aws/agentcore
```

Create a new AgentCore project:

**Example**  

1. 

   ```
   agentcore create --name PolicyDemo --language Python --framework Strands \
     --model-provider Bedrock --memory none
   cd PolicyDemo
   ```

   These options create a Python Strands agent that uses Amazon Bedrock and no memory. The `cd` command moves into the project directory where subsequent commands must be run.

1. You can also run `agentcore create` without flags to use the interactive wizard. The wizard guides you through selecting a project name, agent framework, model provider, and other options. After project creation, change into the project directory with **cd PolicyDemo**.

## Step 2: Add a gateway with a policy engine
<a name="policy-getting-started-create-script"></a>

Use the AgentCore CLI to add a gateway, a Lambda function target, and a policy engine to your project.

 **Add a gateway** 

Create a gateway with no inbound authorization (for simplicity in this tutorial) and attach your agent to it:

**Example**  

1. 

   ```
   agentcore add gateway --name PolicyGateway --authorizer-type NONE --runtimes PolicyDemo
   ```

1. Run `agentcore` to open the TUI, then select **add** and choose **Gateway** :

1. Enter the gateway name:  
![Gateway wizard: enter name](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-name.png)

1. Select the authorizer type. For this tutorial, choose **NONE** :  
![Gateway wizard: select NONE authorizer](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-auth-none.png)

1. Configure advanced options or accept the defaults:  
![Gateway wizard: advanced configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-advanced.png)

1. Review the configuration and press **Enter** to confirm:  
![Gateway wizard: review configuration](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-add-confirm.png)

 **Add a Lambda function target with a refund tool** 

Register your Lambda function as a gateway target with a tool schema that defines a refund processing tool. Create a `refund_tools.json` file in your project directory with the following contents:

```
[
  {
    "name": "process_refund",
    "description": "Process a customer refund request for a given dollar amount",
    "inputSchema": {
      "type": "object",
      "description": "Input for processing a refund",
      "properties": {
        "amount": {
          "type": "integer",
          "description": "The refund amount in dollars"
        }
      },
      "required": ["amount"]
    }
  }
]
```

**Example**  

1. 

   ```
   agentcore add gateway-target --name RefundTarget --type lambda-function-arn \
     --lambda-arn ++<YOUR_LAMBDA_ARN>++ \
     --tool-schema-file refund_tools.json \
     --gateway PolicyGateway
   ```

   Replace `<YOUR_LAMBDA_ARN>` with the ARN of your Lambda function. The `refund_tools.json` file defines the tool schema for the refund tool.

1. Run `agentcore` to open the TUI, then select **add** and choose **Gateway Target** :

1. Enter the target name.

1. Select **Lambda function** as the target type:  
![Gateway target wizard: select Lambda function](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/gateway-target-type-lambda.png)

1. Enter the Lambda ARN and tool schema file path, then confirm.

 **Add a policy engine** 

Create a policy engine and attach it to the gateway in ENFORCE mode:

**Example**  

1. 

   ```
   agentcore add policy-engine --name RefundPolicyEngine \
     --attach-to-gateways PolicyGateway \
     --attach-mode ENFORCE
   ```

1. Run `agentcore` to open the TUI, then select **add** and choose **Policy Engine** :

1. Enter the policy engine name:  
![Policy engine wizard: enter name](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/policy-engine-name.png)

1. Select the gateways to attach the policy engine to:  
![Policy engine wizard: attach gateways](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/policy-engine-gateways.png)

1. Choose the enforcement mode. Select **ENFORCE** :  
![Policy engine wizard: select enforcement mode](http://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/images/tui/policy-engine-mode.png)

 **Create a Cedar policy** 

Provide a Cedar policy file directly. Cedar does not allow wildcard resources in policy statements. This requires a two-phase deployment: first deploy without the policy to create the gateway, then retrieve the gateway ARN. Then add the policy and redeploy.

1. Deploy the gateway first (see [Step 3: Deploy](#policy-getting-started-run-setup)), then run **agentcore status** to get the gateway ARN.

1. Create a `refund_policy.cedar` file in your project directory, substituting the gateway ARN from the previous step:

   ```
   permit(principal,
     action == AgentCore::Action::"RefundTarget___process_refund",
     resource == AgentCore::Gateway::"<gateway-arn>")
   when {
     context.input.amount < 1000
   };
   ```

1. Add the policy and redeploy:

   ```
   agentcore add policy --name RefundLimit \
     --engine RefundPolicyEngine \
     --source refund_policy.cedar
   agentcore deploy
   ```

Alternatively, after deploying your resources in Step 3, you can generate a Cedar policy from a natural-language description:

```
agentcore add policy --name RefundLimit \
  --engine RefundPolicyEngine \
  --generate "Only allow refunds under 1000 dollars" \
  --gateway PolicyGateway
```

The `--generate` flag requires the gateway to be deployed first, because it calls an AWS API that needs the gateway ARN to convert natural language into Cedar. This approach automatically resolves gateway ARNs, making it the simplest path for creating policies.

### Understanding the setup
<a name="policy-understanding-setup-script"></a>

The CLI commands above configure several resources in your AgentCore project. Here’s a detailed explanation of each component.

**Topics**
+ [Create a Gateway](#policy-create-gateway)
+ [Add Lambda target](#policy-add-lambda-target)
+ [Create a Policy Engine](#policy-create-policy-engine)
+ [Create Cedar Policy](#policy-create-cedar-policy)
+ [Attach Policy to Gateway](#policy-attach-to-gateway)

#### Create a Gateway
<a name="policy-create-gateway"></a>

The **agentcore add gateway** command creates a gateway that acts as your MCP server endpoint. Setting `--authorizer-type NONE` disables inbound authorization for simplicity in this tutorial. In production, use IAM or JWT authorization to secure your gateway.

#### Add Lambda target
<a name="policy-add-lambda-target"></a>

The **agentcore add gateway-target** command registers a Lambda function as a target in the gateway. The tool schema file defines the inputs that agents can pass to the function, such as a refund amount.

#### Create a Policy Engine
<a name="policy-create-policy-engine"></a>

The **agentcore add policy-engine** command creates a policy engine — a collection of Cedar policies that evaluates and authorizes agent tool calls. The policy engine intercepts all requests at the gateway boundary and determines whether to allow or deny each action based on the defined policies. This provides deterministic authorization outside of the agent’s code, ensuring consistent security enforcement regardless of how the agent is implemented.

#### Create Cedar Policy
<a name="policy-create-cedar-policy"></a>

Cedar is an open-source policy language developed by AWS for writing authorization policies. The **agentcore add policy** command creates a Cedar policy that governs tool calls through the gateway. You can either generate a policy from a natural-language description using `--generate` , or provide a Cedar policy file directly using `--source`.

The following is an example Cedar policy that allows refunds under USD $1000:

```
permit(principal,
  action == AgentCore::Action::"RefundTarget___process_refund",
  resource == AgentCore::Gateway::"<gateway-arn>")
when {
  context.input.amount < 1000
};
```

The policy uses:
+  `permit` – Allows the action (Cedar also supports `forbid` to deny actions)
+  `principal` – The entity making the request
+  `action` – The specific tool being called (RefundTarget\_\_\_process\_refund)
+  `resource` – The gateway instance where the policy applies
+  `when` condition – Additional requirements (amount must be < USD $1000)

#### Attach Policy to Gateway
<a name="policy-attach-to-gateway"></a>

The `--attach-to-gateways` and `--attach-mode ENFORCE` flags on the **agentcore add policy-engine** command attach the policy engine to the gateway in ENFORCE mode. In this mode:
+ Every tool call is intercepted and evaluated against all policies
+ By default, all actions are denied unless explicitly permitted
+ If any `forbid` policy matches, access is denied (forbid-wins semantics)
+ Policy decisions are logged to CloudWatch for monitoring and compliance

This ensures all agent operations through the gateway are governed by your security policies.

## Step 3: Deploy
<a name="policy-getting-started-run-setup"></a>

Deploy all resources to AWS:

```
agentcore deploy
```

The AgentCore CLI creates the gateway, registers the Lambda target, and provisions the policy engine. If you provided an ARN-based Cedar policy file, add it after this deploy and run **agentcore deploy** again to attach it. This process takes approximately 2–3 minutes per deploy.

After deployment completes, you can verify the status of your resources:

```
agentcore status
```

## Step 4: Test the policy
<a name="policy-getting-started-test"></a>

Test the policy by sending requests to the gateway. Because the gateway uses `--authorizer-type NONE` , you can send requests directly with **curl**.

The gateway URL shown in the output of **agentcore status** is the base endpoint. MCP requests go to the `/mcp` path on that endpoint, so append `/mcp` to the URL before sending requests.

 **Test 1: Refund USD $500 (should be allowed)** 

The refund amount of USD $500 is under the USD $1000 limit, so the policy engine permits the request:

```
curl -X POST ++<GATEWAY_URL>++/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"RefundTarget___process_refund","arguments":{"amount":500}}}'
```

 **Test 2: Refund USD $2000 (should be denied)** 

The refund amount of USD $2000 exceeds the USD $1000 limit, so the policy engine denies the request:

```
curl -X POST ++<GATEWAY_URL>++/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"RefundTarget___process_refund","arguments":{"amount":2000}}}'
```

**Note**  
Replace `<GATEWAY_URL>` with the gateway URL shown in the output of **agentcore status**, then append `/mcp`.

## What you’ve built
<a name="policy-getting-started-results"></a>

Through this tutorial, you’ve created:
+  **MCP Server (Gateway)** – A managed endpoint for tools
+  **Lambda target** – A refund processing tool registered in the gateway
+  **Policy engine** – Cedar-based policy evaluation system
+  **Cedar policy** – Governance rule allowing refunds under USD $1000

## Troubleshooting
<a name="policy-getting-started-troubleshooting"></a>

If you encounter issues during setup or testing, refer to the following common problems and solutions:


| Issue | Solution | 
| --- | --- | 
| "AccessDeniedException" | Check IAM permissions for bedrock-agentcore:\* | 
| Gateway not responding | Wait 30–60 seconds after deployment for DNS propagation | 
| Deploy fails | Run **agentcore status** to check resource states and review error messages | 
| Policy not enforced | Verify the policy engine is attached in ENFORCE mode by running **agentcore status**  | 
| Cedar validation error during deploy | Cedar policies must use specific resource ARNs — wildcard resources (e.g., `permit(principal, action, resource);` ) are rejected. Use the gateway ARN from **agentcore status** in your Cedar policy’s `resource` field. | 
| Tool call denied unexpectedly | The policy engine is enforcing and the Cedar policy denied the request. Verify that the policy’s `action` and `resource` fields match the tool call being made. | 
| Deploy fails with policy validation error | The default validation mode `FAIL_ON_ANY_FINDINGS` runs both schema checks and semantic validation, rejecting the policy if either produces findings. You can set the validation mode to `IGNORE_ALL_FINDINGS` to run only schema checks if you don’t need semantic validation. For production, fix the Cedar policy to pass both schema checks and semantic validation. | 

## Clean up
<a name="policy-getting-started-cleanup"></a>

To remove the resources created in this tutorial, remove both the gateway and the policy engine, then redeploy:

```
agentcore remove gateway --name PolicyGateway
agentcore remove policy-engine --name RefundPolicyEngine
agentcore deploy
```

Removing a gateway does not automatically remove its attached policy engine. You must remove the policy engine separately using `agentcore remove policy-engine`.