

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Altering CloudWatch log retention
<a name="log-customize-retention"></a>

You can change the log data retention setting for CloudWatch logs. By default, logs are kept indefinitely and never expire. You can adjust the retention policy for each log group, keeping the indefinite retention, or choosing a retention period between 10 years and one day. To view the allowed minimum retention period in AMS, see the AMS Technical Standards document available through AWS Artifact. To access AWS Artifact, contact your CSDM for instructions or go to [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started/). 

 The CloudWatch Logs log retention feature deletes the log events in a stream based on retention policy. It doesn't delete log streams or log groups. For general information, see the *Amazon CloudWatch Logs User Guide* [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html).

For information on customizing a log retention period, and to learn more, see [ Change Log Data Retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention).