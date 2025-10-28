# Get AgentCore Browser tool

You can get information about the Browser tool in your account and view their details,
status, and configurations.

Console

###### To get information about the Browser tool using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. In the navigation pane, choose **Built-in tools**.
3. The browser tools are listed in the **Browser tools**
   section.
4. You can choose a tool that you created to view it's details such as name,
   ID, status, and creation date for each browser tool.

AWS CLI
To get information about a Browser tool using the AWS CLI, use the
`get-browser` command:

```

aws bedrock-agentcore-control get-browser \
  --region <Region> \
  --browser-id "<your-browser-id>"

```

Boto3
To get information about the Browser tool using the AWS SDK for Python
(Boto3), use the `get_browser` method:

###### Request Syntax

The following shows the request syntax:

```

response = cp_client.get_browser(
    browserId="<your-browser-id>"
)

```

API
To get the browser tool using the API, use the following call:

```

# Using awscurl
awscurl -X GET \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers/<your-browser-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore \
  --region <Region>

```
