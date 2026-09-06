

# Configure add-on for third party monitoring tools
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party"></a>

You can configure the Network Flow Monitor add-on to expose an OpenMetrics server during installation. This enables integration with third-party monitoring tools such as Prometheus, allowing you to collect and analyze network flow metrics alongside your existing monitoring infrastructure. [Learn more about about OpenMetrics](https://openmetrics.io/). This feature is available from add-on version v1.1.0.

To enable the OpenMetrics server, add OPEN\_METRICS, OPEN\_METRICS\_ADDRESS, and OPEN\_METRICS\_PORT to the configuration values of the EKS Network Flow Monitor add-on. This guide will explain how to do this using both CLI and Console. See [Amazon EKS add-ons advanced configuration](https://aws.amazon.com/blogs/containers/amazon-eks-add-ons-advanced-configuration/) for additional details about adding configuration values.

## CLI Configuration
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-cli"></a>

When using AWS Command Line Interface, you can provide the configuration values as a parameter:

```
aws eks create-addon \
  --cluster-name my-cluster-name \
  --addon-name aws-network-flow-monitoring-agent \
  --addon-version v1.1.0-eksbuild.1 \
  --configuration-values '{"env":{"OPEN_METRICS":"on","OPEN_METRICS_ADDRESS":"0.0.0.0","OPEN_METRICS_PORT":9109}}'
```

## Console Configuration
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-console"></a>

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
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-parameters"></a>
+ **OPEN\_METRICS:**
  + Enable or disable open metrics. Disabled if not supplied
  + Type: String
  + Values: ["on", "off"]
+ **OPEN\_METRICS\_ADDRESS:**
  + Listening IP address for open metrics endpoint. Defaults to 127.0.0.1 if not supplied
  + Type: String
+ **OPEN\_METRICS\_PORT:**
  + Listening port for open metrics endpoint. Defaults to 80 if not supplied
  + Type: Integer
  + Range: [0..65535]

**Important:** When setting OPEN\_METRICS\_ADDRESS to 0.0.0.0, the metrics endpoint will be accessible from any network interface. Consider using 127.0.0.1 for localhost-only access or implement appropriate network security controls to restrict access to authorized monitoring systems only.

## Troubleshooting
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-troubleshooting"></a>

If you encounter issues with the OpenMetrics server configuration, use the following information to diagnose and resolve common problems.

### Metrics not displaying
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-troubleshooting-metrics-not-displaying"></a>

Problem: The OpenMetrics server is configured, but metrics are not appearing in your monitoring tool.

Troubleshooting Steps:

1. Verify that the OpenMetrics server is enabled in your add-on configuration:
   + Check that OPEN\_METRICS is set to "on" in your configuration values. See [describe-addon](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-addon.html).
   + Confirm that the add-on version is v1.1.0 or later in the *Configure selected add-ons settings*.

1. Test the metrics endpoint directly:
   + Access the metrics at http://{{pod-ip:port}}/metrics (replace pod-ip with the actual pod IP address and port with your configured port).
   + If you can't access the endpoint, verify your network configuration and security group settings.

1. Validate your monitoring tool configuration. Consult you monitoring tools user guide for details on how to do the following:
   + Make sure your monitoring tool (such as Prometheus) is configured to scrape the correct endpoint.
   + Check that the scraping interval and timeout settings are appropriate.
   + Verify that your monitoring tool has network access to the pod IP address.

### Metrics missing from specific pods
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-troubleshooting-metrics-missing-pods"></a>

Problem: Metrics are available from some pods but not others in your cluster.

Troubleshooting Steps:

The Network Flow Monitor add-on doesn't support pods that use hostNetwork: true. If your pod specification includes this setting, metrics won't be available from those pods.

Workaround: Remove the hostNetwork: true setting from your pod specification if possible. If you require host networking for your application, consider using alternative monitoring approaches for those specific pods.

### Connection refused errors
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-troubleshooting-connection-refused"></a>

Problem: You receive "connection refused" errors when trying to access the metrics endpoint.

Troubleshooting Steps:

1. Verify the OPEN\_METRICS\_ADDRESS configuration:
   + If set to 127.0.0.1, the endpoint is only accessible from within the pod.
   + If set to 0.0.0.0, the endpoint should be accessible from other pods in the cluster.
   + Make sure your monitoring tool can reach the configured address.

1. Check the OPEN\_METRICS\_PORT configuration:
   + Verify that the port number is not already in use by another service.
   + Make sure the port is within the valid range (1-65535).
   + Confirm that any security groups or network policies allow traffic on this port.

### Verification steps
<a name="CloudWatch-NetworkFlowMonitor-agents-kubernetes-eks-third-party-troubleshooting-verification"></a>

To confirm your OpenMetrics configuration is working correctly:

1. Check the add-on status:

   ```
   aws eks describe-addon --cluster-name {{your-cluster-name}} --addon-name aws-network-flow-monitoring-agent
   ```

1. Verify pod status:

   ```
   kubectl get pods app.kubernetes.io/name=aws-network-flow-monitoring-agent
   ```

1. Test the metrics endpoint from within the cluster:

   ```
   kubectl exec {{add-on-pod-name}} -- curl localhost:{{9109}}/metrics
   ```

   Replace 9109 with your configured port number, and the pod name with an AddOn pod name.