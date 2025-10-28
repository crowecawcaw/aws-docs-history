# Best practice 1.1 – Validate the data quality of source systems before transferring data for analytics

Data quality can have an intrinsic impact on the success or
failure of your organization’s data analytics projects. To
avoid committing significant resources to process potentially
poor-quality data, your organization should understand the
quality of the source data, and monitor the changes to data
quality throughout the data pipeline.

Data source validation can often be performed quickly on a
subset of the latest data range to look for data defects.
Such defects include missing values, anomalous data, or
wrong data types that could fail the analytics job
completion or lead to completion of the job with inaccurate
results.

For more details refer to following document:

- AWS Blog:
  [How
  to Architect Data Quality on the AWS Cloud](https://aws.amazon.com/blogs/industries/how-to-architect-data-quality-on-the-aws-cloud/ "https://aws.amazon.com/blogs/industries/how-to-architect-data-quality-on-the-aws-cloud/")
- AWS Blog: [Getting started with AWS Glue Data Quality from the AWS Glue Data Catalog](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/ "https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-from-the-aws-glue-data-catalog/")

## Suggestion 1.1.1 – Implement data quality validation mechanisms

The critical attributes of data quality that should be measured and tracked
through your environment are completeness, accuracy, and uniqueness. Validating and
measuring your data quality using metrics is important to build trust in your data, which
increases data adoption throughout your organization.

For more details, refer to the following information:

- AWS Big Data Blog: [Set up advanced rules to validate quality of multiple datasets with AWS Glue Data
  Quality](https://aws.amazon.com/blogs/big-data/set-up-advanced-rules-to-validate-quality-of-multiple-datasets-with-aws-glue-data-quality/ "https://aws.amazon.com/blogs/big-data/set-up-advanced-rules-to-validate-quality-of-multiple-datasets-with-aws-glue-data-quality/")
- AWS Big Data Blog: [Getting started with AWS Glue Data Quality for ETL Pipelines](https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-for-etl-pipelines/ "https://aws.amazon.com/blogs/big-data/getting-started-with-aws-glue-data-quality-for-etl-pipelines/")
- AWS Big Data Blog: [Set up alerts and orchestrate data quality rules with AWS Glue Data Quality](https://aws.amazon.com/blogs/big-data/set-up-alerts-and-orchestrate-data-quality-rules-with-aws-glue-data-quality/ "https://aws.amazon.com/blogs/big-data/set-up-alerts-and-orchestrate-data-quality-rules-with-aws-glue-data-quality/")
- AWS Big Data Blog:
  [Enforce
  customized data quality rules in AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/enforce-customized-data-quality-rules-in-aws-glue-databrew/ "https://aws.amazon.com/blogs/big-data/enforce-customized-data-quality-rules-in-aws-glue-databrew/").
- AWS Big Data Blog:
  [Build
  a data quality score card using AWS Glue DataBrew,
  Amazon Athena, and Quick Suite](https://aws.amazon.com/blogs/big-data/build-a-data-quality-score-card-using-aws-glue-databrew-amazon-athena-and-amazon-quicksight/ "https://aws.amazon.com/blogs/big-data/build-a-data-quality-score-card-using-aws-glue-databrew-amazon-athena-and-amazon-quicksight/").

## Suggestion 1.1.2 – Notify stakeholders and use business logic to determine how to remediate data that is not valid

Alerts and notifications play a crucial role in maintaining data quality because they facilitate prompt and efficient responses to any data quality issues that may arise within a dataset. By establishing and configuring alerts and notifications, you can actively monitor data quality and receive timely alerts when data quality issues are identified. This proactive approach helps mitigate the risk of making decisions based on inaccurate information.

It’s usually more efficient to impute missing values, but in
other cases it’s more efficient to block processing until
the data quality issue can be resolved at source.

## Suggestion 1.1.3 – Score and share the quality of your datasets

To improve the ongoing trust in data quality and adoption
of your organization’s datasets, consider creating a data
quality matrix that can be accessed by the relevant teams
advertising the quality score of your datasets and
potential issues with the data. This information can be
incorporated in your Data Catalog.
