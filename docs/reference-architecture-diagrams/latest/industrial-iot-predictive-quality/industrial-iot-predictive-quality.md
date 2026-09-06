

# AWS Industrial IoT Predictive Quality
<a name="industrial-iot-predictive-quality"></a>

Publication date: **July 16, 2020 ([Diagram history](#pq-diagram-history))**

With this architecture, you can create a computer vision predictive quality ML model by using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) with [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), and [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/). You can detect product defects in near real time and alert operations teams.

## Predictive quality architecture diagram
<a name="pq-diagram"></a>

![Reference architecture diagram for creating a predictive quality ML model by using computer vision on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-iot-predictive-quality/images/AWS Industrial - Predictive Quality Reference Architecture.png)


The following steps describe the architecture:

1. Configure AWS IoT Greengrass to communicate with industrial equipment to capture data and video from factory floor cameras and sensors.

1. Configure the AWS IoT SiteWise Connector on AWS IoT Greengrass to connect by using OPC Unified Architecture (OPC-UA).

1. Use AWS IoT SiteWise to model assets that represent on-premises devices, equipment, and processes.

1. Use AWS IoT Greengrass to exchange messages with AWS IoT Core and send processed images to [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) in Lake Formation.

1. Configure rules in AWS IoT Core to trigger events and send data to [AWS IoT Events](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-events) and [AWS IoT Analytics](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-analytics).

1. Build a predictive quality ML model with Amazon SageMaker AI based on images stored in Lake Formation.

1. Deploy the ML model onto the AWS IoT Greengrass Edge Gateway for local inference at the factory.

1. Create a topic for quality alerts in [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS) to notify the Operations Engineer when defects are detected.

1. Create a web portal with AWS IoT SiteWise Monitor to visualize factory data in near real time.

1. Derive insights with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) on AWS IoT Analytics.

## Further reading
<a name="pq-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Manufacturing on AWS](../manufacturing-on-aws/manufacturing-on-aws.html)

## Diagram history
<a name="pq-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pq-diagram-history) | Reference architecture diagram first published. | July 16, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.