# MLOE-10: Profile data to improve quality

Profile data to use data characteristics like distribution,
descriptive statistics, data types, and data patterns. Review
source data for content and quality. Filter out or correct any
data not passing the reviews. This will contribute to quality
improvement.

## Implementation plan

- Use the built-in data preparation capability of Amazon SageMaker AI Studio Notebook - This allows you to visually
  review data characteristics and remediate data-quality
  problems directly in your notebook environment. When you
  display a data frame (that is, a tabular representation of
  data) in your notebook, Amazon SageMaker AI Studio Notebook
  automatically generates charts to help users identify
  data-quality issues and suggests data transformations to
  help fix common problems. After you select a data
  transformation, Amazon SageMaker AI Studio Notebook generates
  the corresponding code within the notebook so that it can
  be repeatedly applied every time the notebook is run.
- **Use Amazon SageMaker AI Data
  Wrangler** - Import, prepare, transform,
  visualize, and analyze data with
  [SageMaker AI
  Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/"). You can integrate Data Wrangler into
  your ML workflows to simplify and streamline data
  pre-processing and feature engineering with little to no
  coding. You can also add your own Python scripts and
  transformations to customize your data preparation
  workflow. Import data from
  [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"),
  [Amazon Redshift](https://aws.amazon.com/redshift/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/redshift/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc"), or other data sources, and then query the
  data using
  [Amazon](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/")
  [Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/").
  Use Data Wrangler to create sophisticated machine learning
  data preparation workflows with built-in and custom data
  transformations and analysis features. These features
  include feature target leakage and quick modeling.
- **Create an automatic data profile
  and a reporting system** - Use
  [AWS Glue Crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") to crawl the data sources and create a
  data schema. Use
  [AWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md") to list all the tables and
  schemas. Use
  [Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc "https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc") for serverless SQL querying to constantly
  profile data and then use
  [Amazon](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
  [QuickSight](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/")
  dashboards for visualization of the data.
- **Create a baseline dataset with
  SageMaker AI Model Monitor** – The training dataset
  used to train the model is usually a good baseline
  dataset. The training dataset data schema and the
  inference dataset schema should exactly match (the number
  and order of the features).

## Documents

- [Amazon SageMaker AI Notebooks](https://aws.amazon.com/sagemaker/notebooks/ "https://aws.amazon.com/sagemaker/notebooks/")
- [Data
  Wrangler – Getting Started](../../../sagemaker/latest/dg/data-wrangler-getting-started.md "../../../sagemaker/latest/dg/data-wrangler-getting-started.md")
- [SageMaker AI
  Model Monitor – Create baseline](../../../sagemaker/latest/dg/model-monitor-create-baseline.md "../../../sagemaker/latest/dg/model-monitor-create-baseline.md")

## Blogs

- [Next Generation SageMaker
  Notebooks – Now with Built-in Data Preparation, Real-Time Collaboration,
  and Notebook Automation](https://aws.amazon.com/blogs/aws/next-generation-sagemaker-notebooks-now-with-built-in-data-preparation-real-time-collaboration-and-notebook-automation/ "https://aws.amazon.com/blogs/aws/next-generation-sagemaker-notebooks-now-with-built-in-data-preparation-real-time-collaboration-and-notebook-automation/")
- [Introducing
  Amazon SageMaker AI Data Wrangler, a Visual Interface to Prepare
  Data for Machine Learning](https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-data-wrangler-a-visual-interface-to-prepare-data-for-machine-learning/ "https://aws.amazon.com/blogs/aws/introducing-amazon-sagemaker-data-wrangler-a-visual-interface-to-prepare-data-for-machine-learning/")
- [Exploratory
  data analysis, feature engineering, and operationalizing your
  data flow into your ML with Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/exploratory-data-analysis-feature-engineering-and-operationalizing-your-data-flow-into-your-ml-pipeline-with-amazon-sagemaker-data-wrangler/")
- [Prepare
  data for predicting credit risk using Amazon SageMaker AI Data
  Wrangler and Amazon SageMaker AI Clarify](https://aws.amazon.com/blogs/machine-learning/prepare-data-for-predicting-credit-risk-using-amazon-sagemaker-data-wrangler-and-amazon-sagemaker-clarify/ "https://aws.amazon.com/blogs/machine-learning/prepare-data-for-predicting-credit-risk-using-amazon-sagemaker-data-wrangler-and-amazon-sagemaker-clarify/")
- [Prepare
  data from Snowflake for machine learning with Amazon SageMaker AI
  Data Wrangler](https://aws.amazon.com/blogs/machine-learning/prepare-data-from-snowflake-for-machine-learning-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/prepare-data-from-snowflake-for-machine-learning-with-amazon-sagemaker-data-wrangler/")
- [Develop
  and deploy ML models using Amazon SageMaker AI Data Wrangler and
  Amazon SageMaker AI Autopilot](https://aws.amazon.com/blogs/machine-learning/develop-and-deploy-ml-models-without-writing-any-code-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/develop-and-deploy-ml-models-without-writing-any-code-using-amazon-sagemaker/")
- [Build
  an automatic data profiling and reporting solution with Amazon EMR, AWS Glue, and Amazon QuickSight](https://aws.amazon.com/blogs/big-data/build-an-automatic-data-profiling-and-reporting-solution-with-amazon-emr-aws-glue-and-amazon-quicksight "https://aws.amazon.com/blogs/big-data/build-an-automatic-data-profiling-and-reporting-solution-with-amazon-emr-aws-glue-and-amazon-quicksight")
- [Prepare
  image data with Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/prepare-image-data-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/prepare-image-data-with-amazon-sagemaker-data-wrangler/")
