

# Use your Step Functions workflows as tools for AI agents
<a name="tutorial-agentcore-gateway"></a>

You can let AI agents run your Step Functions workflows by exposing a state machine as Model Context Protocol (MCP) tools through Amazon Bedrock AgentCore Gateway. An agent connected to the gateway can start executions, check their status and output, read the event history, and stop executions. You don't need to write a Lambda function or define the tools yourself. The gateway creates the tool schemas and calls Step Functions for the agent.

This pattern is useful when a task must run the same steps in the same order every time. The agent decides when to run the workflow and what input to pass. The state machine decides which steps run, so the agent can't skip or reorder them, and the execution history records each step of the workflow.

You control what the agent can do in two ways. Tools that start or list executions are pinned to the state machine you choose, and the agent can't change it. Tools that act on a specific execution take an execution Amazon Resource Name (ARN) from the agent. The AWS Identity and Access Management policy on your gateway service role limits which executions those tools can access. This tutorial scopes that policy to a single state machine.

In this tutorial, you create a simple Standard state machine and a gateway with a Step Functions connector target that points to it. You then make the same MCP calls an agent makes, using `awscurl`, so you can see each request and response. If you already have a Standard state machine, you can skip to [Step 2: Create a service role for the gateway](#agentcore-gateway-step-2) and use its ARN in place of `AgentHelloWorld`. This tutorial uses a Standard workflow because `ListExecutions`, `DescribeExecution`, and `GetExecutionHistory` don't work with Express executions. The resources that you create can incur charges until you delete them in [Step 6: Clean up](#agentcore-gateway-step-6).

**Important**  
The resources in this tutorial can incur charges for Step Functions state transitions and Amazon Bedrock AgentCore Gateway tool calls. For rates, see [Step Functions pricing](https://aws.amazon.com/step-functions/pricing/) and [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/). To avoid ongoing charges, delete the resources when you finish, as described in [Step 6: Clean up](#agentcore-gateway-step-6).

**Note**  
The Step Functions connector exposes ten operations. This tutorial configures six of them: `StartExecution`, `ListExecutions`, `DescribeStateMachine`, `DescribeExecution`, `GetExecutionHistory`, and `StopExecution`. For the full list, including the task-token operations and the differences between Standard and Express workflows, see [AWS Step Functions as Connector Target](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html) in the *Amazon Bedrock AgentCore Developer Guide*.

## Prerequisites
<a name="agentcore-gateway-prerequisites"></a>

Before you begin, make sure that you have the following:
+ The [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), configured with credentials for your account. Steps 3 through 6 use the AWS CLI.
+ A client that can send Signature Version 4-signed HTTP requests to the gateway. This tutorial uses [awscurl](https://github.com/okigan/awscurl), which you can install with `pip install awscurl`. Any MCP client that supports Signature Version 4 works the same way.
+ Permission to create IAM roles, Step Functions state machines, and AgentCore gateways in your account, and the `bedrock-agentcore:InvokeGateway` permission on the gateway that you create in Step 3 for the identity that calls it in Steps 4 and 5.

Create every resource in this tutorial in the same AWS Region. The gateway calls Step Functions in its own Region, so a state machine in a different Region is not reachable through the connector.

## Step 1: Create a state machine
<a name="agentcore-gateway-step-1"></a>

Create a Standard state machine for the agent to run. The following definition has a single `Pass` state that returns a fixed result. Make sure that the console is set to the Region where you will create the gateway in Step 3.

**To create the state machine (console)**

1. Open the [AWS Step Functions console](https://console.aws.amazon.com/states/) and choose **Create state machine**.

1. Choose **Blank**, and then choose **Select**.

1. Choose **Code** and replace the definition with the following.

   ```
   {
     "Comment": "A workflow that an AI agent starts through AgentCore Gateway",
     "StartAt": "Hello",
     "States": {
       "Hello": {
         "Type": "Pass",
         "Result": "Hello from Step Functions",
         "End": true
       }
     }
   }
   ```

1. Choose **Config**. For **State machine name**, enter **AgentHelloWorld**. Keep **Type** as **Standard**.

1. Choose **Create** to create the state machine.

1. Allow Step Functions to create an execution role when prompted. If you use the AWS CLI instead, create the role yourself, as shown in the following procedure.

1. On the state machine details page, note the **ARN**, as shown in the following example.

   ```
   arn:aws:states:{{region}}:123456789012:stateMachine:AgentHelloWorld
   ```

To create the same state machine with the AWS CLI instead, use the following procedure. Unlike the console, the AWS CLI does not create an execution role for you, so create one first. This `Pass`-only workflow calls no other services, so the role needs no permissions policy.

**To create the state machine (AWS CLI)**

1. Create an execution role that Step Functions can assume. Replace the Region and account ID with your own.

   ```
   aws iam create-role \
     --role-name AgentHelloWorldExecutionRole \
     --assume-role-policy-document '{
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Principal": { "Service": "states.amazonaws.com" },
           "Action": "sts:AssumeRole",
           "Condition": {
             "ArnLike": {
               "aws:SourceArn": "{{arn:aws:states:{{region}}:123456789012:stateMachine:*}}"
             },
             "StringEquals": {
               "aws:SourceAccount": "{{123456789012}}"
             }
           }
         }
       ]
     }'
   ```

1. Save the definition shown in the console procedure to a file named `definition.json`, and then create the state machine.

   ```
   aws stepfunctions create-state-machine \
     --name AgentHelloWorld \
     --type STANDARD \
     --definition file://definition.json \
     --role-arn "{{arn:aws:iam::123456789012:role/AgentHelloWorldExecutionRole}}" \
     --region {{{{region}}}}
   ```

   The response contains the `stateMachineArn`. Note it for Steps 2 and 3.

## Step 2: Create a service role for the gateway
<a name="agentcore-gateway-step-2"></a>

The gateway calls Step Functions with a service role. Scope the role to the state machine you created so the agent cannot act on other workflows in your account.

**To create the gateway service role**

1. Open the [IAM console](https://console.aws.amazon.com/iam/home) and choose **Roles**, **Create role**.

1. For **Trusted entity type**, choose **Custom trust policy**, and enter the following. Replace the Region and account ID with your own.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": { "Service": "bedrock-agentcore.amazonaws.com" },
         "Action": "sts:AssumeRole",
         "Condition": {
           "StringEquals": {
             "aws:SourceAccount": "{{123456789012}}"
           },
           "ArnLike": {
             "aws:SourceArn": "{{arn:aws:bedrock-agentcore:{{region}}:123456789012:gateway/step-functions-gateway-*}}"
           }
         }
       }
     ]
   }
   ```

1. Choose **Next**, and then **Next** again without attaching a managed policy.

1. For **Role name**, enter **AgentCoreGatewayToStepFunctions**, and then choose **Create role**.

1. Open the role, choose **Add permissions**, **Create inline policy**, choose **JSON**, and enter the following policy. Replace the Region and account ID with your own.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "StateMachineOperations",
         "Effect": "Allow",
         "Action": [
           "states:StartExecution",
           "states:ListExecutions",
           "states:DescribeStateMachine"
         ],
         "Resource": "{{arn:aws:states:{{region}}:123456789012:stateMachine:AgentHelloWorld}}"
       },
       {
         "Sid": "ExecutionOperations",
         "Effect": "Allow",
         "Action": [
           "states:DescribeExecution",
           "states:GetExecutionHistory",
           "states:StopExecution"
         ],
         "Resource": "{{arn:aws:states:{{region}}:123456789012:execution:AgentHelloWorld:*}}"
       }
     ]
   }
   ```

1. Name the policy **StepFunctionsConnectorAccess**, and then choose **Create policy**.

1. Note the role ARN, as shown in the following example.

   ```
   arn:aws:iam::123456789012:role/AgentCoreGatewayToStepFunctions
   ```

**Note**  
Execution ARNs are a different resource type from state machine ARNs, which is why the policy has two statements.  
If you later expose the task-token operations (`SendTaskSuccess`, `SendTaskFailure`, and `SendTaskHeartbeat`), you must grant them on `"*"`, because IAM doesn't support resource-level permissions for these actions. The task token is then the only control on which tasks the agent can complete, so treat task tokens as secrets and send each one only to the agent that should act on it.  
All targets on a gateway share its service role. If different workflows need different IAM boundaries, use a separate gateway for each.

## Step 3: Create a gateway and add the Step Functions connector target
<a name="agentcore-gateway-step-3"></a>

Create a gateway that accepts requests signed with AWS credentials, and then add a target that uses the `states` connector and pins it to your state machine.

**To create the gateway and target**

1. Create the gateway with the AWS CLI. Replace the role ARN with the one from Step 2.

   ```
   aws bedrock-agentcore-control create-gateway \
     --name "step-functions-gateway" \
     --protocol-type MCP \
     --authorizer-type AWS_IAM \
     --role-arn "{{arn:aws:iam::123456789012:role/AgentCoreGatewayToStepFunctions}}" \
     --region {{{{region}}}}
   ```

   The response includes the `gatewayId` and `gatewayUrl`. Note both.

1. Wait until the gateway status is `READY`. This can take a few minutes. Replace {{GATEWAY\_ID}} with the `gatewayId` from the previous step.

   ```
   aws bedrock-agentcore-control get-gateway \
     --gateway-identifier "{{GATEWAY_ID}}" \
     --query status --output text --region {{{{region}}}}
   ```

1. Add the connector target. The `configurations` list chooses which operations become tools. `StartExecution`, `ListExecutions`, and `DescribeStateMachine` are pinned to your state machine. `DescribeExecution`, `GetExecutionHistory`, and `StopExecution` take an execution ARN from the agent. Replace {{GATEWAY\_ID}} with your gateway ID.

   ```
   aws bedrock-agentcore-control create-gateway-target \
     --gateway-identifier "{{GATEWAY_ID}}" \
     --name "hello" \
     --target-configuration '{
       "mcp": {
         "connector": {
           "source": { "connectorId": "states" },
           "configurations": [
             {
               "name": "StartExecution",
               "parameterValues": {
                 "stateMachineArn": "{{arn:aws:states:{{region}}:123456789012:stateMachine:AgentHelloWorld}}"
               }
             },
             {
               "name": "ListExecutions",
               "parameterValues": {
                 "stateMachineArn": "{{arn:aws:states:{{region}}:123456789012:stateMachine:AgentHelloWorld}}"
               }
             },
             {
               "name": "DescribeStateMachine",
               "parameterValues": {
                 "stateMachineArn": "{{arn:aws:states:{{region}}:123456789012:stateMachine:AgentHelloWorld}}"
               }
             },
             { "name": "DescribeExecution" },
             { "name": "GetExecutionHistory" },
             { "name": "StopExecution" }
           ]
         }
       }
     }' \
     --credential-provider-configurations '[{"credentialProviderType": "GATEWAY_IAM_ROLE"}]' \
     --region {{{{region}}}}
   ```

1. Wait until the target status is `READY`. This can take a few minutes. Replace {{TARGET\_ID}} with the `targetId` from the `create-gateway-target` response.

   ```
   aws bedrock-agentcore-control get-gateway-target \
     --gateway-identifier "{{GATEWAY_ID}}" --target-id "{{TARGET_ID}}" \
     --query status --output text --region {{{{region}}}}
   ```

The gateway now exposes six MCP tools: `hello___StartExecution`, `hello___ListExecutions`, `hello___DescribeStateMachine`, `hello___DescribeExecution`, `hello___GetExecutionHistory`, and `hello___StopExecution`. The gateway prefixes each tool name with the target name.

## Step 4: Start an execution through the gateway
<a name="agentcore-gateway-step-4"></a>

An MCP client calls the gateway with JSON-RPC requests. Because the gateway uses `AWS_IAM` authorization, requests must be signed with Signature Version 4. The following examples use `awscurl`, which signs requests with your AWS CLI credentials. See [Prerequisites](#agentcore-gateway-prerequisites). In each command, replace {{GATEWAY\_URL}} with the `gatewayUrl` from Step 3.

**To start an execution**

1. List the tools the agent sees.

   ```
   awscurl --service bedrock-agentcore --region {{{{region}}}} \
     -X POST "{{GATEWAY_URL}}" \
     -H "Content-Type: application/json" \
     -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
   ```

   The response lists the six tools with their input schemas. Notice that `hello___StartExecution` advertises only `input`: the pinned `stateMachineArn` is hidden from the agent and cannot be overridden.

1. Start an execution.

   ```
   awscurl --service bedrock-agentcore --region {{{{region}}}} \
     -X POST "{{GATEWAY_URL}}" \
     -H "Content-Type: application/json" \
     -d '{
       "jsonrpc": "2.0",
       "id": 2,
       "method": "tools/call",
       "params": {
         "name": "hello___StartExecution",
         "arguments": { "input": "{\"who\": \"agent\"}" }
       }
     }'
   ```

   The tool result contains the Step Functions response with the new execution's ARN.

   ```
   {
     "jsonrpc": "2.0",
     "id": 2,
     "result": {
       "isError": false,
       "content": [
         {
           "type": "text",
           "text": "{\"executionArn\":\"{{arn:aws:states:{{region}}:123456789012:execution:AgentHelloWorld:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}\",\"startDate\":1.7597E9}"
         }
       ]
     }
   }
   ```

   Note the `executionArn` for the next step.

## Step 5: Confirm the result
<a name="agentcore-gateway-step-5"></a>

Use the execution-level tools to check whether the execution succeeded and to read its output.

**To confirm the execution result**

1. Describe the execution. By default, the response contains metadata only. To include the input and output, set `includedData` to `ALL_DATA`. Replace {{EXECUTION\_ARN}} with the `executionArn` from Step 4.

   ```
   awscurl --service bedrock-agentcore --region {{{{region}}}} \
     -X POST "{{GATEWAY_URL}}" \
     -H "Content-Type: application/json" \
     -d '{
       "jsonrpc": "2.0",
       "id": 3,
       "method": "tools/call",
       "params": {
         "name": "hello___DescribeExecution",
         "arguments": {
           "executionArn": "{{EXECUTION_ARN}}",
           "includedData": "ALL_DATA"
         }
       }
     }'
   ```

   For this state machine, `status` is `SUCCEEDED` and `output` is `"Hello from Step Functions"`. If an execution fails, `status` is `FAILED` and the response includes the `error` and `cause` fields from the failing state.

1. Read the event history to see each step the execution took.

   ```
   awscurl --service bedrock-agentcore --region {{{{region}}}} \
     -X POST "{{GATEWAY_URL}}" \
     -H "Content-Type: application/json" \
     -d '{
       "jsonrpc": "2.0",
       "id": 4,
       "method": "tools/call",
       "params": {
         "name": "hello___GetExecutionHistory",
         "arguments": { "executionArn": "{{EXECUTION_ARN}}" }
       }
     }'
   ```

1. List recent executions of the pinned state machine, optionally filtered by status.

   ```
   awscurl --service bedrock-agentcore --region {{{{region}}}} \
     -X POST "{{GATEWAY_URL}}" \
     -H "Content-Type: application/json" \
     -d '{
       "jsonrpc": "2.0",
       "id": 5,
       "method": "tools/call",
       "params": {
         "name": "hello___ListExecutions",
         "arguments": { "statusFilter": "SUCCEEDED" }
       }
     }'
   ```

1. (Optional) Confirm the execution in the [AWS Step Functions console](https://console.aws.amazon.com/states/). Choose **AgentHelloWorld**, and then choose the execution. An execution started by the gateway appears like any other execution, with the gateway's service role as the caller in AWS CloudTrail.

**Note**  
To stop a running execution, call `hello___StopExecution` with the execution ARN. Calling it on an execution that has already finished succeeds but has no effect. The response returns the execution's original stop time. For a long-running workflow, an agent typically calls `StartExecution`, and then polls `DescribeExecution` until `status` is no longer `RUNNING`.

## Step 6: Clean up
<a name="agentcore-gateway-step-6"></a>

To avoid ongoing charges, delete the resources that you created.

**To clean up**

1. Delete the gateway target, and then the gateway.

   ```
   aws bedrock-agentcore-control delete-gateway-target \
     --gateway-identifier "{{GATEWAY_ID}}" --target-id "{{TARGET_ID}}" --region {{{{region}}}}
   aws bedrock-agentcore-control delete-gateway \
     --gateway-identifier "{{GATEWAY_ID}}" --region {{{{region}}}}
   ```

1. In the Step Functions console, delete the `AgentHelloWorld` state machine.

1. In the IAM console, delete the `AgentCoreGatewayToStepFunctions` role and the state machine's execution role (the role that Step Functions created for you, or `AgentHelloWorldExecutionRole` if you used the AWS CLI).

## Related resources
<a name="agentcore-gateway-related"></a>
+ [AWS Step Functions as Connector Target](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-target-connector-step-functions.html) in the *Amazon Bedrock AgentCore Developer Guide* – all ten operations, which parameters can be pinned, Standard and Express workflow constraints, and tool schemas.
+ [Add a Connector target with AWS Step Functions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-add-target-api-target-config.html#gateway-add-target-api-connector-step-functions) – setup with Boto3, the AWS CLI, and the AgentCore CLI, and the full service role policy including task-token operations.
+ [Create an agent that uses your AgentCore gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-agent-integration.html) – connect an agent framework such as Strands Agents or LangGraph to the gateway.
+ [Invoke Amazon Bedrock AgentCore harness with Step Functions](connect-bedrockagentcore.md) – the reverse direction: call an agent from a Step Functions Task state.