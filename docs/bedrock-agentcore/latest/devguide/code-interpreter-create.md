# Creating an AgentCore Code Interpreter

You can create a Code Interpreter using the Amazon Bedrock AgentCore console, AWS CLI, or AWS
SDK.

Console

###### To create a Code Interpreter using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. Choose **Create Code Interpreter tool**.
4. Provide a unique **Tool name** and optional
   **Description**.
5. Under **Network settings**, choose one of the following
   options:
   - **Sandbox** - Environment with limited external
     network access
   - **Public network** - Allows access to public internet
     resources

6. Under **Permissions**, specify an IAM runtime role that
   defines what AWS resources the Code Interpreter can access.
7. Choose **Create**.

After creating a Code Interpreter tool, the console displays important details
about the tool:

Tool Resource ARN

The Amazon Resource Name (ARN) that uniquely identifies the Code
Interpreter tool resource (e.g.,
arn:aws:bedrock-agentcore:<Region>:123456789012:code-interpreter/code-interpreter-custom).

Code Interpreter Tool ID

The unique identifier for the Code Interpreter tool, used in API calls
(e.g., code-interpreter-custom-abc123).

IAM Role

The IAM role that the Code Interpreter assumes when executing code,
determining what AWS resources it can access.

Network Mode

The network configuration for the Code Interpreter (Sandbox or
Public).

Creation Time

The date and time when the Code Interpreter tool was created.

AWS CLI
To create a Code Interpreter using the AWS CLI, use the
`create-code-interpreter` command:

```
aws bedrock-agentcore create-code-interpreter \
  --region <Region> \
  --name "my-code-interpreter" \
  --description "My Code Interpreter for data analysis" \
  --network-configuration '{
    "networkMode": "PUBLIC"
  }' \
  --execution-role-arn "arn:aws:iam::123456789012:role/my-execution-role"

```

Boto3
To create a Code Interpreter using the AWS SDK for Python, use the
`create_code_interpreter` method:

```
import boto3

# Initialize the boto3 client
cp_client = boto3.client(
    'bedrock-agentcore-control',
    region_name="<Region>",
    endpoint_url="https://bedrock-agentcore-control.<Region>.amazonaws.com"
)

# Create a Code Interpreter
response = cp_client.create_code_interpreter(
    name="myTestSandbox1",
    description="Test code sandbox for development",
    executionRoleArn="arn:aws:iam::123456789012:role/my-execution-role",
    networkConfiguration={
        "networkMode": "PUBLIC"
    }
)

# Print the Code Interpreter ID
code_interpreter_id = response["codeInterpreterId"]
print(f"Code Interpreter ID: {code_interpreter_id}")

```

API
To create a new Code Interpreter instance using the API, use the following
call:

```
# Using awscurl
awscurl -X PUT "https://bedrock-agentcore-control.<Region>.amazonaws.com/code-interpreters" \
-H "Content-Type: application/json" \
--region <Region> \
--service bedrock-agentcore \
-d '{
    "name": "codeinterpreter'$(date +%m%d%H%M%S)'",
    "description": "Test code sandbox for development",
    "executionRoleArn": "'${ROLE_ARN}'",
    "networkConfiguration": {
        "networkMode": "PUBLIC"
    }
}'

```
