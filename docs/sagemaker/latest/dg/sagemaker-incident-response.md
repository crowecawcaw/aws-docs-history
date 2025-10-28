# Logging and Monitoring

You can monitor Amazon SageMaker AI using Amazon CloudWatch, which collects raw data and processes it into
readable, near real-time metrics. These statistics are kept for 15 months, so that you can
access historical information and gain a better perspective on how your web application or
service is performing. You can also set alarms that watch for certain thresholds and send
notifications or take actions when those thresholds are met. For more information, see [Amazon SageMaker AI metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

Amazon CloudWatch Logs enables you to monitor, store, and access your log files from Amazon EC2 instances,
AWS CloudTrail, and other sources. You can collect and track metrics, create customized
dashboards, and set alarms that notify you or take actions when a specified metric reaches a
threshold that you specify. CloudWatch Logs can monitor information in the log files and notify you
when certain thresholds are met. You can also archive your log data in highly durable
storage. For more information, see [CloudWatch Logs for Amazon SageMaker AI](logging-cloudwatch.md "logging-cloudwatch.md").

AWS CloudTrail provides a record of actions taken by a user, role, or an AWS service in SageMaker AI.
Using the information collected by CloudTrail, you can determine the request that was made to
SageMaker AI, the IP address from which the request was made, who made the request, when it was
made, and additional details. For more information, [Logging Amazon SageMaker AI API calls using
AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

[Amazon GuardDuty](../../../guardduty/latest/ug/what-is-guardduty.md "../../../guardduty/latest/ug/what-is-guardduty.md") is a threat detection service that continuously monitors and analyzes
your CloudTrail management and event logs to identify potential security issues. When you enable
GuardDuty for an AWS account, it automatically starts analyzing CloudTrail logs to detect suspicious
activity in SageMaker APIs. For example, GuardDuty will detect suspicious activity when a user
abnormally creates a new pre-signed or blank notebook instance that can later be used for
malicious actions. GuardDuty's unique credential exfiltration detection can help a customer
identify that the AWS credentials associated with the Amazon EC2 instance were exfiltrated, and
then used to call SageMaker APIs from another AWS account.

You can create rules in Amazon CloudWatch Events to react to status changes in status in a SageMaker training,
hyperperparameter tuning, or batch transform job. For more information, see [Events that Amazon SageMaker AI sends to
Amazon EventBridge](automating-sagemaker-with-eventbridge.md "automating-sagemaker-with-eventbridge.md").

###### Note

CloudTrail does not monitor calls to [`runtime_InvokeEndpoint`](../APIReference/API_runtime_InvokeEndpoint.md "../APIReference/API_runtime_InvokeEndpoint.md").
