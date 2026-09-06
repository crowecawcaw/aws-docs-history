

# Producing Data to InforOS over SFTP
<a name="producing-data-to-inforos"></a>

Publication date: **March 20, 2021 ([Diagram history](#pdi-diagram-history))**

With this architecture, you can integrate your applications with Infor CloudSuite by using bulk data transfer over Secure File Transfer Protocol (SFTP). You use [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) as the managed SFTP server, with [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) for storage.

## Producing data to InforOS architecture diagram
<a name="pdi-diagram"></a>

![Architecture diagram for producing data to Infor CloudSuite over SFTP with AWS Transfer Family on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/producing-data-to-inforos/images/producing-data-to-infor-over-sftp-ra.png)


The following steps describe the architecture:

1. Example producers write data to Amazon S3. These include [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/), [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/), and [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

1. (Optional) Use AWS PrivateLink to avoid over-the-internet traffic between your [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/) and Amazon S3.

1. An administrator creates an SFTP user in Transfer Family and passes credentials to Infor ION.

1. Files moving over SFTP can be BOD/XML, delimiter-separated, JSON, or schema-free formats.

1. Infor ION acts as an SFTP client, polling the SFTP server for new data.

1. Infor CloudSuite applications consume data. These applications include Infor M3, Infor WMS, Infor EAM, and others.

## Further reading
<a name="pdi-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Consuming Data from InforOS over SFTP](../consuming-data-from-inforos/consuming-data-from-inforos.html)

## Diagram history
<a name="pdi-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pdi-diagram-history) | Reference architecture diagram first published. | March 20, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.