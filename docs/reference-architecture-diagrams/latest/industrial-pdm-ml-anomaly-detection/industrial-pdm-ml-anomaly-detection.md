

# AWS Industrial PdM ML Model and Anomaly Detection
<a name="industrial-pdm-ml-anomaly-detection"></a>

Publication date: **March 4, 2024 ([Diagram history](#ipa-diagram-history))**

With this architecture, you can create a predictive maintenance (PdM) ML model by using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) with [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) and an anomaly detection application by using Amazon Managed Service for Apache Flink. This solution uses [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/).

## Industrial PdM ML anomaly detection architecture diagram
<a name="ipa-diagram"></a>

![Architecture diagram for AWS Industrial PdM ML Model and Anomaly Detection.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-pdm-ml-anomaly-detection/images/aws-industrial-PdM-ML-anomaly-RA.png)


The following steps describe the architecture:

1. Configure AWS IoT Greengrass with connectors to communicate with factory machines.

1. Configure rules in AWS IoT Core to trigger events based on Message Queuing Telemetry Transport (MQTT) topics.

1. Create an Amazon Data Firehose delivery stream to store factory data in an Amazon S3 data lake.

1. Build a PdM ML model with SageMaker AI.

1. Deploy the ML model onto the AWS IoT Greengrass Edge Gateway.

1. Build data queries in [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) against the [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) Data Catalog.

1. Visualize analysis with [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) on the Athena data source.

1. Create an anomaly detection application in Amazon Managed Service for Apache Flink.

1. Configure [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) as output to send anomaly notifications to Amazon SNS.

For related reference architectures, see [AWS Industrial PdM ML Model with Modbus Communication](../industrial-pdm-ml-modbus/industrial-pdm-ml-modbus.html) and [AWS Industrial IoT Predictive Maintenance ML Model](../industrial-iot-predictive-maintenance-ml/industrial-iot-predictive-maintenance-ml.html).

## Further reading
<a name="ipa-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Industrial PdM ML Model with Modbus Communication](../industrial-pdm-ml-modbus/industrial-pdm-ml-modbus.html)

## Diagram history
<a name="ipa-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ipa-diagram-history) | Reference architecture diagram first published. | March 4, 2024 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.