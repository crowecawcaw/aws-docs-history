# Connected Mobility Platform

Publication date: **December 13, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture addresses three elements of the connected platform: in-vehicle, external infrastructure, and backend services on the cloud. The adoption of serverless architecture will help to reduce the operational overhead for the connected mobility platform.

## Connected Mobility Platform Diagram

![Reference architecture diagram showing how to use AWS services on your connected mobility platform.](images/connected-mobility-platform-on-aws.png)

1. Use an **AWS IoT FleetWise** edge agent and **AWS IoT Core** to
   send and receive data from the cloud. **AWS IoT Greengrass** can host the edge
   components and is used for machine learning (ML) at the edge.
2. Use **AWS IoT Device Management** to onboard vehicles and manage lifecycles. Perform remote
   operations with **AWS IoT Device Shadow service**.
3. An **Amazon Simple Storage Service** (Amazon S3) bucket stores raw telemetry data and meaningful
   values from **Amazon Timestream**. **Amazon DynamoDB**
   stores aggregated data and **AWS Lake Formation** governs the data lake.
4. **AWS Data Exchange** and **Amazon API Gateway** expose service
   and data APIs for internal and external use.
5. **Amazon Managed Service for Apache Flink** generates alerts and insight in near real time.
6. Personalize use cases with **Amazon Rekognition** and develop custom models
   with **Amazon SageMaker AI** for preventive or predictive use cases.
7. Create a fleet management portal for fleet operators to monitor vehicles in near
   real time using **Amazon Location Service**.
8. **Amazon Connect** and **Amazon Chime** enable
   the call center. You can visualize call insights through **Amazon Quick**.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/connected-mobility-platform-on-aws.md "samples/connected-mobility-platform-on-aws.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- |
| Initial publication | Reference architecture diagram first published. | December 13, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
