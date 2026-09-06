

# Automated Archival for Amazon Redshift
<a name="automated-archival-redshift"></a>

Publication date: **July 12, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to automate the periodic data archival process for an [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/welcome.html) database. The cold data remains available instantly, and you can join it with existing datasets in the Amazon Redshift cluster using Amazon Redshift Spectrum.

## Automated Archival for Amazon Redshift
<a name="diagram1"></a>

![Architecture diagram showing automated archival for Amazon Redshift with Step Functions, Lambda, Amazon S3, and EventBridge.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/automated-archival-redshift/images/automated-archival-redshift.png)


The following steps describe the architecture:

1. Ingest data into the Amazon Redshift cluster at various frequencies.

1. After every ingestion load, create a queue of metadata about tables populated into Amazon Redshift tables in Amazon RDS. Data engineers can also create the archival queue manually.

1. Use [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to trigger an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function periodically. The function reads the queue from the RDS table and creates an [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) message for every period due for archival.

1. A proxy Lambda function dequeues the Amazon SQS messages and invokes [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for every message.

1. Step Functions unloads the data from the Amazon Redshift cluster into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket for the given table and period.

1. Amazon S3 Lifecycle configuration moves data in buckets from S3 Standard storage class to S3 Glacier storage class after 90 days.

1. Amazon S3 inventory tool generates manifest files from the Amazon S3 bucket dedicated for cold data on a daily basis and stores them in an Amazon S3 bucket for manifest files.

1. Every time an inventory manifest file is created in a manifest Amazon S3 bucket, a Lambda function triggers through an Amazon S3 event notification.

1. A Lambda function normalizes the manifest file for easy consumption in the event of restore.

1. Query the data stored in the Amazon S3 bucket for cold data using Amazon Redshift Spectrum.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | July 12, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.