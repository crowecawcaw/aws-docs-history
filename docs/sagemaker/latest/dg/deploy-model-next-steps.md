# Next steps for inference with Amazon SageMaker AI

After you have an endpoint and understand the general inference workflow, you can use
the following features in SageMaker AI to improve your inference workflow.

## Monitoring

To track your model over time through metrics such as model accuracy and drift,
you can use Model Monitor. With Model Monitor, you can set alerts that notify you when there are
deviations in your model’s quality. To learn more, see the [Model Monitor
documentation](model-monitor.md "model-monitor.md").

To learn more about tools that can be used to monitor model deployments and events
that change your endpoint, see [Monitor Amazon SageMaker AI](monitoring-overview.md "monitoring-overview.md"). For
example, you can monitor your endpoint’s health through metrics such as invocation
errors and model latency using Amazon CloudWatch metrics. The [SageMaker AI endpoint invocation metrics](monitoring-cloudwatch.md#cloudwatch-metrics-endpoint-invocation "monitoring-cloudwatch.md#cloudwatch-metrics-endpoint-invocation") can provide you with valuable
information about your endpoint’s performance.

## CI/CD for model deployment

To put together machine learning solutions in SageMaker AI, you can use [SageMaker AI
MLOps](sagemaker-projects.md "sagemaker-projects.md"). You can use this feature to automate the steps in your machine
learning workflow and practice CI/CD. You can use [MLOps Project
Templates](sagemaker-projects-templates.md "sagemaker-projects-templates.md") to help with the setup and implementation of SageMaker AI MLOps
projects. SageMaker AI also supports using your own [third-party
Git repo](sagemaker-projects-walkthrough-3rdgit.md "sagemaker-projects-walkthrough-3rdgit.md") for creating a CI/CD system.

For your ML pipelines, use [Model Registry](model-registry.md "model-registry.md") to manage
your model versions and the deployment and automation of your models.

## Deployment guardrails

If you want to update your model while it’s in production without impacting
production, you can use deployment guardrails. Deployment guardrails are a set of
model deployment options in SageMaker AI Inference to update your machine learning models in
production. Using the fully managed deployment options, you can control the switch
from the current model in production to a new one. Traffic shifting modes give you
granular control over the traffic shifting process, and built-in safeguards like
auto-rollbacks help you catch issues early on.

To learn more about deployment guardrails, see the [deployment guardrails
documentation](deployment-guardrails.md "deployment-guardrails.md").

## Inferentia

If you need to run large-scale machine learning and deep learning applications,
you can use an `Inf1` instance with a real-time endpoint. This instance
type is suitable for use cases such as image or speech recognition, natural language
processing (NLP), personalization, forecasting, or fraud detection.

`Inf1` instances are built to support machine learning inference
applications and feature the AWS Inferentia chips. `Inf1` instances
provide higher throughput and lower cost per inference than GPU-based
instances.

To deploy a model on `Inf1` instances, compile your model with SageMaker Neo
and choose an `Inf1` instance for your deployment option. To learn more,
see [Optimize model
performance using SageMaker Neo](neo.md "neo.md").

## Optimize model

performance

SageMaker AI provides features to manage resources and optimize inference performance when
deploying machine learning models. You can use SageMaker AI’s [built-in algorithms and pre-built
models](algos.md "algos.md"), as well as [prebuilt Docker
images](docker-containers-prebuilt.md "docker-containers-prebuilt.md"), which are developed for machine learning.

To train models and optimize them for deployment, see [prebuilt Docker
images](docker-containers-prebuilt.md "docker-containers-prebuilt.md")[Optimize model performance using SageMaker Neo](neo.md "neo.md"). With SageMaker Neo, you can train
TensorFlow, Apache MXNet, PyTorch, ONNX, and XGBoost models. Then, you can optimize them
and deploy on ARM, Intel, and Nvidia processors.

## Autoscaling

If you have varying amounts of traffic to your endpoints, you might want to try
autoscaling. For example, during peak hours, you might require more instances to
process requests. However, during periods of low traffic, you might want to reduce
your use of computing resources. To dynamically adjust the number of instances
provisioned in response to changes in your workload, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md "endpoint-auto-scaling.md").

If you have unpredictable traffic patterns or don’t want to set up scaling
policies, you can also use Serverless Inference for an endpoint. Then, SageMaker AI manages autoscaling for
you. During periods of low traffic, SageMaker AI scales down your endpoint, and if traffic
increases, then SageMaker AI scales your endpoint up. For more information, see the [Deploy models with Amazon SageMaker Serverless Inference](serverless-endpoints.md "serverless-endpoints.md")
documentation.
