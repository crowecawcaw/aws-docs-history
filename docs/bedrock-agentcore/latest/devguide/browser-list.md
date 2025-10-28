# Listing AgentCore Browser tools

You can list all browser tools in your account to view their details, status, and
configurations.

Console

###### To list browser tools using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. The browser tools are listed in the **Browser tools**
   section.
4. You can view details such as name, ID, status, and creation date for each
   browser tool.

AWS CLI
To list browser tools using the AWS CLI, use the `list-browsers`
command:

```

aws bedrock-agentcore-control list-browsers \
  --region <Region>

```

You can filter the results by type:

```

aws bedrock-agentcore-control list-browsers \
  --region <Region> \
  --type SYSTEM

```

You can also limit the number of results and use pagination:

```

aws bedrock-agentcore-control list-browsers \
  --region <Region> \
  --max-results 10 \
  --next-token "<your-pagination-token>"

```

Boto3
To list browser tools using the AWS SDK for Python (Boto3), use the
`list_browsers` method:

###### Request Syntax

The following shows the request syntax:

```

response = cp_client.list_browsers(type="CUSTOM")

```

API
To list browser tools using the API, use the following call:

```

# Using awscurl
awscurl -X POST \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```

You can filter the results by type:

```

awscurl -X POST \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers?type=SYSTEM" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```

You can also limit the number of results and use pagination:

```

awscurl -X POST \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers?maxResults=1&nextToken=<your-pagination-token>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```
