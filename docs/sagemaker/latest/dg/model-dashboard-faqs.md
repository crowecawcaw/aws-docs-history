# Model Dashboard FAQ

Refer to the following FAQ topics for answers to commonly asked questions about
Amazon SageMaker Model Dashboard.

Amazon SageMaker Model Dashboard is a centralized repository of all models created in your account.
The models are generally the outputs of SageMaker training jobs, but you can also import
models trained elsewhere and host them on SageMaker AI. Model Dashboard provides a single interface
for IT administrators, model risk managers, and business leaders to track all deployed
models and aggregates data from multiple AWS services to provide indicators about
how your models are performing. You can view details about model endpoints,
batch transform jobs, and monitoring jobs for additional insights into model performance.
The dashboard’s visual display helps you quickly identify which models have missing or
inactive monitors so you can ensure all models are periodically checked for data drift,
model drift, bias drift, and feature attribution drift. Lastly, the dashboard’s ready
access to model details helps you dive deep so you can access logs, infrastructure-related
information, and resources to help you debug monitoring failures.

You should have one or more models created in SageMaker AI, either trained on
SageMaker AI or externally trained. While this is not a mandatory prerequisite, you
gain the most value from the dashboard if you set up model monitoring jobs via
Amazon SageMaker Model Monitor for models deployed to endpoints.

Model risk managers, ML practitioners, data scientists and business leaders can
get a comprehensive overview of models using the Model Dashboard. The dashboard aggregates
and displays data from Amazon SageMaker Model Cards, Endpoints and Model Monitor services to display valuable information
such as model metadata from the model card and model registry, endpoints where the models
are deployed, and insights from model monitoring.

Model Dashboard is available out of the box with Amazon SageMaker AI and does not require any prior
configuration. However, if you have set up model monitoring jobs using SageMaker Model Monitor
and Clarify, you use Amazon CloudWatch to configure alerts that raise a flag in the dashboard
when model performance deviates from an acceptable range. You can create and add new
model cards to the dashboard, and view all
the monitoring results associated with endpoints. Model Dashboard currently does not
support cross-account models.

With Amazon SageMaker Model Monitor, you can select the data you want to monitor and analyze
without writing any code. SageMaker Model Monitor lets you select data, such
as prediction output, from a menu of options and captures metadata such as
timestamp, model name, and endpoint so you can analyze model predictions.
You can specify the sampling rate of data capture as a percentage of overall
traffic in the case of high volume real-time predictions. This data is stored
in your own Amazon S3 bucket. You can also encrypt this data, configure
fine-grained security, define data retention policies, and implement access
control mechanisms for secure access.

SageMaker Model Monitor provides the following types of [model monitors](model-monitor.md "model-monitor.md"):

- _Data Quality_: Monitor drift in data quality.
- _Model Quality_: Monitor drift in model quality metrics, such as
  accuracy.
- _Bias Drift for Models in Production_: Monitor bias in your model's
  predictions by comparing the distribution of training and live data.
- _Feature Attribution Drift for Models in Production_: Monitor drift in
  feature attribution by comparing the relative rankings of features in training
  and live data.
  Model Monitor currently supports endpoints that host a single model for real-time inference and does not
  support monitoring of [multi-model endpoints](multi-model-endpoints.md "multi-model-endpoints.md").

You can use the following resources to get started with model monitoring:

- [Data quality monitor example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/introduction/SageMaker-ModelMonitoring.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/introduction/SageMaker-ModelMonitoring.ipynb")
- [Model quality monitor example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/introduction/SageMaker-ModelMonitoring.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/introduction/SageMaker-ModelMonitoring.ipynb")
- [Bias drift monitor example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/fairness_and_explainability/SageMaker-Model-Monitor-Fairness-and-Explainability.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/fairness_and_explainability/SageMaker-Model-Monitor-Fairness-and-Explainability.ipynb")
- [Feature attribution drift monitor example notebook](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/fairness_and_explainability/SageMaker-Model-Monitor-Fairness-and-Explainability.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker_model_monitor/fairness_and_explainability/SageMaker-Model-Monitor-Fairness-and-Explainability.ipynb")
  For more examples of model monitoring, see the GitHub repository [amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor").

Amazon SageMaker Model Monitor automatically monitors machine learning models in production, using
rules to detect drift in your model. Model Monitor notifies you when quality issues arise
through alerts. To learn more, see [How Amazon SageMaker Model Monitor works](model-monitor.md#model-monitor-how-it-works "model-monitor.md#model-monitor-how-it-works").

Model Monitor computes model metrics and statistics on tabular data only. For use cases
other than tabular datasets, such as images or text, you can bring your own containers
(BYOC) to monitor your data and models. For example, you can use BYOC to monitor an image
classification model that takes images as input and outputs a label. To learn
more about container contracts, see [Support for Your Own Containers
With Amazon SageMaker Model Monitor](model-monitor-byoc-containers.md "model-monitor-byoc-containers.md").

You can find helpful BYOC examples in the following links:

- [Data and model quality monitoring with Amazon SageMaker Model Monitor](model-monitor.md "model-monitor.md")
- [GitHub
  example repository](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_model_monitor "https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker_model_monitor")
- [Support for Your Own Containers
  With Amazon SageMaker Model Monitor](model-monitor-byoc-containers.md "model-monitor-byoc-containers.md")
- [Detecting
  data drift in NLP using BYOC Model Monitor](https://aws.amazon.com/blogs/machine-learning/detect-nlp-data-drift-using-custom-amazon-sagemaker-model-monitor "https://aws.amazon.com/blogs/machine-learning/detect-nlp-data-drift-using-custom-amazon-sagemaker-model-monitor")
- [Detecting and analyzing incorrect predictions in CV](https://aws.amazon.com/blogs//machine-learning/detecting-and-analyzing-incorrect-model-predictions-with-amazon-sagemaker-model-monitor-and-debugger "https://aws.amazon.com/blogs//machine-learning/detecting-and-analyzing-incorrect-model-predictions-with-amazon-sagemaker-model-monitor-and-debugger")
  For details about how to integrate Model Monitor and Pipelines, see [Amazon Pipelines now integrates with SageMaker Model Monitor and SageMaker Clarify](https://aws.amazon.com/about-aws/whats-new/2021/12/amazon-sagemaker-pipelines-integrates-sagemaker-model-monitor-sagemaker-clarify/ "https://aws.amazon.com/about-aws/whats-new/2021/12/amazon-sagemaker-pipelines-integrates-sagemaker-model-monitor-sagemaker-clarify/") .

For an example, see the GitHub sample notebook
[Pipelines integration with Model Monitor and Clarify](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb "https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-pipelines/tabular/model-monitor-clarify-pipelines/sagemaker-pipeline-model-monitor-clarify-steps.ipynb").

When turned on, data capture occurs asynchronously on the SageMaker AI endpoints. To prevent
impact to inference requests, `DataCapture` stops capturing requests at high levels of disk usage. It is recommended
you keep your disk utilization below 75% to ensure `DataCapture` continues capturing requests.
