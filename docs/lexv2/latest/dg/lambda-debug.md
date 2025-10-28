# Debugging a Lambda function using CloudWatch Logs logs

[Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md") is a tool for
tracking API calls and metrics that you can use to help debug your Lambda functions. When you test your bot in the console
or with API calls, CloudWatch logs each step of the conversation. If you use a print function in your Lambda code, CloudWatch displays it as well.

###### To view CloudWatch logs for your Lambda function

1. Sign in to the AWS Management Console and open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Under the **Logs** menu in the left side bar, select **Log groups**.
3. Select your Lambda function log group, which should be of the format `/aws/lambda/`function-name``.
4. The list of **Log streams** contains a log for each session with a bot. Choose a log stream to view it.
5. In the list of **Log events**, select the right arrow next to the **Timestamp** to expand the details for that event. Anything you print from your Lambda code will appear as a log event. Use this information to debug your code.
6. After you debug your code, remember to **Deploy** the Lambda function and, if you are using the console, to reload the **Test** window before re-testing the bot's behavior.
