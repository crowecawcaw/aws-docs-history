End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Monitoring AWS Elemental MediaStore with

Amazon CloudWatch

You can monitor AWS Elemental MediaStore using CloudWatch, which collects raw data and processes it
into readable metrics. CloudWatch keeps statistics for 15 months so that you can access
historical information and gain a better perspective on how your web application or
service is performing. You can also set alarms that watch for certain thresholds, and
send notifications or take actions when those thresholds are met. For more information,
see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

AWS provides the following monitoring tools to watch MediaStore, report when
something is wrong, and take automatic actions when appropriate:

- Amazon CloudWatch Logs allows you to monitor, store, and access your log files from AWS
  services such as AWS Elemental MediaStore. You can use CloudWatch Logs to monitor applications
  and systems using log data. For example, CloudWatch Logs can track the number of errors
  that occur in your application logs and send you a notification whenever the
  rate of errors exceeds a threshold that you specify. CloudWatch Logs uses your log data
  for monitoring, so no code changes are required. For example, you can monitor
  application logs for specific literal terms (such as "ValidationException") or
  count the number of `PutObject` requests that were made during a
  certain time period. When the term that you are searching for is found, CloudWatch Logs
  reports the data to a CloudWatch metric that you specify. Log data is encrypted while
  in transit and while it is at rest.
- Amazon CloudWatch Events delivers system events that describe changes in AWS resources,
  such as MediaStore objects. Typically, AWS services deliver event
  notifications to CloudWatch Events in seconds but can sometimes take a minute or longer. You
  can set up rules to match events (such as a `DeleteObject` request)
  and route them to one or more target functions or streams. CloudWatch Events becomes aware
  of operational changes as they occur. In addition, CloudWatch Events responds to these
  operational changes and takes corrective action as necessary, by sending
  messages to respond to the environment, activating functions, making changes,
  and capturing state information.
