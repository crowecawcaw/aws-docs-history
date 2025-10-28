# Deleting an AgentCore Code Interpreter

When you no longer need a Code Interpreter, you can delete it to free up resources and
avoid unnecessary charges.

###### Important

Deleting a Code Interpreter permanently removes it and all its configuration. This
action cannot be undone. Make sure all active sessions are stopped before deleting a
Code Interpreter.

Console

###### To delete a Code Interpreter using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. From the list of code interpreter tools, select the tool you want to
   delete.
4. Choose **Delete**.
5. In the confirmation dialog, enter the name of the code interpreter to
   confirm deletion.
6. Choose **Delete** to permanently delete the Code
   Interpreter.

AWS CLI
To delete a Code Interpreter using the AWS CLI, use the
`delete-code-interpreter` command:

```
aws bedrock-agentcore delete-code-interpreter \
  --region <Region> \
  --code-interpreter-id "<your-code-interpreter-id>"

```

Boto3
To delete a Code Interpreter using the AWS SDK for Python, use the
`delete_code_interpreter` method:

```
import boto3

# Initialize the boto3 client
cp_client = boto3.client(
    'bedrock-agentcore-control',
    region_name="<Region>",
    endpoint_url="https://bedrock-agentcore-control.<Region>.amazonaws.com"
)

# Delete a Code Interpreter
response = cp_client.delete_code_interpreter(
    codeInterpreterId="<your-code-interpreter-id>"
)

print("Code Interpreter deleted successfully")

```

API
To delete a Code Interpreter instance using the API, use the following
call:

```
# Using awscurl
awscurl -X DELETE "https://bedrock-agentcore-control.<Region>.amazonaws.com/code-interpreters/<your-code-interpreter-id>" \
-H "Accept: application/json" \
--service bedrock-agentcore \
--region <Region>

```
