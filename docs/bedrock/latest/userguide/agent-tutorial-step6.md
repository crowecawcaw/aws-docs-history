# Step 6: Clean up resources

When you're done with your Amazon Bedrock agent, you should clean up the resources to avoid
incurring unnecessary charges. In this final procedure, you'll systematically delete all
the AWS resources created during this tutorial, including the Bedrock agent, Lambda
function, and associated \*IAM roles. This cleanup process is important for cost
management, as it prevents ongoing charges for resources you're no longer using. The
procedure is organized into three parts: deleting the agent, removing the Lambda
function, and cleaning up the IAM roles that were created to support these
services.

###### Topics

- [Delete the agent](#agent-tutorial-step6-console-agent "#agent-tutorial-step6-console-agent")
- [Delete the Lambda
  function](#agent-tutorial-step6-console-lambda "#agent-tutorial-step6-console-lambda")
- [Delete the IAM roles](#agent-tutorial-step6-console-iam "#agent-tutorial-step6-console-iam")

## Delete the agent

###### Delete the agent

1. In the Amazon Bedrock console, open the agent that you created in [Step 2: Create an Amazon Bedrock agent](agent-tutorial-step2.md "agent-tutorial-step2.md")
2. Select the agent you created.
3. Choose **Delete**.
4. Confirm the deletion.

## Delete the Lambda

function

###### Delete the Lambda function

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Select the Lambda function you created.
3. Choose **Actions**, then
   **Delete**.
4. Confirm the deletion.

## Delete the IAM roles

###### Delete the IAM roles

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles**.
3. Select the agent service role that you created.
4. Choose **Delete**.
5. Confirm the deletion.
6. Repeat for the Lambda execution role.
