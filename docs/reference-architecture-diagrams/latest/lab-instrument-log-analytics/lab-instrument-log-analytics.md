

# Lab Instrument Log Acquisition and Analytics on AWS
<a name="lab-instrument-log-analytics"></a>

Publication date: **October 28, 2020 ([Diagram history](#lab-diagram-history))**

With this architecture, you can build a data pipeline to automate lab instrument log ingestion, collate metadata, transform data, and send results to FDA-compliant electronic laboratory notebooks. You can eliminate multiple manual reviews for [drug discovery and development](https://www.fda.gov/patients/drug-development-process/step-1-discovery-and-development). This architecture uses [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/).

## Lab instrument log analytics architecture diagram
<a name="lab-diagram"></a>

![Reference architecture diagram for automating lab instrument log ingestion and analytics on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/lab-instrument-log-analytics/images/lab-instruments-log-analytics-ra.png)


The following steps describe the architecture:

1. Lab instruments create output log files in Network File System (NFS) shares on premises.

1. Deploy an agent on a virtual machine (VM) to read data from NFS storage.

1. Use AWS DataSync to sync data from the NFS share to Amazon S3.

1. A lab scientist invokes the client application to find the experiment output log file.

1. The client application gets a token from [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/) and invokes the API with the experiment ID and Amazon S3 path.

1. Amazon API Gateway validates the Amazon Cognito token and calls the processing Lambda function.

1. The Lambda function reads the file from Amazon S3 and adds the experiment ID as a tag.

1. The Lambda function transforms the file, applies business rules, converts data to JSON, and pushes it to Amazon OpenSearch Service.

1. If the Lambda function fails, it writes the Amazon S3 file information to an error queue. A timed Lambda function reads from the queue to reprocess failed items.

1. (Optional) A Lambda function maintains Amazon S3 file information with metadata in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

1. The Lambda function sends a JSON response through API Gateway to the electronic lab notebook through the mobile client.

1. The lab scientist accesses data in the electronic lab notebook and discovers or queries data through OpenSearch Dashboards.

## Further reading
<a name="lab-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="lab-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#lab-diagram-history) | Reference architecture diagram first published. | October 28, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.