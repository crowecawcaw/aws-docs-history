

# Well Log Facies Classification Using Machine Learning
<a name="well-log-facies-classification"></a>

Publication date: **September 16, 2022 ([Diagram history](#diagram-history))**

This solution incorporates [well logs](https://en.wikipedia.org/wiki/Well_logging) (borehole measurements) from the corporate data center and applies a low-code ML model on the data by using SageMaker AI Autopilot to obtain a [facies](https://en.wikipedia.org/wiki/Facies) (rock type) classification at each measured depth.

## Well Log Facies Classification Using Machine Learning
<a name="diagram1"></a>

![Architecture diagram showing well log facies classification by using SageMaker AI Autopilot.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/well-log-facies-classification/images/well-log-facies-classification.png)


The following steps describe the architecture:

1. Use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html) to transfer well logs stored in the corporate data center to the AWS Cloud.

1. Use an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket to store all input data for ML models.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) to prepare, build, train, and deploy ML models. SageMaker AI Notebook is a fully managed notebook instance pre-loaded with useful libraries. Use SageMaker AI Autopilot to automatically train ML models. Deploy trained models to SageMaker AI inference endpoints.

1. Use Amazon S3 buckets to store all data and results for ML models.

1. Use [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) to generate dashboards for end users. Quick uses the predictions from ML models stored in Amazon S3 through [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html).

1. Geoscientists can download the ML-classified facies at each well log depth from the Amazon S3 bucket. They can integrate the results with their geoscientific workflow to improve business decisions.

1. Use [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) for fine-grained access control across all services. [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) collects monitoring and operational data. [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) provides an interface to visualize and manage AWS costs.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon SageMaker AI product page](https://aws.amazon.com/sagemaker/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | September 16, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.