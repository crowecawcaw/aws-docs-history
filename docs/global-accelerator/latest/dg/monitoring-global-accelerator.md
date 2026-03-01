# Logging and monitoring in AWS Global Accelerator

You can use Amazon CloudWatch, flow logs, and AWS CloudTrail to monitor your accelerator in AWS Global Accelerator. For example, you
can troubleshoot issues with your listeners and endpoints, analyze traffic patterns, and get information
that's required for audits.

These logging and monitoring methods can have some overlap. The following are typical uses for each method:

- **CloudWatch metrics** provide real time information, without additional setup, that
  can help you troubleshoot setup. You can use the Global Accelerator RST metrics to help you troubleshoot issues with TCP resets.
  You can also create alarms to alert you, for example, when there are production issues.
- **Flow logs** provide detailed information about traffic coming into an accelerator
  and going back to clients. Flow logs are useful for troubleshooting reachability issues and for providing information
  for comprehensive audits. (Note that flow logs require setup and use Amazon S3 storage.)
- **CloudTrail** automatically tracks actions that you take that call Global Accelerator APIs, which can be
  useful for audits, for example.

###### Note

You must view CloudWatch metrics and logs for Global Accelerator in the US West (Oregon) Region, both in the
console or when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region
for your command by including the following parameter: `--region us-west-2`.

###### Topics

- [Using Amazon CloudWatch with AWS Global Accelerator](cloudwatch-monitoring.md "cloudwatch-monitoring.md")
- [Troubleshooting Global Accelerator TCP reset issues](cloudwatch-metrics-globalaccelerator-tcp-resets.md "cloudwatch-metrics-globalaccelerator-tcp-resets.md")
- [Configuring and using flow logs in AWS Global Accelerator](monitoring-global-accelerator.md "monitoring-global-accelerator.md")
- [Using AWS CloudTrail to log AWS Global Accelerator API calls](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
