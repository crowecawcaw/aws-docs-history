

# Get started with AgentCore Code Interpreter
<a name="code-interpreter-getting-started"></a>

AgentCore Code Interpreter enables your agents to execute Python code in a secure, managed environment. The agent can perform calculations, analyze data, generate visualizations, and validate answers through code execution.

This page covers the prerequisites and provides two approaches to get started:
+  **Using AWS Strands** - A high-level agent framework that simplifies building AI agents with built-in tool integration, conversation management, and automatic session handling.
+  **Direct usage** - SDK and Boto3 approaches that provide more control over session management and code execution for custom implementations.

**Topics**
+ [Prerequisites](#code-interpreter-prerequisites)
+ [Configuring your credentials](#code-interpreter-credentials-config)
+ [Using AgentCore Code Interpreter via AWS Strands](code-interpreter-using-strands.md)
+ [Using AgentCore Code Interpreter directly](code-interpreter-using-directly.md)

## Prerequisites
<a name="code-interpreter-prerequisites"></a>

Before you start, ensure you have:
+  AWS account with credentials configured. See [Configuring your credentials](#code-interpreter-credentials-config).
+ Python 3.10\+ installed
+ Boto3 installed. See [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html).
+ IAM execution role with the required permissions. See [Configuring your credentials](#code-interpreter-credentials-config).
+ Model access: Anthropic Claude Sonnet 4.0 [enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) in the Amazon Bedrock console. For information about using a different model with the Strands Agents see the *Model Providers* section in the [Strands Agents SDK documentation](https://strandsagents.com/latest/documentation/docs/).
+  AWS Region where Amazon Bedrock AgentCore is available. See [Supported AWS Regions](agentcore-regions.md).

## Configuring your credentials
<a name="code-interpreter-credentials-config"></a>

Perform the following steps to configure your AWS credentials and attach the required permissions.

1.  **Verify your AWS credentials** 

   Confirm your AWS credentials are configured:

   ```
   aws sts get-caller-identity
   ```
**Note**  
Take note of the user or credentials returned here, as you’ll be using it when attaching the required permissions.

   If this command fails, configure your credentials. For more information, see [Configuration and credential file settings in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

1.  **Attach required permissions** 

   Your IAM user or role needs permissions to use AgentCore Code Interpreter. Attach this policy to your IAM identity:
**Note**  
Replace `<region>` with your chosen region (for example, `us-west-2` ) and `<account_id>` with your AWS account ID in the policy below:

   ```
   {
       "Version":"2012-10-17",	
       "Statement": [
           {
               "Sid": "BedrockAgentCoreCodeInterpreterFullAccess",
               "Effect": "Allow",
               "Action": [
                   "bedrock-agentcore:CreateCodeInterpreter",
                   "bedrock-agentcore:StartCodeInterpreterSession",
                   "bedrock-agentcore:InvokeCodeInterpreter",
                   "bedrock-agentcore:StopCodeInterpreterSession",
                   "bedrock-agentcore:DeleteCodeInterpreter",
                   "bedrock-agentcore:ListCodeInterpreters",
                   "bedrock-agentcore:GetCodeInterpreter",
                   "bedrock-agentcore:GetCodeInterpreterSession",
                   "bedrock-agentcore:ListCodeInterpreterSessions"
               ],
               "Resource": "arn:aws:bedrock-agentcore:<region>:++<account_id>++:code-interpreter/*"
           }
       ]
   }
   ```

 **To attach this policy** 

Follow these steps:

1. Go to the IAM console.

1. Find your user or role from the response returned for the `get-caller-identity` API operation.

1. Choose **Add permissions** and then choose **Create inline policy** 

1. Switch to JSON view and paste the policy above

1. Name it `AgentCoreCodeInterpreterAccess` and save

**Note**  
If you’re deploying agents to Amazon Bedrock AgentCore Runtime, you’ll also need to create an IAM execution role with a service trust policy. For more information, see [Get started with AgentCore Runtime](runtime-getting-started.md).

The following sections show you how to use the Amazon Bedrock AgentCore Code Interpreter with and without the agent framework. Using the Code Interpreter directly without an agent framework is especially useful when you want to execute specific code snippets programmatically.