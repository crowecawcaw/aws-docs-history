# Step 1: Create a Lambda function

First, create a Lambda function that your agent will invoke to perform actions. In this
procedure, you'll create a Python Lambda function that returns the current date and time
when invoked. You'll set up the function with basic permissions, add the necessary code
to handle requests from your Amazon Bedrock agent, and deploy the function so it's ready to be
connected to your agent.

For more information, see [Create your first Lambda function](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md")
in the _AWS Lambda developer guide_.

###### Create a Lambda function

1. Sign in to the AWS Management Console and open the Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose **Create function**.
3. Select **Author from scratch**.
4. In the **Basic information** section:
   - For **Function name**, enter a function name (for
     example, `DateTimeFunction`). Note the name of the function,
     you'll need it in step 15 of [Step 2: Create an Amazon Bedrock agent](agent-tutorial-step2.md "agent-tutorial-step2.md").
   - For **Runtime**, select **Python
     3.9** (or your preferred version).
   - For **Architecture**, leave unchanged.
   - In **Permissions**, select **Change default
     execution role** and then select **Create a new
     role with basic Lambda permissions**.

5. Choose **Create function**.
6. In **Function overview**, under **Function
   ARN**, note the Amazon Resource Name (ARN) for the function. You
   need it for step 24 of [Step 2: Create an Amazon Bedrock agent](agent-tutorial-step2.md "agent-tutorial-step2.md").
7. In the **Code** tab, replace the existing code with the
   following:

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
import datetime
import json


def lambda_handler(event, context):
    now = datetime.datetime.now()

    response = {"date": now.strftime("%Y-%m-%d"), "time": now.strftime("%H:%M:%S")}

    response_body = {"application/json": {"body": json.dumps(response)}}

    action_response = {
        "actionGroup": event["actionGroup"],
        "apiPath": event["apiPath"],
        "httpMethod": event["httpMethod"],
        "httpStatusCode": 200,
        "responseBody": response_body,
    }

    session_attributes = event["sessionAttributes"]
    prompt_session_attributes = event["promptSessionAttributes"]

    return {
        "messageVersion": "1.0",
        "response": action_response,
        "sessionAttributes": session_attributes,
        "promptSessionAttributes": prompt_session_attributes,
    }
```

8. Choose **Deploy** to deploy your function.
9. Choose the **Configuration** tab.
10. Choose **Permissions**.
11. Under **Resource-based policy statements**, choose
    **Add permissions**.
12. In **Edit policy statement**, do the following:
    1. Choose **AWS service**
    2. In **Service** select **Other**.
    3. For **Statement ID**, enter a unique identifier (for
       example, `AllowBedrockInvocation`).
    4. For **Principal**, enter
       `bedrock.amazonaws.com`.
    5. For **Source ARN**, enter
       `arn:aws:bedrock:`region`:`AWS account ID`:agent/*`

    Replace `region` with AWS Region that you are using, such as `us-east-1`. Replace
    `AWS account ID` your AWS account Id. 6. For **Action**, select
    `lambda:InvokeFunction`.

13. Choose **Save**.
