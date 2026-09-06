

# Connected Home: Machine Learning at the Edge
<a name="connected-home-ml-edge"></a>

Publication date: **July 13, 2021 ([Diagram history](#home-ml-history))**

With this architecture, you can run machine learning (ML) inference on Internet of Things (IoT) video cameras and other home devices. The solution uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/) for edge deployments and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for model training and optimization.

## Connected home ML at the edge diagram
<a name="home-ml-diagram"></a>

![Reference architecture diagram showing how to run ML inference on IoT home devices by using AWS IoT Greengrass, SageMaker AI, Amazon Data Firehose, and Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/connected-home-ml-edge/images/connected-home-ml-edge.png)


The following steps describe the architecture:

1. Publish training data from an IoT video camera running AWS IoT Greengrass to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/).

1. Configure an AWS IoT rule that listens for camera data and forwards messages to Amazon Data Firehose for storage in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Use SageMaker AI to train, optimize, and build ML models that use less than a tenth of the memory footprint found in resource-constrained devices like cameras.

1. Output trained models from SageMaker AI to Amazon S3 for delivery to the IoT video camera.

1. Use the AWS IoT Greengrass cloud service to orchestrate deployments to the target IoT video camera. Deployments can include trained ML models and application logic, such as a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function or Docker container.

1. Run a Lambda function locally on the IoT video camera to perform inference by using the latest version of the trained ML model.

1. View the camera's video stream through Amazon Kinesis Video Streams by using a mobile application.

## Further reading
<a name="home-ml-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="home-ml-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#home-ml-history) | Reference architecture diagram first published. | July 13, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.