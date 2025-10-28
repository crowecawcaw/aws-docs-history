# Listing AgentCore Code Interpreter tools

You can view a list of all your Code Interpreter tools to manage and monitor
them.

Console

###### To list code interpreters using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. The console displays a list of all your Code Interpreter tools, including
   their names, IDs, creation dates, and status.
4. You can use the search box to filter the list by name or other
   attributes.
5. Select a Code Interpreter to view its details, including active sessions and
   configuration settings.

AWS CLI
To list Code Interpreters using the AWS CLI, use the
`list-code-interpreters` command:

```
aws bedrock-agentcore list-code-interpreters \
  --region <Region> \
  --max-results 10

```

You can use the `--next-token` parameter for pagination if you have
more than the maximum results:

```
aws bedrock-agentcore list-code-interpreters \
  --region <Region> \
  --max-results 10 \
  --next-token "<your-pagination-token>"

```

Boto3
To list Code Interpreters using the AWS SDK for Python, use the
`list_code_interpreters` method:

```
import boto3

# Initialize the boto3 client
cp_client = boto3.client(
    'bedrock-agentcore-control',
    region_name="<Region>",
    endpoint_url="https://bedrock-agentcore-control.<Region>.amazonaws.com"
)

# List Code Interpreters
response = cp_client.list_code_interpreters()

# Print the Code Interpreters
for interpreter in response.get('codeInterpreterSummaries', []):
    print(f"Name: {interpreter.get('name')}")
    print(f"ID: {interpreter.get('codeInterpreterId')}")
    print(f"Creation Time: {interpreter.get('createdAt')}")
    print(f"Status: {interpreter.get('status')}")
    print("---")

# If there are more results, get the next page using the next_token
if 'nextToken' in response:
    next_page = cp_client.list_code_interpreters(
        nextToken=response['nextToken']
    )
    # Process next_page...

```

API
To list Code Interpreter instances using the API, use the following call:

###### Note

For pagination, include the nextToken parameter.

```
# Using awscurl
awscurl -X POST "https://bedrock-agentcore-control.<Region>.amazonaws.com/code-interpreters" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```
