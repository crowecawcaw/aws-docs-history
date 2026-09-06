

# Storage services
<a name="sns-event-sources-storage"></a>

The following table describes how Amazon SNS integrates with AWS storage services like AWS Backup, Amazon Elastic File System (EFS), Amazon Glacier, Amazon S3, and AWS Snowball Edge to provide notifications for various events such as backup activities, file system alarms, data retrieval jobs, bucket changes, and data transfer operations. 

These integrations help you to efficiently monitor and manage your storage solutions by receiving timely alerts on critical storage events.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) – Helps you centralize and automate the backup of data across AWS services in the Cloud and on premises | Receive notifications of AWS Backup events. For more information, see [Using Amazon SNS to track AWS Backup events](https://docs.aws.amazon.com/aws-backup/latest/devguide/sns-notifications.html) in the *AWS Backup Developer Guide*. | 
| [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) – Provides file storage for your Amazon EC2 instances. | Receive notifications of alarms you've created for Amazon EFS events. For more information, see [Automated monitoring tools](https://docs.aws.amazon.com/efs/latest/ug/monitoring_automated_manual.html#monitoring_automated_tools) in the *Amazon Elastic File System User Guide*. | 
| [Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) – Provides storage for infrequently used data. | Set a notification configuration on a vault so that when a job completes, a message is sent to an SNS topic. For more information, see [Configuring vault notifications in Amazon Glacier](https://docs.aws.amazon.com/amazonglacier/latest/dev/configuring-notifications.html) in the *Amazon Glacier Developer Guide*. | 
| [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) – Provides object storage. | Receive notifications when changes occur to an Amazon S3 bucket or in the rare instance when objects don't replicate to their destination Region. For more information, see [Walkthrough: Configure a bucket for notifications (SNS topic or SQS queue)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ways-to-add-notification-config-to-bucket.html) and [Monitoring progress with replication metrics and Amazon S3 event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-metrics.html) in the *Amazon Simple Storage Service User Guide*. | 
| [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/ug/whatissnowball.html) – Uses physical storage devices to transfer large amounts of data between Amazon S3 and your onsite data storage location at faster-than-internet speeds. | Receive notifications for Snowball Edge jobs. For more information, see [Notifications for Snow Family devices](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/notifications.html) in the *AWS Snowball Edge User Guide*. | 