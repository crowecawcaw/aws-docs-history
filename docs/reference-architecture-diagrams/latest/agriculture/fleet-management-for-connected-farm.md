

# Fleet Management Solution for Connected Farm
<a name="fleet-management-for-connected-farm"></a>

Publication date: **August 19, 2022 ([Diagram history](diagram-history.md))**

This architecture enables you to create an intelligent fleet management solution for farming, using data from Internet of Things (IoT) sensors and cameras at strategic locations and in assets such as tractors and combine harvesters. Increasingly, these assets are equipped with multiple sensors for monitoring environmental conditions, hazards, and detecting changes in operations. 

## Fleet Management Solution for Connected Farm diagram
<a name="fleet-management-for-connected-farm-diagram1"></a>

![Reference architecture diagram showing how to create an intelligent fleet management solution for farming, using data from Internet of Things (IoT) sensors and cameras at strategic locations and in assets such as tractors and combine harvesters. Increasingly, these assets are equipped with multiple sensors for monitoring environmental conditions, hazards, and detecting changes in operations.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/agriculture/images/fleet-management-for-connected-farm.png)


1. Third-party sensors send data such as environmental conditions and operations data through [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) with protocol compatibility. 

1. AWS IoT Greengrass streams enable ingestion from edge devices to AWS IoT Analytics for data processing and analysis. 

1. AWS IoT Analytics stores and enriches data for use in ML model building. Use custom AWS Lambda functions to derive new attributes to classify the data. 

1. Analyze and visualize time-series data using AWS IoT Analytics and [AWS Quick Sight](https://docs.aws.amazon.com/quick/latest/userguide/). 

1. Apply machine learning to data with hosted Jupyter Notebooks. Build and deploy predictive maintenance models for edge inference with [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/). 

1. AWS IoT Events monitors change events from IoT sensors and sends an image capture request back to edge devices through an [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) MQTT topic. 

1. Upload images to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) via AWS IoT Greengrass streams. Lambda uses SageMaker AI to run images against models to optimize operations by detecting crop conditions, the state of physical assets and detecting obstacles. 

1. Geofencing an area of interest in [Amazon Location](https://docs.aws.amazon.com/location/latest/developerguide/). Fleets send location coordinates captured through AWS IoT Core. 

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) routes geofence events to predefined targets in near real-time. 

1. Notify users via [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS). 

## Further reading
<a name="fleet-management-for-connected-farm-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 