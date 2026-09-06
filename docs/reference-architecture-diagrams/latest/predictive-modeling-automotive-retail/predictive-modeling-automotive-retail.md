

# Predictive Modeling for Automotive Retail
<a name="predictive-modeling-automotive-retail"></a>

Publication date: **September 15, 2021 ([Diagram history](#auto-predict-history))**

With this architecture, you can predict fine-grained return on investment (ROI) for automotive sales incentives. The solution uses [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for model training and inference, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) for data preprocessing, and [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) for pipeline orchestration.

## Predictive modeling for automotive retail diagram
<a name="auto-predict-diagram"></a>

![Reference architecture diagram showing how to predict ROI for automotive sales incentives by using SageMaker AI, AWS Glue, Step Functions, and Lake Formation.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/predictive-modeling-automotive-retail/images/predictive-modeling-automotive-retail.png)


The following steps describe the architecture:

1. Use a centralized data lake account to accelerate development of new use cases.

1. Strip personally identifiable information. Aggregate data to obfuscate dealer specifics and prevent bias for or against OEM dealers.

1. Use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) to replicate on-premises databases that are not available through a data lake account.

1. Preprocess data with AWS Glue PySpark Transforms and output the results into a primary table for model training.

1. Push the training input primary table from the data ingestion pipeline at regular intervals and store it in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. Trigger the model training pipeline when the primary table changes. The pipeline includes hyperparameter tuning, validation, and fit. Step Functions controls this pipeline by using AWS Deep Learning Containers.

1. Trigger a container build on model source commits. Store the container in [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/).

1. Store versioned model outputs in Amazon S3, including the training report and evaluation.

1. Use [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) to notify an administrator for review before triggering deployment with Step Functions.

1. Serve inference requests through [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/), and an SageMaker AI endpoint that uses the trained model container.

1. Build the inference dashboard by using [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/). Host static content on Amazon S3 and serve it through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/).

## Further reading
<a name="auto-predict-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="auto-predict-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#auto-predict-history) | Reference architecture diagram first published. | September 15, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.