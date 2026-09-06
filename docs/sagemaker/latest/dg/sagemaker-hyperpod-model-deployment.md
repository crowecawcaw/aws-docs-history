

# Deploying models on Amazon SageMaker HyperPod
<a name="sagemaker-hyperpod-model-deployment"></a>

Amazon SageMaker HyperPod now extends beyond training to deliver a comprehensive inference platform that combines the flexibility of Kubernetes with the operational excellence of AWS managed services. Deploy, scale, and optimize your machine learning models with enterprise-grade reliability using the same HyperPod compute throughout the entire model lifecycle.

Amazon SageMaker HyperPod offers flexible deployment interfaces that allow you to deploy models through multiple methods including kubectl, Python SDK, Amazon SageMaker Studio UI, or HyperPod CLI. The service provides advanced autoscaling capabilities with dynamic resource allocation that automatically adjusts based on demand. Additionally, it includes comprehensive observability and monitoring features that track critical metrics such as time-to-first-token, latency, and GPU utilization to help you optimize performance.

**Note**  
When deploying on GPU-enabled instances, you can use GPU partitioning with Multi-Instance GPU (MIG) technology to run multiple inference workloads on a single GPU. This allows for better GPU utilization and cost optimization. For more information about configuring GPU partitioning, see [Using GPU partitions in Amazon SageMaker HyperPod](sagemaker-hyperpod-eks-gpu-partitioning.md).

**Unified infrastructure for training and inference**

Maximize your GPU utilization by seamlessly transitioning compute resources between training and inference workloads. This reduces the total cost of ownership while maintaining operational continuity.

**Enterprise-ready deployment options**

Deploy models from multiple sources including open-weights and gated models from Amazon SageMaker JumpStart and custom models from Amazon S3 and Amazon FSx with support for both single-node and multi-node inference architectures.

**Managed tiered Key-value (KV) caching and intelligent routing**

KV caching saves the precomputed key-value vectors after processing previous tokens. When the next token is processed, the vectors don't need to be recalculated. Through a two-tier caching architecture, you can configure an L1 cache that uses CPU memory for low-latency local reuse, and an L2 cache that leverages Redis to enable scalable, node-level cache sharing.

Intelligent routing analyzes incoming requests and directs them to the inference instance most likely to have relevant cached key-value pairs. The system examines the request and then routes it based on one of the following routing strategies:

1. `prefixaware` — Subsequent requests with the same prompt prefix are routed to the same instance

1. `kvaware` — Incoming requests are routed to the instance with the highest KV cache hit rate.

1. `session` — Requests from the same user session are routed to the same instance.

1. `roundrobin` — Even distribution of requests without considering the state of the KV cache.

For more information on how to enable this feature, see [Configure KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md#sagemaker-hyperpod-model-deployment-deploy-ftm-cache-route).

**Inbuilt L2 cache Tiered Storage Support for KV Caching**

Building upon the existing KV cache infrastructure, HyperPod now integrates tiered storage as an additional L2 backend option alongside Redis. With the inbuilt SageMaker managed tiered storage, this offers improved performance. This enhancement provides customers with a more scalable and efficient option for cache offloading, particularly beneficial for high-throughput LLM inference workloads. The integration maintains compatibility with existing vLLM model servers and routing capabilities while offering better performance.

**Note**  
**Data encryption:** KV cache data (attention keys and values) is stored unencrypted at rest to optimize inference latency and improve performance. For workloads with strict encryption-at-rest requirements, consider application-layer encryption of prompts and responses, or disable caching.  
**Data isolation:** When using managed tiered storage as the L2 cache backend, multiple inference deployments within a cluster share cache storage with no isolation. L2 KV cache data (attention keys and values) from different deployments is not separated. For workloads requiring data isolation (multi-tenant scenarios, different data classification levels), deploy to separate clusters or use dedicated Redis instances.

You can reduce cold start latency when scaling out deployments by caching model weights on host-local NVMe storage and pre-pulling the inference server container image onto target nodes. You can enable these features independently or together through the `modelCacheConfig` field, and they work with models from Amazon SageMaker JumpStart, Amazon S3, and Amazon FSx. For more information, see [Model weights caching and image caching](sagemaker-hyperpod-model-deployment-model-caching.md).

**Multi-instance type deployment with automatic failover**

HyperPod Inference supports multi-instance type deployment to improve deployment reliability and resource utilization. Specify a prioritized list of instance types in your deployment configuration, and the system automatically selects from available alternatives when your preferred instance type lacks capacity. The Kubernetes scheduler uses `preferredDuringSchedulingIgnoredDuringExecution` node affinity to evaluate instance types in priority order, placing workloads on the highest-priority available instance type while ensuring deployment even when preferred resources are unavailable. This capability prevents deployment failures due to capacity constraints while maintaining your cost and performance preferences, ensuring continuous service availability even during cluster capacity fluctuations.

**Custom node affinity for granular scheduling control**

HyperPod Inference supports custom node affinity to control workload placement beyond instance type selection. Specify node selection criteria such as availability zone distribution, capacity type filtering (on-demand vs. spot), or custom node labels through the `nodeAffinity` field. The system supports mandatory placement constraints using `requiredDuringSchedulingIgnoredDuringExecution` and optional preferences through `preferredDuringSchedulingIgnoredDuringExecution`, providing full control over pod scheduling decisions while maintaining deployment flexibility.

**Note**  
We collect certain routine operational metrics to provide essential service availability. The creation of these metrics is fully automated and does not involve human review of the underlying model inference workload. These metrics relate to deployment operations, resource management, and endpoint registration.

**Topics**
+ [Setting up your HyperPod clusters for model deployment](sagemaker-hyperpod-model-deployment-setup.md)
+ [Deploy foundation models and custom fine-tuned models](sagemaker-hyperpod-model-deployment-deploy.md)
+ [Custom certificates and Route 53 DNS management for HyperPod Inference](sagemaker-hyperpod-model-deployment-custom-certs.md)
+ [Configure request limits for your HyperPod inference model deployment](sagemaker-hyperpod-model-deployment-request-limits.md)
+ [Autoscaling policies for your HyperPod inference model deployment](sagemaker-hyperpod-model-deployment-autoscaling.md)
+ [Implementing inference observability on HyperPod clusters](sagemaker-hyperpod-model-deployment-observability.md)
+ [Task governance for model deployment on HyperPod](sagemaker-hyperpod-model-deployment-task-gov.md)
+ [Data capture for inference on HyperPod](sagemaker-hyperpod-model-deployment-data-capture.md)
+ [Disaggregated Prefill and Decode for HyperPod inference](sagemaker-hyperpod-model-deployment-dpd.md)
+ [HyperPod inference troubleshooting](sagemaker-hyperpod-model-deployment-ts.md)
+ [Model weights caching and image caching](sagemaker-hyperpod-model-deployment-model-caching.md)
+ [KV caching and intelligent routing](sagemaker-hyperpod-model-deployment-caching-routing.md)
+ [Amazon SageMaker HyperPod Inference release notes](sagemaker-hyperpod-inference-release-notes.md)