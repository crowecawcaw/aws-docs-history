# MLOPS06-BP02 Enable model observability and tracking

Establish model monitoring mechanisms to identify and proactively
avoid inference issues. ML models can degrade in performance over
time due to drifts. Monitor metrics that are attributed to your
model's performance. For real time inference endpoints, measure the
operational health of the underlying compute resources hosting the
endpoint and the health of endpoint responses. Establish lineage to
trace hosted models back to versioned inputs and model artifacts for
analysis.

**Desired outcome:** You can
continuously monitor your machine learning models in production to
detect and avoid performance degradation over time. You have
mechanisms in place to track model lineage, identify various types
of drift, and receive alerts when models deviate from expected
behavior. Your monitoring solution provides clear visibility into
both the technical health of model endpoints and the business
performance of the models themselves, enabling you to maintain
high-quality predictions and make informed decisions about model
updates.

**Common anti-patterns:**

- Deploying models without monitoring capabilities.
- Failing to establish model lineage tracking for audit and
  governance.
- Not monitoring for data drift or concept drift in production
  models.
- Ignoring model bias and fairness considerations after
  deployment.
- Lacking documentation of model information and performance
  metrics.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Improved model governance and adherence through comprehensive
  documentation.
- Enhanced ability to explain model predictions and address bias
  concerns.
- Reduced operational risk through proactive monitoring of model
  health.
- Streamlined model updates and improvements based on real-world
  performance data.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model observability is critical for maintaining the reliability,
fairness, and performance of machine learning systems in
production. Without proper monitoring mechanisms, ML models can
silently degrade over time as the data they process begins to
differ from the data they were trained on, a phenomenon known as
drift.

You need to implement comprehensive monitoring across several
dimensions: data quality to check that inputs remain consistent
with training data, model quality to track performance metrics,
bias detection to verify fairness, and explainability to
understand model decisions. Additionally, model lineage tracking
can trace issues back to specific model versions, training
datasets, and hyperparameters.

Amazon SageMaker AI provides integrated tools that make implementing
these monitoring capabilities straightforward. SageMaker AI Model
Monitor can automatically detect deviations in your model's data
and performance characteristics, while SageMaker AI Clarify
identifies bias and explains predictions. By setting up proper
alerts, you can be notified when issues arise and take corrective
action before they impact your business.

Documentation is equally important for model governance. SageMaker AI
Model Cards provide a centralized location to store important
model information, including performance metrics, intended use
cases, and potential limitations.

### Implementation steps

1. **Set up Amazon SageMaker AI Model
   Monitor**. Configure
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") to automatically monitor the
   quality of your ML models in production. Create baseline
   statistics and constraints during model training, then
   monitor for deviations in production data. Set up the
   following types of monitoring:
   - Data quality monitoring to detect changes in data
     distributions
   - Model quality monitoring to track accuracy and other
     performance metrics
   - Bias drift monitoring to detect changes in model
     fairness
   - Feature attribution drift monitoring to track changes in
     feature importance

2. **Integrate with Amazon CloudWatch**. SageMaker AI Model Monitor automatically
   sends metrics to
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/"), allowing you to track usage statistics
   for your ML models. Set up CloudWatch dashboards to
   visualize key metrics and create alarms that go off when
   metrics exceed predefined thresholds. Configure
   notifications through Amazon SNS to alert relevant teams
   when issues are detected.
3. **Implement SageMaker AI Model
   Dashboard**. Use the
   [SageMaker AI
   Model Dashboard](../../../sagemaker/latest/dg/model-dashboard.md "../../../sagemaker/latest/dg/model-dashboard.md") to gain a centralized view of your
   models. From the SageMaker AI console, you can search, view,
   and explore your models in one place. Set up monitors to
   track the performance of models deployed on real-time
   inference endpoints and identify models that violate
   thresholds for data quality, model quality, bias, and
   explainability.
4. **Enable bias detection with SageMaker AI
   Clarify**. Deploy
   [SageMaker AI
   Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to identify various types of bias that can
   emerge during model training or when the model is in
   production. Configure both pre-training and post-training
   bias metrics to understand how your model's predictions
   affect different segments of your user base. Use Clarify's
   monitoring capabilities to detect bias drift in production
   models.
5. **Implement model
   explainability**. Configure SageMaker AI Clarify's
   feature attribution capabilities to explain how your models
   make predictions. This builds trust with stakeholders and
   can identify potential issues with model logic. Set up
   monitoring to detect when feature attribution patterns drift
   from baseline, which could indicate underlying problems with
   the model.
6. **Establish ML lineage
   tracking**. Implement
   [SageMaker AI
   ML Lineage Tracking](https://sagemaker.readthedocs.io/en/v2.77.0/workflows/lineage/ "https://sagemaker.readthedocs.io/en/v2.77.0/workflows/lineage/") to create and store information
   about each step in your machine learning workflow, from data
   preparation to model deployment. This creates a running
   history of your ML experiments and establishes model
   governance by tracking model lineage artifacts for auditing
   and adherence verification.
7. **Create Model Cards for
   documentation**. Use
   [Amazon SageMaker AI Model Cards](../../../sagemaker/latest/dg/model-cards.md "../../../sagemaker/latest/dg/model-cards.md") with enhanced documentation and
   governance capabilities to document critical information
   about your models in a single location. Include business
   requirements, key decisions, observations during
   development, performance goals, risk ratings, and evaluation
   results. This streamlines documentation throughout a model's
   lifecycle and supports approval workflows, registration, and
   audits.
8. **Implement shadow testing for model
   validation**. Before deploying new model versions
   to production, use
   [Amazon SageMaker AI Shadow Testing](../../../sagemaker/latest/dg/shadow-tests.md "../../../sagemaker/latest/dg/shadow-tests.md") to compare the performance
   of new models against production models using real-world
   inference request data. Configure SageMaker AI to route copies
   of production inference requests to the new model variant
   and generate dashboards displaying performance differences
   across key metrics in real-time.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with Amazon SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Amazon SageMaker AI Model Dashboard](../../../sagemaker/latest/dg/model-dashboard.md "../../../sagemaker/latest/dg/model-dashboard.md")
- [Shadow
  tests](../../../sagemaker/latest/dg/shadow-tests.md "../../../sagemaker/latest/dg/shadow-tests.md")
- [Lineage
  Tracking Entities](../../../sagemaker/latest/dg/lineage-tracking-entities.md "../../../sagemaker/latest/dg/lineage-tracking-entities.md")
- [Using
  CloudWatch outlier detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md")
- [Monitoring
  Amazon ML with Amazon CloudWatch Metrics](../../../machine-learning/latest/dg/cw-doc.md "../../../machine-learning/latest/dg/cw-doc.md")
- [New
  for Amazon SageMaker AI – Perform Shadow Tests to Compare
  Inference Performance Between ML Model Variants](https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/ "https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/")
- [Integrate
  Amazon SageMaker AI Model Cards with the model registr](https://aws.amazon.com/blogs/machine-learning/integrate-amazon-sagemaker-model-cards-with-the-model-registry/ "https://aws.amazon.com/blogs/machine-learning/integrate-amazon-sagemaker-model-cards-with-the-model-registry/")
- [Improve
  governance of your machine learning models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/ "https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/")

**Related examples:**

- [Monitoring
  bias drift and feature attribution drift with Amazon SageMaker AI
  Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/fairness_and_explainability/SageMaker AI-Model-Monitor-Fairness-and-Explainability.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/fairness_and_explainability/SageMaker AI-Model-Monitor-Fairness-and-Explainability.html")
