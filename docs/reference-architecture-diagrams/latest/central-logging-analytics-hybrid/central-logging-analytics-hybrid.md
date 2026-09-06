

# Central Logging and Analytics in Hybrid Environments
<a name="central-logging-analytics-hybrid"></a>

Publication date: **July 21, 2020 ([Diagram history](#diagram-history))**

This architecture shows how to build a central logging and analytics solution. You can analyze [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) logs from a hybrid environment, including VMware Cloud on AWS.

## Central Logging and Analytics in Hybrid Environments
<a name="diagram1"></a>

![Architecture diagram showing a central logging and analytics solution for hybrid environments with Amazon CloudWatch.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/central-logging-analytics-hybrid/images/central-logging-analytics-hybrid.png)


1. Install the Amazon CloudWatch agent on VMs on-premises.

1. Send CloudWatch metrics and logs to the customer central logging VPC through and AWS Transit Gateway.

1. Send CloudWatch data from VMware Cloud on AWS to the CloudWatch endpoint in the customer-owned VPC through an elastic network interface.

1. Export log data from your log group to load onto other systems such as ISV solutions.

1. Create a subscription to deliver logs from a specific CloudWatch log group to [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) in the logging account destination.

1. Use Amazon Data Firehose to continuously stream the log data to [https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).

1. Use Amazon Data Firehose to deliver log data to the [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

1. Use [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to build the Data Catalog and to create the ETL jobs for data processing.

1. [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) uses the AWS Glue Data Catalog to discover and query data in Amazon S3.

1. [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) reads and loads data from multiple data files stored in Amazon S3 buckets.

1. Build visualizations and dashboards by using [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) with Amazon Athena and Amazon Redshift.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon CloudWatch product page](https://aws.amazon.com/cloudwatch/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 21, 2020 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.