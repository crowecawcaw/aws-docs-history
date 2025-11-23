# MLPERF06-BP04 Monitor, detect, and handle model performance

degradation

Model performance could degrade over time for reasons such as data
quality, model quality, model bias, and model explainability.
Continuously monitor the quality of the ML model in real time.
Identify the right time and frequency to retrain and update the
model. Configure alerts to notify and initiate actions if a drift in
model performance is observed.

**Desired outcome:** You establish a
comprehensive monitoring system for your machine learning models
that detects performance degradation, alerts relevant stakeholders,
and takes appropriate remediation actions. Your ML systems maintain
high accuracy and reliability over time through automated
monitoring, detection, and handling of performance issues.

**Common anti-patterns:**

- Implementing ML models without ongoing monitoring.
- Relying solely on periodic manual checks of model performance.
- Ignoring data drift or concept drift until model performance
  severely degrades.
- Not having an established retraining strategy or schedule.
- Missing alert systems for model performance degradation.

**Benefits of establishing this best
practice:**

- Early detection of model performance issues.
- Automated notifications when models start to degrade.
- Improved model reliability and accuracy over time.
- Reduced operational risk from poor model predictions.
- Better understanding of model behavior in production
  environments.
- Increased trust in ML-powered systems.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model performance monitoring is critical for maintaining reliable
machine learning systems in production environments. As real-world
data changes over time, models can experience data drift (changes
in the distribution of input data) or concept drift (changes in
the relationship between inputs and target variables). Establish a
robust monitoring framework to detect these issues early and take
appropriate action.

Avoid implementing ML models without ongoing monitoring. Many
organizations rely solely on periodic manual checks of model
performance, ignore data drift or concept drift until model
performance severely degrades, don't have an established
retraining strategy or schedule, and miss alert systems for model
performance degradation.

When implementing model monitoring, you should establish baseline
performance metrics during the training and validation phases.
These baselines serve as the foundation for comparison once the
model is deployed. Monitor not just accuracy metrics, but also
data statistics, feature distributions, and prediction patterns to
identify subtle changes that might indicate underlying problems.

Setting up automated alerts notifies your team when key
performance indicators fall below acceptable thresholds. These
alerts should be configured with appropriate severity levels to
reflect the business impact of model degradation. Additionally,
implement automated scaling to handle varying workloads
efficiently, which keeps your model endpoints responsive
regardless of demand.

### Implementation steps

1. **Monitor model
   performance**.
   [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") continually monitors the
   quality of Amazon SageMaker AI machine learning models in
   production. Establish a baseline during training before
   model is in production. Collect data while in production and
   compare changes in model inferences. Observations of drifts
   in the data statistics will indicate that the model may need
   to be retrained. Use
   [SageMaker AI
   Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to identify model bias. Configure alerting
   systems with
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to send notifications for unexpected bias
   or changes in data quality.
2. **Perform automatic
   scaling**. Amazon SageMaker AI includes automatic
   scaling capabilities for your hosted model to dynamically
   adjust underlying compute supporting an endpoint based on
   demand. This capability verifies that that your endpoint can
   dynamically support demand while reducing operational
   overhead.
3. **Monitor endpoint metrics**.
   Amazon SageMaker AI also outputs endpoint metrics for
   monitoring the usage and health of the endpoint. Amazon SageMaker AI Model Monitor provides the capability to monitor
   your ML models in production and provides alerts when data
   quality issues appear. For enhanced observability, leverage
   one-click metrics and monitoring for HyperPod training jobs,
   deployments, health, resource usage, and historical job
   traces to drive faster debugging and operational excellence
   in foundation model workflows. Create a mechanism to
   aggregate and analyze model prediction endpoint metrics
   using services, such as
   [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/"). OpenSearch Service supports
   [dashboards](../../../opensearch-service/latest/developerguide/dashboards.md "../../../opensearch-service/latest/developerguide/dashboards.md")
   for visualization. Consider integrating third-party AI tools
   (Comet, Deepchecks, Fiddler AI, Lakera) for extended
   governance, bias detection, explainable AI, and vertical
   solutions. The traceability of hosting metrics back to
   versioned inputs allows for analysis of changes that could
   be impacting current operational performance.
4. **Establish data quality
   monitoring**. Configure SageMaker AI Model Monitor to
   track data quality metrics such as missing values,
   statistical outliers, and feature distribution shifts. Set
   up constraints that define acceptable ranges for these
   metrics and generate alerts when violations occur.
5. **Implement bias detection and
   tracking**. Use SageMaker AI Clarify to detect bias in
   your model predictions over time. Monitor for changes in
   fairness metrics across different segments of your data and
   create visualizations to track these metrics over time.
6. **Set up model explainability
   analysis**. Deploy SageMaker AI Clarify to track
   feature importance and SHAP values over time. These values
   can determine if the model's decision-making process is
   changing in unexpected ways that might indicate performance
   issues.
7. **Create a retraining
   pipeline**. Develop an automated pipeline that can
   retrain your models when performance degradation is
   detected. Use
   [AWS Step Functions](https://aws.amazon.com/step-functions/ "https://aws.amazon.com/step-functions/") to orchestrate the retraining
   workflow, including data preparation, model training,
   evaluation, and deployment.
8. **Implement A/B testing for model
   updates**. When deploying updated models, use
   SageMaker AI's
   [production
   variants](../../../sagemaker/latest/dg/model-ab-testing.md "../../../sagemaker/latest/dg/model-ab-testing.md") to perform A/B testing between the current
   and new model versions. This allows you to validate
   performance improvements before fully replacing the existing
   model.

## Resources

**Related documents:**

- [Data
  and model quality monitoring with SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [Fairness
  and Explainability with SageMaker AI Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.html "https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-clarify/fairness_and_explainability/fairness_and_explainability.html")
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/ "https://aws.amazon.com/sagemaker/feature-store/")
- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI
  Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
- [ML
  model explainability with Amazon SageMaker AI Clarify and the
  SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/")

**Related videos:**

- [Understand
  ML model predictions & biases with Amazon SageMaker AI
  Clarify](https://www.youtube.com/watch?v=t2SJTYiTnYM "https://www.youtube.com/watch?v=t2SJTYiTnYM")
- [Deep
  Dive on Amazon SageMaker AI Debugger & Amazon SageMaker AI Model
  Monitor](https://www.youtube.com/watch?v=0zqoeZxakOI "https://www.youtube.com/watch?v=0zqoeZxakOI")
- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

**Related examples:**

- [Amazon SageMaker AI Model Monitor Examples - Github](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor")
- [SageMaker AI
  Clarify Examples - Github](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify")
