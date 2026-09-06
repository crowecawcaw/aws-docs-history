

# Patient Outcome Prediction
<a name="patient-outcome-prediction"></a>

Publication date: **September 14, 2022 ([Diagram history](#pop-history))**

With this architecture, you can use machine learning (ML) on patient health data to train models that predict medical outcomes. The solution uses [AWS HealthLake](https://docs.aws.amazon.com/healthlake/latest/devguide/) to transform health data, [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to train and deploy custom prediction models, and [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/) to discover and protect sensitive data.

## Patient outcome prediction diagram
<a name="pop-diagram"></a>

![Reference architecture diagram showing how to predict patient outcomes by using AWS HealthLake, SageMaker AI, Amazon Macie, AWS Glue, and CloudFront.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/patient-outcome-prediction/images/patient-outcome-prediction.png)


The following steps describe the data flow and prediction pipeline for this architecture:

1. Access the Patient Outcome Prediction application and input your health data, such as medical records, insurance claims, lab reports, and doctor's notes, through AWS Transit Gateway.

1. Input your health data into AWS HealthLake, a HIPAA-eligible service that transforms health data to be more easily queried and ML-ingestible.

1. Run privacy-sensitive datasets through Amazon Macie with a series of [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) to discover and protect sensitive data.

1. Store your data from HealthLake and Macie in [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Process the data with [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), which transforms and prepares it for ingestion as training data into a custom SageMaker AI model.

1. Train custom SageMaker AI models to predict patient outcomes such as disease progression and hospital readmission probability. Create SageMaker AI model endpoints for inference.

1. Access the web client frontend to perform model inference through [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/).

1. Pick a SageMaker AI model endpoint to perform predictions by using a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function.

1. Explore model explainability by using a Lambda function that invokes SageMaker AI Clarify to examine potential bias in training data and trained models.

1. Record all Amazon VPC flow logs, API metrics, and AWS resource usage by using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/), [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/), and AWS CloudTrail for operational and cost monitoring.

## Further reading
<a name="pop-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="pop-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#pop-history) | Reference architecture diagram first published. | September 14, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.