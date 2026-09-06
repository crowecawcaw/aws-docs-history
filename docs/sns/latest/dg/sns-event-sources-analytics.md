

# Analytics services
<a name="sns-event-sources-analytics"></a>

The following table describes how Amazon SNS integrates with AWS analytics services such as Athena, AWS Data Pipeline, and Amazon Redshift to provide real-time notifications for key events, including control limit breaches, pipeline status updates, and data warehouse activities.

You can leverage these integrations to automate responses and maintain effective oversight of your data operations.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) – Allows you to analyze data in Amazon S3 using standard SQL. | Receive notifications when control limits are exceeded. For more information, see [Setting data usage control limits](https://docs.aws.amazon.com/athena/latest/ug/workgroups-setting-control-limits-cloudwatch.html) in the *Amazon Athena User Guide*. | 
| [AWS Data Pipeline](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/what-is-datapipeline.html) – Helps automate the movement and transformation of data. | Receive notifications about the status of pipeline components. For more information, see [SnsAlarm](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-object-snsalarm.html) in the *AWS Data Pipeline Developer Guide*. | 
| [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) – Manages all of the work of setting up, operating, and scaling a data warehouse. | Receive notifications of Amazon Redshift events. For more information, see [Amazon Redshift event notifications](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-event-notifications.html) in the *Amazon Redshift Management Guide*. | 