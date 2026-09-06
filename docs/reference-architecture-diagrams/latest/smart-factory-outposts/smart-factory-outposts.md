

# Smart Factory on AWS Outposts
<a name="smart-factory-outposts"></a>

Publication date: **March 16, 2022 ([Diagram history](#sfo-diagram-history))**

With this architecture, you can build a scalable, secure IoT-backed smart factory by using [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/) and AWS Regions. This architecture uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Smart factory architecture diagram
<a name="sfo-diagram"></a>

![Reference architecture for a smart factory on AWS Outposts.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-factory-outposts/images/smart-factory-on-outposts-ra.png)


The following steps describe the architecture:

1. The Outpost is located on the factory premises and connected to the factory network through the local gateway (LGW).

1. The Outpost also connects back to the AWS Region, so you can use AWS services in the Region.

1. The plant network connects devices like cameras, equipment, and programmable logic controller (PLC) systems to run plant operations.

1. An Amazon EC2 instance on Outposts acts as an edge gateway. It runs AWS IoT Greengrass and AWS IoT SiteWise Edge to connect with the plant network.

1. The AWS IoT SiteWise Edge component ingests real-time equipment data to the Cloud. It also buffers the data during disconnections.

1. Deploy local dashboards and custom applications on AWS IoT Greengrass for time-critical monitoring and processing.

1. Enterprise apps and point solutions deployed on Outposts as containers can consume data locally from AWS IoT Greengrass.

1. SageMaker AI Neo-optimized models deploy on Outposts for edge inferencing.

1. [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/) automates transfer of data between [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) on Outposts and in the AWS Region.

1. Use Amazon Athena and Quick in the Region for running weekly analytics on the data.

## Further reading
<a name="sfo-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="sfo-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#sfo-diagram-history) | Reference architecture diagram first published. | March 16, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.