

# Real-Time Fraud Detection Powered by Redis Enterprise Cloud
<a name="realtime-fraud-detection-redis"></a>

Publication date: **May 5, 2022 ([Diagram history](#fraud-redis-history))**

With this architecture, you can detect fraud in real time by using Redis Enterprise Cloud on AWS as both a primary database and an online feature store. The solution uses [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for machine learning (ML) model inference, [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/) for event capture, and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) for processing.

## Real-Time fraud detection diagram
<a name="fraud-redis-diagram"></a>

![Reference architecture diagram showing how to detect fraud in real time by using Redis Enterprise Cloud, SageMaker AI, Amazon Kinesis Data Streams, and Lambda.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/realtime-fraud-detection-redis/images/realtime-fraud-detection-redis.png)


The following steps describe the data flow and ML inference pipeline for this architecture:

1. Store historical datasets of credit card transactions in an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket.

1. Train different ML models by using an SageMaker AI notebook instance on the historical datasets.

1. Process transactions from the historical datasets by using a Lambda function. Invoke two SageMaker AI endpoints that assign anomaly scores and classification scores to incoming data points.

1. Invoke the [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) REST API for predictions by using signed HTTP requests from end users (mobile and web clients).

1. Capture real-time event data by using Amazon Kinesis Data Streams.

1. Read the stream by using a Lambda function. Persist transactional data to RediSearch and RedisJSON-enabled Redis Enterprise Cloud database.

1. Use Redis Enterprise Cloud as a feature store for the Lambda function. No Redis modules are required for this functionality.

1. Persist the prediction results to the Redis Enterprise Cloud database. (Optional) Store results with transactional details to a time-series database for data visualizations by using [Amazon Managed Service for Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/).

1. (Optional) Pass prediction results through Amazon Data Firehose to persist data to an Amazon S3 bucket. Use [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/developerguide/welcome.html) to consume this data for visualizations and analytics.

## Further reading
<a name="fraud-redis-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="fraud-redis-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#fraud-redis-history) | Reference architecture diagram first published. | May 5, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.