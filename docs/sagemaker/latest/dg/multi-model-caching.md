# Set SageMaker AI multi-model endpoint model caching

behavior

By default, multi-model endpoints cache frequently used models in memory (CPU or GPU,
depending on whether you have CPU or GPU backed instances) and on disk to provide low latency
inference. The cached models are unloaded and/or deleted from disk only when a container runs
out of memory or disk space to accommodate a newly targeted model.

You can change the caching behavior of a multi-model endpoint and explicitly enable or
disable model caching by setting the parameter `ModelCacheSetting` when you call
[create_model](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker.html#SageMaker.Client.create_model").

We recommend setting the value of the `ModelCacheSetting` parameter to
`Disabled` for use cases that do not benefit from model caching. For example,
when a large number of models need to be served from the endpoint but each model is invoked
only once (or very infrequently). For such use cases, setting the value of the
`ModelCacheSetting` parameter to `Disabled` allows higher transactions
per second (TPS) for `invoke_endpoint` requests compared to the default caching
mode. Higher TPS in these use cases is because SageMaker AI does the following after the
`invoke_endpoint` request:

- Asynchronously unloads the model from memory and deletes it from disk immediately
  after it is invoked.
- Provides higher concurrency for downloading and loading models in the inference
  container. For both CPU and GPU backed endpoints, the concurrency is a factor of the
  number of the vCPUs of the container instance.
  For guidelines on choosing a SageMaker AI ML instance type for a multi-model endpoint, see [Instance recommendations for multi-model
  endpoint deployments](multi-model-endpoint-instance.md "multi-model-endpoint-instance.md").
