# Creating an AgentCore Browser

You can create a Browser Tool using the Amazon Bedrock AgentCore console, AWS CLI, or AWS
SDK.

Console

###### To create a Browser Tool using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. Choose **Create browser tool**.
4. Provide a unique **Tool name** and optional
   **Description**.
5. Under **Network settings**, choose **Public
   network** which allows access to public internet resources.
6. Under **Session recording**, you can enable recording of
   browser sessions to an S3 bucket for later review.
7. Under **Permissions**, specify an IAM execution role that
   defines what AWS resources the Browser Tool can access.
8. Choose **Create**.

AWS CLI
To create a Browser Tool using the AWS CLI, use the `create-browser`
command:

```

aws bedrock-agentcore-control create-browser \
  --region <Region> \
  --name "my-browser" \
  --description "My browser for web interaction" \
  --network-configuration '{
    "networkMode": "PUBLIC"
  }' \
  --recording '{
    "enabled": true,
    "s3Location": {
      "bucket": "my-bucket-name",
      "prefix": "sessionreplay"
    }
  }' \
  --execution-role-arn "arn:aws:iam::123456789012:role/my-execution-role"

```

Boto3
To create a Browser Tool using the AWS SDK for Python (Boto3), use the
`create_browser` method:

###### Request Syntax

The following shows the request syntax:

```

response = cp_client.create_browser(
    name="my_custom_browser",
    description="Test browser for development",
    networkConfiguration={
        "networkMode": "PUBLIC"
    },
    executionRoleArn="arn:aws:iam::123456789012:role/Sessionreplay",
    clientToken=str(uuid.uuid4()),
    recording={
    "enabled": True,
    "s3Location": {
        "bucket": "session-record-123456789012",
        "prefix": "replay-data"
      }
    }
)

```

API
To create a new browser instance using the API, use the following call:

```

# Using awscurl
awscurl -X PUT \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region> \
  -d '{
    "name": "test_browser_1",
    "description": "Test sandbox for development",
    "networkConfiguration": {
      "networkMode": "PUBLIC"
    },
    "recording": {
      "enabled": true,
      "s3Location": {
        "bucket": "<your-bucket-name>",
        "prefix": "sessionreplay"
      }
    },
    "executionRoleArn": "arn:aws:iam::123456789012:role/my-execution-role"
  }'

```
