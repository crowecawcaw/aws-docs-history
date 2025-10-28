# Implementing

inference observability on HyperPod clusters

Amazon SageMaker HyperPod provides comprehensive inference observability capabilities that
enable data scientists and machine learning engineers to monitor and optimize their
deployed models. This solution is enabled through SageMaker HyperPod Observability and
automatically collects performance metrics for inference workloads, delivering
production-ready monitoring through integrated [Prometheus](https://prometheus.io/ "https://prometheus.io/") and [Grafana](https://grafana.com/oss/ "https://grafana.com/oss/")
dashboards.

With metrics enabled by default, the platform captures essential model performance
data including invocation latency, concurrent requests, error rates, and token-level
metrics, while providing standard Prometheus endpoints for customers who prefer to
implement custom observability solutions.

###### Note

This topic contains a deep dive in to implementing inference observability on
HyperPod clusters. For a more general reference, see [Cluster and task
observability](sagemaker-hyperpod-eks-cluster-observability-cluster.md "sagemaker-hyperpod-eks-cluster-observability-cluster.md").

This guide provides step-by-step instructions for implementing and using inference
observability on your HyperPod clusters. You'll learn how to configure metrics in your
deployment YAML files, access monitoring dashboards based on your role (administrator,
data scientist, or machine learning engineer), integrate with custom observability
solutions using Prometheus endpoints, and troubleshoot common monitoring issues.

## Supported inference metrics

**Invocation metrics**

These metrics capture model inference request and response data, providing
universal visibility regardless of your model type or serving framework. When
inference metrics are enabled, these metrics are calculated at invocation time and
exported to your monitoring infrastructure.

- `model_invocations_total` - Total number of invocation requests
  to the model
- `model_errors_total` - Total number of errors during model
  invocation
- `model_concurrent_requests` - Active concurrent model
  requests
- `model_latency_milliseconds` - Model invocation latency in
  milliseconds
- `model_ttfb_milliseconds` - Model time to first byte latency in
  milliseconds

**Model container metrics**

These metrics provide insights into the internal operations of your model
containers, including token processing, queue management, and framework-specific
performance indicators. The metrics available depend on your model serving
framework:

- [TGI container metrics](https://huggingface.co/docs/text-generation-inference/en/reference/metrics "https://huggingface.co/docs/text-generation-inference/en/reference/metrics")
- [LMI container metrics](https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md "https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md")

**Metric dimensions**

All inference metrics include comprehensive labels that enable detailed filtering
and analysis across your deployments:

- **Cluster Identity:**
  - `cluster_id` - The unique ID of the HyperPod
    cluster
  - `cluster_name` - The name of the HyperPod
    cluster

- **Resource Identity:**
  - `resource_name` - Deployment name (For example,
    "jumpstart-model-deployment")
  - `resource_type` - Type of deployment (jumpstart,
    inference-endpoint)
  - `namespace` - Kubernetes namespace for
    multi-tenancy

- **Model Characteristics:**
  - `model_name` - Specific model identifier (For example,
    "llama-2-7b-chat")
  - `model_version` - Model version for A/B testing and
    rollbacks
  - `model_container_type` - Serving framework (TGI, LMI,
    -)

- **Infrastructure Context:**
  - `pod_name` - Individual pod identifier for
    debugging
  - `node_name` - Kubernetes node for resource
    correlation
  - `instance_type` - EC2 instance type for cost
    analysis

- **Operational Context:**
  - `metric_source` - Collection point (reverse-proxy,
    model-container)
  - `task_type` - Workload classification
    (inference)

## Configure

metrics in deployment YAML

Amazon SageMaker HyperPod enables inference metrics by default for all model deployments,
providing immediate observability without additional configuration. You can
customize metrics behavior by modifying the deployment YAML configuration to enable
or disable metrics collection based on your specific requirements.

**Deploy a model from JumpStart**

Use the following YAML configuration to deploy a JuJumpStartmpStart model with
metrics enabled:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: JumpStartModel
metadata:
  name:mistral-model
  namespace: ns-team-a
spec:
  model:
    modelId: "huggingface-llm-mistral-7b-instruct"
    modelVersion: "3.19.0"
  metrics:
    enabled:true # Default: true (can be set to false to disable)
  replicas: 2
  sageMakerEndpoint:
    name: "mistral-model-sm-endpoint"
  server:
    instanceType: "ml.g5.12xlarge"
    executionRole: "arn:aws:iam::123456789:role/SagemakerRole"
  tlsConfig:
    tlsCertificateOutputS3Uri: s3://hyperpod/mistral-model/certs/
```

**Deploy custom and fine-tuned models from Amazon S3 or
Amazon FSx**

Configure custom inference endpoints with detailed metrics settings using the
following YAML:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: JumpStartModel
metadata:
  name:mistral-model
  namespace: ns-team-a
spec:
  model:
    modelId: "huggingface-llm-mistral-7b-instruct"
    modelVersion: "3.19.0"
  metrics:
    enabled:true # Default: true (can be set to false to disable)
  replicas: 2
  sageMakerEndpoint:
    name: "mistral-model-sm-endpoint"
  server:
    instanceType: "ml.g5.12xlarge"
    executionRole: "arn:aws:iam::123456789:role/SagemakerRole"
  tlsConfig:
    tlsCertificateOutputS3Uri: s3://hyperpod/mistral-model/certs/

Deploy a custom inference endpoint

Configure custom inference endpoints with detailed metrics settings using the following YAML:

apiVersion: inference.sagemaker.aws.amazon.com/v1alpha1
kind: InferenceEndpointConfig
metadata:
  name: inferenceendpoint-deepseeks
  namespace: ns-team-a
spec:
  modelName: deepseeks
  modelVersion: 1.0.1
  metrics:
    enabled: true # Default: true (can be set to false to disable)
    metricsScrapeIntervalSeconds: 30 # Optional: if overriding the default 15s
    modelMetricsConfig:
        port: 8000 # Optional: if overriding, it defaults to the WorkerConfig.ModelInvocationPort.ContainerPort within the InferenceEndpointConfig spec 8080
        path: "/custom-metrics" # Optional: if overriding the default "/metrics"
  endpointName: deepseek-sm-endpoint
  instanceType: ml.g5.12xlarge
  modelSourceConfig:
    modelSourceType: s3
    s3Storage:
      bucketName: model-weights
      region: us-west-2
    modelLocation: deepseek
    prefetchEnabled: true
  invocationEndpoint: invocations
  worker:
    resources:
      limits:
        nvidia.com/gpu: 1
      requests:
        nvidia.com/gpu: 1
        cpu: 25600m
        memory: 102Gi
    image: 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.32.0-lmi14.0.0-cu124
    modelInvocationPort:
      containerPort: 8080
      name: http
    modelVolumeMount:
      name: model-weights
      mountPath: /opt/ml/model
    environmentVariables: ...
  tlsConfig:
    tlsCertificateOutputS3Uri: s3://hyperpod/inferenceendpoint-deepseeks4/certs/


```

###### Note

To disable metrics for specific deployments, set `metrics.enabled:
 false` in your YAML configuration.

## Monitor and

troubleshoot inference workloads by role

Amazon SageMaker HyperPod provides comprehensive observability capabilities that support
different user workflows, from initial cluster setup to advanced performance
troubleshooting. Use the following guidance based on your role and monitoring
requirements.

**HyperPod admin**

**Your responsibility:** Enable observability
infrastructure and ensure system health across the entire cluster.

**What you need to know:**

- Cluster-wide observability provides infrastructure metrics for all
  workloads
- One-click setup deploys monitoring stack with pre-configured
  dashboards
- Infrastructure metrics are separate from model-specific inference
  metrics

**What you need to do:**

1. Navigate to the HyperPod console.
2. Select your cluster.
3. Go to the HyperPod cluster details page you just created. You
   will see a new option to install the HyperPod observability add-on.
4. Click on the **Quick install** option. After 1-2 minutes
   all the steps will be completed and you will see the Grafana dashboard and
   Prometheus workspace details.

This single action automatically deploys the EKS Add-on, configures observability
operators, and provisions pre-built dashboards in Grafana.

**Data scientist**

**Your responsibility:** Deploy models efficiently
and monitor their basic performance.

**What you need to know:**

- Metrics are automatically enabled when you deploy models
- Grafana dashboards provide immediate visibility into model
  performance
- You can filter dashboards to focus on your specific deployments

**What you need to do:**

1. Deploy your model using your preferred method:
   1. Amazon SageMaker Studio UI
   2. HyperPod CLI commands
   3. Python SDK in notebooks
   4. kubectl with YAML configurations

2. Access your model metrics:
   1. Open Amazon SageMaker Studio
   2. Navigate to HyperPod Cluster and open Grafana
      Dashboard
   3. Select Inference Dashboard
   4. Apply filters to view your specific model deployment

3. Monitor key performance indicators:
   1. Track model latency and throughput
   2. Monitor error rates and availability
   3. Review resource utilization trends

After this is complete, you'll have immediate visibility into your model's
performance without additional configuration, enabling quick identification of
deployment issues or performance changes.

**Machine learning engineer (MLE)**

**Your responsibility:** Maintain production model
performance and resolve complex performance issues.

**What you need to know:**

- Advanced metrics include model container details like queue depths and
  token metrics
- Correlation analysis across multiple metric types reveals root
  causes
- Auto-scaling configurations directly impact performance during traffic
  spikes

**Hypothetical scenario:** A customer's chat model
experiences intermittent slow responses. Users are complaining about 5-10 second
delays. The MLE can leverage inference observability for systematic performance
investigation.

**What you need to do:**

1. Examine the Grafana dashboard to understand the scope and severity of the
   performance issue:
   1. High latency alert active since 09:30
   2. P99 latency: 8.2s (normal: 2.1s)
   3. Affected time window: 09:30-10:15 (45 minutes)

2. Correlate multiple metrics to understand the system behavior during the
   incident:
   1. Concurrent requests: Spiked to 45 (normal: 15-20)
   2. Pod scaling: KEDA scaled 2→5 pods during incident
   3. GPU utilization: Remained normal (85-90%)
   4. Memory usage: Normal (24GB/32GB)

3. Examine the distributed system behavior since the infrastructure metrics
   appear normal:
   1. Node-level view: All pods concentrated on same node (poor
      distribution)
   2. Model container metrics: TGI queue depth shows 127 requests
      (normal: 5-10)

```
Available in Grafana dashboard under "Model Container Metrics" panel
        Metric: tgi_queue_size{resource_name="customer-chat-llama"}
        Current value: 127 requests queued (indicates backlog)
```

4. Identify interconnected configuration issues:
   1. KEDA scaling policy: Too slow (30s polling interval)
   2. Scaling timeline: Scaling response lagged behind traffic spike by
      45+ seconds

5. Implement targeted fixes based on the analysis:
   1. Updated KEDA polling interval: 30s → 15s
   2. Increased maxReplicas in scaling configuration
   3. Adjusted scaling thresholds to scale earlier (15 vs 20 concurrent
      requests)

You can systematically diagnose complex performance issues using comprehensive
metrics, implement targeted fixes, and establish preventive measures to maintain
consistent production model performance.

## Implement

your own observability integration

Amazon SageMaker HyperPod exposes inference metrics through industry-standard Prometheus
endpoints, enabling integration with your existing observability infrastructure. Use
this approach when you prefer to implement custom monitoring solutions or integrate
with third-party observability platforms instead of using the built-in Grafana and
Prometheus stack.

**Access inference metrics endpoints**

**What you need to know:**

- Inference metrics are automatically exposed on standardized Prometheus
  endpoints
- Metrics are available regardless of your model type or serving
  framework
- Standard Prometheus scraping practices apply for data collection

**Inference metrics endpoint configuration:**

- **Port:** 9113
- **Path:** /metrics
- **Full endpoint:**
  http://pod-ip:9113/metrics

**Available inference metrics:**

- `model_invocations_total` - Total number of invocation requests
  to the model
- `model_errors_total` - Total number of errors during model
  invocation
- `model_concurrent_requests` - Active concurrent requests per
  model
- `model_latency_milliseconds` - Model invocation latency in
  milliseconds
- `model_ttfb_milliseconds` - Model time to first byte latency in
  milliseconds

**Access model container metrics**

**What you need to know:**

- Model containers expose additional metrics specific to their serving
  framework
- These metrics provide internal container insights like token processing
  and queue depths
- Endpoint configuration varies by model container type

**For JumpStart model deployments using Text Generation
Inference (TGI) containers:**

- **Port:** 8080 (model container port)
- **Path:** /metrics
- **Documentation:**
  [https://huggingface.co/docs/text-generation-inference/en/reference/metrics](https://huggingface.co/docs/text-generation-inference/en/reference/metrics "https://huggingface.co/docs/text-generation-inference/en/reference/metrics")

**For JumpStart model deployments using Large Model Inference
(LMI) containers:**

- **Port:** 8080 (model container port)
- **Path:** /server/metrics
- **Documentation:**
  [https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md](https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md "https://github.com/deepjavalibrary/djl-serving/blob/master/prometheus/README.md")

**For custom inference endpoints (BYOD):**

- **Port:** Customer-configured (default 8080
  Defaults to the WorkerConfig.ModelInvocationPort.ContainerPort within the
  InferenceEndpointConfig spec.)
- **Path:** Customer-configured (default
  /metrics)

**Implement custom observability integration**

With a custom observability integration, you're responsible for:

1. **Metrics Scraping:** Implement
   Prometheus-compatible scraping from the endpoints above
2. **Data Export:** Configure export to your
   chosen observability platform
3. **Alerting:** Set up alerting rules based on
   your operational requirements
4. **Dashboards:** Create visualization
   dashboards for your monitoring needs

## Troubleshoot inference observability issues

**The dashboard shows no data**

If the Grafana dashboard is empty and all panels show "No data," perform the
following steps to investigate:

1. Verify Administrator has inference observability installed:
   1. Navigate to HyperPod Console > Select cluster > Check if
      "Observability" status shows "Enabled"
   2. Verify Grafana workspace link is accessible from cluster
      overview
   3. Confirm Amazon Managed Prometheus workspace is configured and
      receiving data

2. Verify HyperPod Observabilty is enabled:

```
hyp observability view
```

3. Verify model metrics are enabled:

```
kubectl get jumpstartmodel -n <namespace> customer-chat-llama -o jsonpath='{.status.metricsStatus}' # Expected: enabled: true, state:Enabled
```

```
kubectl get jumpstartmodel -n <namespace> customer-chat-llama -o jsonpath='{.status.metricsStatus}' # Expected: enabled: true, state:Enabled
```

4. Check the metrics endpoint:

```
kubectl port-forward pod/customer-chat-llama-xxx 9113:9113
curl localhost:9113/metrics | grep model_invocations_total# Expected: model_invocations_total{...} metrics
```

5. Check the logs:

```
# Model Container
kubectl logs customer-chat-llama-xxx -c customer-chat-llama# Look for: OOM errors, CUDA errors, model loading failures

# Proxy/SideCar
kubectl logs customer-chat-llama-xxx -c sidecar-reverse-proxy# Look for: DNS resolution issues, upstream connection failures

# Metrics Exporter Sidecar
kubectl logs customer-chat-llama-xxx -c otel-collector# Look for: Metrics collection issues, export failures
```

**Other common issues**

| Issue                                    | Solution                                            | Action                                          |
| ---------------------------------------- | --------------------------------------------------- | ----------------------------------------------- |
| Inference observability is not installed | Install inference observability through the console | "Enable Observability" in HyperPod console      |
| Metrics disabled in model                | Update model configuration                          | Add `metrics: {enabled: true}` to model spec    |
| AMP workspace not configured             | Fix data source connection                          | Verify AMP workspace ID in Grafana data sources |
| Network connectivity                     | Check security groups/NACLs                         | Ensure pods can reach AMP endpoints             |
