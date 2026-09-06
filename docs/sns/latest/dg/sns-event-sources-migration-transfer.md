

# Migration & transfer services
<a name="sns-event-sources-migration-transfer"></a>

The following table describes how Amazon SNS integrates with AWS migration and transfer services, such as AWS Application Discovery Service, AWS Database Migration Service (DMS), and AWS Snowball Edge, to provide notifications for events like server data collection, database migration activities, and data transfer jobs. 

These integrations help you to effectively manage and monitor your Cloud migration processes by offering real-time alerts and updates on critical migration tasks.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [AWS Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) – Helps you plan your migration to the AWS Cloud by collecting usage and configuration data about your on-premises servers. | Receive notifications of events through AWS CloudTrail. For more information, see [Logging Application Discovery Service API calls with AWS CloudTrail](https://docs.aws.amazon.com/application-discovery/latest/userguide/logging-using-cloudtrail.html) in the *Application Discovery Service User Guide*. | 
| [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Introduction.html) – Migrates data from on-premises databases into the AWS Cloud. | Receive notifications when AWS DMS events occur; for example, when a replication instance is created or deleted. For more information, see [Working with events and notifications in AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html) in the *AWS Database Migration Service User Guide*. | 
| [AWS Snowball Edge](https://docs.aws.amazon.com/snowball/latest/ug/whatissnowball.html) – Uses physical storage devices to transfer large amounts of data between Amazon S3 and your onsite data storage location at faster-than-internet speeds. | Receive notifications for Snowball Edge jobs. For more information, see [Notifications for Snow Family devices](https://docs.aws.amazon.com/snowball/latest/snowcone-guide/notifications.html) in the *AWS Snowball Edge User Guide*. | 