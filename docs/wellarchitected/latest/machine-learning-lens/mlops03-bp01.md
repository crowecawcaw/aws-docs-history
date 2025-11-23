# MLOPS03-BP01 Profile data to improve quality

Data profiling is essential for understanding data characteristics
such as distribution, descriptive statistics, data types, and
patterns. By systematically reviewing source data for content and
quality, you can filter out or correct problematic data, leading to
significant quality improvements in your machine learning workflows.

**Desired outcome:** You gain
comprehensive insights into your data's characteristics, enabling
you to identify and remediate quality issues before they impact your
machine learning models. Through systematic profiling, you establish
a robust data preprocessing pipeline that provides high-quality,
consistent data flows to your ML models, resulting in more accurate
predictions and better business outcomes.

**Common anti-patterns:**

- Skipping data profiling and moving directly to model training.
- Manually reviewing data without automated profiling tools.
- Performing one-time data quality checks without continuous
  monitoring.
- Ignoring data distribution shifts between training and inference
  data.
- Failing to document data quality issues and their resolutions.

**Benefits of establishing this best
practice:**

- Improved model performance through higher quality training data.
- Earlier detection of data anomalies and inconsistencies.
- Enhanced understanding of data characteristics and limitations.
- Reduced time spent debugging model issues caused by data
  problems.
- More transparent and reproducible machine learning workflows.
- Increased stakeholder confidence in model outputs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data profiling is a critical step in the machine learning
workflow. By thoroughly examining your data before model training,
you gain valuable insights that improve data quality and
ultimately lead to better model performance. Data profiling
involves analyzing the statistical properties, distributions, and
patterns within your dataset to identify anomalies, missing
values, outliers, and other quality issues.

Effective data profiling requires both automated tools and human
judgment. While tools can quickly generate statistical summaries
and visualizations, subject matter experts should interpret these
findings to determine appropriate actions for data cleaning and
transformation. For instance, you might discover that a numerical
feature has an unexpected distribution that requires
normalization, or that categorical variables contain inconsistent
values requiring standardization.

Consider a retail company building a customer churn prediction
model. Through data profiling, they discover that 15% of customer
records have missing age values, 5% have impossibly high
transaction amounts, and several categorical fields contain
inconsistent formatting. By addressing these issues early, they
can significantly improve their model's performance.

### Implementation steps

1. **Set up Amazon SageMaker AI Unified
   Studio for visual data review**. Use
   [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/ "https://aws.amazon.com/sagemaker/unified-studio/") with enhanced collaborative
   features and team sharing capabilities to visually review
   data characteristics and remediate data-quality problems
   directly in your integrated environment. The unified
   solution provides improved debugging and monitoring
   capabilities for data processing workflows, automatically
   generating charts to identify data quality issues and
   suggesting transformations to fix common problems.
2. **Implement Amazon SageMaker AI Data
   Wrangler for comprehensive data preparation**.
   Import, prepare, transform, visualize, and analyze data with
   [SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/ "https://aws.amazon.com/sagemaker/data-wrangler/") with
   [Q
   integration for interactive analysis](../../../sagemaker/latest/dg/data-wrangler-q-integration.md "../../../sagemaker/latest/dg/data-wrangler-q-integration.md"). You can
   integrate Data Wrangler into your ML workflows to simplify
   and streamline data pre-processing and feature engineering
   with little to no coding. Import data from
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"),
   [Amazon Redshift](https://aws.amazon.com/redshift/ "https://aws.amazon.com/redshift/"), or other data sources, and then query the
   data using
   [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/"). Use Data Wrangler's built-in and custom data
   transformations and analysis features, including feature
   target leakage detection and quick modeling, to create
   sophisticated machine learning data preparation workflows.
3. **Build an automatic data profile and
   reporting system**. Use
   [AWS Glue Crawler](../../../glue/latest/dg/add-crawler.md "../../../glue/latest/dg/add-crawler.md") to crawl your data sources and
   automatically create a data schema. The crawler detects the
   schema of your data and registers tables in the
   [AWSAWS Glue Data Catalog](../../../glue/latest/dg/populate-data-catalog.md "../../../glue/latest/dg/populate-data-catalog.md"), providing a comprehensive listing
   of tables and schemas. Use
   [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") for serverless SQL querying to constantly
   profile your data, and create
   [Quick Suite](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") dashboards for data visualization and
   monitoring.
4. **Create a baseline dataset with
   SageMaker AI Model Monitor**. The training dataset
   used to train your model typically serves as a good baseline
   dataset. Verify that the training dataset schema and the
   inference dataset schema exactly match (the number and order
   of the features). With
   [SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor-create-baseline.md "../../../sagemaker/latest/dg/model-monitor-create-baseline.md"), you can automatically detect
   concept drift in deployed models by comparing production
   data against this baseline.
5. **Implement continuous data quality
   monitoring**. Set up automated checks that
   continuously monitor data quality metrics like completeness,
   uniqueness, consistency, and validity. Configure alerts to
   notify relevant stakeholders when data quality issues arise,
   enabling prompt intervention and resolution. Use
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to create dashboards and set up alerts for
   key data quality metrics.
6. **Document data profiling insights and
   transformations**. Maintain comprehensive
   documentation of data profiling findings, quality issues
   discovered, and the transformations applied to address them.
   This documentation promotes transparency, facilitates
   knowledge sharing across teams, and supports regulatory
   adherence in regulated industries.
7. **Use generative AI for enhanced data
   profiling**. Use large language models in
   [Amazon
   Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") or
   [Amazon
   Nova](https://aws.amazon.com/ai/generative-ai/nova/ "https://aws.amazon.com/ai/generative-ai/nova/") to automatically extract and enrich metadata,
   identify patterns in your data, and generate natural
   language summaries of data quality issues. Generative AI can
   analyze unstructured data fields and provide insights that
   traditional data profiling tools might miss, though you
   should validate AI-generated suggestions before
   implementation.

## Resources

**Related documents:**

- [Prepare
  ML Data with Amazon SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler.md "../../../sagemaker/latest/dg/data-wrangler.md")
- [Get
  Started with Data Wrangler](../../../sagemaker/latest/dg/data-wrangler-getting-started.md "../../../sagemaker/latest/dg/data-wrangler-getting-started.md")
- [Data
  quality](../../../sagemaker/latest/dg/model-monitor-data-quality.md "../../../sagemaker/latest/dg/model-monitor-data-quality.md")
- [Create
  a Baseline](../../../sagemaker/latest/dg/model-monitor-create-baseline.md "../../../sagemaker/latest/dg/model-monitor-create-baseline.md")
- [AWS Glue Data Quality](../../../glue/latest/dg/glue-data-quality.md "../../../glue/latest/dg/glue-data-quality.md")
- [Data
  discovery and cataloging in AWS Glue](../../../glue/latest/dg/catalog-and-crawler.md "../../../glue/latest/dg/catalog-and-crawler.md")
- [Amazon SageMaker AI notebooks](https://aws.amazon.com/sagemaker/notebooks/ "https://aws.amazon.com/sagemaker/notebooks/")
- [What
  is Amazon Athena?](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md")
- [What
  is Amazon Quick Suite?](../../../quicksight/latest/user/welcome.md "../../../quicksight/latest/user/welcome.md")
