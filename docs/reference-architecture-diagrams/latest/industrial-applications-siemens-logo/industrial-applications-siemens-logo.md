

# AWS Industrial Applications with Siemens LOGO\!
<a name="industrial-applications-siemens-logo"></a>

Publication date: **September 27, 2021 ([Diagram history](#slogo-diagram-history))**

With this architecture, you can ingest near real-time data from Siemens LOGO\! controllers to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/). You can build modern applications including dashboards, event detection, alerting, predictive maintenance, and Alexa integration. Use analytics and ML on a data lake for predictive models and forecasts. This architecture uses AWS IoT Core, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/), [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/), and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

## Siemens LOGO\! industrial applications architecture diagram
<a name="slogo-diagram"></a>

![Reference architecture diagram for AWS industrial applications with Siemens LOGO! automation controllers.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/industrial-applications-siemens-logo/images/aws-industrial-applications-with-siemens-logo-ra.png)


The following steps describe the architecture:

1. Siemens LOGO\! controls automation equipment and ingests data to AWS IoT Core. Lambda transforms incoming data before ingestion.

1. Build custom low-code web and mobile applications with Mendix to monitor and control IoT devices.

1. [AWS IoT Events](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/internet-of-things-services.html#aws-iot-events) detects changes and anomalies. It triggers notifications through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS).

1. Use Amazon Data Firehose to ingest data into a data lake on [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) performs extract, transform, and load (ETL) jobs and builds the data catalog.

1. AWS IoT SiteWise models and stores data from equipment for large-scale deployments.

   Use [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/) to visualize data on near real-time dashboards.

1. Use curated data from the data lake with AI and ML services. Use Amazon SageMaker AI, [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/), and [Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/) for predictive health analysis.

1. [Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/) stores time series data optimized for fast analytical queries.

1. Configure global data exchange between LOGO\! devices through AWS IoT Core.

1. Custom Alexa skills let users control input and output variables in LOGO\! with voice commands.

## Further reading
<a name="slogo-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Industrial Data Platform on AWS](../industrial-data-platform/industrial-data-platform.html)

## Diagram history
<a name="slogo-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#slogo-diagram-history) | Reference architecture diagram first published. | September 27, 2021 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.