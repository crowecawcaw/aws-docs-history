

# Connected Mobility Platform
<a name="connected-mobility-platform-on-aws"></a>

Publication date: **December 13, 2022 ([Diagram history](diagram-history.md))**

This architecture addresses three elements of the connected platform: in-vehicle, external infrastructure, and backend services on the cloud. The adoption of serverless architecture helps reduce the operational overhead for the connected mobility platform.

The AWS IoT FleetWise edge agent and AWS IoT Core move vehicle data to the cloud, where Amazon Simple Storage Service (Amazon S3), Amazon Timestream, and Amazon DynamoDB store it and AWS Lake Formation governs the data lake. AWS Data Exchange and Amazon API Gateway expose the data APIs, Amazon Managed Service for Apache Flink, Amazon Rekognition, and Amazon SageMaker AI produce alerts, insights, and models, Amazon Location Service powers a fleet management portal, and Amazon Connect Customer and Amazon Chime run the call center.

## Connected Mobility Platform diagram
<a name="connected-mobility-platform-on-aws-diagram1"></a>

![Diagram of the Connected Mobility Platform on AWS, from vehicle edge components through AWS IoT Core to cloud data and services.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/automotive/images/connected-mobility-platform-on-aws.png)


1. Use an [AWS IoT FleetWise](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/) edge agent and [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) to send and receive data from the cloud. [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) can host the edge components and is used for machine learning (ML) at the edge. 

1. Use [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/) to onboard vehicles and manage lifecycles. Perform remote operations with [AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/). 

1. Store raw telemetry data and meaningful values from [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/) in an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) bucket, store aggregated data in [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/), and govern the data lake with [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/). 

1. Expose service and data APIs for internal and external use with [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/). 

1. Generate alerts and insights in near real time with [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/). 

1. Personalize use cases with [Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/) and develop custom models with [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for preventive or predictive use cases. 

1. Create a fleet management portal for fleet operators to monitor vehicles in near real time using [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/). 

1. Run the call center with [Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/) and [Amazon Chime](https://docs.aws.amazon.com/chime/latest/ag/), and visualize call insights with [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/). 

## Further reading
<a name="connected-mobility-platform-on-aws-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 