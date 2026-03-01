# Connected Aircraft Solution Architecture

Publication date: **September 22, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This reference architecture shows how you can onboard flight data collection for fleet-wide analytics and predictive maintenance using AWS IoT Greengrass, Amazon S3, Amazon Managed Service for Apache Flink, and Amazon SageMaker AI.

## Connected Aircraft Solution Architecture Diagram

![Reference architecture diagram showing how you can use AWS services to onboard flight data collection for fleet-wide analytics and predictive maintenance.](images/connected-aircraft-solution-architecture.png)

1. Flight (avionics) and telemetry (sensor) data is collected by **AWS IoT Greengrass**, running on the flight-data acquisition unit on board.
2. Near real-time events are anonymized and sent to Flight Operations on the ground.
   Flight data is offloaded to **Amazon Simple Storage Service** (Amazon S3) with aircraft
   at the gate and analyzed by the Flight Operations Team for fuel burn optimization, fault
   analysis, and other use cases.
3. Engine flight data is processed and analyzed with **Amazon Managed Service for Apache Flink** for engine health maintenance and the Flight
   Operations Team notified of any anomalies.
4. Anonymized flight and fault data is aggregated using **Amazon Athena** and stored in an **Amazon S3**
   data lake.
5. Models trained from aggregated flight and fault data are deployed to **AWS IoT Greengrass** on the aircraft for Machine Learning inference driving predictive
   maintenance.
6. App developers build new digital solutions for the connected ecosystem using **Amazon API Gateway**, **AWS Lambda**, and **Athena**.
7. Anonymized data is offered to third-party developers on a subscription basis with **AWS Data Exchange**.
8. Fleet–wide analytics is performed by the Engine Health Management team by querying processed
   flight data using **Amazon Quick** and **Athena**.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/connected-aircraft-solution-architecture.md "samples/connected-aircraft-solution-architecture.md") which contains an editable PowerPoint.

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

| Change              | Description                                     | Date               |
| ------------------- | ----------------------------------------------- | ------------------ |
| Initial publication | Reference architecture diagram first published. | September 22, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
