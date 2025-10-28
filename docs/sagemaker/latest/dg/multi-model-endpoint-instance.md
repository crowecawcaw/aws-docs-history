# Instance recommendations for multi-model

endpoint deployments

There are several items to consider when selecting a SageMaker AI ML instance type for a
multi-model endpoint:

- Provision sufficient [Amazon Elastic Block Store (Amazon EBS)](../../../AWSEC2/latest/UserGuide/AmazonEBS.md "../../../AWSEC2/latest/UserGuide/AmazonEBS.md") capacity for all
  of the models that need to be served.
- Balance performance (minimize cold starts) and cost (don’t over-provision instance
  capacity). For information about the size of the storage volume that SageMaker AI attaches for
  each instance type for an endpoint and for a multi-model endpoint, see [Instance storage volumes](host-instance-storage.md "host-instance-storage.md").
- For a container configured to run in `MultiModel` mode, the storage volume
  provisioned for its instances are larger than the default `SingleModel` mode.
  This allows more models to be cached on the instance storage volume than in
  `SingleModel` mode.
  When choosing a SageMaker AI ML instance type, consider the following:

- Multi-model endpoints are currently supported for all CPU instances types and on
  single-GPU instance types.
- For the traffic distribution (access patterns) to the models that you want to host
  behind the multi-model endpoint, along with the model size (how many models could be
  loaded in memory on the instance), keep the following information in mind:
  - Think of the amount of memory on an instance as the cache space for models to be
    loaded, and think of the number of vCPUs as the concurrency limit to perform inference
    on the loaded models (assuming that invoking a model is bound to CPU).
  - For CPU backed instances, the number of vCPUs impacts your maximum concurrent
    invocations per instance (assuming that invoking a model is bound to CPU). A higher
    amount of vCPUs enables you to invoke more unique models concurrently.
  - For GPU backed instances, a higher amount of instance and GPU memory enables you
    to have more models loaded and ready to serve inference requests.
  - For both CPU and GPU backed instances, have some "slack" memory available so that
    unused models can be unloaded, and especially for multi-model endpoints with multiple
    instances. If an instance or an Availability Zone fails, the models on those instances
    will be rerouted to other instances behind the endpoint.

- Determine your tolerance to loading/downloading times:

      + d instance type families (for example, m5d, c5d, or r5d) and g5s come with an NVMe
       (non-volatile memory express) SSD, which offers high I/O performance and might reduce
       the time it takes to download models to the storage volume and for the container to
       load the model from the storage volume.
      + Because d and g5 instance types come with an NVMe SSD storage, SageMaker AI does not
       attach an Amazon EBS storage volume to these ML compute instances that hosts the
       multi-model endpoint. Auto scaling works best when the models are similarly sized and
       homogenous, that is when they have similar inference latency and resource
       requirements.

  You can also use the following guidance to help you optimize model loading on your
  multi-model endpoints:

**Choosing an instance type that can't hold all of the targeted models
in memory**

In some cases, you might opt to reduce costs by choosing an instance type that can't hold
all of the targeted models in memory at once. SageMaker AI dynamically unloads models when it runs out
of memory to make room for a newly targeted model. For infrequently requested models, you
sacrifice dynamic load latency. In cases with more stringent latency needs, you might opt for
larger instance types or more instances. Investing time up front for performance testing and
analysis helps you to have successful production deployments.

**Evaluating your model cache hits**

Amazon CloudWatch metrics can help you evaluate your models. For more information about metrics you
can use with multi-model endpoints, see [CloudWatch Metrics for Multi-Model
Endpoint Deployments](multi-model-endpoint-cloudwatch-metrics.md "multi-model-endpoint-cloudwatch-metrics.md") .

You can use the `Average` statistic of the `ModelCacheHit` metric
to monitor the ratio of requests where the model is already loaded. You can use the
`SampleCount` statistic for the `ModelUnloadingTime` metric to monitor
the number of unload requests sent to the container during a time period. If models are
unloaded too frequently (an indicator of _thrashing_, where
models are being unloaded and loaded again because there is insufficient cache space for the
working set of models), consider using a larger instance type with more memory or increasing
the number of instances behind the multi-model endpoint. For multi-model endpoints with
multiple instances, be aware that a model might be loaded on more than 1 instance.
