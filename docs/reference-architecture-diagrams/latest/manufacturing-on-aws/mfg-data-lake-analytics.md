

# Data lake and analytics
<a name="mfg-data-lake-analytics"></a>

The data lake and analytics diagram shows how to process, analyze, and derive insights from manufacturing data.

![Data lake and analytics diagram showing processing and analysis of manufacturing data on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/manufacturing-on-aws/images/manufacturing-on-aws-ra-3.png)


1. Use Lake Formation or Amazon S3 for the data lake structure to store raw and processed manufacturing data.

1. Use Amazon Managed Service for Apache Flink for streaming analytics on real-time factory data.

1. Use Lambda for near real-time analytics and event-driven processing.

1. Use [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to build, train, and deploy ML models for predictive maintenance and quality.

1. Use [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) for large-scale data processing and transformation.

1. Use [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) for demand forecasting.

1. Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) for structured data warehousing and analytics.

1. Use [Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) with [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/) and Amazon Redshift for business intelligence (BI) dashboards.