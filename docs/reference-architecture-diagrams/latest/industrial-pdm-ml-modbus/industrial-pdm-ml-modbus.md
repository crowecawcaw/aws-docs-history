

# AWS Industrial PdM ML Model with Modbus Communication
<a name="industrial-pdm-ml-modbus"></a>

Publication date: **March 4, 2024 ([Diagram history](#ipm-diagram-history))**

With this architecture, you can create a predictive maintenance (PdM) ML model by using [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/) and [AWS IoT Analytics](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-analytics) with [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS) anomaly detection notifications. This solution uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/), [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/), and [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

## Industrial PdM ML Modbus architecture diagram
<a name="ipm-diagram"></a>

![Architecture diagram for AWS Industrial PdM ML Model with Modbus communication.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-pdm-ml-modbus/images/aws-industrial-PdM-ML-modbus-RA.png)


The following steps describe the architecture:

1. Deploy an AWS IoT SiteWise Gateway to connect to factory machines' OPC Unified Architecture (OPC-UA) Servers.

1. Create a view in AWS IoT SiteWise and define factory machines as assets with metrics to monitor.

1. Configure a Modbus Greengrass Connector on AWS IoT Greengrass to send Modbus data to AWS IoT Analytics through an AWS IoT Core rule.

1. Build a Docker image and add it to Amazon ECR.

1. In AWS IoT Analytics, create a container data set from the AWS IoT SiteWise data store linked to your Docker container.

1. Create a Jupyter Notebook for the data set to build a PdM ML model.

1. Visualize analysis with Quick on the AWS IoT Analytics data source.

1. Create a topic for anomaly detection notifications in Amazon SNS and configure the trigger.

For a related reference architecture, see [AWS Industrial IoT Predictive Maintenance ML Model](../industrial-iot-predictive-maintenance-ml/industrial-iot-predictive-maintenance-ml.html).

## Further reading
<a name="ipm-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Industrial PdM ML Model and Anomaly Detection](../industrial-pdm-ml-anomaly-detection/industrial-pdm-ml-anomaly-detection.html)

## Diagram history
<a name="ipm-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ipm-diagram-history) | Reference architecture diagram first published. | March 4, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.