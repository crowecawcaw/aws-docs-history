

# Standard telemetry attributes

The CloudWatch agent adds the same set of resource attributes, which follow the OpenTelemetry semantic conventions for Kubernetes, host, and cloud, to the OpenTelemetry telemetry that the Amazon CloudWatch Observability add-on and Helm chart collect. Because every product uses the same attributes, you can correlate the metrics, traces, and logs of a pod across products in one query.

The attributes apply to the following products:
+ [OTel Container Insights (Recommended)](container-insights-eks-otel.md) metrics and logs
+ Telemetry that your applications send to the [OTLP ingestion](eks-observability-addon-otlp-endpoint.md) endpoint

They don't apply to metrics from [Scraping ServiceMonitor and PodMonitor targets](eks-observability-addon-prometheus-monitors.md), or to Enhanced Container Insights (Classic) and Application Signals (Classic), which send classic CloudWatch metrics.

The agent adds the following attributes.

`k8s.cluster.name`, `k8s.namespace.name`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `k8s.node.name`  
The cluster, namespace, pod, container, and node that the telemetry comes from.

`k8s.workload.name`, `k8s.workload.type`  
The workload that owns the pod, such as a Deployment or a StatefulSet.

`k8s.pod.label.*`, `k8s.node.label.*`  
The labels of the pod and the node. The `otelFilters.podLabels` and `otelFilters.nodeLabels` settings decide which labels are added. For more information, see [Telemetry filters](eks-observability-addon-telemetry-filters.md).

Cloud and host attributes, such as `cloud.region`, `cloud.availability_zone`, and `host.type`  
The Region, Availability Zone, and instance of the node.

`cloud.resource_id`  
The resource ID of the cluster.

`service.name`, `service.namespace`, `service.version`, `service.instance.id`, `deployment.environment.name`  
The service identity of the pod. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).

For OTLP telemetry, the agent sets the service identity attributes only when the sender didn't set them. Each OTel Container Insights metric carries at most 150 labels.