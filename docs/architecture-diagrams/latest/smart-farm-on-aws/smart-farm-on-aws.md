# Smart Farm on Amazon Web Services

Publication date: **October 24, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This Connected Farm reference architecture enables sensors, computer vision, and edge
inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness
for each operation’s growing and changing needs.

## Smart Farm on Amazon Web Services Diagram

### Reference Architecture

Diagram

![Reference architecture diagram showing how to create a Connected Farm that enables sensors, computer vision, and edge inference in agriculture by focusing on ensuring scalability, elasticity, and a responsiveness for each operation’s growing and changing needs.](images/smart-farm-on-aws.png)

1. Third-party sensors or drones not using **FreeRTOS** send
   data through **AWS Lambda** for protocol conversion.
2. Sensors or cameras running **FreeRTOS** send data to
   **AWS IoT Greengrass**, providing protection from
   intermittent connectivity.
3. **AWS IoT Greengrass** streams enable ingestion from
   edge devices to **Kinesis Data Streams**.
4. Use real-time video via **Amazon Kinesis Video Streams** for streaming and replay of video
   content.
5. Derive real-time insights with **Amazon Managed Service for Apache Flink** and notify users via **Amazon Simple Notification Service**.
6. Enable analytics with **OpenSearch** and
   use **Amazon Simple Storage Service** for a
   data lake strategy.
7. Transfer owned data, like planting records or farm finances, securely into your data
   lake with **Direct Connect**.
8. Securely consume data from a sensor ecosystem hosted on AWS with **AWS PrivateLink**.
9. Empower users with insights delivered via **Amazon API Gateway** or visualizations with **Quick Suite**.
10. Build and deploy machine learning (ML) models for edge inference with **Amazon SageMaker AI**. Use **Amazon SageMaker Ground Truth** to manage data labeling workflow.
11. Each time a new file is written into **Amazon S3**, **AWS Glue crawler** crawls the data to infer the schema and make
    it available into the **AWS Glue Data Catalog**. **Amazon Athena** does on-demand querying.
12. Use a **Lambda** function that imports the **AWS IoT Device Defender** reports into **AWS Security Hub** to centralize incident response.

### Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/smart-farm-on-aws.md "samples/smart-farm-on-aws.md") which contains an editable PowerPoint.

### Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

### Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

### Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- |
| Initial publication | Reference architecture diagram first published. | October 24, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
