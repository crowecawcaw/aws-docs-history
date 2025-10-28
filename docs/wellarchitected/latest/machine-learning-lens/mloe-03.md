# MLOE-03: Monitor model compliance to business requirements

Machine learning models degrade over time due to changes in the
real world, such as _data drift_ and
_concept drift_. If not monitored, these
changes could lead to models becoming inaccurate or even
obsolete over time. It’s important to have a periodic monitoring
process in place to make sure that your ML models continue to
comply to your business requirements, and that deviations are
captured and acted upon promptly. 

## Implementation plan

- **Agree on the metrics to monitor -** Clearly establish the metrics that you want to
  capture from your model monitoring process. These metrics
  should be tied to your business requirements and should
  cover your dataset-related statistics and model inference
  metrics.
- **Have an action plan on a drift
  –** If an unacceptable drift is detected in a
  dataset or the model output, have an action plan to mitigate
  it based on the type of drift and the metrics associated.
  This mitigation could include kicking off a retraining
  pipeline, updating the model, augmenting your dataset with
  more instances, or enriching your feature engineering
  process.

## Documents

- [Monitor
  models for data and model quality using SageMaker AI Model
  Monitor](../../../sagemaker/latest/dg/model-monitor.md "../../../sagemaker/latest/dg/model-monitor.md")

## Blogs

- [Model
  monitoring at scale for production models](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/ "https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/")
