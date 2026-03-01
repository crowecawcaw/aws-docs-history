# Kelvin AI on AWS

Publication date: **October 20, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

Kelvin’s solution, built on AWS Cloud, allows enterprises to scale faster, optimize their industrial operations in real time, and accelerate their digital transformation initiatives.

## Kelvin AI on AWS Diagram

![Reference architecture diagram showing Kelvin’s solution, built on AWS Cloud, which allows enterprises to scale faster, optimize their industrial operations in real time, and accelerate their digital transformation initiatives.](images/kelvin-ai-on-aws.png)

1. Time-series data from industrial historians or industrial gateway/programmable
   logic controllers (PLCs) leveraging MQTT, OPC-UA, and Modbus protocols are sent
   to the edge nodes.
2. The solution consists of a streaming data broker for time series data, a node
   historian for short-term time series data store, an edge sync module that syncs
   edge node with the cloud after loss of connectivity. The solution also manages
   workload orchestration using connectivity brokers, node telemetry, and services
   for asset models and their configuration.
3. Kelvin Manager manages the edge nodes and deploys Kelvin Bridges (connectors)
   or custom Python apps, users, assets, and metric definitions.
4. Kelvin SDK is used to develop, configure, deploy and manage services, with
   both a CLI and a library framework to develop apps.
5. Kelvin cluster is built on **Amazon Elastic Kubernetes Service** (Amazon EKS)
   and hosts the Kelvin platform. It consists of streaming data brokers, cloud
   historians, APIs, and integration services. Control changes are processed and
   sent to the industrial gateway/PLC through edge nodes from the platform.
6. Kelvin Nodes run on **Amazon Elastic Compute Cloud** (Amazon EC2) to
   ingest telemetry data already in the AWS account.
7. Kelvin Maps allows users to visualize processes, asset performance,
   time-series data, and alarms. Copilots is a specialized user experience
   solution aimed at specific tasks or industries.
8. **Amazon Simple Storage Service** (Amazon S3) can be used to store asset
   hierarchy and time-series data that is ingested by Kelvin Nodes. Kelvin can
   push data to **AWS IoT SiteWise**. It integrates with
   **Amazon Quick** as an alternative to Kelvin Maps.
   Integration with **Amazon SageMaker AI** allows for creating
   and importing customer algorithms to deploy on Kelvin Nodes.
9. The Kelvin platform in the cloud stores asset information and user profiles
   in **Amazon Relational Database Service** (Amazon RDS), while **Amazon Simple Notification Service**
   (Amazon SNS) is used to initiate alarm notifications to end users.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/kelvin-ai-on-aws.md "samples/kelvin-ai-on-aws.md") which contains an editable PowerPoint.

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

## Contributors

Contributors to this reference architecture diagram include:

- Avinash Venkatagiri, Partner Solutions Architect, Amazon Web Services
- Madhu Pai, Principal Partner Solutions Architect, Amazon Web Services

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- |
| Initial publication | Reference architecture diagram first published. | October 20, 2023 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
