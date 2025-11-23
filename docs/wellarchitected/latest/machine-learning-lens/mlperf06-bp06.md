# MLPERF06-BP06 Review for updated data and features for

retraining

Establishing a framework to regularly review and update your machine
learning model's data and features is essential for maintaining
model accuracy. As business environments evolve, new data patterns
emerge that can impact your model's performance. By systematically
reviewing your data and features at appropriate intervals, you can
keep your models accurate and reliable.

**Desired outcome:** You establish a
systematic approach to monitor data changes, explore new features,
and incorporate updated data into your models. Through regular data
exploration and feature engineering, you maintain model accuracy
even as underlying data patterns evolve. This creates a proactive
rather than reactive approach to model maintenance and verifies that
your ML solutions consistently deliver business value.

**Common anti-patterns:**

- Assuming that data patterns remain stable over time.
- Retraining models only when performance degrades.
- Failing to explore new potential features as business evolves.
- Using the same feature engineering approach regardless of
  changing data characteristics.
- Not establishing regular review schedules for data and feature
  updates.

**Benefits of establishing this best
practice:**

- Improved model accuracy through updated training data and
  features.
- Early detection of data drift and proactive model updates.
- Continuous discovery of new, potentially valuable features.
- Consistent model performance despite changing business
  conditions.
- Extended model lifecycle and reduced need for complete rebuilds.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data is the foundation of a machine learning model, and its
characteristics can change over time due to various factors such
as seasonal variations, market shifts, or changes in customer
behavior. Without a framework to regularly review and update your
data and features, models can gradually become less accurate as
they fail to account for these changes.

Avoid assuming that data patterns remain stable over time. Many
organizations retrain models only when performance degrades, fail
to explore new potential features as their business evolves, and
use the same feature engineering approach regardless of changing
data characteristics.

To implement this practice effectively, you need to understand the
volatility of your business environment and establish appropriate
review intervals. For example, retail businesses might need more
frequent reviews during holiday seasons when consumer behavior
changes rapidly. You also need tools to efficiently explore data,
identify new patterns, and engineer features that capture these
insights.

Amazon SageMaker AI provides comprehensive capabilities for data
preparation, feature engineering, and model monitoring. By using
these tools, you can create an efficient pipeline for regularly
reviewing and updating your model's data and features, providing
continued accuracy and relevance.

### Implementation steps

1. **Assess data volatility in your
   business environment**. Analyze how quickly your
   business data changes by examining historical data patterns
   and identifying seasonal trends, market shifts, or other
   factors that affect your data. This assessment can determine
   how frequently you need to review your model's data and
   features.
2. **Establish a review
   schedule**. Based on your data volatility
   assessment, create a calendar for regular data and feature
   reviews. For highly volatile environments, you may need
   monthly reviews, while more stable contexts might require
   quarterly or biannual reviews.
3. **Set up data monitoring**.
   Implement
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to continuously track data
   drift by comparing production data against your model's
   training data. Configure alerts when deviations occur to run
   expedited reviews.
4. **Create a data exploration workflow
   with Amazon SageMaker AI Canvas**. Use
   [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas-data-prep.md "../../../sagemaker/latest/dg/canvas-data-prep.md") to build data exploration workflows.
   The unified SageMaker AI Studio environment provides seamless
   integration with S3, Redshift, and EMR for comprehensive
   data exploration, engineering, training, and deployment
   workflows. Canvas now includes enhanced no/low-code ML tools
   with templates, automation, and wizards that enable
   non-engineering users to train custom models for verticals
   like sales, fraud, and demand with minimal technical
   expertise. These workflows should include data
   visualizations, statistical analyses, and data quality
   assessments.
5. **Implement feature engineering
   processes**. Develop standardized feature
   engineering pipelines in SageMaker AI Data Wrangler that can
   transform raw data into model features. Include steps to
   identify potential new features during each review cycle.
6. **Integrate with SageMaker AI Feature
   Store**. Store engineered features in
   [Amazon SageMaker AI Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md") to maintain feature
   consistency between training and inference. This creates a
   single source of truth for features and simplifies
   retraining with updated data.
7. **Establish an evaluation
   framework**. Create a systematic approach to
   compare model performance using original features versus
   updated or new features. This quantifies the impact of
   feature changes and supports data-driven decisions about
   model updates.
8. **Form a cross-functional review
   team**. Assemble a team including data scientists,
   domain experts, and business stakeholders who can
   collectively evaluate data changes, validate new features,
   and authorize model retraining when necessary.
9. **Document changes and maintain
   version control**. Track changes to data sources,
   feature definitions, and transformation logic using version
   control systems. This creates an audit trail and supports
   reproducibility.
10. **Automate the retraining
    pipeline**. Use
    [Amazon SageMaker AI Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md") to create automated workflows
    that can retrain models with updated data and features when
    approved by the review team.

## Resources

**Related documents:**

- [Automate
  data preparation with Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas-data-export.md "../../../sagemaker/latest/dg/canvas-data-export.md")
- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")
- [Pipelines](../../../sagemaker/latest/dg/pipelines.md "../../../sagemaker/latest/dg/pipelines.md")
- [No-code
  data preparation for time series forecasting using Amazon SageMaker AI Canvas](https://aws.amazon.com/blogs/machine-learning/no-code-data-preparation-for-time-series-forecasting-using-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/no-code-data-preparation-for-time-series-forecasting-using-amazon-sagemaker-canvas/")

**Related videos:**

- [Introducing
  Amazon SageMaker AI Canvas](https://www.youtube.com/watch?v=Tb4NTq9n_Hc "https://www.youtube.com/watch?v=Tb4NTq9n_Hc")
- [Automating
  Machine Learning Workflows with SageMaker AI Pipelines](https://aws.amazon.com/awstv/watch/f2ed03696ea/ "https://aws.amazon.com/awstv/watch/f2ed03696ea/")
