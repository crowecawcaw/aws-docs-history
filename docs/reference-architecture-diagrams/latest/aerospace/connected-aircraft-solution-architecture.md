

# Connected Aircraft Solution Architecture
<a name="connected-aircraft-solution-architecture"></a>

Publication date: **September 22, 2022 ([Diagram history](diagram-history.md))**

This reference architecture shows how you can onboard flight data collection for fleet-wide analytics and predictive maintenance using AWS IoT Greengrass, Amazon S3, Amazon Managed Service for Apache Flink, and Amazon SageMaker AI.

## Connected Aircraft Solution Architecture diagram
<a name="connected-aircraft-solution-architecture-diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to onboard flight data collection for fleet-wide analytics and predictive maintenance.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/aerospace/images/connected-aircraft-solution-architecture.png)


1. Flight (avionics) and telemetry (sensor) data is collected by [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/), running on the flight-data acquisition unit on board. 

1. Near real-time events are anonymized and sent to Flight Operations on the ground. Flight data is offloaded to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) with aircraft at the gate and analyzed by the Flight Operations Team for fuel burn optimization, fault analysis, and other use cases. 

1. Engine flight data is processed and analyzed with [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/) for engine health maintenance and the Flight Operations Team notified of any anomalies. 

1. Anonymized flight and fault data is aggregated using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) and stored in an Amazon S3 data lake. 

1. Models trained from aggregated flight and fault data are deployed to AWS IoT Greengrass on the aircraft for Machine Learning inference driving predictive maintenance. 

1. App developers build new digital solutions for the connected ecosystem using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and Athena. 

1. Anonymized data is offered to third-party developers on a subscription basis with [AWS Data Exchange](https://docs.aws.amazon.com/data-exchange/latest/userguide/). 

1. Fleet–wide analytics is performed by the Engine Health Management team by querying processed flight data using [Amazon Quick](https://docs.aws.amazon.com/quick/latest/userguide/) and Athena. 

## Further reading
<a name="connected-aircraft-solution-architecture-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 