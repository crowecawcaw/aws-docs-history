# Deleting an AgentCore Browser

When you no longer need a browser tool, you can delete it to free up resources. Before
deleting a browser tool, make sure to stop all active sessions associated with it.

Console

###### To delete a Browser tool using the console

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home#](https://console.aws.amazon.com/bedrock-agentcore/home# "https://console.aws.amazon.com/bedrock-agentcore/home#").
2. Navigate to **Built-in tools** and select your browser
   tool.
3. Choose **Delete** from the **Actions**
   menu.
4. Confirm the deletion by typing the browser tool name in the confirmation
   dialog.
5. Choose **Delete**.

###### Note

You cannot delete a browser tool that has active sessions. Stop all sessions
before attempting to delete the tool.

AWS CLI
To delete a Browser tool using the AWS CLI, use the `delete-browser`
command:

```

aws bedrock-agentcore-control delete-browser \
  --region <Region> \
  --browser-id "<your-browser-id>"

```

Boto3
To delete a Browser tool using the AWS SDK for Python (Boto3), use the
`delete_browser` method:

###### Request Syntax

The following shows the request syntax:

```

response = cp_client.delete_browser(
    browserId="<your-browser-id>"
    )

```

API
To delete a browser tool using the API, use the following call:

```

# Using awscurl
awscurl -X DELETE \
  "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers/<your-browser-id>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  --service bedrock-agentcore-control \
  --region <Region>

```
