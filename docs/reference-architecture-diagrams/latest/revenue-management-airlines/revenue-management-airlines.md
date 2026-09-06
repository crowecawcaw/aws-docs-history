

# Revenue Management Architecture for Airlines
<a name="revenue-management-airlines"></a>

Publication date: **April 5, 2023 ([Diagram history](#revenue-management-airlines-history))**

This reference architecture provides a migration path for airline revenue management systems to AWS. Airlines use this architecture to scale revenue management workloads, add near real-time data feeds, and reduce infrastructure costs. Revenue management teams can dynamically adjust booking controls and meet changing analytics needs.

On-premises revenue management systems cannot scale to meet growing business demands without significant cost increases. They cannot add near real-time data feeds from sources such as ATPCO, QL2/INFARE, and 3Victors. Dynamic adjustments to booking controls and reporting needs require a cloud-native approach.

This migration architecture builds on the [Airlines Data Platform](../airlines-data-platform/airlines-data-platform.html) foundation.

## Revenue management architecture diagram
<a name="revenue-management-airlines-diagram"></a>

![Architecture for airline revenue management using Amazon S3, Amazon EC2, Amazon Redshift, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/revenue-management-airlines/images/migration-arch-revenue-management-ra.png)


The following steps describe the architecture:

1. Use a tiered data lake on [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) for ingestion and processing of batch and near real-time data feeds. Add new data feeds and propagate data changes without reengineering the platform.

1. Migrate existing revenue management modules to [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Spot Instances. Reduce infrastructure costs compared to on-premises systems. Use [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/) to replicate the file structure that the modules require.

1. Convert outputs from revenue management modules and store them in the data lake. Make outputs available for reporting and analytics.

1. Use Amazon EC2 On-Demand Instances for near real-time booking controls. Update fares, rules, and availability in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) for availability services.

1. Provide flexible reporting by using the data lake with [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) and [Athena](https://docs.aws.amazon.com/athena/latest/ug/).

1. Build a revenue management dashboard for reporting, analytics, and configuration adjustments.

## Further reading
<a name="revenue-management-airlines-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="revenue-management-airlines-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#revenue-management-airlines-history) | Reference architecture diagram first published. | April 5, 2023 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.