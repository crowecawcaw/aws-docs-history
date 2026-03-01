# Fleet Management Solution for Connected Farm

Publication date: **August 19, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to to create an intelligent fleet management solution for farming, using data from Internet of Things (IoT) sensors and cameras at strategic locations and in assets such as tractors and combine harvesters. Increasingly, these assets are equipped with multiple sensors for monitoring environmental conditions, hazards, and detecting changes in operations.

## Fleet Management Solution for Connected Farm Diagram

![Reference architecture diagram showing how to create an intelligent fleet management solution for farming, using data from Internet of Things (IoT) sensors and cameras at strategic locations and in assets such as tractors and combine harvesters. Increasingly, these assets are equipped with multiple sensors for monitoring environmental conditions, hazards, and detecting changes in operations.](images/fleet-management-for-connected-farm.png)

1. Third-party sensors send data such as environmental conditions and operations data
   through **AWS IoT Greengrass** and **AWS Lambda** with protocol compatibility.
2. **AWS IoT Greengrass** streams enable ingestion from edge devices to
   **AWS IoT Analytics** for data processing and analysis.
3. **AWS IoT Analytics** stores and enriches data for use in ML
   model building. Use custom **AWS Lambda** functions to derive
   new attributes to classify the data.
4. Analyze and visualize time-series data using **AWS IoT Analytics**
   and **Amazon Quick**.
5. Apply machine learning to data with hosted Jupyter Notebooks. Build and deploy
   predictive maintenance models for edge inference with **Amazon SageMaker AI**.
6. **AWS IoT Events** monitors change events from IoT sensors and
   sends an image capture request back to edge devices through an **AWS IoT Core** MQTT topic.
7. Upload images to **Amazon Simple Storage Service** (Amazon S3) via **AWS IoT Greengrass** streams. **Lambda** uses
   **SageMaker AI** to run images against models to optimize
   operations by detecting crop conditions, the state of physical assets and detecting
   obstacles.
8. Geofencing an area of interest in **Amazon Location**. Fleets
   send location coordinates captured through **AWS IoT Core**.
9. **Amazon EventBridge** routes geofence events to predefined targets
   in near real-time.
10. Notify users via **Amazon Simple Notification Service** (Amazon SNS).

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/fleet-management-for-connected-farm.md "samples/fleet-management-for-connected-farm.md") which contains an editable PowerPoint.

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

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | August 19, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
