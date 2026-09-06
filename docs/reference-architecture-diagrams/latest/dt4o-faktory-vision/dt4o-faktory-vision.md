

# DT4o Faktory Vision: Quality Insights on AWS
<a name="dt4o-faktory-vision"></a>

Publication date: **December 11, 2022 ([Diagram history](#dfv-diagram-history))**

With this architecture, you can deploy computer vision-based quality detection and defect analytics to minimize product defects in manufacturing. DT4o Faktory Vision uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/), and [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/).

## DT4o Faktory Vision architecture diagram
<a name="dfv-diagram"></a>

![Architecture diagram for DT4o Faktory Vision quality insights on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/dt4o-faktory-vision/images/DT4o-faktory-vision-ra.png)


The following steps describe the architecture:

1. At the plant, acquire production data and synchronize cameras with the production controller (PLC). AWS IoT Greengrass initiates camera capture and inference events.

1. Capture images from cameras at low latency at the edge by using Message Queuing Telemetry Transport (MQTT). Store images in Amazon S3 through AWS IoT Greengrass.

1. The DT4o Faktory Vision container on Amazon EC2 configures the plant hierarchy and initiates ML modeling. Fine-tune and generate new model versions based on operator input.

1. Use SageMaker AI to train ML models per product type. Store model versions in Amazon S3.

1. Download ML models into the Faktory Inference local disk.

1. Load ML models onto the Faktory Inference service by plant hierarchy.

1. Access ML models for runtime inference at Faktory Edge (under 500 ms for inference).

1. Product quality insights display with raw and processed images (under 600 ms).

## Further reading
<a name="dfv-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="dfv-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#dfv-diagram-history) | Reference architecture diagram first published. | December 11, 2022 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.