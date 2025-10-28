# Tutorial: Test your configuration

You can now test your EventBridge configuration by submitting a job to your job queue. If everything is configured
properly, your Lambda function is triggered and it writes the event data to a CloudWatch Logs log stream for the
function.

###### To test your configuration

1. Open the AWS Batch console at
   [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. Submit a new AWS Batch job. For more information, see [Tutorial: submit a job](submit_job.md "submit_job.md").
3. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
4. On the navigation pane, choose **Logs** and select the log group for your Lambda function
   (for example, **/aws/lambda/**`my-function`).
5. Select a log stream to view the event data.
