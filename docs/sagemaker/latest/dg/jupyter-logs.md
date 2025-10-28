# Monitor Jupyter Logs in Amazon CloudWatch Logs

Jupyter logs include important information such as events, metrics, and health
information that provide actionable insights when running Amazon SageMaker notebooks. By
importing Jupyter logs into CloudWatch Logs, customers can use CloudWatch Logs to detect anomalous
behaviors, set alarms, and discover insights to keep the SageMaker AI notebooks running more
smoothly. You can access the logs even when the Amazon EC2 instance that hosts the notebook
is unresponsive, and use the logs to troubleshoot the unresponsive notebook. Sensitive
information such as AWS account IDs, secret keys, and authentication tokens in
presigned URLs are removed so that customers can share logs without leaking private
information.

###### To view Jupyter logs for a notebook instance:

1. Sign in to the AWS Management Console and open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Choose **Notebook instances**.
3. In the list of notebook instances, choose the notebook instance for which you
   want to view Jupyter logs by selecting the Notebook instance
   **Name**.

This will bring you to the details page for that notebook instance. 4. Under **Monitor** on the notebook instance details page,
choose **View logs**. 5. In the CloudWatch console, choose the log stream for your notebook instance. Its
name is in the form
``NotebookInstanceName`/jupyter.log`.
For more information about monitoring CloudWatch logs for SageMaker AI, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md "logging-cloudwatch.md").
