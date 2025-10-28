# MLPER-04: Use a modern data architecture

Get the best insights from exponentially growing data using a
modern data architecture. This architecture enables easy
movement of data between a data lake and purpose-built stores
including a data warehouse, relational databases, non-relational
databases, ML and big data processing, and log analytics. A data
lake provides a single place to run analytics across mixed data
structures collected from disparate sources. Purpose-built
analytics services provide the speed required for specific use
cases like real-time dashboards and log analytics.

## Implementation plan

- **Unify data governance and
  access** - Integrate a data lake, a data
  warehouse, and purpose-built stores. This will enable
  unified governance and easy data movement. With a
  [Modern
  Data Architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/ "https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/"), you can store data in a
  data lake and use data services around it. Use
  [AWS Lake Formation](../../../lake-formation/latest/dg/what-is-lake-formation.md "../../../lake-formation/latest/dg/what-is-lake-formation.md") to build a scalable and secure data
  lake. Build a high-speed analytic layer with purpose-built
  services, such as
  [Amazon Redshift](https://aws.amazon.com/redshift/lake-house-architecture/ "https://aws.amazon.com/redshift/lake-house-architecture/"),
  [Amazon Kinesis](https://aws.amazon.com/kinesis/ "https://aws.amazon.com/kinesis/"), and
  [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc"). Integrate data across services and data
  stores with
  [AWS Glue](https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/glue/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc"). Apply governance policies to manage security,
  access control, and audit trails across all the data
  stores using
  [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/").

## Documents

- [Data
  Lake on AWS](https://aws.amazon.com/solutions/implementations/data-lake-solution/ "https://aws.amazon.com/solutions/implementations/data-lake-solution/")
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/lake-formation/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc")
- [Derive
  Insights from Modern Data](../../../whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.md "../../../whitepapers/latest/derive-insights-from-aws-modern-data/derive-insights-from-aws-modern-data.md")

## Blogs

- [Build
  a Lake House Architecture on AWS](https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/ "https://aws.amazon.com/blogs/big-data/build-a-lake-house-architecture-on-aws/")
- [Moving
  from notebooks to automated ML pipelines using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/ "https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/")
- [Data
  preprocessing for machine learning on Amazon EMR made easy
  with AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/data-preprocessing-for-machine-learning-on-amazon-emr-made-easy-with-aws-glue-databrew/ "https://aws.amazon.com/blogs/big-data/data-preprocessing-for-machine-learning-on-amazon-emr-made-easy-with-aws-glue-databrew/")

## Videos

- [Build
  and Govern Your Data Lakes with AWS Glue](https://www.youtube.com/watch?v=JsNR8uBVSiA "https://www.youtube.com/watch?v=JsNR8uBVSiA")
- [The
  lake house approach to data warehousing with Amazon Redshift](https://www.youtube.com/watch?v=35wXL0Q1Dcc "https://www.youtube.com/watch?v=35wXL0Q1Dcc")
