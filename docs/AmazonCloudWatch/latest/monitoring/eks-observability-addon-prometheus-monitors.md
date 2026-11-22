

# Scraping ServiceMonitor and PodMonitor targets

If you already describe your Prometheus scrape targets with prometheus-operator ServiceMonitor and PodMonitor objects (`monitoring.coreos.com/v1`), the CloudWatch agent can scrape the same targets and send the metrics to CloudWatch over OTLP. You don't have to rewrite your scrape configuration. You query the metrics with PromQL.

Scraping is on by default, and is available in version 8.0.0 and later of the Amazon CloudWatch Observability Amazon EKS add-on and Helm chart. It works with or without OTel Container Insights.

## How scraping works
<a name="eks-observability-addon-prometheus-monitors-how"></a>
+ The CloudWatch agent on each node scrapes the targets on its own node. To have the cluster-level CloudWatch agent scrape the targets of a monitor instead, add the annotation `cloudwatch.aws.amazon.com/scraper: cluster-scraper` to the monitor's metadata.
+ By default, the agent scrapes every ServiceMonitor and PodMonitor in the cluster, every 30 seconds.
+ The metrics carry the resource attribute `cloudwatch.solution` with the value `k8s-otel-prometheus-monitors`, the Kubernetes attributes of the scraped pod, and the service identity attributes. For more information, see [OpenTelemetry service identity](eks-observability-addon-service-identity.md).
+ The agent keeps the `up` metric for every target, so `up == 0` shows a target that fails to scrape.
+ The metrics always go to the regional CloudWatch endpoint.

The add-on and the chart don't install the ServiceMonitor and PodMonitor custom resource definitions (CRDs). The CloudWatch agent operator creates both CRDs only if they don't exist, and leaves a copy that prometheus-operator, kube-prometheus-stack, or another tool installed unchanged.

## Configuring scraping
<a name="eks-observability-addon-prometheus-monitors-configure"></a>

The following configuration values control scraping.


| Value | Default | Description | 
| --- | --- | --- | 
| otelPrometheusMonitor.enabled | true | Turns scraping on or off. | 
| otelPrometheusMonitor.scrapeInterval | 30s | How often the targets are scraped, in the format {{N}}s. | 
| otelPrometheusMonitor.serviceMonitorSelector | Empty | A Kubernetes label selector (matchLabels, matchExpressions, or both) that chooses which ServiceMonitors are scraped. Empty selects every ServiceMonitor. | 
| otelPrometheusMonitor.podMonitorSelector | Empty | A label selector that chooses which PodMonitors are scraped. Empty selects every PodMonitor. | 
| otelPrometheusMonitor.readSecrets | false | Lets the agent read the Secrets that monitors reference for basicAuth, authorization, oauth2, and tlsConfig. | 

Use the selectors to leave some monitors to your own Prometheus. The following add-on configuration scrapes only the ServiceMonitors with the label `cloudwatch: "true"` and the PodMonitors whose `team` label is `payments` or `checkout`, every 60 seconds. It also lets the agent read the Secrets that those monitors reference.

```json
{
  "otelPrometheusMonitor": {
    "readSecrets": true,
    "scrapeInterval": "60s",
    "serviceMonitorSelector": {
      "matchLabels": {
        "cloudwatch": "true"
      }
    },
    "podMonitorSelector": {
      "matchExpressions": [
        {
          "key": "team",
          "operator": "In",
          "values": [
            "payments",
            "checkout"
          ]
        }
      ]
    }
  }
}
```

The following configuration turns scraping off:

```json
{
  "otelPrometheusMonitor": {
    "enabled": false
  }
}
```

**Important**  
`readSecrets` grants the Target Allocator component of the agent `get` permission on Secrets in every namespace. It reads each Secret by the name in the monitor, and sends the credentials to the agents only over mutual TLS. It picks up a rotated Secret within about 5 minutes. Without `readSecrets`, monitors that need credentials scrape without them: the target rejects the scrape, and no metrics reach CloudWatch for that monitor.

## Example: a ServiceMonitor and a PodMonitor
<a name="eks-observability-addon-prometheus-monitors-example"></a>

In this example, an application `orders` in the namespace `shop` exposes Prometheus metrics on a container port named `metrics` (port 8080, path `/metrics`), behind a Service with the label `app: orders`.

A ServiceMonitor scrapes the pods behind a Service. It selects the Service by its labels, and names the Service port:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: orders
  namespace: shop
  labels:
    cloudwatch: "true"
spec:
  selector:
    matchLabels:
      app: orders
  endpoints:
    - port: metrics
      path: /metrics
```

A PodMonitor scrapes pods directly, without a Service. It selects the pods by their labels, and names the container port:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: orders
  namespace: shop
  labels:
    team: payments
spec:
  selector:
    matchLabels:
      app: orders
  podMetricsEndpoints:
    - port: metrics
      path: /metrics
```

Use one or the other for the same pods. With both, every pod is scraped twice and sends duplicate series.

With the default configuration, the agent scrapes both monitors, because empty selectors select every monitor. With the selector example in the previous section, it also scrapes both: the ServiceMonitor has the label `cloudwatch: "true"`, and the PodMonitor's `team` label is `payments`.

## Uninstalling
<a name="eks-observability-addon-prometheus-monitors-uninstall"></a>

The CloudWatch agent operator never deletes the ServiceMonitor and PodMonitor CRDs. When you uninstall the add-on or the chart, the CRDs and every ServiceMonitor and PodMonitor stay in the cluster. To remove the CRDs after you uninstall, run the following command.

**Warning**  
Deleting the CRDs also deletes every ServiceMonitor and PodMonitor in the cluster, including the ones that another Prometheus uses.

```bash
kubectl delete crd servicemonitors.monitoring.coreos.com podmonitors.monitoring.coreos.com
```