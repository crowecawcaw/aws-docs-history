# Access CloudWatch logs for Debugger rules and training

jobs

You can use the training and Debugger rule job status in the CloudWatch logs to take
further actions when there are training issues. The following procedure shows how to
access the related CloudWatch logs. For more information about monitoring training jobs
using CloudWatch, see [Monitor
Amazon SageMaker AI](monitoring-overview.md "monitoring-overview.md").

###### To access training job logs and Debugger rule job logs

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane under the **Log** node,
   choose **Log Groups**.
3. In the log groups list, do the following:
   - Choose **/aws/sagemaker/TrainingJobs** for
     training job logs.
   - Choose **/aws/sagemaker/ProcessingJobs** for
     Debugger rule job logs.
