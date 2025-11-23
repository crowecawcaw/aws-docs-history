# MLPERF06-BP03 Evaluate data drift

Data drift can impact the performance of your machine learning
models, leading to inaccurate predictions and diminished business
value. By implementing effective monitoring and detection
strategies, you can identify when your models are no longer
performing optimally due to changes in the underlying data patterns.

**Desired outcome:** You can detect
and mitigate data drift in your machine learning models, providing
continued accuracy and reliability over time. By implementing model
monitoring capabilities, you gain visibility into changes in data
distributions and model performance, allowing for timely
interventions and retraining when necessary.

**Common anti-patterns:**

- Deploying models without drift monitoring mechanisms.
- Ignoring gradual changes in input data distribution until model
  performance deteriorates.
- Assuming that a model trained on historical data will remain
  accurate indefinitely.
- Manually checking model performance at arbitrary intervals
  rather than implementing continuous monitoring.
- Retraining models on fixed schedules without considering actual
  data drift patterns.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation before it
  impacts business outcomes.
- Increased trust in ML model predictions through continuous
  quality assurance.
- Improved model lifecycle management with data-driven retraining
  decisions.
- Reduced operational risks associated with inaccurate
  predictions.
- Enhanced ability to detect and mitigate bias in ML models over
  time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data drift occurs when the statistical properties of model inputs
change over time, causing discrepancies between training data and
production data. This can happen gradually due to evolving user
behaviors, market conditions, or abrupt changes like economic
shifts. When your model encounters data drift, it's essentially
making predictions on data distributions it wasn't trained on,
which can lead to decreased accuracy and potentially harmful
business decisions.

Avoid deploying models without drift monitoring mechanisms. Many
organizations ignore gradual changes in input data distribution
until model performance deteriorates, assume that a model trained
on historical data will remain accurate indefinitely, and manually
check model performance at arbitrary intervals rather than
implementing continuous monitoring.

Implementing a robust data drift monitoring strategy assists you
in maintaining high-performing models by identifying when
retraining becomes necessary. Rather than retraining models on
arbitrary schedules, you can make data-driven decisions based on
actual changes in your data distributions and model performance
metrics. This approach verifies that you're optimizing both model
performance and resource utilization.

Amazon SageMaker AI provides comprehensive tools to monitor your ML
models in production environments, allowing you to detect data
drift, concept drift, and bias. By setting up automated monitoring
pipelines, you can receive alerts when your models require
attention, enabling proactive management of your ML systems.

### Implementation steps

1. **Set up baseline data for
   monitoring**. Establish a reference dataset that
   represents your model's expected input and output
   distributions. This baseline will be used to compare against
   your production data to detect drift. Use the training data
   or a representative subset that performed well during model
   validation.
2. **Configure SageMaker AI Model
   Monitor**. Use
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to automatically detect
   deviations in your model's data quality and performance
   metrics. SageMaker AI Model Monitor can be set up to run on a
   schedule, analyzing incoming production data and comparing
   it to your baseline.
3. **Define data quality and drift
   metrics**. Determine which statistical metrics are
   most relevant for detecting drift in your use case.
   SageMaker AI Model Monitor supports various statistical
   measures like KL divergence, Jensen-Shannon divergence, and
   population stability index to quantify differences between
   distributions.
4. **Establish threshold
   values**. Set appropriate threshold values for your
   metrics that, when exceeded, will initiate alerts. These
   thresholds should balance sensitivity to meaningful changes
   while avoiding false alarms from minor variations.
5. **Create automated monitoring
   schedules**. Configure SageMaker AI Model Monitor to
   run analysis jobs at regular intervals that match your
   business requirements. For critical models, consider more
   frequent monitoring schedules.
6. **Implement bias detection**.
   Use
   [Amazon SageMaker AI Clarify](../../../sagemaker/latest/dg/clarify-detect-post-training-bias.md "../../../sagemaker/latest/dg/clarify-detect-post-training-bias.md") to detect bias in your ML models
   both pre-training and during production. SageMaker AI Clarify
   can identify if your model is developing biases over time as
   the data distribution changes.
7. **Set up alert mechanisms**.
   Configure Amazon CloudWatch alarms to notify appropriate
   stakeholders when data drift exceeds your defined
   thresholds. Integrate these alerts with your team's
   communication tools for timely responses.
8. **Develop a retraining
   strategy**. Establish clear criteria for when to
   retrain models based on drift detection results. This should
   include considerations for data collection, feature
   engineering updates, and model revalidation.
9. **Implement automated retraining
   pipelines**. Create SageMaker AI pipelines that can be
   run automatically when drift exceeds critical thresholds,
   streamlining the retraining process and minimizing the time
   models operate with degraded performance.
10. **Document drift patterns and
    interventions**. Maintain records of detected drift
    incidents, their causes, and the effectiveness of
    interventions. This documentation builds institutional
    knowledge that can improve future model development and
    monitoring strategies.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Model
  Explainability](../../../sagemaker/latest/dg/clarify-model-explainability.md "../../../sagemaker/latest/dg/clarify-model-explainability.md")
- [Detecting
  bias after training](../../../sagemaker/latest/dg/clarify-detect-post-training-bias.md "../../../sagemaker/latest/dg/clarify-detect-post-training-bias.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
  of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/ "https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/")
- [Detecting
  data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/ "https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/")

**Related videos:**

- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

**Related examples:**

- [Amazon SageMaker AI Clarify](https://github.com/aws/amazon-sagemaker-clarify "https://github.com/aws/amazon-sagemaker-clarify")
- [Amazon SageMaker AI Model Monitor examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor")
