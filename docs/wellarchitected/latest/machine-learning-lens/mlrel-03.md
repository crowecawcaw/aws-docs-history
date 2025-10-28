# MLREL-03: Use a data catalog

Process data across multiple data stores using data catalog
technology. An advanced data catalog service can enable ETL
process integration. This approach enables more reliability and
efficiency.

## Implementation plan

- **Use AWS Glue Data Catalog** -
  AWS Glue Data Catalog provides a way to track the data
  assets that have been loaded into your ML workload. Data
  catalogs also describe how data is transformed as it is
  loaded into the data lake and data warehouse. AWS Glue is
  a fully managed ETL (extract, transform, and load)
  service. It enables a simple and cost-effective approach to
  categorize your data, clean it, enrich it, and move it
  reliably between various data stores and data streams. AWS Glue consists of a central metadata repository known as
  the AWS Glue Data Catalog. It also has an ETL engine that
  automatically generates Python or Scala code. With a
  flexible scheduler, AWS Glue handles dependency resolution,
  job monitoring, and retries.

## Documents

- [Data
  Cataloging](../../../whitepapers/latest/building-data-lakes/data-cataloging.md "../../../whitepapers/latest/building-data-lakes/data-cataloging.md")
- [Populating
  the AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md")

## Blogs

- [Moving
  from notebooks to automated ML pipelines using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/ "https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/")
- [How
  Genworth built a serverless ML pipeline on AWS using
  Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/ "https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/")

## Videos

- [Getting
  Started with AWS Glue Data Catalog](https://www.youtube.com/watch?v=qNojanBn1NY "https://www.youtube.com/watch?v=qNojanBn1NY")
- [AWS re:Invent 2018: How Bill.com Uses Amazon SageMaker AI &
  AWS Glue to Enable Machine Learning -](https://www.youtube.com/watch?v=2WkxDdVkBNg "https://www.youtube.com/watch?v=2WkxDdVkBNg")
  [STP10](https://www.youtube.com/watch?v=2WkxDdVkBNg "https://www.youtube.com/watch?v=2WkxDdVkBNg")
- [AWS re:Invent 2018: Build and Govern Your Data Lakes with AWS Glue (ANT309)](https://www.youtube.com/watch?v=JsNR8uBVSiA "https://www.youtube.com/watch?v=JsNR8uBVSiA")

## Examples

- [Explaining
  Credit Decisions with Amazon SageMaker AI](https://github.com/awslabs/sagemaker-explaining-credit-decisions "https://github.com/awslabs/sagemaker-explaining-credit-decisions")
- [How
  to build an end-to-end Machine Learning pipeline using AWS Glue, Amazon S3, Amazon](https://github.com/aws-samples/amazon-sagemaker-predict-accessibility "https://github.com/aws-samples/amazon-sagemaker-predict-accessibility")
  [SageMaker AI
  and Amazon Athena.](https://github.com/aws-samples/amazon-sagemaker-predict-accessibility "https://github.com/aws-samples/amazon-sagemaker-predict-accessibility")
