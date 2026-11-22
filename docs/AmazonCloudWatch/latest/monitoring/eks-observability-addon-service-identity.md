

# OpenTelemetry service identity

The CloudWatch agent sets `service.name`, `service.namespace`, `service.version`, and `service.instance.id` the same way on all the OpenTelemetry telemetry that it collects from a pod. So one service has one name across its OTLP metrics, traces, and logs, its OTel Container Insights metrics and kube-state-metrics series, its ServiceMonitor and PodMonitor metrics, and its application logs. You can then find all the telemetry of a service by its name.

Service identity is always on, and is available in version 8.0.0 and later of the Amazon CloudWatch Observability Amazon EKS add-on and Helm chart. The agent sets each attribute only when the sender didn't set it.

## How the attributes are set
<a name="eks-observability-addon-service-identity-sources"></a>

The agent follows the [OpenTelemetry Kubernetes attributes convention](https://opentelemetry.io/docs/specs/semconv/non-normative/k8s-attributes/). For each attribute, it uses the first value that it finds in the following list.

`service.name`  
The value that the sender set. Then the `resource.opentelemetry.io/service.name` pod annotation. Then the name of the Deployment, ReplicaSet, StatefulSet, DaemonSet, CronJob, or Job, or the pod or container name. A value that starts with `unknown_service`, the SDK default, counts as not set.

`service.namespace`  
The `resource.opentelemetry.io/service.namespace` pod annotation. Then the Kubernetes namespace.

`service.version`  
The `resource.opentelemetry.io/service.version` pod annotation.

`service.instance.id`  
The `resource.opentelemetry.io/service.instance.id` pod annotation. Then `{{namespace}}.{{pod}}.{{container}}`.

`deployment.environment.name`  
`{{cloud.platform}}:{{cluster}}/{{namespace}}`

To give a service a name of your choice, set the `resource.opentelemetry.io/service.name` annotation in the pod template of its workload, for example:

```yaml
spec:
  template:
    metadata:
      annotations:
        resource.opentelemetry.io/service.name: checkout
```

On KServe pods, the InferenceService name comes after the annotation. Series about the agent's own scrape targets, such as node-exporter series and the series of control-plane components like the Kubernetes API server and Karpenter, keep the scrape job name as `service.name`, because they describe those components and not your services. Host logs carry no service identity.

## Using the app.kubernetes.io labels
<a name="eks-observability-addon-service-identity-app-labels"></a>

The OpenTelemetry convention also lists the well-known `app.kubernetes.io/instance`, `app.kubernetes.io/name`, and `app.kubernetes.io/version` pod labels as sources. It asks for an opt-in flag, because you might not know that your labels are used this way. The `otelServiceIdentity.useAppLabels` value is that flag, and it is `false` by default.

When you turn it on, the agent uses `app.kubernetes.io/instance` and then `app.kubernetes.io/name` for `service.name`, after the annotation. It uses `app.kubernetes.io/version` for `service.version`, after the annotation.

**Note**  
All the pods of one Helm release usually share the same `app.kubernetes.io/instance` label. With `useAppLabels` on, they then share one `service.name`.

The following add-on configuration turns it on:

```json
{
  "otelServiceIdentity": {
    "useAppLabels": true
  }
}
```