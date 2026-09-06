

# Predict Vessel Time of Arrival at Berth
<a name="predict-vessel-time-of-arrival"></a>

Publication date: **July 16, 2020 ([Diagram history](#vessel-history))**

With this architecture, you can predict vessel time of arrival at berth. Accurate predictions help you coordinate cargo operations and reduce idle time. The solution uses [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for machine learning (ML) model training and inference, [Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/) for real-time streaming, and [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) as the data lake.

## Vessel arrival prediction diagram
<a name="vessel-diagram"></a>

![Reference architecture diagram showing how to predict vessel arrival times by using SageMaker AI, Amazon Kinesis, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/predict-vessel-time-of-arrival/images/predict-vessel-time-of-arrival.png)


The following steps describe the data pipeline and ML workflow for this architecture:

1. Build a low-latency data pipeline from multiple data sources. Use AWS managed networking and data synchronization services. Stream and transform live data in real time with Amazon Kinesis.

1. Store all data in a single data lake on Amazon S3. Prepare data for ML processing with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/). Store SageMaker AI ML models and outputs in dedicated Amazon S3 buckets. Use Amazon S3 Intelligent-Tiering for cost-effective scalability.

1. Orchestrate SageMaker AI capabilities with a manual or automated workflow. Train, evaluate, optimize, deploy, and test the ML model. Expose the model as an API for real-time or batch predictions.

1. Send real-time push notifications when SageMaker AI detects possible vessel delays. Use a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function with SageMaker AI endpoint integration and Amazon Kinesis to raise alarms.

1. Import predictions to enrich your [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/) data warehouse. Visualize reports by using [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) to discover trends and implement corrective actions.

## Further reading
<a name="vessel-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="vessel-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#vessel-history) | Reference architecture diagram first published. | July 16, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.