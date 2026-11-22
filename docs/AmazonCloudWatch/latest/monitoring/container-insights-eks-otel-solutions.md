

# Solutions

With Solutions, you can get pre-built observability for third-party Kubernetes tools that run on your Amazon EKS clusters. Each solution collects metrics from a specific tool and surfaces them in a dedicated dashboard within Container Insights.

When you enable OTel Container Insights, every solution is on by default. If your cluster doesn't run a tool, its solution finds no targets and sends nothing. To turn off one solution, set its `enabled` value to `false`. To turn off all OTel Container Insights solutions at once, set `otelContainerInsights.solutions.enabled` to `false`. The following list gives the configuration value of each solution.

Karpenter  
`otelContainerInsights.solutions.karpenter.enabled`

KEDA  
`otelContainerInsights.solutions.keda.enabled`

vLLM  
`otelContainerInsights.solutions.vllm.enabled`

SGLang (version 8.0.0 and later)  
`otelContainerInsights.solutions.sglang.enabled`

Ray (version 8.0.0 and later)  
`otelContainerInsights.solutions.ray.enabled`

KServe control plane  
`otelContainerInsights.solutions.kserve.controlPlane.enabled`

Knative Serving  
`otelContainerInsights.solutions.knative.dataPlane.enabled` and `otelContainerInsights.solutions.knative.controlPlane.enabled`

The vLLM and SGLang solutions collect the inference engine metrics, such as `vllm:num_requests_running` and `sglang:num_running_reqs`, that uses to identify inference workloads. For more information, see [Accelerated Compute Insights](Accelerated-Compute-Insights.md).

**Topics**
+ [Collecting Karpenter metrics with OTel Container Insights](container-insights-eks-otel-karpenter.md)
+ [Collecting KEDA metrics with OTel Container Insights](container-insights-eks-otel-keda.md)
+ [Collecting vLLM metrics with OTel Container Insights](container-insights-eks-otel-vllm.md)
+ [Collecting SGLang metrics with OTel Container Insights](container-insights-eks-otel-sglang.md)
+ [Collecting Ray metrics with OTel Container Insights](container-insights-eks-otel-ray.md)
+ [Collecting KServe metrics with OTel Container Insights](container-insights-eks-otel-kserve.md)
+ [Collecting Knative Serving metrics with OTel Container Insights](container-insights-eks-otel-knative.md)