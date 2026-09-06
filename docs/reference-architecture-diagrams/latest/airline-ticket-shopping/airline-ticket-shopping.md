

# Streaming Airline Ticket Shopping Insights
<a name="airline-ticket-shopping"></a>

Publication date: **March 10, 2021 ([Diagram history](#ticket-shopping-history))**

3Victors implemented an AWS architecture to capture and durably store over 10 TB of daily streamed air shopping data into a data lake. Dozens of extract, transform, and load (ETL) jobs run at regular intervals.

The implementation provides an extensible, real-time predictive analytics pipeline for demand forecasting and deal classification.

## Streaming airline ticket shopping insights diagram
<a name="ticket-shopping-diagram"></a>

![Architecture for streaming airline ticket shopping insights on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/airline-ticket-shopping/images/airline-ticket-shopping-ra.png)


The following steps describe the architecture:

1. [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) directs per-stream vendor content to source-specific AWS Elastic Beanstalk application orchestration. Handle 20,000 per second HTTPS POST transactions with autoscaling on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Spot Instances. Monitor with [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/). Log statistics to [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) through Amazon Data Firehose.

1. Transform captured pricing data into a common format. Place data on a durable 24-hour [Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) streaming buffer across 100 or more shards.

1. Two concurrent pipelines fan out from the streaming buffer.

1. A data lake pipeline persists data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) Intelligent-Tiering. Directory paths support partitioning and cross-account access. Update schema-on-read mappings in [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) metastore for [Athena](https://docs.aws.amazon.com/athena/latest/ug/) analytics. Lifecycle policies archive to Amazon S3 Glacier Deep Archive.

1. Periodic ETL jobs deposit results into cross-account Data Ponds by using [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) transient compute with Spot Instance fleets. AWS Glue metastore provides Amazon Redshift Spectrum access integrated with Amazon Redshift for business intelligence tool access.

1. A real-time analytics pipeline fans out to Kinesis stream buffers. Populate [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) (row) and [Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/) (graph) databases for customer API access through serverless API Gateway and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/). Optimize database I/O with [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/).

## Further reading
<a name="ticket-shopping-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ticket-shopping-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ticket-shopping-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.