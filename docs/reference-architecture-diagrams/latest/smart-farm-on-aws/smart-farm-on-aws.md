

# Smart Farm on Amazon Web Services
<a name="smart-farm-on-aws"></a>

Publication date: **October 24, 2022 ([Diagram history](#diagram-history))**

This Connected Farm reference architecture enables sensors, computer vision, and edge inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness for each operation’s growing and changing needs.

## Smart Farm on Amazon Web Services Diagram
<a name="diagram1"></a>

### Reference Architecture Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to create a Connected Farm that enables sensors, computer vision, and edge inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness for each operation’s growing and changing needs.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/smart-farm-on-aws/images/smart-farm-on-aws.png)


1. Third-party sensors or drones not using **FreeRTOS** send data through **AWS Lambda **for protocol conversion.

1. Sensors or cameras running **FreeRTOS** send data to **AWS IoT Greengrass**, providing protection from intermittent connectivity.

1. **AWS IoT Greengrass** streams enable ingestion from edge devices to **Kinesis Data Streams**.

1. Use real-time video via **Amazon Kinesis Video Streams** for streaming and replay of video content. 

1. Derive real-time insights with **Amazon Managed Service for Apache Flink ** and notify users via **Amazon Simple Notification Service**.

1. Enable analytics with **OpenSearch** and use **Amazon Simple Storage Service** for a data lake strategy.

1. Transfer owned data, like planting records or farm finances, securely into your data lake with **Direct Connect**.

1. Securely consume data from a sensor ecosystem hosted on AWS with **AWS PrivateLink**.

1. Empower users with insights delivered via **Amazon API Gateway **or visualizations with **Quick**.

1. Build and deploy machine learning (ML) models for edge inference with **Amazon SageMaker AI**. Use **Amazon SageMaker Ground Truth** to manage data labeling workflow.

1. Each time a new file is written into **Amazon S3**, **AWS Glue crawler** crawls the data to infer the schema and make it available into the **AWS Glue Data Catalog**. **Amazon Athena **does on-demand querying.

1. Use a** Lambda **function that imports the **AWS IoT Device Defender** reports into **AWS Security Hub CSPM** to centralize incident response.

### Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

### Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | October 24, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.