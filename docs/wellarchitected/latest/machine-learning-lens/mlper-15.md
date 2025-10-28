# MLPER-15: Monitor, detect, and handle model performance degradation

Model performance could degrade over time for reasons such as
data quality, model quality, model bias, and model
explainability. Continuously monitor the quality of the ML
model in real time. Identify the right time and frequency to
retrain and update the model. Configure alerts to notify and
initiate actions if any drift in model performance is
observed.

## Implementation plan

- **Monitor model
  performance** -
  [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md") continually monitors the
  quality of Amazon SageMaker AI machine learning models in
  production. Establish a baseline during training before
  model is in production. Collect data while in production
  and compare changes in model inferences. Observations of
  drifts in the data statistics will indicate that the
  model may need to be retrained. The timing of drifts
  will establish a schedule for retraining. Use
  [SageMaker AI
  Clarify](https://aws.amazon.com/sagemaker/clarify/ "https://aws.amazon.com/sagemaker/clarify/") to identify model bias. Configure alerting
  systems with
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to send notifications for unexpected
  bias or changes in data quality.
- **Perform automatic
  scaling** - Amazon SageMaker AI includes automatic
  scaling capabilities for your hosted model to
  dynamically adjust underlying compute supporting an
  endpoint based on demand. This capability ensures that
  your endpoint can dynamically support demand while
  reducing operational overhead.
- **Monitor endpoint
  metrics** - Amazon SageMaker AI also outputs
  endpoint metrics for monitoring the usage and health of
  the endpoint. Amazon SageMaker AI Model Monitor provides
  the capability to monitor your ML models in production
  and provides alerts when data quality issues appear.
  Create a mechanism to aggregate and analyze model
  prediction endpoint metrics using services, such as
  [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/ "https://aws.amazon.com/elasticsearch-service/") (OpenSearch Service).
  OpenSearch Service supports
  [Kibana](../../../elasticsearch-service/latest/developerguide/es-kibana.md "../../../elasticsearch-service/latest/developerguide/es-kibana.md")
  for dashboards and visualization. The traceability of
  hosting metrics back to versioned inputs allows for
  analysis of changes that could be impacting current
  operational performance.

## Documents

- [Amazon SageMaker AI Model Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")
- [How
  Amazon CloudWatch works](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_architecture.md")
- [Fairness, model explainability and bias detection with SageMaker Clarify](../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md "../../../sagemaker/latest/dg/clarify-configure-processing-jobs.md")

## Blogs

- [Monitoring
  in-production ML models at large scale using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
- [ML
  model explainability with Amazon SageMaker AI Clarify and
  the SKLearn pre-built container](https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/ "https://aws.amazon.com/blogs/machine-learning/use-amazon-sagemaker-clarify-with-the-sklearn-pre-built-container/")

## Videos

- [Understand
  ML model predictions & biases with Amazon SageMaker AI
  Clarify](https://www.youtube.com/watch?v=t2SJTYiTnYM "https://www.youtube.com/watch?v=t2SJTYiTnYM")
- [Deep
  Dive on Amazon SageMaker AI Debugger & Amazon SageMaker AI
  Model Monitor](https://www.youtube.com/watch?v=0zqoeZxakOI "https://www.youtube.com/watch?v=0zqoeZxakOI")
- [Detect
  machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w "https://www.youtube.com/watch?v=J9T0X9Jxl_w")

## Examples

- [Amazon SageMaker AI Model Monitor Examples- Github](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_model_monitor")
