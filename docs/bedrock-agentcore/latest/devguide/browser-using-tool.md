

# Using Browser Tool
<a name="browser-using-tool"></a>

## Creating an AgentCore Browser
<a name="browser-create"></a>

You can create a Browser Tool using the Amazon Bedrock AgentCore console, AWS CLI, or AWS SDK.

**Example**  

1.  **To create a Browser Tool using the console** 

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home\#](https://console.aws.amazon.com/bedrock-agentcore/home#).

1. In the navigation pane, choose **Built-in tools**.

1. Choose **Create browser tool**.

1. Provide a unique **Tool name** and optional **Description**.

1. Under **Network settings** , choose **Public network** which allows access to public internet resources.

1. Under **Session recording** , you can enable recording of browser sessions to an S3 bucket for later review.

1. Under **Permissions** , specify an IAM execution role that defines what AWS resources the Browser Tool can access.

1. Choose **Create**.

1. To create a Browser Tool using the AWS CLI, use the `create-browser` command:

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

1. To create a Browser Tool using the AWS SDK for Python (Boto3), use the `create_browser` method:

    **Request Syntax** 

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

1. To create a new browser instance using the API, use the following call:

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

## Get AgentCore Browser tool
<a name="browser-get"></a>

You can get information about the Browser tool in your account and view their details, status, and configurations.

**Example**  

1.  **To get information about the Browser tool using the console** 

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home\#](https://console.aws.amazon.com/bedrock-agentcore/home#).

1. In the navigation pane, choose **Built-in tools**.

1. The browser tools are listed in the **Browser tools** section.

1. You can choose a tool that you created to view it’s details such as name, ID, status, and creation date for each browser tool.

1. To get information about a Browser tool using the AWS CLI, use the `get-browser` command:

   ```
   aws bedrock-agentcore-control get-browser \
     --region <Region> \
     --browser-id "<your-browser-id>"
   ```

1. To get information about the Browser tool using the AWS SDK for Python (Boto3), use the `get_browser` method:

    **Request Syntax** 

   The following shows the request syntax:

   ```
   response = cp_client.get_browser(
       browserId="<your-browser-id>"
   )
   ```

1. To get the browser tool using the API, use the following call:

   ```
   # Using awscurl
   awscurl -X GET \
     "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers/<your-browser-id>" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     --service bedrock-agentcore \
     --region <Region>
   ```

## Listing AgentCore Browser tools
<a name="browser-list"></a>

You can list all browser tools in your account to view their details, status, and configurations.

**Example**  

1.  **To list browser tools using the console** 

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home\#](https://console.aws.amazon.com/bedrock-agentcore/home#).

1. In the navigation pane, choose **Built-in tools**.

1. The browser tools are listed in the **Browser tools** section.

1. You can view details such as name, ID, status, and creation date for each browser tool.

1. To list browser tools using the AWS CLI, use the `list-browsers` command:

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

1. To list browser tools using the AWS SDK for Python (Boto3), use the `list_browsers` method:

    **Request Syntax** 

   The following shows the request syntax:

   ```
   response = cp_client.list_browsers(type="CUSTOM")
   ```

1. To list browser tools using the API, use the following call:

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

## Deleting an AgentCore Browser
<a name="browser-delete"></a>

When you no longer need a browser tool, you can delete it to free up resources. Before deleting a browser tool, make sure to stop all active sessions associated with it.

**Example**  

1.  **To delete a Browser tool using the console** 

1. Open the AgentCore console at [https://console.aws.amazon.com/bedrock-agentcore/home\#](https://console.aws.amazon.com/bedrock-agentcore/home#).

1. Navigate to **Built-in tools** and select your browser tool.

1. Choose **Delete** from the **Actions** menu.

1. Confirm the deletion by typing the browser tool name in the confirmation dialog.

1. Choose **Delete**.
**Note**  
You cannot delete a browser tool that has active sessions. Stop all sessions before attempting to delete the tool.

1. To delete a Browser tool using the AWS CLI, use the `delete-browser` command:

   ```
   aws bedrock-agentcore-control delete-browser \
     --region <Region> \
     --browser-id "<your-browser-id>"
   ```

1. To delete a Browser tool using the AWS SDK for Python (Boto3), use the `delete_browser` method:

    **Request Syntax** 

   The following shows the request syntax:

   ```
   response = cp_client.delete_browser(
       browserId="<your-browser-id>"
       )
   ```

1. To delete a browser tool using the API, use the following call:

   ```
   # Using awscurl
   awscurl -X DELETE \
     "https://bedrock-agentcore-control.<Region>.amazonaws.com/browsers/<your-browser-id>" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     --service bedrock-agentcore-control \
     --region <Region>
   ```