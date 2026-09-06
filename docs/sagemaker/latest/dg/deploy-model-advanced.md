

# Advanced endpoint options for inference with Amazon SageMaker AI
<a name="deploy-model-advanced"></a>

With real-time inference, you can further optimize for performance and cost with the following advanced inference options:
+ [Multi-model endpoints](multi-model-endpoints.md) – Use this option if you have multiple models that use the same framework and can share a container. This option helps you optimize costs by improving endpoint utilization and reducing deployment overhead.
+ [Multi-container endpoints](multi-container-endpoints.md) – Use this option if you have multiple models that use different frameworks and require their own containers. You get many of the benefits of Multi-Model Endpoints and can deploy a variety of frameworks and models.
+ [Serial Inference Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) – Use this option if you want to host models with pre-processing and post-processing logic behind an endpoint. Inference pipelines are fully managed by SageMaker AI and provide lower latency because all of the containers are hosted on the same Amazon EC2 instances.