

# Next steps for inference with Amazon SageMaker AI
<a name="deploy-model-next-steps"></a>

After you have an endpoint and understand the general inference workflow, you can use the following features in SageMaker AI to improve your inference workflow.

## Monitoring
<a name="deploy-model-next-steps-monitoring"></a>

To track your model over time through metrics such as model accuracy and drift, you can use Model Monitor. With Model Monitor, you can set alerts that notify you when there are deviations in your model’s quality. To learn more, see the [Model Monitor documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html). 

To learn more about tools that can be used to monitor model deployments and events that change your endpoint, see [Monitor Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-overview.html). For example, you can monitor your endpoint’s health through metrics such as invocation errors and model latency using Amazon CloudWatch metrics. The [SageMaker AI endpoint invocation metrics](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html#cloudwatch-metrics-endpoint-invocation) can provide you with valuable information about your endpoint’s performance.

## CI/CD for model deployment
<a name="deploy-model-next-steps-cicd"></a>

To put together machine learning solutions in SageMaker AI, you can use [SageMaker AI MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html). You can use this feature to automate the steps in your machine learning workflow and practice CI/CD. You can use [MLOps Project Templates](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates.html) to help with the setup and implementation of SageMaker AI MLOps projects. SageMaker AI also supports using your own [third-party Git repo](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-walkthrough-3rdgit.html) for creating a CI/CD system.

For your ML pipelines, use [Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to manage your model versions and the deployment and automation of your models.

## Deployment guardrails
<a name="deploy-model-next-steps-guardrails"></a>

If you want to update your model while it’s in production without impacting production, you can use deployment guardrails. Deployment guardrails are a set of model deployment options in SageMaker AI Inference to update your machine learning models in production. Using the fully managed deployment options, you can control the switch from the current model in production to a new one. Traffic shifting modes give you granular control over the traffic shifting process, and built-in safeguards like auto-rollbacks help you catch issues early on. 

To learn more about deployment guardrails, see the [deployment guardrails documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html).

## Inferentia
<a name="deploy-model-next-steps-inferentia"></a>

If you need to run large-scale machine learning and deep learning applications, you can use an `Inf1` instance with a real-time endpoint. This instance type is suitable for use cases such as image or speech recognition, natural language processing (NLP), personalization, forecasting, or fraud detection.

`Inf1` instances are built to support machine learning inference applications and feature the AWS Inferentia chips. `Inf1` instances provide higher throughput and lower cost per inference than GPU-based instances.

To deploy a model on `Inf1` instances, compile your model with SageMaker Neo and choose an `Inf1` instance for your deployment option. To learn more, see [Optimize model performance using SageMaker Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html).

## Optimize model performance
<a name="deploy-model-next-steps-optimize"></a>

SageMaker AI provides features to manage resources and optimize inference performance when deploying machine learning models. You can use SageMaker AI’s [built-in algorithms and pre-built models](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html), as well as [prebuilt Docker images](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-prebuilt.html), which are developed for machine learning.

To train models and optimize them for deployment, see [prebuilt Docker images](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers-prebuilt.html)[Optimize model performance using SageMaker Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html). With SageMaker Neo, you can train TensorFlow, Apache MXNet, PyTorch, ONNX, and XGBoost models. Then, you can optimize them and deploy on ARM, Intel, and Nvidia processors.

## Autoscaling
<a name="deploy-model-next-steps-autoscaling"></a>

If you have varying amounts of traffic to your endpoints, you might want to try autoscaling. For example, during peak hours, you might require more instances to process requests. However, during periods of low traffic, you might want to reduce your use of computing resources. To dynamically adjust the number of instances provisioned in response to changes in your workload, see [Automatic scaling of Amazon SageMaker AI models](endpoint-auto-scaling.md).

If you have unpredictable traffic patterns or don’t want to set up scaling policies, you can also use Serverless Inference for an endpoint. Then, SageMaker AI manages autoscaling for you. During periods of low traffic, SageMaker AI scales down your endpoint, and if traffic increases, then SageMaker AI scales your endpoint up. For more information, see the [Deploy models with Amazon SageMaker Serverless Inference](serverless-endpoints.md) documentation.