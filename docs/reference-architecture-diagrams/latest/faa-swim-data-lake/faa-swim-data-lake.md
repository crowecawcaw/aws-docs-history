

# Using the Federal Aviation Administration SWIM Data Lake
<a name="faa-swim-data-lake"></a>

Publication date: **March 10, 2021 ([Diagram history](#faa-swim-history))**

The Federal Aviation Administration (FAA) System Wide Information Management (SWIM) Data Lake provides real-time delivery of aeronautical flight and weather information. This helps airline companies optimize their operations.

This architecture processes SWIM data through a series of [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) functions and [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) Data Streams. It transforms, enriches, and analyzes flight data. You can then visualize the results with Amazon Quick Sight or consume them through custom applications.

## FAA SWIM data lake diagram
<a name="faa-swim-diagram"></a>

![Architecture for FAA SWIM data lake using Amazon Kinesis, AWS Lambda, and AWS Glue.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/faa-swim-data-lake/images/FAA-SWIM-Data-Lake.png)


The following steps describe the architecture:

1. The SWIM Consumer App consumes SWIM data. It sends the data to an [Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) Data Stream.

1. [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) converts the XML data to JSON format.

1. Lambda simplifies the JSON data for downstream processing.

1. Lambda filters customer flight data. It writes one copy to Kinesis Data Stream and a second to the subsequent Lambda function.

1. Lambda enriches customer flight messages with operational or external datasets.

1. Lambda writes enriched flight data to [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/).

1. Lambda writes enriched flight data to Kinesis Data Stream.

1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) extract, transform, and load (ETL) jobs transform enriched flight data from JSON to Parquet with appropriate partitions. The jobs register Parquet files as external tables in AWS Glue Data Catalog.

1. Services such as [Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/), and Amazon Aurora analyze the transformed and enriched flight data.

1. Services such as [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html), custom applications, and APIs consume the analyzed data.

1. AWS Glue Data Catalog stores databases and tables. These represent raw, transformed, enriched, and analyzed datasets in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), Amazon Aurora, and Amazon Redshift.

## Further reading
<a name="faa-swim-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="faa-swim-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#faa-swim-history) | Reference architecture diagram first published. | March 10, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.