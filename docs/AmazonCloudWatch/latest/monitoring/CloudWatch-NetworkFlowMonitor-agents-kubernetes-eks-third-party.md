# Configure add-on for third party monitoring tools

You can configure the Network Flow Monitor add-on to expose an OpenMetrics server during installation. This enables integration with third-party monitoring tools such as Prometheus, allowing you to collect and analyze network flow metrics alongside your existing monitoring infrastructure. [Learn more about about OpenMetrics](https://openmetrics.io/ "https://openmetrics.io/"). This feature is available from add-on version v1.1.0.

To enable the OpenMetrics server, add OPEN_METRICS, OPEN_METRICS_ADDRESS, and OPEN_METRICS_PORT to the configuration values of the EKS Network Flow Monitor add-on. This guide will explain how to do this using both CLI and Console. See [Amazon EKS add-ons advanced configuration](https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/ "https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/") for additional details about adding configuration values.

## CLI Configuration

When using AWS Command Line Interface, you can provide the configuration values as a parameter:

```
aws eks create-addon \
  --cluster-name my-cluster-name \
  --addon-name aws-network-flow-monitoring-agent \
  --addon-version v1.1.0-eksbuild.1 \
  --configuration-values '{"env":{"OPEN_METRICS":"on","OPEN_METRICS_ADDRESS":"0.0.0.0","OPEN_METRICS_PORT":9109}}'
```

## Console Configuration

When using the Amazon EKS Console, these values can be added under Optional configuration settings, as part of the Configuration values.

**Sample JSON:**

```
{
    "env": {
        "OPEN_METRICS": "on",
        "OPEN_METRICS_ADDRESS": "0.0.0.0",
        "OPEN_METRICS_PORT": 9109
    }
}
```

**Sample YAML:**

```
env:
  OPEN_METRICS: "on"
  OPEN_METRICS_ADDRESS: "0.0.0.0"
  OPEN_METRICS_PORT: 9109
```

## EKS Network Flow Monitor add-on OpenMetric Parameters

- **OPEN_METRICS:**
  - Enable or disable open metrics. Disabled if not supplied
  - Type: String
  - Values: ["on", "off"]

- **OPEN_METRICS_ADDRESS:**
  - Listening IP address for open metrics endpoint. Defaults to 127.0.0.1 if not supplied
  - Type: String

- **OPEN_METRICS_PORT:**
  - Listening port for open metrics endpoint. Defaults to 80 if not supplied
  - Type: Integer
  - Range: [0..65535]

**Important:** When setting OPEN_METRICS_ADDRESS to 0.0.0.0, the metrics endpoint will be accessible from any network interface. Consider using 127.0.0.1 for localhost-only access or implement appropriate network security controls to restrict access to authorized monitoring systems only.

## Troubleshooting

If you encounter issues with the OpenMetrics server configuration, use the following information to diagnose and resolve common problems.

### Metrics not displaying

Problem: The OpenMetrics server is configured, but metrics are not appearing in your monitoring tool.

Troubleshooting Steps:

1. Verify that the OpenMetrics server is enabled in your add-on configuration:
   - Check that OPEN_METRICS is set to "on" in your configuration values. See [describe-addon](../../../cli/latest/reference/eks/describe-addon.md "../../../cli/latest/reference/eks/describe-addon.md").
   - Confirm that the add-on version is v1.1.0 or later in the _Configure selected add-ons settings_.

2. Test the metrics endpoint directly:
   - Access the metrics at http://`pod-ip:port`/metrics (replace pod-ip with the actual pod IP address and port with your configured port).
   - If you can't access the endpoint, verify your network configuration and security group settings.

3. Validate your monitoring tool configuration. Consult you monitoring tools user guide for details on how to do the following:
   - Ensure your monitoring tool (such as Prometheus) is configured to scrape the correct endpoint.
   - Check that the scraping interval and timeout settings are appropriate.
   - Verify that your monitoring tool has network access to the pod IP address.

### Metrics missing from specific pods

Problem: Metrics are available from some pods but not others in your cluster.

Troubleshooting Steps:

The Network Flow Monitor add-on doesn't support pods that use hostNetwork: true. If your pod specification includes this setting, metrics won't be available from those pods.

Workaround: Remove the hostNetwork: true setting from your pod specification if possible. If you require host networking for your application, consider using alternative monitoring approaches for those specific pods.

### Connection refused errors

Problem: You receive "connection refused" errors when trying to access the metrics endpoint.

Troubleshooting Steps:

1. Verify the OPEN_METRICS_ADDRESS configuration:
   - If set to 127.0.0.1, the endpoint is only accessible from within the pod.
   - If set to 0.0.0.0, the endpoint should be accessible from other pods in the cluster.
   - Ensure your monitoring tool can reach the configured address.

2. Check the OPEN_METRICS_PORT configuration:
   - Verify that the port number is not already in use by another service.
   - Ensure the port is within the valid range (1-65535).
   - Confirm that any security groups or network policies allow traffic on this port.

### Verification steps

To confirm your OpenMetrics configuration is working correctly:

1. Check the add-on status:

```
aws eks describe-addon --cluster-name `your-cluster-name` --addon-name aws-network-flow-monitoring-agent
```

2. Verify pod status:

```
kubectl get pods app.kubernetes.io/name=aws-network-flow-monitoring-agent
```

3. Test the metrics endpoint from within the cluster:

```
kubectl exec `add-on-pod-name` -- curl localhost:`9109`/metrics
```

Replace 9109 with your configured port number, and the pod name with an AddOn pod name.
